# 原文核对

## 来源

- 文件：用户提供的 EPUB（`EmpireofAI_InsidetheRaceforTotalDominati.epub`），SHA-256 记在 `book.json` 的 `source` 里。EPUB 本身不放进仓库。
- 版本：书名页和版权页都是美国 Penguin Press 2025 年版《Empire of AI: Dreams and Nightmares in Sam Altman's OpenAI》，电子书 ISBN 9780593657515。EPUB 元数据里的副标题 “Inside the Race for Total Domination” 是英国版的，正文以书里的版权页为准。
- 这个 EPUB 是出版社制作的，结构完整，没有乱码。斜体、粗体用 CSS 类表示，书末注释只从注释链回正文里的空锚点，正文里没有注释编号。

## 导入和整理

```bash
uv run --project framework/tools python books/empire-of-ai/tools/prepare_epub.py book.epub prepared.epub
python3 scripts/site.py import-epub empire-of-ai prepared.epub --force
uv run --project framework/tools python books/empire-of-ai/tools/curate_source.py book.epub
```

`tools/prepare_epub.py` 先复制一份 EPUB，做两件事：

- 把表示斜体和粗体的 CSS 类换成 `<i>` 和 `<b>`，导入后书名、报刊名保留斜体。第 13 章的 5 个上标指数（10²⁶ 和 10²⁵）换成上标数字，否则会变成 1026。
- 在每条注释链回的锚点处放一个标记，导入后还能知道注释在正文里的位置。

`tools/curate_source.py` 再处理导入结果：

| 问题 | 处理 |
| --- | --- |
| 书名页图片、版权页、四个部分的标题页（只有 Part I 到 IV，没有标题）、纸质版索引（两个文件）、出版社的推荐书目页被导成了章节 | 删除。EPUB 的封面图改作书架封面 |
| 798 条书末注释放在 19 个单独的文件里 | 每条注释改成所在章节的脚注 `[^n]`，放在注释引用的那几个词后面。798 条全部按引用的词找到了位置 |
| 章节有两个标题（目录标题和章内标题） | 只留一个一级标题，编号章节写成 “# 1. Divine Right” |
| 场景之间的分隔是一个单独的 “—” 段落 | 改成分隔线 |
| 推文和论文标题里的三个表情符号是小图片 | 换成表情字符 🦃、🦜、🔄 |
| 其中两处表情后面多了一个左引号（“Too Big? 🦜“”、“loop 🔄“,”） | 去掉多余的引号 |

第 1 篇题词的注释在 EPUB 里没有锚点，放在它引用的 “It is said” 之后。

## 完整性核对

逐节比较英文词数和 EPUB 对应文件的词数（不算标题和脚注，首字下沉的字母和后面的字母算一个词）：25 节全部一致，正文共 146,135 个词。798 条注释全部成为脚注，每条只出现一次，正文里没有剩下的标记。

## 保留的结构

献辞、题词、作者说明、序章、第 1 到 18 章、尾声、致谢、作者简介，共 25 节。四个部分没有标题，只有编号，所以没有保留部分页。

## 原文疑点

| 位置 | 原文 | 处理 |
| --- | --- | --- |
| 第 7 章正文和注释 | “Too Big? 🦜“” | 多了一个左引号，已去掉 |
| 第 11 章 | “loop 🔄“,” | 多了一个左引号，已去掉 |
