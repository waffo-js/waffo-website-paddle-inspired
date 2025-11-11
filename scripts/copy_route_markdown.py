#!/usr/bin/env python3
"""
Copy Markdown files from paddle_content/ into waffo-website/content/
based on entries in waffo-website/content/route-map.json.

For each route item, if `paddle_content/<source_md>` exists, copy it to
`waffo-website/content/<source_md>` (creating parent dirs as needed).
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PADDLE_CONTENT = BASE / 'paddle_content'
SITE_CONTENT = BASE / 'waffo-website' / 'content'
ROUTE_MAP = SITE_CONTENT / 'route-map.json'


def main() -> int:
    if not ROUTE_MAP.exists():
        print(f"! route map not found: {ROUTE_MAP}")
        return 1
    try:
        data = json.loads(ROUTE_MAP.read_text(encoding='utf-8'))
        routes = data.get('routes', [])
    except Exception as e:
        print(f"! failed to read/parse route map: {e}")
        return 1

    copied = 0
    missing = 0
    for item in routes:
        src_rel = item.get('source_md')
        if not src_rel:
            continue
        src = PADDLE_CONTENT / src_rel
        if src.is_file():
            dest = SITE_CONTENT / src_rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            copied += 1
            print(f"✓ copied {src_rel}")
        else:
            missing += 1
            # Show a short message but don't fail the run
            print(f"- missing in paddle_content: {src_rel}")

    print(f"\nSummary: copied={copied}, missing={missing}, total={len(routes)}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

