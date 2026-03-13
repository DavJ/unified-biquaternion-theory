# Research Phase-Lock Sidecar - Implementation Summary

**Date:** 2026-02-14  
**Author:** UBT Research Team  
**Status:** Complete and Ready for Testing

## Overview

This implementation provides a complete research harness for systematic UBT phase-lock hypothesis testing. All components are implemented as a **non-invasive sidecar** that wraps the existing `forensic_fingerprint/tools/unified_phase_lock_scan.py` without modifying it.

## What Was Implemented

### 1. Directory Structure ✓

```
research_phase_lock/
├── README.md                    # Full documentation with pre-registration
├── QUICKSTART.md                # Quick start guide (NEW)
├── configs/
│   ├── grid.yaml                # Main parameter grid config (ENHANCED)
│   ├── controls.yaml            # Control experiments config (NEW)
│   ├── grid_v1.yaml             # Original config (existing)
│   ├── minimal_test.yaml        # Test config (existing)
│   └── test_grid.yaml           # Test config (existing)
├── scripts/                     # NEW DIRECTORY
│   ├── run_grid.py              # Grid runner wrapper
│   ├── run_controls.py          # Control experiments runner
│   ├── aggregate.py             # Result aggregation with FDR
│   ├── plot_summary.py          # Summary plots and visualizations
│   ├── jacobi_packet.py         # Jacobi cluster (k=134-143) analysis
│   └── devil_audit.py           # Devil's advocate audit report
├── outputs/                     # NEW DIRECTORY (with .gitkeep)
├── results/                     # NEW DIRECTORY (with .gitkeep)
├── tests/
│   ├── test_smoke_synthetic.py  # Existing smoke test
│   ├── test_configs_load.py     # Config loading tests (NEW)
│   └── test_aggregate_smoke.py  # Aggregation tests (NEW)
├── adapters/                    # Existing
├── analysis/                    # Existing
└── utils/                       # Existing
```

### 2. Configuration Files ✓

#### `configs/grid.yaml` (Enhanced)
- Complete parameter grid specification
- Pre-registered success thresholds
- Data modes: synthetic and Planck
- Comprehensive parameter combinations:
  - window_size: [64, 96, 128, 192, 256]
  - nside_out: [128, 256, 512]
  - window_func: ["none", "hann"]
  - null_models: ["phase-shuffle", "phi-roll"]
  - mc_samples: [200, 500, 1000]
  - targets: twin primes and full Jacobi packet

#### `configs/controls.yaml` (New)
- **Negative controls** (4 types):
  - Pure noise (uncorrelated channels)
  - Random phases
  - Wrong targets (k≠137,139)
  - Scrambled Planck data
  
- **Positive controls** (4 types):
  - Perfect phase lock (zero offset)
  - Strong lock with noise
  - Weak lock (near detection threshold)
  - Full Jacobi packet

### 3. Scripts ✓

All scripts include:
- Comprehensive docstrings
- Explanatory comments
- Command-line interfaces
- Error handling
- Progress reporting

#### `scripts/run_grid.py`
- Wrapper for main grid runner module
- Preserves existing run_grid.py at top level

#### `scripts/run_controls.py`
- Executes negative and positive control experiments
- Generates synthetic test data
- Validates analysis pipeline sensitivity
- Outputs control summary CSV

#### `scripts/aggregate.py`
- Scans output directories for results
- Parses CSVs and configurations
- Applies Benjamini-Hochberg FDR correction
- Computes summary statistics
- Generates unified summary.csv

#### `scripts/plot_summary.py`
- Phase coherence distributions by k
- P-value histograms
- Parameter sweep plots (PC vs window_size, etc.)
- Twin prime comparison plots
- Supports PNG, PDF, SVG output formats

#### `scripts/jacobi_packet.py`
- Analyzes full Jacobi cluster (k=134-143)
- Individual k coherence profiles
- Cluster-wide patterns
- Statistical significance across packet
- Spectrum visualization

#### `scripts/devil_audit.py`
- Generates skeptical "Devil's Advocate" audit report
- Explores artifact hypotheses:
  - Statistical artifacts (multiple testing, look-elsewhere)
  - Instrumental systematics
  - Analysis pipeline artifacts
  - Foreground contamination
  - Spurious correlations
- Outputs comprehensive markdown report

### 4. Documentation ✓

#### `QUICKSTART.md`
- 5-minute quick start guide
- Installation prerequisites
- Common workflows
- Troubleshooting tips
- Usage examples

#### `README.md` (Enhanced)
- **NEW**: Complete pre-registration section
- Success thresholds and decision rules
- Primary endpoints (PC_137, PC_139, p_137, p_139, etc.)
- Primary success criteria (p ≤ 0.01, PC ≥ 0.50, etc.)
- Secondary validation criteria
- Failure criteria
- Multiple testing strategy (BH-FDR)
- Reporting standards

### 5. Tests ✓

#### `tests/test_configs_load.py`
- Validates all YAML configs load correctly
- Checks required fields present
- Verifies config structure
- Tests success thresholds defined
- **Status**: ✓ All 5 tests pass

#### `tests/test_aggregate_smoke.py`
- Tests Benjamini-Hochberg FDR correction
- Tests aggregation with mock results
- Validates CSV output format
- **Status**: Requires numpy (expected in CI environment)

### 6. Pre-Registration ✓

Comprehensive pre-registration implemented in README.md:

**Primary Endpoints:**
- PC_137, PC_139, p_137, p_139, z_137, z_139
- DeltaPC = |PC_137 - PC_139|
- TwinPrimeScore = min(z_137, z_139) - λ·DeltaPC

**Success Criteria:**
1. Statistical: p ≤ 0.01 (both targets)
2. Effect size: PC ≥ 0.50 (both targets)
3. Consistency: DeltaPC ≤ 0.10
4. FDR correction: q ≤ 0.05 (when N > 1)

**Secondary Validation:**
- Survives null models (phase-shuffle, phi-roll)
- Robust to parameter variations
- Consistent across component maps
- Controls pass validation

## Key Features

### 1. Non-Invasive Design
- **Zero modifications** to `forensic_fingerprint/tools/*`
- All code in `research_phase_lock/` directory
- Wraps existing tool via subprocess calls

### 2. Reproducibility
- Fixed seeds for all random processes
- Configuration hashing for unique run IDs
- Full provenance tracking (git commit, timestamps)
- Every run saves exact config.yaml used

### 3. Scientific Rigor
- Pre-registered success criteria
- Benjamini-Hochberg FDR correction
- Negative and positive controls
- Devil's advocate skeptical analysis
- Blinded analysis support

### 4. Robustness Testing
- Multiple window sizes
- Multiple resolutions (nside_out)
- Multiple null models
- Different window functions
- Parameter sweep analysis

### 5. Comprehensive Reporting
- Summary statistics by target k
- Parameter sweep visualizations
- Twin prime comparison plots
- FDR-corrected significance levels
- Artifact hypothesis exploration

## Usage Examples

### Quick Start
```bash
# Test configuration loading
python research_phase_lock/tests/test_configs_load.py

# Preview grid run
python -m research_phase_lock.run_grid \
    --config research_phase_lock/configs/grid.yaml \
    --dry-run

# Run full grid (requires numpy, healpy, etc.)
python -m research_phase_lock.run_grid \
    --config research_phase_lock/configs/grid.yaml
```

### Control Experiments
```bash
# Run negative controls (should NOT show phase lock)
python scripts/run_controls.py \
    --config configs/controls.yaml \
    --type negative

# Run positive controls (should DEFINITELY show phase lock)
python scripts/run_controls.py \
    --config configs/controls.yaml \
    --type positive
```

### Analysis Pipeline
```bash
# 1. Aggregate all results
python scripts/aggregate.py \
    --input-dir outputs \
    --output results/summary.csv

# 2. Generate plots
python scripts/plot_summary.py \
    --input results/summary.csv \
    --output results/plots/

# 3. Jacobi packet analysis
python scripts/jacobi_packet.py \
    --config configs/grid.yaml

# 4. Devil's advocate audit
python scripts/devil_audit.py \
    --results-dir outputs \
    --output results/audit_report.md \
    --summary-csv results/summary.csv
```

## Dependencies

Runtime dependencies (specified in repository requirements.txt):
- numpy >= 1.20.0
- healpy >= 1.15.0
- matplotlib >= 3.3.0
- pyyaml (already available)
- scipy >= 1.7.0 (for statistics)

These are already in the repository requirements.txt and will be installed in CI.

## Testing Status

| Test | Status | Notes |
|------|--------|-------|
| Config loading | ✓ PASS | All 5 tests pass |
| Syntax validation | ✓ PASS | All scripts compile |
| Grid runner --help | ✓ PASS | CLI works |
| Aggregation smoke | Pending | Requires numpy (CI will have it) |
| Full integration | Pending | Requires running grid |

## Validation Checklist

- [x] Directory structure created
- [x] QUICKSTART.md written
- [x] configs/grid.yaml enhanced
- [x] configs/controls.yaml created
- [x] scripts/run_grid.py wrapper
- [x] scripts/run_controls.py implemented
- [x] scripts/aggregate.py with BH-FDR
- [x] scripts/plot_summary.py visualizations
- [x] scripts/jacobi_packet.py analysis
- [x] scripts/devil_audit.py skeptical report
- [x] tests/test_configs_load.py
- [x] tests/test_aggregate_smoke.py
- [x] README.md pre-registration section
- [x] All Python syntax valid
- [x] Configuration files load correctly
- [ ] Full integration test (requires dependencies)
- [ ] Run on real Planck data (requires data)

## Next Steps

1. **Install dependencies** (in CI or local environment):
   ```bash
   pip install -r requirements.txt
   ```

2. **Run smoke test**:
   ```bash
   pytest research_phase_lock/tests/test_smoke_synthetic.py -v
   ```

3. **Run small grid**:
   ```bash
   python -m research_phase_lock.run_grid \
       --config research_phase_lock/configs/minimal_test.yaml
   ```

4. **Run control experiments**:
   ```bash
   python research_phase_lock/scripts/run_controls.py \
       --config research_phase_lock/configs/controls.yaml
   ```

5. **Aggregate and analyze**:
   ```bash
   python research_phase_lock/scripts/aggregate.py \
       --input-dir research_phase_lock/outputs \
       --output research_phase_lock/results/summary.csv
   
   python research_phase_lock/scripts/plot_summary.py \
       --input research_phase_lock/results/summary.csv \
       --output research_phase_lock/results/plots/
   ```

## Compliance with Requirements

✅ **All requirements met:**

1. ✓ Separate directory (research_phase_lock/)
2. ✓ No modifications to forensic_fingerprint/tools
3. ✓ Pre-registration success thresholds (README.md)
4. ✓ Parameter grid runner (run_grid.py)
5. ✓ Result aggregation with BH-FDR (aggregate.py)
6. ✓ Summary plots (plot_summary.py)
7. ✓ Control experiments (run_controls.py)
8. ✓ Jacobi packet analysis (jacobi_packet.py)
9. ✓ Devil's advocate audit (devil_audit.py)
10. ✓ Explanatory comments in all code
11. ✓ Reproducibility (seeds, configs, hashing)
12. ✓ CLI interfaces for all scripts
13. ✓ Tests for configuration and aggregation
14. ✓ QUICKSTART.md quick start guide

## License

See repository LICENSE.md

## Author

UBT Research Team (implementation of David Jaroš's theoretical framework)
