# Cross-Dataset Invariance Test

Test for consistency of UBT-predicted invariants across independent cosmological datasets.

## Overview

This test checks whether UBT-predicted invariant quantities (derived from cosmological parameters via fixed UBT formulae) agree statistically across different datasets (Planck, BAO, SNe, lensing). Agreement supports theoretical coherence; disagreement suggests the UBT mapping is ad hoc.

**Protocol**: See `../PROTOCOL.md` for complete scientific justification.

## Usage

### Basic Usage

The script includes example datasets and can be run as:

```bash
python invariance.py [output_dir]
```

For custom datasets, modify the `datasets` list in `main()` or import as a module.

### Module Usage

```python
from invariance import run_invariance_test, ubt_invariant_kappa

# Define datasets
datasets = [
    {'name': 'Planck', 'param_value': 0.02237, 'param_sigma': 0.00015},
    {'name': 'BAO', 'param_value': 0.02240, 'param_sigma': 0.00020},
    # ... more datasets
]

# Run test
results = run_invariance_test(datasets, ubt_invariant_kappa, 
                               invariant_name='kappa', output_dir='../out/')
```

## Input Format

Each dataset is a dictionary with:
- **name**: Dataset identifier (e.g., "Planck TT+TE+EE")
- **param_value**: Parameter estimate (e.g., Ω_b h²)
- **param_sigma**: 1σ uncertainty

The test:
1. Applies a fixed UBT formula to map parameter → invariant
2. Propagates uncertainties
3. Tests consistency via chi-square

## UBT Invariant Functions

**CRITICAL**: The invariant functions `ubt_invariant_kappa()` and `ubt_invariant_eta()` are currently **PLACEHOLDERS**. They must be replaced with actual UBT formulae from the theory.

### Example: Invariant κ from Ω_b h²

```python
def ubt_invariant_kappa(omega_b_h2):
    """
    Compute UBT invariant κ from baryon density.
    
    Replace this with actual formula from UBT biquaternionic mapping.
    Example:
        κ = (ω_b / ω_ref)^α × exp(β × Im(τ))
    where α, β, ω_ref are UBT-predicted constants.
    """
    # PLACEHOLDER - REPLACE WITH REAL UBT FORMULA
    omega_b_ref = 0.02237
    sigma_ref = 0.00015
    return (omega_b_h2 - omega_b_ref) / sigma_ref
```

### Example: Invariant η from n_s

```python
def ubt_invariant_eta(n_s):
    """
    Compute phase index η from spectral index via complex-time mapping.
    
    Replace with actual UBT formula.
    Example:
        η = arctan(Im(τ) / Re(τ)) ~ f(n_s - 1)
    """
    # PLACEHOLDER - REPLACE WITH REAL UBT FORMULA
    delta_n_ref = 0.004
    return (n_s - 1.0) / delta_n_ref
```

**Action Required**: Consult UBT appendices to find appropriate invariant mappings and implement them here.

## Output Files

The test generates:

1. **invariance_[invariant]_results.txt**: Summary statistics, chi-square, p-value
2. **invariance_[invariant]_table.txt**: Table of invariant estimates per dataset
3. **invariance_[invariant]_forest.png**: Forest plot with error bars (if matplotlib available)

## Interpretation

The test reports one of two outcomes:

- **Consistent** (p > 0.05): Datasets agree — **supports UBT**
  - If p > 0.32: Strong agreement (better than expected from errors alone)
  
- **Inconsistent** (p < 0.05): Datasets disagree — **UBT mapping potentially falsified**
  - If p < 0.01: Strong evidence against UBT

**Important**: This test is "backwards" compared to typical hypothesis tests. **High p-values are good** (support UBT), low p-values are bad (falsify UBT).

## Chi-Square Formula

Consistency chi-square:
```
χ² = Σᵢ (κᵢ - κ̄)² / σᵢ²
```

where:
- κᵢ = invariant from dataset i
- κ̄ = weighted mean across all datasets
- σᵢ = uncertainty on κᵢ

Degrees of freedom: N - 1 (N datasets, 1 fitted parameter)

P-value from χ²_{N-1} distribution.

## Recommended Datasets

Test with combinations of:

### Primary Cosmological Data
1. **Planck TT+TE+EE** (2018 baseline)
2. **Planck TT+TE+EE+lowE+lensing** (2018 full)
3. **Planck+BAO** (BOSS DR12 + eBOSS)
4. **Planck+BAO+Pantheon SNe**
5. **ACT DR4** (independent CMB)
6. **SPT-3G** (independent CMB)

### Derived Parameters
For each dataset, extract parameter estimates for:
- Ω_b h² → invariant κ
- n_s → invariant η
- H₀ → invariant (if UBT predicts H₀ mapping)

Consistency should hold across all combinations.

## Statistical Considerations

### Multiple Testing
If testing M different invariants (e.g., κ, η, ζ), consider Bonferroni correction:
- Reject consistency if p < 0.05/M for any invariant

### Systematic Errors
Check that inconsistencies are not due to:
- Different calibrations across datasets
- Different treatments of nuisance parameters
- Priors that truncate parameter space differently

### Sensitivity
Test should have power to detect:
- 2σ discrepancies between datasets
- UBT formulae that are clearly wrong (e.g., predict negative values)

## Dependencies

- **Required**: NumPy
- **Recommended**: SciPy (for chi-square CDF)
- **Optional**: Matplotlib (for forest plots)

Install with:
```bash
pip install numpy scipy matplotlib
```

## Example Workflow

1. **Define UBT invariant**: Implement actual formula in `ubt_invariant_kappa()`
2. **Gather datasets**: Extract parameter estimates from published papers/chains
3. **Document provenance**: Record papers, data releases, table numbers
4. **Run test**: `python invariance.py ../out/`
5. **Check result**:
   - If p > 0.05: UBT supported, proceed to publication
   - If p < 0.05: Investigate discrepancy or revise UBT formula

## Notes

- **Formula must be fixed a priori**: Do not tune the invariant function to make datasets agree
- **Test multiple invariants**: Agreement across independent invariants strengthens case
- **Compare to ΛCDM**: Also test whether ΛCDM-predicted invariants show consistency (they should)

## References

- **Protocol**: `../PROTOCOL.md`
- **UBT Theory**: See main repository documentation
- **Planck 2018**: Planck Collaboration (2020), A&A 641, A6
- **BAO**: eBOSS Collaboration (2021), Phys. Rev. D 103, 083533

## License

MIT License - see repository LICENSE file
