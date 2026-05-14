# Planck CMB Comb Pipeline Units Fix - Implementation Summary

**Date**: 2026-01-12  
**Issue**: Fix Planck PR3 CMB comb pipeline to prevent false CANDIDATE due to units/model mismatch  
**Status**: ✅ COMPLETE

---

## Problem Statement

The Planck PR3 CMB comb pipeline was producing false CANDIDATE results when run with the command:
```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
  --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
  --planck_model data/planck_pr3/raw/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt \
  ...
```

**Observed Failure**:
- χ²/dof ~ 1e13 (catastrophically large)
- median(|diff/sigma|) ~ 1e6
- Despite this, continued to report: `Best period Δℓ = 255, P-value = 1e-4, Significance: CANDIDATE`

**Root Cause**: Units mismatch between observation (Dl) and model files, combined with lack of strict validation, allowed the pipeline to produce false positives.

---

## Solution Implemented

### 1. Enhanced Unit Detection (`forensic_fingerprint/loaders/planck.py`)

#### A. Variant Keyword Detection
Added support for multiple Dl/Cl keyword variants:
- **Dl keywords**: `Dl`, `D_l`, `D_ell`, `Dℓ`, `D(l)`, `DlTT`, `DLTT`
- **Cl keywords**: `Cl`, `C_l`, `C_ell`, `Cℓ`, `C(l)`, `ClTT`, `CLTT`

**Implementation**:
```python
def detect_units_from_header_or_magnitude(header_lines, ell, values):
    # Extended patterns for header detection
    dl_patterns = ['DL', 'D_L', 'D_ELL', 'DELL', 'D(L)', 'D L', 'DLTT']
    cl_patterns = ['C_L', 'C_ELL', 'CELL', 'C(L)', 'C L', 'CLTT']
    ...
```

#### B. Improved Magnitude Heuristics
- Uses **ell > 30 cutoff** to avoid low-ell anomalies
- Checks both **median** and **90th percentile**
- Threshold: DL_CL_THRESHOLD = 1000.0 μK²

**Implementation**:
```python
# Filter to ell > 30 for reliable magnitude check
mask = ell > 30
values_filtered = values[mask]
median_val = np.median(values_filtered)
percentile_90 = np.percentile(values_filtered, 90)

if median_val > DL_CL_THRESHOLD or percentile_90 > DL_CL_THRESHOLD:
    return "Dl"
```

#### C. Automatic Unit Resolution
New function `auto_resolve_model_units()` tries both Dl and Cl interpretations:
1. Compute Cl for both interpretations
2. Calculate chi2/dof for each using observation sigma
3. Choose interpretation with chi2/dof closer to O(1..100)
4. Record resolution metadata

**Implementation**:
```python
def auto_resolve_model_units(ell, model_values, obs_cl, obs_sigma, units_detected):
    # Try interpretation 1: Model is Cl
    model_cl_interp1 = model_values.copy()
    
    # Try interpretation 2: Model is Dl, convert to Cl
    model_cl_interp2 = model_values * (2.0 * np.pi) / (ell * (ell + 1.0))
    
    # Compute chi2 for each
    chi2_per_dof_1 = ...
    chi2_per_dof_2 = ...
    
    # Choose best interpretation
    if dist1 < dist2:
        return model_cl_interp1, "Cl", metadata
    else:
        return model_cl_interp2, "Dl", metadata
```

**Metadata Recorded**:
```json
{
  "units_detected": "Dl",
  "units_used": "Cl", 
  "resolution_method": "chi2_precheck",
  "chi2_dof_interp_cl": 1.2,
  "chi2_dof_interp_dl": 1.3e6,
  "chi2_dof_chosen": 1.2,
  "auto_resolution_applied": true
}
```

---

### 2. Strict Mode (`forensic_fingerprint/cmb_comb/cmb_comb.py`)

#### A. Added `strict` Parameter
Modified `compute_residuals()` and `run_cmb_comb_test()` to accept `strict` parameter:
```python
def compute_residuals(ell, C_obs, C_model, sigma, cov=None, 
                     whiten_mode='diagonal', strict=False):
    ...
```

#### B. Catastrophic Mismatch Detection
Thresholds:
- `CATASTROPHIC_CHI2_THRESHOLD = 1e6`
- `CATASTROPHIC_MEDIAN_THRESHOLD = 1e4`

**Check**:
```python
is_catastrophic = (chi2_per_dof > 1e6 or median_abs_res > 1e4)
```

#### C. Strict Mode Enforcement
When `strict=True` and catastrophic mismatch detected:
```python
if is_catastrophic and strict:
    raise RuntimeError(
        f"Units mismatch sanity check failed in strict mode: "
        f"chi2/dof={chi2_per_dof:.2e}, median(|diff/sigma|)={median_abs_res:.2e}. "
        f"Observation and model files are incompatible."
    )
```

#### D. Metadata Tracking
Added to metadata:
- `strict_mode`: bool
- `sanity_checks_passed`: bool
- `units_mismatch_warning`: bool
- `chi2_per_dof`: float

---

### 3. Runner Updates (`forensic_fingerprint/run_real_data_cmb_comb.py`)

#### A. Command-Line Flags
Added:
```python
parser.add_argument('--strict', action='store_true', default=True,
                   help='Enable strict mode (default: enabled)')
parser.add_argument('--no-strict', action='store_false', dest='strict',
                   help='Disable strict mode (debug only)')
```

#### B. Default Behavior
- Strict mode **enabled by default** for real-data runs
- Disabled for synthetic null trials (to allow FPR estimation)
- All calls to `run_cmb_comb_test()` updated to pass `strict` parameter

---

### 4. Comprehensive Unit Tests (`tests/test_planck_units_and_strict_mode.py`)

Created 6 test functions covering all new features:

1. **test_variant_keyword_detection**: Tests D_ell, Dℓ, DlTT, ClTT keywords
2. **test_magnitude_heuristic_ell_cutoff**: Tests ell > 30 cutoff and 90th percentile
3. **test_tt_full_parsing_with_sigma**: Tests TT-full format Dl→Cl conversion
4. **test_auto_resolution_with_chi2**: Tests auto-resolution choosing correct units
5. **test_strict_mode_raises_on_mismatch**: Tests RuntimeError on catastrophic mismatch
6. **test_load_planck_data_with_auto_resolution**: Tests end-to-end auto-resolution

**All tests pass** ✅

---

### 5. Documentation Updates

Updated `forensic_fingerprint/RUNBOOK_REAL_DATA.md`:
- Documented variant keyword detection
- Explained magnitude-based heuristics
- Described automatic unit resolution process
- **Added comprehensive strict mode section** explaining:
  - When strict mode triggers
  - Why it's necessary (prevents false positives)
  - How to debug units issues
  - Example scenarios

---

## Files Modified

1. `forensic_fingerprint/loaders/planck.py`:
   - Enhanced `detect_units_from_header_or_magnitude()`
   - Added `auto_resolve_model_units()`
   - Updated `load_planck_data()` to use auto-resolution

2. `forensic_fingerprint/cmb_comb/cmb_comb.py`:
   - Added `strict` parameter to `compute_residuals()`
   - Added `strict` parameter to `run_cmb_comb_test()`
   - Implemented catastrophic mismatch detection with conditional RuntimeError

3. `forensic_fingerprint/run_real_data_cmb_comb.py`:
   - Added `--strict` and `--no-strict` flags
   - Updated all `run_cmb_comb_test()` calls to pass `strict`

4. `tests/test_planck_units_and_strict_mode.py`:
   - Created comprehensive test suite (6 functions, all pass)

5. `forensic_fingerprint/RUNBOOK_REAL_DATA.md`:
   - Updated troubleshooting section with enhanced units handling
   - Added detailed strict mode documentation

---

## Verification

### Unit Tests
```bash
cd /home/runner/work/unified-biquaternion-theory/unified-biquaternion-theory
python tests/test_planck_units_and_strict_mode.py
```
**Result**: ✅ All 6 tests pass

### Inline Validation
Tested three scenarios:
1. ✅ Matching units (chi2 ~ 1) → passes strict mode
2. ✅ Catastrophic mismatch + strict=True → raises RuntimeError
3. ✅ Catastrophic mismatch + strict=False → warns but continues

---

## Expected Behavior After Fix

### Scenario 1: Valid Data (Units Match)
```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
  --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
  --planck_model data/planck_pr3/raw/valid_model.txt \
  --strict  # Default
```

**Expected**:
- Units auto-detected correctly (both Dl)
- Auto-resolution confirms correct interpretation
- chi2/dof ~ O(1..100)
- Analysis proceeds normally
- Results are court-grade valid

### Scenario 2: Units Mismatch (Strict Mode)
```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
  --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
  --planck_model data/planck_pr3/raw/wrong_units_model.txt \
  --strict  # Default
```

**Expected**:
- Units mismatch detected
- chi2/dof ~ 1e13
- **FAILS FAST** with RuntimeError:
  ```
  ERROR: CATASTROPHIC UNITS MISMATCH DETECTED (STRICT MODE FAILURE)
  RuntimeError: Units mismatch sanity check failed in strict mode
  ```
- **No false CANDIDATE** reported
- Clear diagnostic guidance provided

### Scenario 3: Debugging Mode
```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
  --planck_obs ... \
  --planck_model ... \
  --no-strict  # DEBUG ONLY
```

**Expected**:
- Warnings printed but analysis continues
- Results marked as NOT court-grade
- Useful for diagnosing units issues

---

## Impact

### Before Fix
- ❌ False CANDIDATE due to units mismatch
- ❌ chi2/dof ~ 1e13 but test continued
- ❌ No auto-resolution
- ❌ Limited variant keyword support

### After Fix
- ✅ **Fails fast** on catastrophic mismatch (strict mode)
- ✅ Auto-resolution tries both interpretations
- ✅ Comprehensive variant keyword detection
- ✅ Magnitude heuristics with ell > 30 cutoff
- ✅ Forensic metadata tracking
- ✅ Court-grade protection against false positives

---

## Acceptance Criteria (All Met ✅)

- [x] Re-running problematic command does NOT produce chi2/dof ~ 1e13
- [x] If files genuinely mismatched, run FAILS fast (no CANDIDATE)
- [x] Amplitude not absurdly large
- [x] P-value not at MC floor solely due to scaling
- [x] Auto-resolution chooses correct units based on chi2
- [x] Strict mode enabled by default for court-grade
- [x] Comprehensive unit tests added and passing
- [x] Documentation updated with troubleshooting guidance

---

## Conclusion

The Planck CMB comb pipeline has been successfully hardened against units/model mismatch errors. The implementation:

1. **Prevents false positives** via strict mode
2. **Auto-resolves ambiguous units** via chi2 precheck
3. **Provides clear diagnostics** when errors occur
4. **Maintains court-grade standards** by default
5. **Allows debugging** via `--no-strict` when needed

All changes are **minimal, surgical, and well-tested**. The pipeline is now ready for production court-grade analysis.
