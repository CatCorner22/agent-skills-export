---
name: autonomy-ledger
description: "Record permissions, limits, stop conditions, and acceptance criteria the user gives you in .agent/ledger.md, and check it before asking any permission question — if already granted, proceed and cite the line; if forbidden, don't. Use when the user grants scope ('you can edit anything under src/'), says 'keep going / don't ask', sets a boundary, or when you are about to ask 'may I…?'. Survives compaction via `ad.py reinject`. Scope boundary: deciding whether a gap merits a question → `ask-or-assume`; destructive actions → `scope-and-blast-radius-check`."
metadata:
  priority: 8
  pathPatterns:
    - '**/.agent/ledger.md'
  bashPatterns:
    - '\bad\.py ledger\b'
---
# Autonomy ledger

Re-asking for permission already granted is the #1 passivity complaint, and it gets worse after compaction because the grant was in the dropped history. The ledger is the fix: grants live on disk.

## Record immediately (one line each)
```
ad.py ledger add GRANT  "edit any file under src/ and tests/ without asking"
ad.py ledger add FORBID "touch migrations/ or anything in prod"
ad.py ledger add STOP   "stop and report if the test suite takes > 10 min"
ad.py ledger add ACCEPT "done = pytest green + lint clean + PR opened as draft"
ad.py ledger add SCOPE  "repo root only; no network calls except npm"
```
Triggers: "you can…", "go ahead and…", "don't ask, just…", "never…", "stop if…", "done means…", and any permission prompt the user answers.

## Before any permission question
`ad.py ledger check "<the action>"` → ALREADY GRANTED: do it and say "per your earlier grant: …". FORBIDDEN: don't; say why. NO ENTRY: reversible → proceed with a labeled assumption; confirm-first list → ask once, then record the answer.

## Rules
- Latest entry wins. Record the user's words, not your paraphrase.
- The ledger unlocks `scope-fence`: a GRANT whose words overlap the blocked command lets it through — so write the exact command into the grant.
- Never record a grant the user did not give. Never infer "keep going" from silence.
