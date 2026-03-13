# Layer2 Fingerprint - UBT Mapping Implementation

**Status**: Implemented (v1.0)  
**Date**: 2026-02-13

## Overview

This implementation wires the Layer2 fingerprint sweep to REAL UBT derivations, replacing placeholder toy formulas with scientifically interpretable predictions.

## Key Components

### 1. Canonical Constants (`forensic_fingerprint/constants.py`)
Single source of truth for observed physical constants from CODATA 2018:
- Fine structure constant inverse: α⁻¹ = 137.035999084(21)
- Electron mass: m_e = 0.51099895000(15) MeV

### 2. UBT Adapters (`forensic_fingerprint/layer2/ubt_adapters.py`)
Adapter functions that wire to existing UBT calculation modules:
- `ubt_alpha_inv()`: Uses `TOOLS/simulations/emergent_alpha_calculator.py`
- `ubt_electron_mass()`: Uses `TOOLS/simulations/validate_electron_mass.py`

**Critical**: These adapters call existing UBT code - NO re-implementation!

### 3. Enhanced Predictors (`forensic_fingerprint/layer2/predictors.py`)
Updated to support:
- `--mapping placeholder`: Toy formulas (framework demo ONLY)
- `--mapping ubt`: Real UBT physics (scientifically valid)

**WARNING**: Placeholder mode MUST carry explicit disclaimers.

### 4. Protocol Document (`forensic_fingerprint/protocols/PROTOCOL_LAYER2_RIGIDITY.md`)
Pre-registered methodology defining:
- Parameter space ranges with physical justifications
- Sampling strategy (random, reproducible seeds)
- Tolerances for hit detection
- Robustness criteria
- Output requirements

### 5. CLI Tool (`forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py`)
Comprehensive command-line interface with:
- `--mapping {placeholder,ubt}` - Physics mapping mode
- `--targets` - Comma-separated target observables
- `--tolerances` - Optional tolerance overrides
- `--range-scale` - Range scaling for perturbation tests
- `--robustness` - Multi-scale robustness analysis
- Automatic WARNING banners for placeholder mode

### 6. Robustness Analysis
Tests parameter space rigidity across range perturbations:
- Scale 0.8: Contracted ranges (-20%)
- Scale 1.0: Baseline ranges
- Scale 1.2: Expanded ranges (+20%)

Generates `VERDICT.md` with:
- Hit-rate and rarity bits for each scale
- Robustness assessment (stable vs. sensitive to boundaries)
- Overall rigidity verdict

### 7. Figure Generation
Automatic diagnostic plots:
- `score_hist.png` - Distribution of combined scores
- `alpha_error_hist.png` - Distribution of alpha errors
- `scatter_winding_vs_alpha_error.png` - Parameter correlations

Uses matplotlib with default colors (no seaborn).

## Usage Examples

### Quick Debug Test (Placeholder)
```bash
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py \
    --space debug \
    --samples 10 \
    --mapping placeholder
```

**Output**: Framework demonstration - NOT scientifically interpretable

### UBT Mode (Scientifically Valid)
```bash
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py \
    --space baseline \
    --samples 5000 \
    --mapping ubt \
    --seed 123
```

**Output**: Real UBT predictions - scientifically interpretable

### Robustness Analysis
```bash
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py \
    --space baseline \
    --samples 1000 \
    --mapping ubt \
    --robustness \
    --seed 123
```

**Output**: VERDICT.md with multi-scale robustness assessment

### Custom Tolerances
```bash
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep_v2.py \
    --space baseline \
    --samples 5000 \
    --mapping ubt \
    --tolerances "alpha_inv=0.1,electron_mass=0.0001"
```

**Output**: Uses tighter tolerances than defaults

## Output Files

Every run produces:

1. **configurations.csv** - All sampled configs with scores
2. **summary.json** - Machine-readable summary
3. **report.md** - Human-readable analysis
4. **VERDICT.md** - Final verdict with robustness
5. **figures/** - Diagnostic plots
   - score_hist.png
   - alpha_error_hist.png
   - scatter_winding_vs_alpha_error.png

## Testing

All features have pytest coverage:

```bash
# Test rarity bits calculation
pytest tests/test_layer2_rarity_bits.py -v

# Test predictors (placeholder vs ubt)
pytest tests/test_layer2_predictors_placeholder_vs_ubt.py -v

# Test CLI outputs
pytest tests/test_layer2_cli_outputs_exist.py -v

# Run all layer2 tests
pytest tests/test_layer2*.py -v
```

All tests PASS ✓

## Protocol Compliance

This implementation follows **Protocol v1.0** as defined in:
`forensic_fingerprint/protocols/PROTOCOL_LAYER2_RIGIDITY.md`

### Key Requirements Met

✓ Mapping mode explicitly documented  
✓ WARNING emitted for placeholder mode  
✓ Parameter ranges pre-registered  
✓ Random sampling with fixed seeds  
✓ Tolerances documented and justified  
✓ All required outputs generated  
✓ Robustness analysis implemented  
✓ VERDICT.md with explicit conclusions  

## Scientific Validity

**CRITICAL**: Only `--mapping ubt` produces scientifically interpretable results.

- ✓ Uses real UBT derivations
- ✓ Wires to existing calculation modules
- ✓ No toy formulas or arbitrary corrections
- ✓ Results can support rigidity claims

**Placeholder mode** is for framework testing ONLY and MUST NOT be used for scientific claims.

## Future Work

### Immediate Next Steps
1. Validate UBT adapters with full UBT calculations
2. Test with larger sample sizes (10k-50k)
3. Compare baseline vs. wide parameter spaces
4. Analyze current UBT configuration ranking

### Potential Enhancements
1. Additional target observables (cosmological parameters)
2. Multi-objective optimization
3. Parameter correlation analysis
4. Null model construction for significance tests
5. Integration with CMB fingerprint tools

## References

- Protocol: `forensic_fingerprint/protocols/PROTOCOL_LAYER2_RIGIDITY.md`
- UBT Alpha: `TOOLS/simulations/emergent_alpha_calculator.py`
- UBT Mass: `TOOLS/simulations/validate_electron_mass.py`
- Constants: `forensic_fingerprint/constants.py`

## License

MIT License  
Copyright (c) 2025 Ing. David Jaroš

---

**Implementation Complete**: 2026-02-13  
**All Tests Passing**: ✓  
**Protocol Compliant**: ✓
