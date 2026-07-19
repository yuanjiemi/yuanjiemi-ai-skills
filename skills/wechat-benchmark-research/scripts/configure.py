#!/usr/bin/env python3
"""Create and validate the private configuration for the WeChat benchmark skill."""

from __future__ import annotations

import argparse
import json
import os
import stat
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = SKILL_DIR / "assets" / "config.example.json"
OFFICIAL_WEBSITE = "https://www.worldtreetech.cn/"
API_DOCS = "https://s.apifox.cn/2592d2ef-25b9-4e40-b92b-c1484ee35b14"


def default_config_path() -> Path:
    override = os.environ.get("YUANJIEMI_WECHAT_CONFIG")
    if override:
        return Path(override).expanduser()
    if os.name == "nt" and os.environ.get("APPDATA"):
        root = Path(os.environ["APPDATA"])
    else:
        root = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    return root / "yuanjiemi-ai-skills" / "wechat-benchmark-research" / "config.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("配置文件根节点必须是 JSON 对象")
    return data


def initialize(path: Path) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    data = load_json(TEMPLATE_PATH)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if os.name != "nt":
        path.chmod(stat.S_IRUSR | stat.S_IWUSR)
    return True


def check(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "配置文件尚未创建"
    try:
        data = load_json(path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return False, f"配置文件无法读取：{exc}"
    api_key = (
        os.environ.get("WORLD_TREE_API_KEY")
        or os.environ.get("WORLDTREE_API_KEY")
        or data.get("worldtree", {}).get("api_key", "")
    )
    if not isinstance(api_key, str) or not api_key.strip():
        return False, "世界树 API Key 尚未配置"
    count = data.get("collection", {}).get("latest_count", 3)
    if not isinstance(count, int) or count < 1 or count > 20:
        return False, "collection.latest_count 必须是 1 到 20 的整数"
    return True, f"配置有效；默认采集 {count} 篇；API Key 已设置（不会显示）"


def print_guide(path: Path) -> None:
    print("\n世界树 API 申请与配置：")
    print("1. 账号采集使用你自己的世界树 API Key；公开 Skill 不包含元子的 Key。")
    print(f"2. 打开世界树官网联系服务方申请，并先确认当前额度与计费规则：{OFFICIAL_WEBSITE}")
    print(f"   接口文档：{API_DOCS}")
    print(f"3. 拿到 Key 后，只在本机打开配置文件并填入 worldtree.api_key：{path}")
    print("4. 不要把 Key 发到聊天框、截图或 GitHub。保存后让智能体再次检查配置。")
    print("5. 暂时不申请 Key 也没关系：发送单篇文章正文、截图或可访问链接，仍可免费拆解并写入 Excel。")


def import_env_file(config_path: Path, env_path: Path) -> None:
    api_key = ""
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        if name.strip() in {"WORLD_TREE_API_KEY", "WORLDTREE_API_KEY"}:
            api_key = value.strip().strip('"\'')
            break
    if not api_key:
        raise ValueError("指定文件中没有 WORLD_TREE_API_KEY 或 WORLDTREE_API_KEY")
    initialize(config_path)
    data = load_json(config_path)
    data.setdefault("worldtree", {})["api_key"] = api_key
    config_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if os.name != "nt":
        config_path.chmod(stat.S_IRUSR | stat.S_IWUSR)


def main() -> int:
    parser = argparse.ArgumentParser(description="配置公众号对标文章采集与分析 Skill")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--init", action="store_true", help="创建私有配置文件")
    action.add_argument("--check", action="store_true", help="检查私有配置文件")
    action.add_argument("--show-path", action="store_true", help="仅显示配置文件位置")
    action.add_argument("--guide", action="store_true", help="显示世界树 API 申请与安全配置指引")
    action.add_argument("--import-env-file", type=Path, help="从已有 .env 安全迁移世界树 Key")
    parser.add_argument("--config", type=Path, help="覆盖默认配置文件位置")
    args = parser.parse_args()
    path = (args.config or default_config_path()).expanduser().resolve()

    if args.show_path:
        print(path)
        return 0
    if args.guide:
        print_guide(path)
        return 0
    if args.init:
        created = initialize(path)
        print(f"{'已创建' if created else '配置已存在'}：{path}")
        ok, _ = check(path)
        if not ok:
            print_guide(path)
        return 0
    if args.import_env_file:
        try:
            import_env_file(path, args.import_env_file.expanduser().resolve())
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(f"迁移失败：{exc}", file=sys.stderr)
            return 2
        print(f"已将世界树 Key 写入私有配置（Key 不会显示）：{path}")
        return 0

    ok, message = check(path)
    print(message)
    print(f"配置位置：{path}")
    if not ok:
        print_guide(path)
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
