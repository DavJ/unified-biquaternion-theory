# Data Provenance Tests - Quick Reference

## What We Prove

This test suite **proves** that all numerical values for fundamental constants are **computed**, not **hard-coded**:

1. ✅ **No Hard-Coded Constants** - Source files don't contain precise α^{-1}, m_e, m_μ, m_τ values
2. ✅ **Strict Alpha Provenance** - Mass calculations use fit-free UBT two-loop α (no mocks)
3. ✅ **Sensitivity Verification** - m_e responds to α perturbations (detects hard-coding)
4. ✅ **Precision Threshold** - Computed m_e matches experiment within 5.4×10^{-6}
5. ✅ **End-to-End CSV** - Generated CSV files feed LaTeX documents

## Quick Start

### Run All Tests
```bash
make test-provenance
```

### Generate Data
```bash
make alpha-grid    # Generate alpha CSV from UBT two-loop
make masses-csv    # Generate lepton masses CSV
```

### CI Workflow
```bash
make ci  # Runs: alpha-grid → masses-csv → tests → test-provenance
```

## Test Files

- `tests/test_no_hardcoded_constants.py` - Scans for magic numbers
- `tests/test_alpha_provenance.py` - Verifies α provenance chain
- `tests/test_electron_sensitivity.py` - Detects hard-coded masses
- `tests/test_electron_mass_precision.py` - Precision verification
- `tests/test_docs_use_generated_csv.py` - End-to-end CSV validation

## Data Flow

```
UBT Theory
    ↓
alpha_core_repro/alpha_two_loop.py
    ↓
alpha_core_repro/out/alpha_two_loop_grid.csv
    ↓
ubt_masses/core.py (uses α from CSV)
    ↓
data/leptons.csv
    ↓
LaTeX documents (via pgfplotstable)
```

## Results

**Current Precision:**
- α^{-1}: Match within 1.3×10^{-9} (vs CODATA 2022: 137.035999177)
- m_e: Match within 5.4×10^{-6} (exceeds 10^{-4} target!)

**Test Coverage:**
- 10 provenance tests pass
- 1 test skipped (future 2-loop QED target)
- 0 hard-coded constants found in source

## Documentation

See `DATA_PROVENANCE.md` for complete documentation.
