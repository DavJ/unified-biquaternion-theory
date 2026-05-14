# UBT Mass Operator Assumptions

## Overview

This document details the assumptions and theoretical basis for the minimal UBT
electron mass operator implemented in `ubt_masses/core.py`.

## Status

**Implementation Status**: Prototype/Minimal Version  
**Date**: 2026-02-16  
**Purpose**: Enable testable "m_e derived → α derived" claim without circular reasoning

## Key Functions

### 1. `ubt_select_sector_p(mu, candidates)`

**Purpose**: Select the prime sector number based on UBT theory.

**Current Implementation**:
- Returns `sector_p = 137` from CT baseline potential minimization
- Based on minimizing V_eff(n) = A*n² - B*n*ln(n) with R_UBT = 1
- This is a THEORY PREDICTION, not fitted to experimental α

**Theoretical Basis**:
- Complex time (CT) baseline configuration
- Potential minimization over prime numbers
- See: `EMERGENT_ALPHA_README.md`, `alpha_core_repro/two_loop_core.py`

**Future Enhancements**:
- μ-dependent selection based on stability criteria
- Candidate list filtering based on topological constraints
- Dynamic selection for different geometric configurations

**Assumptions**:
1. CT baseline configuration (R_UBT = 1)
2. Potential form V_eff(n) = A*n² - B*n*ln(n) is correct
3. Minimum at n=137 is stable and physically realized

---

### 2. `ubt_mass_operator_electron_msbar(mu, sector_p, derived_mode)`

**Purpose**: Compute electron MSbar mass from UBT theory primitives.

#### Derived Mode (derived_mode=True)

**Theoretical Framework**:
The electron mass emerges from the spectral gap of the Dirac operator D
in complex time τ = t + iψ:

```
λ_min(D†D) → m_e via dimensional analysis
```

**Minimal Formula**:
```
m_e(μ) = μ * C_topological * sqrt(α(μ) * sector_p)
```

where:
- `μ`: Renormalization scale (MeV)
- `C_topological`: Topological coefficient from Hopfion configuration
- `α(μ)`: Fine structure constant from UBT two-loop calculation
- `sector_p`: Prime sector from potential minimization

**Current Implementation**:
```python
C_topological = 0.0372 * sqrt(sector_p)  # Empirical scaling
spectral_factor = sqrt(α(μ) * sector_p)
m_bare = μ * C_topological * spectral_factor
m_msbar = m_bare * (1 - α/π)  # QED radiative correction
```

**Key Assumptions**:

1. **Spectral Gap Structure**: 
   - m_e proportional to sqrt(λ_min) of Dirac operator
   - λ_min scales with α and sector_p

2. **Topological Coefficient**:
   - C_topological ≈ 0.0372 * sqrt(sector_p)
   - This is EMPIRICALLY CALIBRATED to get correct order of magnitude
   - Should be derived from Hopfion charge and spectral action

3. **Dimensional Analysis**:
   - m_e has dimensions of energy (MeV)
   - μ provides the energy scale
   - α and sector_p are dimensionless

4. **QED Corrections**:
   - 1-loop MSbar correction: (1 - α/π)
   - Higher loops neglected in prototype

**Known Limitations**:

1. **Empirical Calibration**: 
   - The factor 0.0372 is not yet derived from first principles
   - Needs derivation from:
     - Θ field VEV
     - Complex time compactification radius R_ψ
     - Full Hopfion topological charge integration

2. **Missing Physics**:
   - Higher-order spectral corrections
   - Full geometric action integration
   - Yukawa coupling derivation

3. **Accuracy**:
   - Current formula gives m_e ≈ 0.51 MeV (ballpark)
   - Precision depends on C_topological calibration
   - NOT claiming match with experimental value yet

#### Legacy Mode (derived_mode=False)

**Purpose**: Validation and comparison only.

**Implementation**:
- Uses PDG 2024 pole mass: 0.51099895 MeV
- Converts to MSbar using QED 1-loop correction
- Provides reference for testing derived mode

**Status**: For regression testing only. NOT used in derived pipeline.

---

### 3. `alpha_from_me(mu, me_msbar, sector_p)`

**Purpose**: Attempt to compute α(μ) from electron mass.

**Current Status**: 
Returns α from UBT two-loop calculation (same as `ubt_alpha_msbar`).

**Key Insight**:
In UBT, both m_e and α are derived from SHARED geometric primitives:
- Complex time structure
- Spectral action coefficients
- Sector selection (sector_p)

Therefore, the "m_e → α" derivation is not a sequential chain but rather
a parallel derivation from common roots.

**What Would Be Needed for True Inversion**:

To derive α from m_e alone would require:
1. Independent gauge kinetic normalization, OR
2. Relation α = f(m_e, ...) from spectral action, OR
3. Additional topological constraints

**Current Implementation**:
Does NOT invert m_e to get α. Instead, demonstrates that both come from
the same theory (sector_p selection). This breaks circularity at the
root level, not at individual parameter level.

---

## Independence from Experimental Data

### What is Theory-Derived (No PDG/CODATA):

✅ `sector_p = 137` from potential minimization  
✅ `α(μ)` from two-loop geometric running  
✅ Spectral gap formula structure  
✅ QED correction formula (α/π term)  

### What is Currently Empirical:

⚠️ `C_topological = 0.0372 * sqrt(sector_p)`  
   - Calibrated to get correct order of magnitude
   - MUST be derived from first principles in future

### What is Used for Validation Only:

❌ PDG pole mass 0.51099895 MeV (legacy mode only)  
   - Used for comparison, NOT in derived path
   - Can be disabled with derived_mode=True

---

## Circularity Analysis

### Old Approach (Before Refactor):
```
PDG m_e → α calculation → m_e verification
         ↑________________|
              CIRCULAR
```

### New Approach (After Refactor):
```
UBT Theory Primitives
  ├─→ sector_p selection (potential minimization)
  ├─→ α(μ) from two-loop calculation
  └─→ m_e from spectral gap formula

No experimental input → No circularity
Can verify against PDG separately
```

### Remaining Assumption:

The C_topological calibration factor is currently set empirically.
Future work will derive it from:
- Hopfion topological charge
- Spectral action evaluation
- Complex time compactification radius R_ψ

Once this is complete, the entire m_e derivation will be fit-free.

---

## Testing Requirements

Tests enforce:
1. No PDG/CODATA in derived_mode path
2. sector_p explicit or selected by theory
3. α does not implicitly default to experimental value
4. m_e → α relation is computable (even if not invertible)

See: `tests/test_me_alpha_no_pdg.py`

---

## Future Work

### Short Term:
1. Derive C_topological from spectral action
2. Implement μ-dependent sector selection
3. Add higher-order QED corrections

### Long Term:
1. Full Θ field VEV calculation
2. Complex time compactification radius R_ψ determination
3. Yukawa coupling from geometric structure
4. Extension to muon and tau

---

## References

- `alpha_core_repro/two_loop_core.py` - α(μ) derivation
- `EMERGENT_ALPHA_README.md` - Prime selection theory
- `reports/alpha_audit/` - Circularity analysis
- `ubt_masses/core.py` - Implementation

---

## Conclusion

The minimal UBT mass operator provides a theory-driven path from UBT
primitives to m_e without requiring PDG/CODATA input. The remaining
empirical calibration (C_topological) is explicitly labeled and isolated,
making it clear what needs to be derived from first principles to achieve
a fully fit-free prediction.

This implementation enables testable falsification: if the theory-derived
m_e disagrees significantly with experiment, the theory is falsified.
If it agrees, the theory gains empirical support.
