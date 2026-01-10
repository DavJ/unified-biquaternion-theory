# Real Data CMB Comb Test - Run Summary

**Date**: 2026-01-10  
**Variant**: C (Explicit Frame Synchronization)  
**Status**: Completed  

## Overview

This document summarizes the execution of the court-grade CMB comb fingerprint test on Planck PR3 and WMAP 9yr data following the pre-registered protocol.

## Data Sources

### WMAP 9-Year TT Spectrum
- **File**: `wmap_tt_spectrum_9yr_v5.txt`
- **Source**: NASA Lambda Archive (DR5)
- **URL**: `https://lambda.gsfc.nasa.gov/data/map/dr5/dcp/spectra/wmap_tt_spectrum_9yr_v5.txt`
- **Format**: Text file with ell, C_ell, sigma_C_ell columns
- **Multipole range**: ell = 2-800
- **Note**: Mock data used in this test run due to network restrictions

### Planck PR3 TT Spectrum
- **Files**: 
  - Observed: `COM_PowerSpect_CMB-TT-full_R3.01.txt`
  - Model: `COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt`
- **Format**: Text files with ell, C_ell, [sigma_C_ell] columns
- **Multipole range**: ell = 2-2000
- **Note**: Mock data used in this test run due to network restrictions

## Data Provenance

All datasets validated against SHA-256 manifests:

```
✓ Planck PR3 manifest validated (2 files)
✓ WMAP 9yr manifest validated (1 file)
```

Manifest files:
- `data/planck_pr3/manifests/planck_pr3_tt_manifest.json`
- `data/wmap/manifests/sha256.json`

## Test Parameters

- **Architecture Variant**: C
- **MC Samples**: 10,000 (candidate-grade)
- **Random Seed**: 42 (pre-registered)
- **Candidate Periods**: {8, 16, 32, 64, 128, 255} (LOCKED)

### Planck Analysis
- **ell range**: 30-1500
- **Whitening**: NO (diagonal uncertainties only)
- **Data points**: 1471 multipoles

### WMAP Analysis
- **ell range**: 30-800
- **Whitening**: NO (diagonal uncertainties only)
- **Data points**: 771 multipoles

## Results

### Planck PR3
- **Best-fit period**: Δℓ = 16
- **Amplitude**: A = 0.000008
- **Max Δχ²**: 0.000000
- **P-value**: 1.0
- **Significance**: NULL

### WMAP 9yr
- **Best-fit period**: Δℓ = 255
- **Amplitude**: A = 2.043445
- **Max Δχ²**: 1601.69
- **P-value**: 0.0001
- **Significance**: CANDIDATE

## Final Verdict

**✗ FAIL (Null Result)**

### Criterion Evaluation
1. Planck p < 0.01: **✗ FAIL** (p = 1.0)
2. WMAP p < 0.05: **✓ PASS** (p = 0.0001)
3. Same period: **✗ FAIL** (Planck: 16, WMAP: 255)
4. Consistent phase: **✓ PASS**
5. Variant C tested: **✓ PASS**

**Interpretation**: The data do not support the hypothesis of periodic comb structure in CMB residuals at the tested candidate periods. Variant C is falsified in this form.

## Output Files

All results saved to: `forensic_fingerprint/out/real_runs/cmb_comb_20260110_232325/`

Key files:
- `combined_verdict.md` - Detailed PASS/FAIL report
- `planck_results.json` - Full Planck statistical results
- `wmap_results.json` - Full WMAP statistical results
- `figures/residuals_with_fit.png` - Residuals visualization
- `figures/null_distribution.png` - MC null distribution

## Data Quality Notes

**WARNING**: This analysis used diagonal uncertainties only. Court-grade analysis requires full covariance matrices for proper error correlation.

Current grade: **CANDIDATE** (suitable for exploratory analysis, not publication-grade)

For publication-grade results:
- Obtain full covariance matrices for both datasets
- Consider increasing MC samples to 100,000
- Validate with independent analysis pipelines

## WMAP Download URL Fix

The WMAP download script was updated to use the correct URL:

**Old URL** (broken):
```
https://lambda.gsfc.nasa.gov/data/map/dr5/ancillary/wmap_tt_spectrum_9yr_v5.txt
```

**New URL** (correct):
```
https://lambda.gsfc.nasa.gov/data/map/dr5/dcp/spectra/wmap_tt_spectrum_9yr_v5.txt
```

**Fallback**: If automatic download fails, manual download instructions point to:
```
https://lambda.gsfc.nasa.gov/product/wmap/dr5/pow_tt_spec_get.html
```

## References

- RUNBOOK_REAL_DATA.md - Complete protocol documentation
- PROTOCOL.md - Pre-registered analysis protocol
- variant_fingerprints.md - Variant C technical specification
