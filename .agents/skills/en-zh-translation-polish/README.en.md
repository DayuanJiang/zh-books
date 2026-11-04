<div align="center">

# en-zh-translation-polish

### Translate English into idiomatic, translationese-free Chinese, with paragraph-by-paragraph bilingual output

[![License: MIT](https://img.shields.io/badge/License-MIT-f5c542.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.7.0--local-2ea44f.svg)](./SKILL.md)
[![Agent Skills](https://img.shields.io/badge/agent-skills-black.svg)](https://github.com/vercel-labs/skills)

**English | [中文](./README.md)**

</div>

---

## Philosophy

This skill turns the English-to-Chinese methodology of Ye Zinan's *Advanced Course in English-Chinese Translation (Fourth Edition)* (《高级英汉翻译理论与实践》) into an executable pipeline. One conviction sits at its core:

> The deadliest mistake in English-to-Chinese translation is carrying English's **hypotactic** (form-driven) structure into Chinese, which produces *translationese*.

Good translation therefore rests on four principles:

- **Reader-first** — communicative translation by default, so the Chinese reader meets fluent, natural Chinese;
- **Domestication tuned to the text** — hard texts (law / tech / contracts) put accuracy first and intervene sparingly; soft texts (essays / commentary / ads) lean into Chinese's parataxis and idiom;
- **Improve expression when needed** — change connectives, voice or sentence structure only when meaning and authorial focus remain intact; retain correct, suitable translations;
- **Mind rhythm and cadence** — use disyllables, four-character structures, and parallelism, but only as far as it stays natural.

The workflow supports text analysis, understanding, Chinese reconstruction, polishing, accuracy checks, and punctuation. Select relevant checks for the text type. Short passages do not require displaying every diagnostic stage or reading every reference table; accuracy and source fidelity still apply.

## What it's for

- **Removing translationese from MT and literal drafts** — hypotaxis transfer, the runaway "的" particle, abstract-noun subjects, overused passives, literally-rendered idioms: each is named and fixed;
- **A consistent editing standard** — three verifiable reference tables fix *what to change, how, and how far* into reusable criteria;
- **Maintaining bilingual versions** — preserve existing project structure and derive Chinese output from confirmed paragraph mappings;
- **Correct Chinese punctuation** — edit only identified Chinese prose, preserving code, English, URLs and technical exceptions rather than rewriting the whole file with regex;
- **Book-scale collaboration and verification** — evidence-backed terminology, chapter ownership, immutable baselines and traceable completion states; diagrams and reader styling are opt-in.

## Boundaries

Method serves the translation, not the other way around. Two cautions from Ye Zinan:

- **Domesticate in moderation** — keep the source's style, terminological precision, and cultural markers; foreignization is a continuum, and hard / lasting-value texts tolerate more of it;
- **Restrain ornament** — rhythm is a means, not an end; four-character phrases are used sparingly;
- When unsure how far to go, return to the task agreement and source context; a freedom score cannot decide meaning.

Bottom line: relaxing accuracy ≠ misunderstanding the source. **A misreading is never forgivable.**

## Workflow

Return short passages directly without book-management overhead. Preserve existing project structure. Diagnose existing translations before choosing revision, full post-editing or local retranslation. Review-only requests produce findings, not manuscript edits.

| Step | Purpose for book-scale work |
|---|---|
| Task agreement and source acceptance | Establish intended use and quality; check edition, text and ancillary material separately from file protection |
| Book overview and language resources | Map concepts, senses, style and approved examples with access to relevant source context |
| Pilot and route selection | When needed, compare final quality and total editing effort rather than assume MT or retranslation is best |
| Translation and self-check | Check meaning and completeness before polishing; recheck substantive changes against the source |
| Bilingual revision and Chinese read-through | Record distinct roles, actual reviewers and coverage; examine continuity and voice without claiming human review |
| Final-format proofreading | Inspect the actual HTML, EPUB, PDF or other agreed artifact without automatically redesigning it |
| Finalization and change review | Resolve queries, retain suitable wording, stop unjustified polishing and recheck affected material after changes |

Three reference tables back the workflow (in `reference/`, each with source quotations and worked English–Chinese examples):

- **`text-analysis-and-qa.md`** — text typing (7 dimensions → freedom, Newmark's XYZ coefficients, the soft/hard master switch), metaphor-translation decisions, and the accuracy-QA checklist;
- **`translationese-symptoms.md`** — 9 classes of translationese with detection signals and fixes, prosody rules, and the foreignization-acceptability boundary;
- **`techniques.md`** — 14 actionable techniques (unpacking, part-of-speech conversion, amplification/omission, division/combination, reordering, relative-clause transforms, negation, passive transforms).

For project-scale work, read [`repository-workflow.md`](reference/repository-workflow.md). Read [`reader-visualization.md`](reference/reader-visualization.md) only when diagrams or reader changes are explicitly requested; ordinary translation does not require it.

## Installation

**Option 1 · One command (recommended)**

```bash
npx skills add -g HoraceLuBFA/en-zh-translation-polish
```

> [`npx skills`](https://github.com/vercel-labs/skills) installs the skill into `~/.agents/skills/` — the shared skill directory read by multiple agents — and wires up each agent's symlinks automatically.

**Option 2 · Let your agent install it**

Send the repo link to your coding agent (Claude Code / Codex / Gemini CLI, etc.) and just ask:

> Install this skill for me: https://github.com/HoraceLuBFA/en-zh-translation-polish

**Option 3 · Manual clone**

```bash
git clone https://github.com/HoraceLuBFA/en-zh-translation-polish.git ~/.agents/skills/en-zh-translation-polish
```

Verify:

```bash
test -f ~/.agents/skills/en-zh-translation-polish/SKILL.md && echo OK
```

## Usage

**Natural language** — just state what you want; agents that auto-trigger will load the skill from the `description` field in `SKILL.md`. Common phrasings:

- "Translate this English into natural, idiomatic Chinese: …"
- "Translate this article — I want an English-Chinese bilingual version."
- "Please translate this technical passage / press release / novel excerpt into Chinese."

This skill handles English texts and source-grounded polishing of existing Chinese translations. This skill can be installed and used independently, without another translation skill. For PDF or other document inputs, use the current host’s available reading tools to obtain the source. Preserve the requested text, captions, formulas, citations, and references. Report extraction gaps rather than handing the task to an uninstalled skill.

**Explicit command** — name the skill directly and pass a file or text as the argument:

```text
# Claude Code: slash command
/en-zh-translation-polish path/to/article.md

# Codex: invoke with $ (or run /skills and pick from the list)
$en-zh-translation-polish path/to/article.md
```

> ⚠️ **Want Chinese only?** The skill **produces a bilingual file by default**. If you want the translation alone, say so explicitly in your prompt (e.g. "Chinese only, no English" / "output the translation only").

## Deliverables

The following files are defaults for new standalone translations. Return short passages in chat; preserve existing project structure and explicit output choices.

1. **`<name> 翻译(中英对照).md`** — the approved translation master: each English paragraph as a blockquote followed by Chinese; retain the original English artifact separately;
2. **`<name> 翻译(全中文).md`** (on request) — derived from confirmed paragraph mappings, never by deleting every blockquote; retain and report untranslated content;
3. Notes where needed on trade-offs, actual coverage and unverified work; short translations need no process or register announcement.

## Output preview

> The confidence that the West would remain a dominant force in the 21st century is giving way to a sense of foreboding.

西方曾笃信自己将在 21 世纪稳居主导地位，如今这份自信，正让位于一种隐隐的不祥之感。

## Sister skill

For the opposite direction (Chinese → English), use **[zh-en-translation-polish](https://github.com/HoraceLuBFA/zh-en-translation-polish)** — distilled from Joan Pinkham's *The Translator's Guide to Chinglish* and Lu Guoqiang's *Classic Examples of Converting Chinese to English*, it produces idiomatic, Chinglish-free English with bilingual pairing. The two skills are structural mirrors, one per direction.

## Repository layout

```text
en-zh-translation-polish/
├── SKILL.md                       # Entry point (translation + conditional routing)
├── README.md                      # Project guide (Chinese)
├── README.en.md                   # Project guide (English)
├── reference/
│   ├── text-analysis-and-qa.md    # Text typing + metaphor + accuracy QA
│   ├── translationese-symptoms.md # Translationese symptoms + prosody + foreignization limits
│   ├── techniques.md              # 14 actionable techniques
│   ├── repository-workflow.md     # Book-scale terminology and preservation checks
│   └── reader-visualization.md    # Optional diagrams and rendered validation
├── test-prompts.json              # Trigger / decoy / edge-case test cases
├── LICENSE
└── .gitignore
```

## Acknowledgments & license

The code, prompts, and structure of this skill are released under the **MIT License** — free to use, modify, and redistribute. See [LICENSE](./LICENSE).

The methodology and worked examples are distilled and paraphrased from **Ye Zinan, 《高级英汉翻译理论与实践》 (Advanced Course in English-Chinese Translation, Fourth Edition), Tsinghua University Press, 2020**, with gratitude. The short quotations in `reference/` are brief excerpts for commentary and teaching; copyright remains with the author and publisher. This skill is a working tool, not a substitute for the book — readers who want to study the subject systematically should buy the original.

This skill was generated with the help of [cangjie-skill](https://github.com/kangarooking/cangjie-skill), an open-source pipeline that distills books into invokable AI skills — also gratefully acknowledged.

## Version history

The current `1.7.0-local` adds, on top of the 1.6.x book translation, review and delivery flow, a three-role split for book figures (opening map, section figure, closing storyline), data-driven figure generation and a browser geometry check. It has not been released upstream. See [SKILL.md](./SKILL.md) and the [project workflow](reference/repository-workflow.md) for current instructions; [CHANGELOG.md](./CHANGELOG.md) retains earlier history.

[v1.1.0](https://github.com/HoraceLuBFA/en-zh-translation-polish/releases/tag/v1.1.0) clarifies triggering and delivery scope, reducing unnecessary process for short passages. See [CHANGELOG.md](./CHANGELOG.md). The original [v1.0.0](https://github.com/HoraceLuBFA/en-zh-translation-polish/releases/tag/v1.0.0) tag, release notes, and source history remain available.
