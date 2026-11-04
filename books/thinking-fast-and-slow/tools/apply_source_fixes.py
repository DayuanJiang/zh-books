"""Repair garbled passages of the EPUB text listed in source_fixes.json (run after curate_source.py).

Each fix replaces one exact passage in one chapter. A fix whose passage is already repaired is skipped,
so the script can run again; a passage found neither way is an error.
"""

import json
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import config as book_config  # noqa: E402


def main():
    files = {c["id"]: BOOK / "en" / c["file"] for c in book_config.load(BOOK)["chapters"]}
    fixes = json.loads((Path(__file__).with_name("source_fixes.json")).read_text())
    applied = skipped = 0
    for fix in fixes:
        path = files[fix["chapter"]]
        text = path.read_text()
        if text.count(fix["before"]) == 1:
            path.write_text(text.replace(fix["before"], fix["after"]))
            applied += 1
        elif fix["before"] not in text and fix["after"] in text:
            skipped += 1
        else:
            raise SystemExit(f"{fix['chapter']}: passage not found exactly once: {fix['before']!r}")
    print(f"{applied} fixes applied, {skipped} already in place, {len(fixes)} listed")


if __name__ == "__main__":
    main()
