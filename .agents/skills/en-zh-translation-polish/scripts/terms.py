#!/usr/bin/env python3
"""Discover terminology candidates or count reviewed aliases. Never rewrite translations."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from importlib.metadata import version
import json
from pathlib import Path
import re
import sys
import tempfile

from io_utils import digest, write_json

WORD = re.compile(r"\.[A-Za-z][A-Za-z0-9]*|[A-Za-z][A-Za-z0-9]*(?:[-./'][A-Za-z0-9]+)*(?:\+\+|#)?|[^\w\s]")
ZH_STOP = {"我们", "你们", "他们", "这个", "那个", "这些", "那些", "以及", "但是", "因此", "一个", "一种"}
EN_STOP = set("""a an the and or but if then else so as at by for from in into of on onto
to with without through about above below between under over after before during
is are was were be been being am do does did done have has had having can could
may might must shall should will would not no nor yes i me my mine we us our ours
you your yours he him his she her hers it its they them their theirs this that
these those who whom whose which what when where why how here there all any each
every both either neither some such more most other another than very also only
just own same too up down out off once again s t""".split())


def load_corpora(paths):
    segments, identities, seen = [], {}, {}
    for path in paths:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("type") != "translation-corpus" or data.get("schema") != 1:
            raise ValueError(f"Not a supported corpus: {path}")
        for file, checksum in data["sources"].items():
            identity = (data["root"], file)
            if identity in identities and identities[identity] != checksum:
                raise ValueError(f"Mixed revisions of the same document: {identity}")
            identities[identity] = checksum
        for entry in data["segments"]:
            row = {**entry, "root": data["root"]}
            key = (data["root"], entry["id"])
            if key in seen:
                if seen[key] != row:
                    raise ValueError(f"Conflicting extraction policies for {entry['id']}")
                continue
            seen[key] = row
            segments.append(row)
    if not segments:
        raise ValueError("Corpus has no analyzable segments")
    return segments


def alias_pattern(aliases, english, case_sensitive=False):
    if not aliases or any(not isinstance(alias, str) or not alias.strip() for alias in aliases):
        raise ValueError("Aliases must be nonempty strings")
    alternatives = [r"\s+".join(re.escape(word) for word in alias.split())
                    for alias in sorted(set(aliases), key=lambda item: (-len(item), item))]
    expression = "(?:" + "|".join(alternatives) + ")"
    if english:
        expression = r"(?<![A-Za-z0-9_+#])" + expression + r"(?![A-Za-z0-9_+#])"
    return re.compile(expression, re.I if english and not case_sensitive else 0)


def segment_index(segments, language):
    index = defaultdict(set)
    for number, segment in enumerate(segments):
        if segment["language"] == language:
            tokens = re.findall(r"[A-Za-z0-9_]+", segment["text"].casefold()) if language == "en" else set(segment["text"])
            for token in tokens:
                index[token].add(number)
    return index


def recount(segments, aliases, language, index=None, *, case_sensitive=False):
    pattern = alias_pattern(aliases, language == "en", case_sensitive)
    forms, documents, evidence = Counter(), Counter(), []
    possible = set()
    if index is not None:
        for alias in aliases:
            first = re.search(r"[A-Za-z0-9_]+", alias.casefold()) if language == "en" else None
            key = first.group() if first else alias[0] if language == "zh" else None
            if key is None:
                possible = set(range(len(segments)))
                break
            possible.update(index.get(key, set()))
    for number in sorted(possible) if index is not None else range(len(segments)):
        segment = segments[number]
        if segment["language"] != language:
            continue
        for match in pattern.finditer(segment["text"]):
            forms[match.group()] += 1
            documents[f'{segment["root"]}/{segment["file"]}'] += 1
            evidence.append({"root": segment["root"], "file": segment["file"],
                "segment": segment["id"], "line": segment["line"],
                "start": match.start(), "end": match.end(),
                "context": segment["text"][max(0, match.start() - 40):match.end() + 40]})
    return {"frequency": sum(forms.values()), "document_frequency": len(documents),
            "documents": dict(sorted(documents.items())), "forms": dict(sorted(forms.items())),
            "evidence": evidence}


def noun_spans(tagged, max_words):
    """Shared short-phrase policy; backend tags/lemmas remain separately reported."""
    for start in range(len(tagged)):
        for end in range(start + 1, min(start + max_words, len(tagged)) + 1):
            span = tagged[start:end]
            if any(item["pos"] not in {"NOUN", "PROPN", "ADJ"} for item in span):
                break
            if span[-1]["pos"] not in {"NOUN", "PROPN"}:
                continue
            yield span[0]["start"], span[-1]["end"], " ".join(item["lemma"].casefold() for item in span)


def load_expression_patterns(path):
    rules = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(rules, list) or not rules:
        raise ValueError("Expression rules must be a nonempty JSON array")
    seen = set()
    for rule in rules:
        if not isinstance(rule, dict) or set(rule) != {"id", "patterns"}:
            raise ValueError("Each expression rule needs only id and patterns")
        identifier = rule["id"]
        if not isinstance(identifier, str) or not identifier.strip() or identifier in seen:
            raise ValueError("Expression rule IDs must be unique nonempty strings")
        seen.add(identifier)
        patterns = rule["patterns"]
        if not isinstance(patterns, list) or not patterns:
            raise ValueError(f"Empty expression patterns: {identifier}")
        if any(not isinstance(pattern, list) or not pattern or
               any(not isinstance(token, dict) or not token for token in pattern)
               for pattern in patterns):
            raise ValueError(f"Patterns must contain nonempty token-attribute objects: {identifier}")
    return rules


def english_vocabulary(segments, backend, model, max_words, expression_patterns=()):
    if expression_patterns and backend != "spacy":
        raise ValueError("--expression-patterns requires the explicit spaCy backend; no fallback")
    vocabulary = defaultdict(lambda: {"forms": set(), "signals": set(), "pattern_matches": []})
    english_segments = [segment for segment in segments if segment["language"] == "en"]
    english = [segment["text"] for segment in english_segments]
    if not english:
        return vocabulary, {"backend": backend, "status": "not_run_no_english"}

    def add(text, start, end, key, signal):
        form = text[start:end]
        if len(key) < 2 or key.casefold() in EN_STOP or not re.search("[A-Za-z]", key):
            return
        vocabulary[key]["forms"].add(form)
        vocabulary[key]["signals"].add(signal)

    if backend == "nltk":
        import nltk
        from nltk.stem import WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()
        try:
            for text in english:
                matches = list(WORD.finditer(text))
                tagged = nltk.pos_tag([match.group() for match in matches])
                normalized = []
                for match, (word, tag) in zip(matches, tagged):
                    pos = "PROPN" if tag.startswith("NNP") else "NOUN" if tag.startswith("NN") else "ADJ" if tag.startswith("JJ") else "OTHER"
                    lemma = word if pos == "PROPN" or word.isupper() else lemmatizer.lemmatize(word.lower(), "a" if pos == "ADJ" else "n")
                    normalized.append({"pos": pos, "lemma": lemma, "start": match.start(), "end": match.end()})
                for start, end, key in noun_spans(normalized, max_words):
                    add(text, start, end, key, "pos_ngram")
        except LookupError as error:
            raise ValueError("NLTK data missing. Explicitly install averaged_perceptron_tagger_eng and wordnet; no automatic download was attempted.") from error
        info = {"backend": backend, "version": version("nltk"), "model": "averaged_perceptron_tagger_eng + wordnet"}
    else:
        import spacy
        from spacy.matcher import Matcher
        try:
            nlp = spacy.load(model)
        except OSError as error:
            raise ValueError(f"spaCy model unavailable: {model}. Install/select a local English model explicitly.") from error
        if not {"tagger", "parser", "lemmatizer"}.issubset(nlp.pipe_names):
            raise ValueError("spaCy backend requires a trained English POS/parser/lemmatizer pipeline")
        matcher = Matcher(nlp.vocab, validate=True)
        for rule in expression_patterns:
            matcher.add(rule["id"], rule["patterns"])
        for segment, doc in zip(english_segments, nlp.pipe(english, batch_size=32)):
            normalized = [{"pos": token.pos_, "lemma": token.text if token.pos_ == "PROPN" else token.lemma_,
                           "start": token.idx, "end": token.idx + len(token)} for token in doc]
            for start, end, key in noun_spans(normalized, max_words):
                add(doc.text, start, end, key, "pos_ngram")
            for chunk in doc.noun_chunks:
                trimmed = list(chunk)
                while trimmed and (trimmed[0].is_stop or trimmed[0].pos_ in {"DET", "PRON", "NUM"}):
                    trimmed.pop(0)
                if trimmed and len(trimmed) <= max_words:
                    key = " ".join((token.text if token.pos_ == "PROPN" else token.lemma_).casefold() for token in trimmed)
                    add(doc.text, trimmed[0].idx, trimmed[-1].idx + len(trimmed[-1]), key, "noun_chunk")
            for match_id, start, end in matcher(doc) if expression_patterns else ():
                span = doc[start:end]
                if not span or len(span) > max_words or any(token.is_sent_start for token in span[1:]):
                    continue
                key = " ".join((token.text if token.pos_ == "PROPN" else token.lemma_).casefold()
                               for token in span)
                identifier = nlp.vocab.strings[match_id]
                add(doc.text, span.start_char, span.end_char, key, "expression_pattern:" + identifier)
                if key in vocabulary:
                    vocabulary[key]["pattern_matches"].append({
                        "rule": identifier, "root": segment.get("root"), "file": segment.get("file"),
                        "segment": segment.get("id"), "line": segment.get("line"),
                        "start": span.start_char, "end": span.end_char, "text": span.text})
        info = {"backend": backend, "version": version("spacy"), "model": model,
                "model_version": nlp.meta.get("version"), "pipeline": nlp.pipe_names}
    for text in english:
        for match in WORD.finditer(text):
            word = match.group()
            if len(word) > 1 and (word.isupper() or word.endswith(("++", "#")) or word.startswith(".")):
                add(text, match.start(), match.end(), word.casefold(), "technical_surface")
    return vocabulary, info


def chinese_vocabulary(segments, dictionary, max_tokens):
    if not any(segment["language"] == "zh" for segment in segments):
        return set()
    import jieba
    import jieba.posseg
    tokenizer = jieba.Tokenizer()
    tokenizer.tmp_dir = tempfile.gettempdir()
    if dictionary:
        with Path(dictionary).open("rb") as stream:
            tokenizer.load_userdict(stream)
    tagger = jieba.posseg.POSTokenizer(tokenizer)
    words = set()
    for segment in segments:
        if segment["language"] != "zh":
            continue
        tokens = list(tagger.cut(segment["text"], HMM=False))
        for start in range(len(tokens)):
            if start and tokens[start - 1].word in {"不", "非", "无", "未"}:
                continue
            phrase = ""
            for end in range(start, min(start + max_tokens, len(tokens))):
                token = tokens[end]
                negation = end == start and token.word in {"不", "非", "无", "未"}
                if not re.fullmatch(r"[\u3400-\u9fff]+", token.word) or token.word in ZH_STOP:
                    break
                if token.flag[0] not in "nvajli" and not negation:
                    break
                phrase += token.word
                if 2 <= len(phrase) <= 16 and not negation:
                    words.add(phrase)
                if len(phrase) > 16:
                    break
    return words


def glossary_entries(path):
    if path.suffix == ".tsv":
        with path.open(encoding="utf-8", newline="") as stream:
            raw = list(csv.DictReader(stream, delimiter="\t"))
        entries = [{**row, "id": row.get("id") or row["english"], "english": row["english"],
                    "preferred_zh": row["preferred_zh"],
                    "en_forms": row["en_forms"].split("|"), "zh_forms": row["zh_variants"].split("|"),
                    "scope": row.get("scope", row.get("meaning", row.get("sense", ""))), "status": row.get("status", "")}
                   for row in raw]
    else:
        entries = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise ValueError("Glossary must be a nonempty JSON array or supported TSV")
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or not all(entry.get(key) for key in ("id", "preferred_zh", "en_forms", "zh_forms")):
            raise ValueError("Each glossary entry needs id, preferred_zh, en_forms, zh_forms")
        if not all(isinstance(entry[key], str) for key in ("id", "preferred_zh")):
            raise ValueError("Glossary id and preferred_zh must be strings")
        if entry["id"] in seen:
            raise ValueError(f"Duplicate glossary ID: {entry['id']}")
        seen.add(entry["id"])
        if "en_case_sensitive" in entry and not isinstance(entry["en_case_sensitive"], bool):
            raise ValueError("en_case_sensitive must be a JSON boolean")
        for key in ("en_forms", "zh_forms"):
            if not isinstance(entry[key], list):
                raise ValueError(f"{key} must be an alias array")
            alias_pattern(entry[key], key == "en_forms")
    return entries


def main(argv=None):
    cli = argparse.ArgumentParser(description=__doc__)
    sub = cli.add_subparsers(dest="command", required=True)
    candidates = sub.add_parser("candidates")
    count = sub.add_parser("count")
    for command in (candidates, count):
        command.add_argument("--corpus", type=Path, nargs="+", required=True)
        command.add_argument("--out", type=Path, required=True)
        command.add_argument("--overwrite", action="store_true")
    candidates.add_argument("--english-backend", choices=["nltk", "spacy"], default="nltk")
    candidates.add_argument("--spacy-model", default="en_core_web_sm")
    candidates.add_argument("--zh-dictionary", type=Path)
    candidates.add_argument("--expression-patterns", type=Path, help="Explicit project spaCy Matcher rules; never auto-applied.")
    candidates.add_argument("--min-frequency", type=int, default=2)
    candidates.add_argument("--max-words", type=int, default=5)
    candidates.add_argument("--zh-max-tokens", type=int, default=3)
    count.add_argument("--glossary", type=Path, required=True)
    args = cli.parse_args(argv)
    try:
        segments = load_corpora(args.corpus)
        indices = {language: segment_index(segments, language) for language in ("en", "zh")}
        forbidden = [*args.corpus]
        for file in args.corpus:
            data = json.loads(file.read_text(encoding="utf-8"))
            forbidden.extend(Path(data["root"]) / name for name in data["sources"])
        result = {"schema": 1, "inputs": {str(p.resolve()): digest(p.read_bytes()) for p in args.corpus},
                  "tool_sha256": digest(Path(__file__).read_bytes()),
                  "count_policy": "Longest alias first within an entry; separate entries may overlap. English uses ASCII identifier boundaries, case-insensitive unless en_case_sensitive is true; Chinese counts literal substrings. Whitespace in aliases is flexible.",
                  "boundary": "Counts are not reviewed senses, bilingual alignment, missing-translation findings or permission to replace text."}
        if args.command == "count":
            forbidden.append(args.glossary)
            result["type"] = "glossary-counts"
            result["glossary_sha256"] = digest(args.glossary.read_bytes())
            result["terms"] = [{**entry, "english_counts": recount(segments, entry["en_forms"], "en", indices["en"], case_sensitive=entry.get("en_case_sensitive", False)),
                                "chinese_counts": recount(segments, entry["zh_forms"], "zh", indices["zh"])}
                               for entry in glossary_entries(args.glossary)]
        else:
            if args.min_frequency < 1 or not 1 <= args.max_words <= 12 or not 1 <= args.zh_max_tokens <= 6:
                raise ValueError("Frequency must be positive; max words 1-12; Chinese max tokens 1-6")
            patterns = load_expression_patterns(args.expression_patterns) if args.expression_patterns else []
            vocabulary, info = english_vocabulary(segments, args.english_backend, args.spacy_model,
                                                  args.max_words, patterns)
            result.update(type="terminology-candidates", english_analyzer=info,
                          jieba_version=version("jieba") if any(s["language"] == "zh" for s in segments) else None,
                          status="unreviewed_candidates")
            if args.zh_dictionary:
                forbidden.append(args.zh_dictionary)
                result["dictionary_sha256"] = digest(args.zh_dictionary.read_bytes())
            if args.expression_patterns:
                forbidden.append(args.expression_patterns)
                result["expression_patterns_sha256"] = digest(args.expression_patterns.read_bytes())
            rows = []
            for key, entry in vocabulary.items():
                counts = recount(segments, entry["forms"], "en", indices["en"])
                if counts["frequency"] >= args.min_frequency:
                    row = {"candidate": key, "signals": sorted(entry["signals"]), **counts}
                    if entry["pattern_matches"]:
                        row["pattern_matches"] = entry["pattern_matches"]
                    rows.append(row)
            result["english"] = sorted(rows, key=lambda row: (-row["frequency"], row["candidate"]))
            rows = []
            for word in chinese_vocabulary(segments, args.zh_dictionary, args.zh_max_tokens):
                counts = recount(segments, [word], "zh", indices["zh"])
                if counts["frequency"] >= args.min_frequency:
                    rows.append({"candidate": word, **counts})
            result["chinese"] = sorted(rows, key=lambda row: (-row["frequency"], row["candidate"]))
            result["discovery_policy"] = {"min_frequency": args.min_frequency, "max_english_words": args.max_words,
                                          "max_chinese_tokens": args.zh_max_tokens, "surface_recount": True,
                                          "expression_rule_ids": [rule["id"] for rule in patterns],
                                          "expression_scope": "Within one sentence, bounded by max_words. Pattern evidence is distinct from global surface recount."}
        write_json(args.out, result, forbidden=forbidden, overwrite=args.overwrite)
        print(f"Wrote {args.out}")
        return 0
    except (ValueError, OSError, ImportError, KeyError) as error:
        cli.exit(2, f"error: {error}\nSee reference/reusable-scripts.md for explicit dependency/model setup.\n")


if __name__ == "__main__":
    sys.exit(main())
