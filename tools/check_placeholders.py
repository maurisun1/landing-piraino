#!/usr/bin/env python3
"""Fail if generated HTML still contains visible data placeholders."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = re.compile(r"DATO DA INSERIRE", re.I)
# Visible leftover wording (not HTML input placeholder= attributes)
VISIBLE_BAD = re.compile(r"\b(lorem ipsum|\[TODO\]|\[TBD\])\b", re.I)


def main() -> int:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".github/"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in FORBIDDEN.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            errors.append(f"{rel}:{line}: DATO DA INSERIRE")
        for m in VISIBLE_BAD.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            errors.append(f"{rel}:{line}: {m.group(0)}")
    # JSON source must not ship unresolved placeholders into guides
    for path in (ROOT / "seo").glob("*.json"):
        text = path.read_text(encoding="utf-8")
        if FORBIDDEN.search(text):
            errors.append(f"{path.relative_to(ROOT)}: DATO DA INSERIRE in source JSON")
    if errors:
        print("PLACEHOLDER CHECK FAILED:")
        for e in errors:
            print(" -", e)
        return 1
    print("placeholder check OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
