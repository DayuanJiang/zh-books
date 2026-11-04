#!/usr/bin/env python3
"""Export blind tasks, capture actual runs, and summarize supplied judgments offline."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

from io_utils import digest, select_files, write_json


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_suite(path):
    suite = read_json(path)
    if not isinstance(suite, dict) or not isinstance(suite.get("test_cases"), list):
        raise ValueError("Suite needs test_cases")
    cases = {}
    for case in suite["test_cases"]:
        if not isinstance(case, dict) or any(not isinstance(case.get(key), str) or not case[key].strip()
                                             for key in ("id", "prompt", "expected_behavior")):
            raise ValueError("Cases need nonempty id, prompt and expected_behavior")
        if case["id"] in cases:
            raise ValueError(f"Duplicate case: {case['id']}")
        cases[case["id"]] = case
    required = suite.get("required_case_ids")
    if not cases or not isinstance(required, list) or any(not isinstance(key, str) for key in required):
        raise ValueError("Suite needs cases and an explicit required_case_ids array")
    if len(set(required)) != len(required) or not set(required) <= cases.keys():
        raise ValueError("Unknown or duplicate required case IDs")
    threshold = suite.get("minimum_pass_rate")
    if isinstance(threshold, bool) or not isinstance(threshold, (int, float)) or not 0 <= threshold <= 1:
        raise ValueError("minimum_pass_rate must be between 0 and 1")
    return suite, cases


def selected_cases(cases, requested):
    chosen = requested or list(cases)
    if len(set(chosen)) != len(chosen) or not set(chosen) <= cases.keys():
        raise ValueError("Unknown or duplicate selected case IDs")
    return chosen


def evidence_file(path):
    path = Path(path).resolve()
    if not path.is_file():
        raise ValueError(f"Evidence file missing: {path}")
    return {"path": str(path), "sha256": digest(path.read_bytes())}


def check_evidence(item):
    if not isinstance(item, dict) or set(item) != {"path", "sha256"}:
        raise ValueError("Malformed evidence reference")
    if evidence_file(item["path"]) != item:
        raise ValueError(f"Evidence changed after capture: {item['path']}")


def worktree_fingerprint(root, baseline):
    selection = baseline["selection"]
    files = select_files(root, selection["include"], selection["exclude"], allow_empty=True)
    state = {name: {"sha256": digest(path.read_bytes()),
                    "symlink": str(path.readlink()) if path.is_symlink() else None}
             for name, path in files.items()}
    return digest(json.dumps(state, sort_keys=True))


def export_tasks(suite_path, requested):
    _, cases = load_suite(suite_path)
    return {"schema": 1, "type": "skill-eval-tasks",
            "suite_sha256": digest(Path(suite_path).read_bytes()),
            "tasks": [{"id": key, "prompt": cases[key]["prompt"]}
                      for key in selected_cases(cases, requested)]}


def capture_run(args):
    _, cases = load_suite(args.suite)
    selected_cases(cases, [args.case])
    if args.repetition < 1 or not args.model.strip() or not args.variant.strip():
        raise ValueError("Model/variant must be nonempty and repetition positive")
    settings = read_json(args.settings)
    if not isinstance(settings, dict):
        raise ValueError("Settings must be a JSON object of actual or explicitly unknown runtime values")
    response = evidence_file(args.response)
    if not Path(response["path"]).read_bytes().strip():
        raise ValueError("No response captured; leave this run missing instead of declaring completion")
    trace = evidence_file(args.trace)
    if not Path(trace["path"]).read_bytes().strip():
        raise ValueError("Trace must contain actual execution evidence")
    artifacts = []
    if args.artifacts_root:
        if not args.include:
            raise ValueError("--artifacts-root requires explicit --include globs")
        if args.out.resolve().is_relative_to(args.artifacts_root.resolve()):
            raise ValueError("Keep the run report outside the evaluated artifact directory")
        artifacts = [evidence_file(path) for path in
                     select_files(args.artifacts_root, args.include).values()]
    elif args.include or args.baseline:
        raise ValueError("--include/--baseline require --artifacts-root")
    skill_files = []
    if args.skill:
        if not (args.skill / "SKILL.md").is_file():
            raise ValueError("--skill must contain SKILL.md")
        skill_files = [evidence_file(path) for path in select_files(
            args.skill, ["SKILL.md", "reference/*.md", "scripts/*.py", "scripts/requirements*.txt"]).values()]
    protection = None
    if args.baseline:
        import corpus
        baseline = evidence_file(args.baseline)
        source_baseline = read_json(args.baseline)
        protection = {"baseline": baseline,
                      "result": corpus.compare(args.artifacts_root, source_baseline),
                      "worktree_sha256": worktree_fingerprint(args.artifacts_root, source_baseline)}
    return {"schema": 1, "type": "skill-eval-run", "case_id": args.case,
            "suite_sha256": digest(args.suite.read_bytes()),
            "prompt_sha256": digest(cases[args.case]["prompt"]),
            "variant": args.variant, "mode": args.mode, "model": args.model,
            "settings": settings, "repetition": args.repetition,
            "execution_kind": args.execution_kind,
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "response": response, "trace": trace, "artifacts": artifacts,
            "skill_root": str(args.skill.resolve()) if args.skill else None,
            "skill_files": skill_files, "protection": protection,
            "boundary": "Hashes bind captured files, not proof of model identity, instruction use or reviewer independence."}


def summarize(suite_path, runs, judgments_path, variant, mode, requested=(), repetitions=1):
    suite, cases = load_suite(suite_path)
    chosen = selected_cases(cases, requested)
    if repetitions < 1:
        raise ValueError("Repetitions must be positive")
    judgments = read_json(judgments_path) if judgments_path else []
    if not isinstance(judgments, list):
        raise ValueError("Judgments must be an array")
    reviews = {}
    for judgment in judgments:
        if not isinstance(judgment, dict) or any(
                not isinstance(judgment.get(key), str) or not judgment[key].strip()
                for key in ("run_sha256", "response_sha256", "reviewer", "rationale")):
            raise ValueError("Judgments need run/response hashes, reviewer and rationale")
        if judgment.get("method") not in {"human", "model", "fixture"} or judgment.get("verdict") not in {"pass", "fail", "unreviewed"}:
            raise ValueError("Invalid judgment method/verdict")
        if judgment["run_sha256"] in reviews:
            raise ValueError("Duplicate judgment for a run; resolve disagreements explicitly")
        reviews[judgment["run_sha256"]] = judgment
    captured, run_hashes, configurations = {}, set(), set()
    for path in runs:
        run_hash = digest(Path(path).read_bytes())
        run = read_json(path)
        if not isinstance(run, dict) or run.get("schema") != 1 or run.get("type") != "skill-eval-run":
            raise ValueError(f"Unsupported run: {path}")
        if run.get("suite_sha256") != digest(Path(suite_path).read_bytes()):
            raise ValueError("Run belongs to a different suite version")
        key, repetition = run.get("case_id"), run.get("repetition")
        if key not in chosen or type(repetition) is not int or not 1 <= repetition <= repetitions:
            raise ValueError("Run outside selected cases/repetitions")
        if run.get("variant") != variant or run.get("mode") != mode:
            raise ValueError("Do not mix variants or trigger/task modes")
        if (key, repetition) in captured:
            raise ValueError("Duplicate case/repetition")
        if run.get("prompt_sha256") != digest(cases[key]["prompt"]):
            raise ValueError("Run prompt differs from suite")
        if run.get("execution_kind") not in {"model", "fixture"}:
            raise ValueError("Run must declare model or fixture execution")
        if not isinstance(run.get("model"), str) or not run["model"].strip() or not isinstance(run.get("settings"), dict):
            raise ValueError("Run must declare model and settings")
        for field in ("artifacts", "skill_files"):
            if not isinstance(run.get(field), list):
                raise ValueError(f"Run needs {field} array")
        for item in [run["response"], run["trace"], *run["artifacts"], *run["skill_files"]]:
            check_evidence(item)
        if bool(run["skill_files"]) != bool(run.get("skill_root")):
            raise ValueError("Skill evidence needs both root and files, or neither")
        skill_signature = sorted((str(Path(item["path"]).relative_to(run["skill_root"])), item["sha256"])
                                 for item in run["skill_files"])
        configurations.add(json.dumps([run["model"], run["settings"], skill_signature], sort_keys=True))
        if run.get("protection") is not None:
            import corpus
            check_evidence(run["protection"]["baseline"])
            previous = run["protection"]["result"]
            if not isinstance(previous, dict) or not isinstance(previous.get("failures"), list):
                raise ValueError("Malformed protection result")
            source_baseline = read_json(run["protection"]["baseline"]["path"])
            current = corpus.compare(previous["root"], source_baseline)
            if current != previous or worktree_fingerprint(previous["root"], source_baseline) != run["protection"].get("worktree_sha256"):
                raise ValueError("Protected worktree changed after capture; collect fresh evidence")
        judgment = reviews.get(run_hash)
        if judgment and judgment["response_sha256"] != run["response"]["sha256"]:
            raise ValueError("Judgment refers to a different response")
        status = judgment["verdict"] if judgment else "unreviewed"
        if run["execution_kind"] == "fixture" or judgment and judgment["method"] == "fixture":
            status = "not_model_run"
        elif run.get("protection") and run["protection"]["result"]["failures"]:
            status = "fail"
        captured[key, repetition] = {"case_id": key, "repetition": repetition,
                                    "status": status, "run_sha256": run_hash,
                                    "judgment": judgment}
        run_hashes.add(run_hash)
    if set(reviews) - run_hashes:
        raise ValueError("Judgments include unknown runs")
    if len(configurations) > 1:
        raise ValueError("Mixed model/settings/skill versions within one variant")
    rows = [captured.get((key, repetition), {"case_id": key, "repetition": repetition, "status": "not_run"})
            for key in chosen for repetition in range(1, repetitions + 1)]
    completed = all(row["status"] in {"pass", "fail"} for row in rows)
    rate = sum(row["status"] == "pass" for row in rows) / len(rows)
    required_failures = [row for row in rows if row["case_id"] in suite["required_case_ids"] and row["status"] != "pass"]
    accepted = completed and not required_failures and rate >= suite["minimum_pass_rate"]
    full_scope = set(chosen) == cases.keys()
    return {"schema": 1, "type": "skill-eval-summary", "variant": variant, "mode": mode,
            "suite_sha256": digest(Path(suite_path).read_bytes()), "selected_cases": chosen,
            "repetitions": repetitions, "full_suite_scope": full_scope,
            "status": ("passed_suite" if full_scope else "passed_selected") if accepted else "failed" if completed else "incomplete",
            "pass_rate": rate, "required_failures": required_failures, "runs": rows,
            "boundary": "Only recorded runs and supplied judgments. Not a learning-effect study or independent authentication of execution."}


def main(argv=None):
    cli = argparse.ArgumentParser(description=__doc__)
    sub = cli.add_subparsers(dest="command", required=True)
    export = sub.add_parser("export")
    capture = sub.add_parser("record")
    summary = sub.add_parser("summarize")
    for command in (export, capture, summary):
        command.add_argument("--suite", type=Path, required=True)
        command.add_argument("--out", type=Path, required=True)
    for command in (export, summary):
        command.add_argument("--case", action="append")
    for command in (capture, summary):
        command.add_argument("--variant", required=True)
        command.add_argument("--mode", choices=["trigger", "task"], default="task")
    capture.add_argument("--case", required=True)
    capture.add_argument("--model", required=True)
    capture.add_argument("--settings", type=Path, required=True)
    capture.add_argument("--response", type=Path, required=True)
    capture.add_argument("--trace", type=Path, required=True)
    capture.add_argument("--repetition", type=int, default=1)
    capture.add_argument("--execution-kind", choices=["model", "fixture"], required=True)
    capture.add_argument("--skill", type=Path)
    capture.add_argument("--artifacts-root", type=Path)
    capture.add_argument("--include", action="append")
    capture.add_argument("--baseline", type=Path)
    summary.add_argument("--runs", nargs="*", type=Path, default=[])
    summary.add_argument("--judgments", type=Path)
    summary.add_argument("--repetitions", type=int, default=1)
    args = cli.parse_args(argv)
    try:
        forbidden = [args.suite]
        if args.command == "export":
            result = export_tasks(args.suite, args.case)
        elif args.command == "record":
            result = capture_run(args)
            forbidden += [args.settings, args.response, args.trace]
            forbidden += [item["path"] for item in result["artifacts"] + result["skill_files"]]
            if args.baseline:
                forbidden.append(args.baseline)
        else:
            result = summarize(args.suite, args.runs, args.judgments, args.variant,
                               args.mode, args.case, args.repetitions)
            forbidden += args.runs + ([args.judgments] if args.judgments else [])
        result["tool_sha256"] = digest(Path(__file__).read_bytes())
        write_json(args.out, result, forbidden=forbidden)
        print(f"Wrote {args.out}: {result.get('status', result['type'])}")
        return int(args.command == "summarize" and result["status"] not in {"passed_suite", "passed_selected"})
    except (ValueError, OSError, KeyError, TypeError, ImportError) as error:
        cli.exit(2, f"error: {error}\n")


if __name__ == "__main__":
    sys.exit(main())
