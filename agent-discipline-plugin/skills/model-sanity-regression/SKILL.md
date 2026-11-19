---
name: model-sanity-regression
description: "When 'the model feels off', after a vendor update, or before relying on a new model: run a 12-item personal regression set (one per failure family — inventory, re-read, narrow read, context, passivity, blast radius, evidence, sycophancy, rules, tool misuse, assumptions, drift), record pass/fail with date and model version, and compare to the dated scoreboard to separate model/infra drift from your own prompt changes. Tooling: `ad.py regress show|record|report`. Scope boundary: fixing an individual failure → the matching skill."
metadata:
  priority: 4
  bashPatterns:
    - '\bad\.py regress\b'
---
# Model sanity regression

Vendors have confirmed infra bugs that degraded output for weeks; users also misattribute their own prompt drift to the model. Only a dated, fixed regression set tells the two apart.

## Procedure
1. `ad.py regress init` (once) → `.agent/regress/set.json`, 12 items with prompt, expected behavior, fail signals. Edit it: add your own recurring cases (e.g. "check project files before download").
2. `ad.py regress show` → run each prompt against the model under test in a **fresh** session with your standard rules/skills loaded.
3. Score strictly: pass = expected behavior and no fail signal; partial = right action, wrong form; fail otherwise. `ad.py regress record F1-inventory pass "claude-opus-4.1 (2026-11-10)" --note "searched project first"`.
4. `ad.py regress report` → scoreboard by model/date.

## Reading the board
- Many items drop on one date, same prompts → model/infra drift. Check the vendor status page and changelog; pin the version if possible.
- One item drops after you edited a rules file → your change. Revert and re-run that item.
- Pass counts flat but "feels worse" → your tasks changed; add a representative item.
