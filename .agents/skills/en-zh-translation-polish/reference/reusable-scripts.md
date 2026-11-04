# 可复用脚本

用于多文件翻译任务中缺少现成工具的情况。优先复用仓库已有解析器与审核流程；
这些脚本不迁移文档框架，不写正文，不内置书籍路径、术语裁定或翻译例外。
所有输出都是 JSON 报告。基线不能覆盖；其他报告仅在显式 `--overwrite`
且原文件是同种报告时可覆盖。输出不能指向输入文件。

## 环境

脚本在 Python 3.12 下测试。复用适合的现有环境，或创建临时环境，避免修改书籍
仓库的依赖。`svg_check.py` 只用标准库；其余依赖分开列出：

- `scripts/requirements.txt`：Markdown 语料提取与基线比较。
- `scripts/requirements-nltk.txt`：上面依赖，加 NLTK 和 jieba。
- `scripts/requirements-spacy.txt`：上面依赖，加 spaCy 和 jieba。

示例，`$SKILL` 是本技能目录：

```sh
uv venv /tmp/translation-tools --python 3.12
uv pip install --python /tmp/translation-tools/bin/python -r "$SKILL/scripts/requirements-nltk.txt"
```

分析脚本不会下载模型，也不会因缺少模型而静默换用另一后端。
需要安装时，先确认网络/环境写入授权，显式执行安装。NLTK 用
`averaged_perceptron_tagger_eng` 和 `wordnet`，可由 `NLTK_DATA` 指向已有目录：

```sh
/tmp/translation-tools/bin/python -m nltk.downloader -d /tmp/translation-nltk averaged_perceptron_tagger_eng wordnet
```

spaCy 测试组合为 3.8.7 与本地 `en_core_web_sm` 3.8.0；须有英文
tagger、parser、lemmatizer。已有模型可直接复用；`--spacy-model` 可指定已安装
模型名或路径。模型不随技能打包。

## 语料与基线：corpus.py

只扫描明确给出的根目录和 glob；glob 要加引号，Markdown 输入使用 UTF-8。
不会把 `HEAD` 当成未提交工作区。
分语言目录可分别提取，再把两个报告交给计数工具：

```sh
python "$SKILL/scripts/corpus.py" extract --root /path/to/book --include 'docs/en/*.md' --language en --out /tmp/review/en.json
python "$SKILL/scripts/corpus.py" extract --root /path/to/book --include 'docs/*.md' --language zh --exclude-section '译者术语表' --out /tmp/review/zh.json
```

英中交错文件：

```sh
python "$SKILL/scripts/corpus.py" extract --root /path/to/book --include 'zh-cn/**/*.md' --language auto --out /tmp/review/mixed.json
```

- 解析 CommonMark、表格、命名脚注、美元/括号形式数学表达式及 frontmatter。
- 保留正文列表、英中引用、表格单元格及未被引用的命名脚注，不按 `>` 整行跳过。
- NLP 默认排除标题、块级代码、行内代码、公式、HTML 块、图片、URL 和 frontmatter。
  `--include-headings`、`--include-inline-code` 可显式改变口径。
- `--exclude-section` 按完整标题忽略该节及其子节的 NLP 内容；重复传参可排除目录、
  现有词表等。不要默认整本 README 后半部都是导航。
- 报告包含文件及脚本哈希、节点 ID、所在行范围、章节、语言来源和被排除的类别数量。
  `line` 是所属节点的源位置，不是精确的双语逐词位置。
- `auto` 是按行的 Latin/Han 启发式，同一节点内相邻同语言行合并。
  单行混杂的英中内容标记 `mixed`，不能据此断言完整提取了所有英文或确认了译文配对。

保存实际工作区的保护基线：

```sh
python "$SKILL/scripts/corpus.py" snapshot --root /path/to/book --include 'docs/**/*.md' --include 'docs/figures/*' --exact 'docs/en/*.md' --out /tmp/review/baseline.json
python "$SKILL/scripts/corpus.py" verify --root /path/to/book --baseline /tmp/review/baseline.json --out /tmp/review/verification.json
```

非 Markdown 文件及 `snapshot --exact` 指定的 Markdown 按字节保护；其他 Markdown
比较代码、公式、英文节点、段内 Latin/数字、链接目标与定义、脚注标识、结构、HTML
和 frontmatter。`verify --exact` 要求所有文件逐字节一致。
文件增删、不同解析器版本及保护内容变化均不静默放行。

**边界**：块级代码按源切片比较；行内代码保留原定界符和空格，但继承 Markdown
解析器的换行正规化。HTML 块整体保护、NLP 排除；复杂 HTML/自定义 Markdown
需要项目适配。混排英文的精确句子范围、中文意义、段落配对和框架生成锚点不由此
证明。合法的结构调整也可能报差异，应单独审查，不重建基线消除失败。

## 术语：terms.py

候选发现支持 spaCy 或 NLTK，中文用 jieba；两种英文分析方法不要求结果相同。
有候选后，用观测到的词形在同一语料中重新计数，避免只计算 POS 标注命中的位置。
输出频次、文档覆盖、原始词形与上下文证据，不产出“已确认译法”。

```sh
NLTK_DATA=/tmp/translation-nltk python "$SKILL/scripts/terms.py" candidates --corpus /tmp/review/en.json /tmp/review/zh.json --english-backend nltk --out /tmp/review/candidates.json
python "$SKILL/scripts/terms.py" candidates --corpus /tmp/review/mixed.json --english-backend spacy --spacy-model en_core_web_sm --out /tmp/review/spacy-candidates.json
```

可选：`--min-frequency`、`--max-words`、`--zh-max-tokens`、
`--zh-dictionary`（jieba 用户词典格式）。中文短语候选保留常见否定前缀。
常见英文功能词从自动候选中排除，不限制人工词表。低频概念、动词短语、长专业表达
与错误分词仍须补查；候选缺席不妨碍审定词条。

### 专业表达的额外候选渠道

默认名词短语策略不会完整发现所有专业表达。另读标题、索引和定义句；需要标题线索
时，单独生成 `--include-headings` 的语料用于发现，不与正文语料合并后声称正文频次。
已知表达可直接加入词表别名。需要自动发现特定结构时，显式提供项目级 spaCy
Matcher JSON，不内置书名或具体概念：

```json
[
  {
    "id": "verb-object-out-of-noun",
    "patterns": [[
      {"POS": "VERB"}, {"POS": "NOUN"}, {"LOWER": "out"},
      {"LOWER": "of"}, {"POS": "NOUN"}
    ]]
  }
]
```

```sh
python "$SKILL/scripts/terms.py" candidates --corpus /tmp/review/en.json --english-backend spacy --expression-patterns /path/to/expressions.json --min-frequency 1 --out /tmp/review/expressions.json
```

此例可发现动词结构，不是通用技术术语定义。`patterns` 使用 spaCy Matcher
属性规则并验证格式；只保留句内、长度不超过 `--max-words` 的匹配。选 NLTK 时
不能使用此选项，也不静默切换后端。规则、正文和原始词形均有哈希或定位证据。

`expression_pattern:<id>` 标记发现渠道，`pattern_matches` 记录实际规则命中；
`frequency/evidence` 仍按观测到的表面词形在整份所选语料中复核，可能包含规则
没有命中的其他语境，不应混称规则频率或义项频率。最低频次也适用于此渠道，
低频表达可设 `--min-frequency 1` 后人工筛选。用人工确认的小样本核对遗漏与噪声；
未被规则提取不等于不是术语。

规则语法参考 spaCy 官方文档：

```text
https://spacy.io/usage/rule-based-matching
```

已审词表使用 JSON 数组；至少列出以下字段，义项/证据/状态按项目需要补充：

```json
[
  {
    "id": "test-size",
    "english": "test size",
    "preferred_zh": "测试规模",
    "en_forms": ["test size", "test sizes"],
    "en_case_sensitive": false,
    "zh_forms": ["测试规模"],
    "scope": "实际语境与不应混同的概念",
    "status": "reviewed",
    "evidence": [{"file": "chapter.md", "quote": "已对照的定义或例子"}]
  }
]
```

也支持 TSV 列 `english / preferred_zh / en_forms / zh_variants`，
后两列用 `|` 分隔别名。其他项目的 lemma keys 不自动当成完整表面词形。

```sh
python "$SKILL/scripts/terms.py" count --corpus /tmp/review/en.json /tmp/review/zh.json --glossary /path/to/terms.json --out /tmp/review/counts.json
```

英文默认按不区分大小写的 ASCII 标识符边界；JSON 词条可用
`en_case_sensitive: true` 区分 `US/us` 等表面词形。词间空白可折叠，同词条长别名优先，
重叠只计一次。中文是字串计数，例如“稳定”可能在“不稳定”内命中；不等于
义项或逐词译法频率。不同词条可能重叠，不能把它们简单相加。
同一文档的不同快照不能混用，同一语料重复输入会去重。零中文命中不证明漏译，
高频译法也不自动成为规范。脚本没有正文替换命令。

## 可选静态图检查：svg_check.py

仅在用户要求图解/阅读器时使用：

```sh
python "$SKILL/scripts/svg_check.py" --root /path/to/book --include 'assets/diagrams/*.svg' --out /tmp/review/svg.json
```

检查 XML、viewBox、非空 title/desc、重复 ID、引用目标及静态矢量资源边界。
脚本/事件/外部资源/内嵌位图等超出此静态配置会报错。
复合路径上的端点 marker 和内嵌 CSS 会给出需人工判断的提示。
只有计划把所选文件放入同一 DOM 范围时才用 `--inline-set` 检查跨文件 ID；
`--warnings-as-errors` 可将提示升级为失败。

这不是 SVG 安全沙箱，也不渲染字形、不检查主题对比、实际箭头外观或理解效果。
字形越界、文字重叠和越出所属方框要在真实浏览器里查，做法见
[reader-visualization.md](reader-visualization.md) 的浏览器验收第 5 步；批量生成的图另由生成器的宽度预算在构建时拦截。
存在非空 title/desc 也不证明宿主页面有合适的 alt、可访问名称或完整文字说明。
浏览器脚本、章节清单、SVG 布局模板、翻译例外和自动接受规则留在项目内；
不要把某本书的 URL、章节数、术语或“通过”状态复制成通用标准。

## 验证

```sh
python -m unittest discover -s "$SKILL/scripts/tests" -v
```

退出码：0 为本次所选检查通过，1 为保护/静态检查发现差异，2 为输入或环境错误。
单元测试验证机械行为；不能替代真实语料、逐项语义裁定或浏览器验收。

维护本技能时，按[行为评估流程](skill-evaluation.md)使用 `evals.py` 导出盲测输入、
记录实际响应和产物哈希、汇总另行判读的结果。它不调用模型，不自动授予 agent/API
执行权限，也不把单元测试的模拟输出算作模型测试。
