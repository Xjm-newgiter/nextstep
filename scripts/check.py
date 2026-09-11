"""Static checks for the NextStep repository: manifest JSON validity, template
line budget and registry capacity, relative markdown links, manifest version
sync, protocol-version marker consistency, and example disclaimer. Exits 1 on failure."""
import json
import re
import sys
from pathlib import Path

root = Path('.')
fail = []

# 1. every JSON manifest parses (rglob reaches dot-directories)
for f in root.rglob('*.json'):
    try:
        json.loads(f.read_text(encoding='utf-8'))
    except Exception as e:
        fail.append(f'JSON {f}: {e}')

# 2. template line budget (<=40) and registry capacity (>=3 rows), per template
caps = {}
for rel in ('skills/nextstep/assets/AGENTS.md', 'skills/nextstep/assets/AGENTS.en.md'):
    n = len((root / rel).read_text(encoding='utf-8').splitlines())
    if n > 40:
        fail.append(f'LINES {rel}: {n} > 40')
    caps[rel] = 40 - n + 1
    if caps[rel] < 3:
        fail.append(f'CAPACITY {rel}: only {caps[rel]} registry row(s) fit under the red line')
print(f"registry capacity (rows under the 40-line red line): {caps}")

# 3. relative markdown links resolve from each file's own directory
for p in root.rglob('*.md'):
    if '.git' in p.parts:
        continue
    for m in re.finditer(r'\]\(([^)#]+)(?:#[^)]*)?\)', p.read_text(encoding='utf-8')):
        link = m.group(1).strip()
        if link.startswith(('http', '~', 'mailto')):
            continue
        if not (p.parent / link).is_file():
            fail.append(f'LINK {p} -> {link}')

# 4. plugin/marketplace manifests agree on name and version
vers = set()
for f in root.glob('.*/plugin.json'):
    d = json.loads(f.read_text(encoding='utf-8'))
    vers.add((d.get('name'), d.get('version'), str(f.parent.name)))
for f in list(root.glob('.*/marketplace.json')) + list(root.glob('.agents/plugins/marketplace.json')):
    if not f.is_file():
        continue
    d = json.loads(f.read_text(encoding='utf-8'))
    for p in d.get('plugins', []):
        vers.add((p.get('name'), p.get('version'), f'{f.parent.name}#plugins'))
names = {v[0] for v in vers}
nums = {v[1] for v in vers}
if len(names) != 1:
    fail.append(f'MANIFEST name skew: {sorted(vers)}')
if len(nums - {None}) > 1:
    fail.append(f'MANIFEST version skew: {sorted(vers)}')

# 5. protocol version markers agree across templates, spec title, CHANGELOG
marks = set()
for rel in ('skills/nextstep/assets/AGENTS.md', 'skills/nextstep/assets/AGENTS.en.md'):
    t = (root / rel).read_text(encoding='utf-8')
    m = re.search(r'(?:协议版本|Protocol version)[：:]\s*v([\d.]+)', t)
    marks.add(m.group(1) if m else None)
m = re.search(r'（NextStep）v([\d.]+)', (root / '会话推进协议.md').read_text(encoding='utf-8'))
marks.add(m.group(1) if m else None)
if None in marks or len(marks) != 1:
    fail.append(f'PROTOCOL VERSION marker skew: {marks}')

# 6. the shipped example is marked as non-reusable in both templates
for rel in ('skills/nextstep/assets/AGENTS.md', 'skills/nextstep/assets/AGENTS.en.md'):
    t = (root / rel).read_text(encoding='utf-8')
    if '勿复用' not in t and 'do not reuse' not in t:
        fail.append(f'EXAMPLE disclaimer missing in {rel}')

print('\n'.join(fail) if fail else 'all checks passed')
sys.exit(1 if fail else 0)
