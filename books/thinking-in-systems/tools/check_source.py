"""Compare each section of en/ with the EPUB file it came from, word by word (see review/source.md).

    uv run --project framework/tools python -I books/thinking-in-systems/tools/check_source.py book.epub

For every section it prints the word counts of the EPUB file (without the chapter title) and of the
Markdown (without the # title line and the note definitions), then every run of words that differs,
so each difference can be checked against the list of fixes in prepare_epub.py. The notes are compared
the same way: the note texts in the EPUB's notes file against the [^n] definitions of each section.
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

SOURCES = {
    "dedication": "chap6", "authors-note": "chap8", "editors-note": "chap9", "epigraph": "chap10",
    "introduction": "chap11", "part1": "chap12", "ch01": "chap13", "ch02": "chap14", "part2": "chap15",
    "ch03": "chap16", "ch04": "chap17", "ch05": "chap18", "part3": "chap19", "ch06": "chap20", "ch07": "chap21",
    "appendix": "chap22", "bibliography": "chap24", "acknowledgments": "chap25", "about-the-author": "chap26",
}
TITLE_CLASSES = {"h9", "h7", "h13"}


def html_words(soup):
    """Words of the text blocks, without note numbers, leading bullets and the title paragraphs."""
    for sup in soup.find_all("sup"):
        if sup.find("a", href=re.compile("part23|#d411519681")):
            sup.decompose()
    for star in soup.find_all("a", href=re.compile("#d411519681")):
        star.decompose()
    for br in soup.find_all("br"):
        br.replace_with(" ")
    words = []
    for block in soup.body.find_all(["p", "td"]):
        if set(block.get("class") or []) & TITLE_CLASSES:
            continue
        block_words = [w for w in block.get_text("").split() if set(w) != {"_"}]
        words += block_words[1:] if block_words[:1] == ["•"] else block_words
    return words


def markdown_words(text):
    lines = []
    for line in text.splitlines():
        if line.startswith("![") or re.match(r"^\[\^\d+\]:", line) or re.fullmatch(r"\|?[ |-]*-{3}[ |-]*\|?|-{3}", line.strip()):
            continue
        line = re.sub(r"^(#+|>|- )\s?", "", line.strip())
        line = re.sub(r"^>\s?", "", line)
        line = re.sub(r"^- ", "", line)
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"\[\^\d+\]", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("*", "").replace("\\", "").replace("|", " ")
    return text.split()


def notes_by_document(epub):
    """Words of each endnote, grouped by the document that cites it, in order."""
    soup = BeautifulSoup(epub.read("OEBPS/chap23_thinking_9781603581486_epub_part23.html"), "html.parser")
    notes = {}
    for p in soup.find_all("p", class_="tx12a"):
        link = p.find("a")
        target = link["href"].split("_", 1)[0]
        link.decompose()
        words = p.get_text("").split()
        if words and words[0] == ".":
            words = words[1:]
        elif words and words[0].startswith("."):
            words[0] = words[0][1:]
        notes.setdefault(target, []).append(words)
    return notes


def show(a, b):
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != "equal":
            out.append(f"    {tag}: {' '.join(a[i1:i2])[:150]!r} -> {' '.join(b[j1:j2])[:150]!r}")
    return out


def main(epub_path):
    epub = zipfile.ZipFile(epub_path)
    names = {n.rsplit("/", 1)[-1].split("_", 1)[0]: n for n in epub.namelist() if n.endswith(".html")}
    notes = notes_by_document(epub)
    total_source = total_markdown = 0
    for entry in book_config.load(BOOK)["chapters"]:
        doc = SOURCES[entry["id"]]
        text = (BOOK / "en" / entry["file"]).read_text()
        source = html_words(BeautifulSoup(epub.read(names[doc]), "html.parser"))
        if doc == "chap13":
            # The asterisk note sits at the end of chapter 1 in the EPUB; it is footnote 2 here.
            star = "* Definitions of words in bold face can be found in the Glossary.".split()
            assert source[-len(star):] == star
            source = source[:-len(star)]
        body = text.split("\n", 1)[1]
        mine = markdown_words(body)
        total_source += len(source)
        total_markdown += len(mine)
        print(f"{entry['id']:<16} EPUB {len(source):>6}  en/ {len(mine):>6}  difference {len(mine) - len(source):+d}")
        for line in show(source, mine):
            print(line)
        definitions = re.findall(r"(?m)^\[\^\d+\]: (.*)$", text)
        expected = notes.get(doc, [])
        if doc == "chap13":
            expected = expected[:1] + [star[1:]] + expected[1:]
        if definitions or expected:
            mine_notes = [markdown_words(d) for d in definitions]
            same = sum(a == b for a, b in zip(expected, mine_notes))
            print(f"{'':<16} notes: EPUB {len(expected)}, en/ {len(mine_notes)}, identical words {same}")
            for k, (a, b) in enumerate(zip(expected, mine_notes), 1):
                if a != b:
                    print(f"    note {k}:")
                    for line in show(a, b):
                        print("  " + line)
    print(f"total EPUB {total_source}  en/ {total_markdown}  difference {total_markdown - total_source:+d}")


if __name__ == "__main__":
    main(sys.argv[1])
