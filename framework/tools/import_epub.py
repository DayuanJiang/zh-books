"""Import an EPUB into a book: one English Markdown file per section under en/, listed in book.json as "todo".

    uv run --project framework/tools python framework/tools/import_epub.py books/<id> path/to/book.epub

- Reading order comes from the EPUB spine. Titles come from the table of contents (nav.xhtml or toc.ncx),
  otherwise from the first heading. Sections without any text (cover pages, the table of contents) are skipped.
- Each section becomes en/NN-<slug>.md, starting with a level 1 heading; images are copied to en/images/.
- Footnotes and endnotes become [^n] markers with [^n]: definitions in the section that cites them. Notes are
  found through epub:type (noteref, footnote, endnote) or role (doc-noteref, doc-footnote, doc-endnote) markup.
- A title that starts with a number ("7 A Machine for Jumping to Conclusions", "Chapter 7") gives the
  section a "number" and an id like ch07; other sections get an id from their title.

The output is a first draft of the source text. Compare it with the EPUB before translating: EPUB markup varies
a lot, and the importer cannot know which sections belong to the book you mean to publish.
"""

import argparse
import hashlib
import posixpath
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote
import xml.etree.ElementTree as ET
import zipfile

from bs4 import BeautifulSoup
from markdownify import markdownify

import config as book_config

NS = {"c": "urn:oasis:names:tc:opendocument:xmlns:container", "opf": "http://www.idpf.org/2007/opf",
      "ncx": "http://www.daisy.org/z3986/2005/ncx/"}
NOTE_TYPES = {"footnote", "endnote", "rearnote", "note"}
NOTE_ROLES = {"doc-footnote", "doc-endnote"}
NUMBERED = re.compile(r"^(?:chapter\s+(\d{1,3}|[ivxlc]+)|(\d{1,3}))(?=$|[\s.:：、—\[-])", re.I)
NOTE_TEXT = re.compile(r"^[\[(]?(\d{1,3}|[*†‡§])[\])]?$")
ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100}
MARK = "ZZNOTEREF{}ZZ"


def chapter_number(title):
    """7 for "7 A Machine for Jumping to Conclusions", "Chapter 7" or "CHAPTER VII. ..."; None otherwise."""
    match = NUMBERED.match(title)
    if not match:
        return None
    value = match[1] or match[2]
    if value.isdigit():
        return int(value)
    digits = [ROMAN[c] for c in value.lower()]
    return sum(-d if i + 1 < len(digits) and d < digits[i + 1] else d for i, d in enumerate(digits))


def types(tag):
    return set((tag.get("epub:type") or "").split()) | set((tag.get("role") or "").split())


def slug(text, limit=32):
    """ASCII words joined by hyphens, cut at a word boundary."""
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(value) > limit:
        value = value[:limit].rsplit("-", 1)[0]
    return value


class Epub:
    def __init__(self, path):
        self.zip = zipfile.ZipFile(path)
        container = ET.fromstring(self.zip.read("META-INF/container.xml"))
        self.opf_path = container.find(".//c:rootfile", NS).get("full-path")
        self.base = posixpath.dirname(self.opf_path)
        opf = ET.fromstring(self.zip.read(self.opf_path))
        self.items = {}
        for item in opf.find("opf:manifest", NS):
            self.items[item.get("id")] = {"href": self.resolve(self.base, item.get("href")),
                                          "type": item.get("media-type"), "properties": item.get("properties", "")}
        self.spine = [self.items[ref.get("idref")]["href"] for ref in opf.find("opf:spine", NS)
                      if ref.get("linear", "yes") != "no"]
        self.toc_id = opf.find("opf:spine", NS).get("toc")
        self.nav = next((i["href"] for i in self.items.values() if "nav" in i["properties"].split()), None)
        self.titles = self.read_toc()
        self.labels = list(dict.fromkeys(self.titles_in_order))

    @staticmethod
    def resolve(base, href):
        return posixpath.normpath(posixpath.join(base, unquote(href.split("#")[0])))

    def soup(self, name):
        return BeautifulSoup(self.zip.read(name), "html.parser")

    def toc_target(self, base, href):
        """The spine document a table-of-contents link opens.

        Books converted from Kindle files often put the anchor at the very end of the previous document;
        when no text follows the anchor there, the entry belongs to the next document.
        """
        name, fragment = self.resolve(base, href), href.partition("#")[2]
        if not fragment or name not in self.spine:
            return name
        anchor = self.soup(name).find(id=fragment)
        if anchor is None or any(s.strip() for s in anchor.find_all_next(string=True)):
            return name
        index = self.spine.index(name)
        return self.spine[index + 1] if index + 1 < len(self.spine) else name

    def read_toc(self):
        """First table-of-contents label for each document (and every label in reading order)."""
        titles = {}
        self.titles_in_order = []
        nav = next((i for i in self.items.values() if "nav" in i["properties"].split()), None)
        if nav:
            page = self.soup(nav["href"])
            toc = next((n for n in page.find_all("nav") if "toc" in types(n)), page.find("nav"))
            for link in (toc.find_all("a", href=True) if toc else []):
                target = self.toc_target(posixpath.dirname(nav["href"]), link["href"])
                titles.setdefault(target, " ".join(link.get_text(" ").split()))
                self.titles_in_order.append(" ".join(link.get_text(" ").split()))
        elif self.toc_id and self.toc_id in self.items:
            ncx_path = self.items[self.toc_id]["href"]
            ncx = ET.fromstring(self.zip.read(ncx_path))
            for point in ncx.iter(f"{{{NS['ncx']}}}navPoint"):
                label = point.find("ncx:navLabel/ncx:text", NS)
                content = point.find("ncx:content", NS)
                if label is not None and content is not None:
                    target = self.toc_target(posixpath.dirname(ncx_path), content.get("src"))
                    titles.setdefault(target, " ".join((label.text or "").split()))
                    self.titles_in_order.append(" ".join((label.text or "").split()))
        return titles


def block_of(tag):
    return tag.find_parent(["p", "li", "aside", "div", "dd", "td"]) or tag


def starts_block(link):
    """True when the link opens its block and text follows it: the shape of a note body, unlike a reference in running text."""
    block = block_of(link)
    text, own = " ".join(block.get_text(" ").split()), " ".join(link.get_text(" ").split())
    return text.startswith(own) and len(text) > len(own) + 1


def bold_only(tag):
    """A short paragraph whose whole text is bold: how books converted from Kindle files mark headings."""
    text = " ".join(tag.get_text(" ").split())
    if not text or len(text) > 100 or text[-1] in ".,;:":
        return False
    for piece in tag.find_all(string=True):
        if not piece.strip():
            continue
        parent, bold = piece.parent, False
        while parent is not None and parent is not tag.parent:
            classes = " ".join(parent.get("class") or [])
            if parent.name in ("b", "strong") or "bold" in classes or "bold" in (parent.get("style") or ""):
                bold = True
                break
            parent = parent.parent
        if not bold:
            return False
    return True


def note_body(tag):
    """The element that holds a note's text: the target itself, or its block parent when the target is an empty anchor."""
    if tag.name == "a" and not tag.get_text(strip=True):
        return tag.find_parent(["p", "li", "aside", "div"]) or tag
    return tag


def inline_markdown(tag):
    """Markdown of a note body on one line, without the leading number or back link."""
    for link in tag.find_all("a"):
        text = link.get_text(strip=True)
        if re.fullmatch(r"[\[(]?\d+[\])]?\.?|↩|↑|\^", text or ""):
            link.decompose()
    text = markdownify(str(tag), heading_style="ATX", bullets="-")
    text = " ".join(text.split())
    return re.sub(r"^\d+[.)]?\s+", "", text)


def plain_title(text):
    """Lowercase title without a leading chapter number, for matching headings with table-of-contents labels."""
    text = " ".join(re.sub(r"[\\*]+", " ", text).replace("’", "'").replace("‘", "'").lower().split())
    return re.sub(r"^(?:chapter\s+)?(?:\d{1,3}|[ivxlc]+)[.:]?\s+", "", text)


def import_epub(root, epub_path, force=False):
    root, epub_path = Path(root), Path(epub_path)
    config = book_config.load(root)
    if config.get("chapters") and not force:
        raise ValueError("book.json already lists chapters; use --force to import again and replace them")
    for entry in config.get("chapters", []):
        if entry["status"] != "todo":
            raise ValueError(f"{entry['id']} is already being translated; move zh-cn/ away before importing again")
        (root / "en" / entry["file"]).unlink(missing_ok=True)
    if (root / "en" / "images").is_dir():
        shutil.rmtree(root / "en" / "images")
    epub = Epub(epub_path)
    pages = {name: epub.soup(name) for name in epub.spine}

    # Note bodies anywhere in the book, by (document, id).
    bodies = {}
    for name, page in pages.items():
        for tag in page.find_all(id=True):
            if types(tag) & (NOTE_TYPES | NOTE_ROLES):
                bodies[(name, tag["id"])] = tag
    for name, page in pages.items():
        for link in page.find_all("a", href=True):
            if "noteref" in types(link) or "doc-noteref" in types(link):
                target_name = epub.resolve(posixpath.dirname(name), link["href"]) if not link["href"].startswith("#") else name
                fragment = link["href"].partition("#")[2]
                target = pages.get(target_name)
                found = target.find(id=fragment) if target and fragment else None
                if found is not None:
                    bodies.setdefault((target_name, fragment), note_body(found))
            elif NOTE_TEXT.match(link.get_text(strip=True)) and not starts_block(link):
                # Plain numbered links whose target links back: the reference/note pairs many converters produce.
                target_name = name if link["href"].startswith("#") else epub.resolve(posixpath.dirname(name), link["href"])
                fragment = link["href"].partition("#")[2]
                target = pages.get(target_name)
                found = target.find(id=fragment) if target and fragment else None
                own = {value for value in (link.get("id"), link.get("name"), (link.find_parent("sup") or {}).get("id")) if value}
                if found is None or not own:
                    continue
                # The target is the back link itself, or an empty anchor (or block) that holds the back link.
                holder = block_of(found) if found.name == "a" and not found.get("href") else found
                anchors = [found] if found.name == "a" and found.get("href") else holder.find_all("a", href=True, limit=3)
                back = next((a for a in anchors if a["href"].partition("#")[2] in own), None)
                if back is not None and starts_block(back):
                    bodies.setdefault((target_name, fragment), block_of(back))
    # Render every note before any section is converted: converting a section removes the notes it contains.
    note_text = {key: inline_markdown(BeautifulSoup(str(tag), "html.parser")) for key, tag in bodies.items()}

    images, used_names = {}, set()
    en = root / "en"
    (en / "images").mkdir(parents=True, exist_ok=True)
    chapters, ids, notes_total = [], set(), 0
    unused_labels = list(epub.labels)
    for name in epub.spine:
        page = pages[name]
        body = page.body or page
        # Replace note references with markers and collect the definitions this section needs.
        definitions = []
        for link in body.find_all("a", href=True):
            is_ref = "noteref" in types(link) or "doc-noteref" in types(link)
            target_name = name if link["href"].startswith("#") else epub.resolve(posixpath.dirname(name), link["href"])
            key = (target_name, link["href"].partition("#")[2])
            if key not in bodies or not (is_ref or link.find_parent("sup") or link.find("sup") or NOTE_TEXT.match(link.get_text(strip=True))):
                continue
            number = len(definitions) + 1
            definitions.append(note_text[key])
            sup = link.find_parent("sup")
            (sup or link).replace_with(MARK.format(number))
        held_notes = False
        for (body_name, _), tag in bodies.items():
            if body_name == name and tag.parent is not None:
                tag.decompose()
                held_notes = True
        for tag in body.find_all(["script", "style"]):
            tag.decompose()
        links_out = [a for a in body.find_all("a", href=True)
                     if not a["href"].startswith("#") and epub.resolve(posixpath.dirname(name), a["href"]) in pages]
        if len(links_out) >= 5 and sum(len(a.get_text(strip=True)) for a in links_out) > len(body.get_text(strip=True)) / 2:
            continue  # the book's own table of contents page
        if not body.find(["h1", "h2", "h3", "h4", "h5", "h6"]):
            # No heading markup at all: bold paragraphs are the headings, the first one is the title.
            for index, paragraph in enumerate(p for p in body.find_all("p") if bold_only(p)):
                paragraph.string = " ".join(paragraph.get_text(" ").split())
                paragraph.name = "h1" if index == 0 else "h2"
        for image in body.find_all("img", src=True):
            source = epub.resolve(posixpath.dirname(name), image["src"])
            if source not in images:
                base = posixpath.basename(source)
                candidate, n = base, 1
                while candidate in used_names:
                    n += 1
                    stem, dot, ext = base.rpartition(".")
                    candidate = f"{stem}-{n}.{ext}" if dot else f"{base}-{n}"
                used_names.add(candidate)
                (en / "images" / candidate).write_bytes(epub.zip.read(source))
                images[source] = candidate
            image["src"] = "images/" + images[source]
        text = markdownify(str(body), heading_style="ATX", bullets="-")
        text = re.sub(r"[ \t]+\n", lambda m: "  \n" if m.group(0).startswith("  ") else "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        if not re.sub(r"[#\s]", "", text) and "images/" not in text:
            continue  # blank pages such as a cover
        if held_notes and not re.sub(r"^#{1,6} .*$|\s", "", text, flags=re.M):
            continue  # a notes section: its notes moved to the sections that cite them, only its heading is left
        if name == epub.nav:
            continue  # the EPUB's own table of contents
        # The first heading becomes level 1; deeper headings move up by the same amount.
        levels = [len(m) for m in re.findall(r"^(#{1,6}) ", text, flags=re.M)]
        heading = " ".join(re.sub(r"ZZNOTEREF\d+ZZ", "", next(iter(re.findall(r"^#{1,6} (.+)$", text, flags=re.M)), "")).split())
        # Prefer the table-of-contents label that names this section's own first heading; link targets come second,
        # because converted books often point the links a little before the section they mean.
        has_body = bool(re.sub(r"^#{1,6} .*$|\s", "", text, flags=re.M))
        label = next((l for l in unused_labels if heading and has_body and plain_title(l) == plain_title(heading)), None)
        if label:
            unused_labels.remove(label)
        title = label or epub.titles.get(name) or heading or f"Section {len(chapters) + 1}"
        title = " ".join(re.sub(r"ZZNOTEREF\d+ZZ", "", title).split())
        if levels:
            shift = min(levels) - 1
            text = re.sub(r"^(#{1,6}) ", lambda m: "#" * max(1, len(m[1]) - shift) + " ", text, flags=re.M)
            if not text.startswith("# "):
                text = f"# {title}\n\n{text}"
        else:
            text = f"# {title}\n\n{text}"
        first, _, rest = text.partition("\n")
        own = " ".join(re.sub(r"ZZNOTEREF\d+ZZ", "", first[2:]).split())
        if own and own.lower() in title.lower() and own != title:
            # "The Characters of the Story" becomes "1. The Characters of the Story"; note markers stay.
            text = f"# {title}" + "".join(re.findall(r"ZZNOTEREF\d+ZZ", first)) + "\n" + rest
        for number in range(1, len(definitions) + 1):
            text = text.replace(MARK.format(number), f"[^{number}]")
        if definitions:
            text += "\n\n" + "\n".join(f"[^{n}]: {d}" for n, d in enumerate(definitions, 1))
        notes_total += len(definitions)
        index = len(chapters) + 1
        number = chapter_number(title)
        entry = {}
        if number and f"ch{number:02d}" not in ids:
            entry["id"], entry["number"] = f"ch{number:02d}", number
        else:
            key = slug(title) or f"s{index:02d}"
            while key in ids or re.fullmatch(r"ch\d\d", key):
                key = f"{key}-{index}"
            entry["id"] = key
        ids.add(entry["id"])
        file = f"{index:02d}-{slug(title) or 'section'}.md"
        (en / file).write_text(text + "\n")
        entry.update({"file": file, "status": "todo"})
        chapters.append(entry)
    if not any((en / "images").iterdir()):
        (en / "images").rmdir()
    config["chapters"] = chapters
    config["source"] = {"epub": epub_path.name, "sha256": hashlib.sha256(epub_path.read_bytes()).hexdigest()}
    book_config.save(root, config)
    return f"Imported {len(chapters)} sections, {notes_total} notes and {len(images)} images from {epub_path.name}."


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("book", type=Path)
    parser.add_argument("epub", type=Path)
    parser.add_argument("--force", action="store_true", help="replace the chapters already listed in book.json")
    args = parser.parse_args()
    try:
        print(import_epub(args.book, args.epub, args.force))
    except (ValueError, KeyError, zipfile.BadZipFile) as error:
        raise SystemExit(f"error: {error}")


if __name__ == "__main__":
    sys.exit(main())
