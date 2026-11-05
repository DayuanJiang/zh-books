# 术语统计

翻译之前做的统计。英文用整理过的 `en/`（和 EPUB 逐节核对过词数），统计时去掉脚注，只算正文。

```bash
# 1. 正文语料和 spaCy 候选词（en-zh-translation-polish 的脚本，门槛：频次不少于 3）
corpus.py extract --root <去掉脚注的 en/ 副本> --include '*.md' --language en --out en.json
terms.py candidates --corpus en.json --english-backend spacy --spacy-model en_core_web_sm --min-frequency 3 --out candidates.json
# 2. 其余几份表
uv run --project framework/tools python books/empire-of-ai/tools/term_stats.py book.epub candidates.json
```

| 文件 | 内容 | 数量 |
| --- | --- | --- |
| `candidates.tsv` | spaCy 名词短语候选：频次、分布的章数、首次出现的章节、词数、常见词形 | 3501 |
| `index-terms.tsv` | 纸质版索引里人名以外的词条：概念（小写开头）和专名（机构、产品、地名等），含索引页码数、正文出现次数、章数、首次出现的章节 | 555 |
| `people.tsv` | 纸质版索引里的人名，正文出现次数按姓统计 | 270 |
| `people-zh.tsv` | 每个人的中文译名、依据（通行译名或按新华社译名规则音译）和身份 | 见文件 |
| `definitions.tsv` | 原文里的定义句（called、known as、so-called、the term、coined、code-named 等） | 189 |
| `headings.tsv` | 各节标题 | 25 |
| `glossary-evidence.tsv` | 术语表每一条的首次出现和原文例句，以及裁定者 | 87 |

- **筛选**：从这几份数据里挑出书中特有、反复出现或作者专门定义过的概念。比如帝国、攫取主义、规模定律、末日派和繁荣派、“插曲”（The Blip）、全面危机（Omnicrisis）。员工的俗称和内部团队名大多只在一两章出现，频次不高，是从定义句里补上的。常见的 AI 技术词也收进来，保证各章译法一致。
- **结果**：术语表 87 条概念，另有一张机构、产品与地名的表，状态都是“初定”。
- **注意**：
  - 出现次数按英文词形的正则匹配统计，可能把同词根的普通用法也算进去，例如 scale 和 model。
  - 人名表里按姓统计的次数会把同姓的人算在一起，比如奥特曼一家。

## 一致性检查（全书译完后）

对每个术语，找出含这个英文词的段落，统计对应的中文段落里用了哪些译法。同一术语有不止一种译法的，回到上下文判断是否需要统一。
