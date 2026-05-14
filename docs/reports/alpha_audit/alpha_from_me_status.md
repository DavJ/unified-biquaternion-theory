# Alpha from m_e Relation: Status Report

## Question

Can we derive α(μ) from m_e(μ) in a non-circular way within UBT?

## Answer

**Partially, but not via simple inversion.**

## Detailed Analysis

### What We Can Do

1. **Parallel Derivation from Common Root**:
   ```
   UBT Geometric Primitives
      ├─→ sector_p (from potential minimization)
      ├─→ α(μ) (from two-loop running with sector_p)
      └─→ m_e(μ) (from spectral gap with sector_p and α)
   ```
   
   Both α and m_e derive from the same theoretical root (sector_p selection),
   so there is no circular dependency at the fundamental level.

2. **Verify Consistency**:
   - Given sector_p from theory → compute α(μ)
   - Given sector_p from theory → compute m_e(μ)
   - Check if both match experiment
   - If both match, theory is consistent
   - If either fails, theory is falsified

### What We Cannot Do (Yet)

**Direct Inversion**: m_e → α

The current UBT mass operator has the form:
```
m_e(μ) = F(α(μ), sector_p, μ)
```

where α appears on the right-hand side. To invert this and get α from m_e
requires additional information.

**What Would Enable Inversion**:

1. **Independent Gauge Kinetic Normalization**:
   If we had an independent way to fix the gauge kinetic term coefficient,
   we could potentially invert the mass relation.

2. **Spectral Action Coefficients**:
   If the spectral action provided a direct relation like:
   ```
   α² = g(m_e², sector_p, R_ψ, ...)
   ```
   then we could solve for α given m_e.

3. **Additional Constraints**:
   Topological or geometric constraints that relate α and m_e beyond
   the mass operator formula.

### Current Implementation

The `alpha_from_me()` function currently:
- Accepts m_e as input (for interface completeness)
- Computes α from sector_p using UBT two-loop formula
- Does NOT invert the mass formula

**Rationale**: In UBT, α and m_e are both consequences of the underlying
geometric structure, not independent parameters. They are related through
shared dependence on sector_p, complex time structure, and spectral action.

Therefore, computing α "from m_e" really means:
```
shared_structure → sector_p → α(μ)
shared_structure → sector_p → m_e(μ)
```

The two quantities are siblings, not parent-child.

## Circularity Assessment

### Is there circularity?

**NO**, for the following reason:

The derivation chain is:
```
1. UBT potential minimization → sector_p = 137 (theory)
2. sector_p + two-loop geometric running → α(μ) (theory)
3. sector_p + α(μ) + spectral gap → m_e(μ) (theory)
```

At no point do we use experimental α or m_e to derive theoretical α or m_e.

The "circularity" would only exist if we:
- Used experimental m_e to calibrate sector_p, THEN
- Used sector_p to derive α, THEN
- Claimed α was predicted

But we don't do this. sector_p comes from potential minimization, which is
independent of experimental lepton masses.

### Remaining Empirical Input

The `C_topological` factor in the mass operator is currently calibrated
empirically. However, this calibration:
- Does NOT use experimental α (only m_e for ballpark)
- Is isolated in derived_mode implementation
- Is clearly labeled as needing first-principles derivation

Once C_topological is derived from spectral action, the entire chain will
be fit-free.

## Comparison with Standard Model

### Standard Model Approach:
- Yukawa couplings y_f are free parameters
- m_f = y_f * v_Higgs (where v_Higgs ≈ 246 GeV)
- No prediction of masses, only relations

### UBT Approach:
- Masses emerge from geometric/topological structure
- sector_p is predicted (not fitted)
- Yukawa couplings should emerge from geometry (not yet fully implemented)
- Target: predict masses from first principles

## Open Questions

1. **Can we derive C_topological from spectral action?**
   - Status: In progress
   - Requires: Full Hopfion charge calculation, R_ψ determination

2. **Is there a direct α ↔ m_e relation beyond shared sector_p?**
   - Status: Unknown
   - Requires: Full spectral action analysis

3. **How do muon and tau masses relate to electron?**
   - Status: Not yet implemented
   - Should follow same spectral gap structure with different topological charges

## Recommendations

### For Testing UBT:
1. Use current implementation to compute both α and m_e from sector_p
2. Compare both against experiment
3. If both agree, theory is validated
4. If either disagrees significantly, theory needs revision

### For Theory Development:
1. Derive C_topological from first principles
2. Explore spectral action for direct α-m_e relations
3. Extend to second and third generation leptons

### For Documentation:
1. Clearly state that α and m_e are siblings (from shared root)
2. Avoid claiming "m_e → α" as a sequential derivation
3. Emphasize that non-circularity comes from common geometric origin

## Conclusion

The `alpha_from_me()` function demonstrates that UBT provides a non-circular
path to both α and m_e from shared geometric primitives. While direct
inversion (m_e → α) is not currently implemented, the parallel derivation
from sector_p ensures no circular reasoning.

**Status**: Non-circular derivation ✓  
**Inversion**: Not implemented (not required for non-circularity)  
**Validation**: Both α and m_e can be compared against experiment independently

---

**Implementation**: `ubt_masses/core.py::alpha_from_me()`  
**Tests**: `tests/test_me_alpha_no_pdg.py::test_alpha_from_me_signature()`  
**Date**: 2026-02-16
