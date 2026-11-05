"""After translating: find aligned blocks whose English has a glossary term or a person's name but whose Chinese
lacks the agreed rendering (see review/terms/README.md).

    uv run --project framework/tools python -I books/fooled-by-randomness/tools/term_consistency.py report.json
"""

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(BOOK.parents[1] / "framework" / "tools")]
import book  # noqa: E402
import config as book_config  # noqa: E402

SKIP = {"references"}  # the bibliography stays in English

# (label, English pattern, case sensitive, accepted Chinese forms): the book's own terms, where one rendering matters.
TERMS = [
    ("randomness", r"\brandomness\b", False, ["随机"]),
    ("luck", r"\bluck(?:y|ily|ier)?\b", False, ["运气", "幸运", "走运", "侥幸"]),
    ("lucky fool", r"\blucky fools?\b", False, ["幸运的傻瓜"]),
    ("fooled by randomness", r"\bfool(?:s|ed)? (?:of|by) randomness\b", False, ["被随机性愚弄", "随机漫步的傻瓜"]),
    ("Table P.1", r"\bTable P\.1\b", True, ["表P.1"]),
    ("noise", r"\bnoise\b", False, ["噪声"]),
    ("signal", r"\bsignals?\b", False, ["信号"]),
    ("black swan", r"\bblack swans?\b", False, ["黑天鹅"]),
    ("rare event", r"\brare[- ]events?\b", False, ["稀有事件"]),
    ("Solon’s warning", r"\bSolon’s warning\b", True, ["梭伦的警告"]),
    ("skewness", r"\bskewness\b", False, ["偏态", "偏度"]),
    ("asymmetry", r"\basymmetr", False, ["不对称"]),
    ("alternative histories", r"\balternative histor(?:y|ies)\b", False, ["或然历史"]),
    ("Russian roulette", r"\bRussian roulette\b", False, ["俄罗斯轮盘赌"]),
    ("Monte Carlo", r"\bMonte Carlo\b", True, ["蒙特卡罗"]),
    ("generator", r"\bgenerators?\b", False, ["生成器", "根源"]),
    ("sample path", r"\bsample paths?\b", False, ["样本路径"]),
    ("survivorship bias", r"\bsurvivorship\b", False, ["幸存者偏差"]),
    ("hindsight bias", r"\bhindsight bias\b", False, ["后见之明偏差"]),
    ("heuristic", r"\bheuristics?\b", False, ["启发式"]),
    ("bounded rationality", r"\bbounded rationality\b", False, ["有限理性"]),
    ("System 1 / 2", r"\bSystem [12]\b", True, ["系统1", "系统2"]),
    ("probability blind", r"\bprobability blind", False, ["概率盲"]),
    ("expectation", r"\bexpectations?\b", False, ["期望", "预期"]),
    ("median", r"\bmedian\b", False, ["中位数"]),
    ("conditional probability", r"\bconditional probabilit", False, ["条件概率"]),
    ("Wittgenstein’s ruler", r"\bWittgenstein’s ruler\b", True, ["维特根斯坦的尺子"]),
    ("regression to the mean", r"\bregression to the mean\b", False, ["均值回归"]),
    ("ergodicity", r"\bergodic", False, ["遍历"]),
    ("birthday paradox", r"\bbirthday paradox\b", False, ["生日悖论"]),
    ("data mining", r"\bdata mining\b", False, ["数据挖掘"]),
    ("data snooping", r"\bdata snooping\b", False, ["数据窥探"]),
    ("nonlinear", r"\bnonlinear", False, ["非线性"]),
    ("path dependence", r"\bpath[- ]dependen", False, ["路径依赖", "依赖路径"]),
    ("Buridan’s donkey", r"\bBuridan’s donkey\b", False, ["布里丹之驴"]),
    ("induction", r"\binducti(?:on|ve)\b", False, ["归纳"]),
    ("falsification", r"\bfalsif", False, ["证伪"]),
    ("empiricism", r"\bempiricis[mt]", False, ["经验主义"]),
    ("skepticism", r"\bskeptic", False, ["怀疑"]),
    ("epistemology", r"\bepistemolog", False, ["认识论"]),
    ("epiphenomena", r"\bepiphenomen", False, ["副现象"]),
    ("round-trip fallacy", r"\bround-trip fallacy\b", False, ["往返谬误"]),
    ("stoicism", r"\bstoic", False, ["斯多葛"]),
    ("gamblers’ ticks", r"\bgamblers’ ticks\b", False, ["赌徒的怪癖"]),
    ("pecking order", r"\bpecking order\b", False, ["地位排序"]),
    ("work ethics", r"\bwork ethics?\b", False, ["敬业"]),
    ("middlebrow", r"\bmiddlebrow\b", False, ["半吊子"]),
    ("empty suit", r"\bempty suits?\b", False, ["空架子"]),
    ("trader", r"\btraders?\b", False, ["交易员", "交易"]),
    ("proprietary trading", r"\bproprietary trading\b", False, ["自营交易"]),
    ("blow up", r"\bblow(?:s|ing|n)? up\b|\bblew up\b|\bblowups?\b", False, ["爆仓"]),
    ("stop loss", r"\bstop[- ]loss(?:es)?\b", False, ["止损"]),
    ("option seller", r"\b(?:option|premium) sellers?\b", False, ["期权卖方", "期权费卖方"]),
    ("volatility", r"\bvolatility\b", False, ["波动"]),
    ("quant", r"\bquants?\b", False, ["宽客"]),
    ("ten sigma", r"\bten sigma\b", False, ["十西格玛"]),
]

# People whose English key is a first name, a misspelling, or shared with someone else: name in people-zh.tsv ->
# (English pattern, Chinese key). Everyone else is matched by the last word of the name and the last part of the
# Chinese name.
NAME_KEYS = {
    "Nero Tulip": (r"\bNero\b", "尼禄"),
    "John": (r"\bJohn\b(?! (?:Doe|Maynard|Stuart|Harsanyi|Nash|Dos|Kenneth|F\.))", "约翰"),
    "John Doe": (r"\bJohn Doe\b", "无名氏"),
    "Henry": (r"\bHenry\b(?! (?:de|Kyburg))", "亨利"),
    "Marc": (r"\bMarc\b(?! Antony)", "马克"),
    "Janet": (r"\bJanet\b(?! Wygal)", "珍妮特"),
    "Marc Antony": (r"\bAntony\b", "安东尼"),
    "Cyrus": (r"\bCyrus\b(?! Pirasteh)", "居鲁士"),
    "Achilles": (r"\bAchilles\b(?! Venetoulias)", "阿喀琉斯"),
    "Alexander the Great": (r"\bAlexander the Great\b", "亚历山大"),
    "George Will": (r"\bGeorge Wills?\b", "威尔"),
    "Robert Frank": (r"\bRobert Frank\b", "弗兰克"),
    "Adam Smith": (r"\bAdam Smith\b", "斯密"),
    "Vernon Smith": (r"\bVernon Smith\b", "史密斯"),
    "Nassim Nicholas Taleb": (r"\bTaleb\b", "塔勒布"),
    "Minerva Ghosn Taleb": (r"\bMinerva\b", "密涅瓦"),
    "Doktorr Talebski": (r"\bTale[bv]ski\b", "塔勒布斯基"),
    "Ronald Something": (r"\bRonald Something\b", "罗纳德"),
    "Joseph K": (r"\bJoseph K\b", "约瑟夫"),
    "Monsieur de Norpois": (r"\bNorpois\b", "诺布瓦"),
    "Monsieur Prudhomme": (r"\bPrudhomme\b", "普吕多姆"),
    "Chevalier de Méré": (r"\bMéré\b", "梅雷"),
    "Cato the Elder": (r"\bCato\b", "加图"),
    "Zeno of Kition": (r"\bZeno\b", "芝诺"),
    "John F. Kennedy": (r"\bJFK\b", "肯尼迪"),
    "Jacqueline Kennedy Onassis": (r"\bOnassis\b|\bJackie\b", "杰奎琳"),
    "Nicholas II": (r"\bNicholas II\b", "尼古拉二世"),
    "Homer": (r"\bHomer(?:ic|ian)?\b", "荷马"),
    "Patroclus": (r"\bPatrocl", "帕特洛克罗斯"),
    "Paul Lévy": (r"\bLevy\b", "莱维"),
    "George Pólya": (r"\bPolya\b", "波利亚"),
    "Bernoulli": (r"\bBernouilli\b", "伯努利"),
    "Camille Pissarro": (r"\bPissaro\b", "毕沙罗"),
    "Robert Nozick": (r"\bNozik\b", "诺齐克"),
    "Paul Valéry": (r"\bVal[eé]ry\b", "瓦莱里"),
    "al-Ghazālī": (r"\bal-Ghaz", "安萨里"),
    "Richard von Mises": (r"\bvon Mises\b", "米泽斯"),
    "Timmermann": (r"\bTimmerman", "蒂默曼"),
    "H. White": None,  # "White" is too common to match
    "Verdurin": (r"\bVerdurins?\b", "维尔迪兰"),
    "King of Sweden": (r"\bKing of Sweden\b", "瑞典国王"),
    "Prince of Wales": (r"\bPrince of Wales\b", "威尔士亲王"),
}


def people():
    """(label, English pattern, Chinese key) for everyone in people-zh.tsv with a Chinese name."""
    rows = list(csv.DictReader((BOOK / "review" / "terms" / "people-zh.tsv").open(), delimiter="\t"))
    auto = defaultdict(set)
    for row in rows:
        if row["basis"] in ("established", "transliterated") and row["name"] not in NAME_KEYS:
            auto[row["name"].split()[-1]].add(re.split(r"[·\s]", row["chinese"])[-1])
    out = []
    for row in rows:
        name = row["name"]
        if row["basis"] not in ("established", "transliterated"):
            continue
        if name in NAME_KEYS:
            if NAME_KEYS[name]:
                out.append((name, *NAME_KEYS[name]))
            continue
        surname = name.split()[-1]
        if len(auto[surname]) > 1:
            print(f"warning: {surname} is shared by people with different Chinese names; add them to NAME_KEYS")
            continue
        out.append((name, rf"\b{re.escape(surname)}\b", re.split(r"[·\s]", row["chinese"])[-1]))
    return out


def main(report):
    config = book_config.load(BOOK)
    checks = [(label, re.compile(rx, 0 if case else re.I), forms) for label, rx, case, forms in TERMS]
    names = [(f"name: {name}", re.compile(rx), [key]) for name, rx, key in people()]
    flags, totals = defaultdict(list), Counter()
    for entry in config["chapters"]:
        zh_path = BOOK / "zh-cn" / entry["file"]
        if entry["id"] in SKIP or not zh_path.exists():
            continue
        source, _ = book.parse((BOOK / "en" / entry["file"]).read_text())
        target, _ = book.parse(zh_path.read_text())
        pairs = [(i, s, t) for i, (s, t) in enumerate(book.align(source, target, entry["id"], partial=True), 1) if t is not None]
        for index, s, t in pairs:
            en, zh = s.raw, re.sub(r"\s", "", t.raw)
            found = [(label, forms) for label, rx, forms in checks + names if rx.search(en)]
            for label, forms in found:
                totals[label] += 1
                if any(re.sub(r"\s", "", f) in zh for f in forms):
                    continue
                # names in the author-year citations of the notes and in the acknowledgments may stay in English
                if label.startswith("name: ") and entry["id"] in ("notes", "acknowledgments-first", "acknowledgments-second"):
                    if label[6:].split()[-1] in t.raw:
                        continue
                flags[entry["id"]].append({"block": index, "term": label, "preferred": " / ".join(forms),
                                           "english": " ".join(en.split())[:240], "chinese": " ".join(t.raw.split())[:240]})
    Path(report).write_text(json.dumps(flags, ensure_ascii=False, indent=1))
    per = Counter(f["term"] for fl in flags.values() for f in fl)
    print(f"{sum(totals.values())} occurrences checked, {sum(len(v) for v in flags.values())} blocks without the agreed rendering")
    print("most often rendered otherwise:", ", ".join(f"{t} {n}/{totals[t]}" for t, n in per.most_common(30)))


if __name__ == "__main__":
    main(sys.argv[1])
