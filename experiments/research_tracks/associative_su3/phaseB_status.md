<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# Phase B Status: Track A — Associative SU(3)

**Date:** 2026-03-02  
**Status:** STABLE — boundaries clearly labelled; no new claims added.

---

## Scope Boundary

This document summarises the proof status of Track A (Phase B) results.
**No new physics, algebra, or symmetry claims are made here.**
All entries refer to existing documents.

---

## Proof Status Table

| Result | File | Status | Notes |
|--------|------|--------|-------|
| $V_c = \mathrm{span}_\mathbb{C}\{I,J,K\}$ is canonical 3D complex subspace | `papers/su3_triplet/arxiv_version.tex` § Thm. 1 | **Proved** | Algebraic; no physics assumed |
| Hermitian form on $V_c$ is standard $\mathbb{C}^3$ inner product | `papers/su3_triplet/arxiv_version.tex` § Thm. 1 | **Proved** | Algebraic; trace formula |
| $\mathrm{SU}(3)_{V_c}$ is the isometry group of $(V_c,\langle\cdot,\cdot\rangle)$ | `papers/su3_triplet/arxiv_version.tex` § Thm. 2 | **Proved** | Algebraic; standard unitary group |
| $\mathrm{SU}(3)_{V_c}$ is NOT a subgroup of $\mathrm{Aut}_\mathbb{R}(\mathcal{B})$ | `papers/su3_triplet/arxiv_version.tex` § Rem. | **Proved** | Consistent with classical results |
| $\mathbb{Z}_2^3$ grading of $\mathcal{B}$ | `papers/su3_triplet/arxiv_version.tex` | **Proved** | Algebraic; involution table |
| Global SU(3) invariance of free $\Theta$-triplet action (flat background) | `global_invariance.tex` § Thm. | **Proved** | Requires Assumptions A1–A4 (see § Assumptions) |
| Global SU(3) invariance (general curved background, fixed metric) | `global_invariance.tex` § Cor. | **Proved** | Background independence for constant $U$ |
| Noether current $J_A^\mu$ and conservation $\partial_\mu J_A^\mu = 0$ on-shell | `noether_current.tex` | **Proved** | Standard Noether; requires EOM $\Box\Theta=0$ |
| Conserved charges $Q_A$ satisfy $\mathfrak{su}(3)$ Poisson algebra | `noether_current.tex` | **Standard result** | Follows from $[T^A,T^B]=if_{AB}{}^C T^C$ |
| Local (gauge) SU(3) extension: gauge field $A_\mu$, covariant derivative $D_\mu$ | `local_gauge_extension.tex` | **Candidate** | Standard Yang-Mills construction applied to $\mathrm{SU}(3)_{V_c}$ |
| Local covariance of $D_\mu\Theta$ under $U(x)$ | `local_gauge_extension.tex` § Prop. | **Proved (conditional)** | Conditional on global invariance; standard calculation |
| Dynamical symmetry of interacting kinetic operator | — | **Not proved — Open Problem** | Stated in arxiv Open Problems §1 |
| Physical interpretation of $A_\mu$ / connection to QCD | — | **Not claimed** | Explicitly disclaimed in `local_gauge_extension.tex` |

---

## What is NOT Claimed in Phase B

The following are explicitly **not claimed** anywhere in Phase B documents:

- SU(3) is derived from ℂ⊗ℍ automorphisms (it is not; see classical obstruction).
- The local gauge construction is a physical necessity (it is a candidate).
- $A_\mu$ is the QCD gluon field.
- The triplet $\Theta$ is identified with quarks.
- Any mass, coupling constant, or other numerical prediction.

---

## Open Problems (Phase B)

1. Prove or disprove that $\mathrm{SU}(3)_{V_c}$ is a symmetry of a natural
   interacting kinetic operator on $V_c$-valued fields.
2. Determine whether $A_\mu$ can be expressed as a component of the
   biquaternionic connection $\Omega_\mu$.
3. Verify whether the construction of $V_c$ is canonical up to
   $\mathrm{Aut}_\mathbb{R}(\mathcal{B})$.

---

## References

- `papers/su3_triplet/arxiv_version.tex` — self-contained arXiv submission
- `papers/su3_triplet/main.tex` — extended version
- `research_tracks/associative_su3/global_invariance.tex` — global invariance proof
- `research_tracks/associative_su3/noether_current.tex` — Noether current
- `research_tracks/associative_su3/local_gauge_extension.tex` — candidate gauge extension
- `research_tracks/associative_su3/strategy.md` — track strategy overview
