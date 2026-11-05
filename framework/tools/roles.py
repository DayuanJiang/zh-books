"""List the whole-italic paragraphs whose role the rules cannot settle, for a model or a person to judge.

    python3 scripts/site.py roles <book>          # JSON on stdout: the open cases with their context
    python3 scripts/site.py roles <book> --all    # also the cases already judged in roles.json

The rules in book.roles() settle a whole-italic paragraph right under the title of a numbered chapter: one
phrase is the chapter subtitle, full sentences are the chapter lead. Every other whole-italic paragraph is
listed here. Write the decisions to roles.json in the book folder:

    {"<unit id>": {"role": "chapter-subtitle" | "chapter-lead" | "plain" | "subheading" | null, "why": "..."}}

chapter-subtitle keeps the emphasis and is set like a subtitle; chapter-lead and plain show the text without
emphasis (a lead in the muted color); subheading is a short heading-like line; null is an ordinary paragraph
whose italics stay emphasis.
"""

import json
import sys
from pathlib import Path

import book
import config as book_config
import reader_data


def cases(root, include_judged=False):
    config = book_config.load(root)
    judged = reader_data.judged_roles(root)
    out = []
    for entry in config["chapters"]:
        zh = root / "zh-cn" / entry["file"]
        if not zh.exists():
            continue
        chapter = book.compile_chapter(entry["id"], (root / "en" / entry["file"]).read_text(), zh.read_text(), "en", partial=True)
        units = chapter["units"]
        for index, unit in enumerate(units):
            if unit["kind"] != "paragraph" or not book.WHOLE_ITALIC.fullmatch(unit["source"].strip()):
                continue
            if unit["role"] in ("credit", "attribution", "caption", "code-label", "epigraph") and unit["id"] not in judged:
                continue  # these roles come from what the paragraph says, not from its italics
            settled = unit["role"] in ("chapter-subtitle", "chapter-lead") and entry.get("number")
            if settled or (unit["id"] in judged and not include_judged):
                continue
            around = [u for u in units[max(0, index - 2):index + 3] if u is not unit]
            out.append({"id": unit["id"], "chapter": entry["id"], "numbered": bool(entry.get("number")),
                        "rule": unit["role"], "judged": judged.get(unit["id"], "(not judged)"),
                        "english": unit["source"], "chinese": unit["target"],
                        "context": [{"kind": u["kind"], "english": (u["source"] or "")[:200]} for u in around]})
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if len(args) != 1:
        raise SystemExit(__doc__)
    print(json.dumps(cases(Path(args[0]), "--all" in sys.argv), ensure_ascii=False, indent=1))
