# Phase-Lock A/B/C/D Verification Research Harness

Self-contained research project for systematic parameter grid experiments using the existing `forensic_fingerprint/tools/unified_phase_lock_scan.py` tool.

**CRITICAL:** This project does NOT modify anything under `forensic_fingerprint/tools/*`. All code lives under `research_phase_lock/` and only wraps/calls the existing tool.

---

## PRE-REGISTRATION: SUCCESS THRESHOLDS AND DECISION RULES

**STATUS:** Pre-registered before large-scale data analysis  
**PURPOSE:** Prevent p-hacking, data dredging, and confirmation bias

### Primary Endpoints

The following metrics define success/failure of the UBT phase-lock hypothesis:

- **PC_137**: Phase coherence at k=137 (twin prime #1)
- **PC_139**: Phase coherence at k=139 (twin prime #2)  
- **p_137**: Monte Carlo p-value at k=137
- **p_139**: Monte Carlo p-value at k=139
- **z_137**: Z-score at k=137
- **z_139**: Z-score at k=139
- **DeltaPC**: Phase difference metric = |PC_137 - PC_139|
- **TwinPrimeScore**: Combined metric = min(z_137, z_139) - λ·DeltaPC (λ=2.0)

### Primary Success Criteria

The hypothesis is considered **SUPPORTED** if ALL of the following hold:

1. **Statistical Significance (Individual)**:
   - p_137 ≤ 0.01 AND p_139 ≤ 0.01

2. **Effect Size (Phase Coherence)**:
   - PC_137 ≥ 0.50 AND PC_139 ≥ 0.50

3. **Twin Prime Consistency**:
   - DeltaPC ≤ 0.10 (both targets show similar coherence)

4. **Multiple Testing Correction**:
   - When grid contains N > 1 configurations, apply Benjamini-Hochberg FDR correction
   - q_137 ≤ 0.05 AND q_139 ≤ 0.05 (FDR-adjusted significance)

### Secondary Validation Criteria

For **ROBUST** support, signal must additionally survive:

5. **Null Model Tests**:
   - Coherence survives phase-shuffle null model (p ≤ 0.01)
   - Coherence survives phi-roll null model (p ≤ 0.01)

6. **Parameter Robustness**:
   - Signal present across multiple window sizes (at least 3 of 5 tested)
   - Signal present across multiple nside_out values (at least 2 of 3 tested)
   - Signal present for both window_func="none" and window_func="hann"

7. **Component Map Consistency** (if Planck data available):
   - Signal present in SMICA component-separated map
   - Signal present in NILC component-separated map
   - Signal present in SEVEM component-separated map

8. **Control Experiments**:
   - Negative controls show NO phase lock (median PC < 0.20, false positive rate ≤ 10%)
   - Positive controls show STRONG phase lock (detection rate ≥ 90%)

### Failure Criteria

The hypothesis is considered **REJECTED** if ANY of:

- Primary success criteria not met (p > 0.01 or PC < 0.50 or DeltaPC > 0.10)
- FDR-corrected q-values exceed 0.05
- Signal vanishes with different windowing or projection
- Signal present at many k values (not specific to 137/139)
- Negative controls show false positives
- Positive controls fail to detect synthetic signals

### Multiple Testing Strategy

Given M grid configurations and K target frequencies:

- **Total tests**: M × K comparisons
- **Correction method**: Benjamini-Hochberg FDR at α=0.05
- **Procedure**:
  1. Collect all p-values from grid runs
  2. Compute q-values via BH procedure
  3. Declare significance only if q ≤ 0.05

### Decision Thresholds Summary

| Metric | Threshold | Direction |
|--------|-----------|-----------|
| p-value (individual) | 0.01 | ≤ |
| q-value (FDR-corrected) | 0.05 | ≤ |
| Phase coherence (PC) | 0.50 | ≥ |
| DeltaPC | 0.10 | ≤ |
| Z-score | 2.58 | ≥ |
| Negative control FPR | 0.10 | ≤ |
| Positive control detection rate | 0.90 | ≥ |

### Reporting Standards

All results will report:
- Raw p-values
- FDR-corrected q-values  
- Effect sizes (PC values)
- Number of tests performed
- Which success criteria were met/failed
- Results from ALL grid configurations (not cherry-picked)

**NO POST-HOC CHANGES** to these thresholds are permitted after running experiments.

---

## Overview

This research harness enables systematic exploration of parameter space for Phase-Lock verification experiments. We test combinations of:

- **Projection types**: torus, lonlat
- **Window functions**: none, hann
- **Window sizes**: 64, 128, 256
- **Grid resolutions**: various nlat/nlon combinations
- **Null models**: phase-shuffle, phi-roll
- **Monte Carlo samples**: 100, 500, ...
- **Target frequencies**: different k-value combinations

The goal is to test A/B/C/D options systematically (no shooting from the hip) and identify which hypothesis paths survive falsification testing.

## Installation

### Prerequisites

- Python 3.7+
- numpy
- healpy (for CMB map handling)
- matplotlib (for plots)
- pyyaml (for config files)

```bash
pip install numpy healpy matplotlib pyyaml
```

### Repository Setup

This harness is already integrated into the repository under `research_phase_lock/`. No additional installation needed.

## Quick Start

### 1. Dry Run (Preview)

See what the grid runner will do without executing:

```bash
python -m research_phase_lock.run_grid \
    --config research_phase_lock/configs/grid_v1.yaml \
    --dry-run
```

### 2. Run Smoke Test

Test with synthetic data (no Planck data required):

```bash
# Run the smoke test
python -m pytest research_phase_lock/tests/test_smoke_synthetic.py -v
```

### 3. Run Full Grid

Execute the full parameter grid (uses synthetic data by default):

```bash
python -m research_phase_lock.run_grid \
    --config research_phase_lock/configs/grid_v1.yaml
```

Results will be saved to `research_phase_lock/results/`.

### 4. Resume Interrupted Grid

If a grid run is interrupted, resume from where it left off:

```bash
python -m research_phase_lock.run_grid \
    --config research_phase_lock/configs/grid_v1.yaml \
    --resume
```

## Configuration

Configuration is done via YAML files. See `configs/grid_v1.yaml` for an example.

### YAML Structure

```yaml
# Global settings
global:
  output_root: "research_phase_lock/results"
  seed: 42
  max_runs: null  # null = unlimited, or set integer to limit

# Data mode
data:
  mode: "synthetic"  # or "planck"
  
  # Planck data (when mode=planck)
  planck:
    tt_map: "path/to/planck_tt.fits"
    q_map: "path/to/planck_q.fits"
    u_map: "path/to/planck_u.fits"
  
  # Synthetic data (when mode=synthetic)
  synthetic:
    nlat: 256
    nlon: 512
    locked_targets: [137, 139]
    noise_sigma: 0.1
    phase_offset_rad: 0.1

# Parameter grid (cartesian product)
grid:
  projection: ["torus", "lonlat"]
  window: ["none", "hann"]
  window_size: [64, 128, 256]
  nside_out: [128, 256]
  nlat: [512]
  nlon: [1024]
  null: ["phase-shuffle", "phi-roll"]
  mc: [100, 500]
  targets: ["137,139", "134,135,136,137,138,139,140,141,142,143"]
```

### Data Modes

#### Synthetic Mode (Default)

Uses synthetic HEALPix maps with embedded coherent signals. No Planck data required. Good for:
- Smoke testing
- Algorithm validation
- Quick parameter exploration

```yaml
data:
  mode: "synthetic"
  synthetic:
    nlat: 256
    nlon: 512
    locked_targets: [137, 139]  # Embed signals at these k
    noise_sigma: 0.1
    phase_offset_rad: 0.1
```

#### Planck Mode

Uses real Planck CMB data. Requires Planck FITS files.

```yaml
data:
  mode: "planck"
  planck:
    tt_map: "data/planck_pr3/COM_CMB_IQU-smica_2048_R3.00_full.fits"
    q_map: "data/planck_pr3/COM_CMB_IQU-smica_2048_R3.00_full.fits"
    u_map: "data/planck_pr3/COM_CMB_IQU-smica_2048_R3.00_full.fits"
```

## Output Structure

Results are organized by run ID (hash of configuration):

```
research_phase_lock/results/
├── run_a1b2c3d4e5f6g7h8/
│   ├── config.yaml                    # Configuration for this run
│   ├── phase_lock_results.csv         # Target results
│   ├── phase_lock_full_spectrum.csv   # Full k-spectrum
│   ├── phase_lock_plot.png            # Diagnostic plot
│   └── synthetic_*.fits               # Synthetic maps (if mode=synthetic)
├── run_x9y8z7w6v5u4t3s2/
│   └── ...
└── grid_summary.csv                   # Aggregated results
```

### Output Files

- **config.yaml**: Parameters used for this run (reproducibility)
- **phase_lock_results.csv**: Phase coherence and statistics for target k values
- **phase_lock_full_spectrum.csv**: Phase coherence for all k (full spectrum)
- **phase_lock_plot.png**: Diagnostic visualization
- **grid_summary.csv**: All runs aggregated into single CSV

## Usage Examples

### Example 1: Small Grid for Testing

Create a minimal config for quick testing:

```yaml
# configs/test_grid.yaml
global:
  output_root: "research_phase_lock/results/test"
  seed: 42
  max_runs: 4

data:
  mode: "synthetic"
  synthetic:
    nlat: 128
    nlon: 256
    locked_targets: [137, 139]
    noise_sigma: 0.1
    phase_offset_rad: 0.1

grid:
  projection: ["torus"]
  window: ["none", "hann"]
  window_size: [64]
  nside_out: [64]
  nlat: [256]
  nlon: [512]
  null: ["phase-shuffle"]
  mc: [100]
  targets: ["137,139"]
```

Run it:

```bash
python -m research_phase_lock.run_grid --config configs/test_grid.yaml
```

### Example 2: Full Exploration with Planck Data

```yaml
# configs/planck_full.yaml
global:
  output_root: "research_phase_lock/results/planck_grid"
  seed: 42

data:
  mode: "planck"
  planck:
    tt_map: "data/planck_smica.fits"
    q_map: "data/planck_smica.fits"
    u_map: "data/planck_smica.fits"

grid:
  projection: ["torus", "lonlat"]
  window: ["none", "hann"]
  window_size: [64, 128, 256]
  nside_out: [128, 256]
  nlat: [512, 1024]
  nlon: [1024, 2048]
  null: ["phase-shuffle", "phi-roll"]
  mc: [500, 1000]
  targets: ["137,139", "134,135,136,137,138,139,140,141,142,143"]
```

## Analysis

### Aggregate Results

Results are automatically aggregated into `grid_summary.csv` after each grid run.

### Find Best Configurations

The grid runner automatically prints:
- Top 5 runs by phase coherence
- Top 5 runs by p-value
- Summary statistics by target k

### Custom Analysis

Use the analysis modules for custom analysis:

```python
from research_phase_lock.analysis.summarize import aggregate_results, find_best_runs
from research_phase_lock.analysis.plots import plot_parameter_sweep

# Load results
results = aggregate_results("research_phase_lock/results")

# Find best runs
best = find_best_runs(results, metric='phase_coherence', n=10)

# Plot parameter sweep
plot_parameter_sweep(
    results,
    param_name='window_size',
    metric='phase_coherence',
    output_path='analysis/window_size_sweep.png'
)
```

## Directory Structure

```
research_phase_lock/
├── README.md              # This file
├── __init__.py
├── run_grid.py            # Main grid runner
├── configs/
│   └── grid_v1.yaml       # Example configuration
├── adapters/
│   ├── __init__.py
│   └── phase_lock_runner.py    # Wrapper for unified_phase_lock_scan
├── analysis/
│   ├── __init__.py
│   ├── summarize.py       # Result aggregation
│   └── plots.py           # Visualization
├── utils/
│   ├── __init__.py
│   ├── hashing.py         # Config hashing for run IDs
│   ├── io.py              # File I/O helpers
│   └── subprocess.py      # Subprocess wrapper
└── tests/
    └── test_smoke_synthetic.py    # Smoke test with synthetic data
```

## Testing

### Smoke Test

Run the smoke test to verify everything works:

```bash
python -m pytest research_phase_lock/tests/test_smoke_synthetic.py -v
```

The smoke test:
- Uses synthetic data (no Planck maps required)
- Tests minimal grid (2-4 configurations)
- Verifies all components work together
- Runs quickly (<1 minute)

### Integration Test

Run a small grid to test the full workflow:

```bash
python -m research_phase_lock.run_grid \
    --config research_phase_lock/configs/grid_v1.yaml \
    --dry-run
```

## Reproducibility

Each run is identified by a hash of its configuration. This ensures:
- **Deterministic run IDs**: Same config → same run ID
- **Automatic deduplication**: Re-running grid skips completed runs
- **Full provenance**: Every result has an exact config.yaml
- **Easy resume**: `--resume` flag skips completed runs

## Troubleshooting

### healpy not found

```bash
pip install healpy
```

### YAML parsing error

Ensure YAML file is valid:

```bash
python -c "import yaml; yaml.safe_load(open('research_phase_lock/configs/grid_v1.yaml'))"
```

### Out of memory

Reduce grid size or use smaller maps:
- Lower `nside_out`
- Lower `nlat`, `nlon`
- Reduce number of MC samples

### Slow execution

For faster testing:
- Use synthetic mode
- Reduce MC samples (e.g., mc: [50])
- Limit grid combinations with `max_runs`
- Use smaller window sizes

## Design Principles

1. **Non-invasive**: Zero modifications to `forensic_fingerprint/tools/*`
2. **Reproducible**: Config hashing ensures deterministic run IDs
3. **Falsifiable**: Systematic grid exploration, not cherry-picking
4. **Resumable**: Can resume interrupted grids
5. **Self-documenting**: Every run saves its exact configuration

## License

See repository LICENSE.md

## Author

UBT Research Team (implementation of David Jaroš's theoretical framework)
