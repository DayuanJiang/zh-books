import json
from pathlib import Path
import tempfile
import unittest

import chapter_figures as figures
import reader_data as reader

FIXTURES = Path(__file__).with_name("fixtures")


class ChapterFigureTests(unittest.TestCase):
    def test_wrap_respects_width_and_punctuation(self):
        wrapped = figures.wrap("测试代码宁可重复也要直白，别把逻辑和条件放进测试里。", 15, 150)
        for line in wrapped:
            self.assertLessEqual(figures.width(line, 15), 150 + 15)
            self.assertNotIn(line[0], figures.CLOSING)
        self.assertEqual(figures.wrap("Live at Head：一起改、一起测", 15, 400), ["Live at Head：一起改、一起测"])

    def test_text_budgets_fail_the_build_instead_of_overflowing(self):
        with self.assertRaisesRegex(ValueError, "too wide"):
            figures.fit("这一行文字明显超过了给它的宽度预算", 20, 100, "fixture")
        with self.assertRaisesRegex(ValueError, "allows 1"):
            figures.lines("需要换行的长句子，需要换行的长句子，需要换行的长句子", 15, 120, 1, "fixture")

    def test_fixture_chapter_builds_four_figures_that_pass_reader_checks(self):
        metadata = json.loads((FIXTURES / "ch13.json").read_text())
        built = figures.build(metadata)
        self.assertEqual(set(built), {metadata["desktop"], metadata["mobile"], metadata["storyDesktop"], metadata["storyMobile"]})
        self.assertIn(metadata["map"]["form"], figures.FORMS)
        for part in metadata["map"]["parts"]:
            self.assertIn(part["icon"], figures.ICONS)
        for act in metadata["story"]["acts"]:
            self.assertIn(act["icon"], figures.ICONS)
            self.assertIn(act.get("tone", "pri"), figures.TONES)
        with tempfile.TemporaryDirectory() as folder:
            for relative, svg in built.items():
                path = Path(folder) / Path(relative).name
                path.write_text(svg)
                reader.check_svg(path, 13, relative.endswith("-mobile.svg"), story="story" in relative)


if __name__ == "__main__":
    unittest.main()
