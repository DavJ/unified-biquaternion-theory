# Grid 255 Quantization Test

Test for alignment of cosmological parameters to rational grid m/255.

## Overview

This test checks whether MCMC posterior samples for cosmological parameters show statistically significant clustering near multiples of 1/255, potentially suggesting quantization on a byte-like grid structure.

**Protocol**: See `../PROTOCOL.md` for complete scientific justification.

## Usage

### Basic Usage

```bash
python grid_255.py <chain_file> [param_index] [output_dir]
```

### Arguments

- **chain_file**: MCMC chain file in text format (columns are different parameters)
- **param_index**: Column index of parameter to test (0-based, default: 0)
- **output_dir**: Directory to save results (default: `../out/`)

### Input File Format

Input should be plain text with samples in rows:
```
# Sample format (whitespace or comma delimited)
0.02237  0.1200  1.0409  0.0544  0.9649  3.044
0.02241  0.1198  1.0411  0.0547  0.9652  3.046
...
```

Each column represents a different parameter. Specify which column to test using `param_index`.

### Example

```bash
# Test first parameter (column 0)
python grid_255.py planck_base_plikHM_TTTEEE_lowl_lowE.txt 0 ../out/

# Test Ω_b h² (assuming it's in column 2)
python grid_255.py planck_chains.txt 2 ../out/omega_b/
```

## Output Files

The test generates:

1. **grid_255_[param]_results.txt**: Summary statistics and p-values
2. **grid_255_[param]_null_S1.txt**: Null distribution of S₁ statistic
3. **grid_255_[param]_null_S2.txt**: Null distribution of S₂ statistic
4. **grid_255_[param]_distances.txt**: Distances to nearest grid points
5. **grid_255_[param]_distances.png**: Histogram of distances (if matplotlib available)
6. **grid_255_[param]_null.png**: Null distributions with observed values (if matplotlib available)

## Test Statistics

The test computes two summary statistics:

1. **S₁ = median(d)**: Median distance to nearest grid point
   - Robust to outliers
   - Small values suggest clustering near grid

2. **S₂ = mean(log₁₀ d)**: Mean of logarithmic distances
   - More sensitive to tight clustering
   - Negative values suggest grid alignment

For each statistic, a p-value is computed from Monte Carlo null distribution.

## Interpretation

The test reports one of three outcomes based on **minimum p-value**:

- **Null** (p ≥ 0.01): No significant grid alignment — H0 not rejected
- **Candidate** (0.01 > p ≥ 2.9×10⁻⁷): Candidate signal — **test other parameters**
- **Strong** (p < 2.9×10⁻⁷): Strong signal — **verify with independent MCMC chains**

**Important Notes**:
- Signal should appear in **multiple parameters** to be convincing
- Check that grid alignment is not an artifact of parameter priors
- Verify with chains from different cosmological codes (e.g., CosmoMC vs Cobaya)

## Pre-Registered Parameters

From protocol v1.0:

- **Grid denominator**: 255 (fixed, not tunable)
- **Random seed**: 137
- **MC trials**: 10,000
- **No look-elsewhere correction** (denominator fixed a priori)

## Algorithm

1. For each MCMC sample x, compute:
   ```
   d(x) = min_{m ∈ ℤ} |x - m/255|
   ```
2. Compute observed statistics S₁ and S₂
3. Fit smooth distribution (KDE or Gaussian) to samples
4. Monte Carlo null distribution:
   - Resample from fitted distribution
   - Compute S₁ and S₂ for resampled data
   - Repeat 10,000 times
5. P-values: fraction of null trials with S ≤ observed

## Recommended Parameters to Test

From Planck 2018 baseline chains:

1. **Ω_b h²** (baryon density)
2. **Ω_c h²** (CDM density)
3. **θ_s** (sound horizon angle)
4. **τ** (optical depth)
5. **n_s** (scalar spectral index)
6. **ln(10¹⁰ A_s)** (primordial amplitude)

Test each parameter independently and look for consistency across parameters.

## Dependencies

- **Required**: NumPy
- **Recommended**: SciPy (for KDE fitting)
- **Optional**: Matplotlib (for plots)

Install with:
```bash
pip install numpy scipy matplotlib
```

## Data Sources

### Planck 2018 Chains
Download from Planck Legacy Archive: https://pla.esac.esa.int/

Look for:
- **Base ΛCDM**: `base/plikHM_TTTEEE_lowl_lowE/base_plikHM_TTTEEE_lowl_lowE_*.txt`

Or use GetDist to export chains from CosmoMC/Cobaya runs.

## Reproducibility

To ensure exact reproducibility:
1. Document chain file hash (SHA-256)
2. Record which column corresponds to which parameter
3. Use fixed random seed (hardcoded in script)
4. Record chain length and burn-in removal details

## Notes

- **Grid denominator choice**: 255 = 2⁸ - 1 is pre-registered. Do not change post-hoc.
- **Parameter priors**: Ensure parameter has support covering at least one grid cell [m/255, (m+1)/255]
- **Multiple testing**: When testing N parameters, consider Bonferroni correction (multiply p-value by N)

## References

- **Protocol**: `../PROTOCOL.md`
- **UBT Theory**: See main repository documentation
- **Planck Chains**: Planck Collaboration (2020), A&A 641, A5

## License

MIT License - see repository LICENSE file
