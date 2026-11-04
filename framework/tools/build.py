"""Build one bilingual book into a static folder: reader, chapters, figures, search index and fonts.

    uv run --project framework/tools python framework/tools/build.py books/<id> <out-dir> [--drafts]

The book folder holds only sources (book.json, en/, zh-cn/, assets/); everything derived is written to the
output folder. Without --drafts only chapters with status "done" are published and every check is strict.
With --drafts, chapters with status "draft" or "review" are included too, and a translation that stops
part way through a chapter is accepted (the rest shows in English, marked as not translated yet).
"""

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import sys

import chapter_figures
import config as book_config
import fonts
import reader_data
import search_index

READER = Path(__file__).resolve().parents[1] / "reader"


def copy_text(root, out, chapters):
    """Copy en/ and zh-cn/ (images included) without the Markdown of chapters that are not published."""
    published = {c["file"] for c in chapters}
    for language in ("en", "zh-cn"):
        for path in (root / language).rglob("*"):
            relative = path.relative_to(root / language)
            if path.is_dir() or (path.suffix == ".md" and relative.as_posix() not in published):
                continue
            target = out / language / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)


def render_index(config, out, url, repo, start):
    page = config.get("page", {})
    page_title = page.get("title") or f"{config['title']} · {config['originalTitle']}"
    description = page.get("description") or config.get("summary", "")
    values = {
        "pageTitle": page_title,
        "title": config["title"],
        "description": description,
        "shareTitle": page.get("shareTitle") or page_title,
        "shareDescription": page.get("shareDescription") or description,
        "url": url,
        "cover": config.get("cover", ""),
        "themeColor": page.get("themeColor", "#a33e36"),
    }
    book = {"title": config["title"], "originalTitle": config["originalTitle"], "repo": repo,
            "storageKey": page.get("storageKey") or f"{config['id']}-reader-preferences-v1", "start": start}
    text = (READER / "index.html").read_text()
    text = text.replace("{{book}}", json.dumps(book, ensure_ascii=False).replace("<", "\\u003c"))
    text = text.replace("{{docsifyName}}", json.dumps(config["originalTitle"], ensure_ascii=False).replace("<", "\\u003c"))
    for name, value in values.items():
        text = text.replace("{{" + name + "}}", html.escape(value))
    # A content hash on the reader's script and stylesheets, so browsers never serve stale copies.
    text = re.sub(r"\{\{hash:([^}]+)\}\}", lambda m: hashlib.sha256((out / m[1]).read_bytes()).hexdigest()[:8], text)
    if "{{" in text:
        raise ValueError(f"Unfilled placeholder in index.html: {re.search(r'{{[^}]*}}', text)[0]}")
    (out / "index.html").write_text(text)


def build(root, out, drafts=False, url="", repo=""):
    root, out = Path(root).resolve(), Path(out).resolve()
    config = book_config.load(root)
    chapters = reader_data.included(config, drafts)
    if not chapters:
        raise ValueError("No chapter to publish: mark finished chapters as \"done\" in book.json, or build with --drafts")
    if out.exists():
        shutil.rmtree(out)
    (out / "assets").mkdir(parents=True)
    # Shared reader front end, then the book's own assets (cover, fonts, diagram data, figures, code examples).
    shutil.copytree(READER / "vendor", out / "assets" / "vendor")
    for name in ("reader.js", "reader.css", "reader-icons.svg"):
        shutil.copyfile(READER / name, out / "assets" / name)
    if (root / "assets").is_dir():
        shutil.copytree(root / "assets", out / "assets", dirs_exist_ok=True)
    copy_text(root, out, chapters)
    figures = chapter_figures.build_book(root, out)
    manifest = reader_data.compile_book(root, config, out, drafts)
    sections = search_index.build_index(out, manifest)
    labels = [("（草稿）" if page.get("draft") else "") for page in manifest["chapters"]]
    (out / "_sidebar.md").write_text("".join(f"- [{' '.join(page['title'].split())}{label}]({page['file']})\n"
                                             for page, label in zip(manifest["chapters"], labels)))
    start_entry = next((c for c in chapters if c["id"] == config.get("start")), chapters[0])
    render_index(config, out, url, repo, "/zh-cn/" + start_entry["file"].removesuffix(".md"))
    missing = fonts.missing_characters(root, chapters)
    if missing:
        message = (f"The font subset lacks {len(missing)} characters (for example {''.join(missing[:10])}); "
                   f"run: python3 scripts/site.py fonts {root.name}")
        if not drafts:
            raise ValueError(message)
        print("warning: " + message, file=sys.stderr)
    drafts_count = sum(1 for page in manifest["chapters"] if page.get("draft"))
    return (f"{config['title']}: {len(manifest['chapters'])} chapters ({drafts_count} drafts), "
            f"{figures} chapter maps, {sections} search sections")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("book", type=Path, help="book folder, for example books/swe-at-google")
    parser.add_argument("out", type=Path, help="output folder; replaced on every build")
    parser.add_argument("--drafts", action="store_true", help="also publish chapters that are still being translated")
    parser.add_argument("--url", default="", help="public URL of the book, used for link previews")
    parser.add_argument("--repo", default="", help="URL of the book's source folder, linked from the reader")
    args = parser.parse_args()
    try:
        print(build(args.book, args.out, args.drafts, args.url, args.repo))
    except ValueError as error:
        raise SystemExit(f"error: {error}")


if __name__ == "__main__":
    main()
