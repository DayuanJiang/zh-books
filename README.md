# 中文译本书架

对照原文修订的中文译本合集。所有书共用一套阅读器和工具，每本书配有章节图解、术语表和审校记录，发布在同一个网站上。

在线阅读：<https://dayuanjiang.github.io/zh-books/>

## 书目

| 书 | 目录 | 阅读器 | 在线阅读 |
| --- | --- | --- | --- |
| 软件设计的哲学（第二版）<br><sub>A Philosophy of Software Design, 2nd Edition</sub> | [`books/aposd2e`](books/aposd2e) | 自带的 VuePress 阅读器，简体与繁体，代码可切换为 Python | [打开](https://dayuanjiang.github.io/zh-books/aposd2e/) |
| 谷歌的软件工程<br><sub>Software Engineering at Google</sub> | [`books/swe-at-google`](books/swe-at-google) | 共用的中英对照阅读器，代码可切换为 Python | [打开](https://dayuanjiang.github.io/zh-books/swe-at-google/) |

每本书目录里的 README 介绍这本书的特色、审校方法、怎样参与修改，以及译文来源和许可。

## 常用命令

都在仓库根目录运行，只需要 Python 3、[uv](https://docs.astral.sh/uv/)，以及构建《软件设计的哲学》用的 Node.js。

```bash
python3 scripts/site.py serve                 # 构建整站并预览：http://127.0.0.1:8000/zh-books/
python3 scripts/site.py serve --drafts        # 连同正在翻译的章节一起预览
python3 scripts/site.py check swe-at-google   # 运行一本书的全部检查，和 CI 一样
python3 scripts/site.py status <书>           # 每章的翻译进度
python3 scripts/site.py new <书> --title 中文书名 --original-title "English Title" --authors "Author"
python3 scripts/site.py import-epub <书> book.epub
python3 scripts/site.py sync-skill            # 把个人目录里的翻译技能同步进仓库
```

翻一本新书的完整步骤、`book.json` 的写法和中英两边逐块对应的规则，见 [framework/README.md](framework/README.md)。

## 仓库结构

```text
books/<书>/                一本书：book.json 和书的内容；共用阅读器的书只放 en/、zh-cn/、assets/
framework/                 共用的中英对照阅读器和构建、检查、导入工具
scripts/site.py            所有命令的入口：列出、检查、构建、预览、新建、导入、进度
site/shelf.html            书架首页的模板，书的卡片从各书的 book.json 生成
site.json                  网站标题、公开网址和仓库地址
.agents/skills/            译书用的两个技能，Codex 从这里读取：en-zh-translation-polish 和 translate-book
.claude/skills/            指向 .agents/skills/ 同名目录的链接，Claude Code 从这里读取
.github/workflows/ci.yml   每本书一个检查任务，书的列表从 book.json 自动得出；推送到 main 且全部通过后构建整站并部署
```

构建结果写到 `_site/`，不放进仓库。仓库改名或换网址时，改 `site.json`；《软件设计的哲学》的阅读器里还有两处仓库链接（`docs/.vuepress/config.ts` 和 `ReaderLayout.vue`）要一起改。

## 翻译技能

在这个仓库里用 Codex 或 Claude Code 译书时，会自动加载两个技能：

- `en-zh-translation-polish`：英译汉的翻译和润色方法，两本已有的书都是按它做的。它是 HoraceLuBFA 的同名技能（MIT 许可）在本地修订后的 1.7.0-local 版本，主本在个人目录 `~/.claude/skills/` 下，仓库里的是副本。改动先改主本，再运行 `python3 scripts/site.py sync-skill` 同步进仓库；`sync-skill --check` 只报告两边哪里不一样。
- `translate-book`：在这个仓库里译一本书的步骤：建目录、导入 EPUB、定术语、逐章翻译、每章的四项审校记录、分给多个 agent，以及发布前的检查。它只放在这个仓库里，直接在这里修改。

Claude Code 遇到个人目录和项目里有同名技能时，运行的是个人目录那份。所以个人目录里装了这个技能的人，用的是自己那份；其他人克隆仓库后，用的是仓库里的副本。

## 部署

推送到 `main` 后，CI 先运行框架的测试和每本书的检查，全部通过再用 `scripts/site.py build` 构建整站，交给 GitHub Pages 发布。仓库设置里 Pages 的来源（Source）要选 GitHub Actions。

## 历史记录

两本书原来各有一个仓库：[DayuanJiang/aposd2e-zh](https://github.com/DayuanJiang/aposd2e-zh) 和 [DayuanJiang/Software-Engineering-at-Google](https://github.com/DayuanJiang/Software-Engineering-at-Google)。合并时保留了两边的全部提交历史，文件路径移到了 `books/<书>/` 下面，所以 `git log -- books/aposd2e` 就能看到一本书从头到尾的历史。《谷歌的软件工程》原来的两个标签改名为 `swe-at-google/translation-baseline` 和 `swe-at-google/translation-polish`。它的阅读器和构建工具后来移到了 `framework/`，成为所有书共用的框架。

## 许可

每本书的译文来源、原书版权和许可各不相同，写在各自目录的 README 和 LICENSE 里。`.agents/skills/en-zh-translation-polish/` 保留原作者的 MIT 许可，见其中的 LICENSE。
