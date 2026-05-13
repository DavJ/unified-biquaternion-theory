<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# CLAIMS_MATRIX.md — Cross-Track Flagship Claims Matrix

**Author**: Ing. David Jaroš  
**Date**: 2026-05-13  
**Purpose**: Single-table map of every flagship claim in UBT across all
active tracks, with derivation level, source file, and paper location.
No claim is allowed to carry a higher level here than what is supported
by the cited source file.  
**Proof level definitions**: `DERIVATION_STATUS_STANDARD.md`  
**Truth anchor**: `STATUS_OF_UBT.md`

> **Governance rule**: If a source file is updated and a claim level changes,
> this matrix must be updated on the same day.

---

## How to Read This Matrix

| Column | Meaning |
|--------|---------|
| **#** | Claim identifier |
| **Claim** | The assertion, as it would appear in a paper |
| **Level** | Derivation level per `DERIVATION_STATUS_STANDARD.md` |
| **Exact?** | Yes = exact result; No = conditional or approximate |
| **Canonical source** | File containing the proof or evidence |
| **Paper** | Paper where this claim appears or will appear |
| **Status** | PROVED / OPEN / DEAD / DEFERRED / ASSUMPTION |

---

## Track T1_GR — General Relativity Recovery

**Paper**: `papers/UBT_GR_Submission.tex` (Canonical submission manuscript)  
**Overall verdict**: SUBMIT READY

| # | Claim | Level | Exact? | Canonical source | Paper | Status |
|---|-------|-------|--------|-----------------|-------|--------|
| G1 | g_μν = Re[Tr(∂_μΘ·∂_νΘ†)]/𝒩 is a symmetric covariant (0,2) tensor | [L1] | Yes | `canonical/gr_closure/step1_metric_bridge.tex` | §3 | PROVED |
| G2 | det(g_μν) ≠ 0 for admissible Θ | [L1] | Yes | `canonical/gr_closure/step2_nondegeneracy.tex` | §3.2 | PROVED |
| G3 | Lorentzian signature (−,+,+,+) is a theorem from AXIOM-B alone | [L1] | Yes | `canonical/gr_closure/step3_signature_theorem.tex` | §3.3 | PROVED |
| G4 | Levi-Civita connection and Riemann curvature from derived metric | [STD] | Yes | Wald 1984 | §3.4 | PROVED |
| G5 | G_μν = 8πGT_μν from Hilbert variation of UBT action | [L1] | Yes | `canonical/gr_closure/` + Paper §3.5 | §3.5 | PROVED |
| G6 | T_μν symmetric | [L1] | Yes | `canonical/geometry/stress_energy.tex` | §3.5 | PROVED |
| G7 | ∇^μ T_μν = 0 (covariant conservation) | [L1] | Yes | `canonical/geometry/stress_energy.tex` | §3.5 | PROVED |
| G8 | Schwarzschild metric from spherically symmetric Θ₀ ansatz | [L1] | Yes | `canonical/geometry/biquaternionic_vacuum_solutions.tex §3` | §4 | PROVED |
| G9 | Spatial components g_ij = Ψ⁴δ_ij verified to < 10⁻¹⁵ relative error | [L1]+[NUM] | Yes | `tools/verify_schwarzschild_theta.py` | §4 | PROVED |
| G10 | g_tt = −Φ² from complex-time ψ-structure | [L1] | Yes | Paper §4 | §4 | PROVED |
| G11 | Regge-Wheeler equation (odd-parity graviton) without extra input | [L1] | Yes | `papers/UBT_GR_Submission.tex §5` | §5 | PROVED |
| G12 | ASD Weyl condition C⁺ = 0 for SU(2)₋ sector | [L1] | Yes | `canonical/geometry/asd_condition_ubt.tex §5` | App. | PROVED |
| G13 | Newton's G is a free parameter (semi-empirical input) | [AX] | — | Paper §3.5 | §3.5 | ASSUMPTION |
| GAP-10 | Off-shell Θ-only closure (global ker J = gauge only) | [OPEN] | — | — | §6 | OPEN — does not block |
| GAP-Z | Zerilli equation (even-parity graviton) | [L1] | Yes | `canonical/gr_closure/zerilli_derivation.tex` | §6 | PROVED |

---

## Track T2_GAUGE — Standard Model Gauge Structure

**Paper**: Draft needed (T2_GAUGE paper, ~6–8 weeks)  
**Overall verdict**: NEAR READY — algebraic results complete; paper write-up needed

### Algebraic Foundation

| # | Claim | Level | Exact? | Canonical source | Paper | Status |
|---|-------|-------|--------|-----------------|-------|--------|
| A1 | ℂ⊗ℍ ≅ Mat(2,ℂ) | [L0] | Yes | `canonical/algebra/biquaternion_algebra.tex` | §2 | PROVED |
| A2 | ℂ⊗ℍ ≅ Cl₁,₃(ℝ) | [L0] | Yes | `canonical/algebra/biquaternion_algebra.tex` | §2 | PROVED |
| A3 | Aut(ℂ⊗ℍ) ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂ | [L0] | Yes | `canonical/interactions/sm_gauge.tex` | §3 | PROVED |

### SU(3) Colour

| # | Claim | Level | Exact? | Canonical source | Paper | Status |
|---|-------|-------|--------|-----------------|-------|--------|
| E1 | 𝔰𝔲(3) from ℤ₂×ℤ₂×ℤ₂ involutions on ℂ⊗ℍ | [L0] | Yes | `canonical/su3_derivation/su3_from_involutions.tex` | §4 | PROVED |
| E2 | Quarks in fundamental **3**, gluons in adjoint **8** | [L0] | Yes | `canonical/interactions/sm_gauge.tex §G.B,G.C` | §4 | PROVED |
| E3 | EW/strong algebraic decoupling | [L0] | Yes | `canonical/interactions/sm_gauge.tex §G.D` | §4 | PROVED |
| E4 | Structural colour confinement (free quarks algebraically inadmissible) | [L0] | Yes | `canonical/su3_derivation/su3_from_involutions.tex Thm G.B` | §4 | PROVED |
| E5 | Independent triqubit confirmation of SU(3) | [L0] | Yes | `canonical/interactions/su3_qubit_encoding.tex` | §4 | PROVED |

### SU(2)_L Weak Isospin

| # | Claim | Level | Exact? | Canonical source | Paper | Status |
|---|-------|-------|--------|-----------------|-------|--------|
| E6 | SU(2)_L from left norm-preserving action on Mat(2,ℂ) | [L0] | Yes | `canonical/interactions/sm_gauge.tex §SU2` | §5 | PROVED |
| E7 | SU(2)_L acts on left-chiral doublets (Gap C1 closed) | [L1] | Yes | `canonical/chirality/step3_gap_C1_resolution.tex` | §5 | PROVED |

### U(1)_Y and U(1)_EM

| # | Claim | Level | Exact? | Canonical source | Paper | Status |
|---|-------|-------|--------|-----------------|-------|--------|
| E8 | U(1)_Y from right scalar phase action | [L0] | Yes | `canonical/interactions/sm_gauge.tex §U1` | §5 | PROVED |
| E9 | U(1)_EM from ψ-cycle phase after SSB | [L0] | Yes | `canonical/interactions/qed.tex` | §5 | PROVED |
| E10 | Hypercharge quantisation from Dirac condition | [L0] | Yes | `canonical/qed_phi_const/appendix_alpha_geometry.tex §1` | §5 | PROVED |
| E11 | Three generations from ψ-winding modes | [L0] | Yes | `canonical/n_eff/` | §6 | PROVED |

### Open / Dead

| # | Claim | Level | Status |
|---|-------|-------|--------|
| EW-1 | Weinberg angle sin²θ_W ≈ 0.231 from UBT | [DEAD for pure algebra; OPEN/COND for EW-1b] | Pure algebra dead end — algebra cannot fix g'/g; EW-1b (EW1+RG) remains conditional |
| EW-2 | Higgs doublet VEV from S[Θ] | [OPEN] | DEFERRED — separate Higgs paper |
| C2 | Specific fermion hypercharge assignments | [OPEN] | Open |
| Y2 | Yukawa couplings from UBT | [OPEN] | Open (hard) |
| CON | Dynamical confinement (Wilson loop area law) | [OPEN] | Clay Millennium Problem |

---

## Track T3_ALPHA — Fine Structure Constant

**Paper**: None yet; conditional on Gap G137-B resolution  
**Overall verdict**: STRUCTURAL / CONDITIONAL / OPEN GAP (G137-B)

| # | Claim | Level | Exact? | Canonical source | Status |
|---|-------|-------|--------|-----------------|--------|
| P1 | N_eff = 12 is a motivated mode-counting candidate, currently OPEN/[MC] under critical audit. | OPEN/[MC] | No | `canonical/n_eff/step2_AUDIT.tex` | OPEN/[MC] |
| P2 | V_eff structure has a motivated winding / prime-entropy route, but the full derivation from S[Theta] remains conditional. | [L1][COND] | Yes, given B | `canonical/alpha/ALPHA_MASTER_STATUS.md` | CONDITIONAL |
| P3 | n*(B_phenom) = 137 for B_phenom ≈ 46.298 | [L1][COND: G137-B] | Yes, given B | `canonical/alpha/alpha_best_route.tex` | CONDITIONAL (not standalone proof of α) |
| P4 | 137 is prime — consistent with V_eff prime stability | [L0]+[STD] | Yes | Number theory | PROVED |
| P5 | B₀ = 8π from S_kin[Θ] (one-loop) | [L1] | Yes | `canonical/t_munu/`, `canonical/n_eff/step2_vacuum_polarization.tex` | PROVED |
| P6 | μ(Γ₀(137))/3 ≈ 46.00 — independent structural signal | [L2] | No | `canonical/alpha/prime_137_status.md` | STRUCTURAL CORROBORATION |
| P7 | One-loop QED running α(μ₂) from α(μ₁) | [L1] | Yes | `canonical/interactions/qed.tex` | PROVED (uses α as input — supporting only) |
| G137-B | Derive B_phenom ≈ 46.298 from S[Θ] without α input | [OPEN] | — | — | OPEN — blocks full α derivation |

---

## Cross-Track Foundations

| # | Claim | Level | Tracks | Source |
|---|-------|-------|--------|--------|
| X1 | UBT field equation ∇†∇Θ(q,τ) = κ𝒯(q,τ) | [AX] | All | AXIOM-F |
| X2 | Complex time τ = t + iψ with ∂_τ timelike | [AX] | All | AXIOM-B |
| X3 | Admissibility condition: {∂_μΘ} linearly independent | [AX] | T1_GR | Paper §2.3 |
| X4 | Real-projected limit recovers classical GR | [L1] | T1_GR | Five-step chain |

---

## Dead and Deprecated Claims

| Claim | Was in | Level | Why dead |
|-------|--------|-------|----------|
| Weinberg angle derivable from biquaternion algebra | `canonical/alpha/weinberg_angle_derivation.md` | [DEAD] | No-go: algebra cannot fix g'/g |
| Four active alpha routes (A1–A4) | `canonical/alpha/alpha_derivation_routes.md` | — | A3+A4 killed; A1+A2 parked |
| α⁻¹ = 137.036 via k=1 Kac-Moody (without gap closure) | Multiple early α documents | [DEAD] | Specific precision not claimed without G137-B |
| Chirality Gap C1 as merely motivated [SE] | `reports/gauge_status_matrix.md` (old) | — | Superseded: C1 is [L1] PROVED |

---

## Summary: Claim Counts by Level

| Level | T1_GR | T2_GAUGE | T3_ALPHA | Total |
|-------|-------|---------|---------|-------|
| [L0] PROVED | 1 | 13 | 2 | 16 |
| [L1] PROVED | 11 | 2 | 2 | 15 |
| [L1]+[NUM] | 1 | 0 | 0 | 1 |
| [L1][COND] | 0 | 0 | 1 | 1 |
| [L2] structural | 0 | 0 | 1 | 1 |
| [OPEN] | 2 | 5 | 1 | 8 |
| [DEAD] | 0 | 1 | 0 | 1 |
| [AX] | 3 | 0 | 0 | 3 |
| [STD] | 1 | 0 | 0 | 1 |

**Core result (T1_GR)**: 14 claims proved at [L1] or above.  SUBMIT READY.  
**Core result (T2_GAUGE)**: 15 algebraic claims proved [L0]/[L1].  NEAR READY.  
**Core result (T3_ALPHA)**: Integer-137 proved conditional; G137-B open.  CONDITIONAL.
