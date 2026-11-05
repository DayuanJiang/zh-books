# 术语统计

翻译之前做的统计。英文用整理过的 `en/`（和 EPUB 逐节核对过词数，见 [../source.md](../source.md)），统计时去掉脚注，只算正文。这本书的 EPUB 没有纸质版索引，代替索引的来源有三个：作者自己在附录里写的术语表（System Definitions: A Glossary），正文里用粗体排出的定义词（第 1 章的星号注释说，粗体词的定义都在这张术语表里），以及页边的粗体原理句（附录的 Summary of Systems Principles 把它们又列了一遍）。人名和专名用 spaCy 的命名实体识别查漏，再逐条人工核对。

```bash
# 1. 正文语料和 spaCy 候选词（en-zh-translation-polish 的脚本，门槛：频次不少于 3）
#    环境：uv 建的临时虚拟环境，装 scripts/requirements-spacy.txt 和 en_core_web_sm 3.8.0 的 wheel
corpus.py extract --root <去掉脚注的 en/ 副本> --include '*.md' --language en --out en.json
terms.py candidates --corpus en.json --english-backend spacy --spacy-model en_core_web_sm --min-frequency 3 --out candidates.json
# 2. 其余几份表，并把核心概念的首次出现和出现次数填进 glossary.md（框架环境里有 spaCy 和模型）
uv run --project framework/tools python -I books/thinking-in-systems/tools/term_stats.py candidates.json
```

去掉脚注的副本：删掉 `[^n]:` 开头的脚注定义行和正文里的 `[^n]` 标记，其余原样复制。spaCy 3.8.7，模型 en_core_web_sm 3.8.0。`corpus.py` 默认不算标题、图片和网址，所以候选词的频次只来自正文段落、列表、引文和图题。

| 文件 | 内容 | 数量 |
| --- | --- | --- |
| `candidates.tsv` | spaCy 名词短语候选：频次、分布的章数、首次出现的章节、词数、常见词形 | 1610 |
| `book-glossary.tsv` | 附录术语表的每一条：正文里用粗体排出它的章节、正文出现次数（不算附录）、章数、首次出现的章节、作者的定义 | 18 |
| `principles.tsv` | 各章页边的粗体原理句，逐句和附录的原理汇总比较：相同、略有不同（列出附录的写法），以及只在附录里出现的 | 40（相同 31，不同 4，只在附录 5） |
| `people.tsv` | 正文里的每一个人：`tools/term_stats.py` 的 `PEOPLE` 列出的写法、计数用的正则、正文出现次数、章数、首次出现的章节，以及命名实体识别把哪些写法认作这个人 | 97 |
| `people-zh.tsv` | 每个人的中文译名、依据、身份和说明，包括致谢、献辞、参考书目和寓言、漫画里的人物 | 97 人 |
| `named-entities.tsv` | 命名实体识别标为机构、地名、作品、法律等的词，供整理“机构、产品与地名”时查漏 | 231 |
| `definitions.tsv` | 原文里的定义句（called、is called、I call、we call、known as、the term、the word、definition 等），以及正文里粗体定义词所在的句子 | 63 |
| `headings.tsv` | 各节的一到三级标题，带级别 | 112 |
| `glossary-evidence.tsv` | 术语表核心概念每一条的首次出现、出现次数、原文例句，以及裁定者 | 101 |

## 怎样得到这些结果

- **候选词**：门槛设成频次不少于 3，得到 1610 条。排在前面的大多是普通词（system、loop、time、people），书里自己的概念要从多词短语（feedback loop、leverage point、bounded rationality、rule beating、policy resistance）和作者的术语表里挑。模型方程里的变量名（room temperature、perceived sales）也会进入候选。
- **作者的术语表和粗体词**：附录术语表 18 条，每一条在正文里都有一处粗体定义，`book-glossary.tsv` 的 bold in 一列列出所在章节。脚本也会检查正文里有没有不在附录术语表里的粗体小写短语，这次没有。
- **页边原理**：31 句和附录汇总一字不差，4 句略有不同（例如第 1 章写 decoupled and to be independent，附录写 de-coupled and independent），5 句只在附录里有。第 2 章被插入语隔开的一句（Changing the length of a delay may … make a large change …）按一句处理。翻译时同一句英文用同一句中文。
- **人名**：没有索引，人名表是通读和扫描大写词整理出来的，写在 `term_stats.py` 的 `PEOPLE` 里。命名实体识别用来查漏：它认作人名的每一个词，都要能归到 `PEOPLE` 里的某个人，或者写在 `NOT_PEOPLE` 里（Slinky、Mark 4:25、Sevin、Geiger、Koch 等，共 23 条，标明了是什么；这次识别到其中 17 个），否则脚本会打印出来。参考书目条目是“姓, 名.”的格式，识别器有时只留下名，这些写在 `ALIASES` 里。`PEOPLE` 和 `people-zh.tsv` 的人名必须一一对应，否则脚本报错。
- **译名的依据**：`established` 55 人，是有通行中文名的名人，或者有中译本、中文版《系统之美》、中文维基、百度百科可查的译名（例如德内拉·梅多斯、丹尼斯·梅多斯、杰伊·福里斯特、彼得·圣吉、罗素·艾可夫、冈纳·缪尔达尔、扬·丁伯根）；`transliterated` 42 人，按新华社《世界人名翻译大辞典》的规则音译，德语、西班牙语、阿拉伯语的名字按原语读音；`keep` 0 人。书里没有华裔人物。通行译名有分歧的（福里斯特和福瑞斯特、丁伯根和廷贝亨、西蒙和他自取的中文名司马贺），说明一列写了选哪个、依据是什么；没有核实到的也写明了。
- **定义句和标题**：定义句是在正文的每一句里找信号词，人工看过后挑出作者专门命名或引用的说法，例如 system traps、archetypes、messes、eroding goals、boiled frog syndrome、competitive exclusion principle、mutual coercion, mutually agreed upon、error-embracing、tyrannese。标题表用来定下第 5 章八种陷阱、第 6 章十二个杠杆点和第 7 章十五条准则的译名，这三组在附录里各出现一次。
- **筛选**：从这几份数据里挑出书中特有、反复出现或作者专门定义过的概念：附录术语表的 18 条全部收入；再加上系统的组成（要素、相互连接、功能、目的、目标）、存量流量图的部件、八种陷阱和它们的别名、十二个杠杆点的名字、第 7 章的几个说法，以及第 2 章模型里反复出现的经济和人口用语（资本存量、折旧、可再生资源、库存、交货延迟）。低频但重要的词（law of the minimum、gain、meta-resilience、tyrannese、error-embracing，各出现一到两次）也收进来了。
- **结果**：术语表 101 条核心概念，另有一张 49 行的机构、产品与地名表，以及各节标题、两处出现的标题、附录小节和方框标题三张表，状态都是“初定”。核心概念的“首次出现”和“出现次数”由 `term_stats.py` 按 `TERMS` 里的正则统计并写回 `glossary.md`；改了术语表的英文列，要同步改 `TERMS`。
- **注意**：
  - 出现次数按英文词形的正则匹配统计，会把同词根的普通用法也算进去，例如 system、model、rule、structure、constant（形容词）、stock（含 stock of goods 和股市的 stocks）。
  - the way out 的统计去掉了编者的话里的 on the way out（撤退时）；drift to low performance 只算完整的说法，不算 drift nets。
  - 人名表里按姓统计的次数会把同姓的人算在一起，例如两位梅多斯和两位洛文斯；只写名的 Dana、Jay、Nathan 算在对应的人名下。

## 一致性检查（全书译完后）

```bash
uv run --project framework/tools python -I books/thinking-in-systems/tools/term_consistency.py report.json
```

对 `tools/term_consistency.py` 里 `TERMS` 列出的每个术语（存量、调节回路、增强回路、韧性、杠杆点、八种陷阱的名字等 62 条），以及 `people-zh.tsv` 里的每个人，找出含这个英文词的段落，看对应的中文段落里有没有约定的译法，没有的写进报告。同一术语有不止一种译法的，回到上下文判断是否需要统一。人名按姓检查，Calvin 和 Hobbes 在漫画对白里写成大写（CALVIN:），也算在内。
