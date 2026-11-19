"""Copy the eight-skill plugin and its offline evidence snapshot into plugins-dist."""

import argparse
import datetime
import hashlib
import json
import os
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def excluded(directory, names):
    return {n for n in names if n in {'.venv', '.agent', '.git', '__pycache__', 'verification', 'probes', 'STATE.md'}
            or n.startswith('STEP') or n.endswith(('.pyc', '.pyo'))
            or (n == 'cache' and Path(directory).name == 'data')}


def build(destination):
    destination = Path(destination).expanduser().resolve()
    if destination == ROOT or destination in ROOT.parents or destination.is_relative_to(ROOT):
        raise ValueError('Destination must be outside source and its ancestors')
    if not destination.parent.is_dir():
        raise ValueError('Destination parent must already exist')
    if destination.exists() and not (destination / '.devin-plugin/plugin.json').is_file():
        raise ValueError('Refusing to replace a non-plugin directory')
    with tempfile.TemporaryDirectory(prefix=destination.name + '-build-', dir=destination.parent) as temporary:
        stage = Path(temporary) / 'snapshot'
        shutil.copytree(ROOT, stage, ignore=excluded)
        records = []
        for path in sorted(stage.rglob('*')):
            if path.is_file() and path.name != 'DIST_MANIFEST.json':
                records.append(dict(path=str(path.relative_to(stage)), sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        (stage / 'DIST_MANIFEST.json').write_text(json.dumps(dict(built_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                                               files=records), indent=2) + '\n')
        previous = Path(temporary) / 'previous'
        if destination.exists():
            os.replace(destination, previous)
        try:
            os.replace(stage, destination)
        except OSError:
            if previous.exists():
                os.replace(previous, destination)
            raise
    return dict(destination=str(destination), skills=8, files=len(records), dependencies='Python standard library only')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path.home() / 'plugins-dist/muse-guardrails')
    args = parser.parse_args()
    print(json.dumps(build(args.output), indent=2))
