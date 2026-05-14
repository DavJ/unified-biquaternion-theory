# Data Provenance Tools

**Purpose**: Compute and validate SHA-256 hashes for CMB datasets to ensure reproducibility and data integrity.

## Overview

These tools provide cryptographic verification of data files used in UBT forensic fingerprint analysis. By computing and comparing SHA-256 hashes, we ensure:

1. **Reproducibility**: Independent researchers can verify they're using identical datasets
2. **Court-grade provenance**: Cryptographic proof that data hasn't been modified
3. **Error detection**: Detect corrupted downloads or transmission errors

## Tools

### `hash_dataset.py`

Compute SHA-256 hashes for one or more files.

**Usage**:
```bash
python tools/data_provenance/hash_dataset.py <file1> <file2> ... > manifest.json
python tools/data_provenance/hash_dataset.py <file1> --relative-to <dir> > manifest.json
```

**Options**:
- `--relative-to <dir>`: Store file paths relative to the specified directory (default: auto-discovers repository root)

**Example** (Planck PR3):
```bash
cd data/planck_pr3/raw
python ../../../tools/data_provenance/hash_dataset.py *.txt > ../manifests/planck_pr3_tt_manifest.json
```

**Example** (WMAP):
```bash
cd data/wmap/raw
python ../../../tools/data_provenance/hash_dataset.py wmap_tt_*.txt > ../manifests/wmap_tt_manifest.json
```

**Example** (with explicit base directory):
```bash
python tools/data_provenance/hash_dataset.py data/test/*.txt --relative-to . > manifest.json
```

**Output**: JSON manifest with SHA-256 hash for each file

**Note**: By default, the tool auto-discovers the repository root (by searching for `.git`, `pyproject.toml`, or `pytest.ini`) and stores paths relative to it. This ensures manifests work correctly regardless of the current working directory.

### `validate_manifest.py`

Validate files against a previously-generated manifest.

**Usage**:
```bash
python tools/data_provenance/validate_manifest.py <manifest.json>
python tools/data_provenance/validate_manifest.py <manifest.json> --base-dir <dir>
```

**Options**:
- `--base-dir <dir>`: Base directory for resolving relative paths in the manifest (default: auto-discovers repository root)

**Example** (Planck PR3):
```bash
python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/planck_pr3_tt_manifest.json
```

**Example** (WMAP):
```bash
python tools/data_provenance/validate_manifest.py data/wmap/manifests/wmap_tt_manifest.json
```

**Example** (from a subdirectory with explicit base directory):
```bash
cd tools
python data_provenance/validate_manifest.py ../data/planck_pr3/manifests/planck_pr3_tt_manifest.json --base-dir ..
```

**Output**: Success/failure report with details on any hash mismatches

**Exit Codes**:
- `0`: All files validated successfully
- `1`: Validation failed (missing files, hash mismatches, or empty manifest)

**Note**: By default, the tool auto-discovers the repository root and resolves all relative paths in the manifest relative to it. This ensures validation works correctly regardless of the current working directory.

## Standardized Manifest Naming

To ensure consistency across the repository, use these standardized manifest filenames:

| Dataset | Standard Manifest Name | Location |
|---------|------------------------|----------|
| Planck PR3 TT | `planck_pr3_tt_manifest.json` | `data/planck_pr3/manifests/` |
| WMAP TT | `wmap_tt_manifest.json` | `data/wmap/manifests/` |

**Note**: Older documentation may reference `sha256.json` or `manifest.json`. The runner script (`forensic_fingerprint/run_real_data_cmb_comb.py`) automatically falls back to these names if the standard manifest is not found, but new manifests should use the standardized naming above.

## Workflow

### Initial Data Download

1. **Download data**:
   ```bash
   bash tools/data_download/download_planck_pr3_cosmoparams.sh
   bash tools/data_download/download_wmap_tt.sh
   ```

2. **Compute hashes** (Planck):
   ```bash
   cd data/planck_pr3/raw
   python ../../../tools/data_provenance/hash_dataset.py *.txt > ../manifests/planck_pr3_tt_manifest.json
   cd ../../..
   ```

3. **Compute hashes** (WMAP):
   ```bash
   cd data/wmap/raw
   python ../../../tools/data_provenance/hash_dataset.py wmap_tt_*.txt > ../manifests/wmap_tt_manifest.json
   cd ../../..
   ```

4. **Commit manifests** (NOT data files):
   ```bash
   git add data/planck_pr3/manifests/planck_pr3_tt_manifest.json
   git add data/wmap/manifests/wmap_tt_manifest.json
   git commit -m "Add pre-registered data manifests"
   ```

### Validation Before Analysis

Before running any analysis, validate your data matches the pre-registered hashes:

```bash
python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/planck_pr3_tt_manifest.json
python tools/data_provenance/validate_manifest.py data/wmap/manifests/wmap_tt_manifest.json
```

**Critical**: Only proceed with analysis if validation succeeds (all hashes match).

## Manifest Format

Manifests are JSON files with the following structure:

```json
{
  "manifest_version": "1.0",
  "created": "2026-01-10T12:34:56Z",
  "files": {
    "file1.txt": {
      "sha256": "abc123...",
      "size": 12345,
      "path": "relative/path/to/file1.txt"
    },
    "file2.txt": {
      "sha256": "def456...",
      "size": 67890,
      "path": "relative/path/to/file2.txt"
    }
  }
}
```

## Security Notes

- **SHA-256** is a cryptographically secure hash function
- Collision probability is negligible (< 2^-256)
- Hash mismatches indicate:
  - File corruption during download/transfer
  - Wrong version of file
  - Intentional or unintentional modification

## Integration with CMB Runner

The `forensic_fingerprint/run_real_data_cmb_comb.py` script integrates manifest validation:

```bash
python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/spectrum.txt \
    --planck_manifest ../data/planck_pr3/manifests/planck_pr3_tt_manifest.json \
    --wmap_obs ../data/wmap/raw/wmap_spectrum.txt \
    --wmap_manifest ../data/wmap/manifests/wmap_tt_manifest.json
```

**Automatic fallback**: If the specified manifest is not found, the runner automatically tries:
1. Standard manifest name (e.g., `planck_pr3_tt_manifest.json`)
2. `sha256.json` (legacy naming)
3. `manifest.json` (generic fallback)

A warning is printed when using a fallback manifest.

## Related Documentation

- `forensic_fingerprint/RUNBOOK_REAL_DATA.md` - Complete analysis workflow
- `forensic_fingerprint/PROTOCOL.md` - Pre-registered protocol
- `data/planck_pr3/README.md` - Planck data download instructions
- `data/wmap/README.md` - WMAP data download instructions

---

**License**: MIT  
**Author**: UBT Research Team  
**Last Updated**: 2026-01-10
