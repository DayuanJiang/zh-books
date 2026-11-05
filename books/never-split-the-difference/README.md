# 掌控谈话

克里斯·沃斯（Chris Voss）、塔尔·拉兹（Tahl Raz）《Never Split the Difference: Negotiating As If Your Life Depended On It》（HarperBusiness，2016）的中英对照译本，从英文原文直接翻译。书名沿用中文版（赵坤译，北京联合出版公司、磨铁图书，2018）的译名《掌控谈话》。现在英文原文已经导入并核对完，术语统计和术语表也已做完（见 [review/terms/README.md](review/terms/README.md) 和 [glossary.md](glossary.md)），还没有开始翻译。

## 来源与许可

- 原书版权归 Chris Voss 和 Tahl Raz 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文先从用户提供的 EPUB（calibre 重新打包的 HarperCollins 电子书，只有第 1 到 10 章）导入，2026 年 11 月又用用户提供的 HarperCollins 完整电子书（2016）补全。导入、整理和补全的过程见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。

## 内容

第 1 到 10 章共 1,860 个块，中英逐块对应。各章的副标题（例如 *How to Become the Smartest Person . . . in Any Room*）放在章标题下面；第 2 到 10 章末尾的 Key Lessons 保留原来的导语和要点列表。书里的步骤清单、引用的邮件和第 4 章的筹款电话脚本也保留为列表和引用块。

第 10 章之后是致谢、附录 Prepare a Negotiation One Sheet 和关于作者，全书共 13 节、1,958 个块。原书的 23 条书末注释都是文献出处，放在各章对应的位置，写成脚注。献辞、目录、索引、版权页和出版社的广告没有收入。

## 翻译进度

全书各节都已译完，依次经过翻译、双语审校、编辑通读，再由 GPT-6 Astra 独立审校第三轮；各章正文后附“本章小结与要点”。所有章节的状态都是 `review`，等用户认可后改为 `done` 才会在网站上发布。各节的审校记录在 `review/<章节 id>.md`。

查看各节进度，在仓库根目录运行：

```bash
python3 scripts/site.py status never-split-the-difference
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每章一个 Markdown 文件
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表
review/            审校记录：source.md 记原文核对，每章一份 <章节 id>.md 记四项审校
assets/            封面、字体、章首章末图的数据（diagrams/）
tools/             整理 EPUB、导入后收尾和核对原文的脚本
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
