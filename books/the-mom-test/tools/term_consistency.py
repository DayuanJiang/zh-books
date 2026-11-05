"""After translating: find aligned blocks whose English has a glossary term or a person's name but whose Chinese
lacks the agreed rendering (see review/terms/README.md).

    uv run --project framework/tools python -I books/the-mom-test/tools/term_consistency.py report.json
"""

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
import book  # noqa: E402
import config as book_config  # noqa: E402

NOT_A_SURNAME = {"Read", "C"}  # "Read the news", "customer C"

# (label, English pattern, case sensitive, accepted Chinese forms): the book's own terms, where one rendering matters.
TERMS = [
    ("The Mom Test", r"\bmom test\b", False, ["妈妈测试"]),
    ("customer conversation", r"\bcustomer conversations?\b", False, ["客户对话", "客户的对话"]),
    ("Customer Development", r"\bCustomer Development\b", True, ["客户开发"]),
    ("Lean Startup", r"\bLean Startup\b", True, ["精益创业"]),
    ("bad data", r"\bbad data\b", False, ["坏数据"]),
    ("compliment", r"\bcompliment", False, ["恭维", "夸"]),
    ("fluff", r"\bfluff", False, ["空话", "空泛"]),
    ("false positive", r"\bfalse positives?\b", False, ["假阳性"]),
    ("false negative", r"\bfalse negatives?\b", False, ["假阴性"]),
    ("deflect", r"\bdeflect", False, ["挡开"]),
    ("anchor", r"\banchor", False, ["锚定", "锚点", "抓住"]),
    ("feature request", r"\bfeature requests?\b", False, ["功能需求"]),
    ("feature creep", r"\bfeature[- ]creep\b", False, ["功能蔓延"]),
    ("The Pathos Problem", r"\bPathos Problem\b", True, ["悲情问题"]),
    ("pitch mode", r"\bpitch mode\b", False, ["推销模式"]),
    ("lukewarm", r"\blukewarm\b", False, ["不冷不热"]),
    ("premature zoom", r"\bpremature(?:ly)? zoom", False, ["过早聚焦"]),
    ("elephant", r"\belephant\b", False, ["房间里的大象", "大象"]),
    ("product risk", r"\bproduct risks?\b", False, ["产品风险"]),
    ("market risk", r"\bmarket risks?\b", False, ["市场风险"]),
    ("must-solve", r"\bmust-solve\b", False, ["非解决不可", "必须马上解决"]),
    ("Keeping it casual", r"\bkeep(?:ing|s)? it casual\b", False, ["轻松随意"]),
    ("anti-pattern", r"\banti-pattern\b", False, ["反模式"]),
    ("commitment", r"\bcommitments?\b", False, ["承诺"]),
    ("advancement", r"\badvancement\b", False, ["推进"]),
    ("next steps", r"\bnext steps?\b", False, ["下一步"]),
    ("zombie leads", r"\bzombie leads?\b", False, ["僵尸线索"]),
    ("friend-zone", r"\bfriend-zone", False, ["好人卡"]),
    ("stalling tactic", r"\bstalling tactic", False, ["拖延战术"]),
    ("earlyvangelists", r"\bearlyvangelists?\b", False, ["早期布道者"]),
    ("customer segment", r"\bcustomer segments?\b", False, ["客户群"]),
    ("segmentation", r"\bsegmentation\b", False, ["客户细分", "细分"]),
    ("Customer Slicing", r"\bCustomer Slicing\b", False, ["客户切分"]),
    ("who-where", r"\bwho-where\b", False, ["在哪儿"]),
    ("workaround", r"\bworkarounds?\b", False, ["变通办法"]),
    ("warm intro", r"\bwarm intros?\b", False, ["熟人引荐"]),
    ("cold call", r"\bcold calls?\b", False, ["陌生电话"]),
    ("landing page", r"\blanding pages?\b", False, ["落地页"]),
    ("pedestal", r"\bpedestal\b", False, ["捧高"]),
    ("learning bottleneck", r"\bbottleneck", False, ["信息瓶颈", "卡住信息"]),
    ("going through the motions", r"\bgoing through the motions\b", False, ["走过场"]),
    ("desk research", r"\bdesk research\b", False, ["案头调研"]),
    ("opportunity cost", r"\bopportunity cost\b", False, ["机会成本"]),
    ("job-to-be-done", r"\bjob-to-be-done\b", False, ["待完成的任务"]),
    ("Rule of thumb", r"\bRule of thumb\b", False, ["经验法则"]),
    # added after translating, from the editors' suggestions
    ("rewarding", r"\brewarding\b", False, ["有成就感"]),
    ("best guess", r"\bbest[- ]guess", False, ["最佳猜测"]),
    ("exact / key quotes", r"\b(?:exact|key)(?: customer)? quotes?\b", False, ["原话"]),
    ("Don't call me, I'll call you", r"\bDon[’']t call me\b", False, ["别给我打电话，我会打给你"]),
]


def name_pattern(name, names):
    """Full name, surname, or a given name no one else in the list has; single names not followed by a surname."""
    parts = re.sub(r"^(?:[A-Z]\. )+", "", name).split()
    if parts == [name]:
        return rf"\b{re.escape(name)}\b(?! [A-Z][a-z])"
    givens = Counter(n.split()[0] for n in names)
    options = [re.escape(name)]
    if parts[-1] not in NOT_A_SURNAME:
        options.append(re.escape(parts[-1]))
    if len(parts) > 1 and givens[parts[0]] == 1:
        options.append(re.escape(parts[0]))
    return r"\b(?:" + "|".join(options) + r")\b"


def people():
    """(English name, pattern, accepted Chinese forms) for every person in the names table with a Chinese name."""
    rows = [row for row in csv.DictReader((BOOK / "review" / "terms" / "people-zh.tsv").open(), delimiter="\t")
            if row["basis"] in ("established", "transliterated") and row["chinese"]]
    names = [row["name"] for row in rows]
    return [(row["name"], re.compile(name_pattern(row["name"], names)), row["chinese"].split("·")) for row in rows]


def main(report):
    config = book_config.load(BOOK)
    checks = [(label, re.compile(rx, 0 if case else re.I), forms) for label, rx, case, forms in TERMS]
    names = people()
    flags, totals = defaultdict(list), Counter()
    for entry in config["chapters"]:
        zh_path = BOOK / "zh-cn" / entry["file"]
        if not zh_path.exists():
            continue
        source, _ = book.parse((BOOK / "en" / entry["file"]).read_text())
        target, _ = book.parse(zh_path.read_text())
        pairs = [(i, s, t) for i, (s, t) in enumerate(book.align(source, target, entry["id"], partial=True), 1) if t is not None]
        for index, s, t in pairs:
            en, zh = s.raw, re.sub(r"\s", "", t.raw)
            found = [(label, forms) for label, rx, forms in checks if rx.search(en)]
            found += [(f"name: {name}", forms) for name, rx, forms in names if rx.search(en)]
            for label, forms in found:
                totals[label] += 1
                if not any(re.sub(r"\s", "", f) in zh for f in forms):
                    flags[entry["id"]].append({"block": index, "term": label, "preferred": " / ".join(forms),
                                               "english": " ".join(en.split())[:240], "chinese": " ".join(t.raw.split())[:240]})
    Path(report).write_text(json.dumps(flags, ensure_ascii=False, indent=1))
    per = Counter(f["term"] for fl in flags.values() for f in fl)
    print(f"{sum(totals.values())} occurrences checked, {sum(len(v) for v in flags.values())} blocks without the agreed rendering")
    print("most often rendered otherwise:", ", ".join(f"{t} {n}/{totals[t]}" for t, n in per.most_common(30)))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1].startswith("-"):
        raise SystemExit(__doc__)
    main(sys.argv[1])
