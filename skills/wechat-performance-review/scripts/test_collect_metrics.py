#!/usr/bin/env python3

import unittest

from collect_metrics import CollectionError, metric_number, normalize_detail, normalize_metrics


class MetricsTests(unittest.TestCase):
    def test_worldtree_fields(self):
        result = normalize_metrics({"read_num": 1000, "old_like_num": 20, "share_num": 5, "like_num": 10})
        self.assertEqual(result["total_interactions"], 35)
        self.assertEqual(result["interaction_rate"], 0.035)

    def test_nested_and_alias_fields(self):
        result = normalize_metrics({"data": {"readNum": "2,000", "oldLikeNum": "12", "shareNum": 3, "heartNum": 5}})
        self.assertEqual(result["read_count"], 2000)
        self.assertEqual(result["total_interactions"], 20)

    def test_missing_is_not_zero(self):
        result = normalize_metrics({"read_num": 100, "like_num": 4})
        self.assertIsNone(result["like_count"])
        self.assertEqual(result["heart_count"], 4)
        self.assertEqual(result["total_interactions"], 4)

    def test_chinese_ten_thousand(self):
        self.assertEqual(metric_number("1.2万"), 12000)

    def test_empty_metrics_fail(self):
        with self.assertRaises(CollectionError):
            normalize_metrics({"title": "无数据"})

    def test_text_article_detail(self):
        result = normalize_detail({"title": "第一行标题\n" + "正文" * 100, "content": ""}, "https://example.com")
        self.assertEqual(result["title"], "第一行标题")
        self.assertGreater(result["word_count"], 180)


if __name__ == "__main__":
    unittest.main()
