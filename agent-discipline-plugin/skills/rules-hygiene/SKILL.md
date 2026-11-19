---
name: rules-hygiene
description: "Keep instruction files (CLAUDE.md, AGENTS.md, .cursorrules, GEMINI.md, copilot-instructions.md) lean: under ~150 lines, positive phrasing, task-specific sections moved to on-demand skills, hard constraints moved to hooks — because context files cost ~20% more tokens per task and do not raise success rates. Use when creating or editing such a file, when the agent ignores rules, or when a repo's rules file has grown past a screen. Tooling: `ad.py rules lint`. Scope boundary: converting negatives → `negative-constraint-compiler`."
metadata:
  priority: 5
  pathPatterns:
    - '**/CLAUDE.md'
    - '**/AGENTS.md'
    - '**/.cursorrules'
    - '**/copilot-instructions.md'
---
# Rules hygiene

Two independent studies: repos with AGENTS.md-style files see no significant gain in task success and ~20% higher token cost. The rules still matter for *style and safety* — so keep them cheap and make the critical ones mechanical.

## Checklist for a rules file
- [ ] ≤ 150 lines (`ad.py rules lint`). Every line earns its tokens on *every* turn.
- [ ] Top 10 lines = what the agent needs most often: build/test commands, repo layout, the three real gotchas.
- [ ] Positive phrasing with triggers (`When editing X, run Y`). Negatives → `negative-constraint-compiler`.
- [ ] Task-specific material (deploy runbook, migration guide) lives in a skill or `docs/` and is referenced, not inlined.
- [ ] Hard constraints (destructive commands, protected paths, prod) are hooks (`ad.py rules compile`, `ad.py scope set`), with one pointer line here.
- [ ] No duplication of what the tool already enforces (linter config, CI). Say "run `make lint`", not the style guide.
- [ ] Dated `Last reviewed:` line; prune on each review.

## Smells
Narrative history · "always/never" without a trigger · copy of the README · instructions for humans · 40-line code style section (that is what the formatter is for).
