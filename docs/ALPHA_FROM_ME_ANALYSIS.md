<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# ALPHA_FROM_ME_ANALYSIS.md — Derivation of α from the Fixed Point m_e = m_0/α

**Status: [HYPOTÉZA — second route, does not use V_eff]**

---

## 1. Context and Motivation

The primary UBT route to α (energy minimisation of V_eff) is currently blocked:
- B₀ = 2π·N_eff/3 = 25.1 [DERIVED]
- B_base = N_eff^{3/2} = 41.57 [NO DERIVATION — 3 methods failed]
- With B₀ the minimum gives n*≈67, not 137.

A second independent route was identified, based on the fixed point:

```
α = m_0 / (n* · m_e)
```

Numerically: 0.509856 / (137 × 0.510999) = 0.007283 = 1/137.307
Error: 0.197% — exactly matches the 0.22% imprecision of the m_0 derivation.

This file documents the analysis of this second route.

---

## 2. Key Numerical Values

| Quantity | Value | Status |
|---|---|---|
| `m_0` | 0.509856 MeV | [CALIBRATED — parameter A from fermion mass formula] |
| `m_e` | 0.510999 MeV | [PDG — experimental] |
| `n*` | 137 | [TOPOLOGICAL INPUT — prime winding number] |
| `Δm = m_e − m_0` | 1.143 keV | [COMPUTED] |
| `Δm/m_e` | 0.002237 | [COMPUTED] |
| `α/2π` | 0.001161 | [COMPUTED — cf. Δm/m_e ≈ 2×(α/2π)] |
| `α_exp` | 1/137.035999177 | [CODATA 2022] |
| `α from fixed point` | 0.509856/(137×0.510999) = 1/137.307 | [COMPUTED — 0.197% error] |

---

## 3. Fixed Point Relationship

From appendix_E_m0_derivation_strict.tex §E.5:

```
m_e = m_0 / α(m_e)     [NÁČRT — stationarity conditions unsolved without α as input]
```

Rearranged: `α = m_0 / m_e` (if m_0 is independent of m_e).

**Circular logic check:**
- `m_0` = 0.509856 MeV is currently [CALIBRATED] to the fermion mass formula (μ,τ fitted)
- The formula predicts m_e with 0.22% error — NOT fitted to m_e
- Therefore `m_0` is NOT a circular input with respect to `m_e`

The formula `α = m_0/(n*·m_e)` involves:
- n* = 137: [TOPOLOGICAL INPUT] — prime winding number from V_eff, accepted as given
- m_e: [PDG] — experimental input
- m_0: [CALIBRATED] — from μ,τ masses; independent of m_e

**Assessment:** 0.197% error is consistent with the known imprecision in m_0.
If m_0 is derived independently (see §4–5), the error would improve.

---

## 4. Gap Analysis: m_e − m_0 = 1.143 keV

### 4.1 Comparison with QED radiative correction

QED one-loop mass correction:
```
δm_QED = (3α/4π) · m_e · ln(Λ²/m_e²) = (3α/2π) · m_e · ln(Λ/m_e)
```

For each natural UBT UV cutoff at `α = α_exp`:

| Cutoff Λ | Motivation | δm_QED | Factor vs Δm |
|---|---|---|---|
| `n*·m_e = 137·m_e` | KK tower at winding n* | 8.76 keV | ×7.66 |
| `m_e/α` (classical radius) | 1/r_e | 8.76 keV | ×7.66 |
| `m_e/√α` | geometric mean | 4.38 keV | ×3.83 |
| `2·m_e` (pair threshold) | pair creation | 1.23 keV | ×1.08 |

None equals Δm = 1.143 keV exactly, but the pair threshold is closest (8% off).

### 4.2 Required cutoff

Inverting the QED formula for δm = Δm:
```
ln(Λ/m_e) = 0.6420  →  Λ/m_e = 1.900  →  Λ ≈ 971 keV
```

This cutoff lies between m_e (511 keV) and 2m_e (1022 keV — pair threshold).
It is NOT a recognised independent UBT geometric scale.

---

## 5. Self-Consistency Equation (Task 1 results)

From appendix_E_m0_derivation_strict.tex §E.8, the self-consistency equation is:

```
n*·α + g(α) = 1,   g(α) = (3α/2π)·ln(Λ/m_e)
```

Results from `tools/alpha_selfconsistency.py`:

| Cutoff | α_sol | 1/α_sol | Error% | Status |
|---|---|---|---|---|
| `n*·m_e` | 0.00717622 | 139.349 | 1.660% | DEAD END |
| `m_e/α` | 0.00717580 | 139.357 | 1.666% | DEAD END |
| `m_e/√α` | 0.00723712 | 138.177 | 0.825% | PARTIAL (<1%) |
| `2·m_e` | 0.00728168 | 137.331 | 0.215% | BEST — but m_e is input |

**Item 4 update (from original analysis):**
- `pair_threshold` (Λ = 2·m_e) gives α ≈ 1/137.33 with 0.215% error
- Error matches 0.22% systematic of m_0 — suggestive but NOT a proof
- Cutoff uses m_e directly → NOT an independent derivation of α
- `sqrt_alpha` cutoff (Λ = m_e/√α) gives 0.825% error — best "purely algebraic" cutoff

**Overall assessment:**
The self-consistency equation does not have a solution within 1% of α_exp for
any natural UBT scale that is independent of m_e.

Classification: **[HYPOTÉZA]**

What would confirm it: derivation of Λ ≈ 1.90·m_e (971 keV) from UBT geometry
without reference to m_e or α.

---

## 6. Torus Geometry Route (Task 2 results)

### 6.1 α as Output of Stationarity

From `tools/m0_from_torus.py` and appendix_E §E.4 (reformulated):

With `U_geom = −C/(R_t·R_ψ)` (Form A, simplest attractive curvature):
```
α_predicted = C/(2A·n²)    [DERIVED — stationarity without α as input]
```

For n=1: `α_predicted = C/(2A)`.
For `α_predicted = α_exp`: requires `C/A = 2·α_exp = 0.01460`.

This is a **prediction for the curvature-to-kinetic ratio** C/A from experiment.
Computing C from `ℒ_geom` (via `canonical/geometry/biquaternion_curvature.tex`)
would close the argument. Currently: **[SKETCH]**.

**m_0 prediction:** Cell energy at the minimum for n=1 is zero → trivial m_0 = 0.
An independent dimensionful scale is required. **[DEAD END for n=1]**

### 6.2 Independent Fixation of R_ψ (Task 3 results)

From `canonical/geometry/biquaternionic_vacuum_solutions.tex §2`:

**Topological condition tested:**
Winding consistency on the ψ-circle with winding n* requires:
```
R_ψ = k·ℏ/(n*·m_e·c)   for integer k
```

- For k=1: R_ψ = ℏ/(137·m_e) → Λ_ψ = 137·m_e → α = m_0/(n*²·m_e) ≈ 1/137² (too small)
- For k=n*: R_ψ = ℏ/m_e (recovers original identification)

**Conclusion:** No topological condition fixes R_ψ independently of m_e.
The identification R_ψ = ℏ/(m_e·c) is **[KALIBROVÁNO — necessary for consistency,
not derivable from pure geometry in current theory]**.

---

## 7. Overall Assessment

| Route | Formula | Error | Status |
|---|---|---|---|
| Primary (V_eff minimum) | α⁻¹ = n* = 137 | 0.026% | BLOCKED (B_base missing) |
| Second route (fixed point) | α = m_0/(n*·m_e) | 0.197% | CALIBRATED (m_0 not independent) |
| Self-consistency (Task 1) | n*·α + g(α) = 1 | 0.215% (best) | HYPOTHESIS (Λ uses m_e) |
| Torus geometry (Task 2) | α = C/(2A) | requires C/A | SKETCH (C from ℒ_geom pending) |

**The circular-logic test:** None of the approaches currently derives α with
zero circular inputs. The primary route needs B_base; the second and third routes
use m_e (directly or via m_0); the torus route needs C from ℒ_geom.

---

## 8. What Would Constitute a Genuine Derivation

For α to be classified as [DERIVED]:
1. n* = 137 must be derived from V_eff (requires B_base from ℒ_geom) **OR**
2. The self-consistency equation must be satisfied with Λ derived independently **OR**
3. α_predicted = C/(2A) must be confirmed with C computed from ℒ_geom

None of conditions 1–3 is currently satisfied.

---

## References

- `appendix_E_m0_derivation_strict.tex` §E.5, §E.8
- `STATUS_ALPHA.md` §4–5
- `STATUS_FERMIONS.md` §2.1
- `tools/alpha_selfconsistency.py`
- `tools/m0_from_torus.py`
- `canonical/geometry/biquaternionic_vacuum_solutions.tex §2`
- `docs/DERIVATION_INDEX.md`

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
