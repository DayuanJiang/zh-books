import unittest

import book


class AlignerTests(unittest.TestCase):
    EN = "# Title\n\nOne.\n\n- a\n- b\n\n```java\nx();\n```\n\nTwo.[^1]\n\n[^1]: Note.\n"
    ZH = "# 标题\n\n一。\n\n- 甲\n- 乙\n\n二。[^1]\n\n[^1]: 注。\n"

    def test_aligner_rejects_structural_drift(self):
        en, zh = self.EN, self.ZH
        chapter = book.compile_chapter("fixture", en, zh, "en")
        self.assertEqual([u["kind"] for u in chapter["units"]], ["heading", "paragraph", "list", "code", "paragraph"])
        self.assertEqual(chapter["units"][4]["target"], "二。[^1]")
        self.assertIn("note-trigger", chapter["units"][4]["targetHtml"])
        with self.assertRaisesRegex(ValueError, "structure differs"):
            book.compile_chapter("fixture", en, zh.replace("- 甲\n- 乙", "- 甲"), "en")
        with self.assertRaisesRegex(ValueError, "translation missing"):
            book.compile_chapter("fixture", en + "\nThree.\n", zh, "en")
        with self.assertRaisesRegex(ValueError, "footnotes without translation"):
            book.compile_chapter("fixture", en, zh.replace("[^1]: 注。", ""), "en")
        with self.assertRaisesRegex(ValueError, "never referenced"):
            book.compile_chapter("fixture", en, zh + "[^t1]: **译者注** 多余。\n", "en")

    def test_partial_translation_marks_the_untranslated_rest(self):
        zh = "# 标题\n\n一。\n"
        with self.assertRaises(ValueError):
            book.compile_chapter("fixture", self.EN, zh, "en")
        chapter = book.compile_chapter("fixture", self.EN, zh, "en", partial=True)
        pending = [u["kind"] for u in chapter["units"] if u.get("pending")]
        self.assertEqual(pending, ["list", "paragraph"])
        code = next(u for u in chapter["units"] if u["kind"] == "code")
        self.assertNotIn("pending", code)
        self.assertEqual(chapter["footnotes"]["1"]["targetHtml"], "Note.")
        untitled = book.compile_chapter("fixture", self.EN, "", "en", partial=True)
        self.assertEqual(untitled["title"], "Title")
        with self.assertRaisesRegex(ValueError, "structure differs"):
            book.compile_chapter("fixture", self.EN, "# 标题\n\n一。\n\n二。\n", "en", partial=True)

    def test_roles_and_anchors(self):
        en = ("# Unit Testing\n\n**Written by A**\n\n*Quote.*\n\n— Someone\n\nBody.\n\n## Test Sizes\n\n"
              "*Figure 1-1. Sizes*\n\n**Motivations**\n\nfile.py:\n\n```python\npass\n```\n\n## Test Sizes\n")
        zh = "# 单元测试\n\n**作者：A**\n\n引文。\n\n— 某人\n\n正文。\n\n## 测试规模\n\n*图1-1 规模*\n\n**动机**\n\n## 测试规模\n"
        chapter = book.compile_chapter("fixture", en, zh, "en")
        roles = [(u["kind"], u["role"]) for u in chapter["units"]]
        self.assertEqual(roles[1:5], [("paragraph", "credit"), ("paragraph", "epigraph"), ("paragraph", "attribution"), ("paragraph", None)])
        self.assertEqual([u["role"] for u in chapter["units"] if u["kind"] == "paragraph"][4:7], ["caption", "subheading", "code-label"])
        self.assertEqual([u["anchor"] for u in chapter["units"] if u["kind"] == "heading"], ["unit-testing", "test-sizes", "test-sizes-2"])
        self.assertEqual(chapter["englishTitle"], "Unit Testing")


if __name__ == "__main__":
    unittest.main()
