# Changelog

## [1.7.0-local] - 2026-09-21

Local update only; no upstream release.

- 图解参考新增“章首、章中、章末三类图的分工”：章首图是读前地图（问题、分块、一句话答案，日常语言，约一百字），章中图锚在所解释的例子之后只答一个问题，章末图按情节重讲本章并标出最想强调的主张；三类不重复。
- 章首图用五到七种图形形式的小库按章选形，图标承担含义、形状承担关系；把目录装进编号方框不算可视化。
- 审校边界说明留在元数据 `limits`，不写进图底小字；大范围重画前先分析、说方案、出一两章前后对比原型，获准再推广。
- 多章图形由每章内容数据生成：文字槽位有宽度预算，超出即构建失败；固定宽度、高度随内容；手机版式竖向重排；图标路径连许可一起入库；生成接入 CI。
- 浏览器验收补充几何检查步骤：内联 SVG 后按 `getBoundingClientRect()` 报告越界、重叠与越出所属方框，人工复核误报。
- 审核模板增加“图内文字”一行；新增回归用例 edge-34。

- Add a three-role split for book figures: chapter-opening maps (question, parts, one-line answer in everyday words), section figures anchored after the example they explain, chapter-closing storylines that retell the chapter and name what it insists on.
- Opening maps pick one of five to seven visual forms per chapter; icons carry meaning and shape carries relations. Numbered boxes holding an outline do not count as visualization.
- Reviewer caveats stay in `limits` metadata, not in small print inside the figure; large redraws start with analysis, a stated approach and a one- or two-chapter before/after prototype.
- Multi-chapter figures are generated from per-chapter content data with per-slot width budgets that fail the build, fixed width and content-driven height, a stacked mobile layout, vendored icon paths with license, and CI regeneration.
- Rendered validation adds a browser geometry pass over all SVGs; the review template gains an in-figure text row; regression prompt edge-34 added.

## [1.6.1-local] - 2026-09-21

Local update only; no upstream release.

- 最终格式校样增加“同类结构渲染一致”检查：同一列表各项、同一层级标题、同类注释和术语条目外观应相同；术语单独成行的列表项需要行尾两个空格的硬换行。
- Markdown 保护清单点名行尾硬换行；中文照英文结构书写时一并复制硬换行、缩进与嵌套层级。
- 登记为“已审阅、未改动”的行也要与兄弟行比对行尾标记与缩进。
- 新增回归用例 edge-33：同一列表中只有一项渲染成另一种样子。
- 1.3.0-local 到 1.6.0-local 的改动当时没有写入本日志；其内容以 SKILL.md 与 reference/ 为准。

- Final proofreading checks that sibling structures render alike; term-only list lines need the trailing two-space hard break.
- The Markdown protection list names the hard break; Chinese mirroring an English structure copies these markers, indentation and nesting.
- Lines recorded as reviewed-unchanged are compared with sibling lines for line-ending markers and indentation.
- Add regression prompt edge-33. Versions 1.3.0-local through 1.6.0-local were applied without changelog entries; SKILL.md and reference/ are authoritative.

## [1.2.0-local] - 2026-09-20

Local update only; no upstream release or measured translation-quality claim.

- Preserve existing repository formats instead of imposing a new bilingual template.
- Add an optional repository workflow for source baselines, corpus-based terminology,
  chapter-scoped native subagents and separate semantic/preservation verification.
- Replace unsafe whole-line punctuation and blockquote-deletion recipes with
  structure-aware editing and confirmed paragraph mappings.
- Add an opt-in diagram/reader workflow covering source-grounded concepts,
  responsive SVGs and separate static, interaction and visual evidence.
- Add seven realistic regression prompts; the prompt list is not an execution report.

## [1.1.0] - 2026-09-12

### Changed / 变更

- 明确触发范围：英文段落翻译，以及对照原文润色中文译稿。
- 短段落直接在聊天中交付，用户要求文件时才落盘；全文与项目翻译保留默认文件契约。
- 尊重用户已指定的纯译文、双语或目标文件，不重复确认；按文体选择必要检查，短文本无需展示完整诊断过程或通读全部参考表。
- 将版本与标签字段归入标准 `metadata`，同步中英文使用说明。
- 独立安装使用；文档输入依据宿主可用工具读取，明确提取缺口并保留请求范围。

- Clarify triggering for English passages and source-grounded polishing of Chinese translations.
- Deliver short passages in chat unless a file is requested; retain the default file contract for full-text and project translations.
- Honor explicit output choices without repeated confirmation; use checks appropriate to the text without requiring a full diagnostic display or every reference table for short passages.
- Place version and tags under standard `metadata` and align the Chinese and English documentation.
- Support standalone installation and document inputs through available host tools, with explicit extraction limitations.

The translation methodology, source-fidelity requirements, reference materials, and MIT license remain in place. This release does not introduce a new translation engine or claim a measured quality improvement.

## [1.0.0] - 2026-06-14

首个公开发布：基于叶子南英汉翻译方法论的翻译与润色流程，包含文本定档、三份参考表、中英对照交付、中英文说明与 MIT 许可。原标签及 GitHub Release 保留。

First public release: a translation and polishing workflow based on Ye Zinan's methodology, with text classification, three reference tables, bilingual delivery, Chinese and English documentation, and the MIT license. The original tag and GitHub Release are retained.

[1.1.0]: https://github.com/HoraceLuBFA/en-zh-translation-polish/releases/tag/v1.1.0
[1.0.0]: https://github.com/HoraceLuBFA/en-zh-translation-polish/releases/tag/v1.0.0
