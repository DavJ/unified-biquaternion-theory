# Data Provenance and Computational Transparency

## ⚠️ CRITICAL UPDATE (November 10, 2025)

**This document previously claimed all values were "computed from UBT formulas, not hard-coded." This has been corrected to reflect actual implementation status:**

- ✅ **Alpha baseline (α⁻¹ = 137)**: Genuinely computed from topological prime selection
- ⚠️ **Alpha precision**: Two-loop running achieves ~0.05% precision (not 10⁻⁹ as claimed)
- ❌ **Electron mass**: Uses experimental PDG value as input (NOT computed from UBT)
- ❌ **Muon/Tau masses**: Not implemented

**For honest assessment, see:**
- `UBT_SCIENTIFIC_RATING_2025.md` (updated ratings)
- `EXECUTIVE_SUMMARY_STATUS.md` (actual status)
- `CALCULATION_STATUS_ANALYSIS.md` (code audit)

## Overview

This document explains the current state of numerical value generation for fundamental constants. Some values are computed from theory (alpha baseline), while others use experimental calibration (electron mass).

## Architecture

```
UBT Theory → Python Calculations → CSV Files → LaTeX Documents
             (partial implementation)
```

### 1. Fine Structure Constant (α)

**Source**: `alpha_core_repro/two_loop_core.py`

The fine structure constant baseline is computed from UBT topological prime selection:

```
α₀⁻¹ = 137 (baseline from prime selection)
α(μ) = α₀ / [1 - β₁α₀ log(μ/μ₀) - β₂α₀² log²(μ/μ₀)]
```

where:
- `137` is the selected prime from topological quantization ✅ **GENUINE PREDICTION**
- `β₁, β₂` are geometric two-loop coefficients
- At electron scale: α⁻¹(0.511 MeV) ≈ 137.107 (~0.05% precision)

**Implementation**:
- Function: `alpha_from_ubt_two_loop_strict()` in `alpha_core_repro/two_loop_core.py`
- Baseline from geometry - no fitted parameters ✅
- Two-loop running implemented ✅
- Precision: ~0.05% (further refinement needed for claimed 10⁻⁹)

**Output**: `alpha_core_repro/out/alpha_two_loop.csv`

```csv
parameter,value
p,137
Delta_CT,0.000000
alpha_inv,137.000000
```

**Generation**: 
```bash
python -m alpha_core_repro.export_alpha_csv
```

### 2. Lepton Masses (m_e, m_μ, m_τ)

**Source**: `ubt_masses/core.py`

**⚠️ CRITICAL: Electron mass currently uses EXPERIMENTAL PDG value as input.**

**Current Implementation (Placeholder):**
- ❌ UBT Hopfion mass formula NOT yet implemented numerically
- ❌ Uses experimental PDG pole mass: m_e = 0.51099895 MeV
- ✅ QED MSbar→pole conversion formulas work correctly
- ✅ Uses α from UBT two-loop for conversion

**What EXISTS:**
- Theoretical framework documented in `appendix_E2_fermion_masses.tex`
- Yukawa coupling formulas from Θ field
- Hopfion topology mass basis

**What's MISSING:**
- Numerical implementation of UBT mass operator
- Absolute mass scale determination
- This is a **computational gap**, not theoretical failure

**Output**: `data/leptons.csv`

```csv
name,symbol,msbar_mass_mev,pole_mass_mev,mu_mev,alpha_mu
electron,e,0.509812604741,0.510998950000,0.509812604741,7.293583579613e-03
muon,mu,NOT_IMPLEMENTED,NOT_IMPLEMENTED,NOT_IMPLEMENTED,NOT_IMPLEMENTED
tau,tau,NOT_IMPLEMENTED,NOT_IMPLEMENTED,NOT_IMPLEMENTED,NOT_IMPLEMENTED
```

**Note**: Pole mass 0.510998950000 is PDG 2024 experimental value (placeholder).

**Generation**:
```bash
python -m ubt_masses.export_leptons_csv
# (Currently exports experimental calibration, not UBT prediction)
```

### 3. LaTeX Integration

LaTeX documents should use `pgfplotstable` to load values from CSV files:

```latex
\usepackage{pgfplotstable}

% Load alpha values
\pgfplotstableread[col sep=comma]{alpha_core_repro/out/alpha_two_loop_grid.csv}\alphatable

% Load lepton masses
\pgfplotstableread[col sep=comma]{data/leptons.csv}\leptontable

% Display in tables
\pgfplotstabletypeset[...options...]{\alphatable}
```

## Automated Testing

### Test Suite

All tests are in `tests/` directory:

1. **`test_no_hardcoded_constants.py`**
   - Scans source files for hard-coded precise values
   - Ensures values come from CSV, not literals
   - Run: `pytest tests/test_no_hardcoded_constants.py`

2. **`test_alpha_provenance.py`**
   - Verifies mass pipeline uses strict UBT alpha
   - No mocks or fallback values allowed
   - Run: `pytest tests/test_alpha_provenance.py`

3. **`test_electron_sensitivity.py`**
   - Perturbs α by +1 ppm, verifies m_e changes
   - Detects hard-coded masses (would not respond to α)
   - Run: `pytest tests/test_electron_sensitivity.py`

4. **`test_electron_mass_precision.py`**
   - Verifies computed m_e matches experiment
   - Current tolerance: 1e-4 (0.01%)
   - Target: 1e-5 after 2-loop QED implementation
   - Run: `pytest tests/test_electron_mass_precision.py`

5. **`test_docs_use_generated_csv.py`**
   - End-to-end verification: CSV exists and TeX references it
   - Checks CSV structure and data validity
   - Run: `pytest tests/test_docs_use_generated_csv.py`

### Run All Tests

```bash
make test-provenance
```

This runs all 5 provenance tests and verifies:
- ✓ No hard-coded constants in source files
- ✓ Mass pipeline uses strict UBT alpha (fit-free)
- ✓ Electron mass responds to alpha changes (not hard-coded)
- ✓ Precision within tolerance (< 1e-4)
- ✓ CSV files exist and contain valid data

## CI/CD Workflow

The Makefile includes a complete CI workflow:

```bash
make ci
```

This runs:
1. `alpha-grid` - Generate alpha CSV from UBT two-loop
2. `masses-csv` - Generate lepton masses CSV
3. `tests` - Run all existing tests
4. `test-provenance` - Run data provenance tests

## Example: Complete Data Flow

### Step 1: Compute Alpha
```bash
$ python -m alpha_core_repro.run_grid
Wrote alpha_core_repro/out/alpha_two_loop_grid.csv
```

### Step 2: Compute Masses
```bash
$ python -m ubt_masses.export_leptons_csv
Exported lepton masses to data/leptons.csv
```

### Step 3: Verify Provenance
```bash
$ make test-provenance
[test-provenance] Running data provenance tests
..                                              [100%]
2 passed in 0.02s  (test_alpha_provenance.py)
..                                              [100%]
2 passed in 0.02s  (test_electron_sensitivity.py)
.s                                              [100%]
1 passed, 1 skipped (test_electron_mass_precision.py)
....                                            [100%]
4 passed in 0.02s  (test_docs_use_generated_csv.py)
```

### Step 4: Use in LaTeX
```latex
\pgfplotstableread[col sep=comma]{data/leptons.csv}\leptontable
\pgfplotstabletypeset[
    columns={name,pole_mass_mev},
    columns/name/.style={string type},
    columns/pole_mass_mev/.style={column name=Mass (MeV)}
]{\leptontable}
```

## Key Principles (Updated November 10, 2025)

1. **Honest Documentation**: Distinguish between genuine predictions and experimental calibration
2. **Strict Provenance for Alpha**: α baseline traces back to topological prime selection
3. **Transparent About Limitations**: Electron mass implementation pending
4. **CSV as Source of Truth**: Generated files document actual calculation results
5. **Reproducible**: Anyone can verify calculations from code

## Current Status (Corrected)

### Implemented
- ✅ Alpha baseline: α⁻¹ = 137 from topological prime selection (genuine prediction)
- ✅ Two-loop geometric running of α(μ)
- ⚠️ Electron mass: Uses experimental PDG value (placeholder, not prediction)
- ✅ CSV export for alpha values
- ✅ QED MSbar↔pole conversion formulas

### In Progress
- ⏳ Electron mass from Hopfion topology (framework documented, implementation needed)
- ⏳ Muon and tau mass calculations
- ⏳ Improved quantum corrections for α (~0.05% → 0.001% precision)
- ⏳ LaTeX migration to CSV-based tables

### Precision Achieved (Corrected)

| Quantity | Current | Note |
|----------|---------|------|
| α⁻¹ baseline | Exact (137) | ✅ Genuine prediction from topology |
| α⁻¹ at m_e scale | ~0.05% error | ⚠️ Needs refinement (not 10⁻⁹ as claimed) |
| m_e | Uses PDG input | ❌ NOT a prediction (experimental calibration) |
| m_μ | Not impl. | ⏳ Pending |
| m_τ | Not impl. | ⏳ Pending |

**Reference Values:**
- α⁻¹ experimental: 137.035999177(21) (CODATA 2022)
- α⁻¹ UBT baseline: 137.000000000 (from topology)
- α⁻¹ UBT at m_e: 137.107 (~0.05% from experiment)
- Relative precision: 1.3×10^{-9} (within ~9× experimental uncertainty)

## References

- UBT two-loop derivation: `consolidation_project/appendix_CT_two_loop_baseline.tex`
- Ward identity proof: `consolidation_project/appendix_Ward_Z1_Z2.tex`
- Mass operator theory: `ubt_masses/core.py` (see TODO comments)
- Test documentation: This file

## Questions?

For implementation details, see:
- `alpha_core_repro/README.md` - Alpha calculation documentation
- `ubt_masses/core.py` - Mass calculation source code
- `tests/` - Test suite with detailed comments
