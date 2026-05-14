<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# SU(3) Color Symmetry — Topic Index

**Status**: ⭐ **PROVED [L0]** — zero free parameters  
**Last updated**: 2026-03-10  
**Canonical file**: `canonical/su3_derivation/su3_from_involutions.tex`

---

## Quick Answer

SU(3)_c color symmetry is **derived** from the biquaternion algebra ℂ⊗ℍ with zero
free parameters. The dimension of the imaginary quaternion subspace Im(ℍ) = 3 forces
SU(3) — there is no room for a different gauge group.

**Status of open sub-questions**:
- SU(3) emergence: **PROVED**
- Color confinement: **CONJECTURED with experimental support**

---

## Canonical Source (Start Here)

| Document | Role | Status |
|----------|------|--------|
| `canonical/su3_derivation/su3_from_involutions.tex` | **CANONICAL** — complete algebraic proof, Theorems G.A–G.D | PROVED [L0] ⭐ |

**Theorem structure in canonical file**:
- **Thm. G.A** — Lie algebra: Im(ℍ) involutions generate 𝔰𝔲(3)
- **Thm. G.B** — Fundamental representation: quarks live in ℂ³
- **Thm. G.C** — Adjoint representation: gluons live in ℝ⁸
- **Thm. G.D** — EW decoupling: SU(3) commutes with SU(2)_L × U(1)_Y

---

## Supporting Files

| Document | Label | Content |
|----------|-------|---------|
| `canonical/su3_derivation/step1_involution_summary.tex` | **supporting** | Involution-based construction (the canonical approach, abbreviated) |
| `canonical/su3_derivation/step1_superposition_approach.tex` | **supporting** | Complementary derivation via quantum superposition over {I,J,K} |
| `canonical/su3_derivation/step3_SU3_result.tex` | **supporting** | Result compilation; cross-references to canonical |
| `tools/verify_su3_superposition.py` | **supporting** | Numerical verification: all 8 Gell-Mann generators confirmed |
| `tools/verify_su3_from_biquaternion.py` | **supporting** | Alternative numerical check |

---

## Sandbox / Heuristic Files

| Document | Label | Why Not Canonical |
|----------|-------|-------------------|
| `ARCHIVE/archive_legacy/tex/Appendix_G_Emergent_SU3.tex` | **heuristic / motivating sketch** | Maps i,j,k → r,g,b; intuitive but NOT an algebraic proof; see disclaimer inside that file |
| `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/` | **mathematical sandbox** | Valid Lie algebra homomorphism (51 tests pass); derives from a *different* starting point (qubit encoding, not ℂ⊗ℍ); not part of mainline UBT |
| `tools/scan_associative_su3_candidates.py` | **sandbox** | Parameter scan; no new result |
| `docs/reports/associative_su3_scan.md` | **sandbox** | Scan results only |

---

## Open Sub-Problem: Confinement

Color confinement is a **separate** open problem, not required for the SU(3) emergence proof.

| Document | Status |
|----------|--------|
| `ARCHIVE/archive_legacy/consolidation_project/confinement/algebraic_confinement.tex` | **CONJECTURED with experimental support** |
| `ARCHIVE/archive_legacy/consolidation_project/confinement/confinement_verification.py` | **supporting** (numerical verification) |

Free quarks are algebraically inadmissible (⟨C₂⟩ = 4/3 ≠ 0 for color non-singlet states),
and all tested hadron types satisfy ⟨C₂⟩ = 0. Clay Millennium Prize (Yang–Mills mass gap)
remains separate and open.

---

## DERIVATION_INDEX Cross-Reference

Main entries in `DERIVATION_INDEX.md`:

- **SU(3)_c from involutions** — PROVED [L0] ⭐ CANONICAL
- **SU(3)_c from quantum superposition** — PROVED [L0] (complementary approach)
- **SU(3)_c via i,j,k → r,g,b** — [HEURISTIC / MOTIVATING SKETCH]
- **SU(3) via qubit embedding** — [MATHEMATICAL SANDBOX]
- **Color confinement** — [CONJECTURED WITH EXPERIMENTAL SUPPORT L0]

---

## What a New Reader Should Do

1. Read `canonical/su3_derivation/su3_from_involutions.tex` (canonical proof, ~8 pages)
2. Run `tools/verify_su3_superposition.py` to numerically confirm all generators (< 1 second)
3. If interested in the heuristic motivation, consult `ARCHIVE/archive_legacy/tex/Appendix_G_Emergent_SU3.tex` with
   the explicit understanding it is a sketch, not a proof
4. For the qubit-encoding variant (unrelated to UBT first principles), see
   `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/README.md`
