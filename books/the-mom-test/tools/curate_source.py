"""Finish the import of prepared.epub (see prepare_epub.py and review/source.md).

    uv run --project framework/tools python -I books/the-mom-test/tools/curate_source.py "Fitzpatrick - The Mom Test.epub"

- Short ids for the sections around the chapters, the first section to open, the bookshelf facts, and the
  original EPUB (not the prepared copy) as the recorded source.
- The cheat sheet's "process before, during and after the meeting" is three lists in a row. Markdown joins
  lists that follow each other when they use the same marker, so the middle one is written with "*".
- One italic that took in the closing parenthesis, "(*pedestal)*", becomes "(*pedestal*)".

Running it again changes nothing.
"""

import hashlib
import re
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BOOK.parent.parent / "framework" / "tools"))
import config as book_config  # noqa: E402  (the framework's own book.json reader and writer)

IDS = {"conclusion-and-cheatsheet": "conclusion", "acknowledgements": "acknowledgments"}
FIXES = {"07-6-finding-conversations.md": [("(*pedestal)*…", "(*pedestal*)…")]}
PROCESS = "**The process before, during and after the meeting:**"


def split_process_lists(text):
    """Write the second of the three lists after PROCESS with "*" so the three stay separate."""
    head, found, rest = text.partition(PROCESS + "\n\n")
    if not found:
        raise SystemExit("error: cheat sheet process lists not found")
    lists = rest.split("\n\n", 3)
    lists[1] = re.sub(r"^- ", "* ", lists[1], flags=re.M)
    return head + found + "\n\n".join(lists)


def main(epub):
    config = book_config.load(BOOK)
    for entry in config["chapters"]:
        entry["id"] = IDS.get(entry["id"], entry["id"])
    config["start"] = "introduction"
    config["facts"] = ["引言、8 章与结语", "中英逐段对照"]
    config["source"] = {"epub": Path(epub).name, "sha256": hashlib.sha256(Path(epub).read_bytes()).hexdigest()}
    book_config.save(BOOK, config)

    for name, fixes in FIXES.items():
        path = BOOK / "en" / name
        text = path.read_text()
        for old, new in fixes:
            text = text.replace(old, new)
        path.write_text(text)
    path = BOOK / "en" / "10-conclusion-and-cheatsheet.md"
    path.write_text(split_process_lists(path.read_text()))
    print(f"curated {len(config['chapters'])} sections")


if __name__ == "__main__":
    main(sys.argv[1])
