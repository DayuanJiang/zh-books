"""For each glossary term, find aligned block pairs whose English has the term but whose Chinese lacks the preferred rendering.

    uv run --project framework/tools python term_consistency.py <report.json>
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import book  # noqa: E402
import config as book_config  # noqa: E402


def glossary_terms():
    terms = []
    for line in (BOOK / "glossary.md").read_text().splitlines():
        if not line.startswith("| ") or line.startswith("| 英文") or line.startswith("| ---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        english, chinese = cells[0], cells[1]
        en_forms = [re.sub(r"（.*?）|\(.*?\)", "", v).strip() for v in re.split(r" / ", english)]
        en_forms = [v for v in en_forms if v and "…" not in v]
        zh_forms = [re.sub(r"（.*?）|“|”|《|》", "", v).strip() for v in re.split(r" / |；|、", chinese)]
        zh_forms = [v for v in zh_forms if v and "动词" not in v]
        if en_forms and zh_forms:
            terms.append((english, en_forms, zh_forms))
    return terms


# Terms whose English column does not split cleanly, or whose plain-word uses are not the term.
OVERRIDES = {
    "causal / statistical base rate": (["causal base rate", "statistical base rate"], ["因果性基础比率", "统计性基础比率"]),
    "Amos Tversky": (["Amos Tversky"], ["特沃斯基"]),
    "decision making": (["decision making"], ["决策", "作决定", "做决定", "作出决定", "作出的决定"]),
    "intuition / intuitive judgment": (["intuitive judgment"], ["直觉判断"]),
}
SKIP = {"label", "character（虚构的角色）", "Speaking of …", "agent（把两个系统比作行动者）", "impression"}
CASE_SENSITIVE = {"Econs / Humans"}


def main():
    config = book_config.load(BOOK)
    terms = []
    for english, en_forms, zh_forms in glossary_terms():
        if english in SKIP:
            continue
        if english in OVERRIDES:
            en_forms, zh_forms = OVERRIDES[english]
        terms.append((english, en_forms, zh_forms))
    flags = defaultdict(list)
    totals = Counter()
    for entry in config["chapters"]:
        en = (BOOK / "en" / entry["file"]).read_text()
        zh = (BOOK / "zh-cn" / entry["file"]).read_text()
        source, _ = book.parse(en)
        target, _ = book.parse(zh)
        pairs = [(i, s, t) for i, (s, t) in enumerate(book.align(source, target, entry["id"], partial=True), 1) if t is not None]
        for english, en_forms, zh_forms in terms:
            flags_re = 0 if english in CASE_SENSITIVE else re.I
            patterns = [re.compile(r"\b" + re.escape(f).replace(r"\ ", r"[\s-]+") + r"(s|es)?\b", flags_re) for f in en_forms]
            for index, s, t in pairs:
                if not any(p.search(s.raw) for p in patterns):
                    continue
                totals[english] += 1
                # Accept any of the glossary forms, with spaces removed (系统 1 and 系统1 both count).
                zh_text = re.sub(r"\s", "", t.raw)
                if not any(re.sub(r"\s", "", z) in zh_text for z in zh_forms):
                    flags[entry["id"]].append({"block": index, "term": english, "preferred": " / ".join(zh_forms),
                                               "english": " ".join(s.raw.split())[:240], "chinese": " ".join(t.raw.split())[:240]})
    Path(sys.argv[1]).write_text(json.dumps(flags, ensure_ascii=False, indent=1))
    per_term = Counter(f["term"] for fl in flags.values() for f in fl)
    print(f"{sum(totals.values())} term occurrences checked, {sum(len(v) for v in flags.values())} blocks without the preferred rendering")
    print("terms most often rendered otherwise:", ", ".join(f"{t} {n}/{totals[t]}" for t, n in per_term.most_common(25)))


if __name__ == "__main__":
    main()
