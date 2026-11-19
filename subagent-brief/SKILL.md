---
name: subagent-brief
description: "Write a stand-alone brief for any sub-agent, worker or delegated model that sees nothing but the brief: goal, the only context it needs, do-not list, named inputs, suggested steps, an exact JSON return format with status, and a numbered budget with a blocked rule; then lint the brief before dispatch. Use when fanning work out to sub-agents, swarms, child sessions or a second model, and when sub-agent results come back vague or off-scope. Ships a brief template and brief_check.py. Scope boundary: the full task contract for a primary model is skill:task-contract; LangGraph/deep-agents orchestration is skill:deep-agents-orchestration; secrets in the brief are skill:agent-secret-hygiene."
---

# Sub-agent brief

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
Work is about to be delegated to a process that does not share your context.

## Steps
1. Copy `templates/subagent-brief.md`. Fill every `{}`; the sub-agent has no history, no chat, and cannot ask you.
2. Keep context to facts it needs. Decisions already made go in as facts, not as history. Paths are absolute or repo-relative.
3. Name every input and attach or path it. Anything not named is not available to it, and the brief tells it to return "blocked" rather than guess.
4. Keep the exact JSON return format with `status`, `summary`, `evidence`, `changed_files`, `open_questions`. Evidence means a command or `file:line`, so you can verify without re-reading its transcript.
5. `python3 scripts/brief_check.py brief.md --files <inputs>`. Fix placeholders, missing sections, a budget without numbers, a missing blocked rule, and inputs not attached.
6. When results come back, read `evidence` first; a result with `status: ok` and empty evidence is a retry with a tighter brief.

## Evidence
- Sub-agents and swarm workers return only final text; parallel fan-out tools from several vendors warn that unclear briefs multiply cost. Vendor docs and practitioner reports.
- Unvetted sub-agent briefs led to credential posting and install-script execution in one evaluation. https://neoresearch.ai/papers/Kimi_K3_Safety_Evaluation.pdf
- Full notes: [references/evidence.md](references/evidence.md)
