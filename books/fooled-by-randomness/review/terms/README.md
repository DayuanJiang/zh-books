# 术语统计

翻译之前做的统计。英文用整理过的 `en/`（和 EPUB 逐词核对过，见 `review/source.md`）。统计时去掉第 7 章两条脚注的定义，也去掉参考文献一节（条目保留英文，不翻译），其余 27 节都算。“各章概要”逐字重复了各章开头的内容提要，所以这些词会多算一次，首次出现也常常是 summaries。

```bash
# 1. 语料副本：去掉脚注定义和参考文献
mkdir en-body && for f in books/fooled-by-randomness/en/*.md; do
  [ "$(basename "$f")" = 30-references.md ] || sed -e '/^\[\^[0-9]*\]: /d' -e 's/\[\^[0-9]*\]//g' "$f" > en-body/"$(basename "$f")"
done
# 2. 正文语料和 spaCy 候选词（en-zh-translation-polish 的脚本，门槛：频次不少于 3）
python -E -s "$SKILL/scripts/corpus.py" extract --root en-body --include '*.md' --language en --out en.json
python -E -s "$SKILL/scripts/terms.py" candidates --corpus en.json --english-backend spacy --spacy-model en_core_web_sm --min-frequency 3 --out candidates.json
# 3. 其余几份表（spaCy 3.8.7、en_core_web_sm 3.8.0）
python -I books/fooled-by-randomness/tools/term_stats.py candidates.json
# 4. 写好 glossary.md 以后：统计核心概念，填进术语表的“首次出现”和“出现次数”
python3 -I books/fooled-by-randomness/tools/term_stats.py --evidence
```

`corpus.py` 和 `terms.py` 要从技能自己的目录导入辅助模块，所以用 `-E -s` 运行；读书稿的其他脚本都用 `-I`。

| 文件 | 内容 | 数量 |
| --- | --- | --- |
| `candidates.tsv` | spaCy 名词短语候选：频次、分布的章数、首次出现的章节、词数、常见词形 | 2307 |
| `italics.tsv` | 正文里的斜体短语：斜体次数、正文出现次数、章数、首次出现的章节。作者常用斜体引出自己的说法（*lucky fool*、*black swan*、*skewness*），也包括书名和外文引语 | 358 |
| `definitions.tsv` | 原文里的定义句（I call、what I call、called、known as、dubbed、termed、so-called、a.k.a. 等） | 191 |
| `headings.tsv` | 各节的一到三级标题 | 228 |
| `people.tsv` | spaCy 命名实体识别得到的人名，按姓归并，正文出现次数按姓统计。原始数据，有不少误判（例如 Monte Carlo、Amnesia） | 395 |
| `named-entities.tsv` | spaCy 识别的机构、地名、作品、民族等专名，原始数据 | 601 |
| `people-zh.tsv` | 核对过的人名表：每个人的中文译名、依据、身份和说明 | 475 |
| `glossary-evidence.tsv` | 术语表核心概念每一条的首次出现、出现次数、原文例句和裁定者 | 128 |

- **没有索引**：这个 EPUB 没有纸质版的索引，所以没有 `index-terms.tsv`。概念候选来自 spaCy、斜体短语和定义句；人名来自命名实体识别，再加上逐节扫描大写开头、全书从不以小写出现的词，补上识别漏掉的人（梭伦、卡尔内阿德斯、普鲁斯特、帕斯卡等）。
- **人名表的依据**：
  - `established` 221 人：有通行中文名的人（也包括 Bacchus、Jupiter、Baal 这些神名和 Prince of Wales 这类称号），按常见中译本和百科的写法。联网核对过的有：卡尔内阿德斯（中文维基百科）、杰克·施瓦格（《金融怪杰》中译本）；其余按通行写法，没有逐一联网核对，拿不准的写在 note 里（例如 Croesus 也作“克洛伊索斯”）。和《思考，快与慢》重合的人（卡尼曼、特沃斯基、琳达）用同样的写法。
  - `transliterated` 52 人：没有通行译名的人和书中人物，按新华社译名的规则音译，例如尼禄·图利普（Nero 用罗马皇帝的通行译名）、让-马纽埃尔·罗藏、马蒂·奥康奈尔。书里没有华人；Yuzhao Zhang 只在致谢里出现，本名不知道，照写英文。
  - `keep` 202 人：照写英文。70 人只在两版致谢里出现（作者的同事、读稿人和家人；William Easterly 和 Jack Schwager 两位知名作者例外，用通行译名）；130 人只在书末注释“作者（年份）”形式的文献引用里出现，照写英文，和参考文献对应，全名取自参考文献；另有 2 人两处都有。
- **术语表的筛选**：从这几份数据里挑出书中特有、反复出现或作者专门定义过的概念。作者自己的说法，例如幸运的傻瓜、或然历史、偏态、梭伦的警告、维特根斯坦的尺子、往返谬误、反向法则；书里讲到的概率、统计和行为科学概念，例如样本路径、遍历性、启发式、有限理性；交易行话，例如爆仓、止损、宽客。只出现一两次但作者专门定义过的（epistemic opacity、round-trip fallacy、inverse rule）是从定义句和斜体短语里补上的。
- **结果**：术语表 122 条核心概念，另有机构、地名与报刊表和常提到的书表，状态都是“初定”。译第 1 章样章时补了 6 条后面几章也会用到的说法（对随机性的抵抗力、方差、裸期权、国债和垃圾债券、交易主管和场内交易员、幸灾乐祸），共 128 条。全书译完后，又按各节编辑的报告补了 18 条在几章里反复出现的说法（例如行情判断、衍生品、适应度、跑步机效应、领域特定的），现在共 146 条，出现次数用 `term_stats.py` 的同一套正则统计。
- **注意**：
  - 出现次数按英文词形的正则匹配统计，可能把同词根的普通用法也算进去，例如 option 也有“选择”的意思，trading 也包括普通的买卖。每条用的正则写在 `tools/term_stats.py` 的 `EVIDENCE_PATTERNS` 里。
  - `people.tsv` 按姓统计的次数会把同姓的人算在一起，例如 Karl Pearson 和 Egon Pearson，以及 John 这类常见名字。
  - 中信出版社的中译本《随机漫步的傻瓜》（2012，盛逢时译）的章节标题只作参考（目录取自网上书店的页面），术语表的各节标题是重新译的。

## 一致性检查（全书译完后）

```bash
uv run --project framework/tools python -I books/fooled-by-randomness/tools/term_consistency.py report.json
```

对每个术语和人名，找出含这个英文词的段落，统计对应的中文段落里有没有约定的译法，没有的写进报告。术语列表是 `term_consistency.py` 里的 `TERMS`；人名取自 `people-zh.tsv` 里有中文名的人，按姓匹配，书中人物（Nero、John）、拼错的名字和同姓的人写在 `NAME_KEYS` 里。参考文献不查；书末注释和致谢里保留英文的人名不算错。同一术语有不止一种译法的，回到上下文判断是否需要统一。
