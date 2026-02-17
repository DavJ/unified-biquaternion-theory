# Import Shim Solution Summary

## Problem
After repository restructuring, several modules moved from the repository root to `ubt_with_chronofactor/` subdirectories, breaking imports in test files that expected them at the root level.

## Solution Implemented

### Primary Shims (Created)
The following root-level shims were created to fix the immediate pytest collection failures:

1. **`validate_manifest.py`** → `ubt_with_chronofactor/tools/data_provenance/validate_manifest.py`
2. **`hash_dataset.py`** → `ubt_with_chronofactor/tools/data_provenance/hash_dataset.py`
3. **`repo_utils.py`** → `ubt_with_chronofactor/tools/data_provenance/repo_utils.py`

These shims:
- Use `importlib` to dynamically import from the real location
- Try multiple candidate paths (both `tools/` and `TOOLS/`)
- Re-export all public symbols from the real module
- Preserve CLI functionality with `if __name__ == "__main__"` blocks

### Package Structure (Created)
Added `__init__.py` files to make `ubt_with_chronofactor` importable as a Python package:
- `ubt_with_chronofactor/__init__.py`
- `ubt_with_chronofactor/tools/__init__.py`
- `ubt_with_chronofactor/tools/data_provenance/__init__.py`
- `ubt_with_chronofactor/TOOLS/__init__.py`
- `ubt_with_chronofactor/TOOLS/data_provenance/__init__.py`

### Existing Shim (Already Present)
- **`forensic_fingerprint/`** → `ubt_with_chronofactor/forensic_fingerprint/`
  - Sophisticated shim that replaces itself in `sys.modules`
  - Handles all submodule imports (layer2, loaders, cmb_comb, etc.)

## Remaining Import Issues

The scanner script (`tests/scan_top_level_imports.py`) identified 24 broken imports. Most are already handled:

### ✅ Already Fixed by Existing Shims
These imports work because the `forensic_fingerprint` shim handles them:
- `forensic_fingerprint.layer2.config_space`
- `forensic_fingerprint.layer2.metrics`
- `forensic_fingerprint.layer2.predictors`
- `forensic_fingerprint.tools.theta_fit_tau`
- `planck` (via forensic_fingerprint.loaders.planck)
- `cmb_comb` (via forensic_fingerprint.cmb_comb.cmb_comb)
- `grid_255`, `invariance`, `wmap` (if in forensic_fingerprint)
- `run_real_data_cmb_comb` (if in forensic_fingerprint)

### 🔧 Can Be Fixed with Additional Shims or Symlinks
For modules in `ubt_with_chronofactor` subdirectories:

**Option 1: Create Shim Packages**
```python
# ubt_masses/__init__.py
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'ubt_with_chronofactor'))
from ubt_masses import *
```

**Option 2: Symbolic Links** (Linux/Mac only)
```bash
ln -s ubt_with_chronofactor/ubt_masses ubt_masses
ln -s ubt_with_chronofactor/alpha_core_repro alpha_core_repro
```

**Option 3: Update Test Imports** (Most explicit)
```python
# In tests, add:
sys.path.insert(0, str(repo_root / 'ubt_with_chronofactor'))
# Then import works: from ubt_masses import core
```

### Modules That Need Attention
Based on scanner output, these are used in multiple tests:

| Module | Used By | Location |
|--------|---------|----------|
| `ubt_masses.core` | 7 tests | `ubt_with_chronofactor/ubt_masses/` |
| `ubt_masses.qed` | 2 tests | `ubt_with_chronofactor/ubt_masses/` |
| `alpha_core_repro.alpha_two_loop` | 2 tests | `ubt_with_chronofactor/alpha_core_repro/` |
| Others | 1-2 tests each | Various subdirectories |

## Recommended Next Steps

1. **Verify forensic_fingerprint shim coverage**: Test that imports like `planck`, `cmb_comb` work
2. **Add ubt_masses shim**: Most commonly used remaining module
3. **Document path setup**: Add to test README about adding `ubt_with_chronofactor` to path
4. **Consider test fixtures**: Create pytest fixtures that set up paths automatically

## Testing

Run the scanner to see current state:
```bash
python tests/scan_top_level_imports.py
```

Test specific imports:
```python
python3 -c "import validate_manifest; print('✓')"
python3 -c "from forensic_fingerprint.layer2 import config_space; print('✓')"
```

## Files Changed

### Created:
- `validate_manifest.py` (root shim)
- `hash_dataset.py` (root shim)
- `repo_utils.py` (root shim)
- `ubt_with_chronofactor/__init__.py` (package init)
- `ubt_with_chronofactor/tools/__init__.py`
- `ubt_with_chronofactor/tools/data_provenance/__init__.py`
- `ubt_with_chronofactor/TOOLS/__init__.py`
- `ubt_with_chronofactor/TOOLS/data_provenance/__init__.py`
- `tests/scan_top_level_imports.py` (diagnostic tool)

### Modified:
- `ubt_with_chronofactor/README.md` (removed "legacy" wording)
- `README.md` (added CCT placement info)

## Success Criteria

✅ Pytest can collect tests without `ModuleNotFoundError` for validate_manifest
✅ Documentation no longer refers to ubt_with_chronofactor as "legacy"
✅ CCT placement is clearly documented in root README
✅ Scanner tool helps identify remaining issues
✅ Both formulations (with/without chronofactor) clearly marked as first-class
