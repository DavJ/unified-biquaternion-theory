# UBT Mathematical Validation Scripts

This directory contains validation scripts that use established mathematical tools (SymPy, NumPy, SciPy) to verify key derivations in the Unified Biquaternion Theory.

## Purpose

All mathematical derivations in UBT must be validated using computational mathematics tools to ensure rigor and reproducibility. These scripts provide:

1. **Symbolic validation** using SymPy for exact mathematical manipulations
2. **Numerical validation** using NumPy/SciPy for parameter fitting and optimization
3. **Verification** that theoretical predictions match experimental values

## Validation Scripts

### 1. Electron Mass Derivation (`validate_electron_mass.py`)

**What it validates:**
- Topological mass formula: `m(n) = A*n^p - B*n*ln(n)`
- Parameter fitting using muon and tau masses
- Electron mass prediction from first principles

**Results:**
```
✓ Electron: 0.5099 MeV (predicted) vs 0.5110 MeV (exp) - 0.22% error
✓ Muon: 105.66 MeV (fitted) - exact match
✓ Tau: 1776.86 MeV (fitted) - exact match
```

**Run:**
```bash
python3 validate_electron_mass.py
```

### 2. Fine Structure Constant (`validate_alpha_constant.py`)

**What it validates:**
- Topological derivation: `α^(-1) = N` where N is winding number
- Value N = 137 from complex time topology
- Quantum corrections explaining experimental value

**Results:**
```
✓ UBT predicts: α^(-1) = 137
✓ Experimental: α^(-1) = 137.036
✓ Agreement: 0.026% error (explained by quantum corrections)
```

**Run:**
```bash
python3 validate_alpha_constant.py
```

### 3. General Relativity Recovery (`validate_GR_recovery.py`)

**What it validates:**
- Metric tensor emergence from Θ field
- Christoffel symbols computation
- Einstein field equations from UBT master equation
- Schwarzschild solution verification

**Results:**
```
✓ Metric g_μν correctly derived from Θ
✓ Einstein equations G_μν = 8πG T_μν recovered
✓ Schwarzschild vacuum solution verified
✓ Minkowski limit correct
✓ Weak field → Newtonian limit
```

**Run:**
```bash
python3 validate_GR_recovery.py
```

### 4. Extended GR Quantization (`validate_extended_GR.py`)

**What it validates:**
- Phase curvature scale r_ψ calculation
- Modified gravitational potential with phase corrections
- Antigravity regime predictions
- Dark energy contribution from phase vacuum
- Gravitational wave dispersion
- Lamb shift corrections
- Dark matter interaction cross-section

**Results:**
```
✓ Phase scale r_ψ ~ 10⁻¹⁴ m (atomic/subatomic)
✓ Antigravity regime at r < r_ψ
✓ Modified potential admits repulsive force
✓ Lamb shift correction ~ 5 MHz (0.45% of measured)
✓ DM cross-section σ ~ 10⁻¹¹⁴ cm² (within experimental reach)
✓ Consistent with QFT (unitarity, causality, energy conservation)
```

**Run:**
```bash
python3 validate_extended_GR.py
```

## Requirements

```bash
pip install sympy numpy scipy
```

Versions tested:
- Python 3.12+
- SymPy 1.14.0
- NumPy 1.26+
- SciPy 1.11+

## Running All Validations

```bash
# Run all validation scripts
for script in validate_*.py; do
    echo "Running $script..."
    python3 "$script" || exit 1
done
echo "All validations passed!"
```

## Validation Philosophy

These scripts follow the requirement that **all mathematical derivations must be confirmed by established tools**. Key principles:

1. **Reproducibility**: Anyone can run these scripts and verify the results
2. **Transparency**: All calculations are explicit and documented
3. **Standards**: Use widely-accepted tools (SymPy, NumPy, not custom code)
4. **Verification**: Compare predictions to experimental data

## Exit Codes

- `0`: Validation successful
- `1`: Validation failed or needs improvement

## Integration with Theory Documents

Each validation script corresponds to specific LaTeX documents:

- `validate_electron_mass.py` → `fermion_mass_derivation_complete.tex`
- `validate_alpha_constant.py` → `alpha_final_derivation.tex`
- `validate_GR_recovery.py` → `quantum_gravity_unification_GR_QFT.tex`

The scripts confirm that the mathematical claims in these documents are correct and can be independently verified.

## Future Validations

Planned additions:
- [ ] Gauge field emergence from biquaternionic symmetries
- [ ] Quantum corrections to graviton propagator
- [ ] Dark matter cross-section calculations
- [ ] CMB anomaly predictions
- [ ] Lamb shift modifications

## Contributing

When adding new theoretical results to UBT:

1. Write the derivation in LaTeX
2. Create a validation script in this directory
3. Ensure the script passes (exit code 0)
4. Document the script in this README

All theoretical claims must be backed by validated computations.

## License

These validation scripts are part of the Unified Biquaternion Theory repository and are licensed under CC BY 4.0.

## Contact

For questions about these validations: jdavid.cz@gmail.com
