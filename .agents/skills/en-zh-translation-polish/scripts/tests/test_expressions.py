import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import terms
from io_utils import digest

RULES = [{"id": "verb-object-out-of-noun", "patterns": [[
    {"POS": "VERB"}, {"POS": "NOUN"}, {"LOWER": "out"},
    {"LOWER": "of"}, {"POS": "NOUN"},
]]}]


class ExpressionRules(unittest.TestCase):
    def load(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rules.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return terms.load_expression_patterns(path)

    def test_config_shape_and_ids(self):
        self.assertEqual(self.load(RULES), RULES)
        for data in [{}, [], [RULES[0], RULES[0]], [{"id": 3, "patterns": [[{"POS": "VERB"}]]}],
                     [{"id": "x", "patterns": []}], [{"id": "x", "patterns": [[{}]]}],
                     [{"id": "x", "patterns": ["raw regex"]}], [{"id": "x", "patterns": [[{"POS": "VERB"}]], "callback": "run"}]]:
            with self.subTest(data=data), self.assertRaises(ValueError):
                self.load(data)

    def test_no_silent_backend_change(self):
        with self.assertRaisesRegex(ValueError, "explicit spaCy"):
            terms.english_vocabulary([], "nltk", "missing", 5, RULES)

    def test_no_english_does_not_load_model(self):
        vocabulary, info = terms.english_vocabulary([], "spacy", "missing", 5, RULES)
        self.assertFalse(vocabulary)
        self.assertEqual(info["status"], "not_run_no_english")


class InstalledExpressionModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import spacy
            spacy.load("en_core_web_sm")
        except (ImportError, OSError) as error:
            raise unittest.SkipTest(str(error))

    def segments(self, text):
        return [{"root": "/sample", "file": "source.md", "id": "s1", "line": 1,
                 "language": "en", "text": text}]

    def vocabulary(self, text, rules=RULES, max_words=5):
        return terms.english_vocabulary(self.segments(text), "spacy", "en_core_web_sm",
                                        max_words, rules)[0]

    def test_verbal_expression_without_memorized_phrase(self):
        text = "We define errors out of existence. We remove faults out of existence."
        original = self.vocabulary(text, [])
        result = self.vocabulary(text)
        for key, surface in [("define error out of existence", "define errors out of existence"),
                             ("remove fault out of existence", "remove faults out of existence")]:
            self.assertNotIn(key, original)
            self.assertIn(surface, result[key]["forms"])
            self.assertEqual(result[key]["pattern_matches"][0]["text"], surface)
            self.assertEqual(result[key]["pattern_matches"][0]["segment"], "s1")

    def test_surface_recount_distinct_from_rule_evidence(self):
        text = "We define errors out of existence. We define errors out of existence."
        item = self.vocabulary(text)["define error out of existence"]
        self.assertEqual(len(item["pattern_matches"]), 2)
        self.assertEqual(terms.recount(self.segments(text), item["forms"], "en")["frequency"], 2)

    def test_length_and_sentence_boundaries(self):
        self.assertNotIn("define error out of existence",
                         self.vocabulary("We define errors out of existence.", max_words=4))
        rules = [{"id": "cross-sentence", "patterns": [[
            {"LOWER": "first"}, {"IS_PUNCT": True}, {"LOWER": "second"}]]}]
        result = self.vocabulary("First. Second.", rules)
        self.assertFalse(any(entry["pattern_matches"] for entry in result.values()))

    def test_spacy_rejects_unknown_attributes(self):
        with self.assertRaises(ValueError):
            self.vocabulary("Sample text.", [{"id": "bad", "patterns": [[{"NOT_AN_ATTRIBUTE": "x"}]]}])

    def test_cli_rule_provenance_and_input_guard(self):
        scripts = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.md"
            source.write_text("We define errors out of existence.", encoding="utf-8")
            corpus = root / "corpus.json"
            corpus.write_text(json.dumps({"schema": 1, "type": "translation-corpus",
                "root": str(root), "sources": {"source.md": digest(source.read_bytes())},
                "segments": self.segments(source.read_text())}), encoding="utf-8")
            rules = root / "rules.json"
            rules.write_text(json.dumps(RULES), encoding="utf-8")
            before = rules.read_bytes()
            output = root / "output.json"
            command = [sys.executable, str(scripts / "terms.py"), "candidates", "--corpus",
                       str(corpus), "--english-backend", "spacy", "--expression-patterns",
                       str(rules), "--min-frequency", "1", "--out"]
            done = subprocess.run([*command, str(output)], capture_output=True, text=True)
            self.assertEqual(done.returncode, 0, done.stderr)
            data = json.loads(output.read_text())
            self.assertEqual(data["expression_patterns_sha256"], digest(before))
            self.assertIn("define error out of existence", [entry["candidate"] for entry in data["english"]])
            blocked = subprocess.run([*command, str(rules), "--overwrite"], capture_output=True, text=True)
            self.assertEqual(blocked.returncode, 2)
            self.assertEqual(before, rules.read_bytes())


if __name__ == "__main__":
    unittest.main()
