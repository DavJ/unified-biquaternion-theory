<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# SM_CLOSURE_MATRIX.md — P3: Standard Model Closure Status Matrix

**Author**: Ing. David Jaroš  
**Date**: 2026-05-13  
**Purpose**: Single-table reference for the complete status of every Standard Model
element in UBT — what is proved, what is open, what is a dead end, and what action
is needed.  Used to drive gap-closure work before the T2_GAUGE paper submission.  
**Sources**: `research_tracks/T2_GAUGE/gauge_derivation_map.md`,
`research_tracks/T2_GAUGE/missing_axioms.md`,
`research_tracks/T2_GAUGE/su3_proof_status.md`,
`DERIVATION_INDEX.md §Standard Model Gauge Group`,
`MILESTONE_REVIEW.md §3`

---

## 1. Proof-Level Key

| Label | Meaning |
|-------|---------|
| **[L0] PROVED** | Algebraic identity or exact theorem; zero free parameters |
| **[L1] PROVED** | Proved at one-loop level; no free parameters |
| **[SE] MOTIVATED** | Physical/algebraic motivation exists; not a formal theorem |
| **[SE] SEMI-EMP** | Value or relation fixed by experiment; not predicted |
| **[CANDIDATE]** | Partial derivation; mechanism not fully closed |
| **[DEAD END]** | Approach proved to fail; documented and closed |
| **[OPEN]** | No known derivation; active open problem |
| **[OPEN HARD]** | Resisted many approaches; no clear path |

---

## 2. Complete SM Closure Matrix

### 2.1 Algebraic Foundation

| SM Element | UBT Derivation | Status | Source | Paper action |
|------------|----------------|--------|--------|--------------|
| Fundamental algebra | ℂ⊗ℍ ≅ Mat(2,ℂ) postulate | AXIOM (Hurwitz-unique) | `canonical/fields/biquaternion_algebra.tex` | Justify in §2 |
| Biquaternion isomorphism ℂ⊗ℍ ≅ Mat(2,ℂ) | Exact algebraic identity | [L0] PROVED | `canonical/fields/biquaternion_algebra.tex` | State in §2 |
| Aut(ℂ⊗ℍ) structure | Aut ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂ | [L0] PROVED | `canonical/interactions/sm_gauge.tex` | Background in §2 |
| Complex time τ = t+iψ | AXIOM B; ψ-circle S¹_ψ | AXIOM | `canonical/THEORY/axioms/core_assumptions.tex` | State in §2 |

---

### 2.2 SU(3)_c — Colour Gauge Group

| SM Element | UBT Derivation | Status | Source | Paper action |
|------------|----------------|--------|--------|--------------|
| 𝔰𝔲(3) realised in ℂ⊗ℍ (Theorem G.A) | ℤ₂×ℤ₂×ℤ₂ involutions; G-equivariant traceless anti-Hermitian subspace | [L0] PROVED | `canonical/su3_derivation/su3_from_involutions.tex` | Theorem in §3 |
| Quarks in fundamental 3 (Theorem G.B) | ψ-winding modes on S¹_ψ select 3D complex subspace | [L0] PROVED | `canonical/interactions/sm_gauge.tex §G.B` | Theorem in §3 |
| Gluons in adjoint 8 (Theorem G.C) | 8 Gell-Mann generators λ₁–λ₈ in equivariant subspace; commutators verified | [L0] PROVED | `canonical/interactions/sm_gauge.tex §G.C` | Numerical table in §3 |
| EW/strong decoupling (Theorem G.D) | ℂ⊗ℍ decomposition; SU(3) and SU(2)_L sectors orthogonal | [L0] PROVED | `canonical/interactions/sm_gauge.tex §G.D` | Theorem in §3 |
| Independent triqubit confirmation | ℂ⊗ℍ ≅ Mat(2,ℂ) → qubit basis; 8 generators checked | [L0] PROVED | `canonical/interactions/su3_qubit_encoding.tex` | Independent check in §3 |
| Route 1 ↔ Route 2 equivalence | Isomorphism between involution and qubit derivations | [L0] PROVED | `canonical/bridges/su3_gauge_qubit_equivalence.tex` | Note in §3 |
| Structural confinement | Free quarks algebraically inadmissible; ⟨C₂⟩=0 (singlet condition) | [L0] PROVED + exp. support | `canonical/su3_derivation/su3_from_involutions.tex` | §4; distinguish from dynamical |
| Dynamical confinement (Wilson loop area law, mass gap) | Not derived | **[OPEN HARD]** (Clay Millennium) | — | State as Millennium problem in §6 |
| Strong coupling g_s from first principles | Not derived | **[OPEN]** | `research_tracks/T2_GAUGE/su3_proof_status.md §OP-SU3-1` | State as open problem in §6 |
| Quark-hadron duality / spectrum | Not derived | **[OPEN]** | `research_tracks/T2_GAUGE/su3_proof_status.md §OP-SU3-2` | State as open problem in §6 |
| Strong CP problem (θ_QCD) | Not addressed | **[OPEN]** | `research_tracks/T2_GAUGE/su3_proof_status.md §OP-SU3-3` | Note in §6 |

---

### 2.3 SU(2)_L — Weak Isospin

| SM Element | UBT Derivation | Status | Source | Paper action |
|------------|----------------|--------|--------|--------------|
| SU(2)_L from left norm-preserving action | {U∈Mat(2,ℂ): U†U=1} = U(2); special unitary subgroup = SU(2)_L | [L0] PROVED | `canonical/interactions/sm_gauge.tex` | Theorem in §3 |
| [T^a, T^b] = ε^{abc}T^c commutator algebra | Direct computation | [L0] PROVED | `canonical/interactions/sm_gauge.tex` | Background in §3 |
| Chirality: why SU(2)_L not SU(2)_R (Gap C1) | ψ-parity P_ψ: ψ→−ψ breaks L↔R; action S[Θ] invariant only for left couplings | **[SE] MOTIVATED** (not yet theorem) | `canonical/chirality/step3_gap_C1_resolution.tex`, `canonical/symmetry/chirality_and_parity_breaking.tex` | **Close before submission** (1–2 wk); if not: explicit open statement in §3 + §6 |
| W±, Z masses from UBT Higgs sector | Not fully derived; radiative Hosotani partially explored | **[CANDIDATE]** | `research_tracks/research/higgs_yukawa_scan.md` | Defer to separate paper |
| Anomaly cancellation in EW sector | Not explicitly checked in UBT | **[OPEN]** | — | Verify or state as open |

---

### 2.4 U(1)_Y — Hypercharge

| SM Element | UBT Derivation | Status | Source | Paper action |
|------------|----------------|--------|--------|--------------|
| U(1)_Y from scalar phase right action | Θ → Θ·e^{iφ}; scalar phase right multiplication = U(1) | [L0] PROVED | `canonical/interactions/sm_gauge.tex` | Theorem in §3 |
| Hypercharge quantum numbers (Y assignments) | Not derived from algebra; taken from SM representations | **[OPEN]** | `research_tracks/T2_GAUGE/missing_axioms.md §Gap C2` | State as open in §6 |

---

### 2.5 U(1)_EM — Electromagnetism

| SM Element | UBT Derivation | Status | Source | Paper action |
|------------|----------------|--------|--------|--------------|
| U(1)_EM from ψ-cycle phase | ψ-winding phase identified with EM phase; U(1)_EM ⊂ SU(2)_L × U(1)_Y after SSB | [L0] PROVED | `canonical/interactions/qed.tex`, `DERIVATION_INDEX.md` | Include in §3 |
| QED coupling from first principles | Not derived | **[OPEN]** | — | State as open in §6 |

---

### 2.6 Electroweak Unification

| SM Element | UBT Derivation | Status | Source | Paper action |
|------------|----------------|--------|--------|--------------|
| SU(2)_L × U(1)_Y → U(1)_EM symmetry breaking pattern | Candidate: radiative Hosotani mechanism | **[CANDIDATE]** | `research_tracks/research/higgs_yukawa_scan.md` | Defer |
| Weinberg angle sin²θ_W ≈ 0.23122 | Cannot be derived from ℂ⊗ℍ alone (g/g' ratio unconstrained by algebra) | **[DEAD for pure algebra; OPEN/COND for EW-1b]** | `research_tracks/T2_GAUGE/missing_axioms.md §Gap C2`, `PRIORITIES_2026.md OHP-3` | Explicit pure-algebra dead-end statement in §6 + conditional EW-1b note |
| Higgs field as SU(2)_L doublet from S[Θ] | 1⊕3⊕3̄⊕1 decomposition lacks j=1/2 doublet; new input needed | **[OPEN]** (Gap EW-2) | `reports/alpha_no_fit_audit.md §Route A4` | Defer to Higgs paper |
| Higgs VEV ⟨H⟩ = v = 246 GeV | Not derived | **[OPEN]** | `research_tracks/T2_GAUGE/missing_axioms.md §Gap C3` | Defer |
| W± mass m_W ≈ 80.4 GeV | Not derived | **[OPEN]** | — | Defer |
| Z mass m_Z ≈ 91.2 GeV | Not derived | **[OPEN]** | — | Defer |
| Quartic Higgs coupling λ | Radiative Hosotani gives λ_UBT ≈ 11 λ_SM (λ gap ×11) | **[CANDIDATE — blocked]** | `PRIORITIES_2026.md §Bottlenecks`, `DERIVATION_INDEX.md` | Defer; note ×11 discrepancy |

---

### 2.7 Fermion Sector

| SM Element | UBT Derivation | Status | Source | Paper action |
|------------|----------------|--------|--------|--------------|
| Three generations from dim Im(ℍ) = 3 | Three ψ-winding modes n=1,2,3; identical quantum numbers | [L0] PROVED | `DERIVATION_INDEX.md`, `canonical/fields/` | State in §3 |
| Fermion quantum numbers (isospin, hypercharge assignments) | Not derived; taken from SM representations | **[OPEN]** | — | Defer |
| Electron mass m_e | Not derived from first principles | **[OPEN HARD]** | `PRIORITIES_2026.md §Bottlenecks` | Defer |
| Muon mass m_μ | Not derived | **[OPEN HARD]** | — | Defer |
| Tau mass m_τ | Not derived | **[OPEN HARD]** | — | Defer |
| Muon/electron mass ratio 207 | KK mismatch theorem *proves* torus winding cannot reproduce factor-207 | **[BLOCKED — proved impossible via torus winding]** | `PRIORITIES_2026.md §Bottlenecks` | State as open hard problem with known obstruction |
| Quark masses | Not derived | **[OPEN HARD]** | — | Defer |
| Yukawa coupling matrix y_{ij} | Not derived | **[OPEN]** | `research_tracks/T2_GAUGE/missing_axioms.md §Gap Y2` | Defer |
| CKM mixing matrix | Not derived | **[OPEN]** | — | Defer |
| Neutrino masses / PMNS matrix | Not derived | **[OPEN]** | — | Defer |

---

### 2.8 Cross-SM Consistency Checks

| Check | Status | Source | Paper action |
|-------|--------|--------|--------------|
| SU(3)_c × SU(2)_L algebraic decoupling | [L0] PROVED — Theorem G.D | `canonical/interactions/sm_gauge.tex §G.D` | State in §3 |
| 8 Gell-Mann generators numerical verification | [L0] PROVED — all 28 commutator pairs | `tools/verify_su3_from_biquaternion.py`, `tools/verify_su3_superposition.py` | Include in §3 or App. B |
| Involution route ↔ qubit route equivalence | [L0] PROVED | `canonical/bridges/su3_gauge_qubit_equivalence.tex` | Mention in §3 |
| Anomaly cancellation (standard SM consistency check) | Not verified in UBT formalism | **[OPEN]** | — | Verify or acknowledge |

---

## 3. Closure Priority Ranking

### Must close before T2_GAUGE paper submission

| Gap | Type | Difficulty | Required action |
|-----|------|------------|-----------------|
| **C1 — Chirality (SU(2)_L not SU(2)_R)** | Proof gap | Medium | Formalise ψ-parity theorem; ~1–2 weeks |

### State honestly as open (no closure needed for submission)

| Gap | Paper strategy |
|-----|---------------|
| C2 — Weinberg angle | Declare pure-algebra dead end; note EW-1b as conditional branch |
| C3 — Higgs/λ ×11 | Defer to separate Higgs paper |
| Y1 — Fermion masses | Defer; state KK obstruction |
| Y2 — Yukawa couplings | Defer |
| Dynamical confinement | Cite Clay Millennium; structural argument is sufficient |
| g_s strong coupling | Open problem in §6 |
| Anomaly cancellation | Verify or state as open |

### Already addressed: no action needed in T2_GAUGE paper

| Result | Disposition |
|--------|-------------|
| SU(3) Theorems G.A–G.D | Write up from `canonical/su3_derivation/` |
| SU(2)_L from left action | Write up from `canonical/interactions/sm_gauge.tex` |
| U(1)_Y from right action | Write up from `canonical/interactions/sm_gauge.tex` |
| U(1)_EM from ψ-cycle | Write up from `canonical/interactions/qed.tex` |
| Three generations | Write up from `canonical/fields/` |
| EW/strong decoupling | Write up from Theorem G.D |

---

## 4. What the T2_GAUGE Paper Can Claim Without These Gaps

### Zero-parameter proved claims (write-up only needed)

1. ℂ⊗ℍ ≅ Mat(2,ℂ) algebraic isomorphism — [L0]
2. ℤ₂×ℤ₂×ℤ₂ involutions and 𝔰𝔲(3) realisation — [L0]
3. Theorems G.A, G.B, G.C, G.D (SU(3) and representations) — [L0]
4. Independent triqubit confirmation — [L0]
5. Structural colour confinement — [L0] + experimental support
6. SU(2)_L from left norm-preserving action — [L0]
7. U(1)_Y from right scalar phase action — [L0]
8. U(1)_EM from ψ-cycle phase — [L0]
9. Three generations from ψ-winding modes — [L0]
10. EW/strong sector algebraic decoupling — [L0]

### Comparator claim

No currently published single algebraic framework derives all three SM gauge
factors SU(3)×SU(2)_L×U(1)_Y from one 8-real-dimensional algebra with zero
free parameters.  This claim is supported by the Connes-Lott comparison
(NCG requires 21 real dimensions; Chamseddine-Connes requires imposed chirality
via K-theory class).

---

## 5. Confidence Assessment

| Claim category | Confidence | Risk if submitted now |
|----------------|------------|----------------------|
| SU(3) four theorems | High (both routes proved, numerically checked) | Low |
| SU(2)_L from left action | High (algebraic identity) | Low |
| U(1)_Y from right action | High (algebraic identity) | Low |
| Three generations | High (dim Im ℍ = 3) | Low |
| Chirality (C1) | Medium (motivated, not proved) | Medium — close before submission |
| Weinberg angle | Pure-algebra dead end; EW-1b conditional | Low (if stated clearly) |
| Higgs/masses | Open | Low (if deferred explicitly) |

**Overall T2_GAUGE readiness**: **75–80%** given Gap C1 is the only medium-risk
item.  Paper is submittable if C1 is closed or if C1 is honestly stated as a
motivated-only open problem.
