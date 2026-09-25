#!/usr/bin/env python3
"""Deterministically generate the awesome list and detailed catalog from JSON."""
import argparse
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START, END = '<!-- DIRECTORY:START -->', '<!-- DIRECTORY:END -->'

def render(data):
    entries, categories = data['entries'], data['categories']
    counts = Counter(e['category'] for e in entries)
    lines = [f"**{len(entries)} entries · {len(categories)} categories · reviewed {data['as_of']}**", '', '## Contents', '']
    for cat in categories:
        lines.append(f"- [{cat['title']}](#{cat['id']}) ({counts[cat['id']]})")
    detail = ['# Detailed BTCfi directory', '', f"Snapshot: **{data['as_of']}**. [Method and status definitions](methodology.md) · [Awesome list](../README.md)", '',
              'Descriptions summarize publisher documentation. Review focuses are editorial questions, not completed security assessments. Network tags describe relevance, not a certified list of live deployments.', '']
    for cat in categories:
        lines += ['', f'<a id="{cat["id"]}"></a>', f"## {cat['title']}", '']
        detail += [f"## {cat['title']}", '']
        for e in sorted((e for e in entries if e['category']==cat['id']), key=lambda e:e['name'].casefold()):
            lines.append(f"- [{e['name']}]({e['website']}) — {e['description']} `{e['status']}` · [Details & sources](docs/directory.md#{e['id']}).")
            detail += [f'<a id="{e["id"]}"></a>', f"### {e['name']}", '',
                f"**Type:** {e['kind']} · **Networks:** {', '.join(e['networks'])} · **Status:** `{e['status']}` · **Reviewed:** {e['last_reviewed']}", '',
                e['description'], '',
                f"- **Bitcoin mechanism:** {e['bitcoin_mechanism']}",
                f"- **Review focus:** {e['review_focus']}",
                f"- **Status evidence / qualification:** {e['status_note']}",
                f"- **Project/resource:** [{e['name']}]({e['website']})"]
            for i,s in enumerate(e['sources'],1):
                detail.append(f"- **Source {i}:** [{s.get('title', 'Primary source' if s['type']=='primary' else 'Source')}]({s['url']}) — {s['type']}; reviewed {s['checked']}.")
            detail.append('')
    return '\n'.join(lines).rstrip()+'\n', '\n'.join(detail).rstrip()+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/'data/projects.json').read_text())
    listing, detail=render(data)
    readme=(ROOT/'README.md').read_text()
    if readme.count(START)!=1 or readme.count(END)!=1:
        raise SystemExit('README needs one start marker and one end marker.')
    before, rest=readme.split(START)
    _, after=rest.split(END)
    outputs={ROOT/'README.md':before+START+'\n\n'+listing+'\n'+END+after,ROOT/'docs/directory.md':detail}
    for path, content in outputs.items():
        if args.check:
            if not path.exists() or path.read_text()!=content:
                raise SystemExit(f'Out of date: {path.relative_to(ROOT)}; run scripts/build.py')
        else:
            path.write_text(content)
    print('Generated files match.' if args.check else f"Generated {len(data['entries'])} entries.")

if __name__=='__main__':
    main()
