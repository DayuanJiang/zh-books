"""Small shared file/report helpers; no repository discovery or source mutation."""

import hashlib
import json
from pathlib import Path


def digest(value):
    return hashlib.sha256(value.encode("utf-8") if isinstance(value, str) else value).hexdigest()


def write_json(destination, data, *, forbidden=(), overwrite=False):
    destination = Path(destination)
    if destination.suffix.lower() != ".json":
        raise ValueError("Reports must use a .json output path")
    if destination.is_symlink() or destination.resolve() in {Path(p).resolve() for p in forbidden}:
        raise ValueError(f"Output would replace an input or symlink: {destination}")
    if overwrite and destination.exists():
        try:
            previous = json.loads(destination.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as error:
            raise ValueError(f"Refusing to overwrite a non-report: {destination}") from error
        if not isinstance(previous, dict) or previous.get("schema") != data.get("schema") or previous.get("type") != data.get("type") or not data.get("type"):
            raise ValueError(f"Refusing to overwrite a different report type: {destination}")
        if previous.get("type") == "translation-baseline":
            raise ValueError("Baselines are immutable, including through other commands")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w" if overwrite else "x", encoding="utf-8") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def select_files(root, includes, excludes=(), *, allow_empty=False):
    root = Path(root).resolve()
    for pattern in [*includes, *excludes]:
        if Path(pattern).is_absolute() or ".." in Path(pattern).parts:
            raise ValueError(f"Globs must stay relative to --root: {pattern}")
    excluded = {p for pattern in excludes for p in root.glob(pattern)}
    files = {}
    for pattern in includes:
        for file in root.glob(pattern):
            if file in excluded or not file.is_file():
                continue
            if not file.resolve().is_relative_to(root):
                raise ValueError(f"Input symlink escapes --root: {file}")
            files[str(file.relative_to(root))] = file
    if not files and not allow_empty:
        raise ValueError("No input files matched. Quote globs and check --root.")
    return dict(sorted(files.items()))
