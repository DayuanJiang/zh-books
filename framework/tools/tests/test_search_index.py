import json
import unittest

import search_index as search


class SearchIndexTests(unittest.TestCase):
    def test_english_heading_stays_searchable_under_the_chinese_title(self):
        chapter = {"units": [
            {"kind": "heading", "level": 1, "anchor": "title", "source": "# Title", "target": "# 标题"},
            {"kind": "paragraph", "source": "English paragraph.[^1]", "target": "中文段落。"},
            {"kind": "heading", "level": 2, "anchor": "sub", "source": "## Sub", "target": "## 小节"},
            {"kind": "list", "source": "- item", "target": "- 条目"},
            {"kind": "heading", "level": 4, "anchor": "deep", "source": "#### deep", "target": "#### 深"},
            {"kind": "code", "source": "```\ncode\n```", "target": None},
            {"kind": "paragraph", "source": "More.", "target": "更多。"},
        ]}
        self.assertEqual(list(search.sections(chapter)), [
            ("标题", "title", "Title\nEnglish paragraph.\n中文段落。"),
            ("小节", "sub", "Sub\n- item\n- 条目\n#### deep\n#### 深\nMore.\n更多。"),
        ])


if __name__ == "__main__":
    unittest.main()
