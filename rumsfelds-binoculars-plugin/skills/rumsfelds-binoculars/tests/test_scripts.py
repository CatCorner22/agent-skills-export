"""Regression tests for the Rumsfeld's Binoculars scripts. Run: python3 -m unittest discover -s tests"""
import json
import os
import random
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")
TAIL = os.path.join(SCRIPTS, "tail_check.py")
EXPOSURE = os.path.join(SCRIPTS, "exposure_table.py")
FIXTURE = os.path.join(HERE, "fixtures", "scenarios.csv")


def run(script, *args, stdin=None):
    proc = subprocess.run([sys.executable, script, *args], input=stdin, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def series(generator, n, seed):
    rng = random.Random(seed)
    return "\n".join(str(generator(rng)) for _ in range(n)) + "\n"


class TailCheck(unittest.TestCase):
    def test_pareto_sample_reads_as_heavy_with_the_right_index(self):
        text = series(lambda r: (1 - r.random()) ** (-1 / 1.5), 4000, 1)
        code, out, _ = run(TAIL, "--json", "--bootstrap", "20", "-", stdin=text)
        self.assertEqual(code, 0)
        report = json.loads(out)["series"]
        self.assertIn("heavy", report["tail_class"])
        alphas = [v["alpha"] for v in report["hill_alpha"].values()]
        self.assertTrue(all(1.2 < a < 1.8 for a in alphas), alphas)
        xi = report["peaks_over_threshold"]["xi"]
        self.assertTrue(0.45 < xi < 0.9, xi)

    def test_gaussian_sample_reads_as_thin(self):
        text = series(lambda r: r.gauss(100, 10), 3000, 2)
        code, out, _ = run(TAIL, "--json", "--bootstrap", "20", "-", stdin=text)
        report = json.loads(out)["series"]
        self.assertEqual(report["flags"], [])
        self.assertLess(report["peaks_over_threshold"]["xi"], 0.1)
        self.assertIn("not proof of a thin tail", report["tail_class"])

    def test_exponential_sample_has_xi_near_zero_in_both_fits(self):
        text = series(lambda r: r.expovariate(1.0), 3000, 3)
        report = json.loads(run(TAIL, "--json", "--bootstrap", "20", "-", stdin=text)[1])["series"]
        pot = report["peaks_over_threshold"]
        self.assertLess(abs(pot["xi"]), 0.2)
        self.assertLess(abs(pot["pwm_cross_check"]["xi"]), 0.2)

    def test_zero_event_bounds(self):
        code, out, _ = run(TAIL, "--zero-events", "300", "--json")
        self.assertEqual(code, 0)
        bounds = json.loads(out)["zero_events"]
        self.assertAlmostEqual(bounds["rule_of_three_95pct_upper_bound"], 0.01)
        self.assertAlmostEqual(bounds["laplace_point_estimate"], 1 / 302)

    def test_small_sample_is_labelled_undetermined(self):
        report = json.loads(run(TAIL, "--json", "-", stdin="1\n2\n3\n4\n50\n")[1])["series"]
        self.assertIn("too small", report["tail_class"])

    def test_csv_column_and_losses(self):
        csv_text = "date,return\n2020-01-01,0.01\n2020-01-02,-0.05\n2020-01-03,-0.02\n2020-01-04,0.03\n2020-01-05,-0.10\n"
        code, out, _ = run(TAIL, "--json", "--column", "return", "--losses", "-", stdin=csv_text)
        self.assertEqual(code, 0)
        report = json.loads(out)["series"]
        self.assertEqual(report["n"], 3)
        self.assertAlmostEqual(report["max"], 0.10)
        code, _, err = run(TAIL, "--column", "nope", "-", stdin=csv_text)
        self.assertEqual(code, 2)
        self.assertIn("not found", err)

    def test_bad_inputs_exit_2_without_traceback(self):
        for args in (["/no/such/file"], [tempfile.mkdtemp()]):
            code, _, err = run(TAIL, *args)
            self.assertEqual(code, 2)
            self.assertNotIn("Traceback", err)
        code, _, err = run(TAIL, "-", stdin="apple\n")
        self.assertEqual(code, 2)
        self.assertIn("fewer than 2", err)


class ExposureTable(unittest.TestCase):
    def test_fixture_report(self):
        code, out, _ = run(EXPOSURE, "--ruin", "2000000", "--json", FIXTURE)
        self.assertEqual(code, 0)
        result = json.loads(out)
        by_name = {r["scenario"]: r for r in result["rows"]}
        self.assertEqual(by_name["Data breach of patient records"]["class"], "RUIN")
        self.assertEqual(by_name["Building fire"]["class"], "RUIN")
        self.assertEqual(by_name["Payroll error"]["class"], "ROUTINE")
        self.assertEqual(by_name["Owner cannot work for 6 months"]["class"], "HIGH-CONSEQUENCE, LOW-FREQUENCY")
        self.assertAlmostEqual(result["total_expected_loss"], 0.05 * 400000 + 0.02 * 2500000 + 0.3 * 20000 + 0.1 * 150000 + 0.004 * 900000)
        flags = "\n".join(result["flags"])
        self.assertIn("probability 0", flags)
        self.assertIn("blind one-way door", flags)
        self.assertIn("more precision", flags)
        self.assertTrue(result["rank_changes_under_error_factor"])

    def test_expected_shortfall_uses_the_worst_mass(self):
        text = "scenario,probability,impact\nA,0.05,100\nB,0.05,50\nC,0.9,1\n"
        result = json.loads(run(EXPOSURE, "--json", "-", stdin=text)[1])
        self.assertAlmostEqual(result["expected_shortfall_top_10pct"], 75.0)

    def test_percent_and_sum_warning(self):
        text = "scenario,probability,impact\nA,60%,10\nB,0.7,10\n"
        code, out, _ = run(EXPOSURE, "-", stdin=text)
        self.assertEqual(code, 0)
        self.assertIn("probabilities sum to 1.30", out)

    def test_invalid_rows_exit_2(self):
        for text in ("scenario,impact\nA,1\n", "scenario,probability,impact\nA,1.5,10\n", "scenario,probability,impact\nA,x,10\n", "scenario,probability,impact\nA,0.1,-5\n"):
            code, _, err = run(EXPOSURE, "-", stdin=text)
            self.assertEqual(code, 2, text)
            self.assertNotIn("Traceback", err)


if __name__ == "__main__":
    unittest.main()
