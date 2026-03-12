# Task: Layer 2 Fingerprint Sweep

**Task ID**: layer2_fingerprint_sweep  
**Status**: Implementation  
**Created**: 2026-02-13  
**Priority**: High  

## Goal

Implement a new "fingerprint" module that tests the rigidity of Layer 2 (OFDM-like) by sweeping through the configuration space and evaluating how rare it is to hit observed physical constants without tuning.

## Motivation

CMB heuristics have not yet led to a robust signal. We need a Nobel-credible quantification: how much freedom does Layer 2 have, and how unique is our world within the permitted configurations?

## Requirements

### 1. CLI Tool

Create `forensic_fingerprint/tools/layer2_fingerprint_sweep.py` with the following CLI:

**Arguments:**
- `--space` (string): Configuration space to scan
  - `baseline`: Default parameter ranges
  - `wide`: Broader parameter ranges
  - `debug`: Small sample for testing
- `--samples N` (int): Number of random configurations to sample (default: 5000)
- `--seed SEED` (int): Random seed for reproducibility (default: 123)
- `--outdir` (path): Output directory (default: `scans/layer2/`)

**Example usage:**
```bash
python forensic_fingerprint/tools/layer2_fingerprint_sweep.py \
    --space baseline \
    --samples 5000 \
    --seed 123 \
    --outdir scans/layer2/
```

### 2. Functionality

The tool should:

1. **Define configuration spaces**: Layer 2 parameters to vary
   - RS code parameters (n, k)
   - OFDM channels
   - Prime gating patterns
   - Quantization grids
   - Other discrete Layer 2 choices

2. **Random sampling**: Generate random configurations from the specified space

3. **Physical constants evaluation**: For each configuration, compute:
   - Fine structure constant α
   - Electron mass
   - Other derived observables
   - Distance from experimental values

4. **Statistical analysis**:
   - Compute how many configurations match observations within tolerances
   - Calculate p-values and rarity scores
   - Quantify parameter space volume

5. **Output generation**:
   - CSV file with all sampled configurations and scores
   - JSON summary with statistical metrics
   - Diagnostic plots showing parameter distributions

### 3. Output Structure

```
scans/layer2/
├── layer2_sweep_<timestamp>/
│   ├── configurations.csv       # All sampled configurations
│   ├── summary.json            # Statistical summary
│   ├── results.txt             # Human-readable report
│   └── figures/
│       ├── param_distributions.png
│       ├── score_histogram.png
│       └── best_configs.png
```

## Implementation Notes

- Follow existing tool conventions in `forensic_fingerprint/tools/`
- Use numpy for random sampling
- Include proper error handling and validation
- Add docstrings and comments
- Use MIT license header for code
- Ensure reproducibility with fixed random seeds

## Success Criteria

- [ ] CLI tool implemented and functional
- [ ] All three configuration spaces (baseline, wide, debug) work
- [ ] Generates valid output files
- [ ] Statistical analysis is scientifically sound
- [ ] Code is well-documented
- [ ] Manual testing shows expected behavior

## Related Files

- `docs/architecture/LAYERS.md` - Layer 1 vs Layer 2 definitions
- `tools/planck_validation/constants.py` - Current Layer 2 parameters
- `forensic_fingerprint/tools/` - Other fingerprint tools
- `FITTED_PARAMETERS.md` - Parameter transparency documentation
