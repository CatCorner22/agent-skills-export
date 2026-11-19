---
name: pii-minimization-before-send
description: "Redact personal data (emails, phones, SSNs, Luhn-valid card numbers, IBANs, dates of birth, street addresses, IPs, and listed names) from text before it goes to any hosted model, replacing each value with a stable token and keeping a local re-identification map, so the model can still reason about who is who. Use before sending client, patient, employee or customer material to a cloud model, in ingest pipelines, and when a provider's terms allow training on inputs. Ships pii_redact.py. Scope boundary: provider terms and hosting choice are skill:kimi-deployment-governance or the provider's governance skill; injection in the content is skill:untrusted-content-quarantine."
---

# PII minimization before send

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
Text that may contain personal data is about to leave your machine for a hosted model whose terms, retention or jurisdiction you do not fully control.

## Steps
1. Decide what the model needs. Most analysis tasks need roles and relationships, not identities. If identities are not needed, redact.
2. `python3 scripts/pii_redact.py input.txt --out redacted.txt --map map.json --names names.txt`. Put known names (client, patient, staff) in `names.txt`, one per line; the script does not guess names. `--allow email` or other categories when you have a lawful basis to send them.
3. Send `redacted.txt`. Keep `map.json` local; never attach it or paste it. Re-identify the model's output locally by replacing tokens from the map.
4. Read the redacted text once before sending: regexes miss free-text identifiers (unusual names, case numbers, rare diagnoses). Add any misses to `names.txt` and re-run.
5. Log that the redaction ran (counts per category, not values) with the request id.
6. For regulated data (health, legal, financial), pair this with a zero-retention or in-region endpoint; redaction lowers exposure, it does not replace the contract.

## Evidence
- Consumer-app privacy policies for several model vendors permit training on inputs by default; API and enterprise tiers differ. Vendor terms; re-read current versions.
- Regex redaction catches structured identifiers reliably and free-text identifiers poorly; the names list closes most of the gap. Practitioner.
- Full notes: [references/evidence.md](references/evidence.md)
