# WMAP TT Power Spectrum Data

**Purpose**: Instructions for downloading and verifying WMAP 9-year TT power spectrum for independent CMB comb replication.

## ⚠️ Important: Files Not Included in Repository

Large data files are NOT committed to this repository. You must download them separately from the official source.

## Official Data Source

**NASA Lambda Archive**  
URL: https://lambda.gsfc.nasa.gov/product/map/current/

**Release**: WMAP 9-Year Data Release (Final)

## Why WMAP?

WMAP provides **independent replication** of the CMB comb test:
- Different satellite (Wilkinson Microwave Anisotropy Probe vs Planck)
- Different instrument design and systematics
- Different analysis pipeline
- Independently published by NASA (vs ESA)

Per the pre-registered protocol (`forensic_fingerprint/PROTOCOL.md`), a candidate signal **must** appear consistently in at least two independent datasets.

## Required Files

### TT Power Spectrum

| File | Description | Size | Purpose |
|------|-------------|------|---------|
| `wmap_tt_spectrum_9yr_v5.txt` | TT power spectrum | ~20 KB | Independent CMB comb test |
| `wmap_tt_spectrum_9yr_v5.fits` | TT power spectrum (FITS) | ~50 KB | Alternative format |

**Note**: Choose either TXT or FITS format. The loader handles both.

### Optional: Covariance

| File | Description | Size | Purpose |
|------|-------------|------|---------|
| `wmap_tt_cov_9yr_v5.dat` | TT covariance matrix | ~2 MB | Whitening (if available) |

## Download Instructions

### Automated Download (Recommended)

Use the provided download script:

```bash
cd /home/runner/work/unified-biquaternion-theory/unified-biquaternion-theory
bash tools/data_download/download_wmap_tt.sh
```

This will:
1. Download TT spectrum to `data/wmap/raw/`
2. Skip existing files (idempotent)
3. Print hash computation instructions

### Manual Download

1. Visit https://lambda.gsfc.nasa.gov/product/map/current/
2. Navigate to: **Data Products** → **Power Spectra** → **TT Spectrum**
3. Download `wmap_tt_spectrum_9yr_v5.txt`
4. Save to `data/wmap/raw/`

**Direct Link** (as of 2026-01):
```
https://lambda.gsfc.nasa.gov/data/map/dr5/ancillary/wmap_tt_spectrum_9yr_v5.txt
```

## Computing Provenance Hashes

After downloading, compute SHA-256 hashes:

```bash
cd data/wmap/raw
python ../../../tools/data_provenance/hash_dataset.py wmap_tt_*.txt wmap_tt_*.fits > ../manifests/wmap_tt_manifest.json
```

## Validating Data Integrity

Before running analysis:

```bash
python tools/data_provenance/validate_manifest.py data/wmap/manifests/wmap_tt_manifest.json
```

**Critical**: Only use data that passes hash validation for court-grade analysis.

## File Format

### TXT Format

Space-separated columns:
```
# ell  C_ell_TT  sigma_TT
2      1100.2    50.1
3      1850.3    45.2
4      2620.8    48.5
...
```

Where:
- `ell`: Multipole moment (integer, 2 ≤ ℓ ≤ ~1200 for WMAP)
- `C_ell_TT`: TT power spectrum in μK²
- `sigma_TT`: 1-σ diagonal uncertainty

### FITS Format

Binary table with columns:
- `ell` (integer)
- `TT` (float, power in μK²)
- `TT_error` (float, 1-σ uncertainty)

The loader (`forensic_fingerprint/loaders/wmap.py`) auto-detects format.

## Multipole Range

WMAP TT spectrum limitations:
- **Available range**: 2 ≤ ℓ ≤ ~1200
- **Recommended for comb test**: 30 ≤ ℓ ≤ 800
- **Lower resolution** than Planck (larger beams, fewer detectors)

**Note**: WMAP's lower resolution means:
- Fewer multipoles → less statistical power
- Different systematics → independent check
- Use for **replication**, not primary detection

## Pre-Registered Manifests

Pre-registered SHA-256 hashes will be stored in `data/wmap/manifests/` after first download.

**Action Required**: After first download, commit manifest JSON (NOT data files) to repository.

## Data Processing Pipeline

1. **Download**: Use `download_wmap_tt.sh`
2. **Hash**: Compute SHA-256 with `hash_dataset.py`
3. **Validate**: Verify with `validate_manifest.py`
4. **Load**: Use `forensic_fingerprint/loaders/wmap.py`
5. **Analyze**: Run CMB comb test with `cmb_comb.py --dataset wmap`

See `forensic_fingerprint/RUNBOOK_REAL_DATA.md` for complete workflow.

## Data License

WMAP data is in the public domain (NASA policy). Usage for scientific analysis is freely permitted with proper citation.

**Required Citation**:
```
Hinshaw, G., et al. (2013). "Nine-year Wilkinson Microwave Anisotropy Probe (WMAP) 
Observations: Cosmological Parameter Results." 
The Astrophysical Journal Supplement Series, 208(2), 19. DOI: 10.1088/0067-0049/208/2/19
```

## Comparison with Planck

| Aspect | WMAP | Planck |
|--------|------|--------|
| Multipole range | 2-1200 | 2-2500 |
| Angular resolution | ~0.2° | ~5' |
| Sensitivity | Lower | Higher |
| Systematic errors | Different | Different |
| **Purpose** | **Replication** | **Primary detection** |

## Expected Consistency

If the CMB comb signature is real:
- **Same period** should appear in WMAP and Planck
- **Amplitude** may differ (different systematics, resolution)
- **Phase** should be consistent (physical origin)
- **p-value** might be weaker in WMAP (lower sensitivity)

If signature is spurious:
- Inconsistent periods between datasets
- Or null result in one dataset

This is the **independent replication criterion** required by the protocol.

## Related Documentation

- `forensic_fingerprint/RUNBOOK_REAL_DATA.md` - Complete analysis workflow
- `forensic_fingerprint/PROTOCOL.md` - Pre-registered protocol requirements
- `data/planck_pr3/README.md` - Primary dataset
- `tools/data_download/download_wmap_tt.sh` - Download script

---

**Last Updated**: 2026-01-10  
**Data Version**: WMAP 9-Year DR5 (Final Release)  
**Maintained by**: UBT Research Team
