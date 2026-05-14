# Pre-Registration Directory

This directory contains **court-grade pre-registration files** for confirmatory tests.

## Purpose

Pre-registration prevents p-hacking and data dredging by **locking all analysis parameters before examining data**:

- Dataset identities and SHA-256 hashes
- Statistical test specification
- Null model definition
- Significance thresholds
- Multiple-testing correction methods

## File Naming Convention

- `PHASE_TEST_v1_TEMPLATE.json` - Template for phase coherence tests
- `PHASE_TEST_v1.json` - Actual pre-registration (created when ready to confirm)
- `COMB_TEST_v1.json` - Amplitude comb test pre-registration
- etc.

## Required Fields

Every pre-registration JSON must contain:

### Metadata
- `version` - Protocol version (e.g., "1.0")
- `test_name` - Descriptive name
- `description` - What is being tested
- `pre_registration_date` - ISO timestamp

### Dataset
- `dataset.alm_file` - Exact file path
- `dataset.alm_sha256` - SHA-256 hash for validation
- `dataset.description` - Human-readable description
- `dataset.release` - Data release version

### Test Parameters
- `lmax` - Maximum multipole in alm array
- `ell_min` - Minimum ℓ for test
- `ell_max` - Maximum ℓ for test
- `periods` - List of periods to test (LOCKED)

### Statistical Method
- `statistic` - Name of test statistic (e.g., "phase_coherence_R")
- `statistic_definition` - Mathematical definition
- `null_model` - Null model name (e.g., "phase_randomized_surrogates")
- `null_model_description` - How surrogates are generated

### Monte Carlo
- `n_surrogates` - Number of MC samples
- `seed` - Random seed for reproducibility

### Significance
- `significance_threshold` - α level (e.g., 0.01)
- `multiple_testing_correction` - Correction method or "none"

### Replication
- `replication_requirement` - How signal must be replicated

## Creating a Pre-Registration

### Step 1: Copy Template

```bash
cp PHASE_TEST_v1_TEMPLATE.json PHASE_TEST_v1.json
```

### Step 2: Fill in Dataset Details

Compute SHA-256 hash of your data file:

```bash
sha256sum data/planck_pr3/alm/planck_pr3_temperature_alm.fits
```

Insert hash into JSON:

```json
"dataset": {
  "alm_file": "data/planck_pr3/alm/planck_pr3_temperature_alm.fits",
  "alm_sha256": "a1b2c3d4e5f6... (actual hash)"
}
```

### Step 3: Lock Periods

Choose periods based on **theoretical motivation**, not data inspection:

```json
"periods": [255, 256],
"periods_rationale": "255 = byte-like (2^8-1), 256 = power of 2"
```

**DO NOT** add periods after looking at exploratory results.

### Step 4: Set Significance Threshold

Choose α before seeing data:

```json
"significance_threshold": 0.01
```

Standard choices:
- α = 0.01 (2.6σ) - Interesting candidate
- α = 2.9e-7 (5σ) - Discovery threshold

### Step 5: Commit Pre-Registration

```bash
git add PHASE_TEST_v1.json
git commit -m "Pre-register phase coherence test v1"
git push
```

**Important**: Commit BEFORE running confirmatory test.

## Using Pre-Registration

Run confirmatory test with:

```bash
python run_real_data_cmb_phase_confirm.py \
    --pre_registration pre_registration/PHASE_TEST_v1.json \
    --output_dir out/confirmatory_phase_test
```

The script will:
1. ✅ Validate pre-registration format
2. ✅ Verify dataset SHA-256 hashes
3. ✅ Run test ONLY for pre-registered periods
4. ✅ Apply pre-registered significance threshold
5. ✅ Generate PASS/NULL/INCONCLUSIVE verdict

## Violation Checks

The confirmatory runner **refuses to run** if:

- ❌ Pre-registration file missing
- ❌ Dataset SHA-256 mismatch
- ❌ Required fields missing
- ❌ Data file not found

This ensures **court-grade reproducibility**.

## Modification Policy

**Pre-registrations CANNOT be modified after commitment.**

If you need to change parameters:
1. Create a NEW pre-registration file with incremented version (e.g., `PHASE_TEST_v2.json`)
2. Document reason for change
3. Previous pre-registration remains in repository for transparency

## Example: Full Workflow

### Exploratory Phase (Before Pre-Registration)

```bash
# Run exploratory scan (low commitment)
python run_exploratory_phase_scan.py \
    --alm_file data/planck_pr3/alm/planck_pr3_temperature_alm.fits \
    --lmax 2048 \
    --output_dir out/exploratory

# Review results
cat out/exploratory/EXPLORATORY_PHASE_SCAN.md
```

Result: "CANDIDATE signal at period 255 (p = 0.003)"

### Pre-Registration (Lock Parameters)

```bash
# Create pre-registration
cp pre_registration/PHASE_TEST_v1_TEMPLATE.json pre_registration/PHASE_TEST_v1.json

# Edit PHASE_TEST_v1.json:
# - Insert SHA-256 hash
# - Lock periods to [255, 256]
# - Set α = 0.01

# Commit
git add pre_registration/PHASE_TEST_v1.json
git commit -m "Pre-register phase test for periods 255, 256"
git push
```

### Confirmatory Test (Court-Grade)

```bash
# Run confirmatory test
python run_real_data_cmb_phase_confirm.py \
    --pre_registration pre_registration/PHASE_TEST_v1.json \
    --output_dir out/confirmatory_phase_test

# Review verdict
cat out/confirmatory_phase_test/combined_verdict.md
```

Result: "VERDICT: PASS" or "VERDICT: NULL"

### Replication (Independent Dataset)

```bash
# Repeat on E-mode polarization
# Create new pre-registration: PHASE_TEST_v1_EMODE.json
# Run confirmatory test on E-mode data
```

If both PASS → Publication-worthy result  
If one NULL → Non-robust signal, report NULL

## Templates Available

- `PHASE_TEST_v1_TEMPLATE.json` - Phase coherence test
- (Add more templates as needed for other test types)

## References

- See `../PROTOCOL.md` for complete protocol
- See `../README.md` for overall project structure
- See `../RUNBOOK_PHASE_COMB.md` for detailed usage

---

**Last Updated**: 2026-01-12
