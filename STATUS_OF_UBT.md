<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# STATUS_OF_UBT.md — Single Source of Truth

**Author**: Ing. David Jaroš  
**Date**: 2026-05-18 *(last updated — rigour pass 2026-05-18)*  
**Purpose**: Authoritative one-file description of the real current state of every
major UBT track.  All other status files are subordinate to this document.
When in conflict, this file governs.

> **Governance rule**: This file is updated only when a track changes status,
> a gap is solved or killed, or a paper is submitted.  Date every significant change.

---

## Executive Summary

UBT has one submission-ready result (T1_GR), one near-ready result (T2_GAUGE),
and one blocked result (T3_ALPHA).

| Track | Status | Paper | Verdict |
|-------|--------|-------|---------|
| **T1_GR** — GR Recovery | ✅ SUBMIT READY | `papers/UBT_GR_Submission.tex` | Submit to arXiv within 2 weeks |
| **T2_GAUGE** — Gauge Sector | 🔶 NEAR READY | `papers/UBT_Gauge_Submission.tex` | Target submission: 2026-06-08 |
| **T3_ALPHA** — Fine Structure Constant | 🔴 CONDITIONAL | No paper yet | Blocked on Gap G137-B |
| **quantum_ubt** — Quantum UBT Scope | 🔶 SCOPED | Research notes | graviton kvantizace [STD], NCG [MC] |

**No speculative tracks are active.**  Consciousness/CTC content is frozen in
`speculative_extensions/`.  No new branches are being opened during the cleanup window.

**Execution control**: Top-10 priority/gap implementation instructions and locked
sequencing are maintained in `ROADMAP.md` under
`Implemented Top-10 Priority/Gaps Program (Execution-Control Layer)`.

## 2026-05-18 Rigour pass

### Opravy
- GR paper: Cl⁺₁,₃ (even subalgebra) opraveno [P1]
- GR paper: indefinitní vnitřní součin pro $\mathcal N$ zaveden [P1]
- N_eff: dvě různé routes jasně odděleny [P3]
- ΔN_eff: napětí závisí na g*(T_dec); pro benchmark g*≥427 OK, numerický práh je ~389 [P5]
- Gap C2 Step 1: blokér formalizován [P4]

### Aktuální stav
- arXiv: GR ZIP ready po P1/P9/P10/P14/P15
- Gap G137-B: NARROWED, minimální teorém formulován [P7]
- Weinberg: [CONDITIONAL on C2 Step 1]
- Alpha: NOT DERIVED

## 2026-05-18
- GR paper: arXiv ready (Cl^+, indefinite bilinear opraveny)
- Gauge PDF: build command ready; environment lacks `pdflatex` in this run
- NCG B₀ PDF: build command ready; environment lacks `pdflatex` in this run
- Python scaffold: `src/ubt/` updated (Hilbert scaffold + g-2 OPEN_GAP placeholder); targeted scaffold tests passing
- FRW [Prop.]: $g_{0i}=0$ globálně pro $\Theta_0=1_2$ (explicit proposition in track file)
- ΔN_eff: explicit UBT lower bound derived $g_*(T_{\rm Pl})\ge120.75$ [Prop.]; consistency with Planck bound still needs larger $g_*$ (benchmark 427)
- Gap G137-B: V_eff functional derivation path aktivní; residual factor quantified, gap remains NARROWED/OPEN

## 2026-05-17

| Item | Prev status | New status | Source |
|------|-------------|------------|--------|
| NCG B₀ paper | draft pending | compiled PDF (6 pages, 0 fatal errors) | `papers/ncg_poisson_B0_derivation.pdf` |
| Gauge Submission PDF | pending | compiled PDF (8 pages, 0 fatal errors) | `papers/UBT_Gauge_Submission.pdf` |
| ΔN_eff prediction | OPEN (uncomputed) | computed: 0.131/mode, 1.569 naive total; benchmark 0.247 for g*=427 | `research_tracks/quantum_ubt/delta_neff_prediction.tex` |
| Gap G137-B Casimir T³ | unexplored | EXPLORED & CLOSED: B_Casimir ≪ B_phenom; ratio ~1.3×10⁻³ | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §8` |
| FRW from UBT (GAP-C) | OPEN | First steps: refined ansatz formulated; Friedmann [Prop.] | `research_tracks/quantum_ubt/frw_from_ubt.tex` |
| Higgs from S[Θ] (EW-2) | OPEN | First steps: tree-level check (no V(Θ)); CW setup described | `research_tracks/EW/higgs_from_theta.tex` |
| T-dualita | [NO-GO local ansätze] | [NO-GO local ansätze; OPEN globally] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex` |
| C2 uniqueness | OPEN/MC frozen | OPEN/MC frozen — anomálie cesta neselektuje n=1 | unchanged |

## Status update 2026-05-14

| Item | Prev status | New status | Source |
|------|-------------|------------|--------|
| EW-1b (R_psi from S[Θ]) | CONDITIONAL | PROVED [L1 conditional] | rpsi_from_action.tex |
| N_eff=12 SU(2) twist | [L1] | [L1] confirmed | step2_AUDIT.tex |
| N_eff loop-counting | [OPEN/MC] | [OPEN/MC frozen] | step2_AUDIT.tex |
| Proton decay prediction | — | defined τ_p~10³⁴ yr | falsifiable_prediction_sheet.md |
| Anomaly cancellation | OPEN | OPEN (Σ Q³≠0 charge-only) | anomaly_cancellation.tex |
| C2 uniqueness | OPEN | OPEN/MC frozen | colour_charge_lattice.tex |
| Gap G137-B | NARROWED | NARROWED (τ=i [OBS]) | mellin_insertion_B.tex |

## 2026-05-14 update
- Anomaly cancellation (chiral): [NUM/L1 conditional on C2]
- EW-1b: PROVED [L1 conditional]
- T-duality: lemma formulated [OPEN/MC]
- Gap G137-B: T³ volumetric factor identified as source of 3/2 exponent

---

## T1_GR — General Relativity Recovery

**Status**: SUBMIT READY  
**Confidence**: HIGH — all core chain steps proved at [L1]  
**Canonical manuscript**: `papers/UBT_GR_Submission.tex` *(release snapshots are archived in `papers/old_releases/` for provenance and external deposit traceability)*

### Exact Achievements

The five-step chain Θ → g → Γ → R → G_μν = 8πGT_μν is complete at proof level [L1].

| Claim | Level | Source |
|-------|-------|--------|
| Metric g_μν derived from Θ | [L1] | `canonical/gr_closure/step1_metric_bridge.tex` |
| Non-degeneracy det(g) ≠ 0 | [L1] | `canonical/gr_closure/step2_nondegeneracy.tex` |
| Lorentzian signature (−,+,+,+) from AXIOM-B | [L1] | `canonical/gr_closure/step3_signature_theorem.tex` |
| Einstein equations from Hilbert variation | [L1] | Paper §3 |
| T_μν symmetric, ∇^μT_μν = 0 | [L1] | `canonical/geometry/stress_energy.tex` |
| Schwarzschild metric (spatial, < 10⁻¹⁵ error) | [L1]+[NUM] | `tools/verify_schwarzschild_theta.py` |
| Regge-Wheeler equation (odd-parity graviton) | [L1] | Paper §5 |
| Zerilli equation (even-parity) and canonical graviton quantisation notes | PROVED [L1]+[STD] | `canonical/gr_closure/zerilli_derivation.tex`, `research_tracks/quantum_ubt/graviton_quantisation.tex` |

Comprehensive proof audit: `reports/GR_claim_to_proof_matrix.md`  
Reviewer FAQ: `reports/GR_reviewer_FAQ.md`

### Remaining Blockers

None that prevent submission.

| Gap | Level | Impact |
|-----|-------|--------|
| GAP-10 — Off-shell Θ-only closure | [L2] Open | Does not block; stated in paper |

### Pre-Submission Fix

✅ Pre-submission fixes are integrated in the canonical manuscript (`papers/UBT_GR_Submission.tex`).
✅ Local LaTeX build completed in the current rigour pass; arXiv zip prepared.

### Next Action

Submit `papers/UBT_GR_Submission.tex` to arXiv (gr-qc or math-ph) and simultaneously
to *Classical and Quantum Gravity* or *Journal of Mathematical Physics*.

---

## T2_GAUGE — Standard Model Gauge Structure

**Status**: NEAR READY — algebraic results proved; draft paper compiled  
**Confidence**: HIGH for algebraic sector; MEDIUM for chirality claim  
**Paper**: `papers/UBT_Gauge_Submission.tex` (compiled PDF)

### Solved Algebra Pieces (Zero New Work Needed)

All claims below are [L0] algebraic identities or [L1] proved theorems.

| Claim | Level | Source |
|-------|-------|--------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) ≅ Cl₁,₃(ℝ) | [L0] | `canonical/algebra/biquaternion_algebra.tex` |
| 𝔰𝔲(3) from ℤ₂×ℤ₂×ℤ₂ involutions | [L0] | `canonical/su3_derivation/su3_from_involutions.tex` |
| Quarks in **3**, gluons in **8**, EW/strong decoupling | [L0] | `canonical/interactions/sm_gauge.tex` |
| SU(2)_L from left norm-preserving action | [L0] | `canonical/interactions/sm_gauge.tex §SU2` |
| SU(2)_L acts on left-chiral doublets (Gap C1 closed) | [L1] | `canonical/chirality/step3_gap_C1_resolution.tex` |
| U(1)_Y from right scalar phase | [L0] | `canonical/interactions/sm_gauge.tex §U1` |
| U(1)_EM from ψ-cycle phase | [L0] | `canonical/interactions/qed.tex` |
| Three generations from ψ-winding | [L0] | `canonical/n_eff/` |
| Hypercharge quantisation from Dirac condition | [L0] | `canonical/qed_phi_const/appendix_alpha_geometry.tex §1` |

### Open Physical Gaps

| Gap | Description | Priority |
|-----|-------------|----------|
| EW-1 | Weinberg angle sin²θ_W — **DEAD END for pure algebra** (algebra cannot fix g'/g) | Keep dead-end statement for algebra-only route |
| EW-1b | EW1+RG branch ($\sin^2\theta_W^{\mathrm{GUT}}=3/8 \rightarrow \sin^2\theta_W(M_Z)\approx0.231$) | CONDITIONAL on Gap C2 Step 1 closure and on deriving $R_\psi$ from $S[\Theta]$; tracked in `research_tracks/EW/weinberg_angle_ew1_rg.tex` and `research_tracks/EW/rpsi_from_action.tex` |
| EW-2 | Higgs doublet VEV from S[Θ] | Deferred to separate Higgs paper |
| C2 | Specific fermion hypercharge assignments | Open |
| Y2 | Yukawa couplings | Open |
| Dynamical confinement | Wilson loop area law | Clay Millennium Problem |

### Confidence

**Overall**: 85% submit-ready now; 90% after verifying anomaly cancellation.

**Honest statement to use in paper**: The Weinberg angle sin²θ_W ≈ 0.231 cannot
be derived from algebra alone (dead-end no-go for pure algebraic fixing of g'/g).
An EW1+RG route exists only conditionally, pending first-principles closure of
Gap C2 Step 1 for fermion hypercharge assignments.

### Next Action

Begin T2_GAUGE paper draft immediately after T1_GR submission. Target sections 1–3
(algebra, SU(3), SU(2)_L) in weeks 2–3. Target arXiv at week 8–10.

Master status file: `canonical/gauge/GAUGE_MASTER_STATUS.md`

---

## T3_ALPHA — Fine Structure Constant

**Global Objective**: Derive α⁻¹_bare = 137 (integer) without fitting.
Full derivation (137.036) requires solving Gap G137-B first.

**Status**: CONDITIONAL — integer-137 result proved given B = B_phenom; gap remains

### Active Routes

| Route | Status | Confidence | Blocker | Continue? |
|-------|--------|------------|---------|-----------|
| **A_PRIME: V_eff Prime Attractor** | **PRIMARY** | HIGH (conditional) | Gap G137-B | YES — 4-week time-box |

**What is proved in A_PRIME**:
- N_eff^twist = 12 — [L1]: closed on the SU(2)-twist route; the independent
  scalar-loop count remains N_eff^loop = 3 [L1], and the identification
  twist = loop is still OPEN/[MC] (see `canonical/n_eff/step2_AUDIT.tex`)
- V_eff structure has a motivated prime/winding/entropy route, but the full
  derivation from S[Θ] remains conditional.
- n*(B_phenom) = 137 for B_phenom ≈ 46.298 [L1] (conditional on B)
- Prime stability of n* is a structural property [L0]
- $\vartheta_3(0|i)/\eta(i)=\sqrt{2}$ [STD], Ramanujan form
  $B=12^{3/2}\cdot2^{1/8}\cdot\vartheta_3(0|i)^{1/4}$ [OBS]
- Seeley-DeWitt consistency checkpoint: $a_2$ Einstein-Hilbert reproduction
  [Prop.], $a_4\propto\vartheta_3(0|i)$ remains [MC]/OPEN

**What remains open in A_PRIME** (Gap G137-B):
- Derive B_phenom ≈ 46.298 from S[Θ] without using α as input.
- B₀ = 8π (one-loop, proved) gives n* ≈ 65, not 137.
- The missing factor ≈ 1.84 corresponds to a Kac-Moody level or higher-loop correction.

### Gamma Entropy Audit Results (2026-05-11)

The Gamma/prime-factorization entropy interpolation audit produced the following
high-precision numerical results (all at B_Ram **[OBS]**, not derived from S[Θ]):

| Quantity | Value | Status |
|----------|-------|--------|
| n1 (V1 stationary point) | 136.9890996341 | [L1] given B_Ram |
| α⁻¹_exp (CODATA 2018) | 137.035999084 | [PHENOM] |
| n3 (V3 stationary point) | 137.0905214131 | [DERIVATION CANDIDATE] given B_Ram |
| λ_exact (exact stationarity) | 0.4622175427 | **[OBS]** |
| λ_frac (linear fractional) | 0.4624199099 | **[OBS]** |

**Bracket property** [OBS]: n1 < α⁻¹_exp < n3.
The measured fine-structure constant inverse lies strictly between the V1 and V3
stationary points — a structurally suggestive observation that does **not** close
G137-B.

**B_Ram** = 12^(3/2) · 2^(1/8) · θ₃(0|i)^(1/4) ≈ 46.2809 — **[OBS] only**.
Not derived from S[Θ].

**λ** — fit parameter — **[OBS] only**. No derivation from S[Θ] is known.
Nearest candidate constant: 37/80 = 0.4625 (0.06% deviation from λ_exact — NUMERIC_ONLY, no UBT meaning).

**G137-B remains OPEN. Alpha is NOT DERIVED.**

Cross-references:
- `canonical/alpha/gamma_entropy_alpha_refinement_status.tex` — LaTeX status document
- `reports/gamma_entropy_alpha_interpolation_audit.md` — full numerical audit

### Parked Routes

| Route | Reason | Revival condition |
|-------|--------|-------------------|
| A1: Gauge Normalization | Conditional on Gap EW-1 (pure-algebra Weinberg route is dead end; EW-1b conditional) | Only if EW-1b is closed in T2_GAUGE |
| A2: Symmetry-Breaking Projection | Same blocker as A1 (EW-1 + EW-2) | Same |

### Dead-End Routes

| Route | Verdict | Evidence |
|-------|---------|----------|
| **A3: Theta/Modular Route** | **DEFINITIVELY FAILED** | Exhaustive search — no modular invariant = 137.036 |
| **A4: Layer 2 Coding Constraint** | **DEFINITIVELY FAILED** | Proved impossible: coding fixes spectrum, not coupling magnitude |

Archive: `reports/failed_routes_graveyard.md`

### Strongest Next Move (30-Day Attack Plan)

**Week 1–4**: Modular bootstrap on Gap G137-B.
- Target: derive B = μ(Γ₀(n*))/3 from S[Θ] evaluated at n*.
- Evidence: μ(Γ₀(137))/3 ≈ 46.00 (0.64% from B_phenom); non-trivial structural signal.
- Success = route becomes [L1]; publish integer-137 paper.

**Week 4 decision gate** (go/no-go):
- If G137-B solved → write T3_ALPHA paper; submit as companion to T1_GR.
- If G137-B not solved (70–80% probability) → publish conditional integer-137 note,
  downgrade T3_ALPHA to STRUCTURAL EVIDENCE status, redirect effort to T2_GAUGE.

**Do not pursue** A1, A2, A3, A4.  Dead routes receive zero active priority.

Master portfolio file: `canonical/alpha/ALPHA_PORTFOLIO_MASTER.md`  
Detailed route audit: `canonical/alpha/ALPHA_MASTER_STATUS.md`  
Gamma entropy audit: `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`,
`reports/gamma_entropy_alpha_interpolation_audit.md`

---

## Exploratory Tracks

### Side Ideas Worth Preserving

| Topic | Location | Status | Note |
|-------|----------|--------|------|
| ΔN_eff ≈ 0.046 (CMB-S4 prediction) | `research_tracks/` | OPEN | Above CMB-S4 threshold; publishable as prediction |
| Structural colour confinement (algebraic) | `canonical/su3_derivation/` | PROVED [L0] | Distinct from dynamical confinement; include in T2_GAUGE |
| ASD Weyl condition and twistor correspondence | `canonical/geometry/` | PROVED [L1] | Include in T1_GR appendix or follow-on paper |
| Hecke eigenvalue lepton mass ratios | `research_tracks/hecke_bridge/` | [MC] — strong (0.02%) | Corroborates A_PRIME; preserve, do not publicise as proved |

### Frozen Items

| Topic | Location | Reason frozen |
|-------|----------|---------------|
| Complex Consciousness Theory / Psychons | `speculative_extensions/complex_consciousness/` | No mathematical closure; frozen indefinitely |
| Closed Timelike Curves | `speculative_extensions/appendices/` | Speculative; no experimental anchor |
| p-adic dark sector | `research_tracks/p_universes/` | Interesting; deferred beyond 21-day window |
| Cosmological solutions (GAP-C) | `research_tracks/` | Open; no active effort |

---

## Deprecated Claims

| Old Claim | Where It Appeared | Why Deprecated | Replacement |
|-----------|-------------------|----------------|-------------|
| Weinberg angle derivation is a CRITICAL PRIORITY | `canonical/alpha/weinberg_angle_derivation.md`, `reports/ew_mixing_status.md` | No-go argument proves pure algebra cannot fix g'/g; continuous deformations of the SU(2)_L × U(1)_Y embedding change tan θ_W continuously | State pure-algebra DEAD END + EW-1b conditional branch in T2_GAUGE paper §6 |
| "Four active α routes" | `canonical/alpha/alpha_derivation_routes.md` (dated 2026-04-27) | Routes A3 and A4 are definitively killed (exhaustive scan + proved impossibility) | One primary route (A_PRIME), two parked, two killed |
| Chirality Gap C1 as merely MOTIVATED [SE] | `reports/gauge_status_matrix.md` (line 70), `reports/chirality_gap.md` | Formal proof exists: `canonical/chirality/step3_gap_C1_resolution.tex` | C1 is [L1] PROVED — SU(2)_L acts on left-chiral doublets |
| α⁻¹ = 137.036 claimed derivable via B_base/k=1 Kac-Moody route | Multiple early α documents | 27+ approaches exhausted; k=1 has not been proved; this specific number is not the claim | Claim is α⁻¹_bare = 137 (integer), conditional on Gap G137-B |
| N_eff=12 (SU(2) twist route) | [L1] | step2_AUDIT.tex §Final verdict: N_helicity=2 [L1], N_eff=12 [L1], B₀=8π [L1] |
| N_eff=12 (loop counting, independent) | [OPEN/MC] | step2_AUDIT.tex: N_charge double-counting unresolved |

**Note 2026-05-14**: The SU(2)-twist route gives N_eff=12 [L1] (step2_AUDIT.tex). The earlier loop-counting route remains [OPEN/MC]. These are two separate claims; both are tracked.

---

## Repository Public Face

| Document | Status |
|----------|--------|
| `docs/comparison_table.html` | ✅ Vytvořeno — srovnávací tabulka teorií |

---

## Key Source Files

| Purpose | File |
|---------|------|
| What is proved (complete map) | `WHAT_IS_PROVED.md` |
| Cross-track claims matrix | `CLAIMS_MATRIX.md` |
| Derivation level standard | `DERIVATION_STATUS_STANDARD.md` |
| GR claim-to-proof matrix | `reports/GR_claim_to_proof_matrix.md` |
| GR claim strength table | `reports/GR_claim_strength_table.md` |
| GR consolidated review | `reports/GR_REVIEW_MASTER.md` |
| GR canonical manuscript | `papers/UBT_GR_Submission.tex` |
| Alpha portfolio master | `canonical/alpha/ALPHA_PORTFOLIO_MASTER.md` |
| Alpha route detail | `canonical/alpha/ALPHA_MASTER_STATUS.md` |
| Gauge sector truth | `canonical/gauge/GAUGE_MASTER_STATUS.md` |
| Forward plan | `ROADMAP.md` |
| Contradictions resolved | `reports/contradictions_resolved.md` |
| File cleanup log | `reports/files_merged_deleted_redirected.md` |
| Repo integrity check | `reports/repo_integrity_check.md` |
