import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import corpus
import terms
from io_utils import digest, select_files, write_json
from svg_check import check_svg

SCRIPTS = Path(__file__).resolve().parents[1]
MIXED = """---
title: keep configuration
---
# Topic 主题

Deep modules hide details. A deep
module has an interface.
深模块隐藏细节。

> Keep this source quotation.
>
> 中文引文也需要统计。

| English column | 中文列 |
| --- | --- |
| Source cell | 中文单元格 |

Use `literal 中文` and <code>print("中文")</code>, not [a URL](https://example.test/a_(b)).

公式 $C = \\sum c_p t_p$ 与 \\(x+1\\)。

```python
# 中文 in protected code
x = 1
```

Footnote[^note] and missing[^missing].

[^note]: English note.
    中文脚注。

[^unused]: Keep unused English source.

[unused-link]: https://example.test/unused "Title"

<div data-id="keep">HTML 原样保留</div>
"""


class CorpusTests(unittest.TestCase):
    def test_interleaved_quotes_tables_footnotes_and_soft_wraps(self):
        doc = corpus.parse_document("chapter.md", MIXED)
        texts = [entry["text"] for entry in doc["segments"]]
        joined = "\n".join(texts)
        self.assertIn("Deep modules", joined)
        self.assertTrue(any("deep\nmodule" in text for text in texts))
        self.assertIn("中文引文", joined)
        self.assertIn("中文脚注", joined)
        self.assertIn("unused English source", joined)
        self.assertNotIn("literal 中文", joined)
        self.assertNotIn('print("中文")', joined)
        self.assertNotIn("protected code", joined)
        self.assertNotIn("https://", joined)
        self.assertNotIn("\\sum", joined)
        self.assertNotIn("HTML 原样", joined)
        self.assertNotIn("configuration", joined)
        self.assertIn("footnote", {entry["kind"] for entry in doc["segments"]})
        self.assertIn("table", {entry["kind"] for entry in doc["segments"]})
        self.assertEqual(len({entry["id"] for entry in doc["segments"]}), len(texts))

    def test_explicit_exclusions_do_not_assume_all_readme_sections_are_navigation(self):
        text = "# Intro\n\nIntroduction.\n\n## Contents\n\nNavigation.\n\n### Child\n\nNested.\n\n## Design\n\nUseful prose.\n"
        doc = corpus.parse_document("README.md", text, exclude_sections=["Contents"])
        all_text = " ".join(entry["text"] for entry in doc["segments"])
        self.assertIn("Useful prose", all_text)
        self.assertNotIn("Navigation", all_text)
        self.assertNotIn("Nested", all_text)
        self.assertEqual(doc["skipped"]["excluded_section"], 2)

    def test_protection_allows_chinese_but_catches_actual_source_changes(self):
        old = corpus.parse_document("a.md", MIXED)["protected"]
        self.assertEqual(old, corpus.parse_document("a.md", MIXED.replace("深模块隐藏细节", "深模块封装细节"))["protected"])
        mutations = [
            ("Keep this source", "Change this source"),
            ("x = 1", "x = 2"),
            ("`literal 中文`", "` literal 中文 `"),
            ('print("中文")', 'print("改动")'),
            ("a_(b)", "a_(c)"),
            ("example.test/unused", "example.test/changed"),
            ("[^missing]", "[^other]"),
            ("[^unused]", "[^different]"),
            ("Keep unused", "Alter unused"),
            ("\\sum c_p", "\\sum d_p"),
            ("\\(x+1\\)", "\\(x+2\\)"),
            ("data-id=\"keep\"", "data-id=\"change\""),
            ("title: keep", "title: change"),
            ("# Topic", "## Topic"),
        ]
        for before, after in mutations:
            with self.subTest(before=before):
                self.assertNotEqual(old, corpus.parse_document("a.md", MIXED.replace(before, after))["protected"])

    def test_block_code_keeps_crlf_bytes(self):
        before = "正文\r\n\r\n```txt\r\nx\r\n```\r\n"
        self.assertNotEqual(corpus.parse_document("a.md", before)["protected"],
                            corpus.parse_document("a.md", before.replace("\r\n", "\n"))["protected"])

    def test_inline_code_option_and_language_are_explicit(self):
        doc = corpus.parse_document("x.md", "解释 `Buffer` 行为。", language="zh", inline_code=True)
        self.assertIn("Buffer", doc["segments"][0]["text"])
        self.assertTrue(doc["segments"][0]["mixed"])
        self.assertEqual(doc["segments"][0]["language_status"], "declared")

    def test_bare_url_does_not_consume_following_chinese_sentence(self):
        doc = corpus.parse_document("x.md", "参见 https://example.test/a。继续说明。")
        self.assertIn("继续说明", doc["segments"][0]["text"])
        self.assertEqual(doc["protected"]["bare_urls"], ["https://example.test/a"])
        doc = corpus.parse_document("x.md", "Use `https://example.test` here.", inline_code=True)
        self.assertNotIn("https", doc["segments"][0]["text"])

    def test_reference_definition_source_is_preserved(self):
        before = "[Alias]: https://example.test\n\n正文。\n"
        after = before.replace("[Alias]", "[alias]")
        self.assertNotEqual(corpus.parse_document("x.md", before)["protected"],
                            corpus.parse_document("x.md", after)["protected"])

    def test_worktree_baseline_not_git_and_added_deleted_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.md").write_text("English source.\n\n中文正文。\n", encoding="utf-8")
            (root / "image.png").write_bytes(b"\x89PNG\r\n\x00")
            base = corpus.snapshot(root, ["*.md", "*.png"], [])
            (root / "a.md").write_text("English source.\n\n中文已润色。\n", encoding="utf-8")
            self.assertEqual(corpus.compare(root, base)["failures"], [])
            self.assertTrue(corpus.compare(root, base, exact=True)["failures"])
            (root / "image.png").write_bytes(b"changed")
            self.assertIn("image.png", [entry["file"] for entry in corpus.compare(root, base)["failures"]])
            (root / "a.md").unlink()
            (root / "image.png").unlink()
            self.assertEqual(len(corpus.compare(root, base)["failures"]), 2)
            (root / "new.md").write_text("新增", encoding="utf-8")
            self.assertIn("new.md", [entry["file"] for entry in corpus.compare(root, base)["failures"]])

    def test_exact_markdown_profile_rejects_chinese_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            file = root / "en.md"
            file.write_text("English 与中文", encoding="utf-8")
            base = corpus.snapshot(root, ["*.md"], [], ["en.md"])
            file.write_text("English 与改动", encoding="utf-8")
            self.assertTrue(corpus.compare(root, base)["failures"])

    def test_immutable_output_and_input_protection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            file = root / "source.json"
            file.write_text("original", encoding="utf-8")
            with self.assertRaises(ValueError):
                write_json(file, {}, forbidden=[file], overwrite=True)
            with self.assertRaises(FileExistsError):
                write_json(file, {})
            self.assertEqual(file.read_text(), "original")

    def test_symlink_escape_and_relative_globs(self):
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            external = Path(outside) / "other.md"
            external.write_text("not in project")
            (root / "escape.md").symlink_to(external)
            with self.assertRaises(ValueError):
                select_files(root, ["*.md"])
            with self.assertRaises(ValueError):
                select_files(root, ["../*.md"])

    def test_report_overwrite_cannot_be_used_to_refresh_a_baseline(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "report.json"
            baseline = {"schema": 1, "type": "translation-baseline"}
            write_json(file, baseline)
            with self.assertRaises(ValueError):
                write_json(file, baseline, overwrite=True)
            with self.assertRaises(ValueError):
                write_json(file, {"schema": 1, "type": "translation-corpus"}, overwrite=True)
            with self.assertRaises(ValueError):
                write_json(Path(directory) / "source.md", {}, overwrite=True)
            report = Path(directory) / "counts.json"
            write_json(report, {"schema": 1, "type": "glossary-counts", "value": 1})
            write_json(report, {"schema": 1, "type": "glossary-counts", "value": 2}, overwrite=True)
            self.assertEqual(json.loads(report.read_text())["value"], 2)


class TermTests(unittest.TestCase):
    @staticmethod
    def segments():
        return [
            {"root": "/book", "file": "en.md", "id": "one", "line": 1, "language": "en",
             "text": "class classes classical class_count class2 C++ C+++ test\nsize test size"},
            {"root": "/book", "file": "zh.md", "id": "two", "line": 3, "language": "zh",
             "text": "代码缺陷与缺陷，测试规模不同于测试范围。"},
        ]

    def test_aliases_longest_first_boundaries_and_whitespace(self):
        data = self.segments()
        result = terms.recount(data, ["class", "classes"], "en")
        self.assertEqual(result["frequency"], 2)
        self.assertEqual(terms.recount(data, ["C++"], "en")["frequency"], 1)
        self.assertEqual(terms.recount(data, ["test size"], "en")["frequency"], 2)
        self.assertEqual(terms.recount(data, ["代码缺陷", "缺陷"], "zh")["frequency"], 2)
        self.assertEqual(result["document_frequency"], 1)

    def test_recount_index_does_not_change_counts(self):
        data = self.segments()
        for language, aliases in [("en", ["classes", "class"]), ("en", ["C++"]),
                                  ("en", ["test size"]), ("zh", ["代码缺陷", "缺陷"])]:
            self.assertEqual(terms.recount(data, aliases, language),
                             terms.recount(data, aliases, language, terms.segment_index(data, language)))

    def test_duplicate_corpora_deduplicate_but_mixed_revisions_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "a.json"
            data = {"schema": 1, "type": "translation-corpus", "root": "/book",
                    "sources": {"en.md": "hash"}, "segments": [self.segments()[0]]}
            file.write_text(json.dumps(data))
            self.assertEqual(len(terms.load_corpora([file, file])), 1)
            other = Path(directory) / "b.json"
            data["sources"]["en.md"] = "changed"
            other.write_text(json.dumps(data))
            with self.assertRaises(ValueError):
                terms.load_corpora([file, other])

    def test_invalid_aliases_are_not_empty_regex_matches(self):
        for aliases in [[], [""], ["valid", " "]]:
            with self.assertRaises(ValueError):
                terms.alias_pattern(aliases, True)

    def test_case_sensitive_glossary_count_is_explicit(self):
        data = [{"root": "/book", "file": "x.md", "id": "x", "line": 1,
                 "language": "en", "text": "US us US user"}]
        self.assertEqual(terms.recount(data, ["US"], "en")["frequency"], 3)
        self.assertEqual(terms.recount(data, ["US"], "en", case_sensitive=True)["frequency"], 2)

    def test_shared_noun_policy_keeps_proper_names_and_compounds(self):
        tokens = [
            {"pos": "ADJ", "lemma": "deep", "start": 0, "end": 4},
            {"pos": "NOUN", "lemma": "module", "start": 5, "end": 12},
            {"pos": "OTHER", "lemma": ".", "start": 12, "end": 13},
        ]
        self.assertIn((0, 12, "deep module"), list(terms.noun_spans(tokens, 5)))
        self.assertNotIn((0, 4, "deep"), list(terms.noun_spans(tokens, 5)))


class SvgTests(unittest.TestCase):
    @staticmethod
    def svg(content=""):
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" aria-labelledby="t d">'
                '<title id="t">Title</title><desc id="d">Description</desc>'
                '<defs><marker id="a"/></defs>' + content + '</svg>').encode()

    def test_references_duplicate_ids_and_static_profile(self):
        self.assertEqual(check_svg(self.svg('<path d="M0 0H10" marker-end="url(#a)"/>'))["errors"], [])
        for content in ['<path id="t"/>', '<path marker-end="url(#missing)"/>',
                        '<script/>', '<foreignObject/>', '<image href="data:image/png;base64,x"/>',
                        '<rect onclick="alert(1)"/>']:
            with self.subTest(content=content):
                self.assertTrue(check_svg(self.svg(content))["errors"])

    def test_inherited_compound_markers_need_visual_judgment(self):
        result = check_svg(self.svg('<g marker-end="url(#a)"><path d="M0 0H10M20 0H30"/></g>'))
        self.assertFalse(result["errors"])
        self.assertTrue(result["warnings"])
        result = check_svg(self.svg('<g marker-end="url(#a)"><path d="M0 0H10"/><path d="M20 0H30"/></g>'))
        self.assertFalse(result["warnings"])

    def test_invalid_xml_dtd_and_nonfinite_viewbox_fail(self):
        for raw in [b"<svg>", b'<!DOCTYPE svg [<!ENTITY x "x">]><svg/>',
                    self.svg().replace(b"100 100", b"NaN 100")]:
            self.assertTrue(check_svg(raw)["errors"])


class CliTests(unittest.TestCase):
    def run_cli(self, script, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)],
                              text=True, capture_output=True)

    def test_snapshot_cannot_overwrite_and_verify_cannot_replace_baseline(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.md").write_text("Source.\n\n译文。", encoding="utf-8")
            baseline = root / "baseline.json"
            command = ("snapshot", "--root", root, "--include", "*.md", "--out", baseline)
            self.assertEqual(self.run_cli("corpus.py", *command).returncode, 0)
            old = baseline.read_bytes()
            self.assertNotEqual(self.run_cli("corpus.py", *command).returncode, 0)
            self.assertNotEqual(self.run_cli("corpus.py", "verify", "--root", root, "--baseline", baseline, "--out", baseline).returncode, 0)
            self.assertEqual(old, baseline.read_bytes())

    def test_extract_report_count_and_source_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            file = root / "book.md"
            file.write_text("Deep modules hide details.\n深模块隐藏细节。\n", encoding="utf-8")
            old = file.read_bytes()
            data = root / "corpus.json"
            self.assertEqual(self.run_cli("corpus.py", "extract", "--root", root, "--include", "*.md", "--out", data).returncode, 0)
            glossary = root / "terms.json"
            glossary.write_text(json.dumps([{"id": "deep", "preferred_zh": "深模块",
                "en_forms": ["deep module", "deep modules"], "zh_forms": ["深模块"]}]))
            report = root / "counts.json"
            result = self.run_cli("terms.py", "count", "--corpus", data, "--glossary", glossary, "--out", report)
            self.assertEqual(result.returncode, 0, result.stderr)
            entry = json.loads(report.read_text())["terms"][0]
            self.assertEqual(entry["english_counts"]["frequency"], 1)
            self.assertEqual(entry["chinese_counts"]["frequency"], 1)
            self.assertEqual(file.read_bytes(), old)


if __name__ == "__main__":
    unittest.main()
