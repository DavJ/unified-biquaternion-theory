<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# GR_claim_to_proof_matrix.md — Claim-to-Proof Traceability Matrix

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Single-table mapping of every major claim in
`papers/UBT_GR_Submission.tex` to the exact theorem, proof level, and
canonical source file that backs it.  Auditors and reviewers should consult
this matrix first.  
**Verdict**: All core claims are [L1] proved.  Two [L2] gaps are open and
explicitly bounded.

---

## How to Read This Matrix

| Column | Meaning |
|--------|---------|
| **#** | Sequential claim identifier |
| **Claim (as stated in paper)** | Verbatim or paraphrased claim from the paper |
| **Theorem / result** | Theorem number or named result |
| **Level** | Proof confidence level (see key below) |
| **Canonical source** | File containing the formal proof |
| **Paper location** | Section or appendix where the claim appears |
| **Status** | PROVED / OPEN / ASSUMPTION |

### Level Key

| Level | Meaning |
|-------|---------|
| **[L0]** | Algebraic identity — follows from definitions of ℂ⊗ℍ alone |
| **[L1]** | Formal theorem — requires axioms A1–A3 plus standard mathematics |
| **[L2]** | Open problem — stated but not yet proved |
| **[STD]** | Standard result from established mathematics/physics |
| **[NUM]** | Numerically verified (reproducible script) |
| **[AX]** | Axiom — a postulate, not derived |

---

## Part I — Foundational Axioms

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| F1 | Biquaternion algebra 𝔹 := ℂ⊗_ℝℍ ≅ Mat(2,ℂ) ≅ Cl₁,₃(ℝ) | Porteous isomorphism | [L0] | `canonical/algebra/biquaternion_algebra.tex` | §2.1 | PROVED |
| F2 | AXIOM-B: physical time τ = t+iψ with ∂_τ timelike | AXIOM-B | [AX] | Paper §2.2 | §2.2 | ASSUMPTION |
| F3 | AXIOM-F: field Θ: M⁴×ℂ_τ → 𝔹, eq. ∇†∇Θ = κ𝒯 | AXIOM-F | [AX] | Paper §2.3 | §2.3 | ASSUMPTION |
| F4 | Admissibility condition: {∂_μΘ} linearly independent | Assumption A4 | [AX] | Paper §2.3 | §2.3 | ASSUMPTION |

---

## Part II — Five-Step GR Chain

### Step 1: Metric Emergence

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| G1 | g_μν = Re[Tr(∂_μΘ · ∂_νΘ†)]/𝒩 is well-defined | Def. 3.1 | [L0] | `canonical/gr_closure/step1_metric_bridge.tex` | §3.1 | PROVED |
| G2 | g_μν is symmetric | Lemma 3.1 (cyclic trace) | [L0] | `canonical/gr_closure/step1_metric_bridge.tex` | §3.1 | PROVED |
| G3 | g_μν transforms as covariant (0,2) tensor | Theorem 3.1 | [L1] | `canonical/gr_closure/step1_metric_bridge.tex` | §3.1 | PROVED |

### Step 2: Non-Degeneracy

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| G4 | det(g_μν) ≠ 0 for Θ ∈ 𝒜_UBT | Theorem 3.2 (Gram matrix) | [L1] | `canonical/gr_closure/step2_nondegeneracy.tex` | §3.2 | PROVED |

### Step 3: Lorentzian Signature

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| G5 | g₀₀ < 0 from AXIOM-B | Theorem 3.3, App. A | [L1] | `canonical/gr_closure/step3_signature_theorem.tex` | §3.3, App. A | PROVED |
| G6 | g_ii > 0 (i=1,2,3) from spacelike generators | Theorem 3.3, App. A | [L1] | `canonical/gr_closure/step3_signature_theorem.tex` | §3.3, App. A | PROVED |
| G7 | Lorentzian signature (−,+,+,+) is a theorem, not a postulate | Theorem 3.3 | [L1] | `canonical/gr_closure/step3_signature_theorem.tex` | §3.3 | PROVED |

### Step 4: Geometric Apparatus

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| G8 | Levi-Civita connection Γ_μνρ from g_μν | Standard differential geometry | [STD] | Wald 1984 §3 | §3.4 | PROVED (standard) |
| G9 | Riemann and Einstein tensors from connection | Standard | [STD] | Wald 1984 §3 | §3.4 | PROVED (standard) |
| G10 | Contracted Bianchi: ∇^μ G_μν = 0 | Standard | [STD] | Wald 1984 §4 | §3.4 | PROVED (standard) |

### Step 5: Einstein Field Equations

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| G11 | G_μν = 8πG T_μν from Hilbert variation δS/δg = 0 | Theorem 3.5 | [L1] | `canonical/t_munu/step3_einstein_with_matter.tex` | §3.5 | PROVED |
| G12 | T_μν is symmetric | Lemma (variational argument) | [L1] | `canonical/geometry/stress_energy.tex` | §3.5 | PROVED |
| G13 | ∇^μ T_μν = 0 (conservation) | Theorem (Bianchi + diffeo.) | [L1] | `canonical/geometry/stress_energy.tex` | §3.5 | PROVED |
| G14 | Newton's G is an input parameter (Planck scale) | Remark 3.1 | [AX] | Paper §3.5 | §3.5 | ASSUMPTION (⚠️ requires explicit statement) |

---

## Part III — Schwarzschild Sector

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| S1 | Θ₀ = e^{iΦ(r)}[f(r)𝟏 + g(r)e_r] is the unique spherically symmetric vacuum ansatz | Uniqueness theorem | [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §3` | §4 | PROVED |
| S2 | Schwarzschild g_ij = Ψ⁴δ_ij recovered from Θ₀ | Analytical derivation | [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex` | §4 | PROVED |
| S3 | Spatial components verified to < 10⁻¹⁵ relative error | Numerical check | [NUM] | `tools/verify_schwarzschild_theta.py` | §4, App. B | PROVED |
| S4 | g_tt = −Φ² from ψ-structure | Complex-time analysis | [L1] | Paper §4, tcolorbox | §4 | PROVED |
| S5 | ASD Weyl condition C⁺ = 0 for SU(2)₋ sector | Holonomy argument | [L1] | `research_tracks/research/asd_condition_ubt.tex §5` | §4 | PROVED |
| S6 | Penrose nonlinear graviton: curved twistor space exists | Penrose theorem + ASD | [L1]+[STD] | Penrose 1976 | §4 | PROVED |

---

## Part IV — Linearised Gravity / Graviton Sector

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| L1 | Linearised UBT reproduces linearised Einstein equations | Linearisation of Thm 3.5 | [L1] | Step 5 chain, linearised | §5 | PROVED |
| L2 | Odd-parity Regge-Wheeler equation derived without extra input | Theorem 6c | [L1] | Linearised UBT + mode decomposition | §5 | PROVED |
| L3 | Even-parity Zerilli equation | GAP-Z | **[L2]** | `reports/GR_final_gap_checklist.md §GAP-Z` | §5, §6 | **OPEN** |

---

## Part V — Off-Shell Closure

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| O1 | On-shell: δŜ[Θ]/δΘ = 0 ⟺ Einstein equations (for Θ ∈ 𝒜_UBT on-shell) | On-shell closure | [L1] | `canonical/gr_closure/step2_theta_only_closure.tex` | §6 | PROVED |
| O2 | Off-shell: ker J = gauge directions only (global injectivity of Θ → g) | GAP-10 | **[L2]** | `canonical/gr_closure/step2_theta_only_closure.tex`, obstruction map | §6 | **OPEN** |

---

## Part VI — Discussion Claims

| # | Claim | Theorem / result | Level | Canonical source | Paper loc. | Status |
|---|-------|-----------------|-------|-----------------|------------|--------|
| D1 | UBT reduces to GR when ψ → 0 (real-sector limit) | Five-step chain | [L1] | This paper | §7 | PROVED |
| D2 | UBT metric formula is absent from prior biquaternion gravity papers | Literature survey | [STD] | Adler 1995, Finkelstein 1962, De Leo 1996 | §7.2 | PROVED |
| D3 | UBT algebra is 8-dimensional; Connes-Lott NCG uses 21 | Dimension count | [L0] | §7.2 | §7.2 | PROVED |

---

## Summary

| Category | Count | Status |
|----------|-------|--------|
| Core axioms / assumptions | 4 | All explicit |
| [L0] algebraic identities | 4 | All proved |
| [L1] formal theorems | 15 | All proved |
| [STD] standard results | 5 | All standard references given |
| [NUM] numerical verifications | 1 | Script available |
| [L2] open problems | 2 | GAP-10, GAP-Z — explicitly stated in paper |

**Submission verdict**: All core claims proved or explicitly bounded.
Two open [L2] problems stated.  One assumption (Newton's G) requires a
one-sentence clarification before submission (see G14 above).

---

## Cross-References

- `reports/GR_claims_with_evidence_table.md` — full evidence table with circular-reasoning audit
- `reports/GR_final_gap_checklist.md` — detailed gap analysis
- `reports/GR_hostile_review.md` — hostile reviewer simulation
- `reports/GR_reviewer_FAQ.md` — concise FAQ for external readers
- `papers/UBT_GR_Submission.tex` — paper
