"""Clean up the English text right after importing the EPUB (see review/source.md for why each step exists).

    python3 scripts/site.py import-epub thinking-fast-and-slow book.epub --force
    uv run --project framework/tools python books/thinking-fast-and-slow/tools/curate_source.py

The EPUB is a Kindle conversion: part title pages, the copyright page and the print index come in as
sections, the asterisk footnotes sit in separate files with links pointing a little off target, and the
Appendix A references are a separate file. This script turns all of that into the book's own structure.
"""

import re
import shutil
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
EN = BOOK / "en"
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402

# Sections that are not part of the text to translate.
DROP = {
    "section-1": "cover image (used as the bookshelf cover instead)",
    "part-1": "part title page", "two-systems": "part title page",
    "part-2": "part title page", "heuristics-and-biases": "part title page",
    "part-3": "part title page", "overconfidence": "part title page",
    "part-4": "part title page", "choices": "part title page",
    "part-5": "part title page", "two-selves": "part title page",
    "also-by-daniel-kahneman": "list of the author's other books, garbled by the conversion",
    "index-59": "print index whose page numbers do not apply",
    "section-60": "copyright page",
    "section-61": "footnote, moved into chapter 5", "section-62": "footnote, moved into chapter 9",
    "section-63": "footnote, moved into chapter 9", "section-64": "footnote, moved into chapter 9",
    "section-65": "footnote, moved into chapter 9", "section-66": "footnote, moved into chapter 9",
    "section-67": "source note, moved into Appendix A", "section-68": "source note, moved into Appendix B",
    "section-69": "title page image",
}
# The importer names the Appendix A reference list "notes"; it moves into Appendix A as footnotes.
REFERENCES = "notes"
CROSS_LINK = re.compile(r"\[([^\]]+)\]\(index_split_\d+\.html#filepos\d+\)")
STAR = re.compile(r"\[\\\*\]\(index_split_\d+\.html#filepos\d+\)")


def note_text(key, chapters):
    """Body of a one-note section, without its back link."""
    text = (EN / chapters[key]["file"]).read_text()
    body = text.split("\n", 1)[1]
    return " ".join(STAR.sub("", body).split())


def main():
    config = book_config.load(BOOK)
    chapters = {c["id"]: c for c in config["chapters"]}
    if "dedication" in chapters:
        raise SystemExit("already curated")

    # Asterisk footnotes: the marker stays where the book has it; the note text comes from its own section.
    ch05 = EN / chapters["ch05"]["file"]
    text = ch05.read_text()
    assert len(STAR.findall(text)) == 1
    ch05.write_text(STAR.sub("[^1]", text).rstrip("\n") + f"\n\n[^1]: {note_text('section-61', chapters)}\n")
    ch09 = EN / chapters["ch09"]["file"]
    text = ch09.read_text()
    assert len(STAR.findall(text)) == 5  # five items of "Characteristics of System 1" share one note
    ch09.write_text(STAR.sub("[^1]", text).rstrip("\n") + f"\n\n[^1]: {note_text('section-62', chapters)}\n")

    # Appendices: the byline is a paragraph, the source note follows it, and Appendix A cites numbered references.
    references = (EN / chapters["notes"]["file"]).read_text()
    pairs = re.findall(r"^> > \[(\d+)\.\]\([^)]*\)\n\n(.+?)(?=\n\n> > \[|\Z)", references, flags=re.M | re.S)
    assert [int(n) for n, _ in pairs] == list(range(1, 26))
    for key, source in (("appendix-a-judgment-under", "section-67"), ("appendix-b-choices-values-and", "section-68")):
        path = EN / chapters[key]["file"]
        text = path.read_text()
        title, byline, rest = text.split("\n\n", 2)
        title = title.replace(" \\*", "")
        byline = "*" + byline.removeprefix("## ").strip() + "*"
        text = f"{title}\n\n{byline}\n\n*{note_text(source, chapters)}*\n\n{rest}"
        if key == "appendix-a-judgment-under":
            text = re.sub(r"\[(\d+)\]\(index_split_\d+\.html#filepos\d+\)", r"[^\1]", text)
            text = text.rstrip("\n") + "\n\n" + "\n".join(f"[^{n}]: {' '.join(body.split())}" for n, body in pairs) + "\n"
        path.write_text(text)

    # Drop what is not text to translate, then rename the dedication and the book's notes.
    references_entry = chapters[REFERENCES]
    kept = []
    for entry in config["chapters"]:
        if entry is references_entry or entry["id"] in DROP:
            (EN / entry["file"]).unlink()
        else:
            kept.append(entry)
    dedication = chapters["section-2"]
    (EN / dedication["file"]).write_text("# In Memory of Amos Tversky\n")
    dedication["id"] = "dedication"
    notes = chapters["index"]  # the importer took the label of the next contents entry
    renamed = notes["file"].replace("-index", "-notes")
    (EN / notes["file"]).rename(EN / renamed)
    notes.update({"id": "notes", "file": renamed})
    for entry in kept:
        path = EN / entry["file"]
        text = path.read_text()
        text = CROSS_LINK.sub(r"\1", text)             # links between sections of the EPUB: keep the words
        text = re.sub(r"^> > ", "> ", text, flags=re.M)  # the conversion nests every indented block twice
        path.write_text(text)
    config["chapters"] = kept

    # The cover image becomes the bookshelf cover; images no section uses are removed.
    images = EN / "images"
    (BOOK / "assets" / "images").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(images / "00022.jpg", BOOK / "assets" / "images" / "cover.jpg")
    config["cover"] = "assets/images/cover.jpg"
    used = set(re.findall(r"images/([\w.-]+)", "".join((EN / e["file"]).read_text() for e in config["chapters"])))
    for image in images.iterdir():
        if image.name not in used:
            image.unlink()
    book_config.save(BOOK, config)
    print(f"{len(config['chapters'])} sections kept, {len(used)} images in use")


if __name__ == "__main__":
    main()
