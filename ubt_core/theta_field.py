# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
"""Root shim: ubt_core.theta_field -> ubt_no_chronofactor.core.theta_field."""
import importlib as _importlib
import sys as _sys

_real = _importlib.import_module("ubt_no_chronofactor.core.theta_field")
_sys.modules[__name__] = _real
globals().update({k: getattr(_real, k) for k in dir(_real) if not k.startswith("_")})
