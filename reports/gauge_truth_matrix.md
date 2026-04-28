<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# gauge_truth_matrix.md — Brutally Honest Gauge Sector Truth Matrix

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Purpose**: Coldly accurate map of what is algebra, what is physics, what is
proved, what is open, what is speculative, and what is dead.
No hype.  Source: `reports/gauge_status_matrix.md` (detailed proof-level source).

---

## Reading This Document

This is the hostile-reviewer view of the gauge sector.  Every claim is
classified as either:

- **✅ PROVED** — formal theorem or algebraic identity; no free parameters
- **⚠️ CONDITIONAL** — proved if a named gap is solved
- **🔲 OPEN** — no proof; actively researched
- **🔴 DEAD END** — approach proved to fail; closed
- **🔵 DEFERRED** — out of scope for current paper; acknowledged

The column "Can claim in T2 paper?" answers: can this be stated as a theorem
(T), a motivated result (M), an open problem (O), or should it not be mentioned (X)?

---

## 1. Algebraic Foundation

| Claim | Verdict | Notes | Paper? |
|-------|---------|-------|--------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) | ✅ PROVED [L0] | Algebraic identity | T |
| ℂ⊗ℍ ≅ Cl₁,₃(ℝ) | ✅ PROVED [L0] | Algebraic identity | T |
| dim_ℝ(ℂ⊗ℍ) = 8 | ✅ PROVED [L0] | Definition | T |
| Aut(ℂ⊗ℍ) ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂ | ✅ PROVED [L0] | Algebraic | T |
| **No other 8-real-dim algebra gives SU(3)×SU(2)×U(1)** | ✅ PROVED [L0] | Uniqueness of ℂ⊗ℍ | T |

---

## 2. SU(3) — Colour Gauge Group

### What is proved

| Claim | Verdict | Source | Paper? |
|-------|---------|--------|--------|
| 𝔰𝔲(3) realised in ℂ⊗ℍ via ℤ₂×ℤ₂×ℤ₂ involutions | ✅ PROVED [L0] | `su3_from_involutions.tex` | T |
| Quarks in fundamental **3** | ✅ PROVED [L0] | `sm_gauge.tex §G.B` | T |
| Gluons in adjoint **8** (all 28 commutator pairs checked) | ✅ PROVED [L0] | `sm_gauge.tex §G.C` | T |
| EW/strong sector algebraic decoupling | ✅ PROVED [L0] | `sm_gauge.tex §G.D` | T |
| Independent triqubit derivation of SU(3) | ✅ PROVED [L0] | `su3_qubit_encoding.tex` | T |
| Structural colour confinement (free quarks algebraically inadmissible) | ✅ PROVED [L0]+exp. | `su3_from_involutions.tex Thm G.B` | T (distinguish from dynamical) |

### What is NOT proved

| Claim | Verdict | Notes | Paper? |
|-------|---------|-------|--------|
| **Dynamical confinement** (Wilson loop area law, mass gap) | 🔴 OPEN-HRD | Clay Millennium Problem | O (state as Millennium) |
| Strong coupling g_s from first principles | 🔲 OPEN | No approach | O |
| Strong CP problem (θ_QCD = 0) | 🔲 OPEN | Standard SM problem | O (note) |
| Quark-hadron duality, meson/baryon spectrum | 🔵 DEFERRED | Spectroscopy paper | X |

**Honest SU(3) summary**: The algebraic structure is proved.  Dynamical
properties are not proved — they involve the Clay Millennium mass-gap problem.
Do not conflate structural with dynamical confinement in the paper.

---

## 3. SU(2)_L — Weak Isospin

### What is proved

| Claim | Verdict | Source | Paper? |
|-------|---------|--------|--------|
| SU(2)_L from left norm-preserving action on Mat(2,ℂ) | ✅ PROVED [L0] | `sm_gauge.tex §SU2` | T |
| [T^a,T^b] = ε^{abc}T^c commutator algebra | ✅ PROVED [L0] | Standard | T |
| SU(2)_L acts on left-chiral doublets (Gap C1 closed) | ✅ PROVED [L1] | `chirality/step3_gap_C1_resolution.tex` | T |
| W±, W³ as gauge connections | ✅ PROVED [L1] | Gauge principle | T |

### What is NOT proved

| Claim | Verdict | Notes | Paper? |
|-------|---------|-------|--------|
| W± and Z boson masses from SSB | 🔵 DEFERRED | Higgs paper | O (note) |
| **SU(2)_R excluded by UBT dynamics** (stronger chirality claim) | ⚠️ CONDITIONAL | Gap C1 resolution argues P_ψ-odd; not a full dynamical proof | M (motivated) |

---

## 4. U(1)_Y — Hypercharge

### What is proved

| Claim | Verdict | Source | Paper? |
|-------|---------|--------|--------|
| U(1)_Y from right scalar phase action on Mat(2,ℂ) | ✅ PROVED [L0] | `sm_gauge.tex §U1` | T |
| U(1)_Y generator = (1/2)I | ✅ PROVED [L0] | Representation theory | T |
| Hypercharge quantisation from Dirac condition on ψ-circle | ✅ PROVED [L0] | `appendix_alpha_geometry.tex §1` | T |

### What is NOT proved

| Claim | Verdict | Notes | Paper? |
|-------|---------|-------|--------|
| Specific fermion hypercharge assignments | 🔲 OPEN (Gap C2) | No derivation of Q_u = 2/3, Q_d = -1/3 etc. | O |

---

## 5. U(1)_EM — Electromagnetism

| Claim | Verdict | Source | Paper? |
|-------|---------|--------|--------|
| U(1)_EM from ψ-cycle phase after SSB | ✅ PROVED [L0] | `qed.tex` | T |
| Q = T₃ + Y/2 (Gell-Mann–Nishijima) | ✅ PROVED [L1] | Standard EW algebra | T |
| Photon field A_μ = sin θ_W W³_μ + cos θ_W B_μ | ✅ PROVED [L1] | Standard EW | T |

---

## 6. Electroweak Mixing — THE CRITICAL GAP

| Claim | Verdict | Notes | Paper? |
|-------|---------|-------|--------|
| e = g sin θ_W identity | ✅ PROVED [L1] | Standard EW algebra | T (background) |
| **Weinberg angle sin²θ_W ≈ 0.231 from UBT** | 🔴 **DEAD END** | Algebra alone cannot fix g/g'; see below | **O (explicit dead-end §6)** |
| SSB pattern SU(2)_L × U(1)_Y → U(1)_EM | ⚠️ CONDITIONAL [MC] | Pattern is motivated; not derived | M |
| Higgs doublet from S[Θ] (Gap EW-2) | 🔲 OPEN | Θ₀ VEV as doublet unproved | O |

### Dead-End Statement for Paper (copy into §6)

> **Gap EW (dead end)**: The biquaternion algebra $\mathbb{C}\otimes\mathbb{H}$
> contains both SU(2)_L and U(1)_Y as subgroups, but does not fix the ratio
> $g'/g = \tan\theta_W$ of their coupling constants.  The two couplings $g$
> and $g'$ appear as independent parameters in any Lagrangian on
> $\mathbb{C}\otimes\mathbb{H}$.  No purely algebraic argument has been found
> to enforce $\sin^2\theta_W = 0.231$, and a no-go argument suggests none exists:
> the algebra admits continuous deformations of the SU(2)_L × U(1)_Y embedding
> that change $\tan\theta_W$ continuously.  The Weinberg angle is therefore
> a semi-empirical input in UBT at this stage.

---

## 7. Three Generations

| Claim | Verdict | Source | Paper? |
|-------|---------|--------|--------|
| N_gen = 3 from dim_ℝ(Im ℍ) = 3 | ✅ PROVED [L0] | `DERIVATION_INDEX.md §ψ-modes` | T |
| Three ψ-modes carry identical gauge quantum numbers | ✅ PROVED [L0] | `su3_proof_status.md §Three generations` | T |
| Mass hierarchy between generations | 🔲 OPEN-HRD | KK obstruction theorem | O (note proved impossibility of torus approach) |

---

## 8. Higgs and Symmetry Breaking

| Claim | Verdict | Notes | Paper? |
|-------|---------|-------|--------|
| Higgs boson from Θ-field VEV | 🔲 OPEN | No derivation | O (defer) |
| Higgs mass 125 GeV | 🔲 OPEN | No derivation | X (don't mention) |
| Quartic coupling λ | 🔴 CANDIDATE failed | Off by ×11 vs SM | O (note discrepancy) |

---

## 9. Fermion Masses and Yukawa

| Claim | Verdict | Notes | Paper? |
|-------|---------|-------|--------|
| Yukawa coupling matrix y_ij | 🔲 OPEN (Gap Y2) | No derivation | O (defer) |
| e/μ/τ masses | 🔲 OPEN-HRD | KK-mismatch theorem proved | O (state proved impossibility of torus approach) |
| CKM/PMNS mixing matrices | 🔲 OPEN | No derivation | X (don't mention in T2 paper) |

---

## 10. Anomaly Cancellation

| Claim | Verdict | Notes | Paper? |
|-------|---------|-------|--------|
| U(1)_Y³ anomaly cancelled | ⚠️ CONDITIONAL [MC] | Follows if SM reps assumed | O (verify or state open) |
| [SU(2)_L]² U(1)_Y anomaly cancelled | ⚠️ CONDITIONAL [MC] | Follows if SM reps assumed | O (verify or state open) |
| **Anomaly cancellation from UBT first principles** | 🔲 OPEN | No proof; reps partially assigned | O |

---

## 11. Quantitative Gap Summary

### Chirality Gap

| What is needed | Current status | Gap | Weeks to close |
|----------------|---------------|-----|----------------|
| SU(2)_L is left-chiral (W couples to L doublets) | [L1] with P_ψ-odd argument (Gap C1 closed) | None | 0 |
| Dynamical exclusion of SU(2)_R | [MC] — motivated | C1b | 4–6 |

### Anomaly Gap

| What is needed | Current status | Gap | Weeks to close |
|----------------|---------------|-----|----------------|
| All SM gauge anomalies cancelled | [MC] conditional | Verify UV completion | 4–8 |
| Anomaly cancellation proved from UBT algebra | [OPEN] | Hard — fermion assignments missing | >12 |

### Higgs/Yukawa Dependency

| What is needed | Current status | Gap |
|----------------|---------------|-----|
| Higgs mechanism for W/Z masses | [OPEN] | EW-2 |
| Yukawa couplings | [OPEN] | Y2 |
| Fermion hypercharges | [OPEN] | C2 |

All three Higgs/Yukawa items are **deferred to a separate paper**.

---

## 12. T2_GAUGE Paper Readiness

### What can be stated as theorems (zero new work needed)

1. ℂ⊗ℍ ≅ Mat(2,ℂ) — algebraic foundation
2. 𝔰𝔲(3) via ℤ₂×ℤ₂×ℤ₂ (Theorems G.A–G.D)
3. Quarks in **3**, gluons in **8**, EW/strong decoupling
4. Triqubit confirmation of SU(3)
5. Structural colour confinement
6. SU(2)_L from left norm-preserving action
7. U(1)_Y from right scalar phase
8. U(1)_EM from ψ-cycle phase
9. Three generations from ψ-winding modes
10. Hypercharge quantisation from Dirac condition
11. SU(2)_L chirality (left-chiral coupling, Gap C1 resolved)

### What must be stated as open or dead-end

| Result | Honest statement in paper |
|--------|--------------------------|
| Weinberg angle θ_W | **Dead end: algebra cannot fix g'/g** (explicit §6) |
| W/Z masses from SSB | Defer to Higgs paper |
| Fermion masses | Defer; note KK-mismatch theorem |
| Dynamical confinement | Clay Millennium problem |
| Strong coupling g_s | Open problem |
| Anomaly cancellation from first principles | Open — requires fermion hypercharge assignments |

---

## 13. Overall T2_GAUGE Verdict

**Readiness without chirality C1b**: 80%  
**Readiness with C1b closed**: 88%  
**Readiness with anomaly check**: 90%  
**Readiness with EW/Higgs gaps**: Not in scope for T2 paper (deferred)

**Submission verdict**: T2_GAUGE is submittable now with honest dead-end
statements on Weinberg angle and deferred statements on Higgs/Yukawa.
The algebraic SU(3) × SU(2)_L × U(1)_Y emergence result is strong.

---

## References

- `reports/gauge_status_matrix.md` — detailed proof-level source (longer version)
- `canonical/interactions/sm_gauge.tex` — primary canonical gauge source
- `canonical/su3_derivation/` — SU(3) source files
- `canonical/chirality/` — chirality sector
- `reports/chirality_gap.md` — Gap C1 detail
- `reports/anomaly_gap.md` — anomaly gap detail
- `reports/higgs_yukawa_dependency.md` — Higgs/Yukawa gap detail
- `reports/ew_mixing_status.md` — electroweak mixing status
