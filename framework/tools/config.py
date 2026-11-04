"""Read, check and write a book's book.json.

Fields of a bilingual book (reader "bilingual"):
  title, originalTitle, authors   shown on the bookshelf and in the reader
  summary, facts, cover           bookshelf card; cover is a path inside the built book (assets/images/...)
  page                            optional page details: description, shareTitle, shareDescription, themeColor, storageKey
  start                           chapter id the reader opens first (default: the first published chapter)
  chapterMaps                     true: every published numbered chapter needs assets/diagrams/chNN.json
  listed                          false hides the book from the bookshelf (default true)
  chapters                        reading order; each {"id", "number"?, "file", "status"}
                                  file is the same relative path under en/ and zh-cn/
                                  status: todo (English only), draft, review, done (published)
"""

import json
from pathlib import Path

STATUSES = ("todo", "draft", "review", "done")


def load(root):
    """Read and check book.json for a bilingual book."""
    root = Path(root)
    config = json.loads((root / "book.json").read_text())
    config.setdefault("id", root.resolve().name)
    for field in ("title", "originalTitle"):
        if not config.get(field):
            raise ValueError(f"book.json: {field} is required")
    seen = set()
    for entry in config.get("chapters", []):
        key, file = entry.get("id"), entry.get("file")
        if not key or not file:
            raise ValueError(f"book.json: every chapter needs an id and a file: {entry}")
        if key in seen:
            raise ValueError(f"book.json: duplicate chapter id {key}")
        seen.add(key)
        if entry.get("status") not in STATUSES:
            raise ValueError(f"book.json: {key}: status must be one of {', '.join(STATUSES)}")
        if entry.get("number") is not None and key != f"ch{entry['number']:02d}":
            raise ValueError(f"book.json: numbered chapters use ids like ch01: {key} has number {entry['number']}")
        if not (root / "en" / file).exists():
            raise ValueError(f"book.json: {key}: source file missing: en/{file}")
        if entry["status"] != "todo" and not (root / "zh-cn" / file).exists():
            raise ValueError(f"book.json: {key}: status {entry['status']} needs zh-cn/{file}")
    return config


def save(root, config):
    """Write book.json with one line per chapter, so the chapter list stays easy to read and to diff."""
    head = {key: value for key, value in config.items() if key not in ("id", "chapters")}
    text = json.dumps(head, ensure_ascii=False, indent=2)
    chapters = ",\n".join("    " + json.dumps(entry, ensure_ascii=False) for entry in config.get("chapters", []))
    text = text[:-2] + ',\n  "chapters": [\n' + chapters + ("\n" if chapters else "") + "  ]\n}\n"
    (Path(root) / "book.json").write_text(text)
