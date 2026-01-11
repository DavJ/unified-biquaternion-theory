# Court-Grade Runbook: Real CMB Data Analysis

**Purpose**: Step-by-step instructions for running CMB comb fingerprint test on real Planck PR3 and WMAP datasets with full reproducibility and provenance tracking.

**Status**: Pre-registered protocol v1.0  
**Last Updated**: 2026-01-10  
**Author**: UBT Research Team

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Quick Real Run (One Command)](#quick-real-run-one-command)
4. [Data Download and Validation](#data-download-and-validation)
5. [Running CMB Comb Test: Planck PR3](#running-cmb-comb-test-planck-pr3)
6. [Running CMB Comb Test: WMAP (Replication)](#running-cmb-comb-test-wmap-replication)
7. [Interpreting Results](#interpreting-results)
8. [PASS/FAIL Criteria](#passfail-criteria)
9. [Troubleshooting](#troubleshooting)
10. [Archiving Results](#archiving-results)

---

## Overview

This runbook implements the **pre-registered protocol** for detecting periodic "comb" signatures in CMB power spectrum residuals. The protocol is designed to be:

- **Reproducible**: All steps documented, SHA-256 hashes for data provenance
- **Court-grade**: Suitable for peer review and independent verification
- **Conservative**: Multiple datasets, look-elsewhere correction, strict thresholds

**Key Principle**: Any significant signal **must** appear in both Planck and WMAP to be considered real.

---

## Prerequisites

### Software Requirements

```bash
# Python 3.8+
python --version

# Required packages
pip install numpy scipy matplotlib

# Optional (for FITS files)
pip install astropy
```

### Repository Setup

```bash
# Clone repository
git clone https://github.com/DavJ/unified-biquaternion-theory.git
cd unified-biquaternion-theory

# Verify tools exist
ls -l tools/data_download/
ls -l tools/data_provenance/
ls -l forensic_fingerprint/loaders/
```

### Important: manifest generation must be repo-root relative

`tools/data_provenance/hash_dataset.py` stores file paths relative to the **repo root**.
If you generate manifests from a deep subdirectory in a ZIP checkout (no `.git/`),
older versions could accidentally store paths relative to the wrong base.

**Recommended** (run from repo root):

```bash
# Planck PR3 TT observation spectrum
# Note: Only include files you will actually use in analysis
mkdir -p data/planck_pr3/manifests
python tools/data_provenance/hash_dataset.py \
  data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
  > data/planck_pr3/manifests/planck_pr3_tt_manifest.json

# If using a theoretical model spectrum, add it to the manifest:
# python tools/data_provenance/hash_dataset.py \
#   data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
#   data/planck_pr3/raw/your_theoretical_model.txt \
#   > data/planck_pr3/manifests/planck_pr3_tt_manifest.json

# WMAP9 TT
mkdir -p data/wmap/manifests
python tools/data_provenance/hash_dataset.py \
  data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
  > data/wmap/manifests/wmap_tt_manifest.json
```


---

## Quick Real Run (One Command)

**NEW**: For users who want to run the complete CMB comb test with a single command.

### What This Does

The `run_real_data_cmb_comb.py` script provides a one-command entrypoint that:

1. Validates dataset manifests (SHA-256 hashes) if provided
2. Loads Planck PR3 and/or WMAP data using existing loaders
3. Runs CMB comb test on both datasets
4. Generates a court-grade combined verdict report (PASS/FAIL)
5. Saves all results with timestamps in a structured output directory

**Note**: As of the recent update, the runner now works correctly **regardless of your current working directory**. You can run it from the repository root, from `forensic_fingerprint/`, or from any other directory. All paths are automatically resolved relative to the repository root.

### Minimal Example (Planck Only)

**From forensic_fingerprint directory:**
```bash
cd forensic_fingerprint

python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/spectrum.txt \
    --planck_model ../data/planck_pr3/raw/model.txt
```

**From repository root (also works):**
```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt
```

**Output**:
- Creates `out/real_runs/cmb_comb_<timestamp>/` directory
- `planck_results.json` - Full statistical results
- `combined_verdict.md` - Human-readable PASS/FAIL report
- `figures/*.png` - Diagnostic plots

### Full Example (Planck + WMAP with Validation)

```bash
cd forensic_fingerprint

python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model ../data/planck_pr3/raw/theoretical_model_spectrum.txt \
    --planck_manifest ../data/planck_pr3/manifests/planck_pr3_tt_manifest.json \
    --wmap_obs ../data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_manifest ../data/wmap/manifests/wmap_tt_manifest.json \
    --ell_min_planck 30 --ell_max_planck 1500 \
    --ell_min_wmap 30 --ell_max_wmap 800 \
    --variant C --mc_samples 10000
```

**Note**: Replace `theoretical_model_spectrum.txt` with your actual theoretical model file (e.g., from CAMB/CLASS or a Planck "minimum-theory" file). Alternatively, use the TT-full file for both obs and model to test noise characteristics.

**Output**:
- `planck_results.json` - Planck statistical results
- `wmap_results.json` - WMAP statistical results
- `combined_verdict.md` - **READ THIS for PASS/FAIL decision**
- `figures/*.png` - All diagnostic plots

### High-Confidence Run (100k MC Samples)

For publication-grade analysis, increase MC samples to 100,000:

```bash
python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/spectrum.txt \
    --planck_model ../data/planck_pr3/raw/model.txt \
    --wmap_obs ../data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --mc_samples 100000 \
    --variant C
```

**Note**: 100k MC samples provides stronger statistical confidence but takes ~10x longer (~5-10 minutes vs ~30-60 seconds).

### Command-Line Options

#### Required
- `--planck_obs`: Planck observed spectrum file (required)

#### Optional: Planck Data
- `--planck_model`: Planck model spectrum file (default: zeros)
- `--planck_cov`: Planck covariance matrix (enables whitening, court-grade)
- `--planck_manifest`: SHA-256 manifest for Planck data validation
- `--ell_min_planck`: Minimum Planck multipole (default: 30)
- `--ell_max_planck`: Maximum Planck multipole (default: 1500)

#### Optional: WMAP Data
- `--wmap_obs`: WMAP observed spectrum file
- `--wmap_model`: WMAP model spectrum file (default: zeros)
- `--wmap_cov`: WMAP covariance matrix (enables whitening)
- `--wmap_manifest`: SHA-256 manifest for WMAP data validation
- `--ell_min_wmap`: Minimum WMAP multipole (default: 30)
- `--ell_max_wmap`: Maximum WMAP multipole (default: 800)

#### Test Parameters
- `--variant {A,B,C,D}`: Architecture variant to test (default: C)
  - **C** = Explicit Frame Synchronization (predicts periodic signal)
  - **A** = No Synchronization (predicts null)
  - **B** = Implicit Synchronization (predicts null for comb test)
  - **D** = Hierarchical Synchronization (scale-dependent)
- `--mc_samples`: Number of Monte Carlo samples (default: 5000 for candidate-grade, 100000 for strong)
- `--seed`: Random seed for reproducibility (default: 42, pre-registered)

#### Output
- `--output_dir`: Custom output directory (default: auto-generated timestamp)

### Understanding the Output

The script creates a structured output directory:

```
out/real_runs/cmb_comb_<timestamp>/
├── planck_results.json          # Full Planck results (JSON)
├── wmap_results.json            # Full WMAP results (JSON)
├── combined_verdict.md          # ★ COURT-GRADE PASS/FAIL REPORT ★
└── figures/
    ├── residuals_with_fit.png   # Planck residuals + fitted sinusoid
    ├── null_distribution.png    # Planck p-value visualization
    ├── residuals_with_fit_1.png # WMAP residuals + fitted sinusoid
    └── null_distribution_1.png  # WMAP p-value visualization
```

**Key file**: `combined_verdict.md` contains the PASS/FAIL decision based on protocol criteria.

### Court-Grade vs Candidate-Grade

**Candidate-Grade** (default):
- Uses diagonal uncertainties only
- 5,000 MC samples
- Suitable for initial exploration
- ~30-60 seconds runtime

**Court-Grade** (recommended for publication):
- Requires full covariance matrix (`--planck_cov`, `--wmap_cov`)
- 100,000 MC samples (`--mc_samples 100000`)
- Suitable for peer review
- ~5-10 minutes runtime

The script will print warnings if covariance is not provided:

```
WARNING (Planck): Diagonal uncertainties only.
This is candidate-grade only. Court-grade requires covariance.
```

### Example Session

```bash
$ cd forensic_fingerprint

$ python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/spectrum.txt \
    --planck_model ../data/planck_pr3/raw/model.txt \
    --wmap_obs ../data/wmap/raw/wmap_spectrum.txt \
    --variant C --mc_samples 10000

================================================================================
UBT FORENSIC FINGERPRINT - ONE-COMMAND CMB COMB TEST
================================================================================
Output directory: out/real_runs/cmb_comb_20260110_150423
Variant: C
MC samples: 10000
Random seed: 42

================================================================================
RUNNING PLANCK PR3 ANALYSIS
================================================================================

Loading Planck data...
Loaded 1471 multipoles (ℓ = 30 to 1500)

Using diagonal uncertainties (no covariance provided)
Generating null distribution (10000 trials, this may take a moment)...

============================================================
CMB COMB TEST RESULTS
============================================================
Dataset: Planck PR3
Whitening: NO (diagonal only)
Best period: Δℓ = 255
Amplitude: A = 0.1234
Phase: φ = 1.5708 rad (90.00°)
Max Δχ²: 15.67
P-value: 3.45e-03
Significance: CANDIDATE
============================================================

Results saved to: out/real_runs/cmb_comb_20260110_150423/planck_results.json

[... WMAP analysis follows ...]

================================================================================
GENERATING COMBINED VERDICT
================================================================================

Combined verdict saved to: out/real_runs/cmb_comb_20260110_150423/combined_verdict.md

================================================================================
ANALYSIS COMPLETE
================================================================================

All results saved to: out/real_runs/cmb_comb_20260110_150423

Key files:
  - planck_results.json
  - wmap_results.json
  - combined_verdict.md (READ THIS FOR PASS/FAIL DECISION)
  - figures/*.png

Quick Summary:
  Planck: p = 3.45e-03, period = 255, sig = candidate
  WMAP:   p = 4.21e-02, period = 255, sig = candidate

See combined_verdict.md for detailed PASS/FAIL evaluation.
```

### Next Steps

After running:

1. **Read `combined_verdict.md`** - Contains PASS/FAIL decision and detailed statistics
2. **Check figures** - Visual inspection of residuals and fits
3. **Archive results** - If PASS, follow archiving procedures (see [Archiving Results](#archiving-results))
4. **Share** - JSON files are machine-readable for independent replication

---


---

## Court-Grade Whitening with Full Covariance

**Purpose**: Use full covariance matrices to properly account for error correlations between multipoles, providing the most rigorous statistical analysis.

**Status**: Available as of v1.1  
**Requirement**: Full covariance matrix files for Planck and/or WMAP

---

### Why Full Covariance Matters

**Standard approach (diagonal-only)**:
- Treats each multipole as independent
- Uses only σ_ℓ (diagonal uncertainties)
- Simple but ignores correlations
- **Grade**: Candidate-grade

**Court-grade approach (full covariance)**:
- Accounts for correlations between nearby multipoles
- Uses full N×N covariance matrix
- More conservative and rigorous
- **Grade**: Court-grade / publication-ready

**Key differences**:
1. Full covariance properly whitens correlated errors
2. p-values are more reliable (no underestimation of errors)
3. Required for publishable claims

---

### Required Covariance Files

You need N×N covariance matrices matching your ℓ-range.

**Supported formats**:
- `.npy`: NumPy binary (recommended for large matrices)
- `.txt`, `.dat`, `.csv`: Plain text whitespace/comma-separated
- `.fits`: FITS table (requires astropy)

**File structure**:
```
data/planck_pr3/covariance/
  planck_pr3_tt_covariance_ell30_1500.npy   # 1471×1471 matrix
  
data/wmap/covariance/
  wmap_tt_covariance_ell30_800.npy          # 771×771 matrix
```

**Creating covariance files**:

From Python:
```python
import numpy as np

# Your covariance matrix (N×N, must be symmetric positive semi-definite)
cov = ...  # Computed from your data

# Save as .npy (recommended)
np.save('planck_pr3_tt_covariance_ell30_1500.npy', cov)

# Or save as text (for human inspection)
np.savetxt('covariance.txt', cov, fmt='%.6e')
```

**Important**:
- Matrix must be **symmetric**: C[i,j] = C[j,i]
- Matrix must be **positive semi-definite**: all eigenvalues ≥ 0
- Size must match your ℓ-range selection

---

### Example Commands

#### Candidate-Grade (Diagonal Only)

**Default behavior** - no covariance files needed:

```bash
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --whiten diag
```

**Whitening**: Diagonal uncertainties only  
**Grade**: Candidate (suitable for initial exploration)

---

#### Court-Grade (Full Covariance)

**With full covariance matrices**:

```bash
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance/planck_cov.npy \
    --wmap_obs data/wmap/raw/spectrum.txt \
    --wmap_cov data/wmap/covariance/wmap_cov.npy \
    --whiten full \
    --cov_method cholesky \
    --cov_jitter 1e-12 \
    --mc_samples 100000
```

**Whitening**: Full Cholesky decomposition  
**Grade**: Court-grade (publication-ready)

**Flags explained**:
- `--whiten full`: Use full covariance whitening
- `--cov_method cholesky`: Factorization method (cholesky or eigh)
- `--cov_jitter 1e-12`: Regularization parameter for numerical stability
- `--mc_samples 100000`: High MC count for strong confidence

---

### Covariance Validation

The pipeline automatically validates covariance matrices:

**Checks performed**:
1. **Symmetry**: C = C^T (within tolerance)
2. **Finite values**: No NaN or Inf
3. **Positive semi-definite**: All eigenvalues ≥ 0
4. **Size match**: Matrix dimension = number of multipoles

**Example output**:
```
Covariance validation:
  Symmetric: True
  Positive definite: True
  Min eigenvalue: 1.234567e-05
  Max eigenvalue: 9.876543e+03
  Condition number: 8.012345e+08
  ℓ-range: (30, 1500)
```

**If regularization is needed**:
```
WARNING: Covariance is ill-conditioned (cond=1.23e+10)
         Applying ridge regularization...
         Ridge parameter λ = 1.000000e-12
         After regularization:
           Condition number: 8.012345e+08
           Min eigenvalue: 1.234567e-05
```

---

### Troubleshooting

#### Error: "Covariance matrix is not symmetric"

**Cause**: Matrix is not C = C^T

**Fix**:
```python
# Symmetrize manually
cov_sym = 0.5 * (cov + cov.T)
np.save('cov_fixed.npy', cov_sym)
```

---

#### Error: "Covariance matrix is not positive semi-definite"

**Cause**: Negative eigenvalues (numerical errors or invalid covariance)

**Fix 1** - Let pipeline auto-jitter:
```bash
# Pipeline applies automatic jitter if needed
python run_real_data_cmb_comb.py ... --whiten full
```

**Fix 2** - Increase jitter manually:
```bash
python run_real_data_cmb_comb.py ... --whiten full --cov_jitter 1e-10
```

**Fix 3** - Use eigenvalue method:
```bash
python run_real_data_cmb_comb.py ... --whiten full --cov_method eigh
```

The eigh method is more robust for ill-conditioned matrices.

---

#### Error: "Covariance size doesn't match data size"

**Cause**: Matrix dimension ≠ number of multipoles in selected ℓ-range

**Example**:
```
ERROR: Covariance matrix size (1000) doesn't match data size (1471)
```

**Fix**: Provide covariance matching your ℓ-range, or adjust ℓ-range:
```bash
# If cov is for ℓ=30-1029 (1000 multipoles)
python run_real_data_cmb_comb.py \
    --planck_obs ... \
    --planck_cov data/planck_pr3/covariance/cov_ell30_1029.npy \
    --ell_min_planck 30 \
    --ell_max_planck 1029
```

---

#### Warning: "χ²/dof >> 1 suggests possible units mismatch"

**Cause**: Observation and model may have different units (C_ℓ vs D_ℓ)

**Check**:
1. Both files use same units (μK² for C_ℓ, or ℓ(ℓ+1)C_ℓ/2π for D_ℓ)
2. Model corresponds to correct observation
3. Uncertainties are correctly loaded

**Fix**: Verify data files are in consistent units.

---

### Output: whitening_info.json

When using `--whiten full`, the pipeline saves whitening metadata:

```json
{
  "mode": "full",
  "cov_path": "data/planck_pr3/covariance/planck_cov.npy",
  "cov_hash": "a1b2c3d4...",
  "cov_source": "Planck PR3 TT covariance",
  "jitter": 1e-12,
  "method": "cholesky",
  "min_eig_before": 1.234e-05,
  "min_eig_after": 1.235e-05,
  "condition_number_before": 8.012e+08,
  "condition_number_after": 7.998e+08,
  "N": 1471,
  "ell_range": [30, 1500]
}
```

This ensures full reproducibility of the whitening transformation.

---

### Validation: Whitening Calibration Test

The pipeline runs automatic calibration to verify whitening works correctly:

```
Running whitening calibration test...
  Mean variance: 1.0023 (expected: 1.0)
  Mean |correlation|: 0.0145 (expected: ~0)
  ✓ Calibration PASSED
```

**Interpretation**:
- Mean variance ≈ 1.0: Whitened residuals have unit variance
- Mean correlation ≈ 0: Correlations removed
- PASSED: Whitening is working correctly

**If calibration fails**: Check covariance matrix validity or increase jitter.

---

### When to Use Each Mode

| Mode | Use Case | Requirements | Grade |
|------|----------|--------------|-------|
| `none` | Debugging only | None | Not valid |
| `diag` | Initial exploration | Diagonal σ_ℓ | Candidate |
| `full` | Publication claims | Full cov matrix | Court-grade |

**Recommendation**: Always use `--whiten full` with full covariance for final publishable results.

---

### Example Workflow

```bash
# 1. Download data
wget <planck_url> -O data/planck_pr3/raw/spectrum.txt
wget <planck_cov_url> -O data/planck_pr3/covariance/cov.npy

# 2. Validate covariance (optional sanity check)
python -c "
import numpy as np
cov = np.load('data/planck_pr3/covariance/cov.npy')
print(f'Shape: {cov.shape}')
print(f'Symmetric: {np.allclose(cov, cov.T)}')
eigs = np.linalg.eigvalsh(cov)
print(f'Min eig: {np.min(eigs):.6e}')
print(f'Max eig: {np.max(eigs):.6e}')
"

# 3. Run court-grade analysis
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance/cov.npy \
    --whiten full \
    --mc_samples 100000 \
    --output_dir out/court_grade_run1

# 4. Check whitening_info.json
cat out/court_grade_run1/whitening_info.json

# 5. Review combined_verdict.md
cat out/court_grade_run1/combined_verdict.md
```

---

**Next**: See [Data Download and Validation](#data-download-and-validation) for obtaining covariance matrices.

## Data Download and Validation

**Note**: If you've already downloaded data and just want to run the test, use the [Quick Real Run](#quick-real-run-one-command) above.

### Step 1: Download Planck PR3 Data

```bash
# Run download script
bash tools/data_download/download_planck_pr3_cosmoparams.sh
```

**Required files** (automatically downloaded):
- `COM_PowerSpect_CMB-TT-full_R3.01.txt` - Observed TT power spectrum (~167 KB)
- `COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt` - Cosmological parameters table (likelihood minimum, NOT a power spectrum)

**IMPORTANT: Planck Model File Selection**

The Planck PR3 archive contains different types of files. For CMB comb analysis, you need:

**✓ CORRECT files for power spectrum (--planck_obs and potentially --planck_model):**
- `COM_PowerSpect_CMB-TT-full_R3.01.txt` - Observed TT spectrum with uncertainties (~2479 rows, ~167 KB)
- `COM_PowerSpect_CMB-TT-binned_R3.01.txt` - Binned version (if using binned analysis)
- `*-minimum-theory*.txt` files - Theoretical model power spectra (derived from best-fit cosmological parameters)
- CAMB or CLASS output - Theoretical ΛCDM spectra generated with Planck best-fit parameters

**✗ INCORRECT files (DO NOT use as --planck_model):**
- `COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt` - Cosmological parameter table (contains `-log(Like)` likelihood values and best-fit parameters, NOT a power spectrum)
- Other files containing `-log(Like)` or likelihood values in the data (these are parameter/likelihood tables, not spectra)

**Why this matters:**
The "minimum" cosmological parameter files (like `*-plikHM-*-minimum_R3.01.txt`) contain best-fit cosmological parameters and likelihood values, not power spectra. These will be rejected by content validation.

However, "minimum-theory" files contain the theoretical power spectrum derived from those best-fit parameters and are valid model files.

**Recommended approach for model spectrum:**

1. **Preferred: Explicit theoretical model (best for scientific analysis)**
   ```bash
   # Use a theoretical model spectrum file:
   # - "minimum-theory" files from Planck archive (theoretical spectra from best-fit params)
   # - ΛCDM spectrum generated using CAMB or CLASS with Planck best-fit parameters
   python run_real_data_cmb_comb.py \
       --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
       --planck_model path/to/theoretical_model_spectrum.txt
   ```
   This analyzes residuals between observation and theory.

2. **Fallback: TT-full as both observation and model (noise analysis)**
   ```bash
   # Use the same file for both obs and model
   python run_real_data_cmb_comb.py \
       --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
       --planck_model data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt
   ```
   This results in zero residuals (obs - obs = 0), testing pure noise for periodic structure.
   Useful for validating the statistical framework.

3. **Fallback: No model specified (absolute spectrum analysis)**
   ```bash
   # Omit --planck_model
   python run_real_data_cmb_comb.py \
       --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt
   ```
   The loader sets `cl_model = 0`, analyzing the absolute observed spectrum.
   Less scientifically meaningful but can detect gross issues.

**Model fallback hierarchy:**
- If `--planck_model` is provided and valid → use it
- If `--planck_model` is invalid (parameter file) → abort with error
- If `--planck_model` is not provided → use zeros (option 3 above)

**To use TT-full as model (option 2):** Explicitly pass the same file to both arguments.

The validation code will automatically reject parameter files if you try to use them as model input.

**Sanity check** (after download):
```bash
# Check file sizes (approximate)
ls -lh data/planck_pr3/raw/*.txt

# Verify not HTML (should show numeric data, not <!DOCTYPE)
head -5 data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt
head -5 data/planck_pr3/raw/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt
```

**Expected output**:
- Files downloaded to `data/planck_pr3/raw/`
- Script prints next steps for hash computation

**If download fails**: Follow manual instructions in `data/planck_pr3/README.md` or download directly from:
- https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/

### Step 2: Compute Planck Hashes

**Recommended approach (with relative paths):**
```bash
# Run from repository root
# IMPORTANT: Include ONLY the files you will actually use in the analysis
python tools/data_provenance/hash_dataset.py \
    data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    > data/planck_pr3/manifests/planck_pr3_tt_manifest.json

# If using a model file, include it too:
python tools/data_provenance/hash_dataset.py \
    data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    data/planck_pr3/raw/your_model_file.txt \
    > data/planck_pr3/manifests/planck_pr3_tt_manifest.json
```

**CRITICAL: Manifest must match files used in analysis**

The validation system enforces that the manifest contains hashes for the **exact files** you pass to `run_real_data_cmb_comb.py`. If you run:

```bash
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_manifest data/planck_pr3/manifests/planck_pr3_tt_manifest.json
```

Then `planck_pr3_tt_manifest.json` **must** contain hashes for both `spectrum.txt` and `model.txt` (by filename). If the manifest is valid but missing one of these files, the run will abort with:

```
ERROR: Manifest validation succeeded but does not include files used by this run
Missing files:
  - model.txt

To regenerate the manifest with the correct files, run:
  cd /path/to/repo
  python tools/data_provenance/hash_dataset.py data/planck_pr3/raw/spectrum.txt data/planck_pr3/raw/model.txt > data/planck_pr3/manifests/planck_pr3_tt_manifest.json
```

This ensures the manifest is a true record of the data used in the analysis.

**Alternative (hash all files in directory - not recommended for court-grade):**
```bash
cd data/planck_pr3/raw

# Compute SHA-256 hashes for all data files
python ../../../tools/data_provenance/hash_dataset.py *.txt *.fits > ../manifests/planck_pr3_tt_manifest.json
```

**Warning**: Hashing all files means the manifest may include files you don't use in analysis. For court-grade provenance, generate manifests with only the exact files used.

**Note**: Using `--relative-to` stores paths relative to the repository root, making manifests portable across different working directories.

**Expected output**:
- `planck_pr3_tt_manifest.json` created in `data/planck_pr3/manifests/`
- Contains SHA-256 hash for each file

### Step 3: Validate Planck Data

**Recommended (works from any directory):**
```bash
# From repository root
python tools/data_provenance/validate_manifest.py \
    data/planck_pr3/manifests/planck_pr3_tt_manifest.json \
    --base_dir .
```

**Alternative (let it auto-detect):**
```bash
python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/planck_pr3_tt_manifest.json
```

**Expected output**:
```
================================================================================
Dataset Validation Report
================================================================================
Manifest: data/planck_pr3/manifests/planck_pr3_tt_manifest.json
Base directory: /path/to/unified-biquaternion-theory
✓ SUCCESS: All X file(s) validated
Data provenance confirmed. Files match pre-registered hashes.
================================================================================
```

**Note**: The `--base_dir` parameter tells the validator where to resolve relative paths from. If omitted, it defaults to the manifest's parent directory, which now works correctly from any working directory.

**Critical**: If validation fails, DO NOT proceed with analysis. Re-download or investigate discrepancy.

### Step 4: Download WMAP Data

```bash
bash tools/data_download/download_wmap_tt.sh
```

**Expected output**:
- Files downloaded to `data/wmap/raw/`

### Step 5: Compute WMAP Hashes

**Recommended approach (with relative paths):**
```bash
# Run from repository root
python tools/data_provenance/hash_dataset.py \
    data/wmap/raw/wmap_tt_*.txt \
    --relative-to . \
    > data/wmap/manifests/wmap_tt_manifest.json
```

**Alternative (from data directory):**
```bash
cd data/wmap/raw

python ../../../tools/data_provenance/hash_dataset.py wmap_tt_*.txt > ../manifests/wmap_tt_manifest.json
```

### Step 6: Validate WMAP Data

```bash
# Works from any directory
python tools/data_provenance/validate_manifest.py \
    data/wmap/manifests/wmap_tt_manifest.json \
    --base_dir .
```

**Expected**: ✓ SUCCESS (same as Planck)

---

## Running CMB Comb Test: Planck PR3

### Step 7: Run Planck Analysis

```bash
cd forensic_fingerprint/cmb_comb

python cmb_comb.py \
    --dataset planck_pr3 \
    --input_obs ../../data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --input_model ../../data/planck_pr3/raw/theoretical_model_spectrum.txt \
    --ell_min 30 \
    --ell_max 1500 \
    --output_dir ../out/cmb_comb/planck_pr3_run1
```

**Parameters**:
- `--dataset planck_pr3`: Use Planck PR3 loader
- `--input_obs`: Observed TT power spectrum
- `--input_model`: ΛCDM best-fit model
- `--ell_min 30`: Avoid low-ℓ cosmic variance
- `--ell_max 1500`: Avoid high-ℓ systematics
- `--output_dir`: Where to save results

**Optional**: Include covariance for whitening:
```bash
python cmb_comb.py \
    --dataset planck_pr3 \
    --input_obs ../../data/planck_pr3/raw/spectrum.txt \
    --input_model ../../data/planck_pr3/raw/model.txt \
    --input_cov ../../data/planck_pr3/raw/covariance.dat \
    --ell_min 30 \
    --ell_max 1500
```

**Runtime**: ~30-60 seconds (10,000 Monte Carlo trials)

### Step 8: Review Planck Results

**Terminal output**:
```
============================================================
CMB COMB TEST RESULTS
============================================================
Dataset: Planck PR3
Whitening: NO (diagonal only)  [or YES if covariance provided]
Best period: Δℓ = 255
Amplitude: A = 0.1234
Phase: φ = 1.5708 rad (90.00°)
Max Δχ²: 15.67
P-value: 3.45e-03
Significance: CANDIDATE
============================================================
```

**Files created** (in `../out/cmb_comb/planck_pr3_run1/`):
- `cmb_comb_results.txt`: Summary statistics
- `null_distribution.txt`: Monte Carlo null distribution
- `residuals_and_fit.txt`: Residuals with fitted sinusoid
- `residuals_with_fit.png`: Diagnostic plot (if matplotlib installed)
- `null_distribution.png`: P-value visualization

---

## Running CMB Comb Test: WMAP (Replication)

### Step 9: Run WMAP Analysis

```bash
python cmb_comb.py \
    --dataset wmap \
    --input_obs ../../data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --ell_min 30 \
    --ell_max 800 \
    --output_dir ../out/cmb_comb/wmap_run1
```

**Parameters**:
- `--dataset wmap`: Use WMAP loader
- `--ell_max 800`: WMAP has lower resolution than Planck

**Note**: WMAP typically does not include separate model file. The loader will compute residuals relative to best-fit if model column is present, or use Planck model interpolated to WMAP ℓ range.

### Step 10: Review WMAP Results

**Expected**: Similar period if signal is real, but possibly weaker p-value due to WMAP's lower sensitivity.

**Replication Criterion**:
- **Same period** (Δℓ) should be best fit
- **Consistent phase** (within ~π/2)
- **p-value** may be weaker but should still be < 0.05 if real

---

## Interpreting Results

### Significance Levels

| Significance | P-value | Interpretation |
|--------------|---------|----------------|
| **null** | p ≥ 0.01 | No signal detected. H0 not rejected. |
| **candidate** | 0.01 > p ≥ 2.9e-7 | Candidate signal. Requires replication. |
| **strong** | p < 2.9e-7 | Strong signal (~5σ). Immediate verification needed. |

### Look-Elsewhere Effect

The p-value reported is **after** look-elsewhere correction via the max-statistic method:
- We test multiple candidate periods: [8, 16, 32, 64, 128, 255]
- For each Monte Carlo trial, we record max(Δχ²) across all periods
- P-value = fraction of trials with max(Δχ²) ≥ observed

This controls the family-wise error rate (FWER) at the stated significance level.

### Whitening

If full covariance matrix is provided (`--input_cov`):
- **Whitening**: Residuals are decorrelated via Cholesky decomposition
- **Advantage**: Properly accounts for correlations between multipoles
- **Disadvantage**: Requires large covariance file

If only diagonal uncertainties available:
- **No whitening**: Assumes uncorrelated errors
- **Warning**: May underestimate p-value if strong correlations exist

---

## PASS/FAIL Criteria

### PASS: Significant Signal Detected

A signal **passes** if **ALL** of the following hold:

1. **Planck p-value** < 0.01 (candidate or strong)
2. **WMAP p-value** < 0.05 (weaker threshold for replication)
3. **Same period** in Planck and WMAP (best-fit Δℓ matches)
4. **Consistent phase** (within π/2 radians)
5. **Variant C** is the active hypothesis (not A, B, or D)

**Action if PASS**:
- Prepare manuscript for peer review
- Archive full results (see [Archiving Results](#archiving-results))
- Seek independent verification (third dataset or different analysis)

### FAIL: Null Result

A signal **fails** (null result) if **ANY** of the following hold:

1. **Planck p-value** ≥ 0.01
2. **WMAP p-value** ≥ 0.05
3. **Different periods** in Planck and WMAP
4. **Inconsistent phase** (differs by > π/2)

**Action if FAIL**:
- Document null result in lab notebook
- **Do NOT** publish as detection (per pre-registered protocol)
- Consider alternative hypotheses (Variants A, B, D)

### INCONCLUSIVE: Candidate Without Replication

If Planck shows candidate (p < 0.01) but WMAP shows null (p ≥ 0.05):

**Action**:
- **Do NOT** claim detection
- Seek third dataset (e.g., ACT, SPT)
- Investigate systematic differences between Planck and WMAP

---

## Troubleshooting

### Download Script Fails

**Problem**: `download_planck_pr3_cosmoparams.sh` returns error

**Solutions**:
1. Check internet connection
2. Verify URLs in script (may need updating)
3. Download manually from https://irsa.ipac.caltech.edu/Missions/planck.html
4. See `data/planck_pr3/README.md` for manual instructions

### Hash Validation Fails

**Problem**: `validate_manifest.py` reports hash mismatch

**Solutions**:
1. Re-download file (may be corrupted)
2. Verify you downloaded correct version (PR3 not PR2)
3. If persists, document discrepancy and contact data archive

### ImportError: astropy

**Problem**: "astropy is required to load FITS files"

**Solutions**:
1. Install astropy: `pip install astropy`
2. Or convert FITS to TXT manually using NASA tools

### Matplotlib Not Available

**Problem**: "Matplotlib not available - skipping plots"

**Solutions**:
1. Install matplotlib: `pip install matplotlib`
2. Or proceed without plots (numerical results still valid)

### Covariance Not Positive Definite

**Problem**: "WARNING: Covariance matrix is not positive definite"

**Solutions**:
1. Falls back to diagonal uncertainties automatically
2. Verify covariance file is correct format
3. May indicate numerical issues in original data

---

## Archiving Results

If **PASS** criteria met, archive full results:

### Step 11: Create Archive

```bash
cd forensic_fingerprint/out/cmb_comb

# Create timestamped archive
timestamp=$(date +%Y%m%d_%H%M%S)
archive_name="cmb_comb_results_${timestamp}.tar.gz"

tar -czf "${archive_name}" planck_pr3_run1/ wmap_run1/
```

### Step 12: Document Provenance

Create `PROVENANCE.txt`:

```
CMB Comb Fingerprint Test - Full Provenance
============================================

Date: 2026-01-10
Protocol Version: v1.0
Git Commit: <git rev-parse HEAD>

Datasets:
  Planck PR3: SHA-256 manifest in data/planck_pr3/manifests/
  WMAP 9yr:   SHA-256 manifest in data/wmap/manifests/

Results:
  Planck:  p = 3.45e-03, period = 255, amplitude = 0.1234
  WMAP:    p = 4.21e-02, period = 255, amplitude = 0.0987

Conclusion: PASS (signal detected in both datasets)

Analyst: [Your Name]
Signature: [Digital signature or hash]
```

### Step 13: Commit Manifests (Not Data)

```bash
git add data/planck_pr3/manifests/*.json
git add data/wmap/manifests/*.json
git commit -m "Add pre-registered data manifests for CMB comb test"
git push
```

**DO NOT** commit raw data files. Only manifests.

---

## Summary Workflow

```
1. Download Planck PR3 data           → data/planck_pr3/raw/
2. Compute SHA-256 hashes             → data/planck_pr3/manifests/
3. Validate hashes                    → ✓ SUCCESS
4. Download WMAP data                 → data/wmap/raw/
5. Compute SHA-256 hashes             → data/wmap/manifests/
6. Validate hashes                    → ✓ SUCCESS
7. Run Planck CMB comb test           → ../out/cmb_comb/planck_pr3_run1/
8. Review Planck results              → p-value, period, amplitude
9. Run WMAP CMB comb test             → ../out/cmb_comb/wmap_run1/
10. Review WMAP results               → Compare with Planck
11. Apply PASS/FAIL criteria          → Document conclusion
12. Archive results (if PASS)         → tar.gz + PROVENANCE.txt
13. Commit manifests to repository    → git add manifests/ && git commit
```

---

## Advanced Features

### Polarization Spectra (TE/EE/BB)

**Purpose**: Cross-check TT results with polarization spectra to rule out temperature-specific systematics.

**Usage**:
```bash
# Test TE (temperature-E-mode) spectrum
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/planck_te_spectrum.txt \
    --planck_model data/planck_pr3/raw/planck_te_model.txt \
    --spectrum TE \
    --variant C

# Test EE (E-mode-E-mode) spectrum
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/planck_ee_spectrum.txt \
    --planck_model data/planck_pr3/raw/planck_ee_model.txt \
    --spectrum EE \
    --variant C
```

**Interpretation**:
- If signal appears in TT but NOT TE/EE → likely foreground or systematic
- If signal appears in TT, TE, AND EE → strong evidence for real geometric effect

**Note**: Polarization spectra have lower S/N than TT. Real but weak signals may not reach significance in TE/EE.

---

### ℓ-Range Ablation Tests

**Purpose**: Verify signal persists across multiple independent multipole windows, ruling out range-specific artifacts.

**Automatic Ablation**:
```bash
# Run predefined ablation ranges (low, mid, high, overlapping windows)
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --ablate-ell \
    --variant C
```

This runs the test on:
- Low-ℓ: 30-250 (acoustic peaks)
- Mid-ℓ: 251-800 (damping tail)
- High-ℓ: 801-1500 (deep damping)
- Full-low: 30-800 (exclude high-ℓ)
- Full-high: 200-1500 (exclude very low-ℓ)

**Custom Ranges**:
```bash
# Specify custom ℓ-ranges
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --ablate-ranges "30-500,500-1000,1000-1500" \
    --variant C
```

**Output**: Results aggregated in markdown report showing consistency across ranges.

---

### Synthetic ΛCDM Null Control

**Purpose**: Measure false positive rate on synthetic data with NO real signal, calibrating the pipeline.

**Usage**:
```bash
# Run on synthetic ΛCDM (no periodic structure)
python run_real_data_cmb_comb.py \
    --null-data lcdm \
    --null-trials 100 \
    --planck_cov data/planck_pr3/covariance/planck_cov.npy \
    --mc_samples 10000 \
    --variant C
```

**What it does**:
1. Generates 100 synthetic ΛCDM realizations using Planck best-fit cosmology
2. Adds realistic noise from covariance matrix
3. Runs full CMB comb pipeline on each
4. Reports p-value distribution

**Expected behavior**: P-values should be uniformly distributed U(0,1) under null.

**Interpretation**:
- If p-values are uniform → pipeline is well-calibrated, no false positive bias
- If excess at low p-values → pipeline bug, DO NOT proceed with claims

**Note**: This is a CRITICAL validation step for court-grade analysis.

---

### Run Summary Tool

**Purpose**: Quick overview of all analysis runs for comparison and status tracking.

**Usage**:
```bash
# View summary of all runs
python tools/forensic/print_run_summary.py

# View last 10 runs only
python tools/forensic/print_run_summary.py --last 10

# Export as CSV
python tools/forensic/print_run_summary.py --format csv --output runs.csv

# Export as JSON
python tools/forensic/print_run_summary.py --format json --output runs.json

# Search specific pattern
python tools/forensic/print_run_summary.py "forensic_fingerprint/out/real_runs/cmb_comb_2026*"
```

**Output** (table format):
```
Timestamp            Run Name                       Planck p     Period   Phase(°)  ℓ-range         Whiten     WMAP p       Period   Verdict      Status    
2026-01-10 15:04:23  cmb_comb_20260110_150423      3.45e-03     255      90.0      30-1500         full       4.21e-02     255      CANDIDATE    ✓ Complete
```

**Fields**:
- Timestamp: Run date/time
- Planck p / WMAP p: P-values
- Period: Best-fit Δℓ
- Phase(°): Best-fit φ in degrees
- ℓ-range: Multipole range used
- Whiten: Whitening mode
- Verdict: PASS/FAIL/CANDIDATE/INCOMPLETE
- Status: ✓ Complete / ⚠ Incomplete (missing files)

---

## Complete Workflow Example (Court-Grade)

**Scenario**: Full court-grade analysis with all validation steps.

```bash
# 1. Download and validate data (see earlier sections)
bash tools/data_download/download_planck_pr3_cosmoparams.sh
python tools/data_provenance/hash_dataset.py data/planck_pr3/raw/*.txt > data/planck_pr3/manifests/manifest.json
python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/manifest.json

# 2. Run TT analysis with full covariance
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model data/planck_pr3/raw/theoretical_model_tt.txt \
    --planck_cov data/planck_pr3/covariance/planck_tt_cov.npy \
    --planck_manifest data/planck_pr3/manifests/manifest.json \
    --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_cov data/wmap/covariance/wmap_tt_cov.npy \
    --wmap_manifest data/wmap/manifests/wmap_manifest.json \
    --whiten full \
    --mc_samples 100000 \
    --variant C \
    --output_dir out/court_grade_tt

# 3. Run TE/EE cross-checks
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/planck_te_spectrum.txt \
    --planck_model data/planck_pr3/raw/theoretical_model_te.txt \
    --spectrum TE \
    --whiten full \
    --mc_samples 100000 \
    --variant C \
    --output_dir out/court_grade_te

# 4. Run ablation tests
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model data/planck_pr3/raw/theoretical_model_tt.txt \
    --ablate-ell \
    --whiten full \
    --mc_samples 100000 \
    --variant C \
    --output_dir out/ablation_tests

# 5. Run ΛCDM null control
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --null-data lcdm \
    --null-trials 100 \
    --planck_cov data/planck_pr3/covariance/planck_tt_cov.npy \
    --mc_samples 10000 \
    --variant C \
    --output_dir out/lcdm_null_control

# 6. Review all results
python tools/forensic/print_run_summary.py

# 7. Check combined verdicts
cat out/court_grade_tt/combined_verdict.md
cat out/court_grade_te/combined_verdict.md

# 8. Review skeptic checklist
cat forensic_fingerprint/SKEPTIC_CHECKLIST.md
```

**Court-Grade Checklist**:
- ✅ Full covariance whitening (not diagonal)
- ✅ High MC samples (100k not 5k)
- ✅ SHA-256 manifest validation
- ✅ Planck + WMAP replication
- ✅ TE/EE cross-checks
- ✅ ℓ-range ablation tests
- ✅ ΛCDM null control (false positive rate calibration)
- ✅ All results documented in `combined_verdict.md`

---

**Questions?** See `forensic_fingerprint/PROTOCOL.md` for pre-registered protocol details.

**Issues?** Open GitHub issue: https://github.com/DavJ/unified-biquaternion-theory/issues

**Skeptic Arguments?** See `forensic_fingerprint/SKEPTIC_CHECKLIST.md` for how we address counter-arguments.

---

**Last Updated**: 2026-01-11  
**Protocol Version**: v1.0  
**Maintained by**: UBT Research Team
