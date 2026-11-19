---
name: tool-loop-breaker
description: "Detect and break repeated identical tool-call loops in any agent transcript (OpenAI tool_calls or Anthropic tool_use): the same read over and over, read-only stalls with no edits, and harness rejection messages that provoke re-calls. Use when an agent burns tokens without progress, repeats a call the harness rejected, or says it will edit but keeps reading. Ships loop_detector.py. Scope boundary: per-call argument validation and the never-repeat-twice rule are skill:tool-call-validator; checkpointing is skill:context-budget-governor."
---

# Tool loop breaker

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
An agent repeats a tool call, reads without writing, or its reasoning repeats itself. Also when designing a harness.

## Steps
1. Export the transcript (JSON list, `{"messages": [...]}` or JSONL).
2. `python3 scripts/loop_detector.py transcript.json` flags 3 identical consecutive calls or 5 identical calls overall (`--run`, `--total` to tune), read-only stalls (20+ calls, 0 writes), terse dedup messages from the harness, and empty user turns.
3. On LOOP, stop the run. Do not resend an empty message.
4. Restart with a short fresh context: what is known (including the content it kept re-reading), one concrete next action, and an explicit success sentence: "The read succeeded; the file is unchanged; do not read it again."
5. Fix the harness: return cached content with a success message instead of a terse rejection; hard-block after N identical calls and return an instruction to act; compact context before it grows large (reports cluster around 200K+ tokens).
6. Record tokens and calls lost.

## Evidence
- MoonshotAI/kimi-code issue 3214: ~90 identical reads, 395 calls, 0 edits, context 203K-374K. https://github.com/MoonshotAI/kimi-code/issues/3214
- MoonshotAI/Kimi-K3 issue 12: harness dedup text read as failure, more identical calls followed. https://github.com/MoonshotAI/Kimi-K3/issues/12
- Comparable repeated-call reports exist in Claude Code, Codex CLI and Cline trackers; the harness fix is model-neutral. Issue reports, not measured rates.
- Full notes: [references/evidence.md](references/evidence.md)
