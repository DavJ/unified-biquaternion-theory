# Quick Reference: Court-Grade Testing

## Run Tests

```bash
# All tests (warnings = errors)
pytest

# Specific test file
pytest tests/test_no_circularity.py -v

# Specific test
pytest tests/test_no_circularity.py::test_no_circular_imports -v
```

## New Court-Grade Tests

### Circular Import Detection
```bash
pytest tests/test_no_circularity.py::test_no_circular_imports -v
```

**What it does:** Scans all Python files, builds import graph, detects cycles

**Output on failure:**
```
✗ Found 1 circular import(s):
  1. module_a -> module_b -> module_c -> module_a
```

### Dependency Boundary Enforcement
```bash
pytest tests/test_no_circularity.py::test_dependency_boundaries -v
```

**What it does:** Ensures `forensic_fingerprint` doesn't import theory modules

**Current rules:**
- `forensic_fingerprint/` must NOT import:
  - `strict_ubt`
  - `alpha_core_repro`
  - `ubt_masses`
  - `scripts.ubt_*`
  - `scripts.fit_*`

## Test Results

Expected output:
```
======================== 169 passed, 2 skipped in 10s ========================
```

**No warnings** = Success ✅

## Warnings Configuration

**pytest.ini:**
```ini
filterwarnings = error  # All warnings become errors
```

**To handle expected warnings:**
```python
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', message='...', category=...)
    code_that_warns()
```

## What Changed

1. ✅ Removed placeholder `assert True` tests
2. ✅ Added circular import detection
3. ✅ Added dependency boundary checks
4. ✅ Added NaN/inf guards to numeric tests
5. ✅ Configured strict warning enforcement

## Full Documentation

See `tests/COURT_GRADE_TESTING.md` for complete details.

## Files Modified

- `tests/_import_graph.py` - NEW: Import analysis utility
- `tests/test_no_circularity.py` - Enhanced with real checks
- `tests/test_qed_limit.py` - Added NaN/inf guards
- `tests/test_forensic_fingerprint.py` - Explicit warning handling
- `pytest.ini` - Strict mode: warnings as errors
- `tests/COURT_GRADE_TESTING.md` - Full documentation

## Quick Checks

```bash
# Verify no placeholders remain
grep -rn "assert True$\|assert False$" tests/*.py

# Check for circular imports
pytest tests/test_no_circularity.py::test_no_circular_imports

# Run with explicit strict warnings (redundant, but works)
pytest -W error
```
