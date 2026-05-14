# WMAP 9-Year Release Data

**Purpose**: Instructions for downloading and verifying WMAP 9-year datasets for independent replication.

## ⚠️ Important: Files Not Included in Repository

Large data files are NOT committed to this repository. You must download them separately from the official source.

## Official Data Source

**NASA Lambda Archive**  
URL: https://lambda.gsfc.nasa.gov/product/map/current/

**Release**: WMAP 9-Year Data Release

## Required Files for UBT Validation

### Power Spectrum Data

| File | Description | Size | Purpose |
|------|-------------|------|---------|
| `wmap_tt_spectrum_9yr_v5.txt` | TT power spectrum | ~20 KB | Independent CMB comb replication |

## Download Instructions

### Option 1: Direct Download (Recommended)

1. Visit https://lambda.gsfc.nasa.gov/product/map/current/
2. Navigate to: **Data Products** → **Power Spectra**
3. Download `wmap_tt_spectrum_9yr_v5.txt`

### Option 2: Command Line (wget)

```bash
cd data/wmap_9yr/

wget https://lambda.gsfc.nasa.gov/data/map/dr5/ancillary/wmap_tt_spectrum_9yr_v5.txt
```

## Pre-Registered File Hashes (SHA-256)

These hashes are **pre-registered** for protocol v1.0.

### Power Spectra

```
# TBD: Generate hashes after downloading official files
# Run: python ../../tools/data_provenance/hash_dataset.py wmap_tt_spectrum_9yr_v5.txt
```

**⚠️ ACTION REQUIRED**: After downloading, run:
```bash
python ../../tools/data_provenance/hash_dataset.py *.txt > manifest.json
```

## Validation

After downloading files, validate them:

```bash
python ../../tools/data_provenance/validate_manifest.py manifest.json
```

## File Format

### Power Spectrum File

Columns:
1. `ell` - Multipole moment
2. `C_ell` - Power spectrum value (μK²)
3. `sigma_C_ell` - Uncertainty (μK²)

Example:
```
# ell  C_ell  sigma_C_ell
2      1100.2  50.1
3      1850.3  45.2
...
```

## Purpose: Independent Replication

WMAP data provides independent verification of CMB comb signature test:
- Different satellite instrument
- Different analysis pipeline
- Independent systematic errors

Per `forensic_fingerprint/PROTOCOL.md`, a candidate signal must appear in **at least 2 independent datasets** to be considered for publication.

## Data License

WMAP data is public domain (NASA policy). Usage for scientific analysis is freely permitted.  
**Citation Required**: Hinshaw et al. (2013), ApJS, 208, 19

## Related Documentation

- `forensic_fingerprint/PROTOCOL.md` - Analysis protocol requiring replication
- `data/planck_2018/README.md` - Primary dataset
- `data/README.md` - General data directory overview

---

**Last Updated**: 2026-01-10  
**Data Version**: WMAP 9-Year (DR5)  
**Maintained by**: UBT Research Team
