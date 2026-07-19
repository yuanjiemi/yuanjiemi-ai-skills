#!/usr/bin/env python3
"""Collect the latest WeChat articles with the user's WorldTree API key."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from configure import default_config_path, initialize, load_json


class CollectionError(RuntimeError):
    pass


def save_json_atomic(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temp_path = Path(handle.name)
    temp_path.replace(path)


def api_post(base_url: str, endpoint: str, payload: dict, timeout: int) -> dict:
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "yuanjiemi-wechat-benchmark/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            error_body = exc.read().decode("utf-8", errors="replace")
            parsed = json.loads(error_body)
            detail = str(parsed.get("msg") or parsed.get("detail") or parsed.get("error") or "")
        except (OSError, ValueError, json.JSONDecodeError):
            detail = ""
        secret = str(payload.get("key") or "")
        if secret:
            detail = detail.replace(secret, "[REDACTED]")
        suffix = f"：{detail}" if detail else ""
        raise CollectionError(f"世界树接口 HTTP {exc.code}{suffix}") from exc
    except urllib.error.URLError as exc:
        raise CollectionError(f"无法连接世界树接口：{exc.reason}") from exc
    try:
        result = json.loads(body)
    except json.JSONDecodeError as exc:
        raise CollectionError("世界树接口返回了无法解析的数据") from exc
    if result.get("code") != 200:
        message = result.get("msg") or result.get("error") or "未知错误"
        raise CollectionError(f"世界树接口失败：{message}")
    if not isinstance(result.get("data"), dict):
        raise CollectionError("世界树接口没有返回有效 data")
    return result["data"]


def normalize_account_entry(value: Any) -> dict | None:
    if isinstance(value, str) and value.strip():
        return {"username": value.strip()}
    if isinstance(value, dict) and isinstance(value.get("username"), str) and value["username"].strip():
        return value
    return None


def resolve_account(
    config: dict,
    account: str,
    seed_url: str | None,
    api_key: str,
    base_url: str,
    timeout: int,
) -> tuple[str, str, dict | None]:
    accounts = config.setdefault("accounts", {})
    saved = normalize_account_entry(accounts.get(account))
    if saved:
        return saved["username"], saved.get("oa_name", account), None
    if not seed_url:
        raise CollectionError(f"首次采集“{account}”需要提供该账号任意一篇文章链接（--seed-url）")
    detail = api_post(
        base_url,
        "wechat/article/getDetail",
        {"key": api_key, "link": seed_url},
        timeout,
    )
    username = str(detail.get("username") or "").strip()
    if not username:
        raise CollectionError("文章详情中没有可用于采集账号文章列表的 username")
    oa_name = str(detail.get("author") or account).strip() or account
    accounts[account] = {
        "username": username,
        "oa_name": oa_name,
        "seed_url": seed_url,
        "identified_at": datetime.now(timezone.utc).isoformat(),
    }
    return username, oa_name, detail


def select_latest(items: Any, count: int) -> list[dict]:
    if not isinstance(items, list):
        raise CollectionError("文章列表格式异常")
    valid = []
    for item in items:
        if not isinstance(item, dict) or not item.get("url"):
            continue
        if item.get("is_delete", item.get("is_deleted", 0)) not in (0, None):
            continue
        # v1 文档以 2 表示正常；当前 v2 实际响应以 0 表示正常。
        if item.get("msg_status", 0) in (6, 7, 104, 105, "6", "7", "104", "105"):
            continue
        valid.append(item)
    valid.sort(key=lambda item: int(item.get("post_time") or item.get("pre_post_time") or 0), reverse=True)
    return valid[:count]


def normalize_article(detail: dict, summary: dict, oa_name: str) -> dict:
    detail_title = str(detail.get("title") or "").replace("\\n", "\n").strip()
    summary_title = str(summary.get("title") or "").replace("\\n", "\n").strip()
    content = str(detail.get("content") or "").replace("\\n", "\n").strip()

    # 纯文字/小绿书式文章在 v2 中可能把整篇正文放进 title，content 为空。
    if not content and ("\n" in detail_title or len(detail_title) > 180):
        content = detail_title
        title = summary_title
        if not title or len(title) > 120:
            first_line = next((line.strip() for line in detail_title.splitlines() if line.strip()), "")
            title = first_line[:80] + ("…" if len(first_line) > 80 else "")
    else:
        title = detail_title or summary_title

    return {
        "title": title,
        "account_name": detail.get("author") or oa_name,
        "published_at": detail.get("send_time") or summary.get("post_time_str") or "",
        "url": str(summary["url"]),
        "cover_url": summary.get("cover_url") or summary.get("pic_cdn_url_235_1") or "",
        "digest": summary.get("digest") or "",
        "content": content,
        "word_count": len(content),
        "source": "世界树 API",
        "collection_status": "ok" if content else "empty_content",
    }


def output_path(config: dict, account: str, override: Path | None) -> Path:
    if override:
        return override.expanduser().resolve()
    raw_dir = config.get("collection", {}).get("output_dir", "outputs/wechat-benchmark-research")
    root = Path(str(raw_dir)).expanduser()
    if not root.is_absolute():
        root = Path.cwd() / root
    safe_account = "".join(char if char.isalnum() or char in "-_" else "-" for char in account).strip("-") or "account"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return (root / f"{safe_account}-latest-{timestamp}.json").resolve()


def collect(args: argparse.Namespace) -> Path:
    config_path = (args.config or default_config_path()).expanduser().resolve()
    if not config_path.exists():
        initialize(config_path)
        raise CollectionError(f"已创建配置文件，请先在本地填写世界树 API Key：{config_path}")
    config = load_json(config_path)
    worldtree = config.get("worldtree", {})
    api_key = (
        os.environ.get("WORLD_TREE_API_KEY")
        or os.environ.get("WORLDTREE_API_KEY")
        or worldtree.get("api_key")
        or ""
    ).strip()
    if not api_key:
        raise CollectionError(f"世界树 API Key 尚未配置：{config_path}")
    base_url = str(worldtree.get("base_url") or "https://www.worldtreetech.cn/api/v2")
    settings = config.get("collection", {})
    timeout = int(settings.get("request_timeout_seconds", 30))
    count = args.count or int(settings.get("latest_count", 3))
    if count < 1 or count > 20:
        raise CollectionError("采集篇数必须在 1 到 20 之间")

    username, oa_name, seed_detail = resolve_account(
        config, args.account, args.seed_url, api_key, base_url, timeout
    )
    list_data = api_post(
        base_url,
        "wechat/article/getArticleList",
        {"key": api_key, "username": username, "offset": ""},
        timeout,
    )
    summaries = select_latest(list_data.get("content"), count)
    if not summaries:
        raise CollectionError("没有找到状态正常的公众号文章")

    articles = []
    for summary in summaries:
        link = str(summary["url"])
        if seed_detail is not None and args.seed_url == link:
            detail = seed_detail
        else:
            detail = api_post(
                base_url,
                "wechat/article/getDetail",
                {"key": api_key, "link": link},
                timeout,
            )
        articles.append(normalize_article(detail, summary, oa_name))

    account_record = config["accounts"][args.account]
    if isinstance(account_record, dict):
        account_record["last_collected_at"] = datetime.now(timezone.utc).isoformat()
    save_json_atomic(config_path, config)

    target = output_path(config, args.account, args.output)
    result = {
        "schema_version": "1.0.0",
        "account_query": args.account,
        "account_name": oa_name,
        "username": username,
        "requested_count": count,
        "collected_count": len(articles),
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "articles": articles,
    }
    save_json_atomic(target, result)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="采集指定公众号最新文章")
    parser.add_argument("--account", required=True, help="用户可识别的公众号名称")
    parser.add_argument("--seed-url", help="新账号首次识别所需的任意一篇公众号文章链接")
    parser.add_argument("--count", type=int, help="覆盖配置中的默认采集篇数")
    parser.add_argument("--config", type=Path, help="覆盖默认配置路径")
    parser.add_argument("--output", type=Path, help="指定采集结果 JSON 文件")
    args = parser.parse_args()
    try:
        target = collect(args)
    except (CollectionError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"采集失败：{exc}", file=sys.stderr)
        return 2
    print(f"采集完成：{target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
