# 中文译本书架

对照原文修订的中文译本合集。每本书配有专门的阅读器、章节图解、术语表和审校记录，所有书发布在同一个网站上。

在线阅读：<https://dayuanjiang.github.io/zh-books/>

## 书目

| 书 | 目录 | 阅读器 | 在线阅读 |
| --- | --- | --- | --- |
| 软件设计的哲学（第二版）<br><sub>A Philosophy of Software Design, 2nd Edition</sub> | [`books/aposd2e`](books/aposd2e) | VuePress 2，简体与繁体，代码可切换为 Python | [打开](https://dayuanjiang.github.io/zh-books/aposd2e/) |
| 谷歌的软件工程<br><sub>Software Engineering at Google</sub> | [`books/swe-at-google`](books/swe-at-google) | Docsify，中英逐段对照，代码可切换为 Python | [打开](https://dayuanjiang.github.io/zh-books/swe-at-google/) |

每本书目录里的 README 介绍这本书的特色、审校方法、怎样参与修改，以及译文来源和许可。

## 仓库结构

```text
books/<书>/                一本书的全部内容：正文、阅读器、图解、审校记录和工具，各书互相独立
site/index.html            书架首页
scripts/build-site.sh      把所有书构建到 _site/，GitHub Pages 发布的就是这个目录
.github/workflows/ci.yml   每本书一个检查任务；推送到 main 且检查全部通过后，构建整站并部署
```

两本书用的工具不同：《软件设计的哲学》用 Node 和 VuePress 构建，《谷歌的软件工程》的阅读器在浏览器里直接渲染 Markdown，工具脚本用 uv 管理。修改某一本书时，进入它的目录，按那本书 README 里的步骤运行检查。

## 本地预览整站

```bash
bash scripts/build-site.sh
mkdir -p /tmp/zh-books-preview && ln -sfn "$PWD/_site" /tmp/zh-books-preview/zh-books
python3 -m http.server 8000 -d /tmp/zh-books-preview
# 打开 http://localhost:8000/zh-books/
```

网站发布在 `/zh-books/` 路径下，《软件设计的哲学》构建时把这个前缀写进了页面链接，所以本地也要从这个路径打开。

## 部署

推送到 `main` 后，CI 先分别运行每本书的检查，全部通过再用 `scripts/build-site.sh` 构建整站，交给 GitHub Pages 发布。仓库设置里 Pages 的来源（Source）要选 GitHub Actions。

## 添加一本新书

1. 在 `books/` 下新建一个目录，放这本书的正文、阅读器和工具。阅读器可以从现有的两套里复制一套：要中英对照，从 `books/swe-at-google` 开始；只要中文，从 `books/aposd2e` 开始。
2. 在 `scripts/build-site.sh` 里加几行，把这本书的构建结果复制到 `_site/<目录名>/`。
3. 在 `.github/workflows/ci.yml` 里加一个检查任务，并把它加进 `deploy` 的 `needs`。
4. 在 `site/index.html` 里加一张书的卡片，在上面的书目表里加一行。
5. 在这本书的目录里写清译文来源、原书版权和许可。

## 历史记录

两本书原来各有一个仓库：[DayuanJiang/aposd2e-zh](https://github.com/DayuanJiang/aposd2e-zh) 和 [DayuanJiang/Software-Engineering-at-Google](https://github.com/DayuanJiang/Software-Engineering-at-Google)。合并时保留了两边的全部提交历史，文件路径移到了 `books/<书>/` 下面，所以 `git log -- books/aposd2e` 就能看到一本书从头到尾的历史。《谷歌的软件工程》原来的两个标签改名为 `swe-at-google/translation-baseline` 和 `swe-at-google/translation-polish`。

## 许可

每本书的译文来源、原书版权和许可各不相同，写在各自目录的 README 和 LICENSE 里。
