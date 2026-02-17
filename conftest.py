"""
Root conftest.py — runs before any test module is collected.

Imports the forensic_fingerprint shim so that sub-package paths
(cmb_comb, grid_255, invariance, loaders, …) are added to sys.path
before tests that rely on those direct imports are collected.
"""
import sys
from pathlib import Path

# Ensure repo root is on the path so the shim package is importable.
repo_root = Path(__file__).resolve().parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Trigger the shim: this adds ubt_with_chronofactor/forensic_fingerprint
# and its sub-package directories to sys.path.
import forensic_fingerprint  # noqa: F401, E402
