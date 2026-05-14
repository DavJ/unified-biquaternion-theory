# UBT Phase-Lock Research Sidecar - Quick Start Guide

## What is This?

This is a **research harness** for systematically testing the UBT phase-lock hypothesis using parameter grids, control experiments, and reproducible workflows. It wraps the existing `forensic_fingerprint/tools/unified_phase_lock_scan.py` tool without modifying it.

## Prerequisites

```bash
pip install numpy healpy matplotlib pyyaml scipy statsmodels
```

## 5-Minute Quick Start

### 1. Run Smoke Test (Synthetic Data)

Test that everything works using synthetic data (no Planck maps needed):

```bash
cd research_phase_lock
python -m pytest tests/test_smoke_synthetic.py -v
```

This should complete in ~30 seconds and verify all components work.

### 2. Preview Parameter Grid

See what the grid runner will do without executing:

```bash
python scripts/run_grid.py --config configs/grid.yaml --dry-run
```

### 3. Run Minimal Grid

Execute a small 2x2 grid for testing:

```bash
python scripts/run_grid.py --config configs/minimal_test.yaml
```

Results will appear in `outputs/` and aggregated summary in `results/grid_summary.csv`.

### 4. View Results

```bash
# Aggregate all results
python scripts/aggregate.py --input-dir outputs --output results/summary.csv

# Create summary plots
python scripts/plot_summary.py --input results/summary.csv --output results/plots/
```

## Key Concepts

### Pre-Registration (Success Thresholds)

All decision rules are declared **before** running experiments in `README.md`:

- **Primary endpoints**: PC_137, PC_139, p_137, p_139, z_137, z_139
- **Primary success**: p_137 ≤ 0.01 AND p_139 ≤ 0.01, PC ≥ 0.50, DeltaPC ≤ 0.10
- **Multiple testing**: BH-FDR correction with q ≤ 0.05
- **Secondary validation**: Survives null models (phase-shuffle, phi-roll)

### Parameter Grid

The grid explores combinations of:
- Window sizes: [64, 96, 128, 192, 256]
- Grid resolutions: nside_out [128, 256, 512]
- Window functions: ["none", "hann"]
- Null models: ["phase-shuffle", "phi-roll"]
- MC samples: [200, 500, 1000]

### Control Experiments

```bash
# Run negative controls (should NOT show phase lock)
python scripts/run_controls.py --type negative

# Run positive controls (synthetic phase-locked data)
python scripts/run_controls.py --type positive
```

### Jacobi Packet Analysis (k=134-143)

Analyze the full Jacobi cluster:

```bash
python scripts/jacobi_packet.py --config configs/grid.yaml
```

### Devil's Advocate Audit

Generate a skeptical report exploring artifact hypotheses:

```bash
python scripts/devil_audit.py --results-dir outputs --output results/audit_report.md
```

## Directory Structure

```
research_phase_lock/
├── QUICKSTART.md          ← You are here
├── README.md              ← Full documentation
├── configs/
│   ├── grid.yaml          ← Main parameter grid
│   ├── controls.yaml      ← Control experiment config
│   └── minimal_test.yaml  ← Small test grid
├── scripts/
│   ├── run_grid.py        ← Main grid runner
│   ├── run_controls.py    ← Control experiments
│   ├── aggregate.py       ← Result aggregation
│   ├── plot_summary.py    ← Visualization
│   ├── jacobi_packet.py   ← Jacobi 134-143 analysis
│   └── devil_audit.py     ← Skeptical audit
├── outputs/               ← Per-run results
├── results/               ← Aggregated summaries
└── tests/                 ← Automated tests
```

## Common Workflows

### Run Full Grid with Planck Data

```bash
# Edit configs/grid.yaml to point to your Planck FITS files
python scripts/run_grid.py --config configs/grid.yaml
```

### Resume Interrupted Grid

```bash
python scripts/run_grid.py --config configs/grid.yaml --resume
```

### Analyze Specific Target k

```bash
# Focus on k=137,139 twin primes
python scripts/run_grid.py --config configs/grid.yaml --targets 137,139
```

### Run Complete Analysis Pipeline

```bash
# 1. Run grid
python scripts/run_grid.py --config configs/grid.yaml

# 2. Run controls
python scripts/run_controls.py --config configs/controls.yaml

# 3. Jacobi packet analysis
python scripts/jacobi_packet.py --config configs/grid.yaml

# 4. Aggregate results
python scripts/aggregate.py --input-dir outputs --output results/summary.csv

# 5. Create plots
python scripts/plot_summary.py --input results/summary.csv --output results/plots/

# 6. Devil's advocate audit
python scripts/devil_audit.py --results-dir outputs --output results/audit_report.md
```

## Reproducibility

Every run is identified by a **deterministic hash** of its configuration:
- Same config → same run ID
- Re-running skips completed runs automatically
- Every output folder contains exact `config.yaml` used

## Troubleshooting

### "healpy not found"
```bash
pip install healpy
```

### "No Planck data"
Use synthetic mode for testing:
```yaml
data:
  mode: "synthetic"
```

### "Out of memory"
Reduce grid parameters:
- Lower `nside_out: [128]`
- Reduce MC samples: `mc: [100]`
- Smaller window sizes: `window_size: [64]`

### "Runs taking too long"
For faster iteration:
- Use `--dry-run` to preview
- Set `max_runs: 10` in config
- Use synthetic data mode
- Reduce MC samples to 50-100

## Next Steps

1. Read full `README.md` for detailed documentation
2. Review `configs/grid.yaml` to understand parameter space
3. Examine success thresholds in README.md § "Success Thresholds"
4. Run tests: `pytest tests/ -v`
5. Start with minimal grid, then scale up

## Getting Help

- Full docs: `README.md`
- Test examples: `tests/test_smoke_synthetic.py`
- Config examples: `configs/*.yaml`

## License

See repository LICENSE.md

## Author

UBT Research Team (implementation of David Jaroš's theoretical framework)
