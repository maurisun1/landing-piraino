#!/usr/bin/env python3
"""Regenerate sitemap.xml — thin wrapper around tools/build_sitemap.py.

Keeps the historical CI helper entrypoint, but uses the indexable-only
builder (self-canonical, excludes noindex/zh, real lastmod, includes
guide + valutazione pages).
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILDER = ROOT / "tools" / "build_sitemap.py"


def main() -> None:
    if not BUILDER.is_file():
        raise SystemExit(f"Missing sitemap builder: {BUILDER}")
    sys.path.insert(0, str(ROOT / "tools"))
    runpy.run_path(str(BUILDER), run_name="__main__")


if __name__ == "__main__":
    main()
