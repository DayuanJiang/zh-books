#!/usr/bin/env python3
"""Extract Markdown prose or compare immutable, structure-aware worktree snapshots."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from importlib.metadata import version
import json
from pathlib import Path
import re
import sys

from markdown_it import MarkdownIt
from markdown_it.rules_inline import backtick
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.texmath import texmath_plugin
from io_utils import digest, select_files, write_json

SCHEMA = 1
PROFILE = "commonmark-tables-named-footnotes-dollar-bracket-math-v1"
HAN = re.compile(r"[\u3400-\u9fff]")
LATIN = re.compile(r"[A-Za-z][A-Za-z0-9_]*(?:[-'.:+/#][A-Za-z0-9_]+)*(?:\+\+|#)?")
NUMBER = re.compile(r"[+-]?\d+(?:[.,]\d+)*(?:[eE][+-]?\d+)?%?")
URL = re.compile(r"(?:https?://|mailto:)[^\s<>\"`，。；！？、（）“”]+|[\w.+-]+@[\w.-]+\.[A-Za-z]+")
MARKDOWN = {".md", ".markdown", ".mdown"}


def parser_identity():
    return {"profile": PROFILE, "markdown-it-py": version("markdown-it-py"),
            "mdit-py-plugins": version("mdit-py-plugins")}


def markdown_parser():
    md = (MarkdownIt("commonmark").enable("table")
          .use(front_matter_plugin)
          .use(footnote_plugin, inline=False, move_to_end=False, always_match_refs=True)
          .use(dollarmath_plugin)
          .use(texmath_plugin, delimiters="brackets"))

    def literal_backticks(state, silent):
        start, count = state.pos, len(state.tokens)
        matched = backtick(state, silent)
        if matched and not silent:
            for token in state.tokens[count:]:
                if token.type == "code_inline":
                    token.meta["literal_source"] = state.src[start:state.pos]
        return matched

    md.inline.ruler.at("backticks", literal_backticks)
    return md


class InlineHTML(HTMLParser):
    """Track literal inline HTML regions without rewriting or evaluating HTML."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.literal_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"code", "pre", "script", "style", "math", "svg"}:
            self.literal_depth += 1

    def handle_endtag(self, tag):
        if tag in {"code", "pre", "script", "style", "math", "svg"}:
            self.literal_depth = max(0, self.literal_depth - 1)

    def handle_startendtag(self, tag, attrs):
        pass


def parse_document(file, source, *, language="auto", inline_code=False,
                   include_headings=False, exclude_sections=()):
    tokens, env = [], {}
    tokens = markdown_parser().parse(source, env)
    lines = source.splitlines(keepends=True)
    protected = defaultdict(list)
    segments, skipped = [], Counter()
    stack, headings = [], []
    serial = 0
    for index, token in enumerate(tokens):
        if token.type == "heading_open":
            title = tokens[index + 1].content
            level = int(token.tag[1:])
            headings = [entry for entry in headings if entry[0] < level]
            headings.append((level, title))
        if token.nesting:
            if token.nesting == 1:
                stack.append(token)
                if token.type != "paragraph_open":
                    protected["structure"].append([token.type, token.tag, token.markup, token.attrs])
                if token.type == "footnote_reference_open":
                    protected["footnotes"].append(["definition", token.meta.get("label")])
            elif stack:
                stack.pop()
            continue
        span = token.map or next((entry.map for entry in reversed(stack) if entry.map), [0, 0])
        raw = "".join(lines[span[0]:span[1]])
        if token.type in {"fence", "code_block", "html_block", "front_matter"} or token.type.startswith("math_block"):
            protected[token.type].append(raw or token.content)
            skipped[token.type] += 1
            continue
        if token.type != "inline":
            if token.content:
                protected["unknown_tokens"].append([token.type, token.content])
                skipped["unknown_tokens"] += 1
            continue
        parents = {entry.type for entry in stack}
        kind = ("heading" if "heading_open" in parents else "footnote"
                if "footnote_reference_open" in parents else "table" if "table_open" in parents
                else "quote" if "blockquote_open" in parents else "prose")
        if not HAN.search(token.content) and re.search("[A-Za-z]", token.content):
            protected["english_nodes"].append(token.content)
        # Keep node boundaries: moving identifiers between paragraphs is still a change.
        words, numbers, prose = [], [], []
        html = InlineHTML()
        for child in token.children or []:
            if child.nesting:
                protected["inline_structure"].append([child.type, child.markup])
            if child.type in {"link_open", "image"}:
                attrs = {key: value for key, value in child.attrs.items() if key != "alt"}
                protected["destinations"].append([child.type, attrs])
            if child.type == "html_inline":
                protected["html_inline"].append(child.content)
                html.feed(child.content)
                prose.append(" ")
            elif child.type == "code_inline":
                protected["inline_code"].append(child.meta.get("literal_source", child.markup + child.content))
                prose.append(URL.sub(" ", child.content) if inline_code else " ")
            elif child.type.startswith("math_inline"):
                protected["inline_math"].append([child.markup, child.content])
                prose.append(" ")
            elif child.type == "footnote_ref":
                protected["footnotes"].append(["reference", child.meta.get("label")])
                prose.append(" ")
            elif child.type == "text":
                words.extend(LATIN.findall(child.content))
                numbers.extend(NUMBER.findall(child.content))
                protected["bare_urls"].extend(URL.findall(child.content))
                if html.literal_depth:
                    protected["html_literal"].append(child.content)
                    prose.append(" ")
                else:
                    prose.append(URL.sub(" ", child.content))
            elif child.type in {"softbreak", "hardbreak"}:
                prose.append("\n")
            elif child.type == "image":
                prose.append(" ")
            elif not child.nesting and child.content:
                protected["unknown_inline"].append([child.type, child.content])
                prose.append(" ")
                skipped["unknown_inline"] += 1
        protected["latin_and_numbers"].append([words, numbers])
        if html.literal_depth:
            skipped["unclosed_literal_html"] += 1
        if kind == "heading" and not include_headings:
            skipped["heading"] += 1
            continue
        if any(title.casefold() in {s.casefold() for s in exclude_sections} for _, title in headings):
            skipped["excluded_section"] += 1
            continue
        runs = []
        for offset, text in enumerate("".join(prose).splitlines()):
            text = text.strip()
            if not text:
                continue
            detected = "zh" if HAN.search(text) else "en" if re.search("[A-Za-z]", text) else "other"
            if detected == "other":
                continue
            detected = detected if language == "auto" else language
            if runs and runs[-1][0] == detected:
                runs[-1][2] += "\n" + text
            else:
                runs.append([detected, offset, text])
        for detected, offset, text in runs:
            serial += 1
            segments.append({
                "id": f"{file}#s{serial}:{digest(token.content)[:12]}",
                "file": file, "line": span[0] + 1, "end_line": span[1],
                "line_offset_in_prose": offset, "section": [h[1] for h in headings],
                "kind": kind, "language": detected,
                "language_status": "heuristic" if language == "auto" else "declared",
                "mixed": bool(HAN.search(text) and re.search("[A-Za-z]", text)), "text": text,
            })
    protected["reference_definitions"] = [
        [label, value.get("href"), value.get("title"),
         "".join(lines[value["map"][0]:value["map"][1]]) if value.get("map") else None]
        for label, value in sorted(env.get("references", {}).items())
    ]
    return {"sha256": digest(source), "protected": dict(protected),
            "segments": segments, "skipped": dict(skipped)}


def selection_args(parser):
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--include", action="append", required=True, help="Repeat quoted root-relative globs.")
    parser.add_argument("--exclude", action="append", default=[])


def snapshot(root, includes, excludes, exact_globs=(), *, allow_empty=False):
    files = select_files(root, includes, excludes, allow_empty=allow_empty)
    exact = set()
    for pattern in exact_globs:
        matched = select_files(root, [pattern], allow_empty=allow_empty)
        if not allow_empty and not matched.keys() <= files.keys():
            raise ValueError(f"--exact files must also be selected by --include: {pattern}")
        exact.update(matched)
    entries = {}
    for name, file in files.items():
        raw = file.read_bytes()
        item = {"sha256": digest(raw), "symlink": str(file.readlink()) if file.is_symlink() else None}
        if file.suffix.lower() in MARKDOWN and name not in exact:
            item["protected"] = parse_document(name, raw.decode("utf-8"))["protected"]
        entries[name] = item
    return {"schema": SCHEMA, "type": "translation-baseline", "parser": parser_identity(),
            "tool_sha256": digest(Path(__file__).read_bytes()),
            "created_at": datetime.now(timezone.utc).isoformat(), "root": str(Path(root).resolve()),
            "selection": {"include": includes, "exclude": excludes, "exact": exact_globs},
            "files": entries}


def compare(root, baseline, *, exact=False):
    if not isinstance(baseline, dict) or baseline.get("type") != "translation-baseline" or baseline.get("schema") != SCHEMA:
        raise ValueError("Unsupported baseline schema")
    if baseline["parser"] != parser_identity():
        raise ValueError("Parser profile/version differs; use the recorded environment, not a refreshed baseline.")
    selection = baseline["selection"]
    current = snapshot(root, selection["include"], selection["exclude"], selection["exact"], allow_empty=True)
    errors, changed = [], []
    for name in sorted(baseline["files"].keys() | current["files"].keys()):
        old, new = baseline["files"].get(name), current["files"].get(name)
        if old is None or new is None:
            errors.append({"file": name, "changed": ["added" if old is None else "deleted"]})
            continue
        if old["sha256"] != new["sha256"]:
            changed.append(name)
        fields = ["symlink", "sha256"] if exact or "protected" not in old else ["symlink", "protected"]
        differences = [key for key in fields if old.get(key) != new.get(key)]
        if "protected" in differences:
            differences = ["protected." + key for key in sorted(old["protected"].keys() | new["protected"].keys())
                           if old["protected"].get(key) != new["protected"].get(key)]
            if old["symlink"] != new["symlink"]:
                differences.append("symlink")
        if differences:
            errors.append({"file": name, "changed": differences})
    return {"schema": SCHEMA, "type": "baseline-check", "root": str(Path(root).resolve()),
            "changed_files": changed, "failures": errors,
            "boundary": "Structural/protected-token comparison, not Chinese semantic or generated-anchor validation."}


def main(argv=None):
    cli = argparse.ArgumentParser(description=__doc__)
    sub = cli.add_subparsers(dest="command", required=True)
    extract = sub.add_parser("extract")
    selection_args(extract)
    extract.add_argument("--language", choices=["auto", "en", "zh"], default="auto")
    extract.add_argument("--include-inline-code", action="store_true")
    extract.add_argument("--include-headings", action="store_true")
    extract.add_argument("--exclude-section", action="append", default=[])
    extract.add_argument("--out", type=Path, required=True)
    extract.add_argument("--overwrite", action="store_true")
    base = sub.add_parser("snapshot")
    selection_args(base)
    base.add_argument("--exact", action="append", default=[], help="Markdown globs protected byte-for-byte.")
    base.add_argument("--out", type=Path, required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--root", type=Path, required=True)
    verify.add_argument("--baseline", type=Path, required=True)
    verify.add_argument("--exact", action="store_true")
    verify.add_argument("--out", type=Path)
    args = cli.parse_args(argv)
    try:
        if args.command == "verify":
            result = compare(args.root, json.loads(args.baseline.read_text(encoding="utf-8")), exact=args.exact)
            if args.out:
                inputs = select_files(args.root, json.loads(args.baseline.read_text())["selection"]["include"], allow_empty=True)
                write_json(args.out, result, forbidden=[args.baseline, *inputs.values()])
            else:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            return bool(result["failures"])
        files = select_files(args.root, args.include, args.exclude)
        if args.command == "snapshot":
            result = snapshot(args.root, args.include, args.exclude, args.exact)
        else:
            non_markdown = [name for name, file in files.items() if file.suffix.lower() not in MARKDOWN]
            files = {name: file for name, file in files.items() if file.suffix.lower() in MARKDOWN}
            if not files:
                raise ValueError("No Markdown files selected")
            documents = {name: parse_document(name, file.read_bytes().decode("utf-8"),
                language=args.language, inline_code=args.include_inline_code,
                include_headings=args.include_headings, exclude_sections=args.exclude_section)
                for name, file in files.items()}
            result = {"schema": SCHEMA, "type": "translation-corpus", "root": str(args.root.resolve()),
                "tool_sha256": digest(Path(__file__).read_bytes()),
                "parser": parser_identity(),
                "policy": {"language": args.language, "inline_code": args.include_inline_code,
                           "headings": args.include_headings, "excluded_sections": args.exclude_section},
                "sources": {name: doc["sha256"] for name, doc in documents.items()},
                "segments": [segment for doc in documents.values() for segment in doc["segments"]],
                "skipped": {name: doc["skipped"] for name, doc in documents.items()},
                "non_markdown_excluded": non_markdown,
                "boundary": "Language labels are heuristic/declared, not reviewed bilingual alignment. No automatic translation pairing."}
        write_json(args.out, result, forbidden=select_files(args.root, args.include, args.exclude).values(),
                   overwrite=getattr(args, "overwrite", False))
        print(f"Wrote {args.out}: {len(files)} selected files")
        return 0
    except (ValueError, OSError, UnicodeError) as error:
        cli.exit(2, f"error: {error}\n")


if __name__ == "__main__":
    sys.exit(main())
