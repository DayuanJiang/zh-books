"""Compare en/ with the complete HarperCollins e-book, section by section and block by block.

    uv run --project framework/tools python -I books/never-split-the-difference/tools/compare_source.py new.epub [--words]

The first import came from a calibre EPUB with only chapters 1 to 10. The complete e-book (2016, ASIN
B014DUR7L2) also has the dedication, acknowledgments, the appendix, notes, index and About the Authors,
and marks the notes in the chapters with superscript numbers. This script reports:

- Sections: every entry of the e-book's table of contents, and whether en/ has it (book.json order).
- Blocks: the e-book's paragraphs, headings and list items, aligned with the blocks and list items of the
  en/ file (difflib on letters and digits). Unmatched blocks on either side are listed.
- Text: paired blocks whose text differs once whitespace is collapsed; headings are compared without case
  (the e-book sets them in capitals). Each difference is shown as a word diff.
- Emphasis: italic and bold runs that differ between the two sides, per section.
- Figures and tables: <img> and <table> in the e-book's sections.
- Expected after complete_source.py: the ellipsis style (". . ." in the e-book, "…" in en/), the case of
  headings and of the two names set in capitals in About the Authors, and the two fixes of the first
  curation; the appendix's two title lines are compared as one heading, the hc.com advertisement is left out.
- Notes: the superscript note numbers in each chapter, with the words before them, and the entries of the
  Notes section per chapter.

With --words it also prints the word count of each section in the e-book and in en/ (words are
whitespace-separated tokens with a letter or digit; note numbers are left out).
"""

import difflib
import re
import sys
import warnings
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from markdown_it import MarkdownIt

BOOK = Path(__file__).resolve().parent.parent
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
LABEL = re.compile(r"^CHAPTER \d+$")
# Classes of the e-book: "head" section heading, "ct" chapter title, "bl"/"bl1" list items,
# "di"/"email"/"emailm" quoted lines, "da" the dateline of chapter 2, "SECTION-BREAK" an empty spacer.
HEADING_CLASSES = {"head"}
ADVERTISEMENT = "Discover great authors, exclusive offers, and more at"  # last line of About the Authors
LIST_CLASSES = {"bl", "bl1"}


def words(text):
    return [t for t in text.split() if re.search(r"[A-Za-z0-9]", t)]


def key(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def toc(epub):
    """[(label, file, anchor, subtitle)] for the entries of toc.ncx.

    The table of contents is flat: a chapter's subtitle is the next entry, pointing into the same file.
    """
    soup = BeautifulSoup(epub.read("toc.ncx").decode(), "html.parser")
    found = []
    for point in soup.find("navmap").find_all("navpoint"):
        label = " ".join(point.find("text").get_text().split())
        file, _, anchor = point.find("content")["src"].partition("#")
        if found and found[-1][0].startswith("CHAPTER ") and file == found[-1][1] and anchor:
            found[-1] = found[-1][:3] + (label,)
            continue
        found.append((label, file, anchor, ""))
    return found


def is_bold_only(p):
    pieces = [s for s in p.find_all(string=True) if s.strip()]
    return bool(pieces) and all(s.find_parent("b") is not None for s in pieces)


def epub_units(html):
    """[(kind, text, italics, bolds, notes)] for one section of the e-book.

    kind: title, heading, subheading, item, quote, para. notes: [(number, words before it)].
    """
    soup = BeautifulSoup(html, "html.parser")
    for hidden in soup.find_all(class_=["hide1"]):
        hidden.decompose()
    units = []
    for tag in soup.body.find_all(["h2", "p"]):
        classes = set(tag.get("class") or [])
        notes = []
        for sup in tag.find_all("sup"):
            before = " ".join("".join(s for s in sup.find_all_previous(string=True, limit=12)[::-1]).split()[-6:])
            notes.append((sup.get_text(strip=True), before))
            sup.decompose()
        text = " ".join(tag.get_text().split()).replace(" ", " ")
        if not text or LABEL.match(text):
            continue
        italics = [" ".join(i.get_text().split()) for i in tag.find_all("i") if i.get_text(strip=True)]
        italics += [" ".join(s.get_text().split()) for s in tag.find_all("span", class_="bolditalic")]
        if tag.name == "h2":
            kind = "title"
        elif classes & HEADING_CLASSES:
            kind = "heading"
        elif classes & LIST_CLASSES:
            kind = "item"
            text = re.sub(r"^■\s*", "", text)
            text = re.sub(r"^(\d+\.)\s*", r"\1 ", text)
        elif classes & {"di", "email", "emailm"}:
            kind = "quote"
        elif is_bold_only(tag) and not re.search(r"[a-z]", text):
            kind = "subheading"
        else:
            kind = "para"
        bolds = [] if kind in {"title", "heading", "subheading"} else [
            " ".join(b.get_text().split()) for b in tag.find_all("b")
            if b.get_text(strip=True) and not b.find_parent(class_="dropcap") and not re.fullmatch(r"\d+\.", b.get_text(strip=True))]
        units.append((kind, text, italics, bolds, notes))
    return units


def markdown_units(path):
    """[(kind, text, italics, bolds, notes)] for an en/ file: headings, paragraphs and list items."""
    tokens = MarkdownIt("commonmark").enable("table").parse(
        "\n".join(line for line in path.read_text().splitlines() if not re.match(r"^\[\^\w+\]:", line)))
    units, number, kind, quote = [], None, "para", False
    for token in tokens:
        if token.type == "heading_open":
            kind = {"h1": "title", "h2": "heading"}.get(token.tag, "subheading")
        elif token.type == "list_item_open":
            number = f"{token.info}. " if token.info else ""
        elif token.type == "blockquote_open":
            quote = True
        elif token.type == "blockquote_close":
            quote = False
        elif token.type == "inline":
            parts, italics, bolds, stack, notes = [], [], [], [], []
            for child in token.children:
                if child.type in ("text", "code_inline"):
                    for m in re.finditer(r"\[\^(\w+)\]", child.content):
                        notes.append((m[1], " ".join("".join(parts).split()[-6:])))
                    content = re.sub(r"\[\^\w+\]", "", child.content)
                    parts.append(content)
                    for opened in stack:
                        opened[1].append(content)
                elif "break" in child.type:
                    parts.append(" ")
                elif child.type in ("em_open", "strong_open"):
                    stack.append((child.type, []))
                elif child.type in ("em_close", "strong_close"):
                    opened = stack.pop()
                    (italics if opened[0] == "em_open" else bolds).append(" ".join("".join(opened[1]).split()))
            text = " ".join("".join(parts).split())
            this = "item" if number is not None else "quote" if quote else kind
            units.append((this, (number or "") + text, italics, bolds if this not in ("title", "heading", "subheading") else [], notes))
            number, kind = None, "para"
    return units


def word_diff(a, b):
    sm = difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        left, right = " ".join(a.split()[max(0, i1 - 3):i2 + 2]), " ".join(b.split()[max(0, j1 - 3):j2 + 2])
        out.append(f"      e-book: {left}\n      en/:    {right}")
    return out


# Fixes the first curation already made on purpose (review/source.md); the e-book has the same slips.
CURATED = [("http://info .blackswanltd.com", "http://info.blackswanltd.com"), ("the Counterfeit “Yes. “", "the Counterfeit “Yes.”")]


def typographic(text):
    """The e-book spaces its ellipses (". . .", ". . . ." at the end of a sentence); en/ has "…"."""
    text = re.sub(r"\. \. \. \.", ". …", text).replace(". . .", "…")
    text = re.sub(r"… \.", ". …", text)
    return re.sub(r"\s*…\s*", "…", text)


def kind_of_difference(a, b):
    for wrong, right in CURATED:
        a = a.replace(wrong, right)
    if a == b:
        return "curated"
    if typographic(a) == typographic(b):
        return "ellipsis"
    if a.lower() == b.lower():
        return "case"
    return "text"


def same(u, v):
    if u[0] == "title":
        return u[1].lower() == re.sub(r"^\d+\. ", "", v[1]).lower()
    if u[0] in ("heading", "subheading") or v[0] in ("heading", "subheading"):
        return u[1].lower() == v[1].lower()
    return u[1] == v[1]


def compare_section(name, source, target):
    """Print the block alignment of one section; return (changed pairs, missing in en/, extra in en/)."""
    sm = difflib.SequenceMatcher(None, [key(u[1]) for u in source],
                                 [key(re.sub(r"^\d+\. ", "", v[1]) if v[0] == "title" else v[1]) for v in target],
                                 autojunk=False)
    changed, missing, extra = [], [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            pairs = list(zip(range(i1, i2), range(j1, j2)))
        elif op == "replace" and i2 - i1 == j2 - j1:
            pairs = list(zip(range(i1, i2), range(j1, j2)))
        else:
            pairs = []
            missing += list(range(i1, i2))
            extra += list(range(j1, j2))
        for i, j in pairs:
            if not same(source[i], target[j]):
                changed.append((i, j))
    shapes = [(i, j) for op, i1, i2, j1, j2 in sm.get_opcodes() if op == "equal"
              for i, j in zip(range(i1, i2), range(j1, j2)) if source[i][0] != target[j][0]]
    for i, j in shapes:
        print(f"  kind differs: e-book block {i + 1} is {source[i][0]}, en/ unit {j + 1} is {target[j][0]}: {target[j][1][:60]}")
    kinds = {}
    for i, j in changed:
        kind = "case" if source[i][0] in ("title", "heading", "subheading") and typographic(source[i][1]).lower() == typographic(target[j][1]).lower() \
            else kind_of_difference(source[i][1], target[j][1])
        kinds.setdefault(kind, []).append(j + 1)
        if kind != "text":
            continue
        print(f"  changed: e-book block {i + 1} / en/ unit {j + 1} ({target[j][0]})")
        print("\n".join(word_diff(source[i][1], target[j][1])) or f"      e-book: {source[i][1][:100]}\n      en/:    {target[j][1][:100]}")
    for kind, label in (("ellipsis", "ellipsis style only (. . . / …)"), ("curated", "fixes the first curation made"), ("case", "case only (headings, names set in capitals)")):
        if kind in kinds:
            print(f"  {label}: en/ units {kinds[kind]}")
    for i in missing:
        print(f"  missing in en/: e-book block {i + 1} ({source[i][0]}): {source[i][1][:100]}")
    for j in extra:
        print(f"  extra in en/: unit {j + 1} ({target[j][0]}): {target[j][1][:100]}")
    for label, a, b in (("italic", 2, 2), ("bold", 3, 3)):
        left = [x for u in source for x in u[a]]
        right = [x for v in target for x in v[b]]
        if label == "bold" and key("".join(left)) == key("".join(right)):
            if len(left) != len(right):
                print(f"  bold: e-book {len(left)} runs, en/ {len(right)}; same words once adjacent runs are joined")
            continue
        if [key(x) for x in left] != [key(x) for x in right]:
            gone = sorted(set(left) - set(right))
            new = sorted(set(right) - set(left))
            print(f"  {label}: e-book {len(left)}, en/ {len(right)}; only in e-book {gone[:8]}; only in en/ {new[:8]}")
    return changed, missing, extra


def main(path, show_words=False):
    epub = zipfile.ZipFile(path)
    entries = toc(epub)
    config = (BOOK / "book.json").read_text()
    files = re.findall(r'"file": "([^"]+)"', config)
    ids = re.findall(r'"id": "([^"]+)"', config)
    print("sections of the e-book:")
    for label, file, anchor, subtitle in entries:
        print(f"  {label:70} {file}")
    print()
    chapter_entries = [e for e in entries if e[0].startswith("CHAPTER ")]
    by_label = {e[0]: e for e in entries}
    plan = [(f"ch{n:02d}", e) for n, e in enumerate(chapter_entries, 1)]
    for section, label in (("acknowledgments", "Acknowledgments"), ("appendix", "Appendix: Prepare a Negotiation One Sheet"),
                           ("about-the-authors", "About the Authors")):
        plan.append((section, by_label[label]))
    totals = [0, 0]
    figures = []
    for section, (label, file, anchor, subtitle) in plan:
        html = epub.read(file).decode()
        figures += [(label, m) for m in re.findall(r"<(?:img|table)\b[^>]*>", html)]
        source = [u for u in epub_units(html) if not u[1].startswith(ADVERTISEMENT)]
        if [u[0] for u in source[:2]] == ["title", "title"]:  # APPENDIX / PREPARE A NEGOTIATION ONE SHEET
            source[:2] = [("title", f"{source[0][1]}: {source[1][1]}", [], [], [])]
        if subtitle:
            source.insert(1, ("para", subtitle, [subtitle], [], []))
        name = files[ids.index(section)] if section in ids else None
        print(f"== {section}: {label} -> {name or 'not in en/'}")
        if name is None:
            print(f"  {len(source)} blocks, {sum(len(words(u[1])) for u in source)} words")
            continue
        target = markdown_units(BOOK / "en" / name)
        changed, missing, extra = compare_section(section, source, target)
        sw, tw = sum(len(words(u[1])) for u in source), sum(len(words(re.sub(r'^\d+\. ', '', v[1]) if v[0] == 'title' else v[1])) for v in target)
        totals[0] += sw
        totals[1] += tw
        notes = [(n, b) for u in source for n, b in u[4]]
        md_notes = [(n, b) for v in target for n, b in v[4]]
        print(f"  blocks {len(source)}/{len(target)}; changed {len(changed)}, missing {len(missing)}, extra {len(extra)}")
        if notes or md_notes:
            print(f"  note markers: e-book {[n for n, _ in notes]}, en/ {[n for n, _ in md_notes]}")
            for n, before in notes:
                print(f"    {n}: ... {before}")
        if show_words:
            print(f"  words: e-book {sw}, en/ {tw}")
    print()
    print("figures and tables in the compared sections:", figures or "none")
    notes_html = epub.read(by_label["Notes"][1]).decode()
    soup = BeautifulSoup(notes_html, "html.parser")
    current, counts = None, {}
    for p in soup.find_all("p", class_=["notes", "notes1"]):
        text = " ".join(p.get_text().split())
        if p.find("b") and not re.match(r"^\d+\.", text):
            current = text
            counts[current] = 0
        else:
            counts[current] += 1
    print("Notes section:", "; ".join(f"{k} {v}" for k, v in counts.items()))
    if show_words:
        print(f"words in the compared sections: e-book {totals[0]}, en/ {totals[1]}")


if __name__ == "__main__":
    main(sys.argv[1], "--words" in sys.argv[2:])
