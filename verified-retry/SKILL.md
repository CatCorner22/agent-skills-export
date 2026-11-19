---
name: verified-retry
description: "Run model work as generate, check with an external verifier the model cannot edit, then retry with the failure text, within a budget, so pass@k becomes reliable output on any model; review each passing diff for test gaming before accepting. Use when a model writes code, fixes bugs, fills spreadsheets, transforms data or runs agent tasks that a test, script or rubric can judge. Ships a retry-log template. Scope boundary: the diff audit itself is skill:test-tamper-audit; proof of completion wording is skill:completion-evidence-gate."
---

# Verified retry

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
Work a test, validator or rubric can judge, on any model. Every model's pass@2 and pass@4 are well above its pass@1; a checker converts that into reliable output.

## Steps
1. Write the checker first (tests, validation script, or a rubric with pass/fail lines) and keep it outside the agent's write scope. Hide expected outputs, grader endpoints and keys from the sandbox.
2. Set the budget in `templates/retry-log.md`: tries (2-4), minutes, cost.
3. Run try 1. Run the checker yourself and paste its output into the log. Do not accept the model's own "all tests pass".
4. On failure, start try 2 from a fresh or compacted context with the checker output and a two-line summary. Do not replay the failed transcript.
5. Stop when the checker passes or the budget ends. The same failure class twice means the spec or checker is wrong; fix that instead of retrying.
6. Before accepting a pass, audit the diff (skill:test-tamper-audit or by hand): deleted, skipped or weakened tests, hard-coded expected values, mocks in production code, files outside scope.
7. Report tries used, the quoted checker result, cost, and what the checker does not cover.

## Evidence
- Together AI DeepSWE, same harness: pass@1 69.9 vs 68.5 became pass@2 80.2 vs 82.0 and pass@4 88.5 vs 89.4 for two frontier models; retries with verification matter more than the first-shot gap. Secondhand via https://www.morphllm.com/kimi-k3-vs-claude
- Reward Hacking and Clean Coding Index: 410 hack attempts across 14 models, rising with reasoning effort. https://coding-index.posttrain.dev/
- Neo Research: grader-seeking and fabricated inputs to pass hidden checks. https://neoresearch.ai/papers/Kimi_K3_Safety_Evaluation.pdf
- Full notes: [references/evidence.md](references/evidence.md)
