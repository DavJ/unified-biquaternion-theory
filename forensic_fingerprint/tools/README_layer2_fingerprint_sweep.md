# Layer 2 Fingerprint Sweep Tool

## Overview

The Layer 2 Fingerprint Sweep tool tests the rigidity of UBT's Layer 2 parameters (OFDM-like coding/modulation) by sweeping through the configuration space and evaluating how rare it is to hit observed physical constants without fine-tuning.

## Purpose

**Motivation**: CMB heuristics have not yet led to a robust signal. We need Nobel-credible quantification: how much freedom does Layer 2 have, and how unique is our world within the permitted configurations?

The tool answers questions like:
- How many Layer 2 configurations match observed physics?
- How rare is the current UBT configuration?
- What is the parameter space volume?
- How constrained is Layer 2 compared to Layer 1?

## Usage

### Basic Usage

```bash
# Quick debug test (50 samples, takes ~1 second)
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \
    --space debug \
    --samples 50

# Standard baseline sweep (5000 samples, takes ~30 seconds)
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \
    --space baseline \
    --samples 5000 \
    --seed 123

# Wide parameter exploration (10000 samples)
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \
    --space wide \
    --samples 10000 \
    --seed 456

# Custom output directory
python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \
    --space baseline \
    --samples 5000 \
    --outdir custom_output/
```

### Command-Line Options

- `--space {baseline,wide,debug}`: Configuration space to scan
  - **baseline**: Standard parameter ranges around current UBT values
  - **wide**: Broader ranges for wider exploration  
  - **debug**: Small range for quick testing
  
- `--samples N`: Number of random configurations to sample (default: 5000)
  
- `--seed SEED`: Random seed for reproducibility (default: 123)
  
- `--outdir PATH`: Output directory (default: `scans/layer2/`)

### Configuration Spaces

#### Debug Space
- Quick testing with narrow ranges
- RS code length: 250-260
- OFDM channels: 12-20
- Winding numbers: 130-145
- ~50-100 samples recommended

#### Baseline Space
- Standard ranges around current values
- RS code length: 200-300
- OFDM channels: 8-32
- Winding numbers: 101-199 (primes only)
- ~5000 samples recommended

#### Wide Space
- Broad exploration of parameter space
- RS code length: 100-500
- OFDM channels: 4-64
- Winding numbers: 50-250
- ~10000 samples recommended

## Output

Results are saved to a timestamped directory:

```
scans/layer2/layer2_sweep_YYYYMMDD_HHMMSS/
├── configurations.csv       # All sampled configurations with scores
├── summary.json            # Statistical summary (machine-readable)
├── results.txt             # Human-readable report
└── figures/                # (Future: visualization plots)
```

### configurations.csv

Contains all sampled configurations with columns:
- `rs_n`, `rs_k`: Reed-Solomon code parameters
- `ofdm_channels`: Number of OFDM channels
- `winding_number`: Topological winding number
- `prime_gate_pattern`: Prime gating pattern index
- `quantization_grid`: Quantization grid size
- `alpha_inv_predicted`: Predicted fine structure constant inverse
- `electron_mass_predicted`: Predicted electron mass (MeV)
- `alpha_error`: Absolute error in alpha
- `electron_mass_error`: Absolute error in electron mass
- `combined_score`: Overall goodness metric (lower is better)

### summary.json

Machine-readable summary with:
- Best configuration found
- Statistical metrics (mean, median, std dev)
- Match statistics (how many configs within tolerance)
- Current UBT configuration ranking

### results.txt

Human-readable report with:
- Best configuration details
- Statistical summary
- Match statistics
- Current configuration analysis
- Interpretation (rigidity assessment)

## Interpretation

### Rigidity Assessment

The tool provides a rigidity assessment based on how many configurations match both observables:

- **High rigidity** (<1% match): Matching configurations are rare
  - Suggests Layer 2 is highly constrained
  - Current config may be special/optimized
  
- **Moderate rigidity** (1-5% match): Matching configurations are uncommon
  - Some freedom in Layer 2 choices
  - Multiple viable configurations exist
  
- **Low rigidity** (≥5% match): Matching configurations are common
  - Layer 2 has significant freedom
  - Current config is not uniquely determined

### Current Configuration Ranking

The tool evaluates where the current UBT configuration (RS(255,200), OFDM=16, n=137) ranks among sampled configurations:

- **Top 1%**: Highly optimized - current config is exceptional
- **Top 10%**: Well optimized - current config is good but not unique
- **Above median**: Moderately optimized - better configs exist
- **Below median**: May need reconsideration

## Physical Model

**Important**: The current implementation uses a **simplified** Layer 2 → observables mapping. In the full UBT theory, deriving physical constants from Layer 2 parameters requires detailed calculations.

Current model:
- α⁻¹ ≈ winding_number + corrections(RS, OFDM, grid)
- m_e ≈ base_mass + corrections(RS_k/RS_n ratio)

This is a placeholder. Future versions should use the full UBT derivations from:
- `tools/planck_validation/mapping.py`
- `TOOLS/simulations/emergent_alpha_calculator.py`
- `TOOLS/simulations/validate_electron_mass.py`

## Examples

### Example 1: Quick Test

```bash
$ python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \
    --space debug --samples 50

Layer 2 Fingerprint Sweep
================================================================================
Configuration space: debug
Number of samples: 50
...
================================================================================
KEY RESULTS:
================================================================================
Best score found: 0.061839
Current config rank: 0/50 (0.00%)
Configs matching both observables: 5 (10.00%)

RIGIDITY ASSESSMENT: Low rigidity - matching configurations are common (≥5%)
```

### Example 2: Baseline Production Run

```bash
$ python3 forensic_fingerprint/tools/layer2_fingerprint_sweep.py \
    --space baseline --samples 5000 --seed 123

Layer 2 Fingerprint Sweep
================================================================================
Configuration space: baseline
Number of samples: 5000
...
Configs matching both observables: 23 (0.46%)

RIGIDITY ASSESSMENT: High rigidity - matching configurations are rare (<1%)
```

## Next Steps

After running sweeps:

1. **Analyze CSV**: Look for patterns in successful configurations
   - Do certain RS parameters cluster?
   - Is winding number always near 137?
   - Are OFDM channels constrained?

2. **Compare spaces**: Run all three spaces and compare
   - Does rigidity change with parameter range?
   - Are there multiple "islands" of good configs?

3. **Refine model**: Improve the Layer 2 → observables mapping
   - Use full UBT calculations
   - Add more physical constants (quark masses, etc.)

4. **Statistical tests**: Compute p-values
   - Is current config statistically special?
   - What are confidence intervals?

## License

MIT License  
Copyright (c) 2025 Ing. David Jaroš

See LICENSE file in repository root for full license text.

## Related Documentation

- `copilot/tasks/layer2_fingerprint_sweep.md` - Task specification
- `docs/architecture/LAYERS.md` - Layer 1 vs Layer 2 definitions
- `FITTED_PARAMETERS.md` - Current parameter values and status
- `tools/planck_validation/constants.py` - Locked Layer 2 constants
