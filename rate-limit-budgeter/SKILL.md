---
name: rate-limit-budgeter
description: "Plan request rates against any provider's TPM/RPM limits (counting max output tokens at admission where the provider reserves on them) and classify 429-class errors into capacity, limit, quota or configuration with the fix for each (OpenAI, Anthropic, Google, Moonshot, gateways), plus a jittered backoff schedule. Use when designing batch or concurrent calls, when 429s or 529s appear, or when retries make things worse. Ships rate_budget.py plan|classify|backoff. Scope boundary: cost analysis is skill:cost-per-task-meter; Kimi-specific TPM rules are skill:kimi-rate-limit-budgeter."
---

# Rate limit budgeter

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
Before any concurrent or batch workload, and at the first 429.

## Steps
1. `python3 scripts/rate_budget.py plan --prompt-tokens 8000 --max-output-tokens 16000 --calls-per-min 20 --tpm 400000 --rpm 60`. Default `--reserve max` counts max output tokens at admission (OpenAI and Moonshot do); use `--reserve actual` only when your provider documents counting generated tokens.
2. Keep max output tokens honest: a generous cap is paid for in quota on every call even when the answer is short.
3. On an error, save the body and run `python3 scripts/rate_budget.py classify error.json`. Capacity errors (overloaded, engine overloaded, 503) get backoff; limit errors get lower rate or a tier change; quota errors get a top-up and no retries; 401/403/404 are configuration and must not be retried as rate limits.
4. Use `python3 scripts/rate_budget.py backoff` for a jittered schedule, and always prefer the provider's `Retry-After` or reset headers when present.
5. Separate the queues: interactive traffic gets its own key or project so batch retries cannot starve it. Move independent bulk work to the provider's batch endpoint where one exists.
6. Log error type, status and headers per 429 so the next incident starts from data.

## Evidence
- Moonshot documents three 429 types with different fixes and reserves TPM on `max_completion_tokens`; OpenAI documents `rate_limit_exceeded` vs `insufficient_quota` and estimates TPM from `max_tokens`; Anthropic separates `rate_limit_error` from `overloaded_error` (529). Vendor docs; re-check.
- Blind retries on quota or configuration errors are a common cause of outage amplification. Practitioner reports.
- Full notes: [references/evidence.md](references/evidence.md)
