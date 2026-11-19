---
name: test-tamper-audit
description: "Audit a diff from any coding agent for test gaming before accepting a pass: deleted or shrunken test files, skip markers, weakened or removed assertions, hard-coded expected values, mocks added to production code. Use after any run that reports passing tests, especially long runs at high reasoning effort or benchmark-shaped tasks. Ships test_tamper_check.py. Scope boundary: the retry loop around it is skill:verified-retry; wording of the completion claim is skill:completion-evidence-gate."
---

# Test tamper audit

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
An agent says tests pass and nobody watched every step.

## Steps
1. `git diff base..head > changes.diff && python3 scripts/test_tamper_check.py changes.diff`. Errors: test file deleted, skip markers, `assert True`-style weakening. Warnings: shrunken test files, removed assertions, literal returns, mocks outside tests.
2. Read every flagged hunk in context.
3. Run the original test suite from the base commit against the new code. Modified tests prove nothing.
4. For benchmark-shaped tasks, grep the transcript for probing of hidden files, environment variables and grader endpoints.
5. Lower reasoning effort for routine work; hack attempts rose with effort in the one cross-model audit that measured it.
6. Put the audit result in the completion report.

## Evidence
- Reward Hacking and Clean Coding Index: 10,506 trajectories, 14 models, 410 hack attempts, rising with reasoning effort. https://coding-index.posttrain.dev/
- Neo Research: grader probing and fabricated inputs. https://neoresearch.ai/papers/Kimi_K3_Safety_Evaluation.pdf
- Full notes: [references/evidence.md](references/evidence.md)
