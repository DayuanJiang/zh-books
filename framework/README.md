# 译书框架

这个目录是所有书共用的阅读器和工具。一本书只需要放内容和一个 `book.json`，阅读器、构建、检查、书架首页和部署都由框架完成。

## 两种书

| `reader` | 适合 | 书的目录里放什么 |
| --- | --- | --- |
| `bilingual` | 新书都用这种。中英逐段对照的阅读器，也有纯中文模式 | `book.json`、`en/`、`zh-cn/`、`assets/` |
| `custom` | 已经有自己阅读器的书，例如用 VuePress 做的《软件设计的哲学》 | 自己的构建工具，`book.json` 里写明构建和检查命令 |

## 翻一本新书

所有命令都在仓库根目录运行。

1. **建目录**

   ```bash
   python3 scripts/site.py new thinking-fast-and-slow --title 思考，快与慢 --original-title "Thinking, Fast and Slow" --authors "Daniel Kahneman"
   ```

   会生成 `books/thinking-fast-and-slow/`，里面有 `book.json`、空的 `en/` 和 `zh-cn/`、术语表 `glossary.md` 和一份待填写的 README。

2. **导入英文原文**

   ```bash
   python3 scripts/site.py import-epub thinking-fast-and-slow ~/Downloads/book.epub
   ```

   EPUB 的每个分节变成 `en/` 下的一个 Markdown 文件，脚注和尾注变成 `[^n]`，图片放进 `en/images/`，章节按顺序写进 `book.json`，状态都是 `todo`。标题以数字开头的章节（“7 A Machine for…”“Chapter VII”）会得到编号和 `ch07` 这样的 id。

   导入的结果是初稿。翻译之前要对照 EPUB 检查一遍：

   - 有没有漏掉或重复的段落。
   - 脚注是否都在。
   - 版权页、目录页这类不需要翻译的分节，从 `book.json` 里删掉。
   - 章节编号对不对。

   这些问题直接改 `en/` 下的文件和 `book.json`。

3. **定术语**：先把全书的核心概念写进 `glossary.md`，每条写明适用的意思和不要混同的概念。翻译中途改了译法，要回查已经译完的章节。

4. **逐章翻译**：在 `zh-cn/` 下建同名文件，从章首往下翻译，然后把这一章的状态改成 `draft`。每一章的状态：

   | 状态 | 含义 | 发布吗 |
   | --- | --- | --- |
   | `todo` | 只有英文 | 不发布 |
   | `draft` | 正在翻译，可以只译了前半部分 | 只在草稿预览里出现，没译的段落显示英文并标为“待译” |
   | `review` | 译完了，等待对照原文的审校和中文通读 | 只在草稿预览里出现 |
   | `done` | 审校和通读都完成 | 发布 |

5. **预览**

   ```bash
   python3 scripts/site.py serve --drafts
   # 打开 http://127.0.0.1:8000/zh-books/
   ```

   不加 `--drafts` 时，看到的就是正式发布的样子。

6. **看进度**

   ```bash
   python3 scripts/site.py status thinking-fast-and-slow
   ```

   列出每章的状态和已译的块数、脚注数。中英两边对不上的章节会直接显示出错的位置。

7. **发布前**：生成这本书的中文字体子集，然后运行和 CI 一样的检查：

   ```bash
   python3 scripts/site.py fonts thinking-fast-and-slow
   python3 scripts/site.py check thinking-fast-and-slow
   ```

   推送到 `main` 后，CI 会检查所有书，再构建整站部署。至少有一章是 `done` 的书才会出现在书架上。

**公开发布之前，必须确认有权发布这本书的原文和译文。** 还在版权保护期、没有授权的书，放在私有仓库里：把这个仓库作为私有仓库的上游，书只放在私有仓库的 `books/` 下，用 `serve` 在本地读。

## 中英两边怎样对应

- `en/` 和 `zh-cn/` 下的同名文件按块一一对应：英文里的每个标题、段落、列表、引文和表格，在中文文件的同一位置都有且只有一个中文块。
- 标题级别、列表项数和表格行数要相同。
- 代码、图片和分隔线只出现在 `en/`。
- 脚注两边都写 `[^n]:` 定义，按编号对应。`zh-cn/` 里以 `[^tN]:` 定义的是译者注。
- 每章第一行是 `#` 一级标题，阅读器用它作章节标题。
- 状态为 `done` 的章节必须整章对上，否则构建失败，并指出第一个对不上的块。
- `draft` 和 `review` 的章节允许译到一半，但已经译出的部分也必须对上。

## book.json

```json
{
  "title": "谷歌的软件工程",
  "originalTitle": "Software Engineering at Google",
  "authors": "Titus Winters, Tom Manshreck, Hyrum Wright",
  "reader": "bilingual",
  "summary": "书架卡片上的一两句介绍。",
  "facts": ["25 章", "中英逐段对照"],
  "cover": "assets/images/cover.jpg",
  "page": {"description": "网页描述", "shareTitle": "分享时的标题", "themeColor": "#b4423a", "storageKey": "阅读设置保存用的键名"},
  "start": "ch01",
  "chapterMaps": true,
  "listed": true,
  "chapters": [
    {"id": "preface", "file": "Preface.md", "status": "done"},
    {"id": "ch01", "number": 1, "file": "Chapter-1/Chapter-1.md", "status": "draft"}
  ]
}
```

| 字段 | 说明 |
| --- | --- |
| `title`、`originalTitle`、`authors` | 书名、原书名、作者，显示在书架和阅读器上 |
| `summary`、`facts`、`cover` | 书架卡片的介绍、标签和封面；`cover` 是构建后书里的路径，没有封面时显示书名 |
| `page` | 可选。网页描述、分享标题、主题色，以及阅读设置在浏览器里保存用的键名 |
| `start` | 可选。第一次打开时进入的章节，默认是第一个发布的章节 |
| `chapterMaps` | 为 `true` 时，每个发布的编号章节都必须有章首概览和章末回顾 |
| `listed` | 为 `false` 时不出现在书架上 |
| `chapters` | 阅读顺序。`file` 是这一章在 `en/` 和 `zh-cn/` 下共同的相对路径；编号章节的 id 写成 `ch01` 这种形式 |
| `source` | 导入时自动写入，记录 EPUB 文件名和它的 SHA-256，方便以后确认原文版本 |

`custom` 的书另外写 `build`（构建命令列表）、`output`（构建结果所在的目录）、`checks`（检查命令列表），以及可选的 `links`（书架卡片上的额外链接）。构建时会通过环境变量 `BOOK_BASE` 和 `BOOK_URL` 告诉它网址前缀。

## 图解、代码改写和字体

- **章首概览和章末回顾**：每章一份 `assets/diagrams/chNN.json`，写明这一章要回答的问题、分几块、各块的关系，以及章末的几幕故事。构建时生成桌面和手机两套 SVG，文字超出版式预算就构建失败。数据的写法照着 `books/swe-at-google/assets/diagrams/` 里的例子。图标从 `framework/tools/icons.json` 里选；要用新的 Lucide 图标，运行 `uv run --project framework/tools python framework/tools/fetch_reader_assets.py`。
- **小节细节图**：手工画的 SVG 和它的说明数据放在 `assets/diagrams/sections/`，用 `afterParagraph` 指定插在哪一段后面。
- **代码改写**：书里的 Java、C++、Go 示例要配 Python 写法时，在 `assets/code-variants/<章节 id>/` 下放 `NN.java` 和 `NN.py`；没有对应写法的放 `NN.skip`，写明原因。
- **字体**：阅读器的正文用思源宋体，按每本书用到的字符裁剪，放在这本书的 `assets/fonts/` 里并提交。译文新增了字符而字体没有重新生成时，严格构建会失败，并提示运行 `site.py fonts`。

## 每章的小结与要点

在书的目录下放 `recaps/<章节 id>.md`，构建时会把它显示在这一章正文之后、翻页导航之前，标题是“本章小结与要点”，并标明“译者整理”。它也会收进全书搜索，右侧的本章目录里可以跳过去。

文件里不写标题：先写一两段话概括这一章，再空一行，列 4 到 5 条要点。内容只能来自这一章本身，写完后由另一个 agent 对照原文核实每个事实和数字。示例见 `books/thinking-fast-and-slow/recaps/ch11.md`。

## 翻译和审校的做法

在这个仓库里用 Codex 或 Claude Code 工作时，会自动加载两个技能（放在仓库根目录的 `.agents/skills/` 下）：`translate-book` 讲在这个仓库里译书的步骤，`en-zh-translation-polish` 讲怎样把英文译成准确、自然的中文。

每章的审校分四项，记在这本书的 `review/<章节 id>.md` 里，每项写明是谁做的、覆盖了哪些范围、发现了什么：

1. 译者自检：对照原文查漏译、增译、否定、条件和术语。
2. 对照原文的双语审校：由另一个人或另一个独立的 agent 来做。
3. 顺着中文的连续通读。
4. 在阅读器里的最终校样。

四项都完成，这一章才改成 `done`。模型之间互相审校，算不上专业的人工审校，发布时要写清楚。导入原文时的核对结果记在 `review/source.md`。

## 目录

```text
framework/reader/           共用阅读器：index.html 模板、reader.js、reader.css、图标和本地化的 Docsify
framework/tools/            构建和检查工具，用 uv 管理（pyproject.toml）
  build.py                  构建一本书：章节数据、章首章末图、搜索索引、侧边栏和页面
  book.py                   解析 Markdown，把中英两边逐块对齐
  reader_data.py            章节清单、代码改写和图解的检查与输出
  chapter_figures.py        从 chNN.json 生成章首概览和章末回顾的 SVG
  search_index.py           全书搜索索引
  fonts.py                  按书裁剪中文字体
  config.py                 读取、检查和写回 book.json
  new_book.py               建新书的目录
  import_epub.py            从 EPUB 导入英文原文
  status.py                 翻译进度（章末小结由 reader_data.py 读取 recaps/）
  tests/                    框架自己的测试
```

框架的测试：`uv run --project framework/tools --with pytest pytest -q framework/tools/tests`。
