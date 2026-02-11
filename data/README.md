# UBT Data Directory

**Purpose**: This directory provides scaffolding for real cosmological datasets used in UBT validation.

## Important: No Large Files Committed

**This repository does NOT commit large data files**. Instead, we provide:
- Instructions for downloading datasets
- SHA-256 hashes for verification (provenance)
- Scripts to validate downloaded data

This follows best practices for scientific reproducibility without bloating the repository.

## Directory Structure

```
data/
├── README.md (this file)
├── planck_2018/
│   ├── README.md (download instructions, expected files, SHA-256 hashes)
│   └── .gitignore (ensures data files not committed)
├── wmap_9yr/
│   ├── README.md (download instructions, expected files, SHA-256 hashes)
│   └── .gitignore (ensures data files not committed)
```

## Data Provenance Tools

See `tools/data_provenance/` for:
- `hash_dataset.py` - Compute SHA-256 hashes of downloaded files
- `validate_manifest.py` - Validate files match expected hashes

## Court-Grade Reproducibility

For any published analysis:
1. Download data from official sources (links in subdirectory READMEs)
2. Compute SHA-256 hashes using `hash_dataset.py`
3. Verify hashes match pre-registered values using `validate_manifest.py`
4. Document data version, download date, and hash in analysis report

This ensures third-party reproducibility and prevents data tampering.

## Supported Datasets

### Planck 2018 Legacy Release
- **Location**: `data/planck_2018/`
- **Source**: ESA Planck Legacy Archive
- **Description**: CMB temperature and polarization power spectra, MCMC chains
- **See**: `data/planck_2018/README.md` for details

### WMAP 9-Year Release  
- **Location**: `data/wmap_9yr/`
- **Source**: NASA Lambda Archive
- **Description**: CMB power spectra for independent replication
- **See**: `data/wmap_9yr/README.md` for details

## Usage

### For Analysis
1. Read subdirectory README for download links
2. Download required files to subdirectory
3. Validate using `tools/data_provenance/validate_manifest.py`
4. Proceed with analysis

### For Contribution
If adding a new dataset:
1. Create new subdirectory under `data/`
2. Add README with download instructions
3. Generate SHA-256 manifest using `tools/data_provenance/hash_dataset.py`
4. Add `.gitignore` to prevent committing large files
5. Update this README

## Related Documentation

- `forensic_fingerprint/PROTOCOL.md` - Pre-registered analysis protocol
- `REPO_GOVERNANCE.md` - No post-hoc fitting policy
- `tools/planck_validation/` - Planck 2018 validation implementation

---

**Last Updated**: 2026-01-10  
**Maintained by**: UBT Research Team
