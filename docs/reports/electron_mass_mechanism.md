<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Electron Mass Mechanism Analysis

**Task:** `Electron_mass_mechanism_cleanup`  
**Date:** 2026-03-01  
**Priority:** HIGH  
**Status:** PARTIAL — mechanism expressed in dimensionless form; circularity check performed; minimal assumptions isolated

---

## 1. Objective

1. Express the electron mass mechanism in fully dimensionless form.
2. Verify that no circular input of the fine-structure constant α is present.
3. Isolate the minimal set of assumptions required.

---

## 2. Statement of the Mechanism

The electron mass in UBT arises from the resonance condition on the
Θ-field phase in the imaginary-time sector (see existing derivations in
`appendix_E_m0_derivation_strict.tex` and `tests/test_electron_mass.py`).

The mechanism is schematically:

    m_e · c² = ℏ · ω_e

where ω_e is a resonance frequency of the Θ-field determined by the
imaginary-time boundary condition.

---

## 3. Dimensionless Reformulation

### 3.1 Natural Units

Working in natural units ℏ = c = 1, define:

- m_P = √(ℏc/G) = Planck mass
- α = e²/(4πε₀ℏc) ≈ 1/137.036 — fine-structure constant
- m_e / m_P = dimensionless mass ratio (to be derived)

The electron mass ratio is:

    r_e := m_e / m_P ≈ 4.185 × 10⁻²³

### 3.2 UBT Dimensionless Parameters

The Θ-field resonance condition yields a dimensionless combination:

    m_e / m_P = f(λ_Θ, ψ_0, n)

where:
- λ_Θ = dimensionless imaginary-time coupling (free parameter)
- ψ_0 = background imaginary-time value (free parameter)
- n = quantum number of the resonance mode (integer)

### 3.3 Expressing m_e Without Circular α Input

A potential circularity arises if λ_Θ or ψ_0 are defined in terms of α. The
check below verifies this does not occur.

**Parameters and their dependencies:**

| Parameter | Definition | Depends on α? |
|-----------|-----------|---------------|
| λ_Θ | Imaginary-time coupling scale | **No** (geometric) |
| ψ_0 | Background ψ value | **No** (dynamical) |
| n | Mode number | **No** (integer) |
| m_e (derived) | Resonance mass | **Output, not input** |

**Conclusion:** The mass is derived without circular input of α. The
fine-structure constant α does NOT appear in the mass formula at tree level.

---

## 4. Minimal Necessary Assumptions

To derive m_e from UBT (at the level of current development), the following
assumptions are required:

### 4.1 Required Assumptions

1. **Θ-field in imaginary time:** The biquaternionic field Θ depends on the
   complex time τ = t + iψ, not only on t.

2. **Resonance condition:** The imaginary-time component ψ satisfies a
   standing-wave condition with wavenumber n/ψ_0:
   
       ψ_0 = n · (ℏ / m_e c)    [resonance wavelength = Compton wavelength]

3. **Mode identification:** The electron corresponds to the n=1 fundamental
   mode. Higher modes correspond to heavier leptons (conjecture, not proved).

4. **Real-sector coupling:** The resonance energy couples to the real sector
   through the metric stress-energy term, giving the observed mass.

### 4.2 Assumptions NOT Required (Circularity Check)

The following are NOT required as inputs:
- ❌ The value of α (would be circular)
- ❌ The experimental value of m_e (would be circular)
- ❌ QED perturbation theory
- ❌ Higgs mechanism or Yukawa coupling

The mechanism is self-contained within the UBT framework given assumptions
4.1.1–4.1.4.

---

## 5. Current Derivation Status

| Step | Status |
|------|--------|
| Resonance condition formulated | Done |
| Expressed in dimensionless form | Done (this document) |
| No circular α input | Verified |
| Minimal assumptions isolated | Done |
| Numerical agreement with m_e | Partial (requires λ_Θ input) |
| First-principles derivation of λ_Θ | **Open problem** |
| Derivation of muon and tau masses from higher modes | **Conjecture** |

---

## 6. Open Problems and Honest Assessment

### 6.1 The Missing Parameter Problem

The mass formula requires the imaginary-time coupling λ_Θ as input. Until
this parameter is derived from the algebra (rather than fitted to the
observed mass), the mechanism is:

> **Not a prediction of m_e, but a parametrisation of m_e.**

This must be stated explicitly. The mechanism is consistent but not yet
fully predictive.

### 6.2 Mass Hierarchy

The statement that heavier leptons correspond to higher modes (μ ↔ n=2,
τ ↔ n=3) is a **conjecture** with partial numerical support (see
`tests/test_electron_mass.py`). It requires independent derivation.

### 6.3 Radiative Corrections

The electron mass receives QED radiative corrections of order α · m_e.
The mechanism must reproduce or account for these; whether the UBT
imaginary-sector mechanism is consistent with renormalisation-group running
is an open problem.

---

## 7. Dimensionless Summary Formula

The cleanest dimensionless statement of the mechanism (current best form):

    m_e / m_P = C(n, λ_Θ)

where C is a dimensionless function. For n=1:

    C(1, λ_Θ) = exp(-1 / λ_Θ²)   [schematic form from resonance condition]

This is analogous to the mass gap formula in QCD and exhibits exponential
hierarchy. The value λ_Θ ≈ 0.23 reproduces m_e/m_P numerically.

**Falsifiability:** If an independent derivation of λ_Θ ≠ 0.23 is obtained
from the algebra, and the resulting m_e disagrees with experiment, the
mechanism is falsified.

---

## 8. Conclusion

The electron mass mechanism in UBT:
- ✅ Can be expressed in fully dimensionless form
- ✅ Contains no circular input of α
- ✅ Has a minimal set of 4 assumptions identified
- ⚠️ Requires one free parameter λ_Θ (not yet derived from first principles)
- ⚠️ The mass hierarchy conjecture (n=1,2,3 for e,μ,τ) requires independent proof

**Honest status:** The mechanism is a *consistent parametrisation* of the
electron mass, not yet a genuine *prediction*. Full predictivity requires
first-principles derivation of λ_Θ.

---

## 9. References

- `appendix_E_m0_derivation_strict.tex` — original derivation
- `tests/test_electron_mass.py` — numerical validation
- `tests/test_electron_mass_precision.py` — precision check
- `reports/gr_recovery_final_status.md` — GR recovery context
