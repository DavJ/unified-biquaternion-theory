# CMB Comb Test Units Mismatch Fix - Summary

## Problem Statement

The CMB comb test was failing with catastrophic chi2/dof ~ 1e13 due to units mismatch between Planck observation and model files.

### Symptoms
- `chi2/dof ~ 1e13`
- `std(diff) ~ 1.3e3, std(sigma) ~ 1.6e-1`
- `median(|diff/sigma|) ~ 1.8e6`
- WARNING: POSSIBLE UNITS MISMATCH OR WRONG MODEL

### Root Cause
The Planck observation file (`COM_PowerSpect_CMB-TT-full_R3.01.txt`) uses Dl units with format:
```
# l Dl -dDl +dDl
30 1000.5 -12.3 12.5
```

The model file (`COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt`) also uses Dl units but with multi-column format:
```
# L  TT  TE  EE  BB
2  5.51e+01  -1.18e+01  1.34e-02  ...
```

While the code had basic units detection, it wasn't robust enough to handle all cases correctly.

## Solution Implemented

### 1. Enhanced Units Detection (`detect_units_from_header_or_magnitude()`)

**Two-stage detection approach:**

**Stage 1: Header-based detection**
- Scans header lines for keywords: "Dl", "D_l", "D(l)", "Cl", "C_l", "C(l)"
- Excludes error column markers like "-dDl", "+dDl"
- More reliable than magnitude alone

**Stage 2: Magnitude-based fallback**
- Uses median value threshold (DL_CL_THRESHOLD = 1000.0)
- For ell > 10: if median > 1000, assume Dl; otherwise Cl
- Handles files without explicit headers

### 2. Sigma Validation

**Early detection of problems:**
- Validates sigma > 0 (catches zero or negative uncertainties)
- Checks sigma-to-signal ratio (detects units mismatch early)
- Issues warnings for suspiciously small or large ratios

### 3. Improved Logging

**Clear conversion messages:**
```
Observation file units detected: Dl
  → Converted from Dl to Cl using: Cl = Dl × 2π / [l(l+1)]
Model file units detected: Dl
  → Converted from Dl to Cl using: Cl = Dl × 2π / [l(l+1)]
```

### 4. Enhanced Documentation

Updated `RUNBOOK_REAL_DATA.md` with:
- Explicit explanation of Planck file types
- Units handling documentation
- Troubleshooting section for units mismatch
- Examples of correct vs incorrect files

## Files Modified

1. **forensic_fingerprint/loaders/planck.py**
   - Added `detect_units_from_header_or_magnitude()` helper
   - Enhanced all loading functions to use new detection
   - Added sigma validation with ratio checks
   - Improved conversion logging

2. **forensic_fingerprint/RUNBOOK_REAL_DATA.md**
   - Enhanced "Units Mismatch Warning" section
   - Added file format documentation
   - Added troubleshooting examples

3. **forensic_fingerprint/tests/test_units_handling.py**
   - Added `test_detect_units_from_header_or_magnitude()`
   - Updated existing test to include sigma column
   - All 8 tests passing

4. **test_units_fix.py** (new validation script)
   - Creates synthetic Planck-format files
   - Tests units detection and conversion
   - Tests residuals computation
   - Tests sigma validation
   - All 3 validation tests passing

## Verification Steps

### 1. Run Unit Tests

```bash
cd /path/to/unified-biquaternion-theory
python -m pytest forensic_fingerprint/tests/test_units_handling.py -v
```

**Expected output:**
```
8 passed
```

### 2. Run Validation Script

```bash
python test_units_fix.py
```

**Expected output:**
```
ALL VALIDATION TESTS PASSED!
  ✓ Units are correctly detected from headers and magnitudes
  ✓ Dl → Cl conversion works for both obs and model files
  ✓ Residuals computation does not trigger catastrophic chi2
  ✓ Sigma validation catches invalid uncertainties
```

### 3. Test with Real Planck Files

```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model data/planck_pr3/raw/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt \
    --planck_manifest data/planck_pr3/manifests/planck_pr3_tt_manifest.json \
    --ell_min_planck 30 --ell_max_planck 1500 \
    --variant C --mc_samples 10000
```

**Expected behavior:**
1. ✅ Units detection messages appear
2. ✅ Both files show "Dl" detected and converted
3. ✅ No catastrophic chi2 warning
4. ✅ chi2/dof is reasonable (< 100)
5. ✅ `planck_results.json` contains units metadata
6. ✅ `combined_verdict.md` is generated

### 4. Check Results

Inspect `planck_results.json` for units metadata:
```json
{
  "obs_units": "Dl",
  "model_units_original": "Dl",
  "model_units_used": "Cl",
  "sigma_method": "from_file",
  "chi2_dof": 1.23,
  "sanity_checks_passed": true
}
```

## Technical Details

### Conversion Formula

```
Dl → Cl conversion:
Cl = Dl × 2π / [ℓ(ℓ+1)]
```

Special cases:
- ell=0, ell=1: set to 0 (avoid division by zero)
- Sigma converted using same formula

### Detection Thresholds

- **DL_CL_THRESHOLD = 1000.0 μK²**
  - Typical Cl values: ~10-1000 μK² at ell > 10
  - Typical Dl values: ~1000-5000 μK² at ell > 10

- **Catastrophic chi2 threshold = 1e6**
  - If chi2/dof > 1e6, raises RuntimeError in court-grade mode
  - Indicates severe units mismatch or wrong file

- **Sigma-to-signal ratio thresholds**
  - Very small (< 1e-6): Warning, possible units mismatch
  - Very large (> 10): Warning, possible poor quality or wrong units

## What Was NOT Changed

To maintain forensic integrity:

1. **No changes to PROTOCOL.md** - Pre-registered thresholds unchanged
2. **No changes to candidate periods** - Still [8, 16, 32, 64, 128, 255]
3. **No changes to chi2 computation** - Same statistical test
4. **No changes to verdict criteria** - Same PASS/FAIL rules

## Expected Impact

### Before Fix
- chi2/dof ~ 1e13 (catastrophic)
- Units mismatch warning
- Test fails to produce meaningful results
- User confusion about correct files

### After Fix
- chi2/dof ~ O(1) (reasonable)
- No units mismatch warning (if files correct)
- Test produces valid statistical results
- Clear logging shows what happened
- Better error messages guide users

## Troubleshooting

### If chi2/dof still very high

1. **Check you're using correct files:**
   - Observation: `COM_PowerSpect_CMB-TT-full_R3.01.txt`
   - Model: `COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt`

2. **Verify file integrity:**
   - Check file sizes (~167 KB for TT-full)
   - Verify not HTML error page
   - Re-download if corrupted

3. **Check console output:**
   - Look for "Units detected: Dl → Converted"
   - Verify both obs and model show conversion
   - Check for any warnings about sigma

### If units detection fails

1. **Examine file header:**
   ```bash
   head -10 your_file.txt
   ```

2. **Check for expected patterns:**
   - TT-full: `# l Dl -dDl +dDl`
   - Minimum: `# L  TT  TE  EE  BB`

3. **Verify data magnitudes:**
   - Dl values: typically 1000-5000 μK²
   - Cl values: typically 10-1000 μK²

## Next Steps

1. Test with actual Planck PR3 files
2. Verify combined_verdict.md generation
3. Document actual chi2/dof values obtained
4. If successful, mark issue as resolved

## References

- **Issue**: CMB comb test Planck units/model mismatch
- **Code**: `forensic_fingerprint/loaders/planck.py`
- **Docs**: `forensic_fingerprint/RUNBOOK_REAL_DATA.md`
- **Tests**: `forensic_fingerprint/tests/test_units_handling.py`
- **Validation**: `test_units_fix.py`
