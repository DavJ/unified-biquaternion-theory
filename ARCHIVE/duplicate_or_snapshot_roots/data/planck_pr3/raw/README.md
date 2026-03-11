# Planck PR3 TT Power Spectrum Data

**IMPORTANT**: The files in this directory are MOCK DATA for testing the forensic fingerprint pipeline.

## Real Data Source

The actual Planck PR3 CMB power spectrum data should be downloaded from the Planck Legacy Archive (PLA):

**Website**: https://pla.esac.esa.int/pla/

## Expected Files

- `COM_PowerSpect_CMB-TT-full_R3.01.txt` - Observed TT power spectrum with uncertainties
- `COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt` - Best-fit model spectrum

## File Format

Expected format for observed spectrum (3 columns):
```
# ell    C_ell    sigma_C_ell
2      1234.56  78.90
3      2345.67  89.01
...
```

Expected format for model spectrum (2 columns):
```
# ell    C_ell
2      1234.56
3      2345.67
...
```

Units: μK² (C_ell, not D_ell)

## Provenance

After downloading real data, generate a SHA-256 manifest:
```bash
python tools/data_provenance/hash_dataset.py \
  data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
  data/planck_pr3/raw/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt \
  > data/planck_pr3/manifests/planck_pr3_tt_manifest.json
```

Validate the manifest:
```bash
python tools/data_provenance/validate_manifest.py data/planck_pr3/manifests/planck_pr3_tt_manifest.json
```
