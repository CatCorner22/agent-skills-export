#!/usr/bin/env python3
"""Tail check for Rumsfeld's Binoculars: does this data come from a thin-tailed or a heavy-tailed world?

Reads one numeric series (losses, magnitudes, delays, costs, returns) and reports the
evidence for heavy tails, a peaks-over-threshold fit, and return levels, with the limits
that each number carries. It uses only the Python standard library.

Usage:
  python3 tail_check.py FILE [FILE ...]            one number per line, or CSV with --column
  python3 tail_check.py --column loss data.csv     pick a CSV column by name or 0-based index
  cat series.txt | python3 tail_check.py -         read standard input
  python3 tail_check.py --zero-events 400          only the "no event in 400 trials" bounds

Options:
  --losses             treat negative values as losses (flip the sign) and drop the rest
  --absolute           use absolute values
  --threshold-quantile Q  peaks-over-threshold threshold (default 0.90)
  --return-periods LIST   return periods in observations (default 10,100,1000)
  --seed N             bootstrap seed (default 7); --bootstrap N resamples (default 200)
  --json               machine-readable output
Exit: 0 on a report; 2 when the input cannot be read or holds fewer than 2 numbers.

What the report cannot tell you: a sample never contains the event that is larger than every
event in it. Treat "no sign of heavy tails" as "no sign in this sample", not as safety.
"""
import argparse
import csv
import json
import math
import random
import statistics
import sys


class InputError(Exception):
    pass


def read_numbers(path, column=None):
    if path == "-":
        text = sys.stdin.read()
    else:
        try:
            with open(path, encoding="utf-8-sig") as handle:
                text = handle.read()
        except FileNotFoundError:
            raise InputError(f"{path}: no such file")
        except IsADirectoryError:
            raise InputError(f"{path}: is a folder")
        except UnicodeDecodeError:
            raise InputError(f"{path}: not UTF-8 text")
    rows = list(csv.reader(text.splitlines()))
    values, skipped = [], 0
    if column is not None and rows:
        header = [cell.strip() for cell in rows[0]]
        if column in header:
            index, rows = header.index(column), rows[1:]
        elif column.isdigit() and int(column) < len(header):
            index = int(column)
        else:
            raise InputError(f"{path}: column {column!r} not found in {header}")
        cells = [row[index] for row in rows if len(row) > index]
    else:
        cells = [cell for row in rows for cell in row]
    for cell in cells:
        try:
            value = float(cell.strip().replace(",", ""))
            if math.isfinite(value):
                values.append(value)
            else:
                skipped += 1
        except ValueError:
            skipped += 1
    return values, skipped


def moments(xs):
    n = len(xs)
    mean = statistics.fmean(xs)
    sd = statistics.pstdev(xs) if n > 1 else 0.0
    if sd == 0:
        return mean, sd, 0.0, 0.0
    skew = sum(((x - mean) / sd) ** 3 for x in xs) / n
    kurt = sum(((x - mean) / sd) ** 4 for x in xs) / n - 3.0
    return mean, sd, skew, kurt


def hill(xs_desc, k):
    """Hill tail-index estimate from the k largest positive values (sorted descending)."""
    top = [x for x in xs_desc[:k + 1] if x > 0]
    if len(top) < k + 1 or top[k] <= 0:
        return None
    total = sum(math.log(top[i] / top[k]) for i in range(k))
    return k / total if total > 0 else None


def gpd_pwm(excesses):
    """Generalized Pareto fit by probability-weighted moments (Hosking and Wallis 1987).

    Returns (shape xi, scale sigma). Reliable for xi below about 0.5 and n above about 30.
    """
    ys = sorted(excesses)
    n = len(ys)
    if n < 2:
        return None, None
    a0 = statistics.fmean(ys)
    a1 = sum(((n - 1 - i) / (n - 1)) * y for i, y in enumerate(ys)) / n
    denominator = a0 - 2 * a1
    if denominator <= 0:
        return None, None
    xi = 2 - a0 / denominator
    sigma = 2 * a0 * a1 / denominator
    return xi, sigma


def gpd_mle(excesses):
    """Generalized Pareto fit by maximum likelihood with the profile in tau = xi / sigma (Grimshaw 1993).

    Returns (shape xi, scale sigma). Works for any xi; needs about 20 exceedances to mean much.
    """
    ys = [y for y in excesses if y > 0]
    n = len(ys)
    if n < 5:
        return None, None
    top = max(ys)

    def profile(tau):
        if tau == 0:
            return -n * math.log(statistics.fmean(ys)) - n
        logs = [math.log1p(tau * y) for y in ys]
        xi = sum(logs) / n
        if xi == 0 or tau * top <= -1:
            return -math.inf
        sigma = xi / tau
        if sigma <= 0:
            return -math.inf
        return -n * math.log(sigma) - (1 + 1 / xi) * sum(logs)

    low, high = -0.999 / top, 50.0 / statistics.fmean(ys)
    grid = [low + (high - low) * i / 400 for i in range(401)]
    best = max(grid, key=profile)
    index = grid.index(best)
    a, b = grid[max(0, index - 1)], grid[min(len(grid) - 1, index + 1)]
    golden = (math.sqrt(5) - 1) / 2
    for _ in range(80):
        c, d = b - golden * (b - a), a + golden * (b - a)
        if profile(c) < profile(d):
            a = c
        else:
            b = d
    tau = (a + b) / 2
    if abs(tau) < 1e-12:
        return 0.0, statistics.fmean(ys)
    xi = sum(math.log1p(tau * y) for y in ys) / n
    return xi, xi / tau


def return_level(u, xi, sigma, zeta, period):
    if xi is None or sigma is None or period * zeta <= 1:
        return None  # a period this short falls inside the body of the data, below the threshold
    if abs(xi) < 1e-9:
        return u + sigma * math.log(period * zeta)
    return u + sigma / xi * ((period * zeta) ** xi - 1)


def analyse(values, threshold_quantile, periods, seed, resamples):
    n = len(values)
    xs = sorted(values)
    desc = xs[::-1]
    mean, sd, skew, kurt = moments(xs)
    report = {
        "n": n, "min": xs[0], "max": xs[-1], "mean": mean, "median": statistics.median(xs),
        "sd": sd, "skewness": skew, "excess_kurtosis": kurt, "flags": [], "limits": [],
    }
    if n < 30:
        report["limits"].append(f"n={n} is small; every tail estimate below is unstable, and the sample is unlikely to hold a rare event at all")
    positives = [x for x in desc if x > 0]
    total = sum(positives)
    if total > 0 and len(positives) >= 20:
        top1 = sum(positives[:max(1, len(positives) // 100)]) / total
        top5 = sum(positives[:max(1, len(positives) // 20)]) / total
        report["share_top_1pct"], report["share_top_5pct"] = top1, top5
        if top5 > 0.5:
            report["flags"].append(f"the top 5% of observations carry {top5:.0%} of the total: a few events dominate")
    if len(positives) >= 20:
        ms = {p: max(x ** p for x in positives) / sum(x ** p for x in positives) for p in (1, 2, 4)}
        report["max_to_sum_ratio"] = ms
        if ms[2] > 0.2:
            report["flags"].append(f"max-to-sum ratio for p=2 is {ms[2]:.2f}: one observation drives the variance, a heavy-tail sign (Taleb 2020)")
    hills = {}
    for share in (0.05, 0.10, 0.20):
        k = int(len(positives) * share)
        if k >= 5:
            alpha = hill(positives, k)
            if alpha:
                hills[f"k={k}"] = {"alpha": alpha, "se_approx": alpha / math.sqrt(k)}
    report["hill_alpha"] = hills
    if hills:
        alphas = [v["alpha"] for v in hills.values()]
        if min(alphas) < 2:
            report["flags"].append(f"Hill tail index as low as {min(alphas):.2f}: below 2, the variance does not exist and sample averages converge slowly")
        if min(alphas) < 1:
            report["flags"].append("Hill tail index below 1: the mean itself does not exist; no average of this data is meaningful")
    thresholds = [xs[int(n * q)] for q in (0.5, 0.75, 0.9) if int(n * q) < n - 5]
    mean_excess = []
    for u in thresholds:
        exc = [x - u for x in xs if x > u]
        if len(exc) >= 5:
            mean_excess.append({"threshold": u, "count": len(exc), "mean_excess": statistics.fmean(exc)})
    report["mean_excess"] = mean_excess
    if len(mean_excess) >= 3 and mean_excess[0]["mean_excess"] < mean_excess[1]["mean_excess"] < mean_excess[2]["mean_excess"]:
        report["flags"].append("the mean excess grows with the threshold: the bigger the loss already is, the bigger the expected overshoot, a heavy-tail sign")
    u = xs[int(n * threshold_quantile)]
    exc = [x - u for x in xs if x > u]
    pot = {"threshold": u, "exceedances": len(exc)}
    if len(exc) >= 10:
        xi, sigma = gpd_mle(exc)
        pwm_xi, pwm_sigma = gpd_pwm(exc)
        pot.update({"xi": xi, "sigma": sigma, "method": "maximum likelihood",
                    "pwm_cross_check": {"xi": pwm_xi, "sigma": pwm_sigma} if pwm_xi is not None else "not available (needs xi below 0.5)"})
        if xi is not None:
            zeta = len(exc) / n
            pot["return_levels"] = {str(T): return_level(u, xi, sigma, zeta, T) for T in periods}
            rng = random.Random(seed)
            boots = []
            for _ in range(resamples):
                sample = [rng.choice(exc) for _ in exc]
                bxi, bsigma = gpd_mle(sample)
                if bxi is not None:
                    boots.append({str(T): return_level(u, bxi, bsigma, zeta, T) for T in periods} | {"xi": bxi})
            if boots:
                def band(key):
                    vals = sorted(b[key] for b in boots if b.get(key) is not None)
                    return (vals[int(0.05 * len(vals))], vals[min(len(vals) - 1, int(0.95 * len(vals)))]) if vals else None
                pot["xi_90pct_band"] = band("xi")
                pot["return_level_90pct_bands"] = {str(T): band(str(T)) for T in periods}
            if xi > 0.5:
                pot["warning"] = "xi above 0.5: the variance of the exceedances does not exist; return levels far beyond the data carry very wide error"
            if xi > 0:
                report["flags"].append(f"peaks-over-threshold shape xi={xi:.2f} is positive: a Pareto-type tail with no upper limit in the model")
        else:
            pot["warning"] = "the fit failed; the exceedances look degenerate"
    else:
        pot["warning"] = f"only {len(exc)} exceedances above the {threshold_quantile:.0%} quantile; a fit needs at least 10"
    report["peaks_over_threshold"] = pot
    report["limits"] += [
        "the largest event in the sample bounds nothing; the next event can exceed it",
        "every estimate assumes that the process stays the same over time (stationarity); regime change breaks that assumption",
        "if the series mixes units, periods, or populations, split it before you read the tail",
    ]
    heavy = len(report["flags"])
    report["tail_class"] = ("undetermined: sample too small" if n < 30 else
                            "heavy-tail signs present" if heavy >= 2 else
                            "one heavy-tail sign; treat as heavy until more data says otherwise" if heavy == 1 else
                            "no heavy-tail sign in this sample (not proof of a thin tail)")
    return report


def zero_event_bounds(trials):
    return {
        "trials": trials,
        "rule_of_three_95pct_upper_bound": 3.0 / trials,
        "laplace_point_estimate": 1.0 / (trials + 2),
        "note": "With 0 events in n independent trials, the 95% upper bound on the per-trial probability is about 3/n (Hanley and Lippman-Hand 1983). It says nothing about the size of the event when it comes.",
    }


def fmt(value):
    if isinstance(value, float):
        return f"{value:.4g}"
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(fmt(v) for v in value) + "]"
    return str(value)


def print_report(report, zero):
    if zero:
        print("Zero-event bounds")
        for key, value in zero.items():
            print(f"  {key}: {fmt(value)}")
    if not report:
        return
    print(f"Tail class: {report['tail_class']}")
    print(f"n={report['n']} min={fmt(report['min'])} median={fmt(report['median'])} mean={fmt(report['mean'])} max={fmt(report['max'])} sd={fmt(report['sd'])}")
    print(f"skewness={fmt(report['skewness'])} excess kurtosis={fmt(report['excess_kurtosis'])}")
    if "share_top_5pct" in report:
        print(f"share of total in top 1% / top 5%: {report['share_top_1pct']:.1%} / {report['share_top_5pct']:.1%}")
    if "max_to_sum_ratio" in report:
        print("max-to-sum ratios: " + ", ".join(f"p={p}: {v:.3f}" for p, v in report["max_to_sum_ratio"].items()))
    for key, value in report["hill_alpha"].items():
        print(f"Hill alpha at {key}: {value['alpha']:.2f} (approx. SE {value['se_approx']:.2f})")
    for row in report["mean_excess"]:
        print(f"mean excess above {fmt(row['threshold'])} (n={row['count']}): {fmt(row['mean_excess'])}")
    pot = report["peaks_over_threshold"]
    print(f"Peaks over threshold u={fmt(pot['threshold'])}, exceedances={pot['exceedances']}")
    if "xi" in pot and pot["xi"] is not None:
        print(f"  GPD ({pot['method']}) shape xi={pot['xi']:.3f} scale sigma={pot['sigma']:.4g}" + (f" xi 90% band={fmt(pot['xi_90pct_band'])}" if pot.get("xi_90pct_band") else ""))
        cross = pot.get("pwm_cross_check")
        print(f"  PWM cross-check: xi={cross['xi']:.3f} sigma={cross['sigma']:.4g}" if isinstance(cross, dict) else f"  PWM cross-check: {cross}")
        for T, level in pot.get("return_levels", {}).items():
            band = pot.get("return_level_90pct_bands", {}).get(T)
            if level is None:
                print(f"  return level, 1 in {T} observations: below the threshold; read it from the data directly")
            else:
                print(f"  return level, 1 in {T} observations: {fmt(level)}" + (f"  (90% band {fmt(band)})" if band else ""))
    if pot.get("warning"):
        print(f"  warning: {pot['warning']}")
    print("Flags:")
    for flag in report["flags"] or ["none"]:
        print(f"  - {flag}")
    print("Limits:")
    for limit in report["limits"]:
        print(f"  - {limit}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("files", nargs="*", help="input files; '-' reads standard input")
    parser.add_argument("--column", help="CSV column name or 0-based index")
    parser.add_argument("--losses", action="store_true", help="keep negative values as positive losses, drop the rest")
    parser.add_argument("--absolute", action="store_true", help="use absolute values")
    parser.add_argument("--threshold-quantile", type=float, default=0.90)
    parser.add_argument("--return-periods", default="10,100,1000")
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--bootstrap", type=int, default=200)
    parser.add_argument("--zero-events", type=int, help="trials with no event, for the rule-of-three bound")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if not args.files and args.zero_events is None:
        parser.error("give at least one file, '-', or --zero-events N")
    if not 0.5 <= args.threshold_quantile < 1:
        parser.error("--threshold-quantile must lie in [0.5, 1)")
    if args.zero_events is not None and args.zero_events < 1:
        parser.error("--zero-events must be 1 or more")
    try:
        periods = [int(p) for p in args.return_periods.split(",") if p.strip()]
    except ValueError:
        parser.error("--return-periods must be integers separated by commas")
    values, skipped = [], 0
    for path in args.files:
        try:
            got, bad = read_numbers(path, args.column)
        except InputError as error:
            print(f"ERROR {error}", file=sys.stderr)
            return 2
        values += got
        skipped += bad
    if args.losses:
        values = [-x for x in values if x < 0]
    elif args.absolute:
        values = [abs(x) for x in values]
    report = None
    if args.files:
        if len(values) < 2:
            print(f"ERROR fewer than 2 numeric values found ({skipped} cells skipped)", file=sys.stderr)
            return 2
        report = analyse(values, args.threshold_quantile, periods, args.seed, args.bootstrap)
        report["skipped_cells"] = skipped
    zero = zero_event_bounds(args.zero_events) if args.zero_events else None
    if args.json:
        print(json.dumps({"series": report, "zero_events": zero}, indent=2))
    else:
        print_report(report, zero)
        if skipped:
            print(f"({skipped} non-numeric cells skipped)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
