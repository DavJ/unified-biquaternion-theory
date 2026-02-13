# UBT Channel Stability Lab

**Project**: Research sandbox for testing UBT Layer 2 channel selection principles  
**Priority**: Research (Exploratory)  
**Status**: Active Development

## Overview

This isolated laboratory tests UBT Layer 2 channel selection principles (e.g., channels 137, 139) through rigorous statistical analysis. The goal is to evaluate stability criteria objectively without modifying the core UBT repository.

## Key Principles

- **Falsifiability**: All hypotheses must be testable and potentially falsifiable
- **Statistical Rigor**: Apply look-elsewhere correction and null hypothesis testing
- **Reproducibility**: All experiments executable via single CLI commands
- **Blind Protocol**: Pre-declared scan ranges, locked metric definitions
- **Isolation**: Zero modifications to canonical UBT axioms or core repository

## Directory Structure

```
ubt-channel-lab/
├── README.md                    # This file
├── theory/                      # Mathematical definitions
│   ├── stability_definitions.md
│   └── selection_principles.md
├── experiments/                 # Stability criterion implementations
│   ├── spectral_scan.py        # S1: Spectral Robustness
│   ├── twin_prime_scan.py      # S2: Twin Prime Coherence
│   ├── energy_scan.py          # S3: Energy Criterion
│   ├── information_scan.py     # S4: Information Criterion
│   ├── bootstrap_null.py       # Null hypothesis testing
│   └── heatmap_visualization.py
├── analysis/
│   └── results_summary.py      # Aggregate metrics
├── paper/
│   └── draft_channel_selection.tex
├── configs/
│   └── scan_config.yaml        # Experiment parameters
└── results/                     # Generated outputs (not tracked)
```

## Stability Criteria

### S1: Spectral Robustness
Measures peak strength relative to local noise:
```
S1(k) = peak_strength(k) - local_noise(k)
```

### S2: Twin Prime Coherence
Measures combined stability for twin prime pairs:
```
S2(k1, k2) = S1(k1) + S1(k2) + phase_coherence(k1, k2)
```

### S3: Energy Criterion
Energy-based stability via discrete Laplacian:
```
E(k) = ∫ |∇Θ_k|²
```

### S4: Information Criterion
Information-theoretic stability metric:
```
I(k) = mutual_information_stability
```

## Quick Start

### Option A: Run Complete Workflow (Recommended)

The simplest way to run all experiments:

```bash
cd ubt-channel-lab
./run_all_experiments.sh
```

This automated script will:
1. Run all four stability criteria (S1-S4)
2. Perform bootstrap null testing
3. Generate visualizations
4. Aggregate results into final ranking

**See `QUICKSTART.md` for detailed instructions.**

### Option B: Run Individual Experiments

#### 1. Configure Experiment
Edit `configs/scan_config.yaml` to set scan range and parameters:
```yaml
scan_range:
  min: 100
  max: 200
```

#### 2. Run Stability Scans
```bash
# S1: Spectral robustness
python experiments/spectral_scan.py --config configs/scan_config.yaml

# S2: Twin prime coherence
python experiments/twin_prime_scan.py --config configs/scan_config.yaml

# S3: Energy criterion
python experiments/energy_scan.py --config configs/scan_config.yaml

# S4: Information criterion
python experiments/information_scan.py --config configs/scan_config.yaml
```

#### 3. Bootstrap Null Testing
```bash
python experiments/bootstrap_null.py --config configs/scan_config.yaml --n-bootstrap 10000
```

#### 4. Generate Visualizations
```bash
python experiments/heatmap_visualization.py --config configs/scan_config.yaml
```

#### 5. Aggregate Results
```bash
python analysis/results_summary.py --config configs/scan_config.yaml
```

## Statistical Controls

- **Look-Elsewhere Correction**: Applied to account for multiple testing
- **Bootstrap Null Model**: Monte Carlo shuffling to establish baseline
- **P-Value Reporting**: All rankings include statistical significance
- **Pre-Registration**: Scan ranges and metrics locked before execution

## Expected Outputs

- `results/s1_ranking.csv` - Spectral robustness rankings
- `results/s2_heatmap.png` - Twin prime coherence matrix
- `results/s3_energy.csv` - Energy criterion results
- `results/s4_information.csv` - Information criterion results
- `results/null_distributions.png` - Bootstrap null distributions
- `results/combined_ranking.csv` - Unified stability ranking
- `results/significance_report.txt` - Statistical summary

## Research Goals

1. **Objective Evaluation**: Test whether channel 137 emerges naturally from stability criteria
2. **Twin Prime Hypothesis**: Evaluate twin prime pairs (e.g., 137-139) for enhanced coherence
3. **Null Model Validation**: Confirm that stable channels are not statistical flukes
4. **Structural Validation**: Test whether UBT Layer 2 channel selection is falsifiable

## Important Notes

⚠️ **This lab is exploratory and must not bias toward confirming 137.**  
⚠️ **Results may confirm, weaken, or invalidate the Layer 2 channel hypothesis.**  
⚠️ **Purpose is falsifiability and structural validation, not confirmation bias.**

## Dependencies

```bash
pip install numpy scipy matplotlib pandas pyyaml seaborn
```

## License

See main repository LICENSE for terms.

## Contact

For questions about UBT theory, see main repository documentation.
