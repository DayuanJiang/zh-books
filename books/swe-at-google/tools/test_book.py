"""Checks specific to this book, on top of the framework's own build checks.

Run from the repository root: uv run --project framework/tools --with pytest pytest -q books/swe-at-google/tools
"""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))

import build  # noqa: E402
import fonts  # noqa: E402

# Code examples in these languages each need a Python rewrite or a written reason (assets/code-variants/).
TRANSLATED = {"java", "Java", "C++", "golang"}


class BookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder = tempfile.TemporaryDirectory()
        cls.out = Path(cls.folder.name)
        build.build(BOOK, cls.out)
        cls.manifest = json.loads((cls.out / "assets/reader-manifest.json").read_text())

    @classmethod
    def tearDownClass(cls):
        cls.folder.cleanup()

    def test_whole_book_is_published_with_chapter_maps(self):
        self.assertEqual(len(self.manifest["chapters"]), 28)
        self.assertEqual(len(self.manifest["guides"]), 25)
        self.assertFalse([c["id"] for c in self.manifest["chapters"] if c.get("draft")])
        for number in range(1, 26):
            self.assertTrue(self.manifest["guides"][f"ch{number:02d}"]["storyTitle"])

    def test_existing_book_text_is_byte_identical_to_translation_commit(self):
        for folder in ("en", "zh-cn"):
            for path in (BOOK / folder).rglob("*.md"):
                relative = path.relative_to(BOOK).as_posix()
                # The tag marks the latest approved book text; when the text changes deliberately, tag the new text and name the tag here.
                # swe-at-google/translation-polish was the first approved text; translation-review-2026-11 adds the whole-book review.
                before = subprocess.check_output(["git", "-C", str(BOOK), "show", "swe-at-google/translation-review-2026-11:./" + relative])
                self.assertEqual(path.read_bytes(), before, relative)

    def test_every_java_cpp_and_go_example_has_a_python_rewrite_or_a_reason(self):
        for chapter in self.manifest["chapters"]:
            text = (BOOK / chapter["source"]).read_text()
            expected = {t.content.replace("\t", "    ").strip() for t in build.reader_data.book.PARSE.parse(text)
                        if t.type == "fence" and t.info.strip() in TRANSLATED}
            if not expected:
                self.assertNotIn("codeVariants", chapter, chapter["id"])
                continue
            variants = json.loads((self.out / chapter["codeVariants"]).read_text())
            self.assertEqual({v["source"] for v in variants}, expected, chapter["id"])
            for variant in variants:
                self.assertIn(variant["language"], {"java", "cpp", "go"})
                self.assertTrue(variant.get("python") or variant.get("note"), chapter["id"])

    def test_search_index_covers_every_chapter(self):
        index = json.loads((self.out / "assets/search-index.json").read_text())
        self.assertEqual({e["route"] for e in index}, {c["route"] for c in self.manifest["chapters"]})
        for entry in index:
            self.assertEqual(set(entry), {"route", "chapter", "title", "anchor", "text"})
            self.assertTrue(entry["title"] and entry["text"], entry["route"])

    def test_font_subset_is_complete(self):
        for name in fonts.FACES:
            self.assertGreater((BOOK / "assets/fonts" / f"{name}.woff2").stat().st_size, 100_000, name)


if __name__ == "__main__":
    unittest.main()
