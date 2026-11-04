#!/usr/bin/env python3
"""Offline lint for static explanatory SVGs; not a sanitizer or readability verdict."""

import argparse
from collections import Counter, defaultdict
import math
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

from io_utils import digest, select_files, write_json


def check_svg(raw):
    errors, warnings = [], []
    if re.search(br"<!\s*(?:DOCTYPE|ENTITY)\b", raw, re.I):
        return {"errors": ["DTD/entity declarations are outside this static profile"], "warnings": [], "ids": []}
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as error:
        return {"errors": [f"Invalid XML: {error}"], "warnings": [], "ids": []}
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        errors.append("Root is not an SVG element in the SVG namespace")
    try:
        box = [float(number) for number in re.split(r"[\s,]+", root.get("viewBox", "").strip())]
        if len(box) != 4 or not all(map(math.isfinite, box)) or min(box[2:]) <= 0:
            raise ValueError()
    except ValueError:
        errors.append("viewBox must have four finite numbers and positive width/height")
    ids = [node.get("id") for node in root.iter() if node.get("id")]
    errors.extend(f"Duplicate id: {key}" for key, count in Counter(ids).items() if count > 1)
    for tag in ("title", "desc"):
        if not any(node.tag.rsplit("}", 1)[-1] == tag and "".join(node.itertext()).strip() for node in root.iter()):
            errors.append(f"Missing nonempty {tag}")

    def visit(node, marker_start=None, marker_end=None):
        tag = node.tag.rsplit("}", 1)[-1]
        if tag in {"script", "foreignObject", "image", "iframe", "animate", "animateTransform", "set"}:
            errors.append(f"{tag} is outside the static vector profile")
        if tag == "style":
            warnings.append("Embedded CSS needs scoped-selector/resource review; CSS is not parsed by this helper")
        marker_start = node.get("marker-start", marker_start)
        marker_end = node.get("marker-end", marker_end)
        if tag == "path" and any(value and value != "none" for value in (marker_start, marker_end)):
            if len(re.findall("[Mm]", node.get("d", ""))) > 1:
                warnings.append(f"Compound marked path: inspect each intended arrow endpoint: {node.get('d')}")
        for key, value in node.attrib.items():
            key = key.rsplit("}", 1)[-1]
            if key.lower().startswith("on"):
                errors.append(f"Event attribute: {key}")
            if key in {"href", "src"} and not value.startswith("#"):
                errors.append(f"Nonlocal {key}: {value}")
            if key == "href" and value.startswith("#") and value[1:] not in ids:
                errors.append(f"Unresolved local reference: {value}")
            for target in re.findall(r"url\(\s*['\"]?([^)'\"\s]+)['\"]?\s*\)", value):
                if not target.startswith("#") or target[1:] not in ids:
                    errors.append(f"Unresolved/nonlocal URL reference: {target}")
            if key in {"aria-labelledby", "aria-describedby"}:
                errors.extend(f"Unresolved {key}: {target}" for target in value.split() if target not in ids)
        for child in node:
            visit(child, marker_start, marker_end)

    visit(root)
    return {"errors": sorted(set(errors)), "warnings": sorted(set(warnings)), "ids": sorted(ids)}


def main(argv=None):
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, required=True)
    cli.add_argument("--include", action="append", required=True)
    cli.add_argument("--exclude", action="append", default=[])
    cli.add_argument("--out", type=Path)
    cli.add_argument("--inline-set", action="store_true", help="Also report ID reuse across selected files.")
    cli.add_argument("--warnings-as-errors", action="store_true")
    args = cli.parse_args(argv)
    try:
        files = select_files(args.root, args.include, args.exclude)
        if any(file.suffix.lower() != ".svg" for file in files.values()):
            raise ValueError("Select SVG files only")
        rows, owners = [], defaultdict(list)
        for name, file in files.items():
            raw = file.read_bytes()
            result = check_svg(raw)
            for identifier in result.pop("ids"):
                owners[identifier].append(name)
            rows.append({"file": name, "sha256": digest(raw), **result})
        reused = {key: names for key, names in owners.items() if len(names) > 1} if args.inline_set else {}
        result = {"schema": 1, "type": "static-svg-check", "files": rows,
                  "tool_sha256": digest(Path(__file__).read_bytes()),
                  "cross_file_ids": reused,
                  "boundary": "No rendering, font/arrow geometry, theme contrast, comprehension, or arbitrary-SVG sanitization has been validated. Cross-file IDs matter only when sharing one DOM scope."}
        if args.out:
            write_json(args.out, result, forbidden=files.values())
        else:
            import json
            print(json.dumps(result, ensure_ascii=False, indent=2))
        failed = any(row["errors"] for row in rows) or args.warnings_as_errors and (reused or any(row["warnings"] for row in rows))
        return int(bool(failed))
    except (ValueError, OSError) as error:
        cli.exit(2, f"error: {error}\n")


if __name__ == "__main__":
    sys.exit(main())
