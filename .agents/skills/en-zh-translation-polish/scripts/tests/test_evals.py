from argparse import Namespace
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import evals
from io_utils import digest


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.suite = self.put("suite.json", {
            "test_cases": [{"id": key, "prompt": f"Translate {key}.", "expected_behavior": "SECRET JUDGING RULE"}
                           for key in ("critical", "normal")],
            "required_case_ids": ["critical"], "minimum_pass_rate": 0.5})
        self.settings = self.put("settings.json", {"reasoning": "unknown"})

    def put(self, name, data):
        path = self.root / name
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def run_record(self, case="critical", repetition=1, kind="model", variant="candidate"):
        stem = f"{case}-{repetition}-{kind}-{variant}"
        response = self.root / f"{stem}.txt"
        response.write_text("Captured response", encoding="utf-8")
        trace = self.root / f"{stem}.trace"
        trace.write_text("Synthetic unit-test evidence, not an actual model run.", encoding="utf-8")
        args = Namespace(suite=self.suite, case=case, repetition=repetition, model="unit-test-model",
                         variant=variant, settings=self.settings, response=response, trace=trace,
                         artifacts_root=None, include=None, baseline=None, skill=None, mode="task",
                         execution_kind=kind, out=self.root / f"{stem}.json")
        return self.put(args.out.name, evals.capture_run(args))

    def review(self, run, verdict="pass", method="human"):
        data = evals.read_json(run)
        return {"run_sha256": digest(run.read_bytes()), "response_sha256": data["response"]["sha256"],
                "reviewer": "synthetic-test-reviewer", "method": method, "verdict": verdict,
                "rationale": "Unit test of report mechanics only."}

    def summary(self, runs, reviews=None, cases=(), repetitions=1):
        judgments = self.put("judgments.json", reviews) if reviews is not None else None
        return evals.summarize(self.suite, runs, judgments, "candidate", "task", cases, repetitions)

    def test_export_does_not_leak_judging_rules_or_gates(self):
        exported = evals.export_tasks(self.suite, ["critical"])
        self.assertEqual(exported["tasks"], [{"id": "critical", "prompt": "Translate critical."}])
        self.assertNotIn("SECRET", json.dumps(exported))
        self.assertNotIn("required_case_ids", exported)

    def test_invalid_suites_and_selections(self):
        for change in [{"required_case_ids": ["missing"]}, {"minimum_pass_rate": True},
                       {"required_case_ids": ["critical", "critical"]}, {"test_cases": []}]:
            broken = {**evals.read_json(self.suite), **change}
            with self.subTest(change=change), self.assertRaises(ValueError):
                evals.load_suite(self.put("broken.json", broken))
        with self.assertRaises(ValueError):
            evals.export_tasks(self.suite, ["unknown"])

    def test_no_execution_is_incomplete(self):
        report = self.summary([])
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual([row["status"] for row in report["runs"]], ["not_run", "not_run"])
        self.assertEqual(report["pass_rate"], 0)

    def test_execution_without_judgment_is_incomplete(self):
        report = self.summary([self.run_record()], cases=["critical"])
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(report["runs"][0]["status"], "unreviewed")

    def test_selected_pass_is_not_suite_pass(self):
        run = self.run_record()
        report = self.summary([run], [self.review(run)], ["critical"])
        self.assertEqual(report["status"], "passed_selected")
        self.assertFalse(report["full_suite_scope"])
        full = self.summary([run], [self.review(run)])
        self.assertEqual(full["status"], "incomplete")
        self.assertEqual(full["pass_rate"], 0.5)

    def test_full_suite_and_required_failure(self):
        runs = [self.run_record(key) for key in ("critical", "normal")]
        self.assertEqual(self.summary(runs, [self.review(run) for run in runs])["status"], "passed_suite")
        failed = self.summary(runs, [self.review(runs[0], "fail"), self.review(runs[1])])
        self.assertEqual(failed["pass_rate"], 0.5)
        self.assertEqual(failed["status"], "failed")
        self.assertEqual(failed["required_failures"][0]["case_id"], "critical")

    def test_fixture_execution_and_judging_never_count_as_model_pass(self):
        run = self.run_record(kind="fixture")
        self.assertEqual(self.summary([run], [self.review(run)], ["critical"])["status"], "incomplete")
        run = self.run_record()
        report = self.summary([run], [self.review(run, method="fixture")], ["critical"])
        self.assertEqual(report["runs"][0]["status"], "not_model_run")

    def test_duplicate_repetitions_are_rejected_and_missing_repeats_not_ignored(self):
        run = self.run_record()
        with self.assertRaisesRegex(ValueError, "Duplicate case"):
            self.summary([run, run], [self.review(run)], ["critical"])
        report = self.summary([run], [self.review(run)], ["critical"], 2)
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(report["pass_rate"], 0.5)

    def test_judgment_bound_to_exact_run_and_response(self):
        run = self.run_record()
        judgment = self.review(run)
        for key in ("run_sha256", "response_sha256"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.summary([run], [{**judgment, key: "wrong"}], ["critical"])
        with self.assertRaises(ValueError):
            self.summary([run], [judgment, judgment], ["critical"])

    def test_stale_response_trace_and_artifacts_rejected(self):
        for field in ("response", "trace", "artifacts"):
            with self.subTest(field=field):
                run = self.run_record()
                data = evals.read_json(run)
                if field == "artifacts":
                    artifact = self.put("artifact.json", {"original": True})
                    data[field] = [evals.evidence_file(artifact)]
                    run = self.put(run.name, data)
                    path = artifact
                else:
                    path = Path(data[field]["path"])
                path.write_text("changed", encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Evidence changed"):
                    self.summary([run], [self.review(run)], ["critical"])

    def test_mixed_suite_variant_mode_configuration_rejected(self):
        run = self.run_record()
        original = evals.read_json(run)
        for key, value in [("suite_sha256", "wrong"), ("variant", "old"), ("mode", "trigger"),
                           ("prompt_sha256", "wrong"), ("repetition", True)]:
            altered = self.put("altered.json", {**original, key: value})
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.summary([altered], [self.review(altered)], ["critical"])
        other = self.run_record("normal")
        data = evals.read_json(other)
        data["model"] = "different-model"
        other = self.put(other.name, data)
        with self.assertRaisesRegex(ValueError, "Mixed model"):
            self.summary([run, other], [self.review(run), self.review(other)])

    def test_protection_failure_overrides_pass_judgment(self):
        import corpus
        run = self.run_record()
        data = evals.read_json(run)
        source = self.root / "source.md"
        source.write_text("Original English.", encoding="utf-8")
        before = corpus.snapshot(self.root, ["*.md"], [])
        baseline = self.put("baseline.json", before)
        source.write_text("Changed English.", encoding="utf-8")
        data["protection"] = {"baseline": evals.evidence_file(baseline),
                              "result": corpus.compare(self.root, before),
                              "worktree_sha256": evals.worktree_fingerprint(self.root, before)}
        run = self.put(run.name, data)
        report = self.summary([run], [self.review(run)], ["critical"])
        self.assertEqual(report["status"], "failed")
        source.write_text("Changed again.", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "worktree changed"):
            self.summary([run], [self.review(run)], ["critical"])

    def test_capture_real_artifact_scope_and_skill_snapshot(self):
        import corpus
        work = self.root / "work"
        work.mkdir()
        source = work / "source.md"
        source.write_text("English.\n\n中文。", encoding="utf-8")
        baseline = self.put("baseline.json", corpus.snapshot(work, ["*.md"], []))
        skill = self.root / "frozen-skill"
        skill.mkdir()
        (skill / "SKILL.md").write_text("Frozen instructions.", encoding="utf-8")
        response = self.root / "response.txt"
        response.write_text("Response.", encoding="utf-8")
        trace = self.root / "trace.txt"
        trace.write_text("Synthetic unit-test trace.", encoding="utf-8")
        args = Namespace(suite=self.suite, case="critical", repetition=1, model="unit-test-model",
                         variant="candidate", settings=self.settings, response=response, trace=trace,
                         artifacts_root=work, include=["*.md"], baseline=baseline, skill=skill,
                         mode="task", execution_kind="model", out=self.root / "captured.json")
        data = evals.capture_run(args)
        run = self.put(args.out.name, data)
        self.assertEqual(len(data["artifacts"]), 1)
        self.assertEqual(data["protection"]["result"]["failures"], [])
        self.assertEqual(self.summary([run], [self.review(run)], ["critical"])["status"], "passed_selected")
        (skill / "SKILL.md").write_text("Changed instructions.", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Evidence changed"):
            self.summary([run], [self.review(run)], ["critical"])
        args.out = work / "not-allowed.json"
        with self.assertRaisesRegex(ValueError, "outside"):
            evals.capture_run(args)
        args.out = self.root / "captured2.json"
        args.include = None
        with self.assertRaisesRegex(ValueError, "explicit"):
            evals.capture_run(args)

    def test_cli_reports_incomplete_and_refuses_overwrite(self):
        script = Path(evals.__file__)
        output = self.root / "summary.json"
        command = [sys.executable, str(script), "summarize", "--suite", str(self.suite),
                   "--variant", "candidate", "--out", str(output)]
        result = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(result.returncode, 1, result.stderr)
        before = output.read_bytes()
        result = subprocess.run(command, text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(output.read_bytes(), before)

    def test_bundled_suite_gates_and_new_cases_valid(self):
        suite_path = Path(evals.__file__).resolve().parent.parent / "test-prompts.json"
        suite, cases = evals.load_suite(suite_path)
        self.assertEqual(len(cases), 43)
        self.assertTrue({"edge-19", *[f"edge-{index}" for index in range(24, 35)]}
                        <= set(suite["required_case_ids"]))
        self.assertTrue(all(case["id"] in suite["required_case_ids"] for case in cases.values()
                            if case["type"] == "should_not_trigger"))


if __name__ == "__main__":
    unittest.main()
