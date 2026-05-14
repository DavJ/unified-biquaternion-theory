# Alpha Computation Paths

## Where is alpha defined/computed?

### Pattern: `alpha.*=.*1/137`

**alpha_core_repro/two_loop_core.py** (line 80)
```
print(f"μ = {mu:7.1f} MeV → α(μ) = {alpha_from_ubt_two_loop_strict(mu):.9f}  (baseline α(1 MeV) = 1/137)")
```

**scripts/torus_theta_alpha_calculator.py** (line 60)
```
ALPHA_EXP = 1/137.035999084  # Experimental value (CODATA 2018)
```

**scripts/alpha_circularity_audit.py** (line 227)
```
r'alpha.*=.*1/137',
```

### Pattern: `alpha.*=.*137`

**validate_alpha_renormalization.py** (line 52)
```
experimental_alpha_inv = 137.035999084  # CODATA 2018 at low energy
```

**tests/test_scheme_independence.py** (line 128)
```
alpha = 1.0 / 137.0  # Fine structure constant
```

**tests/test_electron_mass.py** (line 45)
```
ALPHA_INV_THOMSON_REF = 137.035999  # α⁻¹ at Thomson limit
```

### Pattern: `fine.*structure`

**tests/test_scheme_independence.py** (line 48)
```
Convert fine structure constant α to coupling parameter B.
```

**tests/test_no_hardcoded_constants.py** (line 46)
```
"appendix_A2_geometrical_derivation_of_fine_structure_constant.tex",  # Contains experimental comparison
```

**tests/test_qed_limit.py** (line 43)
```
alpha: Fine structure constant
```

### Pattern: `alpha_inv`

**validate_alpha_renormalization.py** (line 52)
```
experimental_alpha_inv = 137.035999084  # CODATA 2018 at low energy
```

**tests/test_layer2_predictors_placeholder_vs_ubt.py** (line 32)
```
assert 'alpha_inv' in predictions, "Should predict alpha_inv"
```

**tests/test_electron_mass.py** (line 45)
```
ALPHA_INV_THOMSON_REF = 137.035999  # α⁻¹ at Thomson limit
```

### Pattern: `1/137\.03`

**scripts/torus_theta_alpha_calculator.py** (line 60)
```
ALPHA_EXP = 1/137.035999084  # Experimental value (CODATA 2018)
```

**scripts/alpha_circularity_audit.py** (line 380)
```
"- α is defined independently: α = e²/(4πε_0ℏc) ≈ 1/137.036",
```

**scripts/ubt_neutrino_mass_FIXED.py** (line 28)
```
ALPHA = 1/137.036  # Fine structure constant
```

## Alpha Files Summary

- `alpha_core_repro/two_loop_core.py`
- `scripts/alpha_circularity_audit.py`
- `scripts/torus_theta_alpha_calculator.py`
- `scripts/ubt_neutrino_mass_FIXED.py`
- `tests/test_electron_mass.py`
- `tests/test_layer2_predictors_placeholder_vs_ubt.py`
- `tests/test_no_hardcoded_constants.py`
- `tests/test_qed_limit.py`
- `tests/test_scheme_independence.py`
- `validate_alpha_renormalization.py`

## Known Alpha Calculators

### `TOOLS/simulations/emergent_alpha_calculator.py`

  - `4. This gives alpha^{-1} = 137`

### `TOOLS/simulations/torus_theta_alpha_calculator.py`


### `TOOLS/simulations/padic_alpha_calculator.py`


### `original_release_of_ubt/solution_P4_fine_structure_constant/alpha_running_calculator.py`

  - `alpha_inv_bare = 137.0`
