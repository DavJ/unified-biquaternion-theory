# CSV Data and Documentation Values - Policy

## Overview

This document clarifies the policy for using computed constants vs. reference values in documentation files.

## Data Provenance Chain

The proper data flow for computed constants is:

```
UBT Theory → Python Calculations → CSV Files → LaTeX Documents (via macros)
```

## File Types and Usage Policies

### 1. Python Source Files (`*.py`)

**Policy:** Must NOT contain ultra-precise hard-coded constants

**Exceptions:**
- `validate_*.py` - Validation scripts comparing computed vs. experimental values
- `test_*.py` - Test files with reference values
- Tool scripts (`audit_computed_not_reference.py`, `replace_core_literals_with_macros.py`)

**Enforcement:** `tests/test_no_hardcoded_constants.py` scans all Python files

### 2. LaTeX Documents (`*.tex`)

**Policy:** Should use CSV imports via `\pgfplotstable` or LaTeX macros

**Implementation:**
- CSV data imported in `tex/snippets_insert.tex`
- Values used via `\pgfplotstableread` or similar
- Macros defined in generated `.tex` files (e.g., `UBT_alpha_per_sector_patch.tex`)

**Example:**
```latex
\pgfplotstabletypeset[
  col sep=comma,
  columns={mu,alpha,alpha_inv}
]{data/alpha_two_loop_grid.csv}
```

### 3. Markdown Documentation Files (`*.md`)

**Policy:** Different from LaTeX - markdown files serve as human-readable documentation

**Three Categories:**

#### A. Reference/Comparison Files (Allowed to contain precise values)
These files compare UBT predictions with experimental values:
- `README.md` - Main documentation with comparison tables
- `OVERVIEW.md` - Theory overview with experimental comparisons
- `TESTABILITY_AND_FALSIFICATION.md` - Lists experimental targets
- `FITTED_PARAMETERS.md` - Documents parameters and experimental values
- `UBT_COMPREHENSIVE_REVIEW_DEC_2025.md` - Comprehensive review
- Others listed in `tests/test_no_hardcoded_constants.py` whitelist

**Rationale:** These files need to show both computed AND experimental values for comparison. The experimental values (CODATA, PDG) are NOT hardcoded predictions - they are reference standards.

#### B. Provenance Documentation (Shows CSV examples)
- `DATA_PROVENANCE.md` - Documents the CSV generation process with examples
- `PYTHON_SCRIPTS_REPORT.md` - This report, showing CSV structure

**Rationale:** These files explain the data pipeline and may include sample CSV content for illustration.

#### C. Generated Reports (Values from automated processes)
Ideally, some markdown reports could be generated from CSV data using tools, but this is not currently implemented.

## Why Markdown is Different from LaTeX

**Key Difference:** Markdown files cannot natively import CSV data or use LaTeX macros.

**Options for Markdown:**

1. **Manual Updates:** Update values when CSV files change (current approach for most files)
2. **Template Generation:** Use a tool to generate markdown from CSV (not implemented)
3. **Reference Values Only:** Document experimental values, link to CSV files for computed values

**Current Approach:**
- Documentation files contain experimental reference values (CODATA, PDG)
- CSV files contain UBT-computed values
- Comparison is shown in tables (e.g., "UBT predicts X, experiment shows Y")

## CSV Files - The Source of Truth (Updated November 10, 2025)

For UBT-computed constants, the CSV files are the ONLY source of truth:

| Constant | CSV File | Column | Value | Status |
|----------|----------|--------|-------|--------|
| α⁻¹ baseline (p=137) | `alpha_core_repro/out/alpha_two_loop.csv` | `alpha_inv` | 137.000000 | ✅ Predicted from topology |
| α(μ) running | `validation/alpha_running_table.csv` | `alpha_mu` | varies | ✅ Two-loop running |
| m_e (pole) | `data/leptons.csv` | `pole_mass_mev` | 0.510998950000 | ❌ Experimental (PDG placeholder) |
| m_e (MSbar) | `data/leptons.csv` | `msbar_mass_mev` | 0.509812604741 | ❌ From PDG via QED conversion |

**⚠️ IMPORTANT:** Only α baseline is genuinely predicted. Electron mass uses experimental PDG value as input.

## Generating Markdown from CSV (Future Enhancement)

To automatically generate markdown tables from CSV data:

```bash
# Example tool (not yet implemented)
python tools/csv_to_markdown.py \
  --csv data/leptons.csv \
  --output docs/lepton_masses.md \
  --template templates/lepton_table.md.j2
```

This could ensure markdown documentation always reflects latest CSV values.

## Testing and Enforcement

**For Python/LaTeX:**
```bash
# Verify no hardcoded constants in source files
python tests/test_no_hardcoded_constants.py

# Verify CSV files exist and are used by LaTeX
python tests/test_docs_use_generated_csv.py
```

**For Markdown:**
- Documentation files are whitelisted (they contain reference values)
- Manual review ensures they cite CSV files as source of computed values
- Future: Automated generation from CSV templates

## Summary

1. **Python source files:** Must NOT hardcode precise constants (enforced by tests)
2. **LaTeX documents:** Use CSV imports via macros (enforced by tests and conventions)
3. **Markdown documentation:** Can contain reference values for comparison; should cite CSV files for UBT predictions
4. **CSV files:** Single source of truth for all UBT-computed constants

## See Also

- [PYTHON_SCRIPTS_REPORT.md](PYTHON_SCRIPTS_REPORT.md) - Complete documentation of scripts and CSV files
- [DATA_PROVENANCE.md](DATA_PROVENANCE.md) - Data provenance and computational transparency
- `tests/test_no_hardcoded_constants.py` - Test enforcement
- `tests/test_docs_use_generated_csv.py` - CSV validation
