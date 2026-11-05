# 坏血

约翰·卡雷鲁（John Carreyrou）《Bad Blood: Secrets and Lies in a Silicon Valley Startup》（Alfred A. Knopf，2018）的中英对照译本，从英文原文直接翻译。中文书名沿用简体中文版（成起宏译）的书名《坏血：一个硅谷巨头的秘密与谎言》。

## 来源与许可

- 原书版权归 John Carreyrou 所有。这份译文没有获得授权，发布与否由用户决定。
- 英文原文来自用户提供的 EPUB（美国 Knopf 2018 年第一版）。导入和整理的过程见 [review/source.md](review/source.md)，电子书文件本身不放进仓库。

## 内容

献辞、作者说明、序章、第 1 到 24 章、尾声、致谢、作者简介，共 30 节、1,329 个要翻译的块。原书的 372 条书末注释改成了各章的脚注，放在注释引用的词句后面。英文原文已经逐节和 EPUB 核对过，还没有开始翻译。

## 翻译进度

全书各节都已译完，依次经过翻译、双语审校、编辑通读，再由 GPT-6 Astra 独立审校第三轮；各章正文后附“本章小结与要点”。2026 年 11 月 5 日用户确认后，所有章节都改为 `done`，在书架网站上发布。各节的审校记录在 `review/<章节 id>.md`。

查看各节进度，在仓库根目录运行：

```bash
python3 scripts/site.py status bad-blood
```

## 目录

```text
book.json          书的信息和章节列表，每章的状态：todo（只有英文）、draft、review、done（发布）
en/                英文原文，每章一个 Markdown 文件；书末注释已改成各章的脚注
zh-cn/             中文译文，与 en/ 同名同结构，逐块对应
glossary.md        术语表
review/            审校记录：source.md 记原文核对，每章一份 <章节 id>.md 记四项审校
assets/            封面
tools/             准备 EPUB、整理导入结果和核对原文的脚本
```

翻译和审校的流程见 [framework/README.md](../../framework/README.md)。
