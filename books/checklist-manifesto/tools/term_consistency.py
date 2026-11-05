"""After translating: find aligned blocks whose English has a glossary term or a person's name but whose Chinese
lacks the agreed rendering (see review/terms/README.md).

    uv run --project framework/tools python books/checklist-manifesto/tools/term_consistency.py report.json
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

# (label, English pattern, case sensitive, accepted Chinese forms): the book's own terms, where one rendering matters.
TERMS = [
    ("checklist", r"\bchecklists?\b", False, ["清单"]),
    ("pause point", r"\bpause points?\b", False, ["暂停点"]),
    ("DO-CONFIRM", r"\bDO-CONFIRM\b", True, ["先做后确认"]),
    ("READ-DO", r"\bREAD-DO\b", True, ["边读边做"]),
    ("killer items", r"\bkiller items?\b", False, ["致命项"]),
    ("forcing function", r"\bforcing functions?\b", False, ["强制功能"]),
    ("construction schedule", r"\bconstruction schedules?\b", False, ["施工进度表"]),
    ("submittal schedule", r"\bsubmittal schedules?\b", False, ["报审进度表"]),
    ("Master Builder", r"\bMaster Builders?\b", True, ["总建造师"]),
    ("Master Physician", r"\bMaster Physician\b", True, ["总医师"]),
    ("ignorance", r"\bignorance\b", False, ["无知"]),
    ("ineptitude", r"\bineptitude\b", False, ["无能"]),
    ("eptitude", r"\beptitude\b", False, ["有能"]),
    ("complexity", r"\bcomplexit(?:y|ies)\b", False, ["复杂"]),
    # where both words stand in one block, the Zimmerman and Glouberman distinction is in play
    ("complicated next to complex", r"(?s)\bcomplicated\b.*\bcomplex\b|\bcomplex\b.*\bcomplicated\b", False, ["繁杂"]),
    ("cognitive net", r"\bcognitive net\b", False, ["认知防护网"]),
    ("stupid stuff", r"\b(?:stupid|dumb) (?:but critical )?stuff\b", False, ["傻瓜都知道"]),
    ("communication checks", r"\bcommunication checks?\b", False, ["沟通检查"]),
    ("command-and-control", r"\bcommand-and-control\b", False, ["命令与控制"]),
    ("team briefing", r"\bteam briefing\b", False, ["团队简报"]),
    ("activation phenomenon", r"\bactivation phenomenon\b", False, ["激活现象"]),
    ("discipline", r"\bdiscipline\b", False, ["纪律"]),
    ("autonomy", r"\bautonomy\b", False, ["自主"]),
    ("too much airplane", r"\btoo much airplane\b", False, ["一个人飞不了"]),
    ("Model 299", r"\bModel 299\b", True, ["299 型", "299型"]),
    ("safe surgery checklist", r"\bsafe surgery checklist\b", False, ["安全手术清单"]),
    ("Safe Surgery Saves Lives", r"\bSafe Surgery Saves Lives\b", True, ["安全手术拯救生命"]),
    ("WHO", r"\bWHO\b|\bWorld Health Organization\b", True, ["世卫组织", "世界卫生组织"]),
    ("Keystone Initiative", r"\bKeystone Initiative\b", True, ["基石计划"]),
    ("Cleared for Takeoff", r"\bCleared for Take ?off\b", False, ["准予起飞"]),
    ("central line", r"\bcentral lines?\b", False, ["中心静脉导管"]),
    ("ICU", r"\bICUs?\b", True, ["ICU", "重症监护"]),
    ("anesthesiologist", r"\banesthesiologists?\b", False, ["麻醉科医生", "麻醉医生"]),
    ("anesthetist", r"\banesthetists?\b", False, ["麻醉师"]),
    ("circulating nurse", r"\bcirculating nurses?\b", False, ["巡回护士"]),
    ("scrub nurse", r"\bscrub nurses?\b", False, ["器械护士"]),
    ("complication", r"\bcomplications?\b", False, ["并发症"]),
    ("vital signs", r"\bvital signs?\b", False, ["生命体征"]),
    ("Code Blue", r"\bCode Blue\b", True, ["蓝色代码", "Code Blue"]),
    ("Hawthorne effect", r"\bHawthorne effect\b", False, ["霍桑效应"]),
    ("pilot study", r"\bpilot (?:study|hospitals?|sites?)\b", False, ["试点"]),
    ("pilot not flying", r"\bpilot not flying\b", False, ["非操纵飞行员"]),
    ("cockpit voice recorder", r"\bcockpit voice recorder\b", False, ["驾驶舱话音记录器"]),
    ("ditching", r"\bditching\b", False, ["迫降"]),
    ("value investors", r"\bvalue investors?\b", False, ["价值投资者"]),
    ("margin of safety", r"\bmargin of safety\b", False, ["安全边际"]),
    ("cocaine brain", r"\bcocaine brain\b", False, ["可卡因大脑"]),
    ("mental checklist", r"\bmental checklist\b", False, ["思维清单"]),
    ("Airline Captains", r"\bAirline Captains?\b", True, ["机长型"]),
    ("building failure", r"\bbuilding failures?\b", False, ["建筑失效"]),
    ("tuned mass damper", r"\btuned mass damper\b", False, ["调谐质量阻尼器"]),
]


def people():
    """(English name, surname pattern, Chinese surname) for every person in the names table with a Chinese name."""
    out = []
    for row in csv.DictReader((BOOK / "review" / "terms" / "people-zh.tsv").open(), delimiter="\t"):
        name, chinese = row["name"], row["chinese"]
        if row["basis"] not in ("established", "transliterated") or "·" not in chinese:
            continue
        words = [w for w in re.sub(r"[“\"][^”\"]*[”\"]", "", name).split() if w not in ("III", "Jr.")]
        out.append((name, rf"\b{re.escape(words[-1])}\b", re.split(r"[·.]", chinese)[-1]))
    return out


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
            found += [(f"name: {name}", [surname]) for name, rx, surname in names if re.search(rx, en)]
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
    main(sys.argv[1])
