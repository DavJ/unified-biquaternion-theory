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

# Locate the real implementation
_REPO_ROOT = Path(__file__).resolve().parents[2]
_REAL_SCRIPT = (
    _REPO_ROOT
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

# Ensure the repo root is on sys.path so that subpackage imports work
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

# Run the real script as __main__
runpy.run_path(str(_REAL_SCRIPT), run_name="__main__")
