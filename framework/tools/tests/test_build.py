import json
from pathlib import Path
import shutil
import tempfile
import unittest

import build
import config as book_config
import new_book
import status

EN = "# Chapter One\n\nFirst paragraph.[^1]\n\n- a\n- b\n\nLast paragraph.\n\n[^1]: A note.\n"
ZH_DONE = "# 第一章\n\n第一段。[^1]\n\n- 甲\n- 乙\n\n最后一段。\n\n[^1]: 一条注释。\n"
ZH_HALF = "# 第二章\n\n第一段。\n"


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.root = Path(self.folder.name) / "fixture-book"
        new_book.create(self.root, "测试书", "Fixture Book", "Someone", "一句话简介")
        for name, zh in (("01-one.md", ZH_DONE), ("02-two.md", ZH_HALF)):
            (self.root / "en" / name).write_text(EN)
            (self.root / "zh-cn" / name).write_text(zh)
        config = book_config.load(self.root)
        config["chapters"] = [{"id": "ch01", "number": 1, "file": "01-one.md", "status": "done"},
                              {"id": "ch02", "number": 2, "file": "02-two.md", "status": "draft"}]
        book_config.save(self.root, config)
        # A real subset is not needed here: mark every character as covered.
        fonts = self.root / "assets" / "fonts"
        fonts.mkdir(parents=True)
        (fonts / "charset.txt").write_text("".join(map(chr, range(0x20, 0x10000))).encode("utf-8", "ignore").decode())
        self.out = Path(self.folder.name) / "out"

    def tearDown(self):
        self.folder.cleanup()

    def test_book_json_round_trips_with_one_line_per_chapter(self):
        text = (self.root / "book.json").read_text()
        self.assertIn('    {"id": "ch01", "number": 1, "file": "01-one.md", "status": "done"},\n', text)
        self.assertEqual(json.loads(text)["chapters"][1]["status"], "draft")

    def test_strict_build_publishes_finished_chapters_only(self):
        build.build(self.root, self.out, url="https://example.org/fixture-book/", repo="https://example.org/repo")
        manifest = json.loads((self.out / "assets/reader-manifest.json").read_text())
        self.assertEqual([c["id"] for c in manifest["chapters"]], ["ch01"])
        self.assertEqual((self.out / "_sidebar.md").read_text(), "- [第一章](zh-cn/01-one.md)\n")
        self.assertFalse((self.out / "zh-cn/02-two.md").exists())
        index = (self.out / "index.html").read_text()
        self.assertNotIn("{{", index)
        self.assertIn('"start": "/zh-cn/01-one"', index)
        self.assertIn('content="https://example.org/fixture-book/"', index)
        for name in ("assets/reader.js", "assets/reader.css", "assets/vendor/docsify.min.js", "assets/search-index.json"):
            self.assertTrue((self.out / name).exists(), name)

    def test_recap_is_added_to_the_chapter_and_the_search_index(self):
        (self.root / "recaps").mkdir()
        (self.root / "recaps" / "ch01.md").write_text("本章讲了一件事。\n\n- 第一条要点\n- 第二条要点\n")
        build.build(self.root, self.out)
        chapter = json.loads((self.out / "assets/reader-content/ch01.json").read_text())
        self.assertIn("<li>第一条要点</li>", chapter["recap"]["html"])
        index = json.loads((self.out / "assets/search-index.json").read_text())
        self.assertIn({"route": "/zh-cn/01-one", "chapter": "第一章", "title": "本章小结与要点", "anchor": "chapter-recap",
                       "text": "本章讲了一件事。 - 第一条要点 - 第二条要点"}, index)

    def test_draft_build_marks_untranslated_blocks(self):
        build.build(self.root, self.out, drafts=True)
        manifest = json.loads((self.out / "assets/reader-manifest.json").read_text())
        self.assertEqual([(c["id"], c.get("draft", False)) for c in manifest["chapters"]], [("ch01", False), ("ch02", True)])
        self.assertIn("第二章（草稿）", (self.out / "_sidebar.md").read_text())
        chapter = json.loads((self.out / "assets/reader-content/ch02.json").read_text())
        self.assertEqual([u["kind"] for u in chapter["units"] if u.get("pending")], ["list", "paragraph"])

    def test_a_finished_chapter_must_be_fully_translated(self):
        config = book_config.load(self.root)
        config["chapters"][1]["status"] = "done"
        book_config.save(self.root, config)
        with self.assertRaises(ValueError):
            build.build(self.root, self.out)

    def test_missing_font_characters_fail_the_strict_build(self):
        shutil.rmtree(self.root / "assets" / "fonts")
        with self.assertRaisesRegex(ValueError, "site.py fonts fixture-book"):
            build.build(self.root, self.out)
        build.build(self.root, self.out, drafts=True)  # drafts only warn

    def test_chapter_maps_can_be_required(self):
        config = book_config.load(self.root)
        config["chapterMaps"] = True
        book_config.save(self.root, config)
        with self.assertRaisesRegex(ValueError, "without an opening map"):
            build.build(self.root, self.out)

    def test_book_json_errors_are_reported(self):
        config = book_config.load(self.root)
        config["chapters"][0]["id"] = "one"
        book_config.save(self.root, config)
        with self.assertRaisesRegex(ValueError, "ids like ch01"):
            book_config.load(self.root)
        config["chapters"][0].update({"id": "ch01", "status": "finished"})
        book_config.save(self.root, config)
        with self.assertRaisesRegex(ValueError, "status must be one of"):
            book_config.load(self.root)

    def test_status_counts_translated_blocks(self):
        report = status.report(self.root)
        self.assertIn("| ch01 | done | 4/4 | 1/1 |", report)
        self.assertIn("| ch02 | draft | 2/4 | 0/1 |", report)
        self.assertIn("6/8 blocks translated", report)


if __name__ == "__main__":
    unittest.main()
