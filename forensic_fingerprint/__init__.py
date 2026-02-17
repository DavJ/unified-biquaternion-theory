"""
Forensic Fingerprint - Root-Level Compatibility Shim

This package provides backward compatibility after the repository restructuring.
All functionality delegates to ubt_with_chronofactor/forensic_fingerprint/.

Usage in tests:
    from forensic_fingerprint.layer2.config_space import Layer2Config
    from forensic_fingerprint.loaders.planck import load_planck_map
    
These imports will automatically resolve to the implementation in
ubt_with_chronofactor/forensic_fingerprint/.

For explicit imports, use:
    from ubt_with_chronofactor.forensic_fingerprint.layer2 import ...

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

import sys
import importlib

# First, ensure target is in sys.path
from ._shim import ensure_importable, get_target_root
_TARGET = ensure_importable()

# Now, import the actual forensic_fingerprint from ubt_with_chronofactor
# and replace this module with it in sys.modules
try:
    # Import the real module
    from ubt_with_chronofactor import forensic_fingerprint as _real_ff
    
    # Replace our shim with the real module in sys.modules
    # This makes all subsequent imports use the real module
    sys.modules['forensic_fingerprint'] = _real_ff
    
    # Copy all attributes from real module to this namespace
    # so that direct attribute access also works
    for attr in dir(_real_ff):
        if not attr.startswith('_'):
            globals()[attr] = getattr(_real_ff, attr)
            
except ImportError as e:
    # If import fails, at least provide the shim utilities
    __all__ = ["ensure_importable", "get_target_root"]
    raise RuntimeError(
        f"Failed to import forensic_fingerprint from ubt_with_chronofactor: {e}\n"
        f"Target path: {_TARGET}"
    )
