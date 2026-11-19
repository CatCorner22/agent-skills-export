#!/usr/bin/env python3
"""Exposure table for Rumsfeld's Binoculars: rank scenarios by consequence, test the ranking against
probability error, and separate ruin from routine risk.

Input: a CSV with a header row. Required columns: scenario, probability (per horizon, 0 to 1),
impact (loss in one unit, positive). Optional columns: reversible (yes/no), detectable (yes/no),
evidence (data, model, judgment, or guess).

Usage:
  python3 exposure_table.py scenarios.csv [--ruin 1000000] [--error-factor 3] [--json]
  cat scenarios.csv | python3 exposure_table.py -

Options:
  --ruin X          an impact at or above X is unrecoverable; such scenarios rank by severity, not by expected value
  --error-factor F  multiply every probability below 0.1 by F (default 3) to test whether the ranking survives model error
Exit: 0 on a report; 2 when the input cannot be read or a row is invalid.
"""
import argparse
import csv
import json
import sys


class InputError(Exception):
    pass


def truthy(value):
    return str(value).strip().lower() in ("y", "yes", "true", "1")


def load(path):
    if path == "-":
        text = sys.stdin.read()
    else:
        try:
            with open(path, encoding="utf-8-sig", newline="") as handle:
                text = handle.read()
        except FileNotFoundError:
            raise InputError(f"{path}: no such file")
        except IsADirectoryError:
            raise InputError(f"{path}: is a folder")
        except UnicodeDecodeError:
            raise InputError(f"{path}: not UTF-8 text")
    reader = csv.DictReader(text.splitlines())
    if not reader.fieldnames:
        raise InputError(f"{path}: empty file")
    fields = {name.strip().lower(): name for name in reader.fieldnames if name}
    for required in ("scenario", "probability", "impact"):
        if required not in fields:
            raise InputError(f"{path}: missing column {required!r}; found {list(fields)}")
    rows = []
    for number, raw in enumerate(reader, 2):
        get = lambda key: (raw.get(fields[key]) or "").strip() if key in fields else ""
        name = get("scenario")
        if not name:
            continue
        try:
            probability = float(get("probability").rstrip("%")) / (100 if get("probability").endswith("%") else 1)
            impact = float(get("impact").replace(",", ""))
        except ValueError:
            raise InputError(f"{path}: line {number}: probability and impact must be numbers")
        if not 0 <= probability <= 1:
            raise InputError(f"{path}: line {number}: probability {probability} lies outside 0 to 1")
        if impact < 0:
            raise InputError(f"{path}: line {number}: impact must be 0 or more (enter losses as positive numbers)")
        rows.append({
            "scenario": name, "probability": probability, "impact": impact,
            "reversible": truthy(get("reversible")) if "reversible" in fields else None,
            "detectable": truthy(get("detectable")) if "detectable" in fields else None,
            "evidence": get("evidence").lower() or None,
        })
    if not rows:
        raise InputError(f"{path}: no scenario rows")
    return rows


def expected_shortfall(rows, mass=0.10):
    """Probability-weighted mean impact of the worst scenarios that hold the top MASS of probability."""
    remaining, weighted = mass, 0.0
    for row in sorted(rows, key=lambda r: -r["impact"]):
        take = min(row["probability"], remaining)
        weighted += take * row["impact"]
        remaining -= take
        if remaining <= 1e-12:
            break
    used = mass - remaining
    return weighted / used if used > 0 else None, used


def rank(rows, key):
    order = sorted(rows, key=lambda r: -key(r))
    return {row["scenario"]: position + 1 for position, row in enumerate(order)}


def analyse(rows, ruin, factor):
    for row in rows:
        row["expected_loss"] = row["probability"] * row["impact"]
    impacts = sorted(r["impact"] for r in rows)
    high_cut = impacts[len(impacts) // 2]
    flags = []
    for row in rows:
        row["class"] = ("RUIN" if ruin is not None and row["impact"] >= ruin else
                        "HIGH-CONSEQUENCE, LOW-FREQUENCY" if row["probability"] < 0.1 and row["impact"] >= high_cut else
                        "ROUTINE")
        if row["class"] == "RUIN":
            flags.append(f"{row['scenario']}: impact {row['impact']:,.0f} reaches ruin. Rank it by severity, not by expected loss, and require a control that stops the path or caps the loss below {ruin:,.0f}.")
        if row["probability"] == 0:
            flags.append(f"{row['scenario']}: probability 0 is a claim of impossibility. Replace it with an upper bound (for 0 events in n trials, about 3/n).")
        elif row["probability"] < 0.01 and row["evidence"] not in ("data",):
            flags.append(f"{row['scenario']}: probability {row['probability']:g} claims more precision than {row['evidence'] or 'unstated'} evidence supports. State the base rate and its source, or widen it.")
        if row["reversible"] is False and row["detectable"] is False:
            flags.append(f"{row['scenario']}: irreversible and undetectable, a blind one-way door. Add a tripwire or a reversible path before anything else.")
    total_probability = sum(r["probability"] for r in rows)
    if total_probability > 1:
        flags.append(f"probabilities sum to {total_probability:.2f}. If the scenarios exclude each other, the sum must stay at or below 1; if they can co-occur, say so in the report.")
    base = rank(rows, lambda r: r["expected_loss"])
    stressed = rank(rows, lambda r: min(1.0, r["probability"] * factor if r["probability"] < 0.1 else r["probability"]) * r["impact"])
    moves = [(name, base[name], stressed[name]) for name in base if base[name] != stressed[name]]
    shortfall, mass_used = expected_shortfall(rows)
    return {
        "rows": sorted(rows, key=lambda r: -r["impact"]),
        "total_expected_loss": sum(r["expected_loss"] for r in rows),
        "total_probability": total_probability,
        "expected_shortfall_top_10pct": shortfall,
        "shortfall_mass_used": mass_used,
        "rank_changes_under_error_factor": moves,
        "error_factor": factor,
        "ruin": ruin,
        "flags": flags,
        "limits": [
            "the table holds only the scenarios that someone wrote down; the unknown unknowns are not in it",
            "expected loss hides the tail: 2 scenarios with equal expected loss differ when one of them ends the game",
            "probabilities from judgment carry an error of 2 to 10 times either way; the error-factor check shows what that error does to the ranking",
        ],
    }


def money(value):
    return f"{value:,.0f}" if abs(value) >= 1000 else f"{value:.4g}"


def print_report(result):
    print(f"{'scenario':30} {'p':>8} {'impact':>14} {'exp. loss':>14}  class")
    for row in result["rows"]:
        print(f"{row['scenario'][:30]:30} {row['probability']:>8.4g} {money(row['impact']):>14} {money(row['expected_loss']):>14}  {row['class']}")
    print(f"total expected loss: {money(result['total_expected_loss'])}; probabilities sum to {result['total_probability']:.3g}")
    if result["expected_shortfall_top_10pct"] is not None:
        print(f"expected shortfall (mean impact of the worst {result['shortfall_mass_used']:.0%} of probability): {money(result['expected_shortfall_top_10pct'])}")
    moves = result["rank_changes_under_error_factor"]
    print(f"ranking under a {result['error_factor']}x error on every probability below 0.1: " + ("stable" if not moves else ", ".join(f"{n} {a}->{b}" for n, a, b in moves)))
    print("Flags:")
    for flag in result["flags"] or ["none"]:
        print(f"  - {flag}")
    print("Limits:")
    for limit in result["limits"]:
        print(f"  - {limit}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("file", help="CSV file; '-' reads standard input")
    parser.add_argument("--ruin", type=float, help="impact at or above which the loss is unrecoverable")
    parser.add_argument("--error-factor", type=float, default=3.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.error_factor < 1:
        parser.error("--error-factor must be 1 or more")
    try:
        rows = load(args.file)
    except InputError as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 2
    result = analyse(rows, args.ruin, args.error_factor)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
