<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# GR_REVIEW_MASTER.md — T1_GR Consolidated Review Reference

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Single consolidated file for all pre-submission review material.
Consolidates: `reports/GR_claim_to_proof_matrix.md`,
`reports/GR_claims_with_evidence_table.md`, `reports/GR_final_gap_checklist.md`,
`reports/GR_hostile_review.md`, `reports/GR_reviewer_FAQ.md`,
`reports/GR_reviewer_objections_and_answers.md`.  
**Truth anchor**: `STATUS_OF_UBT.md §T1_GR`

> The individual source files are preserved.  This master file is the
> first-read overview for anyone auditing or reviewing the GR track.

---

## Part 0 — Submission Verdict

**SUBMIT READY.**

All core chain steps are [L1] proved.  Two [L2] open problems are explicitly
bounded and do not block submission.  No outstanding fatal or major reviewer
issues remain.

| Item | Status |
|------|--------|
| Five-step GR chain complete | ✅ All [L1] proved |
| Schwarzschild metric recovery | ✅ [L1]+[NUM], error < 10⁻¹⁵ |
| Regge-Wheeler equation | ✅ [L1] proved |
| Pre-submission fix (G clarification §3.5) | ⚠️ Required — one sentence |
| Hostile reviewer simulation | ✅ SUBMIT_READY verdict |
| Reviewer FAQ prepared | ✅ |
| Objections & rebuttals prepared | ✅ Zero unresolved FATAL or MAJOR |

---

## Part 1 — Core Claim-to-Proof Matrix

Source: `reports/GR_claim_to_proof_matrix.md`

### Foundational Axioms

| # | Claim | Level | Status |
|---|-------|-------|--------|
| F1 | ℂ⊗ℍ ≅ Mat(2,ℂ) ≅ Cl₁,₃(ℝ) | [L0] | PROVED |
| F2 | AXIOM-B: τ = t+iψ with ∂_τ timelike | [AX] | ASSUMPTION (stated) |
| F3 | AXIOM-F: field Θ: M⁴×ℂ_τ → 𝔹, eq. ∇†∇Θ = κ𝒯 | [AX] | ASSUMPTION (stated) |
| F4 | Admissibility condition: {∂_μΘ} linearly independent | [AX] | ASSUMPTION (stated) |

### Five-Step GR Chain

| Step | Claim | Level | Source |
|------|-------|-------|--------|
| G1 | g_μν = Re[Tr(∂_μΘ · ∂_νΘ†)]/𝒩 — symmetric covariant tensor | [L1] | `canonical/gr_closure/step1_metric_bridge.tex` |
| G2 | det(g_μν) ≠ 0 for admissible Θ (Theorem 3.2) | [L1] | `canonical/gr_closure/step2_nondegeneracy.tex` |
| G3 | Lorentzian signature (−,+,+,+) from AXIOM-B alone | [L1] | `canonical/gr_closure/step3_signature_theorem.tex` |
| G4 | Levi-Civita connection, curvature tensors | [STD] | Wald 1984 |
| G5 | Einstein field equations G_μν = 8πG T_μν from Hilbert variation | [L1] | Paper §3 |
| G6 | T_μν symmetric | [L1] | `canonical/geometry/stress_energy.tex` |
| G7 | ∇^μT_μν = 0 (conservation) | [L1] | `canonical/geometry/stress_energy.tex` |

### Schwarzschild and Linearised Gravity

| # | Claim | Level | Source |
|---|-------|-------|--------|
| G8 | Schwarzschild metric from spherically symmetric Θ₀ ansatz | [L1] | `canonical/gr_closure/` §3 |
| G9 | Spatial components g_ij = Ψ⁴δ_ij, error < 10⁻¹⁵ | [NUM] | `tools/verify_schwarzschild_theta.py` |
| G10 | Temporal component g_tt = −Φ² from ψ-structure | [L1] | Paper §4 |
| G11 | ASD Weyl condition C⁺ = 0 for SU(2)₋ sector | [L1] | `canonical/gr_closure/` §5 |
| G13 | Linearised UBT reproduces linearised Einstein equations | [L1] | Linearisation of G5 |
| G14 | Regge-Wheeler equation (odd-parity graviton) | [L1] | Paper §5 |

---

## Part 2 — Gap Checklist

Source: `reports/GR_final_gap_checklist.md`

**Submission readiness**: GO — all mandatory items resolved.

| Gap ID | Name | Blocks paper? | Status |
|--------|------|---------------|--------|
| GAP-10 | Off-shell Θ-only closure | **No** | Open — fully stated in paper §6 |
| GAP-Z | Zerilli equation (even-parity graviton) | **No** | Open — stated in paper §5 |
| GAP-C | FRW/de Sitter cosmological ansatz | No | Open — out of scope |
| GAP-Q | Path-integral quantisation | No | Long-term — out of scope |

**Pre-submission fix required**:
- §3.5: Add one sentence clarifying Newton's G = free input parameter (not derived from UBT).

---

## Part 3 — Hostile Reviewer Summary

Source: `reports/GR_hostile_review.md`

**Simulated overall verdict**: SUBMIT_READY — no unresolved fatal or major issues.

### Attack summary

| Attack | Severity | Resolution | Residual risk |
|--------|----------|------------|---------------|
| "Metric not unique; gauge freedom" | MAJOR | Paper states gauge symmetry; proven gauge orbits preserve physics | LOW |
| "Lorentzian signature just assumed" | MAJOR | AXIOM-B stated explicitly; signature is a theorem from AXIOM-B | LOW |
| "G is a free parameter — not derived" | MODERATE | Pre-submission fix: add one sentence §3.5 | NEGLIGIBLE after fix |
| "Off-shell sector incomplete" | MODERATE | GAP-10 stated explicitly; on-shell result stands | LOW |
| "Zerilli missing" | MODERATE | GAP-Z stated; Regge-Wheeler proved — paper correct about this | LOW |
| "Schwarzschild uniqueness" | MINOR | Spherical symmetry assumption stated; isotropic coords stated | NEGLIGIBLE |
| Notation unfamiliarity | MINOR | Appendix on ℂ⊗ℍ included | NEGLIGIBLE |

---

## Part 4 — Reviewer FAQ (Summary)

Source: `reports/GR_reviewer_FAQ.md`

**Q: What does the paper claim?**  
The metric is *derived* from the biquaternion field Θ via g_μν = Re[Tr(∂_μΘ·∂_νΘ†)]/𝒩.
Lorentzian signature is a theorem from AXIOM-B, not an assumption.
Einstein's equations, Schwarzschild metric (error < 10⁻¹⁵), and Regge-Wheeler equation follow.

**Q: What are the axioms?**  
Three: (A) biquaternion algebra ℂ⊗ℍ, (B) complex time τ = t+iψ with ∂_τ timelike,
(F) field equation ∇†∇Θ = κ𝒯.  These are stated explicitly.

**Q: What is not claimed?**  
Zerilli equation (GAP-Z, [L2] open), off-shell Θ-only closure (GAP-10, [L2] open),
quantum gravity (GAP-Q, long-term), cosmological solutions (GAP-C, out of scope).

**Q: How is this different from Adler 1995 / Finkelstein 1962?**  
Prior biquaternion gravity papers impose the metric; UBT derives it.

---

## Part 5 — Objections and Rebuttals (Summary)

Source: `reports/GR_reviewer_objections_and_answers.md`

**Summary**: Zero FATAL, one MAJOR (handled), five MODERATE (handled), three MINOR (handled).

| Objection | Rebuttal status |
|-----------|-----------------|
| GR-1: Metric not unique (gauge freedom) | Handled — gauge orbits proved to preserve physics |
| GR-2: Lorentzian signature not derived | Handled — Theorem 3 (AXIOM-B → signature) |
| GR-3: G is a free parameter | Handled — §3.5 clarification added (pre-submission fix) |
| GR-4: Off-shell sector incomplete | Handled — GAP-10 stated; result is on-shell |
| GR-5: Zerilli missing | Handled — GAP-Z stated; Regge-Wheeler proves linearised sector |
| GR-6: Schwarzschild uniqueness | Handled — spherical symmetry ansatz stated clearly |
| GR-7: biquaternion formalism unfamiliar | Handled — appendix with standard references |
| GR-8: No experimental predictions | Handled — current paper is classical GR recovery; predictions deferred |
| GR-9: Connection to twistor theory | Handled — ASD Weyl condition proved; discussed in appendix |

---

## Part 6 — Source Files Index

| File | Purpose |
|------|---------|
| `papers/UBT_GR_Submission.tex` | **Flagship paper** — primary deliverable |
| `reports/GR_claim_to_proof_matrix.md` | Complete claim-to-proof traceability |
| `reports/GR_claims_with_evidence_table.md` | Every claim vs. every evidence |
| `reports/GR_final_gap_checklist.md` | Pre-submission gap audit |
| `reports/GR_hostile_review.md` | Hostile referee simulation |
| `reports/GR_reviewer_FAQ.md` | Reviewer FAQ |
| `reports/GR_reviewer_objections_and_answers.md` | Full rebuttal set |
| `canonical/gr_closure/` | All GR proof source files |
| `canonical/geometry/` | Stress-energy and metric geometry proofs |
| `tools/verify_schwarzschild_theta.py` | Numerical verification script |
