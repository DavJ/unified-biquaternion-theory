"""
conftest.py — Repository-wide pytest configuration.

Sets up sys.path so that relocated packages can be imported after
the root_detox_phase1 reorganisation:

  - forensic_fingerprint  →  tools/forensic_fingerprint/
  - alpha_core_repro      →  experiments/alpha_core_repro/
  - ubt_masses            →  research_tracks/ubt_masses/
  - planck, cmb_comb, …   →  experiments/

This file is loaded automatically by pytest before any test collection.

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""
from __future__ import annotations
import sys
from pathlib import Path

# Repository root (this file lives in tests/, so parent is root)
_repo_root = Path(__file__).resolve().parent.parent


def _add(p: Path) -> None:
    s = str(p)
    if s not in sys.path:
        sys.path.insert(0, s)


# tools/          → enables `import forensic_fingerprint`
_add(_repo_root / "tools")

# experiments/    → enables `import alpha_core_repro`, `import planck`, `import cmb_comb`, etc.
_add(_repo_root / "experiments")

# research_tracks/ → enables `import ubt_masses`
_add(_repo_root / "research_tracks")

# scripts/        → enables `import repo_utils`, `import validate_manifest`, etc.
_add(_repo_root / "scripts")

# repo root itself
_add(_repo_root)

# core/           → enables `import strict_ubt` and other core packages
_add(_repo_root / "core")

# archive/ARCHIVE/legacy_variants/ → enables `import ubt_with_chronofactor`
# (ubt_with_chronofactor was archived from root during root_detox_phase1)
_add(_repo_root / "archive" / "ARCHIVE" / "legacy_variants")
