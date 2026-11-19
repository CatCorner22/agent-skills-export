import json
import re
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from lint_skills import GENERIC_SKILLS, ROOT, frontmatter, lint

sys.path.insert(0, str(ROOT / 'scripts'))
import build_dist


class PackTests(unittest.TestCase):
    def test_pack_frontmatter_bodies_citations_scopes_and_links(self):
        result = lint()
        self.assertEqual(result['skills'], 8)
        self.assertEqual(result['research_files_verified'], 74)
        self.assertEqual(result['result'], 'PASS')
        used = set()
        for path in (ROOT / 'skills').glob('*/SKILL.md'):
            used.update(re.findall(r'\bskill:([a-z0-9-]+)', path.read_text()))
        self.assertEqual(used, GENERIC_SKILLS)

    def test_frontmatter_rejects_invalid_yaml_subset(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'SKILL.md'
            for text in ['', '---\nname: x\ndescription: "unterminated\n---\n', 'name: x']:
                path.write_text(text)
                with self.assertRaises(ValueError):
                    frontmatter(path)

    def test_build_filters_and_guards(self):
        names = ['.venv', '.agent', '__pycache__', 'verification', 'probes', 'STATE.md', 'STEP1.md', 'skills', 'tests', 'references']
        self.assertEqual(build_dist.excluded(ROOT, names), set(names[:7]))
        self.assertEqual(build_dist.excluded(ROOT / 'data', ['cache']), {'cache'})
        for destination in [ROOT, ROOT / 'dist', ROOT.parent]:
            with self.assertRaises(ValueError):
                build_dist.build(destination)
        with TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                build_dist.build(directory)

    def test_fixture_citations_exist_in_bundled_report(self):
        ids = set(re.findall(r'\b[FM]\d+\b', (ROOT / 'references/research/report.md').read_text()))
        fixtures = list((ROOT / 'tests/fixtures').glob('*.json'))
        self.assertEqual(len(fixtures), 7)
        for path in fixtures:
            record = json.loads(path.read_text())
            self.assertFalse(set(re.findall(r'\b[FM]\d+\b', record['report_ref'])) - ids)


if __name__ == '__main__':
    unittest.main()
