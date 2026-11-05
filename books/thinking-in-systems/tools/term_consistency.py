"""After translating: find aligned blocks whose English has a glossary term or a person's name but whose Chinese
lacks the agreed rendering (see review/terms/README.md).

    uv run --project framework/tools python -I books/thinking-in-systems/tools/term_consistency.py report.json
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
    ("stock", r"\bstocks?\b(?! (?:market|price|options)\b)", False, ["存量"]),
    ("inflow / outflow", r"\b(?:in|out)flows?\b", False, ["流入", "流出"]),
    ("inventory", r"\binventor(?:y|ies)\b", False, ["库存"]),
    ("feedback loop", r"\bfeedback loops?\b", False, ["回路"]),
    ("balancing loop", r"\bbalancing (?:feedback )?loops?\b", False, ["调节回路"]),
    ("reinforcing loop", r"\breinforcing (?:feedback )?loops?\b", False, ["增强回路"]),
    ("dynamic equilibrium", r"\bdynamic equilibrium\b", False, ["动态平衡"]),
    ("system dynamics", r"\bsystems? dynamics\b", False, ["系统动力学"]),
    ("systems thinking", r"\bsystems? thinking\b", False, ["系统思考"]),
    ("systems zoo", r"\bsystems? zoo\b", False, ["系统动物园"]),
    ("element", r"\belements?\b", False, ["要素"]),
    ("interconnection", r"\binterconnect\w*", False, ["相互连接", "连接"]),
    ("function", r"\bfunctions?\b", False, ["功能"]),
    ("purpose", r"\bpurposes?\b", False, ["目的"]),
    ("goal", r"\bgoals?\b", False, ["目标"]),
    ("delay", r"\bdelays?\b", False, ["延迟"]),
    ("oscillation", r"\boscillat\w+", False, ["振荡"]),
    ("overshoot", r"\bovershoot\w*", False, ["过冲"]),
    ("shifting dominance", r"\bshifting dominance\b", False, ["主导地位的转换"]),
    ("resilience", r"\bresilien\w+", False, ["韧性"]),
    ("self-organization", r"\bself-organi[sz]\w+", False, ["自组织"]),
    ("hierarchy", r"\bhierarch\w+", False, ["层级"]),
    ("suboptimization", r"\bsuboptimi[sz]\w+", False, ["次优化"]),
    ("bounded rationality", r"\bbounded rationality\b", False, ["有限理性"]),
    ("limiting factor", r"\blimiting factors?\b", False, ["限制因素"]),
    ("nonlinear", r"\bnonlinear\w*", False, ["非线性"]),
    ("boundary", r"\bboundar(?:y|ies)\b", False, ["边界"]),
    ("mental model", r"\bmental models?\b", False, ["心智模型"]),
    ("mind-set", r"\bmind-?sets?\b", False, ["思维模式"]),
    ("paradigm", r"\bparadigm\w*", False, ["范式"]),
    ("leverage point", r"\bleverage points?\b", False, ["杠杆点"]),
    ("archetype", r"\barchetyp\w+", False, ["基模"]),
    ("trap", r"\btraps?\b", False, ["陷阱"]),
    ("the way out", r"(?<!on the )\bway out\b", False, ["出路"]),
    ("policy resistance", r"\bpolicy resistance\b", False, ["政策阻力"]),
    ("fixes that fail", r"\bfixes that fail\b", False, ["失效的对策"]),
    ("tragedy of the commons", r"\btragedy of the commons\b", False, ["公地悲剧"]),
    ("mutual coercion", r"\bmutual coercion\b", False, ["相互同意的相互强制"]),
    ("drift to low performance", r"\bdrift\w* (?:to|toward) low performance\b", False, ["滑向低绩效"]),
    ("eroding goals", r"\beroding goals?\b", False, ["目标侵蚀"]),
    ("escalation", r"\bescalat\w+", False, ["升级"]),
    ("success to the successful", r"\bsuccess[- ]to[- ]the[- ]successful\b", False, ["富者愈富"]),
    ("competitive exclusion", r"\bcompetitive exclusion\b", False, ["竞争排斥"]),
    ("intervenor", r"\bintervenors?\b", False, ["干预者"]),
    ("shifting the burden", r"\bshifting the burden\b", False, ["转嫁负担", "把负担转嫁给"]),
    ("addiction", r"\baddict\w*", False, ["上瘾", "瘾"]),
    ("rule beating", r"\brule[- ]beat\w*", False, ["钻规则的空子", "钻空子"]),
    ("wrong goal", r"\bwrong goals?\b", False, ["错误的目标"]),
    ("carrying capacity", r"\bcarrying capacit\w+", False, ["承载能力"]),
    ("renewable", r"\b(?:non)?renewable\b", False, ["可再生"]),
    ("capital stock", r"\bcapital stocks?\b", False, ["资本存量"]),
    ("discrepancy", r"\bdiscrepanc(?:y|ies)\b", False, ["差距"]),
    ("buffer", r"\bbuffers?\b", False, ["缓冲"]),
    ("information flow", r"\binformation flows?\b", False, ["信息流"]),
    ("intrinsic responsibility", r"\bintrinsic responsibility\b", False, ["内在责任"]),
    ("Slinky", r"\bSlink(?:y|ies)\b", True, ["弹簧圈"]),
    ("GNP", r"\bGNP\b", True, ["GNP", "国民生产总值"]),
    ("International Herald Tribune", r"\bHerald Tribune\b", False, ["国际先驱论坛报"]),
]


def people():
    """(English name, surname pattern, Chinese surname) for every person in the names table."""
    out = []
    for row in csv.DictReader((BOOK / "review" / "terms" / "people-zh.tsv").open(), delimiter="\t"):
        name, chinese = row["name"], row["chinese"]
        if row["basis"] not in ("established", "transliterated"):
            continue
        english = re.sub(r",? Jr\.$", "", name).split()[-1]
        if name == "Lord Peston":
            english, surname = "Peston", "佩斯顿"
        else:
            surname = re.split(r"[·.]", chinese)[-1].strip()
        # Calvin and Hobbes speak in capitals (CALVIN:, HOBBES:).
        out.append((name, re.compile(rf"\b(?:{re.escape(english)}|{re.escape(english.upper())})\b"), surname))
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
            found += [(f"name: {name}", [surname]) for name, rx, surname in names if rx.search(en)]
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
