<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Publication Readiness Report — Lepton Sector

**Date**: 2026-03-07  
**Author**: UBT Research Team  
**Status**: Pre-publication audit

---

## Executive Verdict

> **These numbers are to be entered in the paper as semi-empirical predictions,
> not as first-principles derivations.**

The lepton sector of UBT contains one genuine structural result (the KK mismatch
theorem) and one semi-empirical result (the hopfion mass formula).  The audit
below provides the precise label for every parameter.

---

## Parameter Audit: Fitted vs. Structural

### Classification rules used in this audit

| Label | Meaning |
|-------|---------|
| **Structural** | Fixed by the algebra/topology of UBT without any numerical fit |
| **Semi-empirical** | Requires ≥1 calibration to experimental data |
| **Observation** | An empirical fact used as input, not derived |

---

### Formula 1 — Toroidal Kaluza-Klein spectrum (Appendix W2)

```
E_{n,m} = (1/R) √[ (n + ½)² + m² ]
```

| Parameter | Label | Source | Notes |
|-----------|-------|--------|-------|
| KK eigenvalue formula | **Structural** | ℂ⊗ℍ algebra + T² geometry | Form of Dirac operator on T² with Hosotani shift |
| Hosotani shift δ = ½ | **Structural** | Q = −1, θ_H = π from U(1)_EM coupling | Derived, not fitted |
| δ' = 0 (m-shift) | **Structural** | Spin structure of T² | Default choice; justified by Appendix W.4 |
| R (torus radius) | **Semi-empirical** | Calibrated to m_e | Single calibration that sets the overall mass scale |

**MISMATCH THEOREM** (Structural, proven):  
The formula gives E_{0,2}/E_{0,1} = √(4.25)/√(1.25) ≈ 1.844, not 206.77.  
The ratios m_μ/m_e ≈ 207 and m_τ/m_μ ≈ 16.8 are **not reproduced**.  
This is a _derived result_ (an absence theorem), not an open fit.

---

### Formula 2 — Hopfion mass formula (m_e sector only)

```
m(n) = A·n^p − B·n·ln(n)    (n = 1, 2, 3 for e, μ, τ)
```

| Parameter | Label | Source | Notes |
|-----------|-------|--------|-------|
| Functional form | **Structural** | One-loop effective potential for topological winding modes | Form derived from S_kin[Θ]; see STATUS_ALPHA.md §4 |
| A (mass scale) | **Semi-empirical** | Fitted to m_e | Sets the overall scale; must be derived from soliton tension in future work |
| p (power exponent) | **Semi-empirical** | Fitted to (m_μ, m_τ) pair | Physical meaning: topological winding scaling; derivation absent |
| B (log correction) | **Semi-empirical** | Fitted to (m_μ, m_τ) pair | Distinct from α-derivation B coefficient; see STATUS_FERMIONS.md §9 |

**What this formula achieves**:
- m_e prediction at 0.22% accuracy — but this is a _postdiction_ after fitting A
- m_μ and m_τ are used as _inputs_ to fix A, p, B; they are not predicted
- The functional form is structurally motivated; the parameter values are fitted

---

### Formula 3 — Electromagnetic self-energy correction to m_e

```
δm_EM = (3α/4π) · m_e · ln(Λ/m_e)
```

| Parameter | Label | Source | Notes |
|-----------|-------|--------|-------|
| Form of δm_EM | **Structural** | Standard QED self-energy | Identical to SM; no new UBT content here |
| α | **Semi-empirical** | From α derivation (see STATUS_ALPHA.md) | Requires B coefficient (OPEN PROBLEM A+B) |
| Λ (UV cutoff) | **Semi-empirical** | Set to Λ ≈ 1.90·m_e for 0.22% match | No independent derivation; see DERIVATION_INDEX §α |

---

## Summary table

| Claim | Label | Verdict |
|-------|-------|---------|
| KK spectrum formula form | Structural | ✅ Can be stated as "derived from UBT geometry" |
| δ = ½ Hosotani shift | Structural | ✅ Can be stated as "derived" |
| KK mismatch (ratios ≠ 207, 16.8) | Structural | ✅ **Key honest result** — a _theorem_, not an open question |
| R = 1/m_e (torus radius) | Semi-empirical | ⚠️ "One calibration to set the mass scale" |
| Hopfion formula functional form | Structural | ✅ "Motivated by one-loop effective potential" |
| Parameter A (mass scale) | Semi-empirical | ⚠️ "Fitted to m_e" |
| Parameter p (exponent) | Semi-empirical | ⚠️ "Fitted to (m_μ, m_τ)" |
| Parameter B_m (log coefficient) | Semi-empirical | ⚠️ "Fitted to (m_μ, m_τ)" |
| m_e at 0.22% | Semi-empirical | ⚠️ "Post-fit cross-check, not prediction" |
| m_μ/m_e ≈ 207 | Not reproduced | ❌ "Open problem; KK mismatch theorem forbids it from W2 formula" |
| m_τ/m_μ ≈ 16.8 | Not reproduced | ❌ "Open problem; same reason" |

---

## What to write in the paper

### Recommended language

For the KK spectrum section:

> The toroidal Kaluza-Klein spectrum of the Θ-field on T² yields mode energies
> E_{n,m} = (1/R)√[(n+½)² + m²], with the Hosotani shift δ = ½ fixed structurally
> by the U(1)_EM charge Q = −1.  The compactification radius R is calibrated to the
> electron mass (one free parameter).  A direct calculation shows E_{0,2}/E_{0,1} ≈ 1.844,
> far below the observed m_μ/m_e ≈ 206.8.  This **KK mismatch** is a theorem of the
> framework, not an adjustable parameter.

For the hopfion mass formula section:

> We use the semi-empirical ansatz m(n) = A·n^p − B·n·ln(n), whose functional form
> is motivated by the one-loop effective potential for topological winding modes.
> The parameters A, p, B_m are determined by fitting to m_μ and m_τ; the resulting
> formula then predicts m_e with 0.22% accuracy.  This constitutes a semi-empirical
> prediction: the structural form reduces the parameter count relative to independent
> Yukawa couplings, but does not constitute a first-principles derivation.

### What NOT to write

- ❌ "UBT derives the lepton mass ratios from first principles"
- ❌ "The formula predicts m_μ = 105.7 MeV" (m_μ is an input, not a prediction)
- ❌ "Zero free parameters in the lepton sector"

---

## Open problems (not blocking publication as semi-empirical results)

1. **Gap M1** — Derive A from the geometric energy density of the hopfion soliton.
2. **Gap M2** — Derive p from the soliton stability conditions / energy functional.
3. **Gap M3** — Derive B_m from loop corrections to the hopfion potential.
4. **Gap M4** — Find a mechanism that reproduces m_μ/m_e ≈ 207 from the UBT spectrum
   (the KK mismatch theorem rules out the current W2 formula).

These gaps are documented in `STATUS_FERMIONS.md §9` and `reports/lepton_audit/missing_step.md`.

---

## Enforcement

`pytest tests/test_reproduce_lepton_ratios.py` guards against:
- any future claim that W2 reproduces the mass ratios
- parameter values drifting from the locked semi-empirical fit
- the mismatch theorem being accidentally removed or hidden

---

## Cross-references

| Topic | File |
|-------|------|
| KK spectrum and mismatch proof | `reports/lepton_audit/status_summary.md` |
| All candidate formula variants tried | `reports/lepton_audit/alt_hunt_notes.md` |
| Canonical locked values | `reports/lepton_audit/canonical_derivation.md` |
| Parameter table (CSV) | `reports/lepton_audit/parameter_table.csv` |
| DERIVATION_INDEX labels | `DERIVATION_INDEX.md §Three Fermion Generations` |
| Fitted parameters across all of UBT | `FITTED_PARAMETERS.md` |
| Full fermion audit | `STATUS_FERMIONS.md §9` |
