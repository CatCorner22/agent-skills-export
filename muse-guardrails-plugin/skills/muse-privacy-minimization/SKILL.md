---
name: muse-privacy-minimization
description: "Minimize sensitive data and check forgetting in Muse, Muse Spark, Muse Wonder, Meta AI, or Meta Model API; Scope boundary: skill:scope-and-blast-radius-check owns generic data authority and skill:claim-evidence-pairing owns deletion claims."
---

# Muse privacy minimization

## When it fires
Use before uploads, inbox/Drive/calendar access, persistent memory, contributor-tier use or a request to forget/delete information.

## Steps
1. Apply `skill:scope-and-blast-radius-check` to data authority and classify the exact surface, tier, connector and purpose; must not infer that API retention is identical to the personal agent's dossier/memory system.
2. Keep client-confidential material, legal matters/privileged content, health information and third-party personal data out of Muse under this pack's policy. Must use synthetic or genuinely de-identified minimal excerpts instead, including removing relationship/inference clues and metadata; otherwise keep the task in an approved system without uploading it.
3. Check current account controls for memory/personalization, connected accounts, background jobs, training/product-improvement use, contributor/free-credit terms and deletion/retention. Must record what is actually available rather than inventing an opt-out or assuming paid access means no training.
4. Verify any encryption claim and who holds access before relying on it; must not treat marketing or the research-era promise as proof of current protection. Avoid broad connector grants and avoid retaining dossiers about people who never consented to this use.
5. For deletion, identify the minimum necessary record identifiers and separately request removal of memory entries, originating chats/messages/uploads and any relevant connected copies or scheduled jobs through current verified account/privacy channels. Must ask the provider to state scope, retention, exceptions and completion evidence without resending sensitive contents.
6. Recheck visible memory, conversation/upload surfaces and connector access after the request and preserve the acknowledgement; use `skill:claim-evidence-pairing` for each deletion claim. Must not equate “forget” with deletion of original messages, backups, de-identified shared lessons, previously exported copies or downstream recipients; unverified provider-side erasure remains unknown.

## Evidence
- **Behavioral F11 (§3), M4 (§7) — Established:** TIME (Harry Booth, 2026-10-06), @jonny and Meta's quoted response underpin reported user/non-user dossiers and forgetting limits; no direct cross-VM personal-data sharing is established.
- **Behavioral F11 (§3) — Established at theme level:** TIME reported promised provider-excluding encryption was not yet available on October 6; current availability was not tested.
- **Behavioral F14 (§3) — Probable:** contributor/free-credit product-improvement use in captured terms/reports, not a finding about every paid tier.
- [Report](../../references/research/report.md), [TIME source and qualifications](../../references/research/knowledge/sources/time-privacy.md), [evidence](../../references/research/evidence.md). The exclusion policy is a precaution, not a legal or retention guarantee.
