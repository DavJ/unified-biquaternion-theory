# Task: Layer2 Fingerprint Sweep – Hardening (Refactoring Complete)

**Task ID**: layer2_fingerprint_sweep_hardening  
**Status**: ⚠️ Prototype hardening COMPLETE - UBT mapping still PENDING  
**Created**: 2026-02-13  
**Priority**: P0 (Blocking scientific use)  

## Goal
Harden the Layer 2 fingerprint sweep tool to make it scientifically credible by:
1. ✅ Following forensic_fingerprint architecture (modular structure)
2. ✅ Producing interpretable outputs with clear warnings
3. ✅ Separating placeholder physics from real UBT mapping
4. ✅ Being testable and maintainable
5. ❌ **PENDING**: Wire to real UBT mapping for scientific validity

## Completed Work

### Part A - Documentation Fixes ✅
- [x] Updated all documentation with ⚠️ PLACEHOLDER warnings
- [x] Renamed summary file to PROTOTYPE_SUMMARY.md
- [x] Marked all example outputs as TOY MODEL
- [x] Added explicit warnings in README

### Part B - Refactored Architecture ✅  
- [x] Created forensic_fingerprint/layer2/ package
  - [x] __init__.py - Package initialization
  - [x] config_space.py - Layer2Config, ConfigurationSpace with documented parameter status
  - [x] predictors.py - placeholder and ubt modes (ubt raises clear error)
  - [x] metrics.py - Hit-rate, rarity bits (NO p-values!)
  - [x] report.py - CSV, JSON, Markdown output generation
- [x] Created refactored CLI tool: layer2/layer2_sweep.py
- [x] Replaced "p-value" terminology with "hit-rate" and "rarity bits"

### Part C - UBT Mapping Preparation ⚠️ PENDING
- [x] Located existing UBT calculation modules:
  - TOOLS/simulations/emergent_alpha_calculator.py
  - TOOLS/simulations/validate_electron_mass.py
  - tools/planck_validation/mapping.py
- [x] Added clear error message when UBT mode is requested
- [ ] **TODO**: Implement real UBT mapping in predictors.py

### Part D - CLI Improvements ✅
- [x] Refactored CLI to be thin wrapper around modules
- [x] Added --mapping {placeholder,ubt} option
- [x] Added --progress option
- [x] Clear warnings in help text and output
- [ ] **DEFERRED**: --targets, --tolerances, --parallel options (can add later)

## Testing Results

✅ All module components working:
- Configuration space sampling
- Placeholder predictions
- UBT mode error handling
- Hit-rate and rarity bits metrics
- CSV/JSON/MD report generation

✅ CLI tool functional:
- --space {baseline,wide,debug} works
- --samples and --seed work
- --mapping placeholder works (with warnings)
- --mapping ubt fails with helpful error message
- --progress shows incremental updates

## Remaining Work (BLOCKING SCIENTIFIC USE)

### Critical: Implement UBT Mapping Mode

**File**: `forensic_fingerprint/layer2/predictors.py`
**Function**: `_predict_ubt(cfg: Layer2Config)`

**Required implementation**:
1. Import existing UBT calculation functions
2. Map Layer 2 params → UBT input params
3. Call real UBT physics to get predictions
4. Return dictionary with predicted observables

**Example structure**:
```python
def _predict_ubt(cfg: Layer2Config) -> Dict[str, float]:
    # Import real UBT modules
    from TOOLS.simulations.emergent_alpha_calculator import compute_alpha
    from TOOLS.simulations.validate_electron_mass import compute_electron_mass
    
    # Map Layer 2 params to UBT inputs
    alpha_inv = compute_alpha(winding_number=cfg.winding_number, ...)
    electron_mass = compute_electron_mass(...)
    
    return {
        'alpha_inv': alpha_inv,
        'electron_mass': electron_mass,
    }
```

**Notes**:
- Current UBT calculators may not accept Layer 2 params directly
- May need adapter layer to convert Layer 2 → UBT parameters
- Validate against existing UBT test cases

## Usage

### Current (Placeholder Mode)
```bash
# Framework demonstration only - NOT scientifically valid
python3 forensic_fingerprint/layer2/layer2_sweep.py \
    --space baseline --samples 5000 --seed 123 --progress
```

### Future (When UBT Mapping Implemented)
```bash
# Scientifically valid with real UBT physics
python3 forensic_fingerprint/layer2/layer2_sweep.py \
    --space baseline --samples 5000 --seed 123 \
    --mapping ubt --progress
```

## Scientific Status

**Framework**: ✅ Complete and functional
**Physics mapping**: ❌ Placeholder only - BLOCKS scientific use
**Documentation**: ✅ Clear warnings everywhere
**Testability**: ✅ Modular and maintainable

**Bottom line**: Tool is ready for use ONCE UBT mapping is implemented. Until then, all results are framework demonstrations with NO physical meaning.

## Success Criteria

- [x] Modular architecture (layer2 package)
- [x] Clear placeholder warnings
- [x] Hit-rate/rarity terminology (not p-values)
- [x] Functional CLI with helpful errors
- [ ] **PENDING**: Real UBT physics mapping
- [ ] **PENDING**: Scientifically valid results

## Next Steps

1. **Implement UBT mapping** in `_predict_ubt()` function
2. **Validate** against existing UBT test cases
3. **Re-run** all sweeps with real physics
4. **Update** documentation removing placeholder warnings
5. **Publish** results with scientific validity

## Related Files

- `forensic_fingerprint/layer2/` - Modular package (NEW)
- `forensic_fingerprint/layer2/layer2_sweep.py` - Refactored CLI (NEW)
- `forensic_fingerprint/tools/layer2_fingerprint_sweep.py` - Original monolithic tool (OLD)
- `forensic_fingerprint/LAYER2_FINGERPRINT_PROTOTYPE_SUMMARY.md` - Status documentation
- `copilot/tasks/layer2_fingerprint_sweep.md` - Original task spec
