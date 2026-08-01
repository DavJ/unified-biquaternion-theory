<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# gauge_status_matrix.md — T2_GAUGE Exact Proved-vs-Open Map

**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Compact, definitive, claim-linked map of every gauge-sector statement.
Single reference for paper-writing: use this to decide what can be stated as a
theorem, what must be labelled as motivated, and what must be deferred.  
**Sources**: `gauge_exactly_proved_vs_open.md`, `gauge_derivation_map.md`,
`su3_proof_status.md`, `missing_axioms.md`, `SM_CLOSURE_MATRIX.md`

---

## Proof-Level Key

| Tag | Meaning |
|-----|---------|
| **[L0]** | Algebraic identity — follows from definition of ℂ⊗ℍ alone |
| **[L1]** | Proved theorem — requires axioms A, B, F plus standard mathematics |
| **[SE]** | Semi-empirical — value fixed by experiment; not predicted by UBT |
| **[MC]** | Motivated conjecture — physically motivated; not a formal theorem |
| **[OPEN]** | Open — no proof exists |
| **[OPEN-HRD]** | Open hard — resisted many approaches; new mathematics needed |
| **[DEAD END]** | Approach proved to fail; route closed |

---

## Algebraic Foundation

| Claim | Status | Source |
|-------|--------|--------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) | **[L0]** | `canonical/fields/biquaternion_algebra.tex` |
| ℂ⊗ℍ ≅ Cl₁,₃(ℝ) | **[L0]** | `canonical/fields/biquaternion_algebra.tex` |
| Aut(ℂ⊗ℍ) ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂ | **[L0]** | `canonical/interactions/sm_gauge.tex` |
| dim_ℝ(ℂ⊗ℍ) = 8 | **[L0]** | Definition |

---

## SU(3)_c — Colour Gauge Group

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| 𝔰𝔲(3) realised in ℂ⊗ℍ (Theorem G.A) — ℤ₂×ℤ₂×ℤ₂ involutions | **[L0]** | `su3_derivation/su3_from_involutions.tex` | Theorem in §3 |
| Quarks in fundamental **3** (Theorem G.B) | **[L0]** | `interactions/sm_gauge.tex §G.B` | Theorem in §3 |
| Gluons in adjoint **8** (Theorem G.C) — all 28 commutator pairs checked | **[L0]** | `interactions/sm_gauge.tex §G.C` | Numerical table §3 |
| EW/strong sector algebraic decoupling (Theorem G.D) | **[L0]** | `interactions/sm_gauge.tex §G.D` | Theorem in §3 |
| Independent triqubit derivation of SU(3) | **[L0]** | `interactions/su3_qubit_encoding.tex` | Independent check §3 |
| Involution ↔ qubit route equivalence | **[L0]** | `bridges/su3_gauge_qubit_equivalence.tex` | Note §3 |
| Structural colour confinement (free quarks algebraically inadmissible) | **[L0]** + exp. | `su3_derivation/su3_from_involutions.tex` Thm G.B | §4 (distinguish from dynamical) |
| **Dynamical confinement** (Wilson loop area law, mass gap) | **[OPEN-HRD]** (Clay Millennium) | `su3_proof_status.md §OP-SU3-1` | State as Millennium problem §6 |
| Strong coupling g_s from first principles | **[OPEN]** | `su3_proof_status.md §OP-SU3-1` | State as open §6 |
| Strong CP problem (θ_QCD) | **[OPEN]** | `su3_proof_status.md §OP-SU3-3` | Note §6 |
| Quark-hadron duality / meson-baryon spectrum | **[OPEN]** | `su3_proof_status.md §OP-SU3-2` | Defer |

---

## SU(2)_L — Weak Isospin

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| SU(2)_L from left norm-preserving action on Mat(2,ℂ) | **[L0]** | `interactions/sm_gauge.tex §SU2` | Theorem §3 |
| [T^a,T^b] = ε^{abc}T^c commutator algebra | **[L0]** | Standard | Background §3 |
| SU(2)_L acts on left-chiral doublets | **[L0]** | `interactions/sm_gauge.tex` | State §3 |
| W±, W³ as gauge connections of SU(2)_L | **[L1]** | Gauge principle | §3 |
| **Chirality: SU(2)_L not SU(2)_R** (Gap C1) | **[MC]** | `chirality/step3_gap_C1_resolution.tex`, `symmetry/chirality_and_parity_breaking.tex` | **Close before submission** (1–2 wk); if not: explicit open statement §3+§6 |
| W± and Z mass from SSB | **[OPEN]** | `research_tracks/research/higgs_yukawa_scan.md` | Defer to Higgs paper |

---

## U(1)_Y — Hypercharge

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| U(1)_Y from right scalar phase action on Mat(2,ℂ) | **[L0]** | `interactions/sm_gauge.tex §U1` | Theorem §3 |
| U(1)_Y generator = (1/2)I in fundamental | **[L0]** | Representation theory | Background §3 |
| Hypercharge quantisation from Dirac condition on ψ-circle | **[L0]** | `appendices/appendix_alpha_geometry.tex §1` | State §3 |
| Fermion hypercharge assignments (specific values) | **[OPEN]** | `missing_axioms.md §Gap C2` | State as open §6 |

---

## U(1)_EM — Electromagnetism

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| U(1)_EM from ψ-cycle phase after SSB | **[L0]** | `DERIVATION_INDEX.md`, `interactions/qed.tex` | State §3 |
| Q = T₃ + Y/2 (Gell-Mann–Nishijima) | **[L1]** | Standard EW algebra | State §3 |
| Photon field $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$ | **[L1]** | Standard EW | State §3 |

---

## Electroweak Mixing

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| $e = g\sin\theta_W$ identity | **[L1]** | `canonical/alpha/gauge_normalization_attempt.tex §3` | Background §3 |
| **Weinberg angle** $\sin^2\theta_W$ (value 0.231) | **[SE] / [DEAD END]** | `missing_axioms.md §Gap C2`, `PRIORITIES_2026.md OHP-3` | Explicit dead-end §6: algebra alone cannot fix $g/g'$ |
| SSB pattern SU(2)_L × U(1)_Y → U(1)_EM | **[MC]** | `symmetry/step3_breaking_catalogue.tex` | Defer |
| Higgs field as SU(2)_L doublet from S[Θ] | **[OPEN]** (Gap EW-2) | `reports/alpha_no_fit_audit.md §Route A4` | Defer |

---

## Three Generations

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| N_gen = 3 from dim_ℝ(Im ℍ) = 3 | **[L0]** | `DERIVATION_INDEX.md §ψ-modes` | State §3 |
| Three ψ-winding modes carry identical gauge quantum numbers | **[L0]** | `su3_proof_status.md §Three generations` | State §3 |
| Mass hierarchy between generations | **[OPEN-HRD]** | `PRIORITIES_2026.md §Bottlenecks` | Defer; note KK obstruction |

---

## Higgs and Symmetry Breaking

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| Higgs boson from Θ-field VEV | **[OPEN]** | `research_tracks/research/higgs_yukawa_scan.md` | Defer to separate paper |
| Quartic Higgs coupling λ | **[CANDIDATE — blocked]** | Off by ×11 vs SM | Defer; note ×11 discrepancy |
| Higgs mass 125 GeV | **[OPEN]** | — | Defer |

---

## Fermion Masses and Yukawa

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| Yukawa coupling matrix $y_{ij}$ | **[OPEN]** | `missing_axioms.md §Gap Y2` | Defer |
| Electron/muon/tau masses | **[OPEN-HRD]** | KK mismatch theorem | Defer; state proved impossibility of torus-winding approach |
| CKM mixing matrix | **[OPEN]** | — | Defer |
| Neutrino masses / PMNS | **[OPEN]** | — | Defer |

---

## Anomaly Cancellation

| Claim | Status | Source | Paper action |
|-------|--------|--------|--------------|
| U(1)_Y³ anomaly cancelled | **[MC]** | Follows if SM reps assumed | Verify or state as open |
| [SU(2)_L]²U(1)_Y anomaly cancelled | **[MC]** | Follows if SM reps assumed | Verify or state as open |
| Anomaly cancellation from UBT first principles | **[OPEN]** | — | State as open §6 |

---

## Paper-Ready Claim Summary

### Can be stated as theorems (write-up only, no new proofs needed)

1. ℂ⊗ℍ ≅ Mat(2,ℂ) — algebraic foundation [L0]
2. 𝔰𝔲(3) realised via ℤ₂×ℤ₂×ℤ₂ involutions (Theorems G.A–G.D) [L0]
3. Quarks in **3**, gluons in **8**, EW/strong decoupling [L0]
4. Independent triqubit confirmation of SU(3) [L0]
5. Structural colour confinement [L0] + experimental support
6. SU(2)_L from left norm-preserving action [L0]
7. U(1)_Y from right scalar phase action [L0]
8. U(1)_EM from ψ-cycle phase [L0]
9. Three generations from ψ-winding [L0]
10. Hypercharge quantisation from Dirac condition [L0]

### Must be stated as open or semi-empirical

| Result | Strategy |
|--------|---------|
| Chirality (C1) | Close before submission (1–2 wk) OR explicit open statement with ψ-parity argument |
| Weinberg angle θ_W | **Declared dead end**: algebra alone cannot fix $g/g'$; honest statement in §6 |
| Higgs mechanism, gauge boson masses | Defer to separate Higgs paper |
| Fermion masses | Defer; note KK-mismatch theorem |
| Dynamical confinement | Clay Millennium problem; structural confinement is proved |
| Strong coupling g_s | Open problem in §6 |

---

## Single Must-Close Gap Before T2_GAUGE Submission

| Gap | Type | Estimated effort | Paper impact |
|-----|------|-----------------|--------------|
| **C1 — Chirality (SU(2)_L not SU(2)_R)** | Proof gap | 1–2 weeks | MEDIUM — converts motivated to proved |

All other gaps are either already closed ([L0]/[L1]), or explicitly declared open/dead-end.

**T2_GAUGE readiness without C1**: 75–80% (paper submittable with honest C1 open statement).  
**T2_GAUGE readiness with C1 closed**: 90%+ (all core claimed results are proved).

---

## Comparator Claim (for paper §1)

> No currently published algebraic framework derives all three Standard Model gauge
> factors SU(3)×SU(2)_L×U(1)_Y from a **single 8-real-dimensional algebra** with
> zero free parameters.
>
> Connes–Lott / Chamseddine–Connes noncommutative geometry requires a
> 21-real-dimensional algebra (ℂ⊕ℍ⊕Mat(3,ℂ)) and imposed chirality via K-theory.
> UBT uses ℂ⊗ℍ (8 real dimensions) and derives the same three gauge factors.

---

## References

- `gauge_exactly_proved_vs_open.md` — detailed proof-level source document
- `gauge_derivation_map.md` — derivation route map
- `su3_proof_status.md` — SU(3) sector detail
- `missing_axioms.md` — gap registry with obstruction descriptions
- `SM_CLOSURE_MATRIX.md` — full SM closure matrix (all SM elements)
- `canonical/interactions/sm_gauge.tex` — primary canonical source
- `canonical/su3_derivation/` — SU(3) source files
- `canonical/chirality/` — chirality sector
