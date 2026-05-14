<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# General Relativity Recovery — Topic Index

**Status**: **PROVED [L1]** for Steps 1–5; **OPEN [L2]** for Step 6 (off-shell closure)  
**Last updated**: 2026-03-10  
**Canonical bridge**: `canonical/bridges/GR_chain_bridge.tex`

---

## Quick Answer

UBT **generalises and embeds** General Relativity — it does not replace or contradict it.
In the real-valued limit (ψ → 0), the biquaternionic field equation

```
∇†∇Θ(q,τ) = κ𝒯(q,τ)
```

reduces exactly to Einstein's field equations G_μν = 8πG T_μν.
The full derivation chain (Steps 1–5) is proved at level [L1] with one explicit
residual open problem at Step 6.

---

## Canonical Sources (Start Here)

| Document | Role | Status |
|----------|------|--------|
| `canonical/bridges/GR_chain_bridge.tex` | **CANONICAL NAVIGATION** — lists all six steps with cross-references | Navigation |
| `canonical/geometry/metric.tex` | Step 1: metric g_μν = Re Tr(∂_μΘ · ∂_νΘ†) | PROVED [L1] |
| `canonical/gr_closure/step1_metric_bridge.tex` | Step 1b: equivalence of derivative and tetrad definitions | PROVED [L0] |
| `canonical/gr_closure/step2_nondegeneracy.tex` | Step 2: non-degeneracy det(g) ≠ 0 | PROVED [L0] |
| `canonical/gr_closure/step3_signature_theorem.tex` | Step 3: Lorentzian signature (−,+,+,+) | PROVED [L0] |
| `canonical/geometry/connection.tex` | Step 4a: Levi-Civita connection Γ | Standard GR |
| `canonical/geometry/curvature.tex` | Step 4b: Riemann curvature, Einstein tensor G_μν | Standard GR |
| `canonical/geometry/gr_as_limit.tex` | Step 5: Einstein field equations via Hilbert variation | PROVED [L1] |
| `canonical/geometry/gr_completion_attempt.tex` | Step 6: off-shell Θ-only closure | OPEN [L2] |

**Important**: Steps 1–5 are sufficient for the physical claim that GR is recovered.
Step 6 is an additional theoretical tightening that remains open.

---

## Supporting Files

| Document | Label | Content |
|----------|-------|---------|
| `canonical/THEORY/architecture/geometry/biquaternion_curvature.tex` | **supporting** | Biquaternionic curvature tensor background |
| `canonical/THEORY/architecture/geometry/biquaternion_stress_energy.tex` | **supporting** | Stress-energy derivation background |
| `canonical/gr_closure/GR_chain_summary.tex` | **supporting** | Compact summary of the full chain |
| `canonical/geometry/stress_energy.tex` | **supporting** | T_μν derivation; ∇^μ T_μν = 0 conservation |
| `canonical/geometry/biquaternion_metric.tex` | **supporting** | Full biquaternionic metric decomposition |

---

## Historical / Archival Files

| Document | Label | Why Not Canonical |
|----------|-------|-------------------|
| `ARCHIVE/archive_legacy/consolidation_project/appendix_A_biquaternion_gravity_consolidated.tex` | **historical** | Earlier consolidation; superseded by GR_closure/ chain |
| `research_tracks/legacy_theory_variants/unified_biquaternion_theory/ubt_appendix_1_biquaternion_gravity.tex` | **historical** | Original derivation; action principle section still canonical source |
| `docs/papers/appendix_GR_embedding.tex` | **supporting** | Hilbert variation of full action; remains a valid derivation reference |
| `docs/reports/gr_recovery_final_status.md` | **historical** | Status snapshot; live status is in `docs/AUDITS/repository_claim_map.md` |
| `docs/ubt_gr_recovery/gr_recovery_status.md` | **historical** | Earlier status file; see `docs/AUDITS/` for current state |

---

## Step-by-Step Status Table

| Step | Claim | Status | Notes |
|------|-------|--------|-------|
| 1 | Metric emergence: Θ → g_μν | PROVED [L1] | g_μν is derived, not fundamental |
| 1b | Equivalence of derivative and tetrad definitions | PROVED [L0] | |
| 2 | Non-degeneracy: det(g) ≠ 0 | PROVED [L0] | |
| 3 | Lorentzian signature (−,+,+,+) | PROVED [L0] | Algebraic theorem from AXIOM B (complex time) |
| 4 | Levi-Civita connection and Riemann curvature | PROVED | Standard GR from metric; no UBT-specific gap |
| 5 | Einstein field equations G_μν = 8πG T_μν | PROVED [L1] | Hilbert variation; Assumptions A1–A3 used |
| 6 | Off-shell Θ-only closure | OPEN [L2] | Structural obstruction identified; not blocking Steps 1–5 |

---

## Key Claims for External Readers

- **GR is NOT contradicted**: UBT generalises GR; all GR predictions are reproduced in the real sector.
- **Both flat and curved spacetime are covered**: The recovery holds for all curvature regimes (Minkowski, weak-field, strong-field, cosmological).
- **New physics is invisible classically**: The imaginary biquaternionic degrees of freedom couple only to quantum/ψ-circle physics; ordinary matter does not couple to Im(𝒢_μν).
- **All confirmed GR tests automatically validate UBT's real sector**.

---

## DERIVATION_INDEX Cross-Reference

Main entries in `DERIVATION_INDEX.md`:
- **GR Recovery Status** section with all proved/conditional/open sub-claims
- Bridge: `canonical/bridges/GR_chain_bridge.tex`
- Claim evidence: `docs/AUDITS/claim_evidence_matrix.md` rows 1–7

---

## What a New Reader Should Do

1. Read the bridge document `canonical/bridges/GR_chain_bridge.tex` (canonical navigation, ~4 pages)
2. For the full derivation chain, follow Steps 1–5 in `canonical/gr_closure/`
3. For the algebraic proof of Lorentzian signature, see Step 3 (`canonical/gr_closure/step3_signature_theorem.tex`)
4. For the action principle and Hilbert variation, see `canonical/geometry/gr_as_limit.tex`
5. Step 6 (off-shell closure) is an advanced open problem and can be skipped on first reading
