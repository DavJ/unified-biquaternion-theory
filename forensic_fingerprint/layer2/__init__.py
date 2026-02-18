# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim package: forensic_fingerprint.layer2 -> ubt_with_chronofactor.forensic_fingerprint.layer2."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_with_chronofactor.forensic_fingerprint.layer2")
_sys.modules[__name__] = _real
