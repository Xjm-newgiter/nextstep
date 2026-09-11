"""Static checks for the NextStep repository. Every '可复核' claim in
docs/evidence.md maps to one check below. Exits 1 on failure."""
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

# 2. template line budget (<=40), registry capacity (>=3), and — F4-01 — the
#    capacities must MATCH the numbers claimed in docs/evidence.md
caps = {}
for rel in ('skills/nextstep/assets/AGENTS.md', 'skills/nextstep/assets/AGENTS.en.md'):
    n = len((root / rel).read_text(encoding='utf-8').splitlines())
    if n > 40:
        fail.append(f'LINES {rel}: {n} > 40')
    caps[rel] = 40 - n + 1
    if caps[rel] < 3:
        fail.append(f'CAPACITY {rel}: only {caps[rel]} registry row(s) fit under the red line')
ev = (root / 'docs/evidence.md').read_text(encoding='utf-8')
m = re.search(r'登记容量 zh (\d+) 行 / en (\d+) 行', ev)
if not m:
    fail.append('EVIDENCE: capacity claim ("登记容量 zh N 行 / en N 行") not found in docs/evidence.md')
else:
    claimed = (int(m.group(1)), int(m.group(2)))
    actual = (caps['skills/nextstep/assets/AGENTS.md'], caps['skills/nextstep/assets/AGENTS.en.md'])
    if claimed != actual:
        fail.append(f'EVIDENCE capacity mismatch: doc claims {claimed}, actual {actual}')
print(f"registry capacity (rows under the 40-line red line): {caps} — evidence claims {m.groups() if m else 'NOT FOUND'}")

# 3. required manifests EXIST (mutation-attack blind spot: deletion used to pass)
required = [
    '.zcode-plugin/plugin.json',
    '.claude-plugin/plugin.json',
    '.codex-plugin/plugin.json',
    '.claude-plugin/marketplace.json',
    '.agents/plugins/marketplace.json',
]
for f in required:
    if not (root / f).is_file():
        fail.append(f'MISSING required manifest: {f}')

# 3b. relative markdown links resolve from each file's own directory
for p in root.rglob('*.md'):
    if '.git' in p.parts:
        continue
    for m in re.finditer(r'\]\(([^)#]+)(?:#[^)]*)?\)', p.read_text(encoding='utf-8')):
        link = m.group(1).strip()
        if link.startswith(('http', '~', 'mailto')):
            continue
        if not (p.parent / link).is_file():
            fail.append(f'LINK {p} -> {link}')

# 4. manifests agree on name/version; required keys present; marketplaces non-empty.
#    Diagnostics must survive parse errors (F4-05): every branch appends readable
#    messages; skew checks are skipped only when a scan error was already recorded.
vers = set()
scan_errors = 0
try:
    for f in root.glob('.*/plugin.json'):
        try:
            d = json.loads(f.read_text(encoding='utf-8'))
        except Exception as e:
            fail.append(f'JSON {f}: {e}')
            scan_errors += 1
            continue
        vers.add((d.get('name'), d.get('version'), str(f.parent.name)))
        if f.parent.name == '.zcode-plugin' and not d.get('skills'):
            fail.append('ZCODE manifest missing required "skills" key')
        if f.parent.name == '.claude-plugin' and 'skills' in d:
            fail.append('CLAUDE manifest must not carry the ZCode-specific "skills" key')
    for f in list(root.glob('.*/marketplace.json')) + [root / '.agents/plugins/marketplace.json']:
        if not f.is_file():
            continue
        try:
            d = json.loads(f.read_text(encoding='utf-8'))
        except Exception as e:
            fail.append(f'JSON {f}: {e}')
            scan_errors += 1
            continue
        if not d.get('plugins'):
            fail.append(f'MARKETPLACE {f}: empty or missing "plugins" array')
        for p in d.get('plugins', []):
            vers.add((p.get('name'), p.get('version'), f'{f}#plugins'))
except Exception as e:
    fail.append(f'MANIFEST scan error: {e}')
if scan_errors == 0:
    names = {v[0] for v in vers}
    nums = {v[1] for v in vers if v[1] is not None}
    if vers and len(names) != 1:
        fail.append(f'MANIFEST name skew: {sorted(vers, key=str)}')
    if len(nums) > 1:
        fail.append(f'MANIFEST version skew: {sorted((v for v in vers if v[1] is not None), key=str)}')

# 5. protocol version markers agree across templates, spec title — and CHANGELOG (F4-13)
marks = set()
for rel in ('skills/nextstep/assets/AGENTS.md', 'skills/nextstep/assets/AGENTS.en.md'):
    t = (root / rel).read_text(encoding='utf-8')
    m = re.search(r'(?:协议版本|Protocol version)[：:]\s*v?(\d+\.\d+)', t)
    marks.add(m.group(1) if m else None)
m = re.search(r'（NextStep）\s*v?(\d+\.\d+)', (root / '会话推进协议.md').read_text(encoding='utf-8'))
marks.add(m.group(1) if m else None)
if None in marks or len(marks) != 1:
    fail.append(f'PROTOCOL VERSION marker skew: {marks}')
m = re.search(r'^## (\d+\.\d+\.\d+)', (root / 'CHANGELOG.md').read_text(encoding='utf-8'), re.M)
changelog_v = m.group(1) if m else None
if changelog_v and nums and nums != {changelog_v}:
    fail.append(f'CHANGELOG top version {changelog_v} != manifest versions {nums}')

# 6. the shipped example is marked as non-reusable in both templates
for rel in ('skills/nextstep/assets/AGENTS.md', 'skills/nextstep/assets/AGENTS.en.md'):
    t = (root / rel).read_text(encoding='utf-8')
    if '勿复用' not in t and 'do not reuse' not in t:
        fail.append(f'EXAMPLE disclaimer missing in {rel}')

# 7. core disciplines cannot silently regress (F5-04/F5-06); READMEs cannot
#    resurrect withdrawn rules or lose lifecycle guidance (F5-01)
required_snippets = {
    'skills/nextstep/assets/AGENTS.md': ['**持久性**', '输出配额', '自我合理化', '停止协议', '勿复用'],
    'skills/nextstep/assets/AGENTS.en.md': ['**Persistence**', 'Output quota', 'self-justification', 'stop the protocol', 'do not reuse'],
    'skills/nextstep/SKILL.md': ['## Upgrade steps'],
}
for rel, snippets in required_snippets.items():
    t = (root / rel).read_text(encoding='utf-8')
    for s in snippets:
        if s not in t:
            fail.append(f'REGRESSION {rel}: missing "{s}"')
for rel in ('README.md', 'README.zh-CN.md'):
    t = (root / rel).read_text(encoding='utf-8')
    if '8 行' in t or '8 rows' in t:
        fail.append(f'REGRESSION {rel}: withdrawn "8 rows" rule resurfaced')
    if 'uninstall' not in t.lower() and '卸载' not in t:
        fail.append(f'REGRESSION {rel}: turn-off/uninstall guidance missing')

print('\n'.join(fail) if fail else 'all checks passed')
sys.exit(1 if fail else 0)
