---
name: model-handoff-at-boundary
description: "Switch models or providers only at artifact boundaries (a file, diff, report, checkpoint), never mid-thread, because reasoning history is provider-bound and replayed differently; write a handoff checkpoint and start the new model fresh. Use when a tool offers a model picker mid-session, when quality drops after a switch, when a Kimi, Claude, GPT or Gemini thread must continue elsewhere, or when planning multi-model workflows. Ships a handoff-checkpoint template. Scope boundary: periodic in-session checkpoints are skill:context-budget-governor; choosing the model is skill:model-router."
---

# Model handoff at boundary

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A conversation on one model is about to continue on another, including a different variant or effort level of the same family.

## Steps
1. Treat a switch as a new session. Fill `templates/handoff-checkpoint.md`: goal, decisions with reasons, artifacts and how each was verified, open items, one next step.
2. Carry only artifacts and the checkpoint. Do not replay chat history, thinking or reasoning blocks, or tool transcripts; providers reject or silently drop foreign reasoning and the receiving model performs worse on a replay shaped for another model.
3. Within one provider, keep model id and reasoning/thinking setting fixed for the whole task; changing either mid-thread resets prompt caching and alters behavior.
4. Plan multi-model workflows as stages with file outputs: draft (model A) -> file -> review (model B) -> file.
5. After the handoff, have model B restate the goal and next step from the checkpoint before acting; a mismatch means the checkpoint is incomplete.

## Evidence
- Moonshot: K3 is sensitive to replayed thinking history; switching models mid-conversation degrades output. Vendor via press. https://www.jiemian.com/article/14786726.html
- Anthropic rejects altered or foreign thinking blocks (400 Invalid signature); oh-my-pi issue 6379. https://github.com/can1357/oh-my-pi/issues/6379
- OpenAI reasoning items and Anthropic thinking blocks are opaque and provider-bound; no provider documents a lossless cross-provider replay. Vendor docs.
- Full notes: [references/evidence.md](references/evidence.md)
