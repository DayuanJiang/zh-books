"""Optional installed-model tests; skipped explicitly when a backend is unavailable."""

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from terms import chinese_vocabulary, english_vocabulary, recount


class InstalledModels(unittest.TestCase):
    def check_english(self, backend):
        segments = [{"root": "/fixture", "file": "en.md", "id": "en", "line": 1,
                     "language": "en", "text": "Deep modules hide complexity. A deep module hides complexity."}]
        try:
            vocabulary, info = english_vocabulary(segments, backend, "en_core_web_sm", 5)
        except ImportError as error:
            self.skipTest(str(error))
        except ValueError as error:
            if "data missing" in str(error) or "model unavailable" in str(error):
                self.skipTest(str(error))
            raise
        self.assertEqual(info["backend"], backend)
        self.assertIn("deep module", vocabulary)
        self.assertFalse(set(vocabulary) & {"be", "in", "it", "we", "you"})
        self.assertEqual(recount(segments, vocabulary["deep module"]["forms"], "en")["frequency"], 2)

    def test_nltk(self):
        self.check_english("nltk")

    def test_spacy(self):
        self.check_english("spacy")

    def test_jieba_custom_dictionary_and_negative_phrase(self):
        segments = [{"language": "zh", "text": "读写一致性与不稳定测试。读写一致性很重要。"}]
        with tempfile.TemporaryDirectory() as directory:
            dictionary = Path(directory) / "dictionary.txt"
            dictionary.write_text("读写一致性 100000 n\n不稳定测试 100000 n\n", encoding="utf-8")
            try:
                words = chinese_vocabulary(segments, dictionary, 3)
            except ImportError as error:
                self.skipTest(str(error))
        self.assertIn("读写一致性", words)
        self.assertIn("不稳定测试", words)
        self.assertNotIn("稳定测试", words)


if __name__ == "__main__":
    unittest.main()
