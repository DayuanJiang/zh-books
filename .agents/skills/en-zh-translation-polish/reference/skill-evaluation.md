# 技能行为评估

仅在维护、升级或明确评估本技能时读取。普通翻译不启动此流程。单元测试验证脚本，
提示用例定义预期；两者都不能代替模型实际处理任务的结果。

技能行为评估也不等于某本书的质量验收。修改整书流程后，除触发和短样本外，选择含跨章定义、旧译错误、脚注／图文和最终格式的代表性材料走完整流程，记录实际分流、意义修订、审校及校样结果；全部章节的覆盖仍按项目流程记录。只跑短提示或抽样时，结论只能覆盖那些样本，不能写“全书已审”。

## 选择范围与隔离

- 分开测自动触发与任务执行。触发测试只暴露候选技能的名称／描述，不预先要求使用它；
  任务测试才提供指定版本的技能。不能用显式调用成功证明自动触发正确。
- 从 `test-prompts.json` 选与改动有关的真实请求。需要仓库、原文或浏览器的用例，
  先准备最小原始材料；材料缺失就记未运行，不编造执行结果。
- 在独立临时工作区中运行，冻结源文件、技能版本和实际模型配置。完整评估可比较
  无本技能、当前版和候选版；不同版本用相同任务与配置，重复次数按风险和预算选定。
  模型或配置未知时明示未知，不声称完成了严格受控比较。
- 执行者只收到请求、必要原始材料和相应技能，不提供 `expected_behavior`、
  本次怀疑、拟议答案或之前结论。不得把整份用例文件交给执行者。导出的输入只移除
  答案字段，不构成文件访问沙箱；宿主仍需限制可读材料和可写目录。
- 独立 agents 必须得到当前任务授权；不把技能维护授权扩大成付费 API、生产写入
  或读者数据采集授权。脚本不启动模型或 subprocess。

## 离线工具

`scripts/evals.py` 使用标准库；只有记录可选 Markdown 保护校验时才需要 `corpus.py`
的依赖。它导出输入、绑定真实执行材料、汇总外部判读，不自动判断翻译意义。

```sh
python "$SKILL/scripts/evals.py" export --suite "$SKILL/test-prompts.json" --case edge-19 --out /tmp/eval/tasks.json
```

由已获授权的宿主执行器运行选定任务，将实际回答和执行轨迹保存在隔离目录。
文件型任务同时保留修改前基线、实际产物及差异；触发测试的轨迹要能核实实际选中
的技能，而非只看模型口头声称。配置 JSON 填写实际设置，无法取得的项明确记为
`"unknown"`，不推测具体模型版本。记录示例：

```sh
python "$SKILL/scripts/evals.py" record --suite "$SKILL/test-prompts.json" --case edge-19 --variant candidate --mode task --model ACTUAL_MODEL_ID --settings /tmp/eval/settings.json --response /tmp/eval/response.txt --trace /tmp/eval/trace.txt --execution-kind model --skill /path/to/frozen-skill --out /tmp/eval/run.json
```

`--repetition` 标记重复运行。文件型任务可加 `--artifacts-root /tmp/eval/work`
及明确的 `--include '*.md'`；已有保护基线时加 `--baseline /tmp/eval/baseline.json`。
运行记录必须放在产物目录外。纯文本任务可不传产物目录；无本技能的对照不传
`--skill`。`--execution-kind fixture` 仅用于工具测试，不能计为真实模型通过。

记录包含请求、套件、响应、轨迹、技能文件与所选产物的哈希。它不能证明所报模型
身份、执行者确实使用了技能或评审独立性，这些需由宿主运行证据确认。保留这些
文件直到评估完成；材料变动或丢失后应重新采集，不沿用旧通过记录。

## 判读与硬门槛

评审者另看原文、实际输出、产物和 `expected_behavior`；根据可核对的意义及行为
判读，不匹配固定译句、标题或“我完成了”这样的措辞。可用人工或独立模型，模型
评判仍需人工校准，不能自称读者实验。评审不同版本时尽量隐藏版本标签并交换顺序，
减少位置与篇幅偏好；保留分歧，不强行用平均分消除。

每个运行的判读记录使用以下 JSON 数组，哈希从实际文件计算：

```json
[
  {
    "run_sha256": "SHA256_OF_RUN_JSON",
    "response_sha256": "SHA256_OF_RESPONSE_FILE",
    "reviewer": "ACTUAL_REVIEWER_ID",
    "method": "human",
    "verdict": "pass",
    "rationale": "可核对的原文、输出片段和行为证据；包括仍有的限制"
  }
]
```

`method` 为 `human/model/fixture`，`verdict` 为 `pass/fail/unreviewed`。
原文／译文意义问题按[项目审核规则](repository-workflow.md)分类；无法判读的项目
保持 `unreviewed`。一个运行保留一份裁定，多个评审的分歧先明确处理再汇总。

```sh
python "$SKILL/scripts/evals.py" summarize --suite "$SKILL/test-prompts.json" --variant candidate --mode task --case edge-19 --runs /tmp/eval/run.json --judgments /tmp/eval/judgments.json --out /tmp/eval/summary.json
```

`required_case_ids` 是不可被平均分抵消的用例；已记录的保护校验失败也强制失败，
即使外部判读写了通过。缺执行、缺判读或模拟输出均不能通过。

只评估部分用例时最多报告 `passed_selected`；选定整套且完成所有判读才可能为
`passed_suite`。`incomplete` 与 `failed` 都返回非零退出码，不允许用缺失项缩小分母。
重复运行时用 `--repetitions N` 明确期望数量。不同模型／配置／技能快照、不同模式、
不同套件、重复运行标识或过期证据不能混算。

输出与截图数量不等于译文质量、解释增益或稳定性提升。交付评估范围、实际配置、
原始产物、逐项失败、未运行项和修改前后差异；未做版本对照时只报告当前样本表现。

方法参考，按项目规模应用，不绑定云端评估服务：

```text
https://learn.chatgpt.com/docs/build-skills
https://developers.openai.com/api/docs/guides/evaluation-best-practices/
```
