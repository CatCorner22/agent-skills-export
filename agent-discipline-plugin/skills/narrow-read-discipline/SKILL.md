---
name: narrow-read-discipline
description: "Read the smallest slice that answers the question: grep/outline first, ranges with ±15 lines, no whole-file cat over 400 lines without a stated reason, impacted tests before the full suite. Use when opening a file over 200 lines, running tests after edits, reading logs, or paging through large tool output. Pairs with `read-manifest` (what was read) and `test-impact-selector` (which tests)."
metadata:
  priority: 7
  bashPatterns:
    - '\bcat\s+\S+\.(py|ts|js|tsx|jsx|go|rs|java|md|json|log)\b'
    - '\b(pytest|npm test|yarn test|go test|cargo test)\b'
---
# Narrow-read discipline

Tool output is ~90% of an agent's context in long sessions. Every whole-file read evicts something you needed.

## Rules
1. **Locate, then read.** `grep -n`, `rg`, LSP/outline, `git grep`, or `ad.py manifest check` first. Then read `[match−15, match+15]`.
2. **Whole-file reads need a reason** stated in one clause ("reading all 180 lines: the config is interdependent"). Over 400 lines: outline + ranges only.
3. **Logs:** tail, grep for `ERROR|FAIL|Traceback`, or let `tool-output-trimmer` store the full text and hand you failures only.
4. **Tests:** `ad.py test-impact` → run the impacted subset first; full suite only when shared/config code changed or right before the PR. Say which tests you skipped.
5. **Large outputs:** request `--json`/`--quiet`/`head`; never paste a 2,000-line result into the conversation to find one line.
6. **Repeat reads:** second time you open a file, you owe a manifest entry with the summary that would have saved the read.

## Reading budget per task (default)
≤ 3 whole-file reads, ≤ 15 ranged reads, 1 full test run. Exceeding it is fine — say so and why.
