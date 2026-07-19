#!/usr/bin/env python3
"""Offline regression test for the collection pipeline."""

from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import collect_latest


def fake_api(_base_url: str, endpoint: str, payload: dict, _timeout: int) -> dict:
    if endpoint.endswith("getDetail"):
        link = payload["link"]
        index = int(link.rsplit("/", 1)[-1]) if link.rsplit("/", 1)[-1].isdigit() else 9
        if index == 1:
            return {
                "title": "这是纯文字文章的第一段。\\n\\n这是正文第二段，用来验证正文回退。",
                "content": "",
                "author": "测试公众号",
                "send_time": "2026-07-19 08:00",
                "username": "gh_test_account",
            }
        return {
            "title": f"测试文章{index}",
            "content": f"这是测试文章{index}的正文。开头提出问题，结尾邀请读者领取资料。",
            "author": "测试公众号",
            "send_time": f"2026-07-{20-index:02d} 08:00",
            "username": "gh_test_account",
        }
    if endpoint.endswith("getArticleList"):
        return {
            "content": [
                {
                    "url": f"https://mp.weixin.qq.com/s/{index}",
                    "title": f"测试文章{index}",
                    "post_time": 2000 - index,
                    "post_time_str": f"2026-07-{20-index:02d} 08:00",
                    "msg_status": 0,
                    "is_delete": 0,
                }
                for index in range(1, 6)
            ]
        }
    raise AssertionError(endpoint)


class CollectLatestTest(unittest.TestCase):
    def test_first_run_and_saved_account(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            config_path = root / "config.json"
            output_path = root / "result.json"
            config_path.write_text(
                json.dumps(
                    {
                        "worldtree": {"api_key": "test-key", "base_url": "https://example.invalid/api/v1"},
                        "collection": {"latest_count": 3, "request_timeout_seconds": 3, "output_dir": str(root)},
                        "accounts": {},
                    }
                ),
                encoding="utf-8",
            )
            args = argparse.Namespace(
                account="测试公众号",
                seed_url="https://mp.weixin.qq.com/s/9",
                count=None,
                config=config_path,
                output=output_path,
            )
            with patch("collect_latest.api_post", side_effect=fake_api):
                target = collect_latest.collect(args)
            result = json.loads(target.read_text(encoding="utf-8"))
            saved = json.loads(config_path.read_text(encoding="utf-8"))
            self.assertEqual(result["collected_count"], 3)
            self.assertEqual(len(result["articles"]), 3)
            self.assertEqual(result["articles"][0]["collection_status"], "ok")
            self.assertIn("正文第二段", result["articles"][0]["content"])
            self.assertNotIn("\\n", result["articles"][0]["title"])
            self.assertEqual(saved["accounts"]["测试公众号"]["username"], "gh_test_account")
            self.assertNotIn("api_key", json.dumps(result))


if __name__ == "__main__":
    unittest.main()
