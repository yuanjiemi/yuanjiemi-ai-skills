#!/usr/bin/env python3
"""Create and validate private WorldTree configuration for review tasks."""

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


def config_root() -> Path:
    if os.name == "nt" and os.environ.get("APPDATA"):
        return Path(os.environ["APPDATA"])
    return Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))


def default_config_path() -> Path:
    override = os.environ.get("YUANJIEMI_WECHAT_REVIEW_CONFIG")
    if override:
        return Path(override).expanduser()
    return config_root() / "yuanjiemi-ai-skills" / "wechat-performance-review" / "config.json"


def benchmark_config_path() -> Path:
    return config_root() / "yuanjiemi-ai-skills" / "wechat-benchmark-research" / "config.json"


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
    path.write_text(TEMPLATE_PATH.read_text(encoding="utf-8"), encoding="utf-8")
    if os.name != "nt":
        path.chmod(stat.S_IRUSR | stat.S_IWUSR)
    return True


def key_from_file(path: Path) -> str:
    if not path.exists():
        return ""
    data = load_json(path)
    value = data.get("worldtree", {}).get("api_key", "")
    return value.strip() if isinstance(value, str) else ""


def resolve_api_key(path: Path) -> tuple[str, str]:
    env_key = os.environ.get("WORLD_TREE_API_KEY") or os.environ.get("WORLDTREE_API_KEY") or ""
    if env_key.strip():
        return env_key.strip(), "环境变量"
    own = key_from_file(path)
    if own:
        return own, str(path)
    legacy = benchmark_config_path()
    reused = key_from_file(legacy)
    if reused:
        return reused, f"已复用对标分析 Skill 私有配置：{legacy}"
    return "", str(path)


def check(path: Path) -> tuple[bool, str]:
    try:
        api_key, source = resolve_api_key(path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return False, f"配置无法读取：{exc}"
    if not api_key:
        return False, "世界树 API Key 尚未配置"
    return True, f"配置有效；Key 来源：{source}；Key 不会显示"


def print_guide(path: Path) -> None:
    print("\n世界树 API 申请与配置：")
    print("1. 链接自动采集使用你自己的世界树 API Key；公开 Skill 不包含元子的 Key。")
    print(f"2. 打开世界树官网联系服务方申请并确认当前计费规则：{OFFICIAL_WEBSITE}")
    print(f"3. 只在本机配置文件的 worldtree.api_key 中填写：{path}")
    print("4. 不要把 Key 发到聊天框、截图、Excel 或 GitHub；保存后让智能体再次检查。")
    print("5. 已配置公众号对标分析 Skill 的用户可自动复用原私有 Key；不配置也可使用截图或表格免费复盘。")


def main() -> int:
    parser = argparse.ArgumentParser(description="配置公众号数据复盘 Skill")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--init", action="store_true")
    action.add_argument("--check", action="store_true")
    action.add_argument("--show-path", action="store_true")
    action.add_argument("--guide", action="store_true")
    parser.add_argument("--config", type=Path)
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
        ok, message = check(path)
        print(message)
        if not ok:
            print_guide(path)
        return 0
    ok, message = check(path)
    print(message)
    print(f"本 Skill 配置位置：{path}")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
