"""After translating: find aligned blocks whose English has a glossary term or a person's name but whose Chinese
lacks the agreed rendering (see review/terms/README.md).

    uv run --project framework/tools python -I books/never-split-the-difference/tools/term_consistency.py report.json
"""

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK.parents[1] / "framework" / "tools"))
sys.path.insert(0, str(BOOK / "tools"))
import book  # noqa: E402
import config as book_config  # noqa: E402
from term_stats import person_pattern  # noqa: E402  (the same name patterns as people.tsv)

# (label, English pattern, case sensitive, accepted Chinese forms): the book's own terms, where one rendering matters.
TERMS = [
    ("counterpart", r"\bcounterparts?\b", False, ["对方"]),
    ("hostage negotiator", r"\bhostage negotiators?\b", False, ["谈判专家"]),
    ("Tactical Empathy", r"\btactical empathy\b", False, ["战术共情"]),
    ("empathy", r"\bempath(?:y|ize|izes|ized|izing|ic|etic)\b", False, ["共情"]),
    ("sympathy", r"\bsympath\w*", False, ["同情"]),
    ("forced empathy", r"\bforced empathy\b", False, ["强制共情"]),
    ("emotional intelligence", r"\bemotional intelligence\b", False, ["情商"]),
    ("active listening", r"\bactive listening\b", False, ["积极倾听"]),
    ("BCSM", r"\bBehavioral Change Stairway\b|\bBCSM\b", False, ["行为改变阶梯模型", "BCSM"]),
    ("rapport", r"\brapport\b", False, ["融洽"]),
    ("unconditional positive regard", r"\bunconditional positive regard\b", False, ["无条件积极关注"]),
    ("DJ voice", r"\bFM DJ\b|\bDJ(?:’s)? voice\b", False, ["DJ"]),
    ("mirroring", r"\bmirror(?:ing|s|ed)?\b", False, ["镜像"]),
    ("labeling", r"\b(?:mis)?label(?:s|ed|ing|led|ling)?\b", False, ["标注", "标错"]),
    ("accusation audit", r"\baccusation audits?\b", False, ["指责清单"]),
    ("paraphrase", r"\bparaphras\w*", False, ["转述"]),
    ("summary", r"\bsummar(?:y|ies|ize|izes|ized|izing)\b", False, ["总结"]),
    ("That’s right", r"\bthat’s right\b", False, ["没错"]),
    ("You’re right", r"\byou’re right\b", False, ["你说得对"]),
    ("proof of life", r"\bproofs?[- ]of[- ]life\b", False, ["生存证明"]),
    ("counterfeit Yes", r"\bcounterfeit [“\"]?yes\b", False, ["假意的“是”"]),
    ("confirmation Yes", r"\bconfirmation [“\"]?yes\b", False, ["确认的“是”"]),
    ("commitment Yes", r"\bcommitment [“\"]?yes\b", False, ["承诺的“是”"]),
    ("No-oriented", r"[“\"]No[”\"]-oriented\b", False, ["引出“不”"]),
    ("Yes is nothing without How", r"\bnothing without [“\"]?how\b", False, ["没有“怎么做”"]),
    ("No deal is better than a bad deal", r"\bno deal is better than a bad deal\b", False, ["没有交易也比坏交易好"]),
    ("never split the difference", r"\bnever split the difference\b", False, ["绝不折中"]),
    ("split the difference", r"\bsplit(?:ting)? the difference\b", False, ["折中"]),
    ("calibrated questions", r"\bcalibrated\b", False, ["校准"]),
    ("How am I supposed to do that", r"\bhow (?:am I|are we|was I) supposed to\b", False, ["我该怎么", "我们该怎么"]),
    ("illusion of control", r"\billusion of control\b", False, ["掌控的错觉"]),
    ("unbelief", r"\bunbelie\w*", False, ["不信"]),
    ("hostage mentality", r"\bhostage mentality\b", False, ["人质心态"]),
    ("reciprocity", r"\breciproc\w*", False, ["互惠"]),
    ("behind the table", r"\bbehind the table\b", False, ["桌子后面"]),
    ("Rule of Three", r"\bRule of Three\b", False, ["三次法则"]),
    ("7-38-55", r"\b7-38-55\b", False, ["7-38-55"]),
    ("Pinocchio Effect", r"\bPinocchio Effect\b", False, ["匹诺曹效应"]),
    ("Chris discount", r"\bChris discount\b", False, ["克里斯折扣"]),
    ("bid against themselves", r"\bbid(?:ding)? against (?:themselves|himself|herself|yourself)\b", False, ["压价"]),
    ("System 1 / System 2", r"\bSystem [12]\b", True, ["系统 1", "系统 2"]),
    ("Cognitive Bias", r"\bcognitive bias(?:es)?\b", False, ["认知偏差"]),
    ("Framing Effect", r"\bframing effect\b", False, ["框架效应"]),
    ("Prospect Theory", r"\bprospect theory\b", False, ["前景理论"]),
    ("Certainty Effect", r"\bcertainty effect\b", False, ["确定性效应"]),
    ("Loss Aversion", r"\bloss aversion\b|\baversion to loss\b", False, ["损失厌恶"]),
    ("amygdala", r"\bamygdala\b", False, ["杏仁核"]),
    ("Ultimatum Game", r"\bUltimatum Game\b", False, ["最后通牒博弈"]),
    ("fair", r"\bfair(?:ness)?\b|\bunfair\w*", False, ["公平"]),
    ("F-word", r"\bF-(?:word|bomb)\b", False, ["F 字", "F 炸弹"]),
    ("anchor", r"\banchor(?:s|ed|ing)?\b", False, ["锚"]),
    ("nonmonetary", r"\bnon-?monetary\b", False, ["非金钱"]),
    ("BATNA", r"\bBATNA\b", True, ["BATNA"]),
    ("ZOPA", r"\bZOPA\b", True, ["ZOPA"]),
    ("Analyst", r"\bAnalysts?\b", True, ["分析型"]),
    ("Accommodator", r"\bAccommodators?\b", True, ["迁就型"]),
    ("Assertive (type)", r"\bAssertives?\b", True, ["强势"]),
    ("strategic umbrage", r"\bstrategic umbrage\b", False, ["策略性动怒"]),
    ("“I” messages", r"[“\"]I[”\"] messages?\b", False, ["“我”信息"]),
    ("Ackerman", r"\bAckerman (?:model|system|bargaining|plan|process|offers?)\b", False, ["阿克曼"]),
    ("Black Swan", r"\bBlacks? Swans?\b(?! Group)", True, ["黑天鹅"]),
    ("The Black Swan Group", r"\bBlack Swan Group\b", True, ["黑天鹅集团"]),
    ("known / unknown", r"\b(?:known|unknown) (?:knowns?|unknowns?)\b", False, ["已知的已知", "已知的未知", "未知的未知"]),
    ("leverage (noun)", r"\bleverage\b(?! (?:them|it|the|that|their|this)\b)", False, ["筹码"]),
    ("positive leverage", r"\bpositive leverage\b", False, ["正面筹码"]),
    ("negative leverage", r"\bnegative leverage\b", False, ["负面筹码"]),
    ("normative leverage", r"\bnormative leverage\b", False, ["规范筹码"]),
    ("religion", r"\breligio\w*", False, ["信仰", "宗教"]),
    ("similarity principle", r"\bsimilarity principle\b", False, ["相似性原则"]),
    ("Getting to Yes", r"\bGetting to Yes\b", True, ["《谈判力》"]),
    ("CNU", r"\bCNU\b|\bCrisis Negotiation Unit\b", True, ["危机谈判小组", "CNU"]),
    ("JTTF", r"\bJTTF\b|\bJoint Terrorism Task Force\b", True, ["联合反恐特遣队", "JTTF"]),
    ("Key Lessons", r"\bKey Lessons\b", True, ["本章要点"]),
]

# Chinese forms accepted for a person besides the parts of the name in people-zh.tsv.
ALSO = {"Joe Businessman": ["乔"], "Mr. Smith": ["史密斯"]}


def people():
    """(name, compiled English pattern, chapters or None, accepted Chinese forms) for every person in people-zh.tsv.
    The Chinese forms are the parts of the Chinese name of two characters or more (the given name or the surname,
    whichever the English uses), or the whole name when it is one part."""
    table = list(csv.DictReader((BOOK / "review" / "terms" / "people-zh.tsv").open(), delimiter="\t"))
    names = [row["name"] for row in table]
    out = []
    for row in table:
        pattern, chapters = person_pattern(row["name"], names)
        parts = [p for p in re.split(r"[·\s]", row["chinese"]) if re.search(r"[一-鿿]", p) and len(p) >= 2]
        out.append((row["name"], re.compile(pattern), chapters, (parts or [row["chinese"]]) + ALSO.get(row["name"], [])))
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
            found += [(f"name: {name}", forms) for name, rx, chapters, forms in names
                      if (not chapters or entry["id"] in chapters) and rx.search(en)]
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
