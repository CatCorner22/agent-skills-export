"""Lint the pack's restricted valid YAML frontmatter, scope references and citations."""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERIC_SKILLS = {'tool-call-validator', 'completion-evidence-gate', 'context-budget-governor',
                  'model-sanity-regression', 'claim-evidence-pairing', 'premise-check', 'ask-or-assume',
                  'scope-and-blast-radius-check', 'inventory-before-fetch'}
PACK_SKILLS = {'muse-abstention-recovery', 'muse-agent-action-gate', 'muse-injection-hygiene',
               'muse-privacy-minimization', 'muse-api-integration-check', 'muse-benchmark-skepticism',
               'muse-long-session-hygiene', 'muse-verification-pass'}


def frontmatter(path):
    text = path.read_text()
    match = re.fullmatch(r'---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]*")\n---\n([\s\S]*)', text)
    if not match:
        raise ValueError(f'{path}: expected name and JSON-quoted description (valid YAML string subset)')
    name, quoted, body = match.groups()
    description = json.loads(quoted)
    if not isinstance(description, str):
        raise ValueError('description must be a YAML string')
    return name, description, body


def lint(root=ROOT):
    paths = sorted((root / 'skills').glob('*/SKILL.md'))
    if {p.parent.name for p in paths} != PACK_SKILLS:
        raise ValueError('Expected exactly the eight requested skills')
    if list(root.rglob('README*')):
        raise ValueError('Pack must be README-free')
    report = (root / 'references/research/report.md').read_text()
    report_ids = set(re.findall(r'\b[FM]\d+\b', report))
    results = []
    for path in paths:
        name, description, body = frontmatter(path)
        if name != path.parent.name:
            raise ValueError('Frontmatter name does not match directory: ' + name)
        if len(description) > 400 or not description.endswith('.') or len(re.findall(r'[.!?](?:\s|$)', description)) != 1:
            raise ValueError('Description must be one sentence <=400 characters: ' + name)
        if not all(trigger in description for trigger in ('Muse', 'Muse Spark', 'Muse Wonder', 'Meta AI', 'Meta Model API')):
            raise ValueError('Missing model/product trigger: ' + name)
        if 'Scope boundary:' not in description:
            raise ValueError('Missing scope boundary: ' + name)
        scopes = set(re.findall(r'\bskill:([a-z0-9-]+)', description + '\n' + body))
        if not scopes or scopes - GENERIC_SKILLS:
            raise ValueError('Unknown existing skill reference: ' + name)
        if len(body.splitlines()) >= 150:
            raise ValueError('Body must be <150 lines: ' + name)
        if '## When it fires' not in body or '## Steps' not in body or '## Evidence' not in body:
            raise ValueError('Missing operational section: ' + name)
        steps = re.findall(r'^(\d+)\. (.+)$', body, re.M)
        if not steps or [int(n) for n, _ in steps] != list(range(1, len(steps) + 1)) or any('must' not in s.lower() for _, s in steps):
            raise ValueError('Steps must be numbered and checkable with must/must not: ' + name)
        ids = set(re.findall(r'\b[FM]\d+\b', body))
        if not ids or ids - report_ids:
            raise ValueError('Cited failure ID missing from report: ' + name)
        evidence = body.split('## Evidence', 1)[1]
        if not re.search(r'Established|Probable|Single-source|Contested', evidence):
            raise ValueError('Missing report confidence label: ' + name)
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            if not re.match(r'[a-z]+:', link) and not (path.parent / link.split('#')[0]).is_file():
                raise ValueError('Missing linked file: ' + link)
        results.append(dict(name=name, body_lines=len(body.splitlines()), description_chars=len(description)))
    archive = root / 'references/research'
    manifest = json.loads((archive / 'INPUT_MANIFEST.json').read_text())
    for record in manifest['files']:
        if hashlib.sha256((archive / record['path']).read_bytes()).hexdigest() != record['sha256']:
            raise ValueError('Research input differs from supplied snapshot: ' + record['path'])
    return dict(result='PASS', skills=len(paths), research_files_verified=len(manifest['files']), details=results)


if __name__ == '__main__':
    print(json.dumps(lint(), indent=2))
