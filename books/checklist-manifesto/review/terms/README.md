# 术语统计

翻译之前做的统计。英文用整理过的 `en/`（和 EPUB 逐节核对过词数，见 [../source.md](../source.md)），统计时去掉脚注，只算正文。这本书的 EPUB 没有纸质版索引，所以人名和专名改用 spaCy 的命名实体识别找出来，再逐条人工核对。

```bash
# 1. 正文语料和 spaCy 候选词（en-zh-translation-polish 的脚本，门槛：频次不少于 3）
corpus.py extract --root <去掉脚注的 en/ 副本> --include '*.md' --language en --out en.json
terms.py candidates --corpus en.json --english-backend spacy --spacy-model en_core_web_sm --min-frequency 3 --out candidates.json
# 2. 其余几份表，并把核心概念的首次出现和出现次数填进 glossary.md
uv run --with spacy==3.8.7 --with <en_core_web_sm 3.8.0 的 wheel> python -I books/checklist-manifesto/tools/term_stats.py candidates.json
```

去掉脚注的副本：删掉 `[^n]:` 开头的脚注定义行和正文里的 `[^n]` 标记，其余原样复制。spaCy 3.8.7，模型 en_core_web_sm 3.8.0。

| 文件 | 内容 | 数量 |
| --- | --- | --- |
| `candidates.tsv` | spaCy 名词短语候选：频次、分布的章数、首次出现的章节、词数、常见词形 | 1469 |
| `people.tsv` | 命名实体识别标为人名的词，按最后一个词（姓）归组：识别到的写法、次数、正文里姓出现的次数、章数、首次出现的章节，最后一列是它在 `people-zh.tsv` 里对应的人，或者说明它其实不是人名 | 171 组，其中 31 组不是人名 |
| `people-zh.tsv` | 人工整理的全书人名表：每个人的中文译名、依据、身份和说明，包括致谢和献辞里的人 | 149 人 |
| `named-entities.tsv` | 命名实体识别标为机构、地名、作品、产品等的词，供整理“机构、产品与地名”时查漏 | 386 |
| `definitions.tsv` | 原文里的定义句（called、known as、what engineers call、the phrase、the word、meaning 等） | 59 |
| `headings.tsv` | 各节标题 | 13 |
| `glossary-evidence.tsv` | 术语表核心概念每一条的首次出现、出现次数、原文例句，以及裁定者 | 84 |

## 怎样得到这些结果

- **候选词**：门槛设成频次不少于 3，得到 1469 条。排在前面的大多是普通词（patient、hospital、team），书里自己的概念要从多词短语和低频词里挑。
- **人名**：命名实体识别会漏人，也会把普通词当成人名。漏掉的人（例如 Mohnish Pabrai、Martin Makary、Zhi Xiong、Jay Powers、Sue Marchand、Riva Hocherman、Sara Bershtel、Pascience Kibatala、Julia Child）是通读全书和扫描大写词补上的；被误认的 31 组（Jet A-1、Van Halen、Safeguard、Cort、Russia Wharf 等）写在 `tools/term_stats.py` 的 `NOT_PEOPLE` 里，`people.tsv` 最后一列注明了它们是什么。脚本每次运行都会检查：识别出来的人名都要能在 `people-zh.tsv` 里找到，或者在 `NOT_PEOPLE` 里，否则打印出来。
- **译名的依据**：`established` 31 人，是有通行中文名的名人，或者有中译本、中文版《清单革命》、中文维基可查的译名（例如阿图·葛文德、陈冯富珍、莫尼什·帕伯莱、盖伊·斯皮尔、杰夫·斯玛特、丹尼尔·布尔曼）；`transliterated` 114 人，按新华社《世界人名翻译大辞典》的规则音译，法语、葡萄牙语、波兰语、阿拉伯语的名字按原语读音；`keep` 4 人，是汉字查不到的华裔和韩国人（Zhi Xiong、Yen Liow、Eeling Liow、Sooyeon Hwang），照写原名。网上查过的来源写在各行的说明里，没有核实到的也写明了。
- **定义句和标题**：定义句是在正文的每一句里找 called、known as、what … call、the phrase、the word、meaning 这类信号词，人工看过后挑出作者专门命名的说法，例如 forcing functions、submittal schedule、pause points、killer items、activation phenomenon、cocaine brain、Airline Captains。
- **筛选**：从这几份数据里挑出书中特有、反复出现或作者专门定义过的概念：清单、无知和无能、简单、繁杂与复杂三类问题、总建造师、暂停点、先做后确认型和边读边做型清单、致命项、报审进度表、纪律等。低频但重要的词（eptitude、cognitive net、all-or-none、activation phenomenon，各只出现一次）也收进来了。医学、航空、建筑和投资的常用术语收进来，是为了各章译法一致。
- **结果**：术语表 84 条核心概念，另有一张 74 行的机构、产品与地名表，状态都是“初定”。核心概念的“首次出现”和“出现次数”由 `term_stats.py` 按 `TERMS` 里的正则统计并写回 `glossary.md`，改了术语表的英文列，要同步改 `TERMS`。
- **注意**：
  - 出现次数按英文词形的正则匹配统计，会把同词根的普通用法也算进去，例如 check（含“支票”）、power（含“电力”）、case、system。
  - 人名表里按姓统计的次数会把同姓或同名的人算在一起，例如两位 Brown（迈克尔·布朗和戈登·布朗）、两位 Hill、两个 Jay。

## 原文里另外发现的空格问题

做定义句和人名扫描时，又看到几处 `review/source.md` 没有列出的空格问题，EPUB 里就是这样写的，`en/` 照原样保留，翻译时按正确的词理解：

| 位置 | `en/` 里的写法 | 应为 |
| --- | --- | --- |
| 第 3 章 | fire proofing material | fireproofing |
| 第 3 章 | as Joe Salvia explained tome | explained to me |
| 第 4 章 | a roasted tomato soap | 疑为 soup（汤），纸质版未核对 |
| 第 5 章 | *Cleared for Take off* | Takeoff（同一节前文作 “Cleared for Takeoff”） |
| 第 5 章 | button holed | buttonholed |
| 第 7 章 | on my hall way | hallway |
| 第 8 章 | under recognized | underrecognized |

## 一致性检查（全书译完后）

```bash
uv run --project framework/tools python books/checklist-manifesto/tools/term_consistency.py report.json
```

对 `tools/term_consistency.py` 里 `TERMS` 列出的每个术语，以及 `people-zh.tsv` 里有中文译名的每个人，找出含这个英文词的段落，看对应的中文段落里有没有约定的译法，没有的写进报告。同一术语有不止一种译法的，回到上下文判断是否需要统一。complicated 和 complex 出现在同一段时，要求中文里有“繁杂”。
