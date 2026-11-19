---
name: test-impact-selector
description: "Map changed files to the tests that cover them, run that subset first, report what was skipped and why, and run the full suite only when shared/config/build code changed or right before a PR. Use whenever tests are run after edits. Tooling: `ad.py test-impact [--base REF]`. Scope boundary: proving completion → `completion-evidence-gate`."
metadata:
  priority: 6
  bashPatterns:
    - '\b(pytest|npm test|pnpm test|yarn test|go test|cargo test|jest|vitest)\b'
---
# Test impact selector

A full suite after every edit is the testing version of re-reading whole files: slow, noisy, and it floods context with passing output.

## Procedure
1. `ad.py test-impact` (uses `git diff --name-only` + untracked files) → `run` list, `full_suite_reason`, `skipped_count`.
2. Run the `run` list with the narrowest invocation (`pytest tests/test_parser.py -q`, `jest path -t name`, `go test ./pkg/...`).
3. Say what you skipped: `Ran 2 of 41 test files (impacted by src/parser.py); full suite deferred to pre-PR.`
4. Full suite when: `full_suite_reason` is set (lockfile, config, shared/core module, CI file), before opening the PR, or the user asks.
5. Failures: read only the failure block (→ `tool-output-trimmer`). Fix, re-run the single test, then the subset.

## Rules
- Never report "tests pass" for tests you did not run; name the subset.
- If no test maps to the change, say so and write one, or state why none is needed.
- A flaky failure is still a failure until you show it passing twice and failing on unrelated input.
