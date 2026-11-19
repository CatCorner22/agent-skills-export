# Muse Spark Open evaluation methodology — Meta

## Source

- **Title:** Muse Spark Open evaluation methodology — Meta
- **Author/origin:** Meta
- **Date:** publication date not captured; accessed 2026-11-10
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `open-evalmethod.txt`.
- **Source URL / scope:** https://research.meta.ai/static/muse-spark-open-evaluation-methodology — Muse Spark Open evaluation methodology — Meta; publication date not captured; accessed 2026-11-10

## Grade

**A** — First-party statements/specifications about Meta’s own product; not independent validation.

## Product/version covered

Muse Spark Open benchmark configurations

## Summary

Harnesses, LLM judges, subsets, exclusions and run settings bound benchmark comparability. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- A comparison is meaningful only with the same versions, settings and provenance. `"Each task requires the model to produce one or more deliverable files, run as an agent in AA's open-source Stirrup harness with an E2B code-execution sandbox, a 250-turn budget, and access to a range of available tools."` (open-evalmethod.txt PDF text, whitespace normalized).
- A comparison is meaningful only with the same versions, settings and provenance. `"For Beam, we report its self-reported performance, which does not specify the harness."` (open-evalmethod.txt PDF text, whitespace normalized).
- A comparison is meaningful only with the same versions, settings and provenance. `"For all models besides Beam and Mistral Large 4, we report results from Artificial Analysis following the documented benchmarking methodology , which uses the Terminus 2 agent harness in an E2B sandbox environment."` (open-evalmethod.txt PDF text, whitespace normalized).
- A comparison is meaningful only with the same versions, settings and provenance. `"Knowledge & Reasoning ● Humanity's Last Exam (HLE) Diamond (not tools) HLE-Diamond is a refined 1,000-question subset of Humanity's Last Exam, released by 4 Muse Spark Open Evaluation Methodology October 2026 CAIS."` (open-evalmethod.txt PDF text, whitespace normalized).
- A comparison is meaningful only with the same versions, settings and provenance. `"Multimodal Since Nemotron 3 Ultra, GLM 5.3, Qwen3.8-2.4T-A95B, and Beam do not natively support multimodal inputs, we do not run multimodal evals on those models."` (open-evalmethod.txt PDF text, whitespace normalized).
- A comparison is meaningful only with the same versions, settings and provenance. `"Muse Spark Open Evaluation Methodology October 2026 Per-benchmark details General ● Artificial Analysis Intelligence Index Artificial Analysis Intelligence Index v4.3 consists of 10 evaluations: AA-Briefcase, GDPval-AA v2,"` (open-evalmethod.txt PDF text, whitespace normalized).
- A comparison is meaningful only with the same versions, settings and provenance. `"Muse Spark Open Evaluation Methodology We evaluate Muse Spark Open on general agentic, coding, multimodal, knowledge & reasoning, and safety benchmarks."` (open-evalmethod.txt PDF text, whitespace normalized).
- A comparison is meaningful only with the same versions, settings and provenance. `"Results for Muse Spark Open (with Muse Code harness), Kimi K3 (Kimi Code), GLM 5.3 (Open Code), and Qwen3.8-2.4T-A95B (Claude Code) and their corresponding harnesses are sourced from Artificial Analysis following the documented"` (open-evalmethod.txt PDF text, whitespace normalized).

## Data/numbers

- `"Each task requires the model to produce one or more deliverable files, run as an agent in AA's open-source Stirrup harness with an E2B code-execution sandbox, a 250-turn budget, and access to a range of available tools."`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"For all models besides Beam and Mistral Large 4, we report results from Artificial Analysis following the documented benchmarking methodology , which uses the Terminus 2 agent harness in an E2B sandbox environment."`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"Knowledge & Reasoning ● Humanity's Last Exam (HLE) Diamond (not tools) HLE-Diamond is a refined 1,000-question subset of Humanity's Last Exam, released by 4 Muse Spark Open Evaluation Methodology October 2026 CAIS."`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"Multimodal Since Nemotron 3 Ultra, GLM 5.3, Qwen3.8-2.4T-A95B, and Beam do not natively support multimodal inputs, we do not run multimodal evals on those models."`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"Muse Spark Open Evaluation Methodology October 2026 Per-benchmark details General ● Artificial Analysis Intelligence Index Artificial Analysis Intelligence Index v4.3 consists of 10 evaluations: AA-Briefcase, GDPval-AA v2,"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"Results for Muse Spark Open (with Muse Code harness), Kimi K3 (Kimi Code), GLM 5.3 (Open Code), and Qwen3.8-2.4T-A95B (Claude Code) and their corresponding harnesses are sourced from Artificial Analysis following the documented"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"Results for all models besides Beam and Mistral Large 4 are sourced from Scale’s leaderboard, which reports on the private split of FORTRESS."`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"Since Beam and Mistral Large 4 numbers were not available in their model cards or on the JobBench leaderboard, we did not report them. ● GDPval-AA v2 : GDPval-AA v2 assesses models on economically valuable knowledge work spanning"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"Since Beam and Mistral Large 4 numbers were not available in their model cards or on the Toolathlon-Verified leaderboard, we did not report them. 3 Muse Spark Open Evaluation Methodology October 2026 Coding ● DeepSWE v1.1 :"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"Since results for Inkling and Nemotron 3 Ultra were not available in their model cards or on the Artificial Analysis leaderboard, we did not report them. ● Terminal-Bench 2.1 : Terminal-Bench 2.1 evaluates an agent on real-world"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"The VM renders at 1920 × 1080 in all runs, but because models are trained against different coordinate conventions, we run each in its native format rather than imposing one: our models receive the 1920 × 1080 screenshot and emit"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We cite Beam’s self-reported number, and use results produced by Scale AI for the remaining models following the official leaderboard’s 2 Muse Spark Open Evaluation Methodology October 2026 agent harness and scoring pipeline."`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We do not report Nemotron 3 Ultra, GLM 5.3, Qwen3.8-2.4T-A95B, or Beam, as they do not support pure-vision GUI inputs under these settings."`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We do not report results for Mistral Large 4 as the model was not available for internal testing at the time of evaluation. ● Toolathlon-Verified : Toolathlon is an agentic tool-use benchmark in which a language agent completes"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We report BabyVision, SimpleVQA, ZeroBench, and WorldVQA with tool use enabled. ● BabyVision : BabyVision contains 388 visual-reasoning questions spanning fine-grained discrimination, spatial perception, visual tracking, and"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We report results from internal runs for all 3 multimodal models and report the average of 5 runs. ● ZeroBench : ZeroBench contains 100 deliberately difficult multimodal-reasoning questions."`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We source results for Muse Spark Open (with Muse Code harness) from Artificial Analysis, and from each model’s self report for Beam (harness unspecified), Mistral Large 4 (harness unspecified), GLM 5.3 (mini-swe-agent),"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We source results for all models besides Beam and Mistral Large 4 from Scale AI, which maintains the HLE Diamond leaderboard, following the documented methodology . ● AA Omniscience Index : AA-Omniscience is Artificial Analysis's"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We sourced the AA Intelligence Index score for all models (with the exception of Beam, which was not available at the time of writing) from Artificial Analysis on October 7, 2026, following their documented Intelligence Index"`  (open-evalmethod.txt PDF text, whitespace normalized).
- `"We evaluate on the 361-task split that excludes Google Drive–dependent tasks."` OSWorld: GUI-only, execution-based success, four attempts per task; internal Meta/Inkling runs versus Kimi self-report. (open-evalmethod.txt PDF text, whitespace normalized).
- `"An LLM judge assigns each ground-truth claim a score: 1 if fulfilled, 0.5 if partially fulfilled, and 0 if not fulfilled."` MCP-Atlas: claim coverage >=0.75 passes; LLM judge, not literal exact-match success. (open-evalmethod.txt PDF text, whitespace normalized).
- `"the text-only subset of 2,158 questions and with no tool use permitted."` HLE no-tools via AA; with-tools internal Meta runs permit bash/browser with site blocklist, not identical setting. (open-evalmethod.txt PDF text, whitespace normalized).
- `"which excludes 500 questions in the Notable People category."` WorldVQA canonical 3,000-question subset; GPT-OSS-120B high-reasoning correctness judge, internal five-run averages. (open-evalmethod.txt PDF text, whitespace normalized).
- `"GPT-OSS-120B with high reasoning grades correctness against the reference answer."` Model-based judge, not independent human validation. (open-evalmethod.txt PDF text, whitespace normalized).
- Further issue-specific numbers remain in the linked evidence sections; this note does not turn code versions, status codes or issue IDs into benchmark measurements.

## How it relates to other sources

- **Explains the vendor table:** [Muse Spark Open 816B-A42B — Meta model card](hf-card.md) — Harnesses, judges and exclusions define what the scores mean.
- **Disputed comparability:** [HN: Muse Spark 1.1 and Model API discussion](hn-48846184.md) — HN resource critiques and counterarguments do not settle a standardized rerun.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- First-party capabilities, privacy/approval promises and benchmark claims are not independently validated by being quoted here.
- PDF text quotes use whitespace normalization, as labeled in evidence.md. Judge choices, subsets and exclusions limit external validity.
