# Planck PR3 (Release 3) Data

**Purpose**: Instructions for downloading and verifying Planck PR3 cosmological parameter datasets for court-grade CMB comb analysis.

## ⚠️ Important: Files Not Included in Repository

Large data files are NOT committed to this repository. You must download them separately from the official source.

## Official Data Source

**IRSA Planck Mission Archive**  
URL: https://irsa.ipac.caltech.edu/Missions/planck.html

**Release**: Planck 2018 Release 3 (PR3) - Final Legacy Release

## Required Files for UBT CMB Comb Test

### Cosmological Parameters (TT Power Spectrum)

The main file needed for the CMB comb fingerprint test:

| File | Description | Size | Purpose |
|------|-------------|------|---------|
| `COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip` | Best-fit parameters and spectra | ~10 MB | Contains TT power spectrum |
| `COM_PowerSpect_CMB-TT-full_R3.01.txt` (or .fits) | TT power spectrum | ~50 KB | CMB comb test input |

**Note**: The cosmoparams package includes:
- Best-fit ΛCDM model parameters
- TT, TE, EE power spectra
- Theoretical model predictions
- Covariance matrices (if available)

### Alternative: Direct Power Spectrum Download

If you only need the TT power spectrum without full parameter chains:

| File | Description | Size | Purpose |
|------|-------------|------|---------|
| `COM_PowerSpect_CMB-TT-full_R3.01.fits` | TT power spectrum (FITS) | ~100 KB | Direct CMB data |

## Download Instructions

### Automated Download (Recommended)

Use the provided download script:

```bash
cd /home/runner/work/unified-biquaternion-theory/unified-biquaternion-theory
bash tools/data_download/download_planck_pr3_cosmoparams.sh
```

This will:
1. Download files to `data/planck_pr3/raw/`
2. Skip files that already exist (idempotent)
3. Print instructions for hash computation

### Manual Download

1. Visit https://irsa.ipac.caltech.edu/Missions/planck.html
2. Navigate to: **Release 3 (2018)** → **Cosmological Parameters**
3. Locate: `COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip`
4. Download and extract to `data/planck_pr3/raw/`

**Direct Links** (as of 2026-01):
- Cosmoparams: https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/
- Power Spectra: https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/

## Computing Provenance Hashes

After downloading, compute SHA-256 hashes for reproducibility:

```bash
cd data/planck_pr3/raw
python ../../../tools/data_provenance/hash_dataset.py *.txt *.fits > ../manifests/planck_pr3_tt_manifest.json
```

Or for the full cosmoparams package:

```bash
cd data/planck_pr3/raw
python ../../../tools/data_provenance/hash_dataset.py COM_CosmoParams_*.zip > ../manifests/cosmoparams_manifest.json
```

## Validating Data Integrity

Before running analysis, validate file hashes:

```bash
python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/planck_pr3_tt_manifest.json
```

**Critical**: Only use data that passes hash validation for court-grade analysis.

## File Format

### Power Spectrum Files (TEXT format)

Expected columns (space or tab-separated):
```
# ell  C_ell_TT  sigma_TT
2      1305.6    30.2
3      2015.3    28.5
4      2850.1    32.1
...
```

Where:
- `ell`: Multipole moment (integer, typically 2 ≤ ℓ ≤ 2500)
- `C_ell_TT`: TT power spectrum in μK²
- `sigma_TT`: Uncertainty (1-σ diagonal error)

### Power Spectrum Files (FITS format)

FITS files contain:
- Binary table with columns: `ell`, `TT`, `TT_error`
- Additional columns for TE, EE if multi-spectrum file
- Metadata in FITS headers

The loader (`forensic_fingerprint/loaders/planck.py`) handles both formats automatically.

## Covariance Matrix

For the full covariance matrix (if available):

| File | Description | Size | Purpose |
|------|-------------|------|---------|
| `COM_CosmoParams_base-plikHM-TT-lowl_R3.00_cov.dat` | TT covariance | Variable | Whitening in comb test |

**Note**: Full covariance matrices are large. If not available, the CMB comb test will use diagonal uncertainties with a warning.

## Pre-Registered Manifests

Pre-registered SHA-256 hashes will be stored in `data/planck_pr3/manifests/` after the first download. These serve as the **locked reference** for reproducibility.

**Action Required**: After your first download, commit the manifest JSON files (NOT the data files) to the repository.

## Data Processing Pipeline

1. **Download**: Use `download_planck_pr3_cosmoparams.sh`
2. **Hash**: Compute SHA-256 with `hash_dataset.py`
3. **Validate**: Verify with `validate_manifest.py`
4. **Load**: Use `forensic_fingerprint/loaders/planck.py`
5. **Analyze**: Run CMB comb test with `cmb_comb.py --dataset planck_pr3`

See `forensic_fingerprint/RUNBOOK_REAL_DATA.md` for complete workflow.

## Data License

Planck data is released under ESA's scientific data policy. Usage for scientific analysis is permitted with proper citation.

**Required Citation**:
```
Planck Collaboration (2020). "Planck 2018 results. VI. Cosmological parameters."
Astronomy & Astrophysics, 641, A6. DOI: 10.1051/0004-6361/201833910
```

## Multipole Range

For CMB comb test:
- **Minimum ℓ**: 30 (avoid low-ℓ cosmic variance and foreground contamination)
- **Maximum ℓ**: 2000 (sufficient for period detection, avoid high-ℓ systematics)
- **Recommended**: 30 ≤ ℓ ≤ 1500

These can be adjusted via `--ell_min` and `--ell_max` CLI flags.

## Related Documentation

- `forensic_fingerprint/RUNBOOK_REAL_DATA.md` - Complete analysis runbook
- `forensic_fingerprint/PROTOCOL.md` - Pre-registered protocol
- `data/wmap/README.md` - Independent replication dataset
- `tools/data_download/download_planck_pr3_cosmoparams.sh` - Download script

---

**Last Updated**: 2026-01-10  
**Data Version**: Planck PR3 (Release 3.00, 2018 Legacy)  
**Maintained by**: UBT Research Team
