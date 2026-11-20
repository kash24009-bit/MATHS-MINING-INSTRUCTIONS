#!/usr/bin/env python3
# Ported 2026-11-20 from the Physics (042) project: T/phy_notes_apply.py of its vault branch (2026-11-16). Examples and calibration notes cite Physics papers (history).
"""File a reader's NOTES-DRAFT.md (rule card E2 format) into the vault: notes lines to
notes/Y<year>.md, Q-QUEUE items with the next free numbers to QQUEUE.md and their short
lines to PROGRESS "Open". Prints counts only.
  python3 mat_notes_apply.py --draft /home/claude/render/<unit>/NOTES-DRAFT.md --year 2024
"""
import argparse, datetime, os, re
V = os.environ.get('MAT_VAULT', '/home/claude/vault')   # MAT_VAULT only for tests on a copy
ap = argparse.ArgumentParser(); ap.add_argument('--draft', required=True); ap.add_argument('--year', required=True)
a = ap.parse_args()
sec, notes, qq = None, [], []
for line in open(a.draft, encoding='utf-8'):
    s = line.rstrip('\n')
    if s.strip().lower().startswith('## notes'): sec = 'n'; continue
    if s.strip().lower().startswith('## qqueue'): sec = 'q'; continue
    if s.startswith('## '): sec = None; continue
    if sec == 'n' and s.startswith('- '): notes.append(s)
    if sec == 'q' and s.startswith('- ') and '|' in s: qq.append([x.strip() for x in s[2:].split('|')])
if notes:
    p = f'{V}/notes/Y{a.year}.md'; os.makedirs(os.path.dirname(p), exist_ok=True)
    # the port: a new year's first note starts its file
    t = open(p, encoding='utf-8').read().rstrip('\n') if os.path.exists(p) else f'# Y{a.year} notes'
    open(p, 'w', encoding='utf-8').write(t + '\n' + '\n'.join(notes) + '\n')
added = []
if qq:
    qp = f'{V}/QQUEUE.md'; qt = open(qp, encoding='utf-8').read().rstrip('\n')
    n = max((int(x) for x in re.findall(r'\[Q-(\d{3})', qt)), default=0)   # the port: a new vault's queue starts empty
    today = datetime.date.today().isoformat()
    for item in qq:
        kind, text = item[0], item[1] if len(item) > 1 else ''
        short = item[2] if len(item) > 2 else text[:120]
        n += 1; qid = f'Q-{n:03d}'
        qt += f'\n- [{qid} · {today} · open · {kind}] {text}'; added.append(f'- {qid} {short}')
    open(qp, 'w', encoding='utf-8').write(qt + '\n')
    pp = f'{V}/PROGRESS.md'; L = open(pp, encoding='utf-8').read().split('\n')
    i = L.index('## Open'); j = i + 1
    while j < len(L) and not L[j].startswith('## '): j += 1
    while j > i + 1 and not L[j - 1].strip(): j -= 1
    L[j:j] = added
    open(pp, 'w', encoding='utf-8').write('\n'.join(L))
print(f'notes +{len(notes)} lines to Y{a.year}; queue +{len(added)} ({", ".join(x.split()[1] for x in added) or "none"})')
