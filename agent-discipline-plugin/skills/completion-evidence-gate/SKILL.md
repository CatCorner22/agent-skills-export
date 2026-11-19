---
name: completion-evidence-gate
description: "No 'done / fixed / passes / implemented' without an evidence block: Acceptance → Command → quoted Output → Diff → Not verified. Use before any completion claim, PR description, or status report; enforced by the Stop hook (`ad.py hook completion-gate`), which also checks the cited command actually ran this session. Scope boundary: evidence for factual claims → `claim-evidence-pairing`; which tests to run → `test-impact-selector`."
metadata:
  priority: 9
---
# Completion evidence gate

Agents fabricate success: "all tests pass" with no test run, "fixed" with no reproduction. The gate makes the claim structurally impossible without the evidence.

## The block (exact labels; the hook looks for them)
```
Acceptance: what counts as done (from the ledger ACCEPT line or the user's words)
Command: python3 -m pytest tests -q
Output: "47 passed in 3.2s"          ← quoted, verbatim, numbers included
Diff: lib/ad_guards.py (+31 −4), tests/test_ad.py (+18)
Not verified: Windows paths; behavior under concurrent writes
```
Partial is fine — say so: `Status: partial — 2 of 3 acceptance criteria met`.

## Rules
- If you did not run it, you may not say it passes. Run it, or write "not run".
- `Output:` is a quote, never "passed/ok/works". Include the number (tests, exit code, response code, row count).
- The command in `Command:` must appear in this session's tool log (`.agent/toollog.jsonl`); the Stop hook sends you back otherwise.
- A read-after-write check counts as evidence (`ls -la out/`, `git status --short`, `curl -s -o /dev/null -w '%{http_code}'`).
- "Should work", "this will fix", "everything works now" are banned phrases in a completion message.
