#!/usr/bin/env python3
"""Collect WeChat interaction metrics without exposing the user's API key."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from configure import default_config_path, initialize, load_json, resolve_api_key


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
        headers={"Content-Type": "application/json", "User-Agent": "yuanjiemi-wechat-review/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            parsed = json.loads(exc.read().decode("utf-8", errors="replace"))
            detail = str(parsed.get("msg") or parsed.get("detail") or parsed.get("error") or "")
        except (OSError, ValueError, json.JSONDecodeError):
            pass
        secret = str(payload.get("key") or "")
        if secret:
            detail = detail.replace(secret, "[REDACTED]")
        raise CollectionError(f"世界树接口 HTTP {exc.code}{'：' + detail if detail else ''}") from exc
    except urllib.error.URLError as exc:
        raise CollectionError(f"无法连接世界树接口：{exc.reason}") from exc
    try:
        result = json.loads(body)
    except json.JSONDecodeError as exc:
        raise CollectionError("世界树接口返回了无法解析的数据") from exc
    if result.get("code") != 200:
        message = str(result.get("msg") or result.get("error") or "未知错误")
        secret = str(payload.get("key") or "")
        if secret:
            message = message.replace(secret, "[REDACTED]")
        raise CollectionError(f"世界树接口失败：{message}")
    data = result.get("data")
    if not isinstance(data, dict):
        raise CollectionError("世界树接口没有返回有效 data")
    return data


def unwrap(data: dict) -> dict:
    current = data
    known = {"read_num", "readNum", "old_like_num", "like_num", "share_num", "title", "content"}
    while not known.intersection(current) and isinstance(current.get("data"), dict):
        current = current["data"]
    return current


def metric_number(value: Any) -> int | float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        number = float(value)
    else:
        text = str(value).strip().replace(",", "")
        multiplier = 10000 if text.endswith("万") else 1
        if multiplier != 1:
            text = text[:-1]
        try:
            number = float(text) * multiplier
        except ValueError:
            return None
    return int(number) if number.is_integer() else round(number, 2)


def first_metric(data: dict, *names: str) -> int | float | None:
    for name in names:
        value = metric_number(data.get(name))
        if value is not None:
            return value
    return None


def normalize_metrics(raw: dict) -> dict:
    data = unwrap(raw)
    read = first_metric(data, "read_num", "readNum", "read", "read_count")
    like = first_metric(data, "old_like_num", "oldLikeNum", "thumb_num", "thumbNum")
    share = first_metric(data, "share_num", "shareNum", "share", "forward_num", "forwardNum")
    heart = first_metric(data, "like_num", "likeNum", "heart_num", "heartNum", "looking_num")
    available = [value for value in (like, share, heart) if value is not None]
    total = sum(available) if available else None
    rate = round(total / read, 6) if total is not None and read not in (None, 0) else None
    if all(value is None for value in (read, like, share, heart)):
        raise CollectionError("互动接口没有返回可识别的阅读或互动数据")
    return {
        "read_count": read,
        "like_count": like,
        "share_count": share,
        "heart_count": heart,
        "total_interactions": total,
        "interaction_rate": rate,
    }


def normalize_detail(raw: dict, url: str) -> dict:
    data = unwrap(raw)
    title = str(data.get("title") or "").replace("\\n", "\n").strip()
    content = str(data.get("content") or "").replace("\\n", "\n").strip()
    if not content and ("\n" in title or len(title) > 180):
        content = title
        title = next((line.strip() for line in content.splitlines() if line.strip()), "")[:120]
    return {
        "title": title,
        "account_name": str(data.get("author") or "").strip(),
        "published_at": data.get("send_time") or data.get("publish_time") or "",
        "url": url,
        "content": content,
        "word_count": len(content),
    }


def output_path(config: dict, override: Path | None) -> Path:
    if override:
        return override.expanduser().resolve()
    raw_dir = config.get("collection", {}).get("output_dir", "outputs/wechat-performance-review")
    root = Path(str(raw_dir)).expanduser()
    if not root.is_absolute():
        root = Path.cwd() / root
    return (root / f"wechat-metrics-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json").resolve()


def collect(args: argparse.Namespace) -> Path:
    config_path = (args.config or default_config_path()).expanduser().resolve()
    if not config_path.exists():
        initialize(config_path)
    config = load_json(config_path)
    api_key, _ = resolve_api_key(config_path)
    if not api_key:
        raise CollectionError(f"世界树 API Key 尚未配置：{config_path}")
    worldtree = config.get("worldtree", {})
    base_url = str(worldtree.get("base_url") or "https://www.worldtreetech.cn/api/v2")
    timeout = int(config.get("collection", {}).get("request_timeout_seconds", 30))

    records = []
    for url in args.url:
        payload = {"key": api_key, "link": url, "need_comment": False}
        interaction = api_post(base_url, "wechat/article/getInteraction", payload, timeout)
        detail = api_post(base_url, "wechat/article/getDetail", {"key": api_key, "link": url}, timeout)
        records.append({
            **normalize_detail(detail, url),
            **normalize_metrics(interaction),
            "review_phase": args.phase,
            "reviewed_at": datetime.now(timezone.utc).isoformat(),
            "data_source": "世界树 API",
        })

    target = output_path(config, args.output)
    save_json_atomic(target, {
        "schema_version": "1.0.0",
        "record_count": len(records),
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "records": records,
    })
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="采集公众号文章互动数据")
    parser.add_argument("--url", action="append", required=True, help="可重复传入多篇公众号文章链接")
    parser.add_argument("--phase", default="手动复盘", choices=["第3天", "第7天", "第30天", "手动复盘"])
    parser.add_argument("--config", type=Path)
    parser.add_argument("--output", type=Path)
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
