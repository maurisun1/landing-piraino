#!/usr/bin/env python3
"""Ensure all /zh/ pages have noindex,follow."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "zh"


def main() -> None:
    updated = 0
    for p in ZH.rglob("index.html"):
        t = p.read_text(encoding="utf-8")
        if re.search(r'name=["\']robots["\']', t, re.I):
            nt, n = re.subn(
                r'(<meta\s+name=["\']robots["\']\s+content=["\'])([^"\']*)(["\'])',
                r"\1noindex, follow\3",
                t,
                count=1,
                flags=re.I,
            )
            if n == 0:
                # content before name
                nt, n = re.subn(
                    r'(<meta\s+content=["\'])([^"\']*)(["\']\s+name=["\']robots["\'])',
                    r"\1noindex, follow\3",
                    t,
                    count=1,
                    flags=re.I,
                )
            if n and nt != t:
                p.write_text(nt, encoding="utf-8")
                updated += 1
        else:
            nt, n = re.subn(
                r"(</title>\s*)",
                r'\1<meta name="robots" content="noindex, follow" />\n',
                t,
                count=1,
                flags=re.I,
            )
            if n:
                p.write_text(nt, encoding="utf-8")
                updated += 1
    print(f"zh noindex updated={updated}")


if __name__ == "__main__":
    main()
