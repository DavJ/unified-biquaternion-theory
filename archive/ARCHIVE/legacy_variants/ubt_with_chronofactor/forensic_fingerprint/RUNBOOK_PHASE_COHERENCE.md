# Phase Coherence Test Runbook

**Purpose**: Step-by-step guide for running exploratory and confirmatory phase coherence tests  
**Version**: 1.0  
**Date**: 2026-01-12  
**License**: MIT License (code) / CC BY-NC-ND 4.0 (documentation)

---

## Overview

This runbook covers the **complete workflow** for testing phase-locking in CMB spherical harmonics:

1. **Exploratory scan** (low commitment, broad search)
2. **Pre-registration** (lock parameters before confirmation)
3. **Confirmatory test** (court-grade, strict validation)
4. **Replication** (independent datasets)
5. **Interpretation** (only after confirmation)

---

## Prerequisites

### Software Requirements

```bash
# Python 3.8+
python --version

# Required packages
pip install numpy scipy matplotlib healpy pytest

# Verify healpy installation
python -c "import healpy as hp; print(f'healpy {hp.__version__}')"
```

### Data Requirements

You need CMB spherical harmonic coefficients (a_ℓm) in FITS format:

- **Planck PR3 maps**: Download from [ESA Planck Legacy Archive](https://pla.esdc.esa.int/)
- **WMAP maps**: Download from [NASA LAMBDA](https://lambda.gsfc.nasa.gov/)

**Required files**:
- `planck_pr3_temperature_alm.fits` - Temperature a_ℓm coefficients
- `planck_pr3_emode_alm.fits` - E-mode polarization a_ℓm (for replication)

---

## Workflow

### Stage 1: Exploratory Scan

**Goal**: Detect candidate signals without commitment.

**When to use**: Initial exploration, hypothesis generation.

**DO NOT**: Claim detection, use words like "evidence" or "confirmed".

#### Step 1.1: Prepare Data

```bash
# Compute SHA-256 hash for provenance
sha256sum data/planck_pr3/alm/planck_pr3_temperature_alm.fits

# Record hash for later validation
```

#### Step 1.2: Run Exploratory Scan

```bash
cd forensic_fingerprint

python run_exploratory_phase_scan.py \
    --alm_file ../data/planck_pr3/alm/planck_pr3_temperature_alm.fits \
    --lmax 2048 \
    --ell_min 30 \
    --ell_max 1500 \
    --periods 255 256 137 139 \
    --n_surrogates 10000 \
    --seed 42 \
    --output_dir out/exploratory_phase_scan \
    --label planck_pr3_temperature
```

**Parameters**:
- `--alm_file`: Path to FITS file with a_ℓm coefficients
- `--lmax`: Maximum ℓ in alm array (e.g., 2048 for Planck)
- `--ell_min`, `--ell_max`: Multipole range for test (e.g., 30-1500)
- `--periods`: Periods to test (default: [255, 256, 137, 139])
- `--n_surrogates`: Monte Carlo samples (10000 recommended)
- `--seed`: Random seed (42 for reproducibility)

**Optional flags**:
- `--scan_primes`: Add prime numbers in [100, 300] to scan list

#### Step 1.3: Review Results

```bash
# Read Markdown report
cat out/exploratory_phase_scan/EXPLORATORY_PHASE_SCAN.md

# Read JSON results
python -m json.tool out/exploratory_phase_scan/results_planck_pr3_temperature.json
```

**Interpret results**:

| p-value range | Status | Action |
|---------------|--------|--------|
| p < 0.001 | **STRONG CANDIDATE** 🔴 | High priority for confirmation |
| 0.001 ≤ p < 0.01 | **CANDIDATE** 🟡 | Worth confirming |
| p ≥ 0.01 | **NULL** ⚪ | No further action |

**Example output**:
```
Period 255: R = 0.123456, p = 0.0034  → CANDIDATE 🟡
Period 256: R = 0.098765, p = 0.4521  → NULL ⚪
```

**If CANDIDATE found**: Proceed to Stage 2 (Pre-registration).  
**If all NULL**: Try different ℓ-ranges or observables.

---

### Stage 2: Pre-Registration

**Goal**: Lock all analysis parameters before confirmatory test.

**When to use**: After exploratory scan finds candidate signal.

**CRITICAL**: Pre-register BEFORE running confirmatory test on candidate period.

#### Step 2.1: Create Pre-Registration File

```bash
cd forensic_fingerprint/pre_registration

# Copy template
cp PHASE_TEST_v1_TEMPLATE.json PHASE_TEST_v1.json

# Edit PHASE_TEST_v1.json
nano PHASE_TEST_v1.json
```

#### Step 2.2: Fill Required Fields

**Dataset**:
```json
"dataset": {
  "description": "Planck PR3 Temperature Map (full-mission)",
  "alm_file": "data/planck_pr3/alm/planck_pr3_temperature_alm.fits",
  "alm_sha256": "INSERT_ACTUAL_SHA256_HERE",
  "component_separation": "Commander-Ruler",
  "release": "Planck 2018 PR3"
}
```

**Compute SHA-256**:
```bash
sha256sum ../../data/planck_pr3/alm/planck_pr3_temperature_alm.fits
```

**Insert hash** into JSON (replace `INSERT_ACTUAL_SHA256_HERE`).

**Lock periods** (based on exploratory candidate):
```json
"periods": [255, 256],
"periods_rationale": "Exploratory scan found candidate at 255, including 256 as control"
```

**Set significance threshold**:
```json
"significance_threshold": 0.01,
"significance_threshold_description": "p < 0.01 for PASS, p ≥ 0.01 for NULL"
```

**Alternatives**:
- α = 0.01 (2.6σ) - Standard candidate threshold
- α = 2.9e-7 (5σ) - Discovery threshold (very stringent)

#### Step 2.3: Commit Pre-Registration

**IMPORTANT**: Commit BEFORE running confirmatory test.

```bash
git add PHASE_TEST_v1.json
git commit -m "Pre-register phase coherence test v1 for periods 255, 256"
git push
```

**Record commit hash**:
```bash
git rev-parse HEAD
```

This creates a **timestamped, immutable record** of your pre-registration.

---

### Stage 3: Confirmatory Test

**Goal**: Court-grade test with pre-registered parameters.

**When to use**: After pre-registration is committed.

**Requirements**:
- ✅ Pre-registration file exists and committed
- ✅ Dataset SHA-256 verified
- ✅ No modifications to pre-registration

#### Step 3.1: Run Confirmatory Test

```bash
cd forensic_fingerprint

python run_real_data_cmb_phase_confirm.py \
    --pre_registration pre_registration/PHASE_TEST_v1.json \
    --output_dir out/confirmatory_phase_test
```

**What happens**:
1. ✅ Load and validate pre-registration
2. ✅ Verify dataset SHA-256 hash
3. ✅ Refuse to run if validation fails
4. ✅ Run test ONLY for pre-registered periods
5. ✅ Apply pre-registered significance threshold
6. ✅ Generate PASS/NULL verdict

#### Step 3.2: Review Verdict

```bash
cat out/confirmatory_phase_test/combined_verdict.md
```

**Possible verdicts**:

1. **✅ VERDICT: PASS**
   - p < threshold for at least one period
   - Phase coherence detected
   - **Action**: Proceed to Stage 4 (Replication)

2. **⚪ VERDICT: NULL**
   - p ≥ threshold for all periods
   - No significant phase coherence
   - **Action**: Report NULL, try alternative observables

3. **⚠️ VERDICT: INCONCLUSIVE**
   - Data validation failed
   - Insufficient data quality
   - **Action**: Fix data issues, re-run

#### Step 3.3: Save Results

```bash
# Results are already saved in output_dir
ls -lh out/confirmatory_phase_test/

# Should contain:
# - results.json           (full results)
# - combined_verdict.md    (PASS/NULL verdict)
```

**Archive results**:
```bash
# Create dated archive
tar -czf confirmatory_phase_test_$(date +%Y%m%d).tar.gz out/confirmatory_phase_test/

# Store permanently
mv confirmatory_phase_test_*.tar.gz archives/
```

---

### Stage 4: Replication

**Goal**: Verify signal in independent datasets.

**When to use**: ONLY if confirmatory test shows PASS.

**Requirements**: Signal must replicate in ≥2 independent datasets.

#### Step 4.1: Choose Replication Datasets

**Independent datasets**:
1. **E-mode polarization** (same mission, different observable)
2. **Different component separation** (SMICA vs NILC vs SEVEM)
3. **Different frequency** (100 GHz vs 143 GHz Planck maps)
4. **Different mission** (WMAP, ACT, SPT)

**Recommendation**: Start with E-mode polarization.

#### Step 4.2: Pre-Register Replication Test

```bash
cd pre_registration

# Create replication pre-registration
cp PHASE_TEST_v1.json PHASE_TEST_v1_EMODE.json

# Edit to point to E-mode alm file
nano PHASE_TEST_v1_EMODE.json
```

**Change dataset**:
```json
"dataset": {
  "description": "Planck PR3 E-mode Polarization Map",
  "alm_file": "data/planck_pr3/alm/planck_pr3_emode_alm.fits",
  "alm_sha256": "COMPUTE_NEW_SHA256_HERE",
  "component_separation": "Commander-Ruler",
  "release": "Planck 2018 PR3"
}
```

**Keep same periods** (critical for replication):
```json
"periods": [255, 256]
```

**Commit**:
```bash
git add PHASE_TEST_v1_EMODE.json
git commit -m "Pre-register replication test on E-mode polarization"
git push
```

#### Step 4.3: Run Replication Test

```bash
python run_real_data_cmb_phase_confirm.py \
    --pre_registration pre_registration/PHASE_TEST_v1_EMODE.json \
    --output_dir out/replication_emode
```

#### Step 4.4: Compare Results

**Consistent replication**:
- Both tests show PASS at same period
- Similar p-values (within factor of 10)
- Similar R(P) values

**Inconsistent results**:
- One PASS, one NULL
- Different best periods
- **Conclusion**: Signal is NOT robust, report NULL overall

**Example comparison**:

| Dataset | Best Period | R(P) | p-value | Verdict |
|---------|-------------|------|---------|---------|
| T-mode | 255 | 0.123 | 0.0034 | PASS ✅ |
| E-mode | 255 | 0.118 | 0.0071 | PASS ✅ |

→ **CONSISTENT** → Proceed to interpretation

| Dataset | Best Period | R(P) | p-value | Verdict |
|---------|-------------|------|---------|---------|
| T-mode | 255 | 0.123 | 0.0034 | PASS ✅ |
| E-mode | 128 | 0.089 | 0.0654 | NULL ⚪ |

→ **INCONSISTENT** → Report NULL, do not interpret

---

### Stage 5: Interpretation

**Goal**: Connect confirmed signal to theoretical framework.

**When to use**: ONLY after replication shows consistency.

**DO NOT**: Interpret exploratory or unreplicated results.

#### Step 5.1: Fill Interpretation Notes

```bash
cd forensic_fingerprint

# Copy template
cp INTERPRETATION_NOTES.md INTERPRETATION_RESULTS.md

# Fill in confirmed results
nano INTERPRETATION_RESULTS.md
```

**Include**:
- Confirmed signal summary (all datasets)
- Replication status table
- UBT theoretical context (clearly labeled as assumptions)
- Alternative explanations
- Predicted relationships
- Next experimental targets

#### Step 5.2: Prepare Publication

**Recommended structure**:

1. **Empirical paper** (discovery claim):
   - Title: "Periodic Phase Coherence in CMB Spherical Harmonics"
   - Focus: Robust detection across datasets
   - Minimal theoretical speculation
   - Pre-print to arXiv first

2. **Theoretical paper** (UBT interpretation):
   - Title: "Discrete Spacetime Fingerprint: Unified Biquaternion Theory Interpretation"
   - Clearly label as theoretical framework
   - Connect to broader UBT predictions
   - Testable predictions for future work

---

## Common Scenarios

### Scenario A: All Exploratory Periods NULL

**Result**: No candidate signals (all p ≥ 0.01)

**Action**:
1. Try different ℓ-ranges (e.g., 100-800, 500-1200)
2. Test polarization maps (E-mode, B-mode)
3. Try alternative observables (bispectrum, etc.)
4. Document NULL result in SEARCH_SPACE.md

**Do NOT**:
- Add more periods post-hoc
- Run multiple ℓ-ranges without correction
- Cherry-pick results

### Scenario B: Exploratory CANDIDATE, Confirmatory NULL

**Result**: Exploratory scan found p < 0.01, but confirmatory test shows p ≥ 0.01

**Interpretation**: Statistical fluctuation, not a real signal.

**Action**:
1. Report NULL verdict
2. Document in reports/
3. Move on to other observables

**This is expected**: Exploratory scans will occasionally find false positives.

### Scenario C: Confirmatory PASS, Replication NULL

**Result**: One dataset shows PASS, replication shows NULL

**Interpretation**: Non-robust signal, likely systematic artifact.

**Action**:
1. Report NULL overall
2. Document inconsistency
3. Investigate systematic differences between datasets

**Do NOT**: Claim detection based on single dataset.

### Scenario D: Confirmatory PASS, Replication PASS

**Result**: Consistent signal across ≥2 independent datasets

**Interpretation**: Robust candidate for publication.

**Action**:
1. ✅ Fill interpretation notes
2. ✅ Run additional replication tests
3. ✅ Prepare publication
4. ✅ Notify community for independent verification

**This is the goal**: Robust, replicable signal.

---

## Troubleshooting

### Error: "healpy required"

**Solution**:
```bash
pip install healpy
```

### Error: "alm size mismatch"

**Problem**: `lmax` parameter doesn't match alm file.

**Solution**: Check lmax from FITS header:
```python
import healpy as hp
alm = hp.read_alm("your_file.fits")
lmax = hp.Alm.getlmax(len(alm))
print(f"lmax = {lmax}")
```

Use correct `lmax` in command.

### Error: "SHA-256 mismatch"

**Problem**: Data file changed since pre-registration.

**Solution**:
1. Verify you're using correct file
2. Re-compute SHA-256:
   ```bash
   sha256sum your_alm_file.fits
   ```
3. If hash changed → **DO NOT proceed**
4. Create new pre-registration with updated hash

### Warning: "No valid (ℓ,m) pairs for period"

**Problem**: Period too large for ℓ-range.

**Solution**: Ensure `ell_max + period ≤ lmax`.

Example: If `lmax=2048` and `period=255`, need `ell_max ≤ 1793`.

---

## Best Practices

### Pre-Registration
- ✅ Commit BEFORE running confirmatory test
- ✅ Include rationale for period choices
- ✅ Verify SHA-256 hashes before committing
- ❌ Never modify pre-registration after commitment

### Exploratory Scans
- ✅ Label clearly as exploratory
- ✅ Use "candidate" language, not "detection"
- ✅ Document all periods tested
- ❌ Don't add periods based on data inspection

### Replication
- ✅ Use truly independent datasets
- ✅ Pre-register replication tests
- ✅ Report inconsistencies honestly
- ❌ Don't cherry-pick replication datasets

### Interpretation
- ✅ Wait for replication confirmation
- ✅ Consider alternative explanations
- ✅ Make testable predictions
- ❌ Don't over-claim based on single dataset

---

## Quick Reference

### Exploratory Scan
```bash
python run_exploratory_phase_scan.py \
    --alm_file <FITS_FILE> \
    --lmax <LMAX> \
    --periods 255 256 137 139 \
    --n_surrogates 10000 \
    --seed 42 \
    --output_dir out/exploratory
```

### Pre-Registration
```bash
cp pre_registration/PHASE_TEST_v1_TEMPLATE.json pre_registration/PHASE_TEST_v1.json
# Edit file, compute SHA-256
sha256sum <ALM_FILE>
# Insert into JSON, commit
git add pre_registration/PHASE_TEST_v1.json
git commit -m "Pre-register phase test"
```

### Confirmatory Test
```bash
python run_real_data_cmb_phase_confirm.py \
    --pre_registration pre_registration/PHASE_TEST_v1.json \
    --output_dir out/confirmatory
```

---

**Last Updated**: 2026-01-12  
**Version**: 1.0
