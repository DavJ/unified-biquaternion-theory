# CMB Comb Test

Test for periodic "comb" signatures in CMB power spectrum residuals.

## Overview

This test searches for sinusoidal oscillations in the CMB power spectrum residuals (observed - ΛCDM model) that could indicate discrete spacetime architecture. The test is fully pre-registered with fixed candidate periods and significance thresholds.

**Protocol**: See `../PROTOCOL.md` for complete scientific justification.

## Usage

### Basic Usage

```bash
python cmb_comb.py <obs_file> <model_file> [output_dir]
```

### Input File Format

Input files should be plain text with three columns:
```
# ell  C_ell  sigma_ell
2      1200.5  50.2
3      1150.3  48.7
...
```

- **obs_file**: Observed CMB power spectrum (ℓ, C_ℓ^obs, σ_ℓ)
- **model_file**: ΛCDM model prediction (ℓ, C_ℓ^model) — must have same ℓ range
- **output_dir**: Directory to save results (default: `../out/`)

### Example

```bash
# Using synthetic test data
python cmb_comb.py test_obs.txt test_model.txt ../out/

# Using Planck data (after downloading)
python cmb_comb.py planck_2018_TT.txt lcdm_bestfit.txt ../out/planck_tt/
```

## Output Files

The test generates:

1. **cmb_comb_results.txt**: Summary statistics (period, amplitude, phase, p-value)
2. **null_distribution.txt**: Monte Carlo null distribution of max(Δχ²)
3. **residuals_and_fit.txt**: Residuals and fitted sinusoid values
4. **residuals_with_fit.png**: Plot of residuals with best-fit sinusoid (if matplotlib available)
5. **null_distribution.png**: Histogram of null distribution (if matplotlib available)

## Interpretation

The test reports one of three outcomes:

- **Null** (p ≥ 0.01): No significant signal — H0 not rejected
- **Candidate** (0.01 > p ≥ 2.9×10⁻⁷): Candidate signal — **replication required**
- **Strong** (p < 2.9×10⁻⁷): Strong signal (~5σ) — **immediate independent verification needed**

**Important**: A "candidate" or "strong" result is **not** a discovery claim. It requires:
1. Replication in independent dataset (e.g., WMAP, Planck TE/EE)
2. Consistency check across different frequency maps
3. Verification that signal is not instrumental artifact

## Pre-Registered Parameters

From protocol v1.0:

- **Candidate periods**: Δℓ ∈ {8, 16, 32, 64, 128, 255}
- **Random seed**: 42 (fixed for reproducibility)
- **MC trials**: 10,000
- **Look-elsewhere correction**: Max statistic method

## Algorithm

1. Compute normalized residuals: r_ℓ = (C_ℓ^obs - C_ℓ^model) / σ_ℓ
2. For each candidate period Δℓ:
   - Fit sinusoid: r_ℓ ≈ A sin(2πℓ/Δℓ + φ)
   - Compute Δχ² = χ²(no sinusoid) - χ²(with sinusoid)
3. Select best period: max(Δχ²) across all candidates
4. Monte Carlo null distribution:
   - Generate 10,000 synthetic Gaussian residuals
   - Compute max(Δχ²) for each trial
5. P-value: fraction of null trials with max(Δχ²) ≥ observed

## Dependencies

- **Required**: NumPy
- **Optional**: Matplotlib (for plots)

Install with:
```bash
pip install numpy matplotlib
```

## Data Sources

### Planck 2018
Download from Planck Legacy Archive: https://pla.esac.esa.int/

Recommended files:
- **TT spectrum**: `COM_PowerSpect_CMB-TT-full_R3.01.txt`
- **TE spectrum**: `COM_PowerSpect_CMB-TE-full_R3.01.txt`
- **EE spectrum**: `COM_PowerSpect_CMB-EE-full_R3.01.txt`

### WMAP 9-Year
Download from LAMBDA: https://lambda.gsfc.nasa.gov/

For model predictions, use CAMB or CLASS to generate ΛCDM best-fit.

## Reproducibility

To ensure exact reproducibility:
1. Document dataset hashes (SHA-256)
2. Use fixed random seed (hardcoded in script)
3. Record code version (Git commit hash)
4. Archive all outputs with timestamps

See protocol for full reproducibility requirements.

## References

- **Protocol**: `../PROTOCOL.md`
- **UBT Theory**: See main repository documentation
- **Planck 2018**: Planck Collaboration (2020), A&A 641, A6

## License

MIT License - see repository LICENSE file
