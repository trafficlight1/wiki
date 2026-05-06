#!/usr/bin/env python3
"""
Regenerate _manifest.json — sweeps the vault folder and lists all .md files.
Run this script after adding/renaming/removing .md files so the website picks them up.

Usage:
    python regenerate_manifest.py
"""
import os
import json
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))


EXCLUDED = {'README.md'}  # files NOT shown in the vault graph/reader


def collect():
    files = []
    for root, dirs, fs in os.walk(ROOT):
        # Skip hidden folders and node_modules-style stuff
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_')]
        for f in fs:
            if f.endswith('.md') and f not in EXCLUDED:
                path = os.path.relpath(os.path.join(root, f), ROOT).replace('\\', '/')
                files.append(path)
    files.sort()
    return files


def main():
    files = collect()
    manifest = {
        'generated': date.today().isoformat(),
        'files': files,
        'canvas': 'Mind_Map.canvas',
    }
    with open(os.path.join(ROOT, '_manifest.json'), 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
    print(f'Manifest regenerated: {len(files)} markdown files indexed.')


if __name__ == '__main__':
    main()
