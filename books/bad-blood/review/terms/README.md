# 术语统计

翻译之前做的统计。英文用整理过的 `en/`（和 EPUB 逐节核对过词数，见 [../source.md](../source.md)），统计时去掉脚注，只算正文。

```bash
# 1. 正文语料和 spaCy 候选词（en-zh-translation-polish 的脚本，门槛：频次不少于 3）
corpus.py extract --root <去掉脚注定义和 [^n] 标记的 en/ 副本> --include '*.md' --language en --out en.json
terms.py candidates --corpus en.json --english-backend spacy --spacy-model en_core_web_sm --min-frequency 3 --out candidates.json
# 2. 其余几份表，并把术语表里的“首次出现”和“出现次数”填好（需要 spaCy 和 en_core_web_sm 3.8.0）
uv run --with spacy==3.8.7 --with "click>=8.2,<9" --with "en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl" \
    python -I books/bad-blood/tools/term_stats.py candidates.json
```

| 文件 | 内容 | 数量 |
| --- | --- | --- |
| `candidates.tsv` | spaCy 名词短语候选：频次、分布的章数、首次出现的章节、词数、常见词形 | 2604 |
| `people-zh.tsv` | 书里每个人的中文译名、依据、身份和备注，人工整理 | 309 |
| `people.tsv` | `people-zh.tsv` 里每个名字在正文里出现的次数：全名次数、姓（或单名）次数、章数、首次出现的章节 | 309 |
| `definitions.tsv` | 原文里的定义句（known as、called、dubbed、so-called、code-named、the term、parlance、jargon、“, or IRB” 这类缩写说明等） | 125 |
| `headings.tsv` | 各节标题 | 30 |
| `glossary-evidence.tsv` | 术语表核心概念每一条的出现次数、章数、首次出现的章节、原文例句，以及裁定者 | 85 |

## 人名表怎样来的

这本书的纸质版没有索引，EPUB 里也没有，所以没有 `index-terms.tsv`，`people.tsv` 也改成从人名表反过来统计。人名表按三条线索整理，再逐条人工核对上下文：

1. spaCy 在正文里认出的 PERSON 实体，共 579 种写法。
2. 正文里所有连续的大写开头词组（993 种）和句中出现的大写单词，用来补上 spaCy 漏掉的人名、只写名的人（例如 Claudia、Tracy、Corrine）和只写姓的人。
3. 每个名字第一次出现的上下文，用来写“身份”一栏。

`term_stats.py` 最后再跑一遍 spaCy，列出人名表没有覆盖的 PERSON 实体。现在剩下 61 种，逐个看过都不是人：公司和机构（Walgreens、McDermott、Baxter、Pfizer）、设备和房间（Edison、ADVIA、Normandy）、地名和品牌（Deerfield、Gucci、FJ Cruiser）、复数的家族称呼（Holmeses、Clintons）、Drs 这样的称谓，以及理查德·富兹邮件末尾的署名缩写 Rcf。

人名表的 `basis` 一栏：

- `established`（89 人）：有通行中文名的人，按新华社和主要中文媒体的写法，例如乔治·舒尔茨、亨利·基辛格、鲁珀特·默多克、卢煜明。有不止一种常见写法的，在备注里列出另一种。
- `transliterated`（217 人）：按新华社《英语姓名译名手册》的规则音译；德语、法语、荷兰语、意大利语、西班牙语名字按各自的读音。华裔和日裔的人，查得到本人中文名的用本人中文名；查不到的，姓按常见对应字（Cheung 作“张”，Yam 作“任”，Yamamoto 作“山本”），在备注里写明未核实。共有 19 条备注写了族裔和用字的依据。
- `not a person`（3 条）：伊恩·吉本斯家的两条狗和一只猫。

同名或同音的几处在备注里写明了区分办法：霍姆斯家三代都叫 Christian；两位唐纳德·卢卡斯是父子；律师 Laura Brill 和 Mike Brille 分别译作“布里尔”“布里勒”；律师 Stephen Taylor 和泰勒·舒尔茨的“泰勒”同音；Jay Conti 和致谢里的 Jason Conti 是同一个人。

## 术语怎样挑的

- **筛选**：从候选词、定义句和标题里挑出书中特有、反复出现或作者专门解释过的说法。一类是 Theranos 自己的东西：Edison、miniLab（代号 4S）、Theranos 1.0、点胶机器人、nanotainer、卡盒和读取器、健康中心，以及“侏罗纪公园”“诺曼底”“兄弟会帮”这些内部叫法。一类是检验医学的词：免疫测定、常规生化、稀释、能力验证、质控、变异系数、CLIA、CMS、实验室自建检测（LDT），这些在第 14 章以后集中出现，各章要用同一种译法。还有创业和风投的词（独角兽、曲棍球棒式预测、雾件、隐身模式）、法律的词（商业秘密、取证证词、宣誓书、专利抵触程序）和新闻采访的词（线报、消息来源、深度背景、“不搞突然袭击”）。
- **低频但要收的**：hockey-stick forecast、vaporware、No surprises、anti-SLAPP、extra-ordinary 都只出现一次，但作者专门解释过，或者关系到全书的论点，所以照样收进来。
- **结果**：术语表 85 条核心概念，另有检测项目和医学名词表、机构产品与地名表，状态都是“初定”。
- **注意**：
  - 出现次数按英文词形的正则匹配统计，可能把同词根的普通用法也算进去，例如 reader 会算上报纸的读者，tip 会算上移液吸头，source 会算上电源这类用法。
  - `people.tsv` 里按姓统计的次数会把同姓的人算在一起，例如霍姆斯一家、富兹一家、两位卢卡斯；只有名的人按名统计，也会算上同名的其他人。
  - spaCy 候选里 theranos 和 therano、holmes 和 holme 这样的成对条目是词形还原造成的，频次相同，可以只看一条。

## 一致性检查（全书译完后）

```bash
uv run --project framework/tools python -I books/bad-blood/tools/term_consistency.py report.json
```

对每个术语和人名，找出含这个英文词的段落，看对应的中文段落里有没有约定的译法。术语清单写在脚本的 `TERMS` 里，人名从 `people-zh.tsv` 按姓读取，几位主要人物只用名称呼的情况另列在 `FIRST_NAMES` 里。报告里列出没有约定译法的段落，回到上下文判断是否需要统一。
