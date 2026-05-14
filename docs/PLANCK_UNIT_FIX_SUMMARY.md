# Planck Unit Handling Fix - Implementation Summary

## Problem Statement

The Planck data loader was performing automatic unit conversion (Dl→Cl) **before** auto-resolution, which caused:
1. Poor diagnostics (can't see raw values)
2. Potential double conversion
3. Wrong interpretation selection
4. Most critically: **CANDIDATE results could be produced even when sanity checks failed**

In court-grade mode, this is unacceptable - invalid data configurations should NEVER produce a "signal".

## Solution Implemented

### Patch 1: Raw Model Loading

**Files Modified**: `forensic_fingerprint/loaders/planck.py`

#### Changes to `_load_planck_text()`:
- Added `convert_to_cl` parameter (default: `True`)
- Conversion from Dl→Cl now conditional: only if `units_detected == "Dl" and convert_to_cl`
- Allows loading raw values when `convert_to_cl=False`

#### Changes to `_load_planck_minimum_format()`:
- Added `convert_to_cl` parameter (default: `True`)
- Same conditional conversion logic as above

#### Changes to `load_planck_data()`:
- **Observation files**: loaded with `convert_to_cl=True` (default behavior)
- **Model files**: loaded with `convert_to_cl=False` (raw values)
- Model values passed to `auto_resolve_model_units()` in raw form
- Auto-resolution performs conversions internally and chooses best interpretation

### Patch 2: Unit Resolution Failure Detection

**Files Modified**: `forensic_fingerprint/loaders/planck.py`

#### Changes to `auto_resolve_model_units()`:
Added fail-safe check after computing chi2 for both interpretations:
```python
if chi2_per_dof_1 > 1e6 and chi2_per_dof_2 > 1e6:
    return ..., 'UNKNOWN', {
        'unit_resolution_failed': True,
        'reason': 'Both Cl and Dl interpretations yield catastrophic chi2...',
        ...
    }
```

#### Changes to `load_planck_data()`:
- Check `unit_resolution_failed` flag after auto-resolution
- Print warning with chi2 values
- Metadata propagated to downstream analysis

### Patch 3: CMB Comb Validity Gate

**Files Modified**: `forensic_fingerprint/cmb_comb/cmb_comb.py`

#### Changes to `run_cmb_comb_test()`:
Added hard validity gate immediately after `compute_residuals()`:
```python
if not whiten_metadata.get('sanity_checks_passed', True):
    # Return INVALID result immediately
    return {
        'significance': 'invalid',
        'p_value': None,
        'best_period': None,
        ...
    }
```

**Critical behavior**: Even in `strict=False` mode, sanity check failures result in `significance='invalid'`, **never** `'candidate'` or `'strong'`.

### Patch 4: Runner Strict Mode Reporting

**Files Modified**: `forensic_fingerprint/run_real_data_cmb_comb.py`

#### Changes to `main()`:
- Added strict mode status to startup output: `"Strict mode: {args.strict} (court-grade fail-fast)"`

#### Changes to `generate_combined_verdict()`:
- Check for `significance == 'invalid'` before evaluating PASS/FAIL criteria
- If either Planck or WMAP is INVALID → verdict is INVALID (cannot proceed)
- Added INVALID warnings in markdown output

## Behavior Matrix

| Scenario | Strict ON | Strict OFF |
|----------|-----------|------------|
| **Correct units** | Normal test → NULL/CANDIDATE/STRONG | Same |
| **Units mismatch (chi2 > 1e6)** | RuntimeError (fail-fast) | Continue → INVALID |
| **Wrong model file (both chi2 > 1e6)** | RuntimeError | INVALID flagged during load → INVALID result |
| **Sanity check failure** | RuntimeError in compute_residuals | Validity gate → INVALID |

## Testing Results

All tests pass:

### Unit Tests (`test_planck_units_and_strict_mode.py`)
- ✅ Variant keyword detection (D_ell, Dℓ, DlTT, etc.)
- ✅ Magnitude heuristic with ell > 30 cutoff
- ✅ TT-full format parsing
- ✅ Auto-resolution with chi2 precheck
- ✅ Strict mode raises RuntimeError on mismatch
- ✅ load_planck_data with auto-resolution

### Integration Tests
- ✅ Correct data → Valid result (null/candidate/strong)
- ✅ Mismatched units (strict OFF) → INVALID result
- ✅ Mismatched units (strict ON) → RuntimeError
- ✅ Complete resolution failure → Detected and warned

## Impact

### Before This Fix
- Model loaded with pre-conversion → poor diagnostics
- Wrong units could produce CANDIDATE result
- Strict mode existed but validity gate was missing
- No detection of complete resolution failure

### After This Fix
- Model loaded RAW → proper auto-resolution
- **INVALID result enforced when sanity checks fail**
- **No false CANDIDATE results possible from units mismatch**
- Clear warnings when resolution fails
- Court-grade behavior: strict ON fails fast, strict OFF continues but never produces false positives

## Files Modified

1. `forensic_fingerprint/loaders/planck.py`
   - `_load_planck_text()`: Added `convert_to_cl` parameter
   - `_load_planck_minimum_format()`: Added `convert_to_cl` parameter
   - `load_planck_data()`: Load model with `convert_to_cl=False`
   - `auto_resolve_model_units()`: Added fail-safe for catastrophic chi2

2. `forensic_fingerprint/cmb_comb/cmb_comb.py`
   - `run_cmb_comb_test()`: Added validity gate after compute_residuals

3. `forensic_fingerprint/run_real_data_cmb_comb.py`
   - `main()`: Added strict mode reporting
   - `generate_combined_verdict()`: Handle INVALID results

## Commit History

1. `aa15d44` - Implement Planck model raw loading and validity gate for units mismatch
2. `a523c56` - Fix calibration_diagnostics initialization in validity gate
3. `a5d3373` - Fix unit resolution failure metadata handling in load_planck_data

## Conclusion

The implementation successfully prevents false CANDIDATE results due to units/model mismatch while maintaining backward compatibility for correct data. The validity gate ensures court-grade integrity: **invalid configurations can never produce a signal**.
