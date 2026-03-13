# CMB Real Data Integration - Implementation Summary

**Date**: 2026-01-10  
**Status**: COMPLETE ✅  
**PR Branch**: copilot/add-cmb-fingerprint-data-layout

---

## Overview

This implementation enables the UBT Forensic Fingerprint CMB comb test to run on **real Planck PR3 and WMAP datasets** with full court-grade reproducibility and data provenance tracking.

## What Was Delivered

### 1. Data Infrastructure

**Directory Structure:**
```
data/
├── planck_pr3/
│   ├── README.md          # Download and usage instructions
│   ├── .gitignore         # Prevents committing large files
│   ├── raw/               # Downloaded data files (not in git)
│   └── manifests/         # SHA-256 hash manifests (in git)
├── wmap/
│   ├── README.md
│   ├── .gitignore
│   ├── raw/
│   └── manifests/
```

**Features:**
- Comprehensive README files with exact download URLs
- .gitignore preventing accidental data commits
- SHA-256 hash manifests for provenance

### 2. Download Automation

**Scripts Created:**
```
tools/data_download/
├── download_planck_pr3_cosmoparams.sh
└── download_wmap_tt.sh
```

**Features:**
- Idempotent (skip existing files)
- Fallback to manual instructions on failure
- Clear next-step instructions

### 3. Data Provenance Tools

**Scripts Created:**
```
tools/data_provenance/
├── hash_dataset.py      # Compute SHA-256 hashes
└── validate_manifest.py # Validate files against hashes
```

**Features:**
- Court-grade reproducibility
- Tamper detection
- Version control for datasets

### 4. Data Loaders

**Module Created:**
```
forensic_fingerprint/loaders/
├── __init__.py
├── planck.py  # Planck PR3 loader
└── wmap.py    # WMAP loader
```

**Features:**
- Support for text and FITS formats
- Automatic format detection
- Multipole range filtering (--ell_min, --ell_max)
- Full covariance or diagonal sigma
- Unified data interface

### 5. Upgraded CMB Comb CLI

**Enhanced cmb_comb.py with:**

**New Arguments:**
```bash
--dataset {planck_pr3,wmap,custom}  # Dataset selection
--input_obs FILE                     # Observed spectrum
--input_model FILE                   # Theoretical model
--input_cov FILE                     # Covariance (optional)
--ell_min INT                        # Minimum multipole
--ell_max INT                        # Maximum multipole
--output_dir DIR                     # Output directory
```

**New Features:**
- Whitening via Cholesky decomposition when covariance provided
- Timestamped output directories
- Dataset provenance in results
- Backward compatible with legacy mode

### 6. Court-Grade Runbook

**File Created:**
```
forensic_fingerprint/RUNBOOK_REAL_DATA.md (12.5 KB)
```

**Contents:**
- Complete workflow: Download → Hash → Validate → Analyze
- PASS/FAIL criteria with replication requirements
- Example commands for Planck and WMAP
- Troubleshooting guide
- Archiving and provenance procedures

### 7. Comprehensive Testing

**Test Coverage:**
```
tests/test_forensic_fingerprint.py
```

**New Tests Added:**
- 7 data loader tests (Planck/WMAP)
- 2 whitening/covariance tests
- All using synthetic fixtures (no real data)

**Results:**
- 32 total tests
- All passing ✅
- No real data downloads in CI

### 8. CI Integration

**Updated:**
```
.github/workflows/forensic_fingerprint.yml
```

**Ensures:**
- Tests run automatically on push/PR
- No real data downloads
- Clear summary of capabilities

---

## Usage

### Quick Start

```bash
# 1. Download Planck PR3 data
bash tools/data_download/download_planck_pr3_cosmoparams.sh

# 2. Compute hashes
cd data/planck_pr3/raw
python ../../../tools/data_provenance/hash_dataset.py *.txt > ../manifests/manifest.json

# 3. Validate
cd ../../..
python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/manifest.json

# 4. Run CMB comb test
cd forensic_fingerprint/cmb_comb
python cmb_comb.py --dataset planck_pr3 \
    --input_obs ../../data/planck_pr3/raw/spectrum.txt \
    --input_model ../../data/planck_pr3/raw/model.txt \
    --ell_min 30 --ell_max 1500
```

### With Full Covariance (Whitening)

```bash
python cmb_comb.py --dataset planck_pr3 \
    --input_obs ../../data/planck_pr3/raw/spectrum.txt \
    --input_model ../../data/planck_pr3/raw/model.txt \
    --input_cov ../../data/planck_pr3/raw/covariance.dat \
    --ell_min 30 --ell_max 1500
```

### WMAP Replication

```bash
# Download WMAP
bash tools/data_download/download_wmap_tt.sh

# Run test
cd forensic_fingerprint/cmb_comb
python cmb_comb.py --dataset wmap \
    --input_obs ../../data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --ell_min 30 --ell_max 800
```

### Legacy Mode (Backward Compatible)

```bash
# Still works with old interface
python cmb_comb.py obs.txt model.txt output_dir/
```

---

## Files Changed/Created

### New Files (25)

**Data Structure:**
- `data/planck_pr3/README.md`
- `data/planck_pr3/.gitignore`
- `data/planck_pr3/raw/.gitkeep`
- `data/planck_pr3/manifests/.gitkeep`
- `data/wmap/README.md`
- `data/wmap/.gitignore`
- `data/wmap/raw/.gitkeep`
- `data/wmap/manifests/.gitkeep`

**Tools:**
- `tools/data_download/download_planck_pr3_cosmoparams.sh`
- `tools/data_download/download_wmap_tt.sh`

**Loaders:**
- `forensic_fingerprint/loaders/__init__.py`
- `forensic_fingerprint/loaders/planck.py`
- `forensic_fingerprint/loaders/wmap.py`

**Documentation:**
- `forensic_fingerprint/RUNBOOK_REAL_DATA.md`

### Modified Files (3)

- `forensic_fingerprint/cmb_comb/cmb_comb.py` - Major upgrade with new CLI
- `tests/test_forensic_fingerprint.py` - Added 9 new tests
- `.github/workflows/forensic_fingerprint.yml` - Updated summary

---

## Technical Details

### Whitening Algorithm

When full covariance provided:
1. Compute Cholesky decomposition: L such that Cov = L L^T
2. Whiten residuals: r_whitened = L^{-1} (C_obs - C_model)
3. Falls back to diagonal if Cholesky fails (non-positive definite)

### Look-Elsewhere Correction

The p-value includes correction for testing multiple periods:
- For each MC trial, compute max(Δχ²) over all candidate periods
- P-value = fraction of trials with max(Δχ²) ≥ observed
- Controls family-wise error rate (FWER)

### Replication Criterion

For a detection to be valid:
- Planck p-value < 0.01
- WMAP p-value < 0.05
- Same period Δℓ in both datasets
- Consistent phase (within π/2)

---

## Next Steps for Users

1. **Read the runbook**: `forensic_fingerprint/RUNBOOK_REAL_DATA.md`
2. **Download data**: Use provided scripts
3. **Validate hashes**: Ensure data integrity
4. **Run analysis**: Follow runbook examples
5. **Document results**: Use PROVENANCE.txt template from runbook

---

## Maintenance Notes

### For Future Updates

**Adding new datasets:**
1. Create `data/DATASET_NAME/` with same structure
2. Add README with download instructions
3. Create loader in `forensic_fingerprint/loaders/`
4. Update `cmb_comb.py` dataset choices
5. Add tests in `test_forensic_fingerprint.py`

**Updating data URLs:**
1. Edit download scripts in `tools/data_download/`
2. Update README files in `data/*/`
3. Test idempotent behavior

**Changing pre-registered parameters:**
1. Update `CANDIDATE_PERIODS` in `cmb_comb.py`
2. Update documentation in `PROTOCOL.md`
3. Increment protocol version
4. Document in `RUNBOOK_REAL_DATA.md`

---

## Testing

All 32 tests pass:
```bash
pytest tests/test_forensic_fingerprint.py -v
```

Test breakdown:
- 6 CMB comb core tests
- 6 Grid 255 tests
- 6 Invariance tests
- 5 Integration tests
- 7 Data loader tests (NEW)
- 2 Whitening tests (NEW)

---

## Documentation Links

- **Main Runbook**: `forensic_fingerprint/RUNBOOK_REAL_DATA.md`
- **Protocol**: `forensic_fingerprint/PROTOCOL.md`
- **Planck Data**: `data/planck_pr3/README.md`
- **WMAP Data**: `data/wmap/README.md`
- **Architecture**: `forensic_fingerprint/ARCHITECTURE_VARIANTS.md`

---

**Implementation Complete**: 2026-01-10  
**All Deliverables**: ✅ DELIVERED  
**Ready for**: Production use on real CMB data
