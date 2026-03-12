# CMB 2D FFT Spectral Shear Test - Runbook

**Status:** 🔵 EXPLORATORY / PROOF-OF-CONCEPT  
**Layer:** Research Front (Layer C)  
**Last Updated:** 2026-01-13

---

## ⚠️ Critical Disclaimer

**This is NOT part of Core UBT.**

This is an **exploratory proof-of-concept** for testing whether small anisotropic tilts (~arctan(1/256) ≈ 0.224°) are detectable in 2D Fourier space of CMB patches.

**Important:**
- ❌ **NO results claimed** from Planck maps
- ❌ **NOT a pre-registered test**
- ❌ **Any positive result requires independent replication**
- ✅ Failure to detect signal is a **valid outcome**
- ✅ This is a **methods development** exercise

---

## Overview

### What This Test Does

Search for small-angle anisotropic structure in the 2D Fourier transform of local CMB temperature patches.

**Hypothesis:** If UBT's discretization model (256-tick structure with angle arctan(1/256)) manifests in CMB, it might create detectable oriented power in 2D FFT space.

**Expected outcome:** Likely NULL (no detection). This is exploratory, not a prediction.

---

## Step-by-Step Procedure

### Step 1: Run Proof-of-Concept (PoC) with Synthetic Data

**Before touching real Planck data**, validate the analysis pipeline with synthetic test cases.

#### 1a. Default Run (Gaussian Null Control)

```bash
cd research_front/cmb_2d_fft
python cmb_2d_fft_poc.py
```

**Expected output:**
- Generates 256×256 Gaussian random field
- Applies 2D FFT
- Searches for oriented power
- **Should find NO significant tilt** (null control)
- Saves plots to `fft_output/`

**What to check:**
- Is the detected angle random? ✅ (Good - no false positive)
- Is peak/median ratio close to 1? ✅ (Good - no spurious signal)

#### 1b. Synthetic Grid Test (Positive Control)

```bash
python cmb_2d_fft_poc.py --mode synthetic_grid --tilt_deg 0.224
```

**Expected output:**
- Generates grid pattern with known tilt angle (0.224°)
- 2D FFT should detect oriented ridge at ~0.224°
- **This validates that the method CAN detect tilts when present**

**What to check:**
- Does detected angle match input? ✅ (Good - method works)
- Is peak/median ratio > 2? ✅ (Good - clear detection)

#### 1c. Injected Signal Test

```bash
python cmb_2d_fft_poc.py --mode injected --snr 0.5 --tilt_deg 0.224
```

**Expected output:**
- Gaussian field + weak injected tilt
- Tests detection threshold (SNR = 0.5 is borderline)
- **Validates method sensitivity**

**What to check:**
- At what SNR does detection become unreliable?
- Compare to expected noise-limited sensitivity

---

### Step 2: Null Tests and Robustness Checks

**Before claiming any result**, run comprehensive null tests:

#### 2a. Multiple Random Seeds

```bash
for seed in {0..9}; do
    python cmb_2d_fft_poc.py --mode gaussian_field --seed $seed --outdir fft_output/seed_$seed
done
```

**Expected:** Detected angles should be **uniformly distributed** (no preferred direction).

**Red flag:** If all seeds yield similar angle → method bias (bug or systematic error).

#### 2b. Varying Patch Size

```bash
for size in 128 256 512; do
    python cmb_2d_fft_poc.py --mode gaussian_field --size $size --outdir fft_output/size_$size
done
```

**Expected:** Null results **independent of patch size**.

**Red flag:** If detection appears only at specific size → resolution artifact.

#### 2c. Different Tilt Angles (Positive Controls)

```bash
for angle in 0.1 0.224 0.5 1.0; do
    python cmb_2d_fft_poc.py --mode synthetic_grid --tilt_deg $angle --outdir fft_output/tilt_$angle
done
```

**Expected:** Detected angle should **match injected angle** for all cases.

**Red flag:** If method fails to detect known tilts → broken pipeline.

---

### Step 3: Planck Map Analysis (Optional and NOT Required)

**Only proceed if:**
1. PoC tests all pass
2. Null tests show no systematic bias
3. You have legitimate scientific reason (not confirmation bias)
4. You understand this is exploratory, not confirmatory

#### 3a. Download Planck CMB Maps (User Responsibility)

**UBT repository does NOT include Planck FITS files** (too large, requires citation).

**How to download:**

1. Visit [Planck Legacy Archive (PLA)](https://pla.esac.esa.int/)
2. Navigate to: **Planck 2018 Release** → **CMB Maps**
3. Download component-separated maps:
   - `COM_CMB_IQU-smica_2048_R3.00_full.fits` (SMICA)
   - `COM_CMB_IQU-nilc_2048_R3.00_full.fits` (NILC)
   - `COM_CMB_IQU-sevem_2048_R3.00_full.fits` (SEVEM)
   - `COM_CMB_IQU-commander_2048_R3.00_full.fits` (Commander)

4. Also download masks (optional but recommended):
   - `COM_Mask_CMB-common-MaskInt_2048_R3.00.fits`

5. Place in local directory: `data/planck_pr3/raw/`

**File size warning:** ~2-4 GB per map. Ensure sufficient disk space.

**Citation:** Planck Collaboration (2020). "Planck 2018 results. IV. Diffuse component separation." A&A, 641, A4.

#### 3b. Install Dependencies

```bash
pip install healpy astropy
```

**Note:** healpy requires compilers and may take time to install. See [healpy.readthedocs.io](https://healpy.readthedocs.io/) for troubleshooting.

#### 3c. Run Planck Analysis

```bash
python cmb_2d_fft_planck.py
```

**Configuration:** Edit `cmb_2d_fft_planck.py` to set:
- `MAP_FITS`: path to your downloaded Planck map
- `MASK_FITS`: path to mask (optional)
- `LON_DEG`, `LAT_DEG`: patch center coordinates (high galactic latitude recommended, |b| > 30°)
- `PATCH_DEG`: patch size in degrees (10-30° typical)

**What to expect:**
- Script extracts patch via gnomonic projection
- Applies apodization (Hann window)
- Computes 2D FFT and searches for oriented power
- Saves plots and prints detected angle + statistics

**Likely outcome:** **NO significant detection** (null result).

---

### Step 4: Interpret Results

#### 4a. What Constitutes "Candidate Signal"?

**Criteria for claiming candidate (ALL must be met):**

1. **Significance:** Peak/median ratio > 3 (conservative threshold)
2. **Consistency:** Same angle detected across multiple patches (≥5 independent regions)
3. **Consistency across maps:** All 4 component-separated maps (SMICA, NILC, SEVEM, Commander) show same signal
4. **Robustness:** Signal survives mask variations, patch size changes
5. **Physical plausibility:** Detected angle close to arctan(1/256) ≈ 0.224° (±50% tolerance)

**If any criterion fails → NULL result**

#### 4b. What Constitutes "Null Result"?

**Criteria for null (ANY can apply):**

1. Peak/median ratio < 2 (no significant anisotropy)
2. Detected angles vary randomly across patches
3. Different component-separated maps give inconsistent results
4. Signal disappears with different masks or analysis choices
5. Detected angle not close to predicted value

**Current expectation: NULL result is most likely.**

#### 4c. Statistical Analysis Required

**If you think you detect something:**

1. **Quantify significance:**
   - Monte Carlo: run analysis on 1000 Gaussian random fields
   - Compare observed peak/median to distribution
   - Calculate p-value

2. **Blind analysis:**
   - Fix all analysis parameters BEFORE looking at Planck results
   - Document pre-registration (what angle are you looking for, what threshold)

3. **Independent replication:**
   - Share code + data
   - Get independent team to replicate
   - If they get different result → systematic error

4. **Compare to known systematics:**
   - Scanning strategy artifacts (Planck scan pattern)
   - Point source contamination
   - Galactic foreground residuals
   - Beam asymmetries

**Do NOT claim detection without completing these steps.**

---

### Step 5: Reporting Results

#### 5a. If NULL Result (Expected)

**Report honestly:**
> "We searched for anisotropic tilt of angle ~arctan(1/256) ≈ 0.224° in 2D Fourier space of Planck CMB patches. We found **no significant detection** (peak/median ratio < 2, angles randomly distributed). This null result is consistent with the hypothesis that any discrete-time signature is below detection threshold with current methods."

**Document:**
- Patches analyzed (coordinates, sizes)
- Detection thresholds used
- Null test results
- Publication: include as **negative result** (equally valuable)

#### 5b. If Candidate Signal (Unlikely)

**Report cautiously:**
> "We report a **candidate** oriented power structure at angle X ± Y° in 2D Fourier space of Planck CMB patches. This is **not a confirmed detection** and requires:
> 1. Independent replication
> 2. Systematic error investigation
> 3. Blind analysis validation
> 
> Alternative explanations (scanning artifacts, foregrounds, statistical fluctuation) have not been fully ruled out."

**Do NOT:**
- Claim "detection" or "confirmation"
- Attribute to UBT without caveats
- Skip systematic error analysis

#### 5c. Archive All Results

**Regardless of outcome:**
- Save all plots, data, parameters
- Document analysis choices
- Make code + intermediate results available
- Include in repository under `research_front/cmb_2d_fft/results/`

**Transparency:** Negative results are scientifically valuable and must be reported.

---

## Data Policy

### No Embedded Large Data

**Repository does NOT include:**
- Planck FITS maps (too large, ~GB scale)
- HEALPix masks
- Extracted patches (if large)

**Repository DOES include:**
- Analysis code (Python scripts)
- Small synthetic test data (if needed for validation)
- Summary plots (PNG/PDF, < 1 MB each)
- Results tables (CSV, text)

### How to Reproduce

**Users must:**
1. Download Planck maps from PLA (link provided above)
2. Place in expected directory structure
3. Run scripts with provided parameters
4. Compare results to documented values

**Documentation includes:**
- Exact Planck data release used (PR3, 2018)
- Download links
- File checksums (MD5/SHA256) for verification
- Analysis parameter files

---

## Software Dependencies

### Required (PoC)

- Python ≥ 3.7
- numpy
- scipy
- matplotlib

**Installation:**
```bash
pip install numpy scipy matplotlib
```

### Optional (Planck Maps)

- healpy (HEALPix tools)
- astropy (FITS I/O)

**Installation:**
```bash
pip install healpy astropy
```

**Note:** healpy installation can be complex. See [healpy docs](https://healpy.readthedocs.io/) for platform-specific instructions.

---

## Expected Outcomes Summary

| Test | Expected Result | Interpretation |
|------|-----------------|----------------|
| **PoC Gaussian null** | No tilt detected | ✅ Method has no bias |
| **PoC synthetic grid** | Tilt = 0.224° detected | ✅ Method works |
| **PoC injected signal** | Detection at SNR > 0.5 | ✅ Sensitivity validated |
| **Null tests (seeds)** | Random angles | ✅ No systematic bias |
| **Planck analysis** | **Likely NULL** | ⚠️ Signal below threshold or absent |

**Key point:** Absence of detection is a **valid scientific result**, not a failure.

---

## Troubleshooting

### PoC script fails

**Check:**
- Python version (≥ 3.7)
- numpy, scipy, matplotlib installed
- Sufficient disk space for output
- Permissions to write to `fft_output/` directory

### Planck script fails (ImportError)

**Solution:**
- Use PoC instead: `python cmb_2d_fft_poc.py`
- Or install healpy: `pip install healpy astropy`
- Check healpy installation docs for compiler requirements

### Memory issues (large maps)

**Solutions:**
- Reduce patch size (smaller `PATCH_DEG`)
- Use lower resolution (larger `PIX_ARCMIN`)
- Process patches serially, not all at once
- Close other applications

### Unexpected detections in null tests

**This is a bug or systematic error:**
- Re-examine apodization (Hann window applied?)
- Check FFT normalization
- Verify coordinate transformations
- Run with known tilt to validate method

---

## Summary

**CMB 2D FFT Spectral Shear Test Runbook:**

1. **Start with PoC** (synthetic data, no Planck maps needed)
2. **Run null tests** (Gaussian fields, multiple seeds, sizes)
3. **Validate method** (positive controls with known tilts)
4. **Only then:** Optionally analyze Planck maps (user downloads data)
5. **Report honestly:** NULL or candidate (with full caveats)
6. **Archive everything:** Code, data, plots, null results

**Expected outcome:** Likely **NULL result** (no detection). This is scientifically valuable and should be published.

**If positive result:** Requires independent replication, systematic error analysis, blind validation before claiming detection.

---

## References

1. Planck Collaboration (2020). "Planck 2018 results. IV. Diffuse component separation." A&A, 641, A4.
2. Planck Legacy Archive: https://pla.esac.esa.int/
3. HEALPix: https://healpix.sourceforge.io/
4. healpy documentation: https://healpy.readthedocs.io/
5. UBT Repository:
   - [README.md](README.md) - Overview of 2D FFT test
   - [HYPOTHESIS.md](../hubble_latency/HYPOTHESIS.md) - Research Front context
   - [STATUS_OF_CODING_ASSUMPTIONS.md](../../docs/STATUS_OF_CODING_ASSUMPTIONS.md) - UBT layer structure

---

**Document Status:** Complete  
**Last Updated:** 2026-01-13  
**Maintainer:** UBT Research Team
