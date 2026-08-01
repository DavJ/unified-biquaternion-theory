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


# GR_final_gap_checklist.md — T1_GR Final Gap Checklist

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Definitive, pre-submission checklist of every open gap in the GR
recovery chain.  Determines submission readiness.  
**Paper**: `papers/UBT_GR_Flagship.tex`  
**Sources**: `research_tracks/T1_GR/proof_gap_list.md`,
`canonical/gr_closure/`, `canonical/geometry/`

---

## Submission Readiness: GO

All mandatory items for submission are resolved.  Two [L2] gaps are explicitly
bounded and stated in the paper.  No gap blocks submission.

---

## Gap Summary Table

| Gap ID | Name | Level | Blocks paper? | Status |
|--------|------|-------|---------------|--------|
| GAP-10 | Off-shell Θ-only closure | [L2] | **No** | Open — fully stated §6 |
| GAP-Z  | Zerilli equation (even-parity graviton) | [L2] | No | Open — stated §5 |
| GAP-C  | FRW/de Sitter cosmological ansatz | [L2] | No | Open — out of scope |
| GAP-M  | Compact M⁴ off-shell closure | [L2] | No | Open — out of scope |
| GAP-Q  | Path-integral quantisation of UBT | [L3] | No | Long-term — out of scope |

---

## Proved Chain — No Gaps

| Step | Claim | Proof level | Source |
|------|-------|-------------|--------|
| 1 | g_μν = Re[Tr(∂_μΘ · ∂_νΘ†)]/𝒩 is a symmetric covariant tensor | [L1] | `canonical/gr_closure/step1_metric_bridge.tex` |
| 2 | det(g_μν) ≠ 0 for Θ ∈ 𝒜_UBT | [L1] | `canonical/gr_closure/step2_nondegeneracy.tex` Thm 1 |
| 3 | Signature (−,+,+,+) from AXIOM-B | [L1] | `canonical/gr_closure/step3_signature_theorem.tex` Thm 2 |
| 4 | g → Γ → R geometric chain | Standard | Wald 1984, MTW 1973 |
| 5 | G_μν = 8πG T_μν from δS/δg = 0 | [L1] | `canonical/t_munu/step3_einstein_with_matter.tex` |
| 6a | Schwarzschild metric in isotropic coords | [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §3` |
| 6a-num | Schwarzschild spatial components verified < 10⁻¹⁵ | Numerical | `tools/verify_schwarzschild_theta.py` |
| 6b | ASD condition + twistor space for SU(2)₋ sector | [L1] | `research_tracks/research/asd_condition_ubt.tex §5` |
| 6c | Regge-Wheeler equation (odd-parity graviton) | [L1] | linearised UBT field eq. |
| 6d | T_μν symmetric and ∇^μ T_μν = 0 | [L1] | `canonical/geometry/stress_energy.tex` |

---

## GAP-10 — Off-Shell Θ-Only Closure

**Level**: [L2] — does not block paper  
**Paper location**: §6 (Open Problems), tcolorbox  
**Canonical source**: `canonical/gr_closure/step2_theta_only_closure.tex`

### On-shell result (PROVED)

For Θ ∈ 𝒜_UBT satisfying the Euler-Lagrange equation:  
- The induced variation map J = δg^μν/δΘ is non-degenerate on-shell.
- Consequently, δŜ[Θ]/δΘ = 0 is equivalent to the Einstein equations on g = g[Θ].

### Off-shell gap (OPEN [L2])

**Missing lemma**: Show that ker J consists only of gauge directions (pure phase
rotation or diffeomorphism) for all Θ in the full off-shell field space.

### Known obstructions (fully mapped)

1. **Rank mismatch**: Re(∇†∇Θ) is rank-0; G_μν is rank-2.  The multi-step
   chain Θ → ∂_μΘ → G_μν → g_μν is needed; each step must remain
   non-degenerate off-shell.

2. **Topology**: Global injectivity of Θ → g[Θ] requires H²(M⁴, ℤ) analysis
   of the Θ-bundle; generally hard in global analysis.

3. **Non-perturbative existence**: A fixed-point theorem in an appropriate Banach
   or Sobolev space is needed for well-posedness of δŜ/δΘ = 0.

### Why this does not block the paper

The on-shell result (Steps 1–6c) is self-contained and correct.  GAP-10 is a
question about off-shell path-integral completeness — it does not affect the
classical GR recovery.

### Approach that might close this gap

- Global analysis: compute the cohomology of the ker J sheaf over M⁴.
  If H¹(M⁴, ker J) = 0, global non-degeneracy follows from the local result.
- Show that degenerate Θ configurations have measure zero in any reasonable
  function space, making them irrelevant for path-integral purposes.

---

## GAP-Z — Zerilli Equation (Even-Parity Graviton)

**Level**: [L2] — does not block paper  
**Paper location**: §5 (Regge-Wheeler section) and §6  
**Priority**: Highest-priority future work in the graviton sector

### Proved

Regge-Wheeler equation (odd-parity graviton) derived from linearised UBT
without additional input (Theorem 6c in paper).

### Missing

The Zerilli equation for even-parity (polar) perturbations:

```
[d²/dr*² + ω² − V_Zerilli(r)] ψ_Zerilli = 0
```

Even-parity perturbations couple scalar and tensor modes, requiring
Chandrasekhar's two-potential transformation — not yet implemented in the
UBT even-parity Θ sector.

### Closing strategy

1. Derive the even-parity linearised UBT field equation.
2. Show it reduces to the Zerilli equation via Chandrasekhar's transformation.

**Estimated effort**: 2–4 weeks.

---

## GAP-C — Cosmological Solutions (FRW/de Sitter)

**Level**: [L2] — out of scope for this paper

FRW and de Sitter solutions have not been derived from a specific Θ ansatz.
The Friedmann equations should follow from Steps 1–5 applied to an FRW metric,
but the explicit biquaternionic construction is missing.

**Paper treatment**: Listed in §6 as a future direction.

---

## Pre-Submission Checklist

### Mathematical completeness

- [x] Steps 1–5: all proved [L1] with canonical source files cited
- [x] Schwarzschild: analytical derivation complete; spatial numerical < 10⁻¹⁵
- [x] ASD condition: proved [L1]
- [x] Regge-Wheeler: proved [L1]
- [x] T_μν symmetric: proved
- [x] ∇^μ T_μν = 0: proved
- [x] GAP-10 stated with full obstruction map
- [x] GAP-Z stated with closing strategy

### Paper quality

- [x] Notation unified throughout (𝒩, 𝒜_UBT, 𝔹, ℂ⊗ℍ consistent)
- [x] All theorems numbered consistently
- [x] All canonical source files cited
- [x] Comparison table vs. prior work
- [x] Axiom table complete
- [x] Reviewer objections pre-empted (see `reports/GR_reviewer_objections_and_answers.md`)
- [ ] Final proofreading pass (1–2 days)
- [ ] arXiv submission (after proofreading)

### External readability test

- [x] Abstract states the main theorem precisely
- [x] Introduction explains novelty without overclaiming
- [x] Proof sketches given in text; full proofs referenced to canonical files
- [x] Honest accounting of what is proved vs. open
- [x] A mathematically literate outsider can read end-to-end without hidden gaps

---

## References

- `research_tracks/T1_GR/proof_gap_list.md` — detailed gap analysis (source)
- `canonical/gr_closure/GR_chain_summary.tex` — step-by-step theorem chain
- `papers/UBT_GR_Flagship.tex` — main paper
- `reports/GR_reviewer_objections_and_answers.md` — reviewer preparation
