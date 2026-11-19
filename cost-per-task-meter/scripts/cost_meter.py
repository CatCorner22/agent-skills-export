#!/usr/bin/env python3
"""Cost per successful task, reasoning share and cache share from any provider's usage records.

Usage: cost_meter.py USAGE.jsonl --in PRICE --out PRICE [--cached PRICE] [--cache-write PRICE] [--task-key task]
Prices are USD per million tokens for the model you ran (input miss, output, cached input read, cache write).
USAGE.jsonl: one record per call with a `usage` object in OpenAI, Anthropic or Gemini shape (prompt_tokens|
input_tokens|promptTokenCount, completion_tokens|output_tokens|candidatesTokenCount, reasoning_tokens|
thoughtsTokenCount, cached_tokens|cache_read_input_tokens|cachedContentTokenCount, cache_creation_input_tokens)
plus optional `task`, `success` (bool), `model`, `reasoning_effort`. Prints per-task tokens, cache share,
reasoning share, cost, and cost per successful task; flags reasoning share > 85%, cache share < 30% on
multi-call tasks, failures at the lowest effort setting, and mixed models inside one task. Exit 1 if a flag
fires, 2 on bad input.
"""
import json
import sys
from collections import defaultdict


def arg(argv, name, default):
    return float(argv[argv.index(name) + 1]) if name in argv else default


def g(d, *keys, default=0):
    for k in keys:
        if isinstance(d, dict) and k in d and d[k] is not None:
            return d[k]
    return default


def main(argv):
    if len(argv) < 2 or "--in" not in argv or "--out" not in argv:
        print(__doc__); return 2
    p_in, p_out = arg(argv, "--in", 0), arg(argv, "--out", 0)
    p_cached, p_write = arg(argv, "--cached", p_in / 10), arg(argv, "--cache-write", p_in)
    task_key = argv[argv.index("--task-key") + 1] if "--task-key" in argv else "task"
    tasks = defaultdict(lambda: {"calls": 0, "prompt": 0, "cached": 0, "write": 0, "completion": 0, "reasoning": 0, "success": None, "effort": set(), "models": set()})
    try:
        rows = [json.loads(l) for l in open(argv[1], encoding="utf-8") if l.strip()]
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read: {exc}"); return 2
    for r in rows:
        u = r.get("usage", r.get("usageMetadata", r))
        t = tasks[str(r.get(task_key, "all"))]
        t["calls"] += 1
        t["prompt"] += g(u, "prompt_tokens", "input_tokens", "promptTokenCount")
        t["cached"] += g(u.get("prompt_tokens_details", {}), "cached_tokens") or g(u, "cached_tokens", "cache_read_input_tokens", "cachedContentTokenCount")
        t["write"] += g(u, "cache_creation_tokens", "cache_creation_input_tokens")
        t["completion"] += g(u, "completion_tokens", "output_tokens", "candidatesTokenCount")
        t["reasoning"] += g(u.get("completion_tokens_details", {}), "reasoning_tokens") or g(u, "reasoning_tokens", "thoughtsTokenCount")
        if "success" in r:
            t["success"] = bool(r["success"])
        for k in ("reasoning_effort", "effort", "thinking"):
            if r.get(k) is not None:
                t["effort"].add(str(r[k]))
        if r.get("model"):
            t["models"].add(str(r["model"]))
    flags, total_cost, successes = [], 0.0, 0
    print(f"{'task':20} {'calls':>5} {'in_tok':>9} {'cache%':>7} {'out_tok':>9} {'reason%':>8} {'cost$':>8} ok")
    for name, t in tasks.items():
        miss = max(t["prompt"] - t["cached"], 0)
        cost = (miss * p_in + t["cached"] * p_cached + t["write"] * p_write + t["completion"] * p_out) / 1e6
        total_cost += cost
        cache_share = t["cached"] / t["prompt"] if t["prompt"] else 0
        reason_share = t["reasoning"] / t["completion"] if t["completion"] else 0
        ok = "" if t["success"] is None else ("yes" if t["success"] else "no")
        successes += 1 if t["success"] else 0
        print(f"{name[:20]:20} {t['calls']:5d} {t['prompt']:9d} {cache_share*100:6.1f}% {t['completion']:9d} {reason_share*100:7.1f}% {cost:8.4f} {ok}")
        if reason_share > 0.85 and t["completion"] > 2000:
            flags.append(f"{name}: reasoning is {reason_share*100:.0f}% of output; try a lower effort/thinking budget for this task class and re-measure success")
        if t["calls"] >= 3 and cache_share < 0.30:
            flags.append(f"{name}: cache share {cache_share*100:.0f}% over {t['calls']} calls; the prefix is probably changing (timestamps, effort switch, compaction trimming the head)")
        if t["effort"] & {"none", "minimal", "0", "off", "false"} and t["success"] is False:
            flags.append(f"{name}: lowest effort setting and the task failed; the cheapest setting is not free if it drops success")
        if len(t["models"]) > 1:
            flags.append(f"{name}: {len(t['models'])} models in one task ({', '.join(sorted(t['models']))}); mid-task switches degrade history replay")
    scored = [t for t in tasks.values() if t["success"] is not None]
    print(f"total cost ${total_cost:.4f} over {len(tasks)} task(s)")
    if scored:
        rate = successes / len(scored)
        cps = total_cost / successes if successes else float("inf")
        print(f"success rate {rate*100:.0f}%; cost per successful task ${cps:.4f}")
    for f in flags:
        print("FLAG " + f)
    return 1 if flags else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
