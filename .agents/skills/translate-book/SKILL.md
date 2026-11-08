---
name: translate-book
description: Translate or polish a whole book in the zh-books repository, chapter by chapter, with the shared bilingual reader. Covers creating books/<id>/, importing the English EPUB, the glossary, keeping en/ and zh-cn/ aligned block by block, chapter statuses in book.json, per-chapter review records, splitting chapters across agents, previewing, and the checks before a chapter is published. Use for any work on the text of a book under books/. The translation craft itself (meaning checks, translationese, style) comes from the en-zh-translation-polish skill.
---

# 在 zh-books 里译一本书

这个仓库里每本书是 `books/<id>/` 下的一个目录，阅读器和工具都在 `framework/`，所有命令都从仓库根目录的 `scripts/site.py` 运行。书的格式规则和 `book.json` 的全部字段见 `framework/README.md`；这里写的是译书时按什么顺序做、每一步要留下什么。

怎样把一句话译好，按 `en-zh-translation-polish` 技能做：先核对意义和完整性，再修中文表达；整书流程见它的 `reference/repository-workflow.md`。开始前先读这个技能的 `SKILL.md`。

## 开始之前

1. **确认发布权利。** 问清楚这本书的原文和译文能不能公开发布。不能公开的书放在私有仓库里（以这个仓库为上游），本仓库的 `main` 会自动部署到公开网站。
2. **确认英文原文的来源**：用户提供的 EPUB 文件和版本。不要从网上自行下载有版权的书。
3. **建目录并导入**

   ```bash
   python3 scripts/site.py new <id> --title 中文书名 --original-title "English Title" --authors "Author"
   python3 scripts/site.py import-epub <id> path/to/book.epub
   ```

4. **核对导入结果。** 对照 EPUB 检查章节是否齐全、有没有漏段或重复、脚注是否都在、编号章节的 `number` 对不对。版权页、目录页这类不需要翻译的分节，从 `book.json` 删掉，同时删掉 `en/` 下对应的文件。核对中发现的问题和处理方式，记在 `review/source.md`。
5. **先做完术语统计，再开始翻译。** 用核对过、没有乱码的英文统计，数据存进 `books/<id>/review/terms/`，并写一份 README，说明用了哪些来源、什么门槛、得到多少条：
   - 用 `en-zh-translation-polish` 的 `scripts/corpus.py` 和 `scripts/terms.py` 抽取候选词，门槛设低一些（例如频次不少于 3），记录频次和分布的章数（用法见它的 `reference/reusable-scripts.md`）。
   - 纸质版索引的词条：概念和人名分开统计，人名用来统一译名。
   - 原文里的定义句（we call、known as、the term 等）和小节标题。
   - 低频但重要的概念不能漏。

   从这些数据里挑出书中特有、反复出现或作者专门定义过的概念，逐条裁定后写进 `books/<id>/glossary.md`，写明适用的意思和不要混同的概念。全书译完后，对每个术语统计对应中文段落里用了哪些译法，不一致的统一改过来。
6. **译样章。** 先译一章有代表性的（通常是引言或第 1 章），状态设为 `draft`，用 `serve --drafts` 给用户看真实页面。用户认可译文风格后，再推广到其他章节。

## 每一章怎样译

1. 在 `zh-cn/` 下建与 `en/` 同名的文件，在 `book.json` 里把这一章的状态从 `todo` 改成 `draft`。
2. 从章首往下译，不要跳着译。中文文件和英文文件要逐块对应：
   - 每个标题、段落、列表、引文和表格，在中文的同一位置有且只有一个对应块。
   - 标题级别、列表项数和表格行数相同。
   - 代码、图片和分隔线只写在英文文件里。
   - 脚注写成 `[^n]:`，编号和英文一致。译者注写成 `[^t1]:`，并在正文里引用。
   - 第一行是 `#` 一级标题。
3. 随时用 `python3 scripts/site.py status <id>` 看这一章译了多少块。中英两边对不上时，它会显示第一个对不上的块。
4. 用 `python3 scripts/site.py serve --drafts` 在阅读器里看。还没译的段落显示英文，并标着“待译”。
5. 全章译完、做完译者自检后，状态改成 `review`。

## 审校记录

审校按 `framework/translation-review.md`（译文审校规范）来做：问题按类别和轻重记录，改写前后都对照原文核对意思。

每章一份 `books/<id>/review/<章节 id>.md`，分四节，每节写明谁做的、覆盖了哪些范围、发现了什么、怎么处理、还剩什么：

1. **译者自检**：对照原文，检查漏译、增译、否定、条件、数量、比较对象、术语义项和图文关系。
2. **双语审校**：由没有参与这一章翻译的人，或另一个独立上下文的 agent 来做，对照原文看完全章。
3. **中文通读**：顺着中文读完全章，检查连贯、重复和前后概念是否一致。通读中改动的地方要回查原文。
4. **阅读器校样**：在 `serve` 打开的真实页面里看标题、列表、脚注弹窗、图片和表格。

四节都完成、没有未解决的意义问题时，才把状态改成 `done`。模型之间互相审校，不能写成专业人工审校；记录里要写明审校者是哪个模型或哪个人。

## 每章的小结与要点

译文定稿后，为每章写 `books/<id>/recaps/<章节 id>.md`：一两段小结（问题、关键实验和数字、作者的解释），加 4 到 5 条要点，不写标题，不加原书以外的内容。写完后由另一个 agent 对照英文逐句核实，改掉错误、夸大或遗漏。格式见 `framework/README.md` 的“每章的小结与要点”。

## 分给多个 agent 并行

按章节分配，每个 agent 只写自己负责的 `zh-cn/` 文件和 `review/` 文件，`book.json`、`glossary.md` 和共用文件由主会话统一修改。交给 agent 的说明里要写清楚：

- 负责的章节文件和可以写的文件。
- 先读 `en-zh-translation-polish` 的 `SKILL.md`、本技能，以及 `glossary.md`。
- 用户认可的样章路径，照它的风格译。
- 逐块对应的规则（上面“每一章怎样译”第 2 步）。
- 不提交、不推送、不改其他文件。
- 完成后汇报：译了哪些块、哪些地方拿不准、术语表需要补什么。

主会话收到结果后，自己运行 `status` 和 `check`，并在阅读器里抽查页面，然后才接受结果。

## 发布一章之前

```bash
python3 scripts/site.py fonts <id>    # 译文里出现了新的汉字时，重新生成字体子集
python3 scripts/site.py roles <id>    # 列出要判断的整段斜体，判断结果写进 roles.json，直到输出 []
python3 scripts/site.py check <id>    # 和 CI 一样的严格检查
```

`check` 通过后，向用户汇报这一章的四项审校结果，等用户确认后再提交。推送前要先征得用户同意。

## 这个技能和 en-zh-translation-polish 的关系

- `.agents/skills/en-zh-translation-polish/` 是用户个人目录里那份技能的副本，用 `python3 scripts/site.py sync-skill` 从个人目录同步过来。要改这个技能，先改个人目录里的主本，再运行同步。
- 本技能（`translate-book`）只放在这个仓库里，直接在这里修改。
- `.claude/skills/` 下的两个链接都指向 `.agents/skills/` 里的同名目录，Claude Code 和 Codex 读到的是同一份文件。
