---
name: improve-system
description: Make the project's setup compound over time. Use when the user runs /improve-system, gives feedback about how things have been working, reports a repeated problem, or asks to audit/refresh the knowledge base or skills. Five modes - audit, skill-review, experience, historical-review, and foundation - each turn learnings into permanent improvements.
---

# Improve System

Never fix a problem more than twice. If something goes wrong once it might be a one-off; if it happens twice, it is a system problem and the fix belongs in the system — the knowledge base, a skill, or project instructions — not in a manually re-tweaked prompt.

This skill is the compounding layer: it takes what has happened (feedback, mistakes, new experience) and writes durable improvements so the next run is better.

## Where improvements get written

- `knowledge/` — the project knowledge base (see the `ingest-source` skill) for factual updates.
- Skill files (`.agents/skills/*/SKILL.md` or `~/.agents/skills/*/SKILL.md`) for process improvements.
- `AGENTS.md` / project instructions for always-on preferences.
- `knowledge/LEARNINGS.md` — a running log of what was learned and what was changed, one dated entry per improvement session.

## Modes

Pick the mode from the user's request. If they just run `/improve-system` with no argument, ask which mode they want or infer it from what they say next.

### Mode 1: `audit` — scan for outdated information

1. Read `knowledge/INDEX.md` and each source note in `knowledge/sources/`.
2. Flag notes that are stale (old dates in fast-moving topics), contradicted by newer notes, or no longer relevant to the project's goals.
3. For each flag, propose: refresh (re-research via `web-scraping` + `ingest-source`), reconcile (note the conflict and which source wins), or archive.
4. Apply the fixes the user approves and log them in `knowledge/LEARNINGS.md`.

### Mode 2: `skill-review` — improve the skills themselves

1. List the project's skills and review each SKILL.md alongside recent chat history in this session.
2. Look for: skills that failed to trigger when they should have (weak descriptions), instructions that were ambiguous or ignored, repeated manual corrections that should be baked in.
3. Propose concrete edits to the skill files, apply approved edits, and log them.

### Mode 3: `experience` — ingest the user's lived experience

The user's own experience is the biggest differentiator, because no one else has that training data.

1. Take the user's feedback ("here's my feedback on this past week...") and extract concrete learnings: what worked, what didn't, preferences, corrections to prior assumptions.
2. Write each learning where it belongs: factual learnings as a knowledge note (`knowledge/sources/experience-<date>.md`), process learnings into the relevant skill, standing preferences into project instructions.
3. When feedback contradicts the knowledge base, flag the disagreement explicitly and cite the original source — lived experience can outrank published research for this user, but the conflict must be recorded, not silently overwritten.

Example: "/improve-system — Review my fitness knowledge base. Flag any research that agrees or disagrees with what has been working for me and share the original source."

### Mode 4: `historical-review` — mine past sessions for missed learnings

1. Review whatever session history is available (recent conversation, transcripts, or files the user provides).
2. Hunt for: problems solved more than once, answers the user corrected, questions the system could not answer well, workarounds that were never systematized.
3. Turn each finding into a proposed improvement (knowledge note, skill edit, or instruction change), apply what the user approves, and log it.

### Mode 5: `foundation` — interview the user to fill gaps

1. Review the entire setup: project instructions, skills, and knowledge index.
2. Interview the user — a few questions at a time, not a wall of them — about goals, constraints, audience, success criteria, and context the system is missing.
3. Write the answers into the foundation: project instructions for durable context, knowledge notes for facts, new persona files for `ask-the-board` / `internal-focus-group` if relevant.

## Session wrap-up

At the end of every improve-system run, summarize: what was reviewed, what changed (with file paths), and what was deliberately left alone. Append the summary as a dated entry in `knowledge/LEARNINGS.md` so improvements are traceable over time.

## Rules

- Propose before overwriting: show the user what will change and why.
- Small, specific edits beat rewrites; preserve what already works.
- Every change gets a LEARNINGS.md entry — improvements that are not recorded get lost.
