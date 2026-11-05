"""Make a copy of the EPUB that the importer can turn into this book's structure (see review/source.md).

    uv run --project framework/tools python -I books/checklist-manifesto/tools/prepare_epub.py book.epub prepared.epub
    python3 scripts/site.py import-epub checklist-manifesto prepared.epub --force
    uv run --project framework/tools python -I books/checklist-manifesto/tools/curate_source.py book.epub

What a plain import loses or gets wrong in this EPUB:
- Titles are paragraphs with class h9 (chapters) and h6 (chapter groups in the notes), so they become <h1> and <h2>.
  The h9 titles also carry a link back to the contents page, which is dropped.
- Quoted cockpit voice recordings are <div class="ext">, so they become <blockquote>.
- A section inside a chapter opens with a "tx1" paragraph whose first words are bold (small capitals in print).
  The bold is dropped and a rule is put before the paragraph, except at the opening of a chapter ("sgc-11").
- Italic titles are often split in two (<i>New England</i> <i>Journal</i>); the pieces are joined.
- The links in the notes have wrong targets (trailing periods, a "%20", a lone "http://"); they become plain text.
"""

import re
import sys
import zipfile

from bs4 import BeautifulSoup

NOTES = "OEBPS/text/content020.xhtml"


def prepare(html, name, counts):
    html = re.sub(r"</i>(\s*)<i>", r"\1", html)
    soup = BeautifulSoup(html, "html.parser")
    for p in soup.find_all("p", class_="h9"):
        p.string = p.get_text(" ", strip=True)
        p.name, p.attrs = "h1", {}
        counts["titles"] += 1
    for p in soup.find_all("p", class_="h6"):
        p.name, p.attrs = "h2", {}
        counts["note groups"] += 1
    for div in soup.find_all("div", class_="ext"):
        div.name, div.attrs = "blockquote", {}
        counts["quotes"] += 1
    for p in soup.find_all("p", class_="tx1"):
        first = next((c for c in p.contents if not (isinstance(c, str) and not c.strip())), None)
        if getattr(first, "name", None) != "b":
            continue
        first.unwrap()
        counts["bold openings"] += 1
        if "sgc-11" not in p["class"]:
            p.insert_before(soup.new_tag("hr"))
            counts["section breaks"] += 1
    if name == NOTES:
        for a in soup.find_all("a"):
            a.unwrap()
    return str(soup)


def main(source, target):
    epub = zipfile.ZipFile(source)
    counts = dict.fromkeys(["titles", "note groups", "quotes", "bold openings", "section breaks"], 0)
    with zipfile.ZipFile(target, "w") as out:
        for info in epub.infolist():
            data = epub.read(info.filename)
            if info.filename.endswith(".xhtml") and info.filename != "OEBPS/text/content001.xhtml":
                data = prepare(data.decode(), info.filename, counts).encode()
            kind = zipfile.ZIP_STORED if info.filename == "mimetype" else zipfile.ZIP_DEFLATED
            out.writestr(info, data, compress_type=kind)
    print(f"{counts} -> {target}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
