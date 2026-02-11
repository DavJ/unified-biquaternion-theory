# Planck 2018 Legacy Release Data

**Purpose**: Instructions for downloading and verifying Planck 2018 cosmological datasets.

## ⚠️ Important: Files Not Included in Repository

Large data files are NOT committed to this repository. You must download them separately from the official source.

## Official Data Source

**Planck Legacy Archive (PLA)**  
URL: https://pla.esac.esa.int/pla/

**Release**: Planck 2018 Legacy Release (PR4)

## Required Files for UBT Validation

### Power Spectrum Data

| File | Description | Size | Purpose |
|------|-------------|------|---------|
| `COM_PowerSpect_CMB-TT-full_R3.01.txt` | TT power spectrum | ~50 KB | CMB comb test |
| `COM_PowerSpect_CMB-TE-full_R3.01.txt` | TE power spectrum | ~50 KB | Replication |
| `COM_PowerSpect_CMB-EE-full_R3.01.txt` | EE power spectrum | ~50 KB | Replication |

### MCMC Chains (for grid quantization test)

| File | Description | Size | Purpose |
|------|-------------|------|---------|
| `base/plikHM_TTTEEE_lowl_lowE/base_plikHM_TTTEEE_lowl_lowE_*.txt` | Baseline MCMC chains | ~500 MB | Grid 255 test |

**Note**: MCMC chains are very large. Download only if running grid quantization test locally.

## Download Instructions

### Option 1: Direct Download (Recommended)

1. Visit https://pla.esac.esa.int/pla/
2. Navigate to: **Cosmological Parameters** → **Power Spectra**
3. Download `COM_PowerSpect_CMB-TT-full_R3.01.txt` (and TE/EE variants)
4. For MCMC chains: **Cosmological Parameters** → **MCMC Chains** → Baseline

### Option 2: Command Line (wget)

```bash
cd data/planck_2018/

# Power spectra
wget "https://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_PowerSpect_CMB-TT-full_R3.01.fits" -O COM_PowerSpect_CMB-TT-full_R3.01.fits

# Convert FITS to TXT if needed (requires astropy)
# python -c "from astropy.io import fits; import numpy as np; ..."
```

**Note**: Exact URLs may change. Refer to PLA website for current links.

## Pre-Registered File Hashes (SHA-256)

These hashes are **pre-registered** for protocol v1.0. Any dataset with different hash requires new protocol version.

### Power Spectra (Text Format)

```
# TBD: Generate hashes after downloading official files
# Run: python ../../tools/data_provenance/hash_dataset.py COM_PowerSpect_CMB-TT-full_R3.01.txt
```

**⚠️ ACTION REQUIRED**: After downloading, run:
```bash
python ../../tools/data_provenance/hash_dataset.py *.txt > manifest.json
```

This generates the SHA-256 manifest for verification.

## Validation

After downloading files, validate them:

```bash
python ../../tools/data_provenance/validate_manifest.py manifest.json
```

This ensures files match pre-registered hashes.

## File Format

### Power Spectrum Files (TXT)

Columns:
1. `ell` - Multipole moment
2. `C_ell` - Power spectrum value (μK²)
3. `sigma_C_ell` - Uncertainty (μK²)

Example:
```
# ell  C_ell  sigma_C_ell
2      1305.6  30.2
3      2015.3  28.5
...
```

### MCMC Chains

Columns depend on parameter set. Typical columns:
- `weight` - MCMC sample weight
- `omegabh2` - Ω_b h²
- `omegach2` - Ω_c h²
- `theta` - θ_s
- `tau` - Optical depth
- `ns` - n_s
- `logA` - ln(10¹⁰ A_s)

## Data License

Planck data is released under ESA's data policy. Usage for scientific analysis is permitted.  
**Citation Required**: Planck Collaboration (2020), Astronomy & Astrophysics, 641, A1-A10

## Related Documentation

- `forensic_fingerprint/PROTOCOL.md` - Analysis protocol
- `tools/planck_validation/` - Python implementation
- `data/README.md` - General data directory overview

---

**Last Updated**: 2026-01-10  
**Data Version**: Planck 2018 Legacy (PR4)  
**Maintained by**: UBT Research Team
