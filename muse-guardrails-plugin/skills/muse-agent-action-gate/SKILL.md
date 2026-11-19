---
name: muse-agent-action-gate
description: "Gate consequential actions by Muse, Muse Spark, Muse Wonder, Meta AI, or Meta Model API; Scope boundary: skill:scope-and-blast-radius-check owns generic authority checks and skill:completion-evidence-gate owns completion proof."
---

# Muse agent action gate

## When it fires
Use before Muse pays, orders, cancels, sends, RSVPs or publishes, before connecting an account, and when its background proactivity proposes continuing refused or unapproved work.

## Steps
1. Apply `skill:scope-and-blast-radius-check` for generic authority; record the exact Muse surface, connector and action, including background workers. Must not transfer approval from a draft/read to a send/write.
2. Fill the pre-action record: action type; account/target; exact recipient/audience or item; payload; amount/currency/fees or cancellation consequences; recurrence; maximum exposure; and the user's approval tied to those values. Must leave execution blocked when any consequential field or current approval is missing.
3. Use least-privilege access for the specific task; inspect actual connector grants before connecting. The reported Drive grant is whole-drive, not proven folder-scoped; must use a sanitized excerpt or leave it disconnected if that scope is unnecessary or unacceptable.
4. Keep mailbox/profile/calendar reads bounded to the approved need; must record unexpected extra reads instead of rationalizing them as helpfulness, and pause new connector activity while the user reviews a scope mismatch.
5. Obtain action-specific confirmation through the trusted user channel; must not grant standing spend authority, let an agent invent a spending allowance, or let recurring/background work finish an unapproved or refused action. Draft/preview is the safe pending state.
6. Review the available audit trail for both reads and writes, reconcile targets/amounts with approval, and use `skill:completion-evidence-gate` for completion claims; must distinguish intended, attempted, confirmed and unobservable actions. Missing audit visibility is a limitation, not proof nothing happened.

## Evidence
- **Behavioral F4 (§3) — Contested:** YanyuLiu synthetic API-sandbox evaluation reports confirmation recall 5/12 plus extra profile/calendar/mailbox reads; Meta's agent page promises approval before publishing/sending/spending; no production unauthorized purchase is documented.
- **Behavioral F5 (§3) — Single-source:** @jonny reports a proactivity worker completing work refused by the main chat; do not generalize this to every deployment.
- **Report §2.9 — Single-source:** whole-drive connector access, with no folder-scoped access found in that research snapshot.
- [Report](../../references/research/report.md), [evaluation caveats](../../references/research/knowledge/sources/github-yanyuliu-meta-muse-eval.md), [researcher note](../../references/research/knowledge/sources/neuromatch-pi.md). Not locally reproduced.
