"""Build the reader's full-text search index; the browser downloads it only when someone searches."""

import json
import re

MARKER = re.compile(r"\[\^\w+\]")


def plain(text):
    return " ".join(MARKER.sub("", text or "").split())


def sections(chapter):
    """Yield (title, anchor, text) per h1 to h3 section; the title is the Chinese heading, the text holds both languages."""
    title, anchor, body = "", "", []
    for unit in chapter["units"]:
        if unit["kind"] == "heading" and unit["level"] <= 3:
            if body:
                yield title, anchor, "\n".join(body)
            title, anchor, body = plain(re.sub(r"^#+\s*", "", unit["target"] or unit["source"])), unit["anchor"], []
            body.append(plain(re.sub(r"^#+\s*", "", unit["source"])))
            continue
        for field in ("source", "target"):
            text = plain(unit.get(field))
            if text and unit["kind"] != "code":
                body.append(text)
    if body:
        yield title, anchor, "\n".join(body)


def build_index(out, manifest):
    """Write out/assets/search-index.json from the compiled chapters; return the number of sections."""
    entries = []
    for page in manifest["chapters"]:
        chapter = json.loads((out / page["content"]).read_text())
        for title, anchor, body in sections(chapter):
            entries.append({"route": page["route"], "chapter": page["title"], "title": title or page["title"], "anchor": anchor, "text": body})
    (out / "assets" / "search-index.json").write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")) + "\n")
    return len(entries)
