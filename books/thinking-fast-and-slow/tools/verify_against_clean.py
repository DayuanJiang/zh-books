"""Compare every English block of the book with the clean text from the AZW3 file.

    uv run --project framework/tools python verify_against_clean.py <clean.epub> <report.json>

For each block of en/*.md (headings, paragraphs, lists, quotes, tables), find the clean paragraph(s) that
match it best and report blocks whose words differ. Only words are compared (case, punctuation, Markdown
and footnote markers are ignored), so the report lists text differences such as garbled words.
"""

import difflib
import json
import re
import sys
import zipfile
from pathlib import Path

from bs4 import BeautifulSoup

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import book  # noqa: E402
import config as book_config  # noqa: E402


def words(text):
    text = re.sub(r"\[\^\w+\]", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    return re.findall(r"[a-z0-9]+(?:['’][a-z]+)?", text.lower().replace("’", "'"))


def clean_paragraphs(path):
    """Word lists of the clean book's paragraphs, headings, list items and quotes, in reading order."""
    archive = zipfile.ZipFile(path)
    opf_name = next(n for n in archive.namelist() if n.endswith(".opf"))
    opf = archive.read(opf_name).decode()
    base = str(Path(opf_name).parent)
    items = dict(re.findall(r'<item[^>]*?id="([^"]+)"[^>]*?href="([^"]+)"', opf))
    items.update({i: h for h, i in re.findall(r'<item[^>]*?href="([^"]+)"[^>]*?id="([^"]+)"', opf)})
    out = []
    for idref in re.findall(r'<itemref[^>]*idref="([^"]+)"', opf):
        name = (base + "/" if base not in ("", ".") else "") + items[idref]
        soup = BeautifulSoup(archive.read(name), "html.parser")
        for tag in soup.find_all(["p", "h1", "h2", "h3", "h4", "li", "td", "blockquote", "div"]):
            if tag.find(["p", "h1", "h2", "h3", "h4", "li", "blockquote", "div", "table"]):
                continue  # only innermost text blocks
            w = words(tag.get_text(" "))
            if w:
                out.append(w)
    return out


def main():
    clean = clean_paragraphs(sys.argv[1])
    flat, starts = [], []
    for para in clean:
        starts.append(len(flat))
        flat.extend(para)
    config = book_config.load(BOOK)
    report = []
    cursor = 0
    for entry in config["chapters"]:
        blocks, notes = book.parse((BOOK / "en" / entry["file"]).read_text())
        for index, block in enumerate(blocks, 1):
            if block.kind in ("image", "code", "rule", "html"):
                continue
            w = words(block.raw)
            if len(w) < 3:
                continue
            # Locate the block in the clean word stream: exact search near the cursor first, then fuzzy.
            needle = " ".join(w[:8])
            window = " ".join(flat[max(0, cursor - 2000):cursor + 60000])
            pos = window.find(needle)
            if pos >= 0:
                start = max(0, cursor - 2000) + len(window[:pos].split())
            else:
                matcher = difflib.SequenceMatcher(None, flat[cursor:cursor + 20000], w[:40], autojunk=False)
                m = matcher.find_longest_match(0, min(20000, len(flat) - cursor), 0, min(40, len(w)))
                start = cursor + m.a - m.b if m.size >= 5 else None
            if start is None:
                report.append({"chapter": entry["id"], "block": index, "kind": block.kind, "status": "not found",
                               "book": " ".join(w)[:300]})
                continue
            candidate = flat[start:start + len(w) + 20]
            matcher = difflib.SequenceMatcher(None, w, candidate, autojunk=False)
            ops = [op for op in matcher.get_opcodes() if op[0] != "equal"]
            # Trailing words of the candidate beyond the block are not a difference.
            if ops and ops[-1][0] == "insert" and ops[-1][1] == len(w):
                ops = ops[:-1]
            if ops:
                diffs = [{"op": tag, "book": " ".join(w[i1:i2]), "clean": " ".join(candidate[j1:j2])} for tag, i1, i2, j1, j2 in ops]
                report.append({"chapter": entry["id"], "block": index, "kind": block.kind, "status": "differs", "diffs": diffs})
            cursor = start + len(w)
    Path(sys.argv[2]).write_text(json.dumps(report, ensure_ascii=False, indent=1))
    by_chapter = {}
    for r in report:
        by_chapter.setdefault(r["chapter"], [0, 0])
        by_chapter[r["chapter"]][0 if r["status"] == "differs" else 1] += 1
    print(f"{sum(v[0] for v in by_chapter.values())} blocks differ, {sum(v[1] for v in by_chapter.values())} not found")
    print(", ".join(f"{k}:{v[0]}/{v[1]}" for k, v in by_chapter.items()))


if __name__ == "__main__":
    main()
