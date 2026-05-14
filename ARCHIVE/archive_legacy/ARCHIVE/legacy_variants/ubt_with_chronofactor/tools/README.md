# UBT Alpha Audit Tools

This directory contains automated tools for auditing the rigor of UBT's fine-structure constant (α) derivation.

## Tools Overview

### 1. `alpha_audit.py` - Repository Scanner

Scans the entire UBT repository for occurrences of alpha-related terms.

**Usage:**
```bash
# Scan entire repository
python tools/alpha_audit.py --root . --out reports/alpha_hits.json

# Custom context size
python tools/alpha_audit.py --context 10

# Custom terms
python tools/alpha_audit.py --terms "alpha" "137" "fine-structure"
```

**Output:** `reports/alpha_hits.json` - JSON file containing all occurrences with context

### 2. `latex_extract.py` - Equation Extractor

Extracts equations, theorems, lemmas, and definitions from LaTeX files.

**Usage:**
```bash
# Extract all equations
python tools/latex_extract.py --root . --out reports/alpha_equations.json

# Filter for alpha-related only
python tools/latex_extract.py --filter
```

**Output:** `reports/alpha_equations.json` - JSON file containing equations with labels

### 3. `fill_checklist.py` - Checklist Automation

Automatically fills the alpha derivation checklist using data from the audit and extraction tools.

**Usage:**
```bash
# Use default files
python tools/fill_checklist.py

# Custom inputs
python tools/fill_checklist.py --hits reports/alpha_hits.json --equations reports/alpha_equations.json
```

**Output:** `reports/alpha_checklist_filled.md` - Filled checklist with evidence

### 4. `dependency_scan.py` - Dependency Graph Builder

Constructs a directed graph of symbol dependencies to detect circular dependencies.

**Usage:**
```bash
# Build dependency graph
python tools/dependency_scan.py

# Custom output
python tools/dependency_scan.py --dot reports/alpha_deps.dot --svg reports/alpha_deps.svg
```

**Output:**
- `reports/alpha_deps.dot` - Graphviz DOT file
- `reports/alpha_deps.svg` - SVG visualization (requires graphviz installed)

**Requirements:** graphviz (optional, for SVG rendering)

```bash
# Install graphviz
sudo apt-get install graphviz  # Ubuntu/Debian
brew install graphviz          # macOS
```

## Workflow

Complete audit workflow:

```bash
# 1. Scan repository for alpha terms
python tools/alpha_audit.py --root . --out reports/alpha_hits.json

# 2. Extract equations and definitions
python tools/latex_extract.py --root . --out reports/alpha_equations.json --filter

# 3. Fill checklist automatically
python tools/fill_checklist.py

# 4. Build dependency graph
python tools/dependency_scan.py

# 5. Review outputs:
#    - reports/alpha_hits.json (raw occurrences)
#    - reports/alpha_equations.json (equations)
#    - reports/alpha_checklist_filled.md (checklist)
#    - reports/alpha_deps.dot (dependency graph)
#    - reports/alpha_deps.svg (visualization)
```

## Output Files

All outputs are written to the `reports/` directory:

- `alpha_hits.json` - All alpha-related term occurrences with context
- `alpha_equations.json` - Extracted equations, theorems, lemmas
- `alpha_checklist_filled.md` - Filled checklist with evidence
- `alpha_deps.dot` - Dependency graph (DOT format)
- `alpha_deps.svg` - Dependency graph (SVG visualization)

## Templates

The `reports/templates/` directory contains:

- `alpha_checklist.md` - Template for the derivation checklist

## Purpose

These tools automate the verification that UBT's α derivation:

1. **Has no free parameters** - R_ψ, N_eff, R_UBT are all determined by theory
2. **Respects Ward identities** - Z1 = Z2 in the CT scheme
3. **Reduces to QED** - Continuous ψ → 0 limit
4. **Has no circular dependencies** - Derivation chain is well-founded
5. **Is rigorously proven** - Theorems and lemmas support all claims

## Requirements

- Python 3.7+
- Standard library only (no external dependencies for core functionality)
- graphviz (optional, for SVG rendering in dependency_scan.py)

## Author

UBT Team  
Version: 1.0
