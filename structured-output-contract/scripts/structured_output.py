#!/usr/bin/env python3
"""Normalize an output JSON Schema for strict mode and validate model output against it.

Usage: structured_output.py normalize SCHEMA.json [--out normalized.json]
       structured_output.py validate SCHEMA.json OUTPUT.json [--repair-prompt]
normalize: drops keywords strict validators reject (format, pattern, min/max*, default, examples, $schema...),
sets additionalProperties false on every object and makes every property required (the OpenAI/Moonshot strict
contract; optional fields become nullable instead). Exit 1 if anything changed.
validate: checks type, required, additionalProperties, enum, nullable type lists, items and nested objects, plus
"unknown" sentinel strings where the schema allows them. Also strips a ```json fence and leading prose before
parsing, and reports that as a finding. With --repair-prompt, prints a short repair instruction listing each
violation, for one bounded retry. Exit 1 on violations, 2 on bad input.
"""
import json
import re
import sys

DROP = {"$schema", "$id", "$comment", "examples", "default", "format", "pattern", "minLength", "maxLength",
        "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "minItems", "maxItems", "uniqueItems",
        "multipleOf", "patternProperties", "dependencies", "if", "then", "else"}
TYPES = {"string": str, "integer": int, "number": (int, float), "boolean": bool, "array": list, "object": dict, "null": type(None)}


def normalize(node, changes, path="$"):
    if isinstance(node, list):
        return [normalize(x, changes, f"{path}[{i}]") for i, x in enumerate(node)]
    if not isinstance(node, dict):
        return node
    out = {k: v for k, v in node.items() if not (k in DROP and changes.append(f"{path}: dropped {k}") is None and True)}
    if out.get("type") == "object" or "properties" in out:
        props = out.get("properties", {})
        req_before = set(out.get("required", []))
        out["properties"] = {}
        for k, v in props.items():
            v = normalize(v, changes, f"{path}.{k}")
            if k not in req_before and isinstance(v, dict) and isinstance(v.get("type"), str) and v["type"] != "null":
                v["type"] = [v["type"], "null"]
                changes.append(f"{path}.{k}: optional property made nullable")
            out["properties"][k] = v
        if out.get("additionalProperties") is not False:
            out["additionalProperties"] = False
            changes.append(f"{path}: set additionalProperties false")
        req = list(props.keys())
        if out.get("required") != req:
            out["required"] = req
            changes.append(f"{path}: required set to all properties")
    if "items" in out:
        out["items"] = normalize(out["items"], changes, f"{path}[]")
    for comb in ("anyOf", "oneOf", "allOf"):
        if comb in out:
            out[comb] = [normalize(x, changes, f"{path}.{comb}[{i}]") for i, x in enumerate(out[comb])]
    return out


def type_ok(value, t):
    ts = t if isinstance(t, list) else [t]
    for name in ts:
        py = TYPES.get(name)
        if py is None:
            return True
        if name == "integer" and isinstance(value, bool):
            continue
        if name == "number" and isinstance(value, bool):
            continue
        if isinstance(value, py):
            return True
    return False


def validate(schema, value, path, errs):
    if not isinstance(schema, dict):
        return
    for comb in ("anyOf", "oneOf"):
        if comb in schema:
            sub_errs = []
            for s in schema[comb]:
                e = []
                validate(s, value, path, e)
                sub_errs.append(e)
            if not any(not e for e in sub_errs):
                errs.append(f"{path}: matches no {comb} variant")
            return
    t = schema.get("type")
    if t and not type_ok(value, t):
        errs.append(f"{path}: expected {t}, got {type(value).__name__}")
        return
    if "enum" in schema and value not in schema["enum"]:
        errs.append(f"{path}: {value!r} not in enum {schema['enum']}")
    if isinstance(value, dict):
        props = schema.get("properties", {})
        for k in schema.get("required", []):
            if k not in value:
                errs.append(f"{path}.{k}: required property missing")
        if schema.get("additionalProperties") is False:
            for k in value:
                if k not in props:
                    errs.append(f"{path}.{k}: unexpected property")
        for k, v in value.items():
            if k in props:
                validate(props[k], v, f"{path}.{k}", errs)
    if isinstance(value, list) and "items" in schema:
        for i, v in enumerate(value):
            validate(schema["items"], v, f"{path}[{i}]", errs)


def parse_output(raw, findings):
    text = raw.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    if m:
        findings.append("output wrapped in a code fence; stripped")
        text = m.group(1).strip()
    if text and text[0] not in "{[":
        start = min([i for i in (text.find("{"), text.find("[")) if i >= 0] or [0])
        if start > 0:
            findings.append(f"{start} chars of prose before JSON; stripped")
            text = text[start:]
    return json.loads(text)


def main(argv):
    if len(argv) < 3:
        print(__doc__); return 2
    mode = argv[1]
    try:
        schema = json.load(open(argv[2], encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read schema: {exc}"); return 2
    if mode == "normalize":
        changes = []
        norm = normalize(schema, changes)
        for c in changes:
            print(f"CHANGE {c}")
        if "--out" in argv:
            json.dump(norm, open(argv[argv.index("--out") + 1], "w", encoding="utf-8"), indent=2)
            print(f"wrote {argv[argv.index('--out') + 1]}")
        else:
            print(json.dumps(norm, indent=2))
        print(f"summary: {len(changes)} change(s)")
        return 1 if changes else 0
    if mode == "validate":
        if len(argv) < 4:
            print(__doc__); return 2
        findings = []
        try:
            raw = open(argv[3], encoding="utf-8").read()
            value = parse_output(raw, findings)
        except OSError as exc:
            print(f"cannot read output: {exc}"); return 2
        except json.JSONDecodeError as exc:
            print(f"ERROR output is not JSON: {exc}")
            if "--repair-prompt" in argv:
                print("\nREPAIR PROMPT:\nReturn only a JSON value that parses, with no prose or code fence. Error was: " + str(exc))
            return 1
        errs = []
        validate(schema, value, "$", errs)
        for f in findings:
            print(f"WARN  {f}")
        for e in errs:
            print(f"ERROR {e}")
        print(f"summary: {len(errs)} violation(s), {len(findings)} warning(s)")
        if errs and "--repair-prompt" in argv:
            print("\nREPAIR PROMPT:\nYour previous JSON violated the schema. Fix exactly these and return the full JSON only:\n- " + "\n- ".join(errs) + "\nUse null or \"unknown\" where you have no supported value; do not invent one.")
        return 1 if errs else 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
