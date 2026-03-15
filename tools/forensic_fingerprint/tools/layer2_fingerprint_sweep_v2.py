#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
Layer 2 Fingerprint Sweep v2 — Root-level compatibility shim.

This file delegates all functionality to the actual implementation at:
  ubt_with_chronofactor/forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py

Reason: The test suite expects this script at
  forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py
relative to the repository root, while the canonical implementation lives
inside the ubt_with_chronofactor subpackage.
"""
import runpy
import sys
from pathlib import Path


def _find_repo_root(start: Path) -> Path:
    """Walk upward from start to find the repo root (contains pytest.ini)."""
    for parent in [start, *start.parents]:
        if (parent / "pytest.ini").exists():
            return parent
    return start.parents[3]  # fallback


# Locate the real implementation
_REPO_ROOT = _find_repo_root(Path(__file__).resolve())
_REAL_SCRIPT = (
    _REPO_ROOT
    / "ARCHIVE"
    / "archive_legacy"
    / "ARCHIVE"
    / "legacy_variants"
    / "ubt_with_chronofactor"
    / "forensic_fingerprint"
    / "tools"
    / "layer2_fingerprint_sweep_v2.py"
)

if not _REAL_SCRIPT.exists():
    print(
        f"ERROR: Real implementation not found at:\n  {_REAL_SCRIPT}",
        file=sys.stderr,
    )
    sys.exit(1)

# Ensure the ubt_with_chronofactor parent dir is on sys.path so imports work
_LEGACY_ROOT = _REPO_ROOT / "ARCHIVE" / "archive_legacy" / "ARCHIVE" / "legacy_variants"
if str(_LEGACY_ROOT) not in sys.path:
    sys.path.insert(0, str(_LEGACY_ROOT))

# Run the real script as __main__
runpy.run_path(str(_REAL_SCRIPT), run_name="__main__")
