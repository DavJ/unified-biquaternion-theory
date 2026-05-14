# Layer 2 Rigidity Experiment - Multi-Scale Stability Test

## Overview

The **Layer 2 Rigidity Experiment** is a reproducible multi-run experiment pipeline designed to assess the stability of Layer 2 parameter space under scaling perturbations.

This tool complements the single-run `layer2_fingerprint_sweep.py` by running multiple sweeps at different parameter range scales to evaluate robustness.

## Purpose

The experiment addresses the question:

> **Is the rigidity assessment robust to the choice of parameter ranges?**

By testing parameter space at three different scales (narrow, baseline, wide), we can determine if the hit-rate and rarity metrics remain stable or if they vary significantly with the sampling range.

## How It Works

### Multi-Scale Sweeps

The experiment runs three independent parameter sweeps:

1. **Narrow (scale = 0.8)**: Parameter ranges contracted by 20%
2. **Baseline (scale = 1.0)**: Standard parameter ranges (unchanged)
3. **Wide (scale = 1.2)**: Parameter ranges expanded by 20%

For each scale, the tool:
- Samples random Layer 2 configurations
- Evaluates match against observed physical constants
- Computes **hit_rate** (fraction of configurations matching observables)
- Computes **rarity_bits** (information-theoretic measure: -log₂(hit_rate))

### Stability Metrics

After running all three sweeps, the experiment computes:

- **max_delta**: Maximum absolute change in rarity_bits from baseline
- **ratio_hit_rate**: Ratio of maximum to minimum hit rates across scales

### Robustness Verdict

The experiment applies the following rule:

```
IF ratio_hit_rate ≤ 3.0 AND max_delta ≤ 2.0 bits:
    VERDICT = STABLE
ELSE:
    VERDICT = UNSTABLE
```

**STABLE** indicates that the rigidity assessment is robust to the parameter range choice.

**UNSTABLE** indicates that the results are sensitive to sampling ranges and further investigation is needed.

## Usage

### Basic Usage

```bash
python3 forensic_fingerprint/tools/layer2_rigidity_experiment.py \
    --samples 5000 \
    --mapping placeholder \
    --seed 123 \
    --space baseline
```

### Command-Line Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--samples` | int | 5000 | Number of samples per scale |
| `--mapping` | str | placeholder | Physics mapping mode (`placeholder` or `ubt`) |
| `--seed` | int | 123 | Random seed for reproducibility |
| `--space` | str | baseline | Configuration space (`baseline`, `wide`, or `debug`) |
| `--outdir` | str | scans/layer2/ | Output directory |

### Examples

#### Quick Debug Run

```bash
python3 forensic_fingerprint/tools/layer2_rigidity_experiment.py \
    --samples 100 \
    --space debug \
    --seed 42
```

#### Production Run

```bash
python3 forensic_fingerprint/tools/layer2_rigidity_experiment.py \
    --samples 10000 \
    --space baseline \
    --seed 12345
```

#### Wide Exploration

```bash
python3 forensic_fingerprint/tools/layer2_rigidity_experiment.py \
    --samples 20000 \
    --space wide \
    --seed 99999
```

## Output Structure

The experiment creates a timestamped directory:

```
scans/layer2/rigidity_experiment_<timestamp>/
├── VERDICT.md                    # Human-readable consolidated verdict
├── stability_metrics.json        # Machine-readable stability metrics
├── scale_0.8/                    # Results for narrow range (−20%)
│   ├── configurations.csv        # All sampled configurations
│   ├── summary.json              # Statistical summary
│   └── results.txt               # Human-readable report
├── scale_1.0/                    # Results for baseline range
│   ├── configurations.csv
│   ├── summary.json
│   └── results.txt
└── scale_1.2/                    # Results for wide range (+20%)
    ├── configurations.csv
    ├── summary.json
    └── results.txt
```

## Output Files

### VERDICT.md

The main output file containing:
- Experiment configuration (samples, seed, space, mapping)
- Results table (hit rate, rarity bits for each scale)
- Stability metrics (max_delta, ratio_hit_rate)
- Robustness verdict (STABLE or UNSTABLE)
- Interpretation and recommendations

### stability_metrics.json

Machine-readable JSON with:
```json
{
  "max_delta": 1.234,
  "ratio_hit_rate": 2.456,
  "verdict": "STABLE",
  "baseline_rarity_bits": 10.5,
  "scales": [0.8, 1.0, 1.2],
  "hit_rates": [0.01, 0.015, 0.012],
  "rarity_bits": [6.64, 6.06, 6.38]
}
```

### Scale-Specific Directories

Each `scale_X.X/` directory contains:
- **configurations.csv**: All sampled configurations with scores
- **summary.json**: Statistical summary for that scale
- **results.txt**: Human-readable report for that scale

## Interpreting Results

### STABLE Verdict

A **STABLE** verdict indicates:
- ✅ Hit rate varies by less than 3× across scales
- ✅ Rarity bits shift by less than 2 bits
- ✅ The rigidity assessment is robust to parameter range choice

**Interpretation**: The parameter space shows consistent rigidity characteristics regardless of how wide or narrow you sample. This suggests the rigidity assessment is trustworthy.

### UNSTABLE Verdict

An **UNSTABLE** verdict indicates:
- ⚠️ Hit rate varies by more than 3× across scales, OR
- ⚠️ Rarity bits shift by more than 2 bits

**Interpretation**: The rigidity assessment is sensitive to the choice of parameter ranges. This could mean:
1. The parameter space has significant edge effects
2. The sampling strategy needs refinement
3. The parameter ranges need better justification

**Action**: Investigate why stability fails. Consider:
- Examining individual scale results
- Running with different `--space` configurations
- Analyzing which parameters drive the instability

## Technical Details

### Range Scaling

The `range_scale` parameter modifies parameter ranges symmetrically around their center:

```python
scaled_range = center ± (width / 2) * range_scale
```

For example, if the baseline winding_number range is [101, 199]:
- Center: 150
- Width: 98
- scale=0.8: [150 - 39, 150 + 39] = [111, 189]
- scale=1.0: [150 - 49, 150 + 49] = [101, 199] (baseline)
- scale=1.2: [150 - 59, 150 + 59] = [91, 209]

### Stability Thresholds

The stability thresholds (3× for hit_rate ratio, 2 bits for max_delta) are design choices based on:
- **3× hit_rate ratio**: Allows moderate variation while flagging extreme changes
- **2 bits max_delta**: Corresponds to 4× change in rarity (2 bits = factor of 4 in probability space)

These thresholds can be adjusted based on empirical experience with the tool.

## Limitations and Warnings

### Placeholder Mapping

⚠️ **IMPORTANT**: The default `--mapping placeholder` mode uses simplified physics mapping.

Results are **NOT scientifically interpretable** until `--mapping ubt` is implemented with proper UBT-to-observables mapping based on first-principles derivations.

The placeholder mode is useful for:
- Testing the infrastructure
- Validating the stability analysis methodology
- Debugging parameter space sampling

### Computational Cost

The experiment runs **three complete sweeps**, so the total runtime is approximately:
```
Total time ≈ 3 × (time for single sweep with N samples)
```

For large sample counts (N > 10,000), consider:
- Using `--space debug` for initial testing
- Running on a machine with sufficient CPU/memory
- Using parallel execution (future enhancement)

## Integration with Existing Tools

### Relationship to layer2_fingerprint_sweep.py

- **layer2_fingerprint_sweep.py**: Single-run parameter space sweep
- **layer2_rigidity_experiment.py**: Multi-scale robustness test

The rigidity experiment is a meta-analysis tool that runs multiple sweeps and evaluates their consistency.

### Integration with Test Suite

The tool is tested in `tests/test_layer2_rigidity_experiment.py`, which validates:
- Help output
- Successful execution
- Output file creation
- VERDICT.md content
- stability_metrics.json structure
- Reproducibility with different seeds

Run tests with:
```bash
python3 tests/test_layer2_rigidity_experiment.py
```

## Future Enhancements

Potential improvements:
1. **Parallel execution**: Run three scales concurrently
2. **More scales**: Test additional intermediate scales (e.g., 0.9, 1.1)
3. **Parameter-specific analysis**: Identify which parameters drive instability
4. **Visualization**: Generate plots of hit_rate vs. scale
5. **Statistical confidence**: Add bootstrap confidence intervals
6. **UBT mapping**: Implement proper physics mapping from UBT theory

## References

- Layer 2 Parameter Space: `forensic_fingerprint/layer2/config_space.py`
- Hit Rate and Rarity Metrics: `forensic_fingerprint/layer2/metrics.py`
- Single Sweep Tool: `forensic_fingerprint/tools/layer2_fingerprint_sweep.py`

## License

MIT License  
Copyright (c) 2025 Ing. David Jaroš

See LICENSE.md for full license text.
