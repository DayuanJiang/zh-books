"""After translating: find aligned blocks whose English has a glossary term or a person's name but whose Chinese
lacks the agreed rendering (see review/terms/README.md).

    uv run --project framework/tools python books/how-big-things-get-done/tools/term_consistency.py report.json
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
    ("megaproject", r"\bmegaprojects?\b", False, ["超大型项目"]),
    ("Iron Law", r"\bIron Law\b", True, ["铁律"]),
    ("cost overrun", r"\bcost overruns?\b", False, ["超支"]),
    ("benefit shortfall", r"\bbenefits? shortfalls?\b|\bunder benefits\b", False, ["效益不足"]),
    ("think slow, act fast", r"\bthink slow, act fast\b", False, ["慢思考，快行动"]),
    ("think fast, act slow", r"\bthink fast, act slow\b", False, ["快思考，慢行动"]),
    ("planning and delivery", r"\bplanning and delivery\b|\bfirst, planning; second, delivery\b", False, ["规划", "实施"]),
    ("window of doom", r"\bwindow of doom\b", False, ["厄运之窗"]),
    ("black swan", r"\bblack swans?\b", False, ["黑天鹅"]),
    ("fat-tailed", r"\bfat[- ]tail", False, ["肥尾"]),
    ("thin-tailed", r"\bthin[- ]tail", False, ["瘦尾"]),
    ("normal distribution", r"\bnormal distributions?\b", False, ["正态分布"]),
    ("regression to the mean", r"\bregression to the mean\b", False, ["均值回归"]),
    ("regression to the tail", r"\bregression to the tail\b", False, ["向尾部回归"]),
    ("power law", r"\bpower[- ]laws?\b", False, ["幂律"]),
    ("break-fix cycle", r"\bbreak-fix\b", False, ["边坏边修"]),
    ("commitment fallacy", r"\bcommitment fallacy\b", False, ["承诺谬误"]),
    ("lock-in", r"\block(?:s|ed|ing)?[- ]in\b", False, ["锁定"]),
    ("escalation of commitment", r"\bescalation of commitment\b", False, ["承诺升级"]),
    ("optimism bias", r"\boptimism bias\b", False, ["乐观偏差"]),
    ("planning fallacy", r"\bplanning fallacy\b", False, ["规划谬误"]),
    ("Hofstadter’s Law", r"\bHofstadter’s Law\b", False, ["侯世达定律"]),
    ("bias for action", r"\bbias for action\b", False, ["行动偏好"]),
    ("strategic misrepresentation", r"\bstrategic misrepresentation\b", False, ["策略性虚假陈述"]),
    ("System One / Two", r"\bSystems? (?:One|Two)\b", True, ["系统 1", "系统 2"]),
    ("WYSIATI", r"\bWYSIATI\b", True, ["所见即全部"]),
    ("sunk cost", r"\bsunk[- ]costs?\b", False, ["沉没成本"]),
    ("think from right to left", r"\bright to left\b", False, ["从右向左"]),
    ("backcasting", r"\bbackcasting\b", False, ["回推法"]),
    ("Pixar planning", r"\bPixar planning\b", False, ["皮克斯式规划"]),
    ("experiri", r"\bexperiri\b", False, ["experiri"]),
    ("iteration", r"\biterat(?:e|es|ed|ing|ion|ions|ive)\b", False, ["迭代"]),
    ("simulation", r"\bsimulat(?:e|es|ed|ing|ion|ions)\b", False, ["模拟"]),
    ("digital twin", r"\bdigital twins?\b", False, ["数字孪生"]),
    ("maximum virtual product", r"\bmaximum virtual product\b", False, ["最大虚拟产品"]),
    ("minimum viable product", r"\bminimum viable products?\b", False, ["最小可行产品"]),
    ("positive learning", r"\bpositive learning\b", False, ["正向学习"]),
    ("negative learning", r"\bnegative learning\b", False, ["负向学习"]),
    ("uniqueness bias", r"\buniqueness bias\b", False, ["独特性偏差"]),
    ("Eternal Beginner Syndrome", r"\bEternal Beginner\b", False, ["永远的新手综合征"]),
    ("frozen experience", r"\bfrozen experience\b", False, ["凝固的经验"]),
    ("tacit knowledge", r"\btacit knowledge\b", False, ["默会知识"]),
    ("phronesis", r"\bphronesis\b", False, ["phronesis", "实践智慧"]),
    ("masterbuilder", r"\bmasterbuilders?\b", False, ["建造大师"]),
    ("reference-class forecasting", r"\breference[- ]class forecast(?:s|ing)?\b|\bRCF\b", False, ["参照类别预测", "RCF"]),
    ("reference class", r"\breference class(?:es)?\b(?![- ]forecast)", False, ["参照类别"]),
    ("outside view", r"\boutside view\b", False, ["外部视角"]),
    ("inside view", r"\binside view\b", False, ["内部视角"]),
    ("anchoring", r"\banchor(?:s|ed|ing)?\b", False, ["锚"]),
    ("base rate", r"\bbase rates?\b", False, ["基础比率"]),
    ("unknown unknowns", r"\bunknown unknowns?\b", False, ["未知的未知"]),
    ("inchstone", r"\binchstones?\b", False, ["寸程碑"]),
    ("Hiding Hand", r"\bHiding Hand\b", True, ["隐藏之手"]),
    ("survivorship bias", r"\bsurvivorship bias\b", False, ["幸存者偏差"]),
    ("psychological safety", r"\bpsychological safety\b", False, ["心理安全感"]),
    ("modularity", r"\bmodular(?:ity)?\b", False, ["模块"]),
    ("Lego", r"\bLegos?\b", True, ["乐高"]),
    ("scale-free scalability", r"\bscale-free\b", False, ["无标度"]),
    ("heuristic", r"\bheuristics?\b", False, ["启发式"]),
    ("bespoke", r"\bbespoke(?:ness)?\b", False, ["定制"]),
    ("high-speed rail", r"\bhigh-speed rail\b", False, ["高铁"]),
    ("tunnel-boring machine", r"\bboring machines?\b", False, ["掘进机"]),
    ("Electric Lady", r"\bElectric Lady\b(?!land)", True, ["电子女士"]),
    ("Empire State Building", r"\bEmpire State\b", True, ["帝国大厦"]),
    ("Sydney Opera House", r"\bSydney Opera House\b", True, ["悉尼歌剧院"]),
    ("Guggenheim", r"\bGuggenheim\b", True, ["古根海姆"]),
    ("Pentagon", r"\bPentagon\b", True, ["五角大楼"]),
    ("Heathrow Terminal 5", r"\bT5\b|\bTerminal 5\b", True, ["T5", "5 号航站楼"]),
]

# Uses of a surname that are not the person: removed from the English before that surname is looked up.
NOT_THE_PERSON = {
    "White": r"White House",
    "Hall": r"Concert Hall|Hall of",
    "Stone": r"Set in Stone",
    "South": r"South (?:Carolina|Wales|Africa|Korea|America)",
    "Ørsted": r"(?<!Christian )Ørsted",
}


def people():
    """(label, English surname pattern, accepted Chinese surnames): people sharing a surname are checked together."""
    groups = defaultdict(lambda: [[], set()])
    for row in csv.DictReader((BOOK / "review" / "terms" / "people-zh.tsv").open(), delimiter="\t"):
        name, chinese = row["name"], row["chinese"]
        if row["basis"] not in ("established", "transliterated") or len(name.split()) < 2:
            continue
        surname = name.split()[-1]
        group = groups[surname]
        group[0].append(name)
        group[1].add(re.split(r"[·.]", chinese)[-1].strip() if "·" in chinese else chinese)
    return [(" / ".join(names), surname, sorted(forms)) for surname, (names, forms) in groups.items()]


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
            for label, surname, forms in names:
                text = re.sub(NOT_THE_PERSON[surname], "", en) if surname in NOT_THE_PERSON else en
                if re.search(rf"\b{re.escape(surname)}\b", text):
                    found.append((f"name: {label}", forms))
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
