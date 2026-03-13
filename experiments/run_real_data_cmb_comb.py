# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""
Root shim: run_real_data_cmb_comb.

Delegates to archive/ARCHIVE/legacy_variants/ubt_with_chronofactor/forensic_fingerprint/
after root_detox_phase1 reorganisation.
"""
import sys as _sys
from pathlib import Path as _Path

_repo_root = _Path(__file__).resolve().parent.parent

# Add paths needed by the implementation
for _p in [
    _repo_root / "archive" / "ARCHIVE" / "legacy_variants",
    _repo_root / "scripts",
    _repo_root / "tools",
    _repo_root / "experiments",
]:
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import importlib as _importlib
_real = _importlib.import_module("ubt_with_chronofactor.forensic_fingerprint.run_real_data_cmb_comb")
_sys.modules[__name__] = _real
globals().update({k: getattr(_real, k) for k in dir(_real) if not k.startswith("_")})

if __name__ == "__main__":
    import runpy
    runpy.run_module("ubt_with_chronofactor.forensic_fingerprint.run_real_data_cmb_comb", run_name="__main__")
