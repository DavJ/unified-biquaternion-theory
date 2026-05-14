# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim: synthetic -> ubt_with_chronofactor.forensic_fingerprint.synthetic."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_with_chronofactor.forensic_fingerprint.synthetic")
_sys.modules[__name__] = _real
