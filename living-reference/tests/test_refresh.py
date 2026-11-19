"""Tests for refresh_reference.py. Run: python3 -m unittest discover tests"""
import os, sys, subprocess, tempfile, unittest, hashlib, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "scripts", "refresh_reference.py")
TEMPLATE = os.path.join(ROOT, "templates", "living-reference.template.md")
EXAMPLE = os.path.join(ROOT, "examples", "llm-failure-modes.reference.md")

DOC = """# Test reference
## [01] Attack sheet
- x
## [02] Contents
<!-- toc:start -->
<!-- toc:end -->
## [10] Topic A
### [10.01] Rule one is a full sentence
{{index: retrieval | RAG; see also: compaction}}
**Rule.** Something. [S1 at 4]
Last verified: 2026-11-01
### [10.02] Rule two
{{index: compaction}}
**Rule.** Else. [S2] [S9]
See §10.01 and §77.
Last verified: 2025-01-01
## [90] Sources
- [S1] Meta, Docs (2026). https://example.com/a
- [S2] Paper (2025).
- [S3] Orphan source.
## [91] Cite index
<!-- authorities:start -->
<!-- authorities:end -->
## [92] Index
<!-- index:start -->
<!-- index:end -->
## [99] Health
<!-- health:start -->
<!-- health:end -->
"""

def run(*args):
    return subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True)

class TestRefresh(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(); self.f = os.path.join(self.tmp, "ref.md"); open(self.f, "w").write(DOC)
    def tearDown(self): shutil.rmtree(self.tmp, ignore_errors=True)
    def text(self): return open(self.f).read()
    def test_generates_all_four_blocks(self):
        r = run(self.f); self.assertEqual(r.returncode, 0, r.stderr); t = self.text()
        self.assertIn("10.01 Rule one", t.split("toc:start")[1].split("toc:end")[0])
        auth = t.split("authorities:start")[1].split("authorities:end")[0]; self.assertIn("[S1]", auth); self.assertIn("10.01", auth)
        idx = t.split("index:start")[1].split("index:end")[0]; self.assertIn("retrieval", idx); self.assertIn("RAG", idx); self.assertIn("see also", idx.lower())
        health = t.split("health:start")[1].split("health:end")[0]
        for s in ("S9", "§77", "S3", "10.02"): self.assertIn(s, health)   # undefined cite, broken ref, orphan source, stale section
    def test_idempotent(self):
        hashes = []
        for _ in range(3):
            run(self.f); hashes.append(hashlib.sha256(self.text().encode()).hexdigest())
        self.assertEqual(len(set(hashes)), 1)
    def test_check_fails_on_findings_and_passes_when_clean(self):
        r = run(self.f, "--check"); self.assertNotEqual(r.returncode, 0)
        clean = DOC.replace("[S9]", "").replace("§77", "§10.02").replace("- [S3] Orphan source.\n", "").replace("2025-01-01", "2026-11-01")
        open(self.f, "w").write(clean); run(self.f)
        r = run(self.f, "--check"); self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
    def test_template_and_example_refresh_cleanly(self):
        for src in (TEMPLATE, EXAMPLE):
            dst = os.path.join(self.tmp, os.path.basename(src)); shutil.copy(src, dst)
            r = run(dst); self.assertEqual(r.returncode, 0, r.stderr)
            h1 = hashlib.sha256(open(dst, "rb").read()).hexdigest(); run(dst)
            self.assertEqual(h1, hashlib.sha256(open(dst, "rb").read()).hexdigest(), src)

if __name__ == "__main__": unittest.main()
