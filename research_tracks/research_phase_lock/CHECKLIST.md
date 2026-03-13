# UBT Phase-Lock Research Sidecar - Implementation Checklist

## Required Components (from problem statement)

### Directory Structure
- [x] `research_phase_lock/README.md` (enhanced with pre-registration)
- [x] `research_phase_lock/QUICKSTART.md`
- [x] `research_phase_lock/config/` directory
  - [x] `grid.yaml` (enhanced master config)
  - [x] `controls.yaml` (control experiments)
- [x] `research_phase_lock/scripts/` directory
  - [x] `run_grid.py` (wrapper for main runner)
  - [x] `run_controls.py` (control experiments)
  - [x] `aggregate.py` (result aggregation)
  - [x] `plot_summary.py` (visualizations)
  - [x] `jacobi_packet.py` (Jacobi 134-143 analysis)
  - [x] `devil_audit.py` (skeptical audit)
- [x] `research_phase_lock/outputs/` directory with `.gitkeep`
- [x] `research_phase_lock/results/` directory with `.gitkeep`
- [x] `research_phase_lock/tests/` directory
  - [x] `test_configs_load.py`
  - [x] `test_aggregate_smoke.py`

### Pre-Registration (Success Thresholds)
- [x] Defined in README.md (at top, before everything)
- [x] Also implemented in config/grid.yaml
- [x] Primary endpoints: PC_137, PC_139, p_137, p_139, z_137, z_139
- [x] DeltaPC = |PC_137 - PC_139|
- [x] TwinPrimeScore = min(z_137, z_139) - λ·DeltaPC
- [x] Primary success: p ≤ 0.01 AND PC ≥ 0.50 AND DeltaPC ≤ 0.10
- [x] FDR correction: BH q ≤ 0.05
- [x] Secondary validation criteria
- [x] Failure criteria

### Parameter Grid Runner (run_grid.py)
- [x] YAML config input
- [x] Cartesian product of parameters
- [x] Calls unified_phase_lock_scan via subprocess
- [x] Per-run output folders with unique IDs
- [x] Config storage for each run
- [x] Result aggregation
- [x] Resume capability
- [x] Dry-run mode

### Parameter Grid Configuration (grid.yaml)
- [x] Map paths (TT, Q, U)
- [x] Targets: [137,139] and [134-143]
- [x] Projection: ["torus"]
- [x] window_size: [64, 96, 128, 192, 256]
- [x] nside_out: [128, 256, 512]
- [x] nlat/nlon pairs
- [x] window_func: ["none", "hann"]
- [x] null_models: ["phase-shuffle", "phi-roll"]
- [x] mc_samples: [200, 500, 1000]
- [x] seeds: [0, 1, 2]
- [x] max_workers for parallel runs

### Control Experiments (run_controls.py)
- [x] Negative controls (should NOT show phase lock)
  - [x] Pure noise
  - [x] Random phases
  - [x] Wrong targets
  - [x] Scrambled data
- [x] Positive controls (should DEFINITELY show phase lock)
  - [x] Perfect lock
  - [x] Strong lock with noise
  - [x] Weak lock
  - [x] Full Jacobi packet
- [x] Synthetic data generation
- [x] Control validation criteria

### Result Aggregation (aggregate.py)
- [x] Scans output directories
- [x] Parses all CSVs
- [x] Combines into summary.csv
- [x] BH-FDR correction implementation
- [x] Q-values computed
- [x] Summary statistics
- [x] Multiple testing handling

### Visualization (plot_summary.py)
- [x] Phase coherence distributions
- [x] P-value histograms
- [x] Parameter sweep plots
- [x] Twin prime comparison
- [x] Supports PNG/PDF/SVG

### Jacobi Packet Analysis (jacobi_packet.py)
- [x] Analyzes k=134-143
- [x] Individual k profiles
- [x] Cluster-wide patterns
- [x] Spectrum visualization
- [x] Statistical significance

### Devil's Advocate Audit (devil_audit.py)
- [x] Statistical artifacts analysis
- [x] Instrumental systematics
- [x] Analysis pipeline artifacts
- [x] Foreground contamination
- [x] Spurious correlations
- [x] Overall verdict section
- [x] Markdown report output

### Code Quality
- [x] All Python code has explanatory comments
- [x] Docstrings for all functions
- [x] CLI interfaces for all scripts
- [x] Error handling
- [x] Valid Python syntax (tested)

### Reproducibility
- [x] Fixed seeds everywhere
- [x] Config hashing for run IDs
- [x] Stored configs per run
- [x] Version stamping
- [x] Git provenance tracking

### Testing
- [x] Config loading tests
- [x] Aggregation smoke tests
- [x] All tests documented

### Documentation
- [x] README.md with pre-registration
- [x] QUICKSTART.md
- [x] IMPLEMENTATION_SUMMARY.md
- [x] Inline code comments
- [x] Usage examples

## Constraints Satisfied
- [x] NO modifications to forensic_fingerprint/tools/*
- [x] All code under research_phase_lock/
- [x] Easy to re-run from CLI
- [x] Reproducible outputs

## Status: ✅ COMPLETE

All requirements from the problem statement have been implemented.
The research sidecar is ready for testing with dependencies installed.
