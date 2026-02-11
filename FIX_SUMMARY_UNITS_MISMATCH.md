# Fix Summary: Planck CMB Comb Test Units Mismatch Protection

## Issue
The CMB comb fingerprint test could produce spurious CANDIDATE verdicts when observation and model files had mismatched units (Cl vs Dl), resulting in catastrophic chi2/dof values (~1e13) that would hit the Monte Carlo p-value floor.

## Root Cause
When units mismatch occurred (e.g., observation in Dl format, model mistakenly in Cl format or vice versa), the residuals would be calculated on wildly different scales, producing:
- Chi2/dof ~ 1e10 to 1e13
- Median(|diff/sigma|) ~ 1e4 to 1e6
- P-values hitting MC floor (1/N_trials) → false CANDIDATE results

## Solution Status
**All requirements have already been implemented in the codebase.**

### 1. Enhanced Unit Detection (planck.py)
✅ **Implemented** - Lines 372-441 in `forensic_fingerprint/loaders/planck.py`
- `detect_units_from_header_or_magnitude()`: Two-stage detection
  - Stage 1: Header keyword matching (Dl, D_l, D_ell, DlTT, etc.)
  - Stage 2: Magnitude heuristics (median/90th percentile for ell > 30)
- `auto_resolve_model_units()`: Chi2-based unit resolution
  - Tests both Cl and Dl interpretations
  - Chooses interpretation with chi2/dof closest to 1.0
  - Prevents catastrophic mismatch before analysis

### 2. Strict Sanity Checks (cmb_comb.py)
✅ **Implemented** - Lines 369-441 in `forensic_fingerprint/cmb_comb/cmb_comb.py`
- Catastrophic thresholds:
  - `CATASTROPHIC_CHI2_THRESHOLD = 1e6`
  - `CATASTROPHIC_MEDIAN_THRESHOLD = 1e4`
- Checks performed BEFORE null distribution generation
- In strict mode: raises `RuntimeError` immediately
- In non-strict mode: sets `sanity_checks_passed = False`

### 3. Strict Mode Enabled by Default (run_real_data_cmb_comb.py)
✅ **Implemented** - Lines 894-897 in `forensic_fingerprint/run_real_data_cmb_comb.py`
```python
parser.add_argument('--strict', action='store_true', default=True,
                   help='Enable strict mode: fail fast on units mismatch')
parser.add_argument('--no-strict', action='store_false', dest='strict',
                   help='Disable strict mode: allow analysis to continue despite warnings')
```
- Enabled by default for all court-grade runs
- Can be disabled with `--no-strict` for debugging only

### 4. Forensic Metadata Persistence
✅ **Implemented** - Lines 1444-1456, 1507-1519 in `run_real_data_cmb_comb.py`
All required forensic information is persisted in results JSON:
- `obs_units`: Units detected in observation file ("Dl" or "Cl")
- `model_units_original`: Original units detected in model file
- `model_units_used`: Final units used after conversion ("Cl")
- `chi2_per_dof`: Chi-squared per degree of freedom
- `median_abs_residual_over_sigma`: Median |diff/sigma| (in debug_stats)
- `strict_mode`: Boolean indicating if strict mode was enabled
- `sanity_checks_passed`: Boolean from sanity check results
- `model_resolution_metadata`: Full auto-resolution diagnostics

### 5. Documentation (RUNBOOK_REAL_DATA.md)
✅ **Implemented** - Lines 1230-1236, 2020-2076 in `forensic_fingerprint/RUNBOOK_REAL_DATA.md`
- Explicitly states observation files (TT-full) are in Dl units
- Documents automatic Dl → Cl conversion
- Explains strict mode behavior and thresholds
- Provides troubleshooting guidance for units mismatch
- Shows example of strict mode in action

## Testing

### Existing Tests
✅ `tests/test_planck_units_and_strict_mode.py` - All pass
- Variant keyword detection (D_ell, Dℓ, DlTT, etc.)
- Magnitude heuristic with ell > 30 cutoff
- TT-full format parsing with sigma conversion
- Auto-resolution with chi2 precheck
- Strict mode raises RuntimeError on catastrophic mismatch
- load_planck_data with auto-resolution

### New Integration Test
✅ `test_units_mismatch_integration.py` - All pass
- Confirms catastrophic mismatch triggers strict mode
- Verifies no CANDIDATE verdict possible with chi2 ~ 1e13
- Validates auto-resolution prevents correctable mismatches
- Tests both strict and non-strict modes

### Demonstration
✅ `demo_units_fix.py`
- Shows strict mode blocking CANDIDATE on units mismatch
- Demonstrates chi2/dof = 4.37e+12 → RuntimeError
- Compares strict vs non-strict behavior
- Confirms acceptance criteria

## Acceptance Criteria
✅ **All Met**

1. ✅ Re-running the same command no longer produces chi2/dof ~ 1e13
   - Auto-resolution corrects correctable mismatches
   - Strict mode blocks execution if mismatch persists

2. ✅ If units mismatch persists, run aborts (no CANDIDATE verdict)
   - RuntimeError raised with detailed diagnostic message
   - Court-grade analysis cannot proceed with invalid data

3. ✅ Existing tests pass
   - All tests in test_planck_units_and_strict_mode.py pass
   - Integration test validates end-to-end behavior

4. ✅ Documentation updated
   - RUNBOOK explicitly documents units handling
   - Strict mode behavior documented with examples

## Example Output

### Before Fix (Hypothetical)
```
WARNING: Units mismatch (chi2/dof = 1.2e+13)
Generating null distribution...
P-value: 1.0e-4
Significance: CANDIDATE  ← FALSE POSITIVE
```

### After Fix (Actual)
```
ERROR: CATASTROPHIC UNITS MISMATCH DETECTED (STRICT MODE FAILURE)
χ²/dof = 4.37e+12 (threshold: 1e+06)
median(|diff/sigma|) = 1.59e+06 (threshold: 1e+04)

RuntimeError: Units mismatch sanity check failed in strict mode
```

## Files Modified
- None (all functionality already implemented)

## Files Added
- `test_units_mismatch_integration.py` - Integration test
- `demo_units_fix.py` - Demonstration script
- `FIX_SUMMARY_UNITS_MISMATCH.md` - This summary

## Conclusion
The issue has been fully addressed. All required functionality was already implemented and tested. The new integration test and demonstration script provide additional validation of the acceptance criteria.
