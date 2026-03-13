# Court-Grade Runbook: CMB Phase-Comb Test

**Purpose**: Step-by-step instructions for running the CMB phase-comb fingerprint test on real Planck and WMAP map-level data with full reproducibility and provenance tracking.

**Status**: Pre-registered protocol v1.0  
**Last Updated**: 2026-01-12  
**Author**: UBT Research Team

---

## Table of Contents

1. [Overview](#overview)
2. [What This Test Measures](#what-this-test-measures)
3. [Prerequisites](#prerequisites)
4. [Data Requirements](#data-requirements)
5. [Quick Start](#quick-start)
6. [One-Command Usage](#one-command-usage)
7. [Understanding the Output](#understanding-the-output)
8. [Interpretation Guidance](#interpretation-guidance)
9. [Troubleshooting](#troubleshooting)

---

## Overview

The **CMB Phase-Comb Test** searches for periodic phase-locking in spherical harmonic coefficients a_ℓm of the cosmic microwave background.

### Key Differences from TT Spectrum Comb Test

| Feature | TT Spectrum Test | Phase-Comb Test |
|---------|------------------|-----------------|
| **Input** | Power spectrum C_ℓ | HEALPix map → a_ℓm |
| **Measures** | Amplitude oscillations in C_ℓ | Phase coherence in arg(a_ℓm) |
| **Information used** | |a_ℓm|² (averaged over m) | arg(a_ℓm) (phase angles) |
| **Null model** | ΛCDM synthetic C_ℓ | Phase-randomized a_ℓm preserving C_ℓ |
| **Complementarity** | Tests power spectrum | Tests relational structure |

**Critical Point**: A null result in the TT spectrum test does **NOT** preclude a positive result in the phase-comb test. These tests examine different aspects of the CMB data.

---

## What This Test Measures

### Phase Coherence Statistic

For each period P, we compute:

```
R(P) = |⟨exp(i Δφ_ℓm(P))⟩|
```

where:
- Δφ_ℓm(P) = arg(a_{ℓ+P,m}) - arg(a_{ℓ,m})
- ⟨·⟩ denotes average over all valid (ℓ,m) pairs
- R(P) ∈ [0, 1]: 0 = random phases, 1 = perfect phase-locking

### Null Model

Court-grade null hypothesis: **Phase-randomized surrogates preserving C_ℓ**

For each surrogate:
1. Keep amplitudes: r_ℓm = |a_ℓm|
2. Randomize phases: θ_ℓm ~ Uniform(0, 2π)
3. Construct: a'_ℓm = r_ℓm exp(i θ_ℓm)
4. Enforce reality constraints:
   - a_ℓ,0 is real (phase = 0 or π, preserve sign)
   - a_ℓ,-m = (-1)^m conj(a_ℓm) [automatic in healpy]

This preserves the observed power spectrum C_ℓ while destroying any phase structure.

---

## What This Test Does NOT Measure

❌ **Not tested**:
- Power spectrum C_ℓ oscillations (use TT comb test instead)
- Amplitude-only features
- Non-periodic phase patterns
- Individual mode anomalies

✓ **Tested**:
- Periodic phase coherence at pre-registered periods
- Relational structure between modes separated by P

---

## Prerequisites

### Software Requirements

```bash
# Python 3.8+
python --version

# Core packages
pip install numpy scipy matplotlib

# REQUIRED for phase-comb test
pip install healpy

# Optional for FITS handling
pip install astropy
```

**Important**: healpy is **required** for the phase-comb test. It provides:
- HEALPix map I/O
- Spherical harmonic transform (map → a_ℓm)
- Reality constraint handling

### Repository Setup

```bash
# Clone repository
git clone https://github.com/DavJ/unified-biquaternion-theory.git
cd unified-biquaternion-theory

# Verify modules exist
ls -l forensic_fingerprint/cmb_phase_comb/
ls -l tools/data_download/
```

---

## Data Requirements

### Input: HEALPix CMB Maps

Unlike the TT spectrum test (which uses tabulated C_ℓ), the phase-comb test requires:

1. **CMB temperature map** (HEALPix format)
   - FITS file with T field
   - Or NumPy array (.npy)
   
2. **Mask** (optional but recommended)
   - Same resolution as map
   - 0/1 values (0 = masked pixel)
   - Common choice: Planck common mask

### Recommended Datasets

#### Planck PR3 (Primary)
- **Map**: SMICA CMB map
  - File: `COM_CMB_IQU-smica_2048_R3.00_full.fits`
  - Source: Planck Legacy Archive
  - NSIDE: 2048

- **Mask**: Common mask (intensity)
  - File: `COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits`
  - Masks Galactic plane and point sources

#### WMAP 9yr (Replication)
- **Map**: ILC map
  - File: `wmap_ilc_9yr_v5.fits`
  - NSIDE: 512

---

## Quick Start

### Step 1: Download CMB Maps

```bash
# Download Planck PR3 maps (automated script)
bash tools/data_download/download_planck_pr3_maps.sh

# This downloads:
#   - COM_CMB_IQU-smica_2048_R3.00_full.fits (CMB map)
#   - COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits (mask)
# to: data/planck_pr3/maps/raw/
```

### Step 2: Generate SHA-256 Manifest (Court-Grade)

```bash
# From repository root
mkdir -p data/planck_pr3/maps/manifests

python tools/data_provenance/hash_dataset.py \
  data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
  data/planck_pr3/maps/raw/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits \
  > data/planck_pr3/maps/manifests/planck_maps_manifest.json
```

### Step 3: Run Phase-Comb Test

```bash
# Minimal run (candidate-grade, 10k surrogates)
python forensic_fingerprint/run_real_data_cmb_phase_comb.py \
    --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
    --planck_mask data/planck_pr3/maps/raw/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits

# Court-grade run (with manifest, 10k surrogates)
python forensic_fingerprint/run_real_data_cmb_phase_comb.py \
    --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
    --planck_mask data/planck_pr3/maps/raw/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits \
    --planck_manifest data/planck_pr3/maps/manifests/planck_maps_manifest.json \
    --mc_samples 10000 --seed 42
```

### Step 4: Review Results

```bash
# Results are saved to:
# forensic_fingerprint/out/real_runs/cmb_phase_comb_YYYYMMDD_HHMMSS/

# Key files:
#   - combined_verdict.md          ← START HERE (PASS/FAIL decision)
#   - planck_phase_results.json    ← Detailed numerical results
#   - figures/phase_coherence_curve.png  ← Visualization
```

---

## One-Command Usage

### Basic Options

```bash
python forensic_fingerprint/run_real_data_cmb_phase_comb.py \
    --planck_map <path_to_map.fits> \
    [--planck_mask <path_to_mask.fits>] \
    [--planck_manifest <path_to_manifest.json>] \
    [--ell_min 30] \
    [--ell_max 1500] \
    [--mc_samples 10000] \
    [--seed 42]
```

### Pre-Registered Periods (Default)

By default, the test examines periods: **P ∈ {255, 256, 137, 139}**

- **255, 256**: Reed-Solomon code related (primary hypothesis)
- **137, 139**: Fine structure constant vicinity (secondary)

### Custom Periods

```bash
# Test custom periods
python forensic_fingerprint/run_real_data_cmb_phase_comb.py \
    --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
    --periods "128,256,512" \
    --correction bonferroni  # Enable multiple-testing correction
```

### Prime Window Mode

```bash
# Add all primes in range [130, 150]
python forensic_fingerprint/run_real_data_cmb_phase_comb.py \
    --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
    --prime_window "130,150" \
    --correction bonferroni  # REQUIRED for prime window
```

**Warning**: Prime window mode is exploratory and requires multiple-testing correction.

### High-Confidence Run

```bash
# 100k surrogates for better p-value resolution
python forensic_fingerprint/run_real_data_cmb_phase_comb.py \
    --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
    --planck_mask data/planck_pr3/maps/raw/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits \
    --mc_samples 100000 \
    --seed 42
```

**Note**: 100k surrogates takes ~10x longer but provides p-value resolution down to 10^-5.

---

## Understanding the Output

### JSON Results (`planck_phase_results.json`)

```json
{
  "periods": [255, 256, 137, 139],
  "ell_min": 30,
  "ell_max": 1500,
  "lmax": 1500,
  "n_mc_samples": 10000,
  "seed": 42,
  
  "R_observed": {
    "255": 0.012345,
    "256": 0.011234,
    "137": 0.008765,
    "139": 0.009123
  },
  
  "p_values": {
    "255": 0.0234,
    "256": 0.0456,
    "137": 0.1234,
    "139": 0.0987
  },
  
  "best_period": 255,
  "best_p_value": 0.0234,
  "significance": "CANDIDATE",
  
  "surrogate_stats": { ... },
  "metadata": { ... }
}
```

### Verdict Report (`combined_verdict.md`)

The verdict markdown provides:

1. **Data Provenance**
   - Input files used
   - SHA-256 validation status
   - Sky fraction (if masked)

2. **Test Configuration**
   - ℓ-range, periods, MC samples
   - Pre-registration status

3. **Statistical Results**
   - R(P) observed vs surrogate mean/std
   - P-values per period
   - Best period and significance

4. **PASS/FAIL Decision**
   - ✓ PASS (STRONG): p < 2.9e-7 (5σ)
   - ⚠ CANDIDATE: p < 0.01
   - ✗ FAIL (NULL): p ≥ 0.01

5. **Interpretation Guidance**
   - What was tested
   - What was NOT tested
   - Next steps

---

## Interpretation Guidance

### Significance Levels

| Result | P-value | Interpretation | Next Steps |
|--------|---------|----------------|------------|
| **NULL** | p ≥ 0.01 | No significant signal | Document null result |
| **CANDIDATE** | 0.01 > p ≥ 2.9e-7 | Candidate signal | Replicate with WMAP |
| **STRONG** | p < 2.9e-7 | Strong signal (5σ) | Independent verification, prepare manuscript |

### Candidate Signal Guidelines

If p < 0.01 for any pre-registered period:

1. **Replicate** with independent dataset (WMAP)
   - Must see same period P
   - Must see p_WMAP < 0.05

2. **Check robustness**
   - Run ablation tests (different ℓ-ranges)
   - Test different masks

3. **Increase MC samples**
   - Run with --mc_samples 100000
   - Verify p-value doesn't fluctuate

4. **Sanity checks**
   - Verify surrogates preserve C_ℓ
   - Check R(P) → 0 for random phases

### What If TT Comb Was Null But Phase-Comb Is Not?

This is **physically meaningful** and not contradictory:

- **TT spectrum** measures |a_ℓm|² averaged over m
  - Sensitive to amplitude oscillations in C_ℓ
  - Insensitive to phase structure

- **Phase-comb** measures arg(a_ℓm) coherence
  - Sensitive to relational structure
  - Independent of power spectrum

**Analogy**: A clock with random hand positions (random phases) has the same power spectrum as a synchronized clock ensemble, but very different phase coherence.

---

## Troubleshooting

### healpy Not Installed

```
ERROR: healpy not installed
```

**Solution**:
```bash
pip install healpy
```

If installation fails:
```bash
# On some systems, need build dependencies
conda install -c conda-forge healpy  # Using conda
# OR
pip install healpy --no-build-isolation
```

### Map Loading Error

```
ERROR: Map not found: data/planck_pr3/maps/raw/...
```

**Solution**:
1. Run download script: `bash tools/data_download/download_planck_pr3_maps.sh`
2. Or manually download from Planck Legacy Archive
3. Verify file path is correct (use absolute paths if needed)

### Mask Size Mismatch

```
ValueError: Mask size mismatch: map has X pixels, mask has Y
```

**Solution**:
- Map and mask must have same NSIDE resolution
- Planck PR3: Use NSIDE=2048 for both
- Use `hp.ud_grade()` to change mask resolution if needed

### Memory Error (Large NSIDE)

```
MemoryError: Unable to allocate array
```

**Solution**:
- NSIDE=2048 requires ~50 GB RAM for lmax=1500
- Options:
  1. Reduce lmax: `--alm_lmax 1000` (uses less memory)
  2. Downgrade map: Use NSIDE=1024 version
  3. Run on machine with more RAM

### Slow Performance

Phase-comb test is computationally intensive:

- **10k surrogates**: ~30 min (NSIDE=2048, lmax=1500)
- **100k surrogates**: ~5 hours

**Optimization**:
- Reduce lmax if high-ℓ not needed
- Use fewer surrogates for exploratory runs
- Run on multi-core machine (healpy uses OpenMP)

### P-value at MC Floor

```
WARNING: Best p-value at MC floor (1/10000)
```

**Solution**:
- Increase `--mc_samples 100000` for better resolution
- Current p-value is upper bound: true p ≤ 1/n_samples

---

## Advanced Options

### Map2alm Iterations

```bash
# Default: iter=3 (good balance)
--iter 3

# Higher accuracy (slower):
--iter 10

# Fast (less accurate):
--iter 0
```

### Multiple-Testing Correction

```bash
# None (default for pre-registered periods)
--correction none

# Bonferroni (conservative)
--correction bonferroni

# Max-statistic (most conservative, uses max R over periods)
--correction max_statistic
```

---

## Pre-Registration Statement

The candidate periods **P ∈ {255, 256, 137, 139}** were pre-registered before running the phase-comb test on real data. These periods are:

- **Fixed**: No modifications based on results
- **Theory-motivated**: 255 (Reed-Solomon), 137 (fine structure constant)
- **Limited**: Only 4 periods (conservative multiple-testing)

No look-elsewhere correction is applied by default for these pre-registered periods. If additional periods are tested (via `--periods` or `--prime_window`), appropriate corrections must be applied.

---

## References

- **Theory**: See `forensic_fingerprint/reports/PHASE_COMB_TEST_PLAN.md`
- **TT Spectrum Test**: See `forensic_fingerprint/RUNBOOK_REAL_DATA.md`
- **HEALPix**: Górski et al. (2005), ApJ 622, 759
- **Planck PR3**: Planck Collaboration (2020), A&A 641, A1

---

**End of Runbook**
