"""Static checks for the NextStep repository: manifest JSON validity, template
line budget, relative markdown links, and manifest version sync. Exits 1 on failure."""
import glob
import json
import os
import re
import sys

fail = []

# 1. every JSON manifest parses
for f in glob.glob('**/*.json', recursive=True):
    try:
        json.load(open(f, encoding='utf-8'))
    except Exception as e:
        fail.append(f'JSON {f}: {e}')

# 2. template line budget (the 40-line red line)
for f in ('skills/nextstep/assets/AGENTS.md', 'skills/nextstep/assets/AGENTS.en.md'):
    n = sum(1 for _ in open(f, encoding='utf-8'))
    if n > 40:
        fail.append(f'LINES {f}: {n} > 40')

# 3. relative markdown links resolve from each file's own directory
for root, _, files in os.walk('.'):
    if '.git' in root:
        continue
    for fn in files:
        if not fn.endswith('.md'):
            continue
        p = os.path.join(root, fn)
        for m in re.finditer(r'\]\(([^)#]+)(?:#[^)]*)?\)', open(p, encoding='utf-8').read()):
            link = m.group(1).strip()
            if link.startswith(('http', '~', 'mailto')):
                continue
            if not os.path.isfile(os.path.normpath(os.path.join(root, link))):
                fail.append(f'LINK {p} -> {link}')

# 4. all plugin manifests agree on name and version
versions = set()
for f in glob.glob('.*/plugin.json'):
    d = json.load(open(f, encoding='utf-8'))
    versions.add((d.get('name'), d.get('version')))
if len(versions) > 1:
    fail.append(f'MANIFEST version/name skew: {sorted(versions)}')

print('\n'.join(fail) if fail else 'all checks passed')
sys.exit(1 if fail else 0)
