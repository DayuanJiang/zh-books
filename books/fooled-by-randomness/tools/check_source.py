"""Compare every section in en/ with the EPUB file it came from, word by word (see review/source.md).

    uv run --project framework/tools python -I books/fooled-by-randomness/tools/check_source.py book.epub

Words are compared in order, lowercased, without punctuation; a word may contain hyphens, apostrophes and
dots ("risk-taking", "you’re", "B.C."), so joining a split word or adding a missing space after punctuation
does not count as a change. Footnote definitions are compared with the footnotes file. Every difference is
printed; the expected ones are listed in EXPECTED and explained in review/source.md.
"""

import difflib
import re
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

SOURCE = {
    "preface": 3, "summaries": 4, "prologue": 5, "part1": 6, "ch01": 7, "ch02": 8, "ch03": 9, "ch04": 10, "ch05": 11,
    "ch06": 12, "ch07": 13, "part2": 14, "ch08": 15, "ch09": 16, "ch10": 17, "ch11": 18, "part3": 19, "ch12": 20,
    "ch13": 21, "ch14": 22, "epilogue": 23, "postscript": 24, "dedication": 25, "acknowledgments-first": 26,
    "acknowledgments-second": 27, "notes": 28, "references": 29, "about-the-author": 32,
}
NUMBER_WORDS = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen".split()
EXPECTED = {f"ch{n:02d}": [("replace", [word], [str(n)])] for n, word in enumerate(NUMBER_WORDS, 1)}
EXPECTED["dedication"] = [("insert", [], ["dedication"])]  # the importer's heading; the page has none
EXPECTED["preface"] = [("replace", ["chapters13"], ["chapters", "13"])]  # "Chapters<a>13</a>": missing space
# Words split by the hyphen of a print line break, joined by curate_source.py.
EXPECTED["ch01"] += [("replace", ["aloof-ness"], ["aloofness"])] + [("replace", ["out-comes"], ["outcomes"])] * 2
EXPECTED["ch04"] += [("replace", ["non-sense"], ["nonsense"])]
EXPECTED["ch12"] += [("replace", ["po", "tuit"], ["potuit"])]  # a stray diaeresis split the word
EXPECTED["references"] = [("replace", ["al-ghazl"], ["al-ghazālī"])]
EXPECTED_NOTES = [("replace", ["empiri-cism"], ["empiricism"]), ("replace", ["in-dependently"], ["independently"]),
                  ("replace", ["al-ghazälï"], ["al-ghazālī"])]
SUBSCRIPTS = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
WORD = re.compile(r"[^\W_]+(?:[-’'.][^\W_]+)*")


def words(text):
    return WORD.findall(text.lower().translate(SUBSCRIPTS))


def source_words(html):
    """Words of an EPUB file: drop caps joined to the rest of their word, as the reader sees them."""
    html = re.sub(r'<span class="ic">(\w)</span>\s*', r"\1", html.replace("&#13;", ""))
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a", class_="hlink", string=re.compile("Return to text")):
        link.decompose()
    for block in soup.find_all(["p", "div", "li", "h1", "br"]):  # blocks end words; inline tags do not
        block.insert_after(" ")
    return words(soup.body.get_text())


def markdown_words(text):
    """Words of a section without footnote markers and link targets; footnote definitions separately."""
    notes = re.findall(r"(?m)^\[\^\w+\]: (.*)$", text)
    body = re.sub(r"(?m)^\[\^\w+\]: .*$", "", text)
    body = re.sub(r"\[\^\w+\]", "", body)
    body = re.sub(r"\]\([^)]*\)", "]", body)
    return words(body), words(" ".join(notes))


def differences(a, b):
    return [(op, a[i1:i2], b[j1:j2]) for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
            if op != "equal"]


def main(epub_path):
    epub = zipfile.ZipFile(epub_path)
    config = book_config.load(BOOK)
    # Drop caps that stand for a word of their own ("I start") are joined above; split them again here.
    separate = {8: ("istart", "i start"), 11: ("iused", "i used"), 23: ("acouple", "a couple")}
    total_source = total_en = 0
    unexplained = 0
    for entry in config["chapters"]:
        number = SOURCE[entry["id"]]
        html = epub.read(f"EPUB/text{number:05d}.html").decode()
        source = source_words(html)
        if number in separate:
            joined, split = separate[number]
            source = " ".join(source).replace(joined, split, 1).split()
        body, notes = markdown_words((BOOK / "en" / entry["file"]).read_text())
        found = differences(source, body)
        expected = EXPECTED.get(entry["id"], [])
        extra = [d for d in found if d not in expected]
        missing = [d for d in expected if d not in found]
        unexplained += len(extra) + len(missing)
        line = f"{entry['id']:<24} source {len(source):>6}  en {len(body):>6}  difference {len(body) - len(source):+d}"
        if notes:
            note_source = source_words(epub.read("EPUB/text00030.html").decode())
            note_source = note_source[note_source.index("7") + 1:]  # after "Footnotes", the instruction, "Chapter 7"
            note_diff = differences(note_source, notes)
            unexplained += len([d for d in note_diff if d not in EXPECTED_NOTES]) + len([d for d in EXPECTED_NOTES if d not in note_diff])
            line += f"  footnotes source {len(note_source)} en {len(notes)}" + ("" if not note_diff else f" {note_diff}")
            total_source += len(note_source)
            total_en += len(notes)
        print(line + ("" if not found else f"  expected: {found}" if not extra else f"  UNEXPECTED: {extra}"))
        if missing:
            print(f"  expected but not found: {missing}")
        total_source += len(source)
        total_en += len(body)
    print(f"total: source {total_source}, en {total_en}; unexplained differences: {unexplained}")
    return 1 if unexplained else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
