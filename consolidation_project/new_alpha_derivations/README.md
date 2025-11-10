# New Alpha Derivations

**Purpose:** Alternative theoretical approaches to derive the fine structure constant (α) from UBT first principles

**Status:** Active research - exploratory calculations

## Overview

This directory contains theoretical derivations and computational scripts that explore different pathways to derive the electromagnetic fine structure constant α from the Unified Biquaternion Theory framework. The approaches here complement the established two-loop calculations in `alpha_core_repro/`.

## Contents

### Python Scripts

#### 1. `ubt_alpha_minimizer.py`
**Purpose:** Noether current to alpha via effective potential minimization

**Method:**
- Computes effective potential V_eff for massless fields in 5D (M⁴ × S¹_ψ)
- Uses polylog functions to evaluate Casimir-like contributions
- Finds stationary points in θ_H (Higgs phase) space
- Identifies minima and maxima via second derivative test

**Dependencies:**
- `mpmath` - for high-precision polylog calculations
- `numpy` - for numerical analysis

**Usage:**
```bash
python3 ubt_alpha_minimizer.py
```

**Output:** Dictionary of stationary points with V, dV/dθ, d²V/dθ², and type (min/max)

**Theory:** Based on Noether current gauging and 5D Kaluza-Klein reduction

---

#### 2. `ubt_induced_alpha_powerpluslog.py`
**Purpose:** Induced 1/α from 5D power-law + 4D KK logarithmic contributions

**Method:**
- Computes Kaluza-Klein tower masses with Wilson line phases
- Evaluates 5D power-law corrections via heat-kernel C₅ coefficients
- Sums 4D logarithmic contributions from KK modes
- Supports both Dirac fermions and scalar fields

**Dependencies:**
- `numpy` - for array operations
- `mpmath` - for high-precision arithmetic
- `json` - for structured output

**Usage:**
```bash
python3 ubt_induced_alpha_powerpluslog.py
```

**Output:** JSON with:
- `inv_alpha_total` - total 1/α value
- `alpha_total` - induced α
- `inv_alpha_logs` - contribution from logarithmic terms
- `power_term` - contribution from 5D power-law
- `detail` - per-field breakdown

**Configuration:**
- `L` - compactification radius
- `theta_H` - Higgs phase
- `cutoff` - UV cutoff scale
- `Z` - flat zero-mode factor
- `fields` - list of field configurations

**Theory:** Based on dimensional reduction with heat-kernel expansion

---

### LaTeX Documents

These documents trace the evolution of the Noether → α derivation:

#### Version History

**Latest (Clean):**
- `noether_to_alpha_clean_v1.2.tex` - **Current clean derivation** (recommended reading)
- `noether_to_alpha_v1.0_worked_example.tex` - Worked example with numerical values

**Consistency Checks:**
- `ubt_alpha_consistency_v1.1.tex` - Verification of internal consistency
- `ubt_alpha_simple_box_v1.tex` - Simplified box diagram approach

**Development Versions (Historical):**
- `noether_to_alpha_v0.1.tex` - Initial formulation
- `noether_to_alpha_v0.2.tex` - First refinement
- `noether_to_alpha_v0.3.tex` - Gauge coupling clarifications
- `noether_to_alpha_v0.4.tex` - KK mode corrections
- `noether_to_alpha_v0.5.tex` - Wilson line integration
- `noether_to_alpha_v0.7.tex` - Heat kernel improvements
- `noether_to_alpha_v0.9.tex` - Near-final version

**Reading Order (for newcomers):**
1. `noether_to_alpha_clean_v1.2.tex` - start here
2. `noether_to_alpha_v1.0_worked_example.tex` - see concrete example
3. `ubt_alpha_consistency_v1.1.tex` - understand checks
4. Earlier versions - only for historical context

---

## Theoretical Framework

### Noether → α Pathway

The derivation proceeds in three steps:

1. **Global U(1) symmetry:** Start with biquaternionic field Θ carrying phase symmetry Q
2. **Gauging:** Promote global symmetry to local U(1) gauge symmetry
3. **5D → 4D reduction:** Integrate out ψ dimension to obtain effective 4D coupling

**Key Formula:**
```
1/α = ∫ dψ √g₅ × [geometric factors] × [KK sum]
```

where geometric factors arise from metric components and KK sum includes Wilson line phases.

### Power + Log Structure

The induced coupling has two contributions:

**Power-law (5D):**
```
Δ(power) ~ Z × Λ × C₅ × Q²
```
where C₅ are heat-kernel coefficients (different for scalars vs. fermions)

**Logarithmic (4D KK modes):**
```
Δ(log) ~ Σ_n (Q²/6π) × log(Λ/m_n)
```
where m_n = √(m₀² + p_ψ²) are KK masses with Wilson line shifts.

### Relation to Two-Loop Calculations

These derivations are **complementary** to the established two-loop calculations in `alpha_core_repro/`:

- **Two-loop:** Standard QED vacuum polarization approach, MSbar scheme
- **Noether/KK:** 5D geometric approach, dimensionally reduced
- **Both** are valid UBT derivations from different starting points
- **Consistency:** Both should yield α⁻¹ ≈ 137.036 at Thomson limit

---

## Dependencies

### Python Packages
```bash
pip install numpy mpmath
```

### LaTeX Packages
Standard packages required for compilation:
- `amsmath`, `amssymb`, `amsfonts` - mathematical symbols
- `physics` - bra-ket notation and derivatives
- `tcolorbox` - highlighted boxes
- `geometry` - page layout

---

## Running the Scripts

### Test Alpha Minimizer
```bash
cd /path/to/repo
python3 consolidation_project/new_alpha_derivations/ubt_alpha_minimizer.py
```

Expected output: 2 stationary points (one minimum at θ=0, one maximum at θ=π)

### Test Induced Alpha Calculator
```bash
cd /path/to/repo
python3 consolidation_project/new_alpha_derivations/ubt_induced_alpha_powerpluslog.py
```

Expected output: JSON with α_total ≈ 2.4 (placeholder values - needs proper field content)

### Compile LaTeX Documents
```bash
cd consolidation_project/new_alpha_derivations/
pdflatex noether_to_alpha_clean_v1.2.tex
pdflatex noether_to_alpha_clean_v1.2.tex  # Second pass for references
```

---

## Integration with Main UBT

These derivations are referenced in:
- Main UBT document appendices (when discussing α emergence)
- `PYTHON_SCRIPTS_REPORT.md` - inventory of computational scripts
- `EMERGENT_ALPHA_README.md` - overview of α calculation approaches

---

## Development Status

**Current State:**
- ✅ Scripts functional and tested
- ✅ Mathematical framework established
- ⚠️ Numerical values are placeholders (need proper parameter fitting)
- 🔄 Active research - refinements ongoing

**Next Steps:**
1. Match parameters to two-loop results for consistency
2. Explore sector-dependent form factors
3. Investigate Hecke operator corrections
4. Document convergence properties of KK sums

---

## References

**Internal:**
- `alpha_core_repro/README.md` - Two-loop approach
- `EMERGENT_ALPHA_README.md` - Overview of α derivations
- UBT main appendices - Theoretical foundation

**External:**
- Kaluza-Klein theory: compactification and mode expansion
- Heat kernel methods: Seeley-DeWitt coefficients
- Noether's theorem: conserved currents and symmetries

---

## License

SPDX-License-Identifier: CC-BY-4.0  
Copyright (c) 2025 David Jaroš

This work is part of the Unified Biquaternion Theory project.
Licensed under Creative Commons Attribution 4.0 International License.

---

## Authors

**Implementation:** David Jaroš  
**Theory:** See `PRIORITY.md` for attribution  
**Framework:** Unified Biquaternion Theory

---

*Last Updated: 2025-11-09*
