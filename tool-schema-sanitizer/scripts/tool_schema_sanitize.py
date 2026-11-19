#!/usr/bin/env python3
"""Sanitize function/MCP tool definitions so strict providers accept them.

Usage: tool_schema_sanitize.py TOOLS.json [--out fixed.json] [--profile strict|openai|anthropic|gemini|moonshot]
TOOLS.json: {"tools": [OpenAI {"type":"function","function":{...}} or MCP {"name","inputSchema"} items]}
Fixes (profile "strict", the default, applies all): tool names outside ^[a-zA-Z_][a-zA-Z0-9_-]{0,63}$
(digit-leading names get a t_ prefix; other characters become _), untyped anyOf/oneOf unions (collapsed to the
first typed variant, nullable kept as a type list), $ref outside #/$defs (inlined when resolvable, else dropped),
formatting/validation keywords several validators reject, properties without a type, duplicate names, missing
descriptions. Profiles relax rules the named provider documents as accepted (openai/anthropic allow digit-leading
names; openai keeps $defs refs). Output is always OpenAI function shape. Exit 1 if anything changed, 2 on bad input.
Every profile is a starting point: re-check the provider's current schema page.
"""
import copy
import json
import re
import sys

PROFILES = {
    "strict": {"name": r"^[a-zA-Z_][a-zA-Z0-9_-]{0,63}$", "collapse_unions": True, "keep_defs_ref": False},
    "moonshot": {"name": r"^[a-zA-Z_][a-zA-Z0-9_-]{0,63}$", "collapse_unions": True, "keep_defs_ref": True},
    "openai": {"name": r"^[a-zA-Z0-9_-]{1,64}$", "collapse_unions": False, "keep_defs_ref": True},
    "anthropic": {"name": r"^[a-zA-Z0-9_-]{1,64}$", "collapse_unions": False, "keep_defs_ref": True},
    "gemini": {"name": r"^[a-zA-Z_][a-zA-Z0-9_-]{0,63}$", "collapse_unions": True, "keep_defs_ref": False},
}
DROP = {"$schema", "$id", "$comment", "examples", "default", "format", "pattern", "minLength", "maxLength",
        "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "minItems", "maxItems", "uniqueItems",
        "multipleOf", "patternProperties", "dependencies", "if", "then", "else", "title"}


def resolve_ref(ref, root):
    if not ref.startswith("#/"):
        return None
    node = root
    for part in ref[2:].split("/"):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return copy.deepcopy(node)


def fix(node, root, changes, path, prof):
    if isinstance(node, list):
        return [fix(x, root, changes, f"{path}[{i}]", prof) for i, x in enumerate(node)]
    if not isinstance(node, dict):
        return node
    if "$ref" in node and not (prof["keep_defs_ref"] and node["$ref"].startswith("#/$defs/")):
        ref = node["$ref"]
        target = resolve_ref(ref, root)
        if target is not None:
            changes.append(f"{path}: inlined {ref}")
            node = {**target, **{k: v for k, v in node.items() if k != "$ref"}}
        else:
            changes.append(f"{path}: dropped unresolvable {ref}; set type object")
            node = {k: v for k, v in node.items() if k != "$ref"}
            node.setdefault("type", "object")
    out = {}
    for k, v in node.items():
        if k in DROP:
            changes.append(f"{path}: dropped {k}")
            continue
        out[k] = v
    if prof["collapse_unions"]:
        for comb in ("anyOf", "oneOf"):
            if comb in out and "type" not in out:
                variants = [v for v in out[comb] if isinstance(v, dict)]
                typed = [v for v in variants if v.get("type") and v.get("type") != "null"]
                nullable = any(v.get("type") == "null" for v in variants)
                if typed:
                    base = fix(typed[0], root, changes, f"{path}.{comb}[0]", prof)
                    merged = {**base, **{k: v for k, v in out.items() if k != comb}}
                    if nullable and isinstance(merged.get("type"), str):
                        merged["type"] = [merged["type"], "null"]
                    changes.append(f"{path}: collapsed untyped {comb} to {merged.get('type')}")
                    out = merged
                else:
                    changes.append(f"{path}: {comb} had no typed variant; set type string")
                    out.pop(comb)
                    out["type"] = "string"
    if "properties" in out:
        out["properties"] = {k: fix(v, root, changes, f"{path}.{k}", prof) for k, v in out["properties"].items()}
        out.setdefault("type", "object")
        for k, v in out["properties"].items():
            if isinstance(v, dict) and "type" not in v and not any(c in v for c in ("anyOf", "oneOf", "allOf", "enum", "$ref")):
                v["type"] = "string"
                changes.append(f"{path}.{k}: added missing type string")
    if "items" in out:
        out["items"] = fix(out["items"], root, changes, f"{path}[]", prof)
    for comb in ("allOf", "anyOf", "oneOf"):
        if comb in out and isinstance(out[comb], list):
            out[comb] = [fix(v, root, changes, f"{path}.{comb}[{i}]", prof) for i, v in enumerate(out[comb])]
    if "$defs" in out and prof["keep_defs_ref"]:
        out["$defs"] = {k: fix(v, root, changes, f"{path}.$defs.{k}", prof) for k, v in out["$defs"].items()}
    elif "$defs" in out or "definitions" in out:
        out.pop("$defs", None); out.pop("definitions", None)
        changes.append(f"{path}: removed definitions block after inlining")
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    profile = argv[argv.index("--profile") + 1] if "--profile" in argv else "strict"
    if profile not in PROFILES:
        print(f"unknown profile {profile}; choose from {sorted(PROFILES)}"); return 2
    prof = PROFILES[profile]
    name_rx = re.compile(prof["name"])
    try:
        data = json.load(open(argv[1], encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read: {exc}"); return 2
    tools = data.get("tools", data if isinstance(data, list) else [])
    changes, seen, fixed = [], set(), []
    for i, t in enumerate(tools):
        fn = t.get("function", t)
        name = fn.get("name", f"tool{i}")
        if not name_rx.match(name):
            new = re.sub(r"[^a-zA-Z0-9_-]", "_", name)[:60]
            if not re.match(r"^[a-zA-Z_]", new):
                new = "t_" + new
            changes.append(f"tools[{i}]: renamed {name!r} -> {new!r} (invalid for profile {profile})")
            name = new
        if name in seen:
            changes.append(f"tools[{i}]: duplicate name {name!r} dropped")
            continue
        seen.add(name)
        params = fn.get("parameters", fn.get("inputSchema", {"type": "object", "properties": {}}))
        params = fix(params, params, changes, f"tools[{i}].parameters", prof)
        params.setdefault("type", "object")
        params.setdefault("properties", {})
        if not fn.get("description"):
            changes.append(f"tools[{i}]: missing description; added placeholder")
        fixed.append({"type": "function", "function": {"name": name, "description": fn.get("description") or f"Tool {name}", "parameters": params}})
    for c in changes:
        print(f"CHANGE {c}")
    out = {"tools": fixed}
    if "--out" in argv:
        json.dump(out, open(argv[argv.index("--out") + 1], "w", encoding="utf-8"), indent=2)
        print(f"wrote {argv[argv.index('--out') + 1]}")
    print(f"summary: profile {profile}; {len(fixed)} tool(s), {len(changes)} change(s)")
    return 1 if changes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
