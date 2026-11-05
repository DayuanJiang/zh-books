"""After translating: find aligned blocks whose English has a glossary term or a person's name but whose Chinese
lacks the agreed rendering (see review/terms/README.md).

    uv run --project framework/tools python -I books/bad-blood/tools/term_consistency.py report.json
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
    ("Theranos", r"\bTheranos\b", True, ["Theranos"]),
    ("Edison", r"\bEdisons?\b", True, ["Edison"]),
    ("miniLab", r"\bminiLabs?\b", True, ["miniLab"]),
    ("4S", r"\b4S\b", True, ["4S"]),
    ("gluebot", r"\bgluebot\b|\bglue[- ]?(?:dispensing )?robot", False, ["点胶机器人"]),
    ("nanotainer", r"\bnanotainers?\b", False, ["nanotainer", "微型采血管"]),
    ("cartridge", r"\bcartridges?\b", False, ["卡盒"]),
    ("reader (device)", r"(?<!Journal )(?<!our )\breaders?\b", False, ["读取器"]),
    ("wellness center", r"\bwellness cent", False, ["健康中心"]),
    ("Frat Pack", r"\bFrat Pack\b", True, ["兄弟会帮"]),
    ("Jurassic Park", r"\bJurassic Park\b", True, ["侏罗纪公园"]),
    ("Normandy (room)", r"\bNormandy\b", True, ["诺曼底"]),
    ("finger-stick", r"\bfinger[- ]?sticks?\b", False, ["指尖"]),
    ("venous draw", r"\bvenous\b|\bvenipuncture\b", False, ["静脉"]),
    ("immunoassay", r"\bimmunoassays?\b", False, ["免疫测定"]),
    ("general chemistry", r"\bgeneral[- ]chemistry\b", False, ["生化"]),
    ("analyzer", r"\banalyzers?\b", False, ["分析仪"]),
    ("dilution", r"\bdilut", False, ["稀释"]),
    ("proficiency testing", r"\bproficiency[- ]test", False, ["能力验证"]),
    ("quality control", r"\bquality[- ]control\b", False, ["质控"]),
    ("validation", r"\bvalidat", False, ["验证"]),
    ("coefficient of variation", r"\bcoefficients? of variation\b", False, ["变异系数"]),
    ("lab director", r"\blab(?:oratory)? directors?\b", False, ["实验室主任"]),
    ("clinical laboratory scientist", r"\bclinical laboratory scientists?\b|\bCLSs?\b", True, ["CLS", "临床检验技师"]),
    ("laboratory-developed test", r"\b[Ll]aboratory[- ]developed tests?\b|\bLDTs?\b", True, ["实验室自建检测", "LDT"]),
    ("CLIA", r"\bCLIA\b", True, ["CLIA"]),
    ("CMS", r"\bCMS\b", True, ["CMS"]),
    ("FDA", r"\bFDA\b", True, ["FDA"]),
    ("startup", r"\bstart-?ups?\b", False, ["创业公司"]),
    ("venture capitalist", r"\bventure capitalists?\b", False, ["风险投资人", "风投"]),
    ("valuation", r"\bvaluations?\b", False, ["估值"]),
    ("unicorn", r"\bunicorns?\b", False, ["独角兽"]),
    ("trade secrets", r"\btrade secrets?\b", False, ["商业秘密"]),
    ("confidentiality agreement", r"\bconfidentiality agreements?\b|\bnondisclosure agreements?\b", False, ["保密协议"]),
    ("deposition", r"\bdeposition", False, ["取证"]),
    ("affidavit", r"\baffidavits?\b", False, ["宣誓书"]),
    ("patent interference", r"\binterference\b", False, ["抵触"]),
    ("whistleblower", r"\bwhistle-?blow", False, ["吹哨人"]),
    ("la mattanza", r"\bmattanza\b", False, ["mattanza"]),
    ("black turtleneck", r"\bturtleneck", False, ["高领"]),
    ("the Journal", r"\bthe Journal\b|\bWall Street Journal\b", True, ["华尔街日报"]),
    ("Silicon Valley", r"\bSilicon Valley\b|\bthe Valley\b", True, ["硅谷"]),
    ("Walgreens", r"\bWalgreens?\b", True, ["沃尔格林"]),
    ("Safeway", r"\bSafeway\b", True, ["西夫韦"]),
    ("Boies Schiller", r"\bBoies,? Schiller\b", True, ["博伊斯·席勒"]),
    ("McDermott", r"\bMcDermott\b", True, ["麦德莫特"]),
    ("Chiat\\Day", r"\bChiat\\Day\b", True, ["Chiat\\Day"]),
    ("Siemens", r"\bSiemens\b", True, ["西门子"]),
]

# First names the book uses on their own for its main characters.
FIRST_NAMES = [("Elizabeth", "伊丽莎白"), ("Sunny", "桑尼"), ("Tyler", "泰勒"), ("Erika", "埃丽卡"), ("Ian", "伊恩"),
               ("Alan", "艾伦"), ("Daniel", "丹尼尔"), ("Shaunak", "肖纳克"), ("Tony", "托尼"), ("Chelsea", "切尔西"),
               ("Avie", "阿维"), ("Ana", "安娜"), ("Aaron", "阿伦"), ("Greg", "格雷格"), ("Noel", "诺埃尔"),
               ("Rochelle", "罗谢尔"), ("Anjali", "安贾莉")]


def people():
    """(label, English surname pattern, Chinese surname) for every surname in the names table with a Chinese name."""
    out = {}
    for row in csv.DictReader((BOOK / "review" / "terms" / "people-zh.tsv").open(), delimiter="\t"):
        name, chinese = row["name"], row["chinese"]
        if row["basis"] not in ("established", "transliterated") or not re.search(r"[·\s]", chinese):
            continue
        words = re.sub(r"\s*\(.*\)$", "", re.sub(r"[“\"][^”\"]*[”\"]", "", name)).split()
        words = [w for w in words if w not in ("Dr.", "II", "III", "IV", "Jr.")]
        zh = re.sub(r"(医生|二世|三世|四世)$", "", re.split(r"[·.\s]", chinese.strip())[-1])
        if not words or re.fullmatch(r"[A-Z]\.", words[-1]) or not re.fullmatch(r"[一-鿿]+", zh):
            continue
        out.setdefault((words[-1], zh), name)
    return [(f"name: {surname} ({first})", rf"\b{re.escape(surname)}\b", zh) for (surname, zh), first in out.items()]


def main(report):
    config = book_config.load(BOOK)
    checks = [(label, re.compile(rx, 0 if case else re.I), forms) for label, rx, case, forms in TERMS]
    checks += [(f"first name: {en}", re.compile(rf"\b{en}\b"), [zh]) for en, zh in FIRST_NAMES]
    checks += [(label, re.compile(rx), [zh]) for label, rx, zh in people()]
    flags, totals = defaultdict(list), Counter()
    for entry in config["chapters"]:
        zh_path = BOOK / "zh-cn" / entry["file"]
        if not zh_path.exists():
            continue
        source, _ = book.parse((BOOK / "en" / entry["file"]).read_text())
        target, _ = book.parse(zh_path.read_text())
        pairs = [(i, s, t) for i, (s, t) in enumerate(book.align(source, target, entry["id"], partial=True), 1) if t is not None]
        for index, s, t in pairs:
            en, zh = s.raw.replace("*", ""), re.sub(r"\s", "", t.raw)
            for label, rx, forms in checks:
                if not rx.search(en):
                    continue
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
