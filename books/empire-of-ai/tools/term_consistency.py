"""After translating: find aligned blocks whose English has a glossary term or a person's name but whose Chinese
lacks the agreed rendering (see review/terms/README.md).

    uv run --project framework/tools python books/empire-of-ai/tools/term_consistency.py report.json
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
    ("empire", r"\bempires?\b", False, ["帝国"]),
    ("extractivism", r"\bextractivis[mt]", False, ["攫取主义"]),
    ("dispossession", r"\bdispossess", False, ["剥夺"]),
    ("Global South", r"\bGlobal South\b", True, ["全球南方"]),
    ("AGI", r"\bAGI\b", True, ["AGI", "通用人工智能"]),
    ("scaling laws", r"\bscaling laws?\b", False, ["规模定律"]),
    ("compute (noun)", r"\bcompute\b(?! (?:the|a|an|it|its|their)\b)", True, ["算力", "计算"]),
    ("data center", r"\bdata centers?\b", False, ["数据中心"]),
    ("hyperscaler", r"\bhyperscalers?\b", False, ["超大规模云服务商"]),
    ("large language model", r"\blarge language models?\b", False, ["大语言模型"]),
    ("generative AI", r"\bgenerative AI\b", False, ["生成式 AI", "生成式AI"]),
    ("AI safety", r"\bAI safety\b", False, ["AI 安全", "AI安全"]),
    ("Trust and Safety", r"\bTrust (?:and|&) Safety\b", False, ["信任与安全"]),
    ("existential risk", r"\bexistential risks?\b", False, ["生存风险"]),
    ("effective altruism", r"\beffective altruis", False, ["有效利他主义"]),
    ("Doomers", r"\bDoomers?\b", True, ["末日派"]),
    ("Boomers", r"\bBoomers?\b", True, ["繁荣派"]),
    ("Safety clan", r"\bSafety clan\b", True, ["安全派"]),
    ("Applied division", r"\bApplied division\b", True, ["应用部门"]),
    ("Research division", r"\bResearch division\b", True, ["研究部门"]),
    ("The Blip", r"\bThe Blip\b", True, ["插曲"]),
    ("Omnicrisis", r"\bOmnicrisis\b", True, ["全面危机"]),
    ("The Divorce", r"\bThe Divorce\b", True, ["分家"]),
    ("RLHF", r"\bRLHF\b|reinforcement learning from human feedback", False, ["RLHF", "基于人类反馈的强化学习"]),
    ("deep learning", r"\bdeep learning\b", False, ["深度学习"]),
    ("neural network", r"\bneural networks?\b", False, ["神经网络"]),
    ("connectionism", r"\bconnectionis", False, ["联结主义"]),
    ("hallucination", r"\bhallucinations?\b", False, ["幻觉"]),
    ("data annotation", r"\bannotat(?:e|ed|ing|ion|ions|ors?)\b", False, ["标注"]),
    ("content moderation", r"\bcontent moderation\b", False, ["内容审核"]),
    ("nonprofit", r"\bnonprofit\b", False, ["非营利"]),
    ("capped-profit", r"\bcapped[- ]profit\b", False, ["利润封顶"]),
    ("tender offer", r"\btender offer\b", False, ["收购要约"]),
    ("clawback", r"\bclawback\b", False, ["追回条款"]),
    ("superalignment", r"\bsuperalignment\b", False, ["超级对齐"]),
    ("stochastic parrots", r"\bstochastic parrots\b", False, ["随机鹦鹉"]),
    ("Superassistant", r"\bSuperassistant\b", True, ["超级助手"]),
    ("not consistently candid", r"\bconsistently candid\b", False, ["没有始终坦诚"]),
]


def people():
    """(English surname pattern, Chinese surname) for every person in the names table with a Chinese name."""
    out = []
    for row in csv.DictReader((BOOK / "review" / "terms" / "people-zh.tsv").open(), delimiter="\t"):
        name, chinese = row["name"], row["chinese"]
        if row["basis"] not in ("established", "transliterated") or "·" not in chinese:
            continue
        surname = re.sub(r"[“\"][^”\"]*[”\"]", "", name).split()[-1]
        out.append((name, rf"\b{re.escape(surname)}\b", re.split(r"[·.]", chinese)[-1]))
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
    if len(sys.argv) != 2 or sys.argv[1].startswith("-"):
        raise SystemExit(__doc__)
    main(sys.argv[1])
