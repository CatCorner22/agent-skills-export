#!/usr/bin/env python3
"""agent-discipline CLI + hook entrypoint. Standard library only.

  ad.py hook <name>                 run as a hook; reads host JSON on stdin. names: fetch-guard scope-fence validate-call
                                    read-cache record-read log-trim completion-gate reinject
  ad.py manifest record PATH [--range A-B] [--summary TEXT] | check PATH | show
  ad.py ledger add GRANT|FORBID|STOP|ACCEPT|SCOPE|NOTE TEXT | check "action text" | show
  ad.py checkpoint write TEXT | show          ad.py reinject [--full]
  ad.py scope set ROOT [ROOT…] [--allow REGEX…] | show
  ad.py fetch-check "COMMAND"                 ad.py fence-check "COMMAND"
  ad.py gate "LAST MESSAGE TEXT" [--lenient]  ad.py trim FILE [--tool NAME]
  ad.py provenance add SECTION SOURCE [--quote Q] [--confidence C] | show [SECTION] | audit DELIVERABLE.md
  ad.py rules lint [ROOT] | compile [ROOT] | rewrite FILE
  ad.py test-impact [--base REF] [--root DIR]
  ad.py regress show | record ID pass|fail|partial MODEL [--note N] | report | init [--force]
  ad.py deny-regex PATTERN…                   (hook form; used by compiled rule hooks)
"""
import sys, os, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ad_core, ad_state, ad_guards, ad_gates, ad_rules, ad_regress

HOOKS = {
    "fetch-guard": ad_guards.hook_fetch_guard, "scope-fence": ad_guards.hook_scope_fence, "validate-call": ad_guards.hook_validate_call,
    "read-cache": ad_state.hook_read_cache, "record-read": ad_state.hook_record_read, "reinject": ad_state.hook_reinject,
    "log-trim": ad_gates.hook_log_and_trim, "completion-gate": ad_gates.hook_completion_gate,
}

def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help"): print(__doc__); return 0
    cmd, rest = argv[0], argv[1:]
    p = argparse.ArgumentParser(prog=f"ad.py {cmd}", add_help=False)
    def out(x):
        if x is not None: print(x)
        return 0
    if cmd == "hook":
        fn = HOOKS.get(rest[0] if rest else "")
        if not fn: sys.stderr.write(f"unknown hook; choose from {sorted(HOOKS)}\n"); return 0  # fail-open
        try: fn()
        except SystemExit: raise
        except Exception as ex: sys.stderr.write(f"agent-discipline hook error (fail-open): {ex}\n"); return 0
        return 0
    if cmd == "deny-regex": ad_rules.deny_regex_hook(rest); return 0
    if cmd == "manifest":
        sub = rest[0]
        if sub == "record":
            p.add_argument("path"); p.add_argument("--range", action="append", default=[]); p.add_argument("--summary", default=None)
            a = p.parse_args(rest[1:]); rngs = [[int(x) for x in r.split("-")] for r in a.range]
            k, e = ad_state.manifest_record(a.path, rngs, a.summary); return out(f"recorded {k} ({ad_core.human_size(e.get('size', 0))})")
        if sub == "check": return out(ad_state.manifest_check(rest[1]))
        if sub == "show": return out(ad_state.manifest_summary() or "(manifest empty)")
    if cmd == "ledger":
        sub = rest[0]
        if sub == "add": return out(ad_state.ledger_add(rest[1], " ".join(rest[2:])))
        if sub == "check": return out(ad_state.ledger_check(" ".join(rest[1:])))
        if sub == "show": return out(ad_state.ledger_show() or "(ledger empty)")
    if cmd == "checkpoint":
        if rest[0] == "write": return out(ad_state.checkpoint_write(" ".join(rest[1:]) if len(rest) > 1 else sys.stdin.read()))
        if rest[0] == "show": return out(ad_core.read_text("CHECKPOINT.md") or "(no checkpoint)")
    if cmd == "reinject": return out(ad_state.reinject(10**9 if "--full" in rest else 6000) or "(no state yet)")
    if cmd == "scope":
        if rest[0] == "set":
            p.add_argument("roots", nargs="+"); p.add_argument("--allow", nargs="*", default=None); a = p.parse_args(rest[1:])
            return out(ad_guards.scope_set([os.path.abspath(os.path.expanduser(r)) for r in a.roots], a.allow))
        if rest[0] == "show": return out(json.dumps(ad_guards.declared_roots()[1] or {"roots": [os.getcwd()], "note": "default: cwd"}, indent=1))
    if cmd == "fetch-check": return out(ad_guards.fetch_guard_decide(" ".join(rest)) or "ALLOW")
    if cmd == "fence-check": return out(ad_guards.scope_fence_decide({"tool_name": "Bash", "tool_input": {"command": " ".join(rest)}}) or "ALLOW")
    if cmd == "gate": return out(ad_gates.completion_gate_decide(" ".join(r for r in rest if r != "--lenient"), strict="--lenient" not in rest) or "PASS")
    if cmd == "trim":
        p.add_argument("file"); p.add_argument("--tool", default=""); a = p.parse_args(rest)
        t, kind = ad_gates.trim_output(open(a.file, encoding="utf-8", errors="replace").read(), a.tool); return out(f"[{kind}]\n{t}")
    if cmd == "provenance":
        sub = rest[0]
        if sub == "add":
            p.add_argument("section"); p.add_argument("source"); p.add_argument("--quote", default=""); p.add_argument("--confidence", default="probable")
            a = p.parse_args(rest[1:]); return out(ad_gates.provenance_add(a.section, a.source, a.quote, a.confidence))
        if sub == "show": return out(ad_gates.provenance_show(rest[1] if len(rest) > 1 else None))
        if sub == "audit": return out(ad_gates.provenance_audit(rest[1]))
    if cmd == "rules":
        sub = rest[0]; root = rest[1] if len(rest) > 1 else "."
        if sub == "rewrite":
            lines = open(rest[1], encoding="utf-8").read().splitlines()
            return out("\n".join(f"L{i}: {ad_rules.positive_rewrite(l)}" for i, l in enumerate(lines, 1) if ad_rules.positive_rewrite(l)) or "(no negative rules)")
        results = [ad_rules.lint_rules(f) for f in ad_rules.find_rule_files(root)]
        if sub == "lint":
            if not results: return out("(no rules files found)")
            txt = []
            for r in results:
                txt.append(f"## {r['file']} ({r['lines']} lines) — {len(r['findings'])} findings, {len(r['hooks'])} hookable rules")
                txt += [f"- {f}" for f in r["findings"]]
                txt += [f"- HOOKABLE L{h['line']} [{h['label']}]: {h['rule']}" for h in r["hooks"]]
                txt += [f"- REWRITE L{w['line']}: {w['positive']}" for w in r["rewrites"]]
            return out("\n".join(txt))
        if sub == "compile": return out(json.dumps(ad_rules.compile_hooks(results), indent=1))
    if cmd == "test-impact":
        p.add_argument("--base", default=None); p.add_argument("--root", default="."); a = p.parse_args(rest)
        res = ad_rules.test_impact(ad_rules.changed_files(a.base), a.root)
        res["advice"] = ("run FULL suite: " + res["full_suite_reason"]) if res["full_suite_reason"] else ("run impacted subset first; full suite before PR" if res["run"] else "no mapped tests — name the test you will add")
        return out(json.dumps(res, indent=1))
    if cmd == "regress":
        sub = rest[0]
        if sub == "init": return out(ad_regress.regress_init("--force" in rest))
        if sub == "show": return out(ad_regress.regress_show())
        if sub == "record":
            p.add_argument("id"); p.add_argument("result"); p.add_argument("model"); p.add_argument("--note", default=""); a = p.parse_args(rest[1:])
            return out(ad_regress.regress_record(a.id, a.result, a.model, a.note))
        if sub == "report": return out(ad_regress.regress_report())
    print(__doc__); return 1

if __name__ == "__main__":
    sys.exit(main())
