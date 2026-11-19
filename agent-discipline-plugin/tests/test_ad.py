"""Tests for agent-discipline. Run: python3 -m pytest tests -q  (or python3 -m unittest discover tests)."""
import os, sys, json, subprocess, tempfile, unittest, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "lib"); AD = os.path.join(LIB, "ad.py")
sys.path.insert(0, LIB)

class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(); self.state = os.path.join(self.tmp, ".agent")
        os.environ["AGENT_STATE_DIR"] = self.state
        self.old = os.getcwd(); os.chdir(self.tmp)
        for m in list(sys.modules):
            if m.startswith("ad_"): del sys.modules[m]
        import ad_core, ad_state, ad_guards, ad_gates, ad_rules, ad_regress
        self.core, self.st, self.gd, self.gt, self.rl, self.rg = ad_core, ad_state, ad_guards, ad_gates, ad_rules, ad_regress
    def tearDown(self):
        os.chdir(self.old); shutil.rmtree(self.tmp, ignore_errors=True)
    def cli(self, *args, stdin=None):
        return subprocess.run([sys.executable, AD, *args], input=stdin, capture_output=True, text=True, env=dict(os.environ))
    def hook(self, name, payload):
        return self.cli("hook", name, stdin=json.dumps(payload))
    def write(self, name, text):
        p = os.path.join(self.tmp, name); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w").write(text); return p

class TestManifestAndReadCache(Base):
    def test_record_check_unchanged_and_changed(self):
        p = self.write("a.txt", "hello\n" * 100)
        self.st.manifest_record(p, [[1, 20]], "greeting file")
        self.assertIn("UNCHANGED", self.st.manifest_check(p)); self.assertIn("greeting file", self.st.manifest_check(p))
        open(p, "a").write("x"); self.assertIn("CHANGED", self.st.manifest_check(p))
        self.assertIn("NOT IN MANIFEST", self.st.manifest_check("/nope"))
    def test_lookup_by_basename_matches_url_filename(self):
        p = self.write("genome.vcf", "data"); self.st.manifest_record(p)
        k, e = self.st.manifest_lookup("genome.vcf"); self.assertEqual(k, p)
    def test_read_cache_hook_adds_context_never_blocks(self):
        p = self.write("b.py", "x=1\n"); self.st.manifest_record(p, summary="sets x")
        r = self.hook("read-cache", {"tool_name": "Read", "tool_input": {"file_path": p}})
        self.assertEqual(r.returncode, 0); self.assertIn("UNCHANGED", r.stdout); self.assertIn("sets x", r.stdout)
        r = self.hook("read-cache", {"tool_name": "Read", "tool_input": {"file_path": "/missing"}}); self.assertEqual(r.returncode, 0)
    def test_record_read_hook_and_reinject(self):
        p = self.write("c.md", "# c\n")
        self.hook("record-read", {"tool_name": "Read", "tool_input": {"file_path": p, "offset": 1, "limit": 5}})
        m = self.core.load_json("manifest.json", {}); self.assertIn(p, m); self.assertEqual(m[p]["ranges"], [[1, 6]])
        self.st.ledger_add("GRANT", "edit anything under src/"); self.st.checkpoint_write("Goal: ship. Open: tests.")
        r = self.hook("reinject", {"hook_event_name": "SessionStart"})
        for s in ("Autonomy ledger", "edit anything under src/", "CHECKPOINT", "Read manifest", "c.md"): self.assertIn(s, r.stdout)
        self.assertLess(len(self.st.reinject()), 6001)
    def test_reinject_empty_state_is_silent(self):
        r = self.hook("reinject", {}); self.assertEqual(r.stdout, "")

class TestLedger(Base):
    def test_grant_forbid_lookup_latest_wins(self):
        self.st.ledger_add("GRANT", "delete files under build/ output")
        self.assertIn("ALREADY GRANTED", self.st.ledger_check("delete the build output files"))
        self.st.ledger_add("FORBID", "delete files under build/ output")
        self.assertIn("FORBIDDEN", self.st.ledger_check("delete the build output files"))
        self.assertIn("NO LEDGER ENTRY", self.st.ledger_check("deploy to mars"))
    def test_bad_kind_rejected(self):
        with self.assertRaises(SystemExit): self.st.ledger_add("MAYBE", "x")

class TestFetchGuard(Base):
    def test_nebula_redownload_blocked_when_in_manifest(self):
        p = self.write("nebula_genome.cram", "ACGT"); self.st.manifest_record(p, summary="whole-genome CRAM")
        r = self.gd.fetch_guard_decide("curl -L -o nebula_genome.cram https://files.nebula.org/u/123/nebula_genome.cram")
        self.assertIsNotNone(r); self.assertIn("already available", r); self.assertIn("whole-genome CRAM", r)
    def test_large_type_without_inventory_blocked_then_grant_allows(self):
        self.assertIn("no inventory", self.gd.fetch_guard_decide("wget https://example.org/x.vcf.gz"))
        self.st.ledger_add("GRANT", "download x.vcf.gz — not in project knowledge (checked)")
        self.assertIsNone(self.gd.fetch_guard_decide("wget https://example.org/x.vcf.gz"))
    def test_size_hint_over_limit_blocked(self):
        self.assertIn("exceeds", self.gd.fetch_guard_decide("curl https://a.b/c.bin  # size: 2 GB"))
    def test_non_fetch_and_small_fetch_allowed(self):
        self.assertIsNone(self.gd.fetch_guard_decide("ls -la")); self.assertIsNone(self.gd.fetch_guard_decide("curl https://api.example.com/health"))
    def test_hook_contract_deny_json_and_exit2(self):
        p = self.write("f.zip", "z"); self.st.manifest_record(p)
        r = self.hook("fetch-guard", {"tool_name": "Bash", "tool_input": {"command": "wget https://h/f.zip"}})
        self.assertEqual(r.returncode, 2); j = json.loads(r.stdout)
        self.assertEqual(j["hookSpecificOutput"]["permissionDecision"], "deny"); self.assertTrue(r.stderr)

class TestScopeFence(Base):
    def D(self, cmd, tool="Bash", **kw):
        inp = {"tool_name": tool, "tool_input": {"command": cmd} if tool == "Bash" else {"file_path": cmd, "content": "x"}}
        return self.gd.scope_fence_decide(inp, **kw)
    def test_destructive_patterns(self):
        for c in ("rm -rf ~/x", "rm -fr /tmp/a", "git push --force origin main", "git reset --hard", "DROP TABLE users;",
                  "terraform destroy", "psql $PRODUCTION_DATABASE_URL -c 'select 1'", "npm publish", "git push origin main"):
            self.assertIsNotNone(self.D(c), c)
        for c in ("git push --force-with-lease origin feat", "rm file.txt", "git push origin feature/x", "ls /"):
            self.assertIsNone(self.D(c), c)
    def test_grant_unlocks_specific_destructive(self):
        self.st.ledger_add("GRANT", "recursive force delete: rm -rf build/")
        self.assertIsNone(self.D("rm -rf build/")); self.assertIsNotNone(self.D("rm -rf src/"))
    def test_write_outside_roots_blocked_tmp_allowed(self):
        self.gd.scope_set([self.tmp])
        self.assertIsNone(self.D(os.path.join(self.tmp, "ok.txt"), tool="Write"))
        self.assertIn("outside declared roots", self.D("/etc/passwd", tool="Write"))
        self.assertIn("outside declared roots", self.D("../../escape.txt", tool="Write"))
        self.assertIsNone(self.D("/tmp/scratch.txt", tool="Write"))
        self.assertIn("outside", self.D("echo hi > ~/secret.txt"))
    def test_allow_regex(self):
        self.gd.scope_set([self.tmp], ["^/opt/shared/"]); self.assertIsNone(self.D("/opt/shared/a.txt", tool="Write"))

class TestValidator(Base):
    def test_repeated_identical_failure_blocked(self):
        for _ in range(2): self.core.log_tool({"tool_name": "Bash", "tool_input": {"command": "make build"}, "tool_response": "error\nexit code: 2"})
        reason, _ = self.gd.validate_call_decide({"tool_name": "Bash", "tool_input": {"command": "make build"}})
        self.assertIn("failed 2x", reason)
        reason, _ = self.gd.validate_call_decide({"tool_name": "Bash", "tool_input": {"command": "make build VERBOSE=1"}}); self.assertIsNone(reason)
    def test_empty_input_context(self):
        _, ctx = self.gd.validate_call_decide({"tool_name": "Bash", "tool_input": {"command": ""}}); self.assertIn("empty", ctx)

class TestCompletionGate(Base):
    GOOD = "Done.\nAcceptance: tests green\nCommand: pytest tests -q\nOutput: 12 passed in 0.4s\nDiff: lib/a.py\nNot verified: Windows\n"
    def test_claim_without_evidence_blocked(self):
        self.assertIn("evidence block", self.gt.completion_gate_decide("Fixed it, all tests pass!"))
    def test_no_claim_passes(self):
        self.assertIsNone(self.gt.completion_gate_decide("Still investigating the parser."))
    def test_evidence_with_logged_command_passes_unlogged_blocked(self):
        self.assertIn("tool log", self.gt.completion_gate_decide(self.GOOD) or "") if self.gt.commands_in_log() else None
        self.core.log_tool({"tool_name": "Bash", "tool_input": {"command": "python3 -m pytest tests -q"}, "tool_response": "12 passed"})
        self.assertIsNone(self.gt.completion_gate_decide(self.GOOD))
        self.assertIn("tool log", self.gt.completion_gate_decide(self.GOOD.replace("pytest tests -q", "npm test")))
    def test_paraphrased_output_blocked(self):
        self.assertIn("quote", self.gt.completion_gate_decide(self.GOOD.replace("12 passed in 0.4s", "passed"), strict=False))
    def test_stop_hook_reads_transcript_and_respects_stop_hook_active(self):
        tp = self.write("t.jsonl", json.dumps({"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": "All done, it works now."}]}}) + "\n")
        r = self.hook("completion-gate", {"transcript_path": tp}); self.assertEqual(json.loads(r.stdout)["decision"], "block")
        r = self.hook("completion-gate", {"transcript_path": tp, "stop_hook_active": True}); self.assertEqual(r.stdout, "")

class TestTrimmer(Base):
    def test_passthrough_and_kinds(self):
        self.assertEqual(self.gt.trim_output("short")[1], "passthrough")
        grep = "\n".join(f"src/f{i}.py:{i}: foo bar baz {'x'*80}" for i in range(200)); self.assertEqual(self.gt.trim_output(grep)[1], "grep")
        tests = "\n".join([f"tests/test_module_{i}.py::test_case_{i} PASSED" for i in range(300)] + ["FAILED test_x - AssertionError: boom", "1 failed, 300 passed"])
        t, k = self.gt.trim_output(tests); self.assertEqual(k, "test-failures"); self.assertIn("AssertionError", t); self.assertNotIn("test_5 PASSED", t)
        js = json.dumps({"items": [{"id": i, "name": "n" * 50} for i in range(300)]}); self.assertEqual(self.gt.trim_output(js)[1], "json")
        log = "\n".join(f"line {i} {'y'*60}" for i in range(500)); t, k = self.gt.trim_output(log); self.assertEqual(k, "head-tail"); self.assertIn("omitted", t)
    def test_hook_stores_full_output(self):
        big = "z" * 10000
        r = self.hook("log-trim", {"tool_name": "Bash", "tool_input": {"command": "cat big"}, "tool_response": big})
        j = json.loads(r.stdout); ctx = j["hookSpecificOutput"]["additionalContext"]; self.assertIn("saved to", ctx)
        import re as _re; path = _re.search(r"saved to (\S+?\.txt)", ctx).group(1); self.assertEqual(open(path).read(), big)
        self.assertEqual(len(self.gt.commands_in_log()), 1)

class TestProvenance(Base):
    def test_add_show_audit(self):
        self.gt.provenance_add("Findings", "report.md", "quote", "established")
        self.assertIn("Findings", self.gt.provenance_show())
        d = self.write("deliv.md", "# Findings\ntext\n# Methods\n"); self.assertIn("Methods", self.gt.provenance_audit(d)); self.assertNotIn("Findings", self.gt.provenance_audit(d).split(":")[-1])
        with self.assertRaises(SystemExit): self.gt.provenance_add("s", "x", confidence="sure")

class TestRules(Base):
    def test_lint_compile_rewrite(self):
        p = self.write("CLAUDE.md", "# Rules\n- Never run rm -rf on any directory.\n- Don't force-push.\n- Be careful with migrations.\n- Never use tabs.\n" + "- filler\n" * 160)
        r = self.rl.lint_rules(p)
        self.assertTrue(any(">150" in f for f in r["findings"])); self.assertEqual({h["label"] for h in r["hooks"]}, {"recursive delete", "force push"})
        self.assertTrue(any("vague" in f for f in r["findings"])); self.assertTrue(any("no hook equivalent" in f for f in r["findings"]))
        self.assertTrue(any(w["positive"].startswith("Before any step") for w in r["rewrites"]))
        hooks = self.rl.compile_hooks([r]); cmd = hooks["hooks"]["PreToolUse"][0]["hooks"][0]["command"]; self.assertIn("deny-regex", cmd)
        out = self.cli("deny-regex", r"git\s+push\s+.*--force", stdin=json.dumps({"tool_name": "Bash", "tool_input": {"command": "git push --force"}}))
        self.assertEqual(out.returncode, 2)
    def test_find_rule_files(self):
        self.write("AGENTS.md", "x"); self.write("sub/.cursorrules", "y"); self.assertEqual(len(self.rl.find_rule_files(self.tmp)), 2)

class TestImpactAndRegress(Base):
    def test_test_impact_mapping(self):
        self.write("src/parser.py", "def p(): pass"); self.write("tests/test_parser.py", "from src.parser import p"); self.write("tests/test_other.py", "x")
        res = self.rl.test_impact(["src/parser.py"], self.tmp)
        self.assertEqual(res["run"], ["tests/test_parser.py"]); self.assertIsNone(res["full_suite_reason"]); self.assertEqual(res["skipped_count"], 1)
        self.assertIn("pyproject", self.rl.test_impact(["pyproject.toml"], self.tmp)["full_suite_reason"])
    def test_regress_roundtrip(self):
        self.rg.regress_init(); self.assertIn("F1-inventory", self.rg.regress_show())
        self.rg.regress_record("F1-inventory", "pass", "claude-x"); self.rg.regress_record("F7-evidence", "fail", "claude-x", "said done")
        rep = self.rg.regress_report(); self.assertIn("claude-x: 1/12", rep); self.assertIn("fail", rep)
        with self.assertRaises(SystemExit): self.rg.regress_record("F1-inventory", "meh", "m")

class TestFailOpen(Base):
    def test_garbage_stdin_never_blocks(self):
        for h in ("fetch-guard", "scope-fence", "validate-call", "read-cache", "record-read", "log-trim", "completion-gate", "reinject"):
            r = self.cli("hook", h, stdin="not json{{"); self.assertEqual(r.returncode, 0, h)
        self.assertEqual(self.cli("hook", "nope", stdin="{}").returncode, 0)

if __name__ == "__main__":
    unittest.main()
