#!/usr/bin/env python3
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CONTENT_ROOT = BASE / 'paddle_content'
OUTPUT = BASE / 'waffo-website' / 'content'
OUTPUT.mkdir(parents=True, exist_ok=True)
ROUTE_MAP_PATH = OUTPUT / 'route-map.json'

def parse_title(md_path: Path) -> str:
    try:
        text = md_path.read_text(encoding='utf-8')
        m = re.search(r'^title:\s*"(.+?)"', text, re.MULTILINE)
        if m:
            return m.group(1)
        # fallback to first H1
        m2 = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
        if m2:
            return m2.group(1)
    except Exception:
        pass
    return md_path.stem.replace('-', ' ').title()

def to_route(rel: Path) -> str:
    parts = list(rel.parts)
    # drop extension
    if parts[-1].endswith('.md'):
        parts[-1] = parts[-1][:-3]
    # handle index.md → parent path
    if parts[-1] == 'index':
        parts = parts[:-1]
    route = '/' + '/'.join(parts)
    if route == '/':
        return '/'
    return route

def main():
    items = []
    for md in sorted(CONTENT_ROOT.rglob('*.md')):
        rel = md.relative_to(CONTENT_ROOT)
        route = to_route(rel)
        title = parse_title(md)
        items.append({
            'path': route,
            'title': title,
            'source_md': str(rel).replace('\\', '/'),
        })
    ROUTE_MAP_PATH.write_text(json.dumps({'routes': items}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"✓ Wrote {ROUTE_MAP_PATH} with {len(items)} routes")

if __name__ == '__main__':
    main()
