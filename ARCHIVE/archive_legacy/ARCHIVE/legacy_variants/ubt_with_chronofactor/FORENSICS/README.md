# Forensic Testing Framework

## Purpose

This directory contains **court-grade** forensic testing pipelines for UBT predictions. All tests follow strict pre-registration, reproducibility, and fail-fast principles to ensure results are auditable and defensible.

## Core Philosophy

### Pre-Registration

All test parameters are **fixed before running**:
- Observable channel
- Dataset(s)
- Analysis method
- Pass/fail criteria
- Random seeds

**No post-hoc tuning.** If you change parameters after seeing results, you must treat it as a **new experiment**.

### Reproducibility

Every test includes:
- **SHA-256 manifests** for all input data
- **Exact command** to reproduce
- **Version-controlled code** (git commit hash)
- **Pre-registered random seeds**
- **Deterministic pipelines** (same inputs → same outputs)

### Fail-Fast Philosophy

Tests are designed to **fail loudly** rather than produce silent errors:
- HTML file detection (data download failures)
- Units mismatch checks (Dl vs Cl)
- Sanity checks on residuals (χ²/dof limits)
- Manifest validation (SHA-256 hash verification)

**If anything is wrong, the test aborts with clear error message.**

### Manifest Enforcement

Every dataset must have a **manifest file** (JSON) containing:
```json
{
  "generated": "2026-01-12T03:00:00",
  "hash_algorithm": "SHA-256",
  "files": [
    {
      "filename": "...",
      "path": "...",
      "size": <bytes>,
      "sha256": "<hash>"
    }
  ]
}
```

**Before running**, manifest is validated:
1. Compute SHA-256 hash of each file
2. Compare to stored hash
3. **If ANY file fails → ABORT**
4. If all pass → proceed with confidence

This prevents:
- Accidental data corruption
- Silent download failures (HTML error pages)
- Version confusion (different data releases)
- Tampering (malicious or accidental)

## Directory Structure

```
FORENSICS/
├── protocols/                           # Test protocols and criteria
│   ├── PROTOCOL.md                     # General testing protocol
│   ├── FORENSIC_VERDICT_CRITERIA.md   # Pass/fail criteria
│   └── AUDIT_PROTOCOL.md              # Audit procedures
├── cmb_comb/                           # CMB comb fingerprint tests
│   ├── run_cmb_comb_court_grade.py   # Main court-grade pipeline
│   └── cmb_comb.py                    # Core analysis module
├── manifests/                          # SHA-256 manifests (moved to DATA/manifests/)
└── README.md                           # This file
```

**Note**: Manifests are now in `DATA/manifests/` for centralized data provenance.

## Pre-Registration Protocol

### Before Running a Test

1. **Choose test parameters** (dataset, method, criteria)
2. **Document in protocol file** (see `protocols/`)
3. **Commit protocol to git** (creates immutable record)
4. **Do NOT look at results** until protocol is committed

### Running the Test

1. **Validate data manifests** (SHA-256 hashes)
2. **Run analysis with pre-registered parameters**
3. **Save all outputs** (plots, JSON, logs)
4. **Generate verdict** (PASS/FAIL based on pre-registered criteria)

### After the Test

1. **Document result** in `FINGERPRINTS/`
   - PASS → `confirmed/`
   - Weak → `candidate/`
   - **FAIL → `null_results/`** (never delete)
2. **Commit result to git** (permanent record)
3. **Never change** pass/fail criteria retroactively

## Court-Grade Requirements

A test is "court-grade" if:

✅ **Pre-registered** - Parameters fixed before running
✅ **Reproducible** - Includes exact command and seed
✅ **Provenance** - SHA-256 manifests for all data
✅ **Auditable** - Full logs and intermediate outputs saved
✅ **Honest** - Null results preserved and documented

## Example: CMB Comb Test

### Pre-Registration

See `protocols/FORENSIC_VERDICT_CRITERIA.md`:
- Dataset: Planck PR3 TT + WMAP 9yr TT
- Variant: C (Explicit Frame Synchronization)
- ℓ ranges: Planck 30-1500, WMAP 30-800
- MC samples: 10,000
- Random seed: 42
- Pass criteria: p < 0.01 (Planck) AND p < 0.05 (WMAP) AND same period

### Execution

```bash
python FORENSICS/cmb_comb/run_cmb_comb_court_grade.py \
    --planck_obs DATA/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model DATA/planck_pr3/derived/planck_pr3_tt_model_extracted_minfmt.txt \
    --planck_manifest DATA/manifests/planck_pr3_tt_manifest.json \
    --wmap_obs DATA/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_manifest DATA/manifests/wmap_tt_manifest.json \
    --variant C --mc_samples 10000 --seed 42
```

### Result

- Planck: p = 0.919 (NULL)
- WMAP: p = 1e-4 (CANDIDATE, not replicated)
- **Combined verdict**: FAIL
- Documented in: `FINGERPRINTS/null_results/combined_verdict.md`

## Failure Modes and Safeguards

### HTML File Detection

**Problem**: Download failure produces HTML error page instead of data.

**Safeguard**: Check for `<html` or `<!DOCTYPE` in file → abort with clear error.

### Units Mismatch

**Problem**: Wrong model file or Dl/Cl confusion → meaningless results.

**Safeguard**: 
- Reject files containing `-log(Like)` or `logLike`
- Check χ²/dof after loading → abort if > 1000
- Auto-detect and convert Dl ↔ Cl

### Manifest Validation Failure

**Problem**: Data file corrupted or wrong version.

**Safeguard**: Compute SHA-256 → compare to manifest → abort if mismatch.

## For External Auditors

If auditing UBT results:

1. **Check pre-registration** - Verify protocol exists in git before test date
2. **Verify manifests** - Recompute SHA-256 hashes of data files
3. **Reproduce test** - Use exact command from protocol
4. **Compare outputs** - Should match bit-for-bit (given same seed)
5. **Check null results** - Verify failures are documented, not hidden

## Tools for Forensic Testing

See `TOOLS/data_provenance/` for:
- Manifest generation scripts
- SHA-256 validation tools
- Reproducibility checkers

## References

- **Fingerprints**: `FINGERPRINTS/` - Test results organized by status
- **Data**: `DATA/` - Raw data with manifests
- **Theory**: `THEORY/` - Predictions being tested

---

**Philosophy**: Make it impossible to p-hack. Make null results visible. Make auditing easy.

**Last updated**: 2026-01-12
