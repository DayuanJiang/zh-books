import tempfile
import unittest
from pathlib import Path

import reader_data as reader


class CodeVariantTests(unittest.TestCase):
    def test_rewrite_must_parse_and_match_a_code_block(self):
        text = "Intro\n\n```java\nint x = 1;\n```\n"
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            (folder / "01.java").write_text("int x = 1;\n")
            with self.assertRaisesRegex(ValueError, "needs a Python rewrite"):
                reader.compile_code_variants(folder, text)
            (folder / "01.py").write_text("x = 1\n")
            self.assertEqual(reader.compile_code_variants(folder, text),
                             [{"language": "java", "source": "int x = 1;", "python": "x = 1"}])
            (folder / "01.py").write_text("x = = 1\n")
            with self.assertRaisesRegex(ValueError, "does not parse"):
                reader.compile_code_variants(folder, text)
            (folder / "01.py").unlink()
            (folder / "01.skip").write_text("No Python equivalent.\n")
            self.assertEqual(reader.compile_code_variants(folder, text)[0]["note"], "No Python equivalent.")
            (folder / "01.java").write_text("int y = 2;\n")
            with self.assertRaisesRegex(ValueError, "not a code block"):
                reader.compile_code_variants(folder, text)


if __name__ == "__main__":
    unittest.main()
