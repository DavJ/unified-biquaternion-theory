# Forensic Fingerprint Compatibility Shim

## Purpose

This directory provides a **compatibility shim** for the forensic_fingerprint module after the repository restructuring. It delegates all imports to the actual implementation in `ubt_with_chronofactor/forensic_fingerprint/`.

## Why This Exists

After restructuring, the forensic fingerprint implementation moved from root-level to:
```
ubt_with_chronofactor/forensic_fingerprint/
```

However, existing tests and CI workflows expect to import from:
```python
from forensic_fingerprint.layer2 import ...
from forensic_fingerprint.loaders.planck import ...
```

This shim preserves backward compatibility without requiring immediate changes to all tests.

## How It Works

1. **Path Delegation**: The shim adds `ubt_with_chronofactor/` to Python's `sys.path`
2. **Import Resolution**: Python then finds `forensic_fingerprint` as a submodule
3. **Transparent Access**: Tests import as if forensic_fingerprint were at root level

## Implementation

### `_shim.py`

Provides two key functions:

- `get_target_root()` - Returns path to actual forensic_fingerprint implementation
- `ensure_importable()` - Adds ubt_with_chronofactor to sys.path

### `__init__.py`

Automatically calls `ensure_importable()` on import, making the target importable.

## Usage in Tests

**No changes required** to existing test code:

```python
# This still works after restructuring
from forensic_fingerprint.layer2.config_space import Layer2Config
from forensic_fingerprint.layer2.predictors import predict_constants
from forensic_fingerprint.loaders.planck import load_planck_map
```

The shim transparently redirects to:
```
ubt_with_chronofactor/forensic_fingerprint/layer2/...
ubt_with_chronofactor/forensic_fingerprint/loaders/...
```

## Migration Path

This shim is a **temporary compatibility layer**. Over time, tests can migrate to explicit imports:

```python
# Explicit import (preferred for new code)
from ubt_with_chronofactor.forensic_fingerprint.layer2 import Layer2Config
```

Or if/when a chronofactor-free implementation is developed:

```python
# Switch to new implementation
from ubt_no_chronofactor.forensic_fingerprint.layer2 import Layer2Config
```

## CI/CD Integration

GitHub Actions workflows use this shim via:

```yaml
- name: Run forensic fingerprint tests
  run: |
    pytest tests/test_forensic_fingerprint.py -v
```

The shim ensures imports resolve correctly without modifying workflow files.

## Future

This shim can be:

1. **Switched** to point to `ubt_no_chronofactor/forensic_fingerprint/` when that implementation is ready
2. **Extended** to provide a unified interface that works with both formulations
3. **Removed** entirely once all code uses explicit imports

## Files

- `__init__.py` - Package initialization, auto-runs ensure_importable()
- `_shim.py` - Core path manipulation logic
- `README.md` (this file) - Documentation

## Technical Notes

### Why Not Symlinks?

Symlinks could achieve similar results but:
- May not work on all platforms (Windows)
- Don't allow conditional logic
- Can't be switched dynamically

Python delegation provides more flexibility.

### Import Order

The shim must be imported **before** any forensic_fingerprint submodules:

```python
# Correct
import forensic_fingerprint  # Initializes shim
from forensic_fingerprint.layer2 import ...  # Now resolves correctly

# Also correct (import triggers __init__.py automatically)
from forensic_fingerprint.layer2 import ...
```

### Path Priority

The shim uses `sys.path.insert(0, ...)` to give priority to the target location. This ensures forensic_fingerprint resolves to the correct implementation even if other paths exist.

## License

Copyright (c) 2025 Ing. David Jaroš

This shim is released under the MIT License, allowing unrestricted use as infrastructure code.

---

**Repository Structure After Restructuring:**

```
ubt_with_chronofactor/          # First-class formulation
  forensic_fingerprint/         # Actual implementation
    __init__.py
    layer2/
    loaders/
    ...

ubt_no_chronofactor/            # First-class formulation
  core/
  derivations/
  papers/

forensic_fingerprint/           # Root-level shim (this directory)
  __init__.py                   # Delegation logic
  _shim.py                      # Path management
  README.md                     # This file

tests/
  test_forensic_fingerprint.py  # Uses shim imports
  test_layer2_predictors.py     # Uses shim imports
  ...
```
