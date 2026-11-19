---
name: context-budget-governor
description: "Track context spend and write a CHECKPOINT.md (goal, decisions, open items, next step) at roughly every 30% of the window or every 25 tool calls, so compaction or a fresh thread restarts from your checkpoint instead of a lossy auto-summary. Use at session start, when output gets long, before a big read, when the host warns about context, or when you notice repeated work. Reinjected by `ad.py reinject`. Scope boundary: what was read → `read-manifest`; permissions → `autonomy-ledger`."
metadata:
  priority: 7
  pathPatterns:
    - '**/.agent/CHECKPOINT.md'
---
# Context budget governor

Context rot is gradual: quality falls before the window is full, and auto-compaction decides what to drop without you. Write the checkpoint yourself.

## Triggers
Session start (write a 5-line checkpoint) · every ~25 tool calls · before reading anything > 500 lines · before and after a long test/build · any host "context is getting long" notice · when you catch yourself re-deriving something.

## Checkpoint format (≤ 25 lines) — `ad.py checkpoint write` or edit `.agent/CHECKPOINT.md`
```
Goal: <one sentence, user's words>
Acceptance: <3 bullets>
Decisions: <what was chosen and why, dated>
Done: <files/commands>  Open: <next concrete step>
Do-not: <constraints from ledger>   Assumptions: <labeled>
```

## Budget heuristics
- Rough spend = tool output (dominant) + history + your output. If tool output > ~60% of what you've seen, trim (→ `tool-output-trimmer`) and checkpoint.
- Prefer **fresh thread from checkpoint** over a third compaction: `ad.py reinject --full` and paste.
- Ask for `/compact` yourself at a natural boundary (after a passing test, before a new sub-task), not mid-edit.

## After any compaction
Read the reinjected block first. If it is missing, run `ad.py reinject`. Re-verify numbers before reusing them.
