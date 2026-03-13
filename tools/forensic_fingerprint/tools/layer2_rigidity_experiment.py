#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim: forensic_fingerprint.tools.layer2_rigidity_experiment -> ubt_with_chronofactor.

When executed as a script this module forwards all arguments to the real
implementation located under ubt_with_chronofactor.
"""
import importlib as _importlib
import runpy as _runpy
import sys as _sys
from pathlib import Path as _Path

# Resolve the real module path so it can be executed as a script
_REAL_SCRIPT = (
    _Path(__file__).parent.parent.parent
    / "ubt_with_chronofactor"
    / "forensic_fingerprint"
    / "tools"
    / "layer2_rigidity_experiment.py"
)

if __name__ == "__main__":
    _runpy.run_path(str(_REAL_SCRIPT), run_name="__main__")
else:
    _real = _importlib.import_module(
        "ubt_with_chronofactor.forensic_fingerprint.tools.layer2_rigidity_experiment"
    )
    _sys.modules[__name__] = _real
    globals().update({k: getattr(_real, k) for k in dir(_real) if not k.startswith("_")})
