# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim: wmap -> ubt_with_chronofactor.forensic_fingerprint.loaders.wmap."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_with_chronofactor.forensic_fingerprint.loaders.wmap")
_sys.modules[__name__] = _real
globals().update({k: getattr(_real, k) for k in dir(_real) if not k.startswith("_")})
