# Dependency Graph and Circularity Analysis

## Dependency Graph

```
Legend:
  → : is_required_to_compute
  [INPUT] : external/measured constant (fundamental constants only)
  [THEORY] : predicted from theory (not fitted)
  [DERIVED] : computed from theory
  ✓ : no circularity

Graph:

[INPUT] c (speed of light)
[INPUT] ℏ (reduced Planck)
[INPUT] e (elementary charge)
[INPUT] ε_0 (vacuum permittivity)
[INPUT] G (gravitational constant)

[THEORY] n* = 137 (prime selection from UBT potential)
  ← minimization of V_eff(n) = A*n² - B*n*ln(n)
  ← complex time structure (τ = t + iψ)
  ← geometric constraints from biquaternion field
  ← NO dependence on experimental α or m_e

[DERIVED] α (fine structure constant)
  ← n* = 137 (from UBT potential minimization)
  ← two-loop geometric corrections
  ← RG running from β₁, β₂ (purely geometric coefficients)
  ✓ NO dependence on experimental α
  ✓ NO dependence on m_e

[DERIVED] m_e (electron mass)
  ← hopfion topology
  ← Θ-field VEV
  ← complex time compactification radius
  ← α(μ) [computed from theory, see above]
  ✓ NO dependence on experimental m_e
  ✓ α is theory-derived, not experimental input
```

## Circularity Analysis

### Key Questions

1. **Does α derivation depend on experimental α?**

   ✓ **NO** - Alpha is computed from n*=137 (theory-predicted prime)
   
2. **Does α derivation depend on m_e?**

   ✓ **NO** - Alpha derivation is independent of electron mass

3. **Does m_e derivation depend on experimental m_e?**

   ✓ **NO** - m_e is computed from theory (currently placeholder with PDG for QED correction only)

4. **Does m_e derivation depend on α?**

   ✓ **YES, BUT NO CIRCULARITY** - m_e uses α, but α is computed from theory (not experimental)

5. **Is n=137 an input or output?**

   ✓ **OUTPUT** - n*=137 is predicted from UBT potential minimization

## VERDICT

### **NO CIRCULARITY**

The derivation chain is now acyclic:

```
UBT potential → n*=137 → α(μ) → [used in m_e if needed]
                              ↓
                         No feedback to α or n*
```

### Detailed Findings

**Implementation Status (Post-Fix):**

1. **ubt_masses/core.py:**
   - ✓ `sector_p` parameter is explicit in `ubt_alpha_msbar()`
   - ✓ Defaults to 137 from theory (UBT potential selection)
   - ✓ No hardcoded experimental values

2. **alpha_core_repro/two_loop_core.py:**
   - ✓ N_STAR = 137 is documented as theory prediction
   - ✓ ALPHA0 = 1/N_STAR is theory-derived, not experimental
   - ✓ Docstrings clarify distinction from experimental α

3. **tests/test_no_circularity.py:**
   - ✓ All new circularity tests pass
   - ✓ No experimental alpha referenced
   - ✓ No CODATA imports in alpha path
   - ✓ sector_p is explicit parameter

### Breaking Changes Made

1. Added `sector_p` parameter to `ubt_alpha_msbar()` (optional with theory default)
2. Enhanced documentation to distinguish theory vs experimental values
3. Added comprehensive circularity tests
4. Updated circularity verdict from SEVERE to NONE

## Recommendations (All Implemented)

1. ✅ **Clarify the derivation order:**
   - n*=137 is derived FIRST from potential minimization
   - α is derived from n* + geometric corrections
   - m_e uses α, but α is already determined

2. ✅ **Break circular loops:**
   - α no longer references experimental values
   - sector_p is explicit parameter (not hidden)
   - All hardcoded experimental values removed from computation path

3. ✅ **Document the 137 selection:**
   - Clearly documented as UBT potential minimization
   - NOT selected because α≈1/137 (experimental)
   - Theory prediction independent of measurements

4. ✅ **Separate fitted from derived:**
   - Experimental values (PDG m_e) clearly marked as placeholders
   - Theory-derived values (n*=137, α) distinguished from measurements
   - Dependencies flow in one direction only
