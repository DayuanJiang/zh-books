"""Compile a bilingual book into the reader's data: aligned chapter units, the manifest, code variants and guides.

Reads the book folder (en/, zh-cn/, assets/) and writes only into the output folder; book text is never modified.
"""

import ast
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import book

VARIANT_LANGUAGES = {".java": "java", ".cpp": "cpp", ".c": "c", ".go": "go"}

PEDAGOGY_FIELDS = (
    "readerQuestion", "expectedAnswer", "visualEncoding", "sourceEvidence",
    "beforeProblem", "whyBetter", "limits",
)


def check_pedagogy(metadata):
    review = metadata.get("pedagogy", {})
    if review.get("action") not in {"keep", "revise", "replace"}:
        raise ValueError(f"Missing diagram review decision: {metadata.get('id', metadata.get('chapter'))}")
    for key in PEDAGOGY_FIELDS:
        if not isinstance(review.get(key), str) or not review[key].strip():
            raise ValueError(f"Missing diagram review field {key}: {metadata.get('id', metadata.get('chapter'))}")


def anchor_count(chapter, anchor):
    """How many translation blocks contain the anchor text (footnote markers ignored on both sides)."""
    needle = " ".join(re.sub(r"\[\^\w+\]", "", anchor).split())
    if not needle:
        return 0
    return sum(needle in " ".join(re.sub(r"\[\^\w+\]", "", u.get("targetPlain") or "").split()) for u in chapter["units"])


def compile_code_variants(folder, text):
    """Pair each <n>.<lang> code example with its <n>.py rewrite or <n>.skip note and check them."""
    if not folder.is_dir():
        return None
    # The Markdown renderer expands tabs to four spaces, so compare and publish sources that way.
    fences = {t.content.replace("\t", "    ").strip() for t in book.PARSE.parse(text) if t.type == "fence"}
    entries = []
    for source_path in sorted(p for p in folder.iterdir() if p.suffix in VARIANT_LANGUAGES):
        source = source_path.read_text().replace("\t", "    ").strip()
        if source not in fences:
            raise ValueError(f"Code variant source is not a code block of the chapter: {source_path}")
        entry = {"language": VARIANT_LANGUAGES[source_path.suffix], "source": source}
        rewrite, skip = source_path.with_suffix(".py"), source_path.with_suffix(".skip")
        if rewrite.exists():
            entry["python"] = rewrite.read_text().strip()
            try:
                ast.parse(entry["python"], filename=str(rewrite))
            except SyntaxError as error:
                raise ValueError(f"Python rewrite does not parse: {rewrite}: {error}") from error
        elif skip.read_text().strip() if skip.exists() else False:
            entry["note"] = skip.read_text().strip()
        else:
            raise ValueError(f"Code example needs a Python rewrite or a skip note with a reason: {source_path}")
        entries.append(entry)
    return entries or None


def check_svg(path, chapter, mobile, section=None, story=False):
    """Section figures have fixed sizes; generated chapter maps and storylines have a fixed width and any height."""
    root = ET.parse(path).getroot()
    key = section or f"ch{chapter:02d}" + ("-story" if story else "")
    if section:
        valid = root.get("viewBox") == ("0 0 420 600" if mobile else "0 0 960 480")
    else:
        valid = re.fullmatch(r"0 0 (420|960) \d+", root.get("viewBox", "")) and root.get("viewBox").startswith("0 0 420 " if mobile else "0 0 960 ")
    if not valid or root.get("role") != "img":
        raise ValueError(f"Invalid SVG dimensions/accessibility: {path}")
    classes = set(root.get("class", "").split())
    if "chapter-svg" not in classes or "cg-" + key not in classes:
        raise ValueError(f"Missing responsive/scoped SVG class: {path}")
    if len(root.get("aria-labelledby", "").split()) < 2:
        raise ValueError(f"Missing SVG title/description labels: {path}")
    ids = [e.get("id") for e in root.iter() if e.get("id")]
    prefix = f"{key}{'m' if mobile else ''}-"
    if len(ids) != len(set(ids)) or any(not identifier.startswith(prefix) for identifier in ids):
        raise ValueError(f"Invalid or duplicate SVG IDs: {path}")
    for identifier in root.get("aria-labelledby", "").split():
        if identifier not in ids:
            raise ValueError(f"Missing accessible label: {path}")
    for element in root.iter():
        tag = element.tag.split("}")[-1]
        if tag in {"script", "foreignObject", "image", "a"}:
            raise ValueError(f"Unsupported active/external element: {path}")
        for name, value in element.attrib.items():
            if name.lower().startswith("on"):
                raise ValueError(f"Event attribute in SVG: {path}")
            if name.split("}")[-1] == "href" and not value.startswith("#"):
                raise ValueError(f"External SVG reference: {path}")
        for ref in re.findall(r"url\(#([^)]+)\)", ET.tostring(element, encoding="unicode")):
            if ref not in ids:
                raise ValueError(f"Missing marker: {path}: {ref}")


def judged_roles(root):
    """Paragraph roles decided case by case, from roles.json: {"<unit id>": {"role": ..., "why": ...}}."""
    path = root / "roles.json"
    if not path.exists():
        return {}
    judged = {key: value["role"] for key, value in json.loads(path.read_text()).items()}
    unknown = {role for role in judged.values() if role not in book.JUDGED_ROLES}
    if unknown:
        raise ValueError(f"roles.json: unknown roles {sorted(unknown)}; use one of {sorted(r for r in book.JUDGED_ROLES if r)} or null")
    return judged


def included(config, drafts):
    """Chapters to publish: finished ones, plus unfinished translations when previewing drafts."""
    return [c for c in config["chapters"] if c["status"] == "done" or (drafts and c["status"] != "todo")]


def compile_book(root, config, out, drafts=False):
    """Write reader-content, code variants and the manifest into out/assets and return the manifest.

    Chapter maps (assets/diagrams/chNN.json) must already be rendered into out/ by chapter_figures.
    """
    content = out / "assets" / "reader-content"
    variants_out = out / "assets" / "code-variants"
    diagrams = root / "assets" / "diagrams"
    content.mkdir(parents=True, exist_ok=True)
    variants_out.mkdir(parents=True, exist_ok=True)
    chapters, guides = [], {}
    judged = judged_roles(root)
    for entry in included(config, drafts):
        key, n, file = entry["id"], entry.get("number"), entry["file"]
        source, translation = root / "en" / file, root / "zh-cn" / file
        if not translation.exists():
            raise ValueError(f"Translation file missing: zh-cn/{file}")
        partial = entry["status"] != "done"
        text = source.read_text()
        parent = Path(file).parent.as_posix()
        image_root = "en/" + parent if parent != "." else "en"
        chapter = book.compile_chapter(key, text, translation.read_text(), image_root, partial=partial, judged=judged)
        recap = root / "recaps" / f"{key}.md"
        if recap.exists():
            # A summary and takeaways written by the translator, shown after the chapter and marked as such.
            recap_text = recap.read_text()
            chapter["recap"] = {"html": book.RENDER.render(recap_text).strip(), "text": " ".join(recap_text.split())}
        (content / f"{key}.json").write_text(json.dumps(chapter, ensure_ascii=False) + "\n")
        page = {"id": key, "number": n, "title": chapter["title"], "englishTitle": chapter["englishTitle"],
                "file": f"zh-cn/{file}", "source": f"en/{file}", "route": "/zh-cn/" + file.removesuffix(".md"),
                "content": f"assets/reader-content/{key}.json"}
        if partial:
            page["draft"] = True
        chapters.append(page)
        variants = compile_code_variants(root / "assets" / "code-variants" / key, text)
        if variants:
            (variants_out / f"{key}.json").write_text(json.dumps(variants, ensure_ascii=False, indent=2) + "\n")
            page["codeVariants"] = f"assets/code-variants/{key}.json"
        metadata_path = diagrams / f"{key}.json"
        if not (n and metadata_path.exists()):
            continue
        metadata = json.loads(metadata_path.read_text())
        if metadata["chapter"] != n or not metadata["title"] or not metadata["summary"]:
            raise ValueError(f"Invalid guide metadata: {key}")
        check_pedagogy(metadata)
        if metadata["map"]["question"] != metadata["title"] or not metadata["story"]["acts"]:
            raise ValueError(f"Chapter map/story content missing or inconsistent: {key}")
        headings = {" ".join(re.sub(r"^#+\s*", "", u["source"]).split()) for u in chapter["units"] if u["kind"] == "heading"}
        for heading in metadata["sourceSections"]:
            if " ".join(heading.split()) not in headings:
                raise ValueError(f"Unknown source heading in {key}: {heading}")
        check_svg(out / metadata["desktop"], n, False)
        check_svg(out / metadata["mobile"], n, True)
        check_svg(out / metadata["storyDesktop"], n, False, story=True)
        check_svg(out / metadata["storyMobile"], n, True, story=True)
        # The reader only needs titles and file paths; the map text, storyline and review notes stay in the metadata file.
        guides[key] = {field: metadata[field] for field in ("chapter", "title", "summary", "desktop", "mobile", "storyDesktop", "storyMobile")}
        guides[key]["storyTitle"] = metadata["story"]["headline"]
        sections = []
        for section_path in sorted((diagrams / "sections").glob(f"{key}-*.json")):
            section = json.loads(section_path.read_text())
            if section["id"] != section_path.stem or section["chapter"] != n:
                raise ValueError(f"Invalid section guide identity: {section_path}")
            check_pedagogy(section)
            if anchor_count(chapter, section["afterParagraph"]) != 1:
                raise ValueError(f"Ambiguous section insertion point: {section_path}")
            for heading in section["sourceSections"]:
                if " ".join(heading.split()) not in headings:
                    raise ValueError(f"Unknown section guide heading: {section_path}: {heading}")
            check_svg(root / section["desktop"], n, False, section["id"])
            check_svg(root / section["mobile"], n, True, section["id"])
            sections.append(section)
        if sections:
            page["sectionGuides"] = sections
    if config.get("chapterMaps"):
        missing = [c["id"] for c in chapters if c["number"] and not c.get("draft") and c["id"] not in guides]
        if missing:
            raise ValueError(f"Chapters without an opening map and closing storyline: {', '.join(missing)}")
    manifest = {"chapters": chapters, "guides": guides}
    (out / "assets" / "reader-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest
