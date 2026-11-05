"""Finish the import of prepared.epub (see prepare_epub.py and review/source.md).

    uv run --project framework/tools python -I books/never-split-the-difference/tools/curate_source.py book.epub

- The EPUB's cover image becomes the bookshelf cover; the reader opens at chapter 1.
- The original EPUB (not the prepared copy) is recorded as the source, with the bookshelf facts.
- Checks that the import gave the ten chapters ch01 to ch10, each with a single level 1 heading.

The title page (an SVG wrapper around the cover image) has no text, so the importer already leaves it out;
the EPUB has no other sections to drop. Running it again changes nothing.
"""

import hashlib
import re
import sys
import zipfile
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK.parent.parent / "framework" / "tools"))
import config as book_config  # noqa: E402  (the framework's own book.json reader and writer)


def main(epub):
    config = book_config.load(BOOK)
    chapters = config["chapters"]
    expected = [f"ch{n:02d}" for n in range(1, 11)]
    if [c["id"] for c in chapters] != expected or [c.get("number") for c in chapters] != list(range(1, 11)):
        raise SystemExit(f"error: expected chapters ch01 to ch10, got {[c['id'] for c in chapters]}")
    for entry in chapters:
        text = (BOOK / "en" / entry["file"]).read_text()
        headings = re.findall(r"(?m)^# .*$", text)
        if len(headings) != 1 or not text.startswith(f"# {entry['number']}. "):
            raise SystemExit(f"error: {entry['file']}: level 1 headings {headings}")
    (BOOK / "assets" / "images" / "cover.jpg").write_bytes(zipfile.ZipFile(epub).read("cover.jpeg"))
    config["cover"] = "assets/images/cover.jpg"
    config["start"] = "ch01"
    config["facts"] = ["10 章", "中英逐段对照"]
    config["source"] = {"epub": Path(epub).name, "sha256": hashlib.sha256(Path(epub).read_bytes()).hexdigest()}
    book_config.save(BOOK, config)
    print(f"curated {len(chapters)} sections; cover and source recorded")


if __name__ == "__main__":
    main(sys.argv[1])
