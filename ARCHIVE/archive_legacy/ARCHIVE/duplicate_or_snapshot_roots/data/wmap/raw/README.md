# WMAP 9-Year TT Power Spectrum Data

**IMPORTANT**: The files in this directory are MOCK DATA for testing the forensic fingerprint pipeline.

## Real Data Source

The actual WMAP 9-year TT power spectrum data should be downloaded from NASA Lambda Archive:

**Primary URL**:
```
https://lambda.gsfc.nasa.gov/data/map/dr5/dcp/spectra/wmap_tt_spectrum_9yr_v5.txt
```

**Manual Download Page**:
```
https://lambda.gsfc.nasa.gov/product/wmap/dr5/pow_tt_spec_get.html
```

## Download Script

Use the provided downloader script:
```bash
bash tools/data_download/download_wmap_tt.sh
```

## File Format

Expected format (3 columns):
```
# ell    C_ell    sigma_C_ell
2      1234.56  78.90
3      2345.67  89.01
...
```

Units: μK²

## Provenance

After downloading real data, generate a SHA-256 manifest:
```bash
python tools/data_provenance/hash_dataset.py data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt > data/wmap/manifests/sha256.json
```

Validate the manifest:
```bash
python tools/data_provenance/validate_manifest.py data/wmap/manifests/sha256.json
```
