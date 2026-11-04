"""Translation progress of a book: per chapter, its status and how much of it is translated.

    uv run --project framework/tools python framework/tools/status.py books/<id>

Prints a Markdown table. A chapter whose translation does not line up with the source block by block
shows the aligner's error instead of a count.
"""

import argparse
from pathlib import Path

import book
import config as book_config


def progress(root, entry):
    """(translated blocks, translatable blocks, translated notes, notes, error or None) for one chapter."""
    source_blocks, source_notes = book.parse((root / "en" / entry["file"]).read_text())
    total = sum(book.translatable(block) for block in source_blocks)
    translation = root / "zh-cn" / entry["file"]
    if not translation.exists():
        return 0, total, 0, len(source_notes), None
    target_blocks, target_notes = book.parse(translation.read_text())
    try:
        pairs = book.align(source_blocks, target_blocks, entry["id"], partial=True)
    except ValueError as error:
        return None, total, None, len(source_notes), str(error)
    done = sum(1 for block, target in pairs if target is not None)
    return done, total, len(set(target_notes) & set(source_notes)), len(source_notes), None


def report(root):
    root = Path(root)
    config = book_config.load(root)
    lines = [f"# {config['title']} · {config['originalTitle']}", "",
             "| Chapter | Status | Blocks translated | Notes translated |", "| --- | --- | --- | --- |"]
    totals = [0, 0]
    counts = {}
    for entry in config["chapters"]:
        done, total, notes_done, notes, error = progress(root, entry)
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1
        totals[1] += total
        if error:
            lines.append(f"| {entry['id']} | {entry['status']} | error: {error} | |")
            continue
        totals[0] += done
        note_cell = f"{notes_done}/{notes}" if notes else ""
        lines.append(f"| {entry['id']} | {entry['status']} | {done}/{total} | {note_cell} |")
    share = f"{100 * totals[0] / totals[1]:.0f}%" if totals[1] else "0%"
    summary = ", ".join(f"{counts[s]} {s}" for s in book_config.STATUSES if s in counts)
    lines += ["", f"{len(config['chapters'])} chapters ({summary}); {totals[0]}/{totals[1]} blocks translated ({share})."]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("book", type=Path)
    print(report(parser.parse_args().book))


if __name__ == "__main__":
    main()
