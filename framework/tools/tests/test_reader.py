from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

import reader_data as reader

READER = Path(__file__).resolve().parents[2] / "reader"


class ReaderTests(unittest.TestCase):
    def test_lucide_sprite_contains_required_controls(self):
        root = ET.parse(READER / "reader-icons.svg").getroot()
        ids = {node.get("id") for node in root}
        for name in ["menu", "sun", "moon", "minus", "plus", "maximize-2", "minimize-2", "x", "download", "list"]:
            self.assertIn("icon-" + name, ids)

    def test_reader_core_dependencies_are_local(self):
        index = (READER / "index.html").read_text()
        self.assertIn('src="assets/vendor/docsify.min.js"', index)
        self.assertIn('href="assets/reader.css?v={{hash:assets/reader.css}}"', index)
        self.assertIn('src="assets/reader.js?v={{hash:assets/reader.js}}"', index)
        self.assertNotIn("cdn.jsdelivr.net", index)
        css = (READER / "reader.css").read_text()
        self.assertIn('src: url("fonts/NotoSerifSC-Regular.woff2")', css)
        self.assertIn('src: url("fonts/NotoSerifSC-SemiBold.woff2")', css)

    def test_reader_has_no_book_specific_text(self):
        script = (READER / "reader.js").read_text()
        for text in ("谷歌", "Software Engineering at Google", "swe-at-google", "sweg-"):
            self.assertNotIn(text, script)

    def test_diagram_review_requires_question_and_visual_reasoning(self):
        metadata = {"id": "fixture", "pedagogy": {"action": "keep"}}
        with self.assertRaisesRegex(ValueError, "readerQuestion"):
            reader.check_pedagogy(metadata)
        metadata["pedagogy"].update({field: "Reviewed fixture." for field in reader.PEDAGOGY_FIELDS})
        reader.check_pedagogy(metadata)
        metadata["pedagogy"]["action"] = "retire"
        with self.assertRaisesRegex(ValueError, "decision"):
            reader.check_pedagogy(metadata)


if __name__ == "__main__":
    unittest.main()
