# Canonical Derivation — Lepton Ratios from Toroidal Eigenmodes

**Status**: MISMATCH DOCUMENTED  
**Version**: 2026-02-28

---

## 1. Definitions

We consider a Dirac operator on a two-torus `T²(τ)` with complex modular parameter
`τ = iy_*` (rectangular torus, purely imaginary modulus).

**Eigenfunctions** are labelled by integer pairs `(n, m) ∈ ℤ²`.

**Hosotani background**: For electric charge `Q = −1` and Wilson phase `θ_H = π`,
the Hosotani mechanism induces a shift `δ = ½` along the ψ-cycle (n-direction).

**Spin structure**: The shift along the φ-cycle (m-direction) is `δ' = 0`
(as implied by the table in Appendix W.T).

---

## 2. Eigenvalue Formula (Appendix W, eq. W.2, as written)

```
E_{n,m} = (1/R) √[ (n + δ)² + (m + δ')² ]
```

with `δ = 0.5`, `δ' = 0.0`.

**Note**: This formula does not include the torus modulus `y_*` explicitly.

---

## 3. Calibration (1 free parameter)

The single calibration is:

```
m_e ≡ E_{0,1}   →   R = E_{0,1} / m_e   (in natural units: R = 1/m_e)
```

This fixes `R` from the electron mass. No other free parameters.

---

## 4. Predictions (derived, no additional fits)

| Mode (n,m) | `E_{n,m} · R` | Lepton candidate | Predicted ratio to e |
|------------|---------------|------------------|----------------------|
| (0,1)      | 1.11803        | electron         | 1.000 (definition)  |
| (0,2)      | 2.06155        | muon (W.4)       | **1.844**            |
| (1,0)      | 1.50000        | tau (W.4)        | **1.342**            |
| (1,1)      | 1.80278        | tau alt. (W.4)   | **1.612**            |

**Predicted ratios (no additional fits):**

```
m_μ/m_e  ≡  E_{0,2}/E_{0,1}  =  1.844   (experimental: 206.768)
m_τ/m_μ  ≡  E_{1,0}/E_{0,2}  =  0.728   (experimental:  16.817)
```

---

## 5. Comparison with Claims and Experiment

| Ratio   | Predicted | Claimed (W.5) | Experimental | Status |
|---------|-----------|---------------|--------------|--------|
| m_μ/m_e | 1.844     | 207.3         | 206.768      | ❌ MISMATCH (factor ~112) |
| m_τ/m_μ | 0.728     | 16.9          | 16.817       | ❌ MISMATCH (wrong direction) |

---

## 6. Forensic Finding

The numbers 207.3 and 16.9 in Appendix W.5 and table W.T **cannot be derived** from
the eigenvalue formula stated in eq. W.2 of the same appendix, using the stated
parameters (δ=½, δ'=0) and at most one calibration (R = 1/m_e).

The mismatch is **two orders of magnitude** for the μ/e ratio, and the τ/μ ratio
is in the **wrong direction** (formula gives ratio < 1, i.e. E_{1,0} < E_{0,2}).

Hypotheses tested for the missing step (see `missing_step.md`):

1. Torus modulus y_* in rectangular formula → max ratio 2, cannot reach 207. ✗
2. Alternate modulus orientation → same problem. ✗
3. Power-law mass mapping → wrong direction for τ/μ. ✗
4. 3D torus mode labelling → not supported by appendix text. ✗

**Most likely explanation**: The table column "Ratio to E_{0,1}" in Appendix W.T
contains the experimental values (207.3, 3477) rather than values derived from the
formula. The derivation as written is incomplete and internally inconsistent.

---

## 7. What Would Be Needed

A complete, falsifiable derivation would require:

1. A corrected eigenvalue formula that explicitly includes the modular parameter `τ_*`
   from Appendix V and produces a closed-form expression for the lepton mass ratios.
2. A demonstration that this formula yields 207.3 and 16.9 without any additional
   free parameters beyond the single calibration `R = 1/m_e`.
3. A Python script (or analytic proof) that executes the derivation end-to-end.

Until these are provided, the claims of Appendix W remain **unsubstantiated**.

---

## 8. Locked Reference Values (for regression tests)

These are the values the formula **as written** produces.
Any future change to the formula must justify why these change.

```python
DELTA = 0.5
DELTA_PRIME = 0.0
E_01_R = 1.11803399   # sqrt(0.25 + 1.00)
E_02_R = 2.06155281   # sqrt(0.25 + 4.00)
E_10_R = 1.50000000   # sqrt(2.25 + 0.00)
E_11_R = 1.80277564   # sqrt(2.25 + 1.00)
RATIO_MU_E_FORMULA   = 1.84390889   # E_02/E_01
RATIO_TAU_MU_FORMULA = 0.72760688   # E_10/E_02
```
