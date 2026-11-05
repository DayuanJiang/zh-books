"""Compare en/ with the original EPUB: words per section, paragraph by paragraph, and every note once.

    uv run --project framework/tools python -I books/bad-blood/tools/check_source.py book.epub

A section's text is compared with the XHTML file it came from, without headings, scene-break dashes and
notes. Text is compared in a folded form (letters and digits only, lower case), so the case of the small-caps
lead-ins and B₁₂ for B12 do not count as differences. The address on the envelope is one paragraph with line
breaks in en/; each line counts as one paragraph here, as in the EPUB.
"""

import collections
import difflib
import re
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

PREFIX = "OEBPS/Carr_9781524731663_epub3_"
NOTES = PREFIX + "nts_r1.xhtml"
FILES = {"dedication": "ded", "authors-note": "ant", "prologue": "c001", "epilogue": "epl",
         "acknowledgments": "ack", "about-the-author": "ata"}
FOOTNOTE = re.compile(r"^\[\^\d+\]: (.*)$", re.M)
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")


def fold(text):
    return re.sub(r"[^a-z0-9]", "", text.translate(SUB).lower())


def words(text):
    return len(text.split())


def source_paragraphs(epub, name):
    body = BeautifulSoup(epub.read(PREFIX + name + "_r1.xhtml"), "html.parser").body
    return [" ".join(p.get_text("").split()) for p in body.find_all("p")]


def markdown_paragraphs(text):
    """Paragraphs, list items and quoted paragraphs of a section, without headings and footnotes.

    An ordered list item gets its number back ("1. Lie to venture capitalists"), as the EPUB has it in the
    text; a line break starts a new paragraph.
    """
    units, number, previous = [], None, None
    for token in MarkdownIt("commonmark").parse(FOOTNOTE.sub("", text)):
        if token.type == "ordered_list_open":
            number = int(token.attrGet("start") or 1)
        elif token.type == "bullet_list_open":
            number = None
        elif token.type == "inline" and previous != "heading_open":
            lines = [""]
            for child in token.children:
                if child.type in ("text", "code_inline"):
                    lines[-1] += child.content
                elif child.type == "softbreak":
                    lines[-1] += " "
                elif child.type == "hardbreak":
                    lines.append("")
            if number is not None and token.level >= 2:  # inside an ordered list item
                lines[0] = f"{number}. " + lines[0]
                number += 1
            units += [" ".join(re.sub(r"\[\^\d+\]", "", line).split()) for line in lines]
        previous = token.type
    return units


def headings(text):
    return [line for line in text.splitlines() if line.startswith("#")]


def epub_notes(epub):
    """{source file name: [note text]} from the notes file, by the file each note links back to."""
    page = BeautifulSoup(epub.read(NOTES), "html.parser")
    notes = collections.defaultdict(list)
    for paragraph in page.find_all("p", class_="para-en"):
        target = re.search(r"epub3_(\w+)_r1\.xhtml#Y_", paragraph.a["href"]).group(1)
        notes[target].append(" ".join(paragraph.get_text("").split()))
    return notes


def check_markers(text):
    """Every [^n] in the text once, definitions numbered 1..N in the order of the markers."""
    body = FOOTNOTE.sub("", text)
    refs = [int(n) for n in re.findall(r"\[\^(\d+)\]", body)]
    defined = [int(n) for n in re.findall(r"(?m)^\[\^(\d+)\]:", text)]
    return refs == defined == list(range(1, len(defined) + 1))


def main(epub_path):
    epub = zipfile.ZipFile(epub_path)
    config = book_config.load(BOOK)
    notes = epub_notes(epub)
    problems, totals = 0, collections.Counter()
    print(f"{'section':18} {'EPUB words':>10} {'en words':>9} {'paragraphs':>10} {'notes':>7}  result")
    for entry in config["chapters"]:
        name = FILES.get(entry["id"]) or f"c{entry['number'] + 1:03d}"
        text = (BOOK / "en" / entry["file"]).read_text()
        found = []
        if len(headings(text)) != 1 or not text.startswith("# "):
            found.append(f"expected one level 1 heading, found {headings(text)}")
        if not check_markers(text):
            found.append("footnote markers and definitions do not match")
        src = [p for p in source_paragraphs(epub, name) if p]
        md = [p for p in markdown_paragraphs(text) if p]
        a, b = [fold(p) for p in src], [fold(p) for p in md]
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if tag != "equal":
                found.append(f"{tag}: EPUB {src[i1:i2]!r:.300}\n           en   {md[j1:j2]!r:.300}")
        # A note's web address is a Markdown link in en/; only the link text is in the EPUB's text.
        footnotes = [LINK.sub(r"\1", f) for f in FOOTNOTE.findall(text)]
        want, have = notes.get(name, []), footnotes
        if collections.Counter(map(fold, want)) != collections.Counter(map(fold, have)):
            found.append(f"notes differ from the {len(want)} notes that link to {name}")
        counts = {"EPUB words": sum(map(words, src)), "en words": sum(map(words, md)),
                  "EPUB note words": sum(map(words, want)), "en note words": sum(words(f.replace("*", "")) for f in have),
                  "notes": len(want), "footnotes": len(have)}
        totals.update(counts)
        print(f"{entry['id']:18} {counts['EPUB words']:>10} {counts['en words']:>9} {len(src):>5}/{len(md):<4} "
              f"{len(want):>3}/{len(have):<3}  {'same text' if not found else 'PROBLEMS'}")
        for line in found:
            print("    " + line)
        problems += len(found)
    print(f"{'total':18} {totals['EPUB words']:>10} {totals['en words']:>9} {'':10} {totals['notes']:>3}/{totals['footnotes']:<3}")
    all_notes = sum(len(v) for v in notes.values())
    print(f"notes: {all_notes} in the EPUB, {totals['footnotes']} footnotes in en/; "
          f"note words {totals['EPUB note words']} in the EPUB, {totals['en note words']} in en/")
    if all_notes != totals["footnotes"]:
        problems += 1
    print("OK" if not problems else f"{problems} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
