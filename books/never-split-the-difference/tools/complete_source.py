"""Bring en/ up to date with the complete HarperCollins e-book (see review/source.md, 用更好的来源补全).

    uv run --project framework/tools python -I books/never-split-the-difference/tools/complete_source.py new.epub

What compare_source.py found, applied to en/ and book.json:

- Four words the first EPUB's conversion had joined or lost a hyphen in ("punchin-the-face", "shootout",
  "recenter", "deal-and concession-making") are written as the e-book has them.
- The 23 notes: the e-book marks them with superscript numbers in the chapters and lists them by chapter
  in its Notes section, so each becomes a footnote [^n] at the same place, with the same number, and its
  definition at the end of the chapter's file. Two slips in the notes are fixed: a stray space in a URL
  (the same printing break as the URL in chapter 9) and "Don‘t" typed with an opening quotation mark.
- Three new sections in reading order after chapter 10: Acknowledgments, the appendix Prepare a
  Negotiation One Sheet and About the Authors, converted the way prepare_epub.py converts the chapters
  (headings in title case, list items as a list, the drop cap as a plain letter). The last line of About
  the Authors, an advertisement for hc.com, is left out.
- Left out like before: cover, dedication, contents, index, credits, copyright, About the Publisher and
  the Bookperk advertisement.

A new section enters book.json as todo until its zh-cn/ file exists, then as review. Running it again
changes nothing. The Chinese side (zh-cn/) is edited by hand.
"""

import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK.parent.parent / "framework" / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as book_config  # noqa: E402
from prepare_epub import title_case  # noqa: E402

CHAPTERS = {n: name for n, name in enumerate([
    "01-1-the-new-rules.md", "02-2-be-a-mirror.md", "03-3-don-t-feel-their-pain-label-it.md",
    "04-4-beware-yes-master-no.md", "05-5-trigger-the-two-words-that.md", "06-6-bend-their-reality.md",
    "07-7-create-the-illusion-of-control.md", "08-8-guarantee-execution.md", "09-9-bargain-hard.md",
    "10-10-find-the-black-swan.md"], 1)}
TEXT_FIXES = [
    (6, "the real deal-and concession-making", "the real deal- and concession-making"),
    (9, "respond to a punchin-the-face anchor", "respond to a punch-in-the-face anchor"),
    (10, "and have a shootout with him in the parking lot", "and have a shoot-out with him in the parking lot"),
    (10, "time to think and recenter themselves", "time to think and re-center themselves"),
]
# (chapter, note number, the en/ text the e-book's superscript follows); each anchor occurs once in its file.
NOTE_ANCHORS = [
    (1, 1, "*Bargaining with the Devil: When to Negotiate, When to Fight*."),
    (1, 2, "came out with *Getting to Yes*,"),
    (1, 3, "the 2011 bestseller *Thinking, Fast and Slow*."),
    (1, 4, "“Lessons of Waco: Proposed Changes in Federal Law Enforcement,”"),
    (2, 1, "In one of the most cited research papers in psychology,"),
    (3, 1, "In an fMRI brain-scan experiment,"),
    (3, 2, "In one brain imaging study,"),
    (4, 1, "in his excellent book, *Start with NO*,"),
    (6, 1, "In his bestselling 1980 book, *You Can Negotiate Anything*,"),
    (6, 2, "In *Descartes’ Error: Emotion, Reason, and the Human Brain*,"),
    (6, 3, "I stumbled upon the book *How to Become a Rainmaker*,"),
    (6, 4, "In a recent study,"),
    (7, 1, "says in his book *Split-Second Persuasion*."),
    (7, 2, "I read this great article in the *New York Times*"),
    (8, 1, "In two famous studies on what makes us like or dislike somebody,"),
    (8, 2, "In a study of the components of lying,"),
    (9, 1, "A study of American lawyer-negotiators"),
    (9, 2, "increase a negotiator’s advantage and final take."),
    (9, 3, "even when the counterpart didn’t think so."),
    (10, 1, "*Fooled by Randomness* (2001)"),
    (10, 2, "*The Black Swan* (2007),"),
    (10, 3, "In a famous study from the late 1970s,"),
    (10, 4, "In their great book *Negotiation Genius*,"),
]
NOTE_FIXES = [("http://well.blogs.nytimes.com /2014", "http://well.blogs.nytimes.com/2014"),  # stray space
              ("Pros Don‘t Want", "Pros Don’t Want")]  # opening quotation mark for the apostrophe
NEW_SECTIONS = [  # (id, file, e-book file, h1)
    ("acknowledgments", "11-acknowledgments.md", "text/part0013.html", "Acknowledgments"),
    ("appendix", "12-appendix-prepare-a-negotiation.md", "text/part0014.html", "Appendix: Prepare a Negotiation One Sheet"),
    ("about-the-authors", "13-about-the-authors.md", "text/part0017.html", "About the Authors"),
]
LEFT_OUT = "Discover great authors, exclusive offers, and more at"  # publisher advertisement
ROMAN = re.compile(r"\b(Ii|Iii|Iv|V|I)\b(?=:)")
# Where prepare_epub.title_case misses Chicago style: the word after a slash, and a compound adjective.
HEADING_FIXES = [("Labels/accusation", "Labels/Accusation"), ("Identify behind-the-Table", "Identify Behind-the-Table")]


def heading_case(text):
    text = ROMAN.sub(lambda m: m[1].upper(), title_case(text))
    for wrong, right in HEADING_FIXES:
        text = text.replace(wrong, right)
    return text


def inline(tag):
    """Markdown for the inline content of a tag: <i> -> *…*, <b> -> **…**, spacing outside the markers."""
    out = []
    for node in tag.children:
        if getattr(node, "name", None) in ("i", "b"):
            text = inline(node)
            mark = "*" if node.name == "i" else "**"
            core = text.strip()
            if core:
                lead, tail = text[:len(text) - len(text.lstrip())], text[len(text.rstrip()):]
                out.append(f"{lead}{mark}{core}{mark}{tail}")
            else:
                out.append(text)
        elif getattr(node, "name", None) is not None:
            out.append(inline(node))
        else:
            out.append(str(node))
    return "".join(out)


def clean(soup):
    for hidden in soup.find_all(class_=["hide1"]):
        hidden.decompose()
    for cap in soup.find_all("span", class_="dropcap"):
        cap.replace_with(cap.get_text())
    for page in soup.find_all("span", attrs={"epub:type": "pagebreak"}):
        page.decompose()
    return soup


def text_of(tag):
    return " ".join(inline(tag).replace(" ", " ").split())


def section_markdown(html, title):
    """The Markdown of a back matter section of the e-book."""
    body = clean(BeautifulSoup(html, "html.parser")).body
    blocks, items = [f"# {title}"], []
    for tag in body.find_all(["h2", "p"]):
        classes = set(tag.get("class") or [])
        text = text_of(tag)
        if tag.name == "h2" or not text or text.startswith(LEFT_OUT):
            continue
        if "bl" in classes:
            items.append("- " + re.sub(r"^■\s*", "", text))
            continue
        if items:
            blocks.append("\n".join(items))
            items = []
        plain = tag.get_text(" ", strip=True)
        bold_only = text.startswith("**") and text.endswith("**") and text.count("**") == 2
        if "head" in classes:
            blocks.append("## " + heading_case(plain))
        elif bold_only and not re.search(r"[a-z]", plain):
            blocks.append("### " + heading_case(plain))
        else:
            # Names set in bold capitals at the start of About the Authors: the capitals are only typography.
            text = re.sub(r"^\*\*([A-Z][A-Z ]+)\*\*", lambda m: f"**{m[1].title()}**", text)
            blocks.append(text)
    if items:
        blocks.append("\n".join(items))
    return "\n\n".join(blocks) + "\n"


def notes_by_chapter(html):
    """{chapter number: [note Markdown]} from the e-book's Notes section."""
    body = clean(BeautifulSoup(html, "html.parser")).body
    notes, chapter = {}, None
    for p in body.find_all("p", class_=["notes", "notes1"]):
        text = text_of(p)
        heading = re.match(r"^\*\*CHAPTER (\d+):", text)
        if heading:
            chapter = int(heading[1])
            notes[chapter] = []
            continue
        number, note = re.match(r"^(\d+)\.\s*(.*)$", text).groups()
        for wrong, right in NOTE_FIXES:
            note = note.replace(wrong, right)
        notes[chapter].append(note)
        if int(number) != len(notes[chapter]):
            raise SystemExit(f"error: chapter {chapter}: note {number} out of order")
    return notes


def add_notes(text, chapter, notes):
    for _, number, anchor in (a for a in NOTE_ANCHORS if a[0] == chapter):
        marker = f"[^{number}]"
        if anchor + marker in text:
            continue
        if text.count(anchor) != 1:
            raise SystemExit(f"error: chapter {chapter}: anchor for note {number} found {text.count(anchor)} times")
        text = text.replace(anchor, anchor + marker)
    definitions = [f"[^{k}]: {note}" for k, note in enumerate(notes.get(chapter, []), 1)]
    missing = [d for d in definitions if d not in text]
    if missing:
        text = text.rstrip("\n") + "\n\n" + "\n\n".join(missing) + "\n"
    return text


def main(epub_path):
    epub = zipfile.ZipFile(epub_path)
    notes = notes_by_chapter(epub.read("text/part0015.html").decode())
    if sum(len(v) for v in notes.values()) != len(NOTE_ANCHORS):
        raise SystemExit("error: notes and anchors differ")
    for chapter, name in CHAPTERS.items():
        path = BOOK / "en" / name
        text = original = path.read_text()
        for c, wrong, right in TEXT_FIXES:
            if c == chapter and right not in text:
                if text.count(wrong) != 1:
                    raise SystemExit(f"error: {name}: {wrong!r} found {text.count(wrong)} times")
                text = text.replace(wrong, right)
        text = add_notes(text, chapter, notes)
        if text != original:
            path.write_text(text)
            print(f"updated en/{name}")
    for section, name, file, title in NEW_SECTIONS:
        path = BOOK / "en" / name
        text = section_markdown(epub.read(file).decode(), title)
        if not path.exists() or path.read_text() != text:
            path.write_text(text)
            print(f"wrote en/{name}")
    # Read book.json directly: book_config.load rejects a review entry whose zh-cn/ file is not written yet.
    config = json.loads((BOOK / "book.json").read_text())
    known = {c["id"] for c in config["chapters"]}
    for section, name, file, title in NEW_SECTIONS:
        if section not in known:
            status = "review" if (BOOK / "zh-cn" / name).exists() else "todo"
            config["chapters"].append({"id": section, "file": name, "status": status})
    config["facts"] = ["10 章与附录", "中英逐段对照", "23 条注释"]
    config["source"] = {"epub": Path(epub_path).name, "sha256": hashlib.sha256(Path(epub_path).read_bytes()).hexdigest()}
    book_config.save(BOOK, config)
    print(f"book.json: {len(config['chapters'])} sections")


if __name__ == "__main__":
    main(sys.argv[1])
