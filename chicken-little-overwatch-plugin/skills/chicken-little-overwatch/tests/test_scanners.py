"""Regression tests for the Chicken Little Overwatch scanners. Run: python3 -m unittest discover -s tests"""
import io
import os
import re
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")
AV = os.path.join(SCRIPTS, "av_scan.py")
WL = os.path.join(SCRIPTS, "watchlist_scan.py")

PASSIVES = [
    "The form was signed by the patient.",
    "Your test isn't covered.",
    "The consent must be signed before surgery.",
    "The results have been sent to your doctor.",
    "The sample is being tested.",
    "You will be told the results.",
    "Was the form signed?",
    "If you get hurt, call us.",
    "Your records remain protected by law.",
    "Have your blood tested.",
    "The dressing needs changing.",
    "Bring the form signed by the patient.",
    "If swallowed, call poison control.",
    "Measure with the cup provided.",
    "Nothing was done.",
    "The policy was\nwritten by the board.",
]
ACTIVES = [
    "The nurse checks your blood pressure.",
    "Take 1 tablet in the morning.",
    "Call us if you have a fever.",
    "Your doctor will adjust the dose.",
    "The pharmacy closes at 6 p.m.",
    "The nurse has given you the dose.",
    "Your appointment is on 3 March.",
    "Bring your insurance card.",
    "Do not drive after you take this medicine.",
    "Tell us at least 2 days before you travel.",
]


def run(script, *args, stdin=None):
    proc = subprocess.run([sys.executable, script, *args], input=stdin, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def write(text, suffix=".md", raw=None):
    handle = tempfile.NamedTemporaryFile("wb", suffix=suffix, delete=False)
    handle.write(raw if raw is not None else text.encode("utf-8"))
    handle.close()
    return handle.name


class ActiveVoiceScanner(unittest.TestCase):
    def test_catches_every_passive_in_the_set(self):
        for sentence in PASSIVES:
            code, out, _ = run(AV, "-", stdin=sentence + "\n")
            self.assertEqual(code, 1, f"missed passive: {sentence!r}")

    def test_passes_every_active_in_the_set(self):
        for sentence in ACTIVES:
            code, out, _ = run(AV, "-", stdin=sentence + "\n")
            self.assertEqual(code, 0, f"false alarm on active: {sentence!r}\n{out}")

    def test_passive_across_a_line_break_reports_its_start_line(self):
        code, out, _ = run(AV, "-", stdin="Intro.\n\nThe dose was\nchanged yesterday.\n")
        self.assertEqual(code, 1)
        self.assertIn("-:3:", out)

    def test_front_matter_is_skipped_only_when_it_closes(self):
        self.assertEqual(run(AV, "-", stdin="---\ntitle: x\nnote: was done\n---\nThe nurse acts.\n")[0], 0)
        code, out, err = run(AV, "-", stdin="---\nThe form was signed.\n")
        self.assertEqual(code, 1)
        self.assertIn("WARNING", err)

    def test_horizontal_rule_at_top_does_not_hide_text(self):
        code, _, _ = run(AV, "-", stdin="---\n\nThe form was signed.\n\n---\n")
        self.assertEqual(code, 1)

    def test_closed_fence_is_skipped_and_unclosed_fence_is_scanned(self):
        self.assertEqual(run(AV, "-", stdin="```\nx was done\n```\nThe nurse acts.\n")[0], 0)
        self.assertEqual(run(AV, "--include-code", "-", stdin="```\nx was done\n```\n")[0], 1)
        code, _, err = run(AV, "-", stdin="```\nIt was done.\n")
        self.assertEqual(code, 1)
        self.assertIn("never closes", err)

    def test_markers(self):
        mention = "<!-- av:mention -->\nIt was done.\n<!-- /av:mention -->\n"
        self.assertEqual(run(AV, "-", stdin=mention)[0], 0)
        self.assertEqual(run(AV, "--strict", "-", stdin=mention)[0], 1)
        verbatim = "<!-- av:verbatim -->\nTHIS NOTICE DESCRIBES HOW MEDICAL INFORMATION ABOUT YOU MAY BE USED\n<!-- /av:verbatim -->\n"
        code, out, err = run(AV, "--strict", "-", stdin=verbatim)
        self.assertEqual(code, 0)
        self.assertIn("verbatim=1", err)

    def test_unclosed_marker_blocks(self):
        code, _, err = run(AV, "-", stdin="<!-- av:verbatim -->\nThe nurse acts.\n")
        self.assertEqual(code, 1)
        self.assertIn("never closes", err)

    def test_unreadable_inputs_exit_2_without_a_traceback(self):
        folder = tempfile.mkdtemp()
        latin = write("", raw="caf\xe9 was closed.\n".encode("latin-1"))
        for target in (os.path.join(folder, "missing.md"), folder, latin):
            code, _, err = run(AV, target)
            self.assertEqual(code, 2, target)
            self.assertNotIn("Traceback", err)

    def test_bom_and_crlf(self):
        path = write("", raw="\ufeffThe form was signed.\r\nThe nurse acts.\r\n".encode("utf-8"))
        code, out, _ = run(AV, path)
        self.assertEqual(code, 1)
        self.assertIn(":1:", out)

    def test_empty_file_passes(self):
        self.assertEqual(run(AV, write(""))[0], 0)


class WatchlistScanner(unittest.TestCase):
    def test_flags_banned_modals_and_vague_words(self):
        code, out, _ = run(WL, "--fail", "-", stdin="Staff should call promptly and/or as needed.\n")
        self.assertEqual(code, 1)
        for label in ("R1/lexicon", "R9 and/or", "Vague standard"):
            self.assertIn(label, out)

    def test_default_exit_is_0_even_with_hits(self):
        self.assertEqual(run(WL, "-", stdin="You should go.\n")[0], 0)

    def test_do_not_use_and_dose_format(self):
        _, out, _ = run(WL, "-", stdin="Give 10 U daily. Give 5.0 mg. Give .5 mg QD.\n")
        self.assertEqual(run(WL, "-", stdin="Take it Q.D. today. Take it Q.O.D. later.\n")[1].count("QD/QOD"), 2)
        for label in ("U/IU", "trailing zero", "leading zero", "QD/QOD"):
            self.assertIn(label, out)

    def test_one_space_rule_skips_abbreviations(self):
        _, out, _ = run(WL, "--no-length", "-", stdin="See Dr. Lee today.  Then rest.\n")
        self.assertNotIn("1 space", out)
        _, out, _ = run(WL, "--no-length", "-", stdin="Rest today. Then call.\n")
        self.assertIn("1 space", out)
        _, out, _ = run(WL, "--no-length", "--no-spacing", "-", stdin="Rest today. Then call.\n")
        self.assertNotIn("1 space", out)

    def test_wrapped_lines_do_not_create_spacing_hits(self):
        _, out, _ = run(WL, "--no-length", "-", stdin="Rest today.\nThen call.\n")
        self.assertNotIn("1 space", out)

    def test_length_limit_counts_a_wrapped_sentence_once(self):
        sentence = " ".join(["word"] * 20) + "\n" + " ".join(["word"] * 10) + ".\n"
        _, out, _ = run(WL, "--limit", "25", "-", stdin=sentence)
        self.assertIn("S5 length 30 > 25", out)
        self.assertEqual(out.count("S5 length"), 1)

    def test_mention_zone_skipped_unless_strict(self):
        text = "<!-- av:mention -->\nYou should go.\n<!-- /av:mention -->\n"
        self.assertNotIn("R1/lexicon", run(WL, "-", stdin=text)[1])
        self.assertIn("R1/lexicon", run(WL, "--strict", "-", stdin=text)[1])

    def test_bad_limit_and_unreadable_input(self):
        self.assertEqual(run(WL, "--limit", "0", "-", stdin="x\n")[0], 2)
        code, _, err = run(WL, "/no/such/file.md")
        self.assertEqual(code, 2)
        self.assertNotIn("Traceback", err)


class SharedReader(unittest.TestCase):
    def test_reader_blocks_match(self):
        pattern = re.compile(r"# --- Markdown reader.*?# --- end Markdown reader ---", re.S)
        blocks = [pattern.search(read(p)).group(0) for p in (AV, WL)]
        self.assertEqual(blocks[0], blocks[1])

    def test_av_patterns_match_the_writing_standard(self):
        standard = read(os.path.join(os.path.dirname(HERE), "references", "one-way-optimal-language.md"))
        script = read(AV)
        block = re.compile(r"P = \(.*?\n\]\n", re.S)
        self.assertEqual(block.search(standard).group(0), block.search(script).group(0))


if __name__ == "__main__":
    unittest.main()


class SeededFixture(unittest.TestCase):
    FIXTURE = os.path.join(HERE, "fixtures", "seeded-policy.md")

    def test_scanners_find_the_seeded_writing_defects(self):
        code, out, _ = run(AV, self.FIXTURE)
        self.assertEqual(code, 1)
        self.assertIn("seeded-policy.md:9:", out)
        _, out, _ = run(WL, "--no-length", "--no-spacing", self.FIXTURE)
        for line, label in ((10, "R1/lexicon"), (10, "Vague standard"), (10, "R9 and/or"), (11, "R13 time"), (14, "U/IU"), (14, "QD/QOD")):
            self.assertRegex(out, rf"seeded-policy\.md:{line}: \[[^\]]*{re.escape(label)}")

    def test_heading_does_not_join_the_next_line(self):
        code, out, _ = run(AV, "-", stdin="# Results were\nsigned forms go here.\n")
        self.assertEqual(code, 0, out)
