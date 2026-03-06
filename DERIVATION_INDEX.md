<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# DERIVATION_INDEX.md — UBT Derivation Status Index

This index tracks the derivation status of every major theoretical result in UBT.
Labels follow the Layer convention: [L0] = pure biquaternionic geometry, [L1] = one-loop,
[L2] = higher-loop or non-perturbative.

Status labels:
- **Proven** — rigorous derivation exists; no free parameters
- **Semi-empirical** — structural derivation with ≥1 unexplained parameter
- **Conjecture** — proposed but not derived; hypotheses stated explicitly
- **Open Hard Problem** — no known approach reproduces the result
- **Dead End** — approach proved to fail; documented for completeness

---

## Fine Structure Constant (α)

| Result | Status | File | Notes |
|--------|--------|------|-------|
| Complex time compactification | **Proven** [L0] | `STATUS_ALPHA.md §2` | From unitarity + gauge consistency |
| Dirac quantisation condition | **Proven** [L0] | `STATUS_ALPHA.md §2` | Single-valuedness of charged fields |
| Effective potential V_eff(n) form | **Proven** [L1] | `STATUS_ALPHA.md §4` | One-loop structure |
| Prime stability constraint | **Proven** [L0] | `STATUS_ALPHA.md §3` | Homotopy theory |
| N_eff = 12 from SM gauge group | **Proven** [L0] | `STATUS_ALPHA.md §5`, `consolidation_project/N_eff_derivation/step1_mode_decomposition.tex` (Theorem 1.4), `consolidation_project/N_eff_derivation/step3_N_eff_result.tex` | 3×2×2 = N_phases × N_helicity × N_charge; N_phases = 3 from dim Im(ℍ) = 3 (not from SU(3)); zero free parameters; derived from ℂ⊗ℍ algebra alone — see N_eff_derivation/ chain |
| B₀ = 25.1 (one-loop baseline) | **Proven** [L1] | `STATUS_ALPHA.md §5`, `consolidation_project/N_eff_derivation/step2_vacuum_polarization.tex` (Theorem 3.1), `consolidation_project/N_eff_derivation/verify_N_eff.py` | B₀ = 2π·N_eff/3 = 8π ≈ 25.133; zero-free-parameter result from S_kin[Θ]; QED limit N_eff=1 → B₀=2π/3 verified |
| B_base = N_eff^{3/2} = 41.57 | **Open Hard Problem** [L0] | `STATUS_ALPHA.md §9`, `consolidation_project/appendix_ALPHA_one_loop_biquat.tex §B.3`, `tools/compute_B_KK_sum.py` | Three approaches tested (KK sum, zeta, gauge orbit volume); all give HONEST GAP / DEAD END — OPEN PROBLEM A |
| R ≈ 1.114 (correction factor) | **Open Hard Problem** | `docs/PROOFKIT_ALPHA.md §5` | Geometric origin unknown; OPEN PROBLEM B |
| α⁻¹ = 137 (bare value) | **Semi-empirical** | `STATUS_ALPHA.md` | Follows from framework given B=46.3 |
| α⁻¹ = 137.036 (full value) | **Semi-empirical** | `STATUS_ALPHA.md` | + two-loop QED correction |
| Non-circularity test | **Verified** | `validation/validate_B_coefficient.py` | Different N_eff → different n* |
| Self-consistency equation n\*·α + g(α) = 1 | **Dead End** [L2] | `appendix_E_m0_derivation_strict.tex §E.8`, `tools/alpha_selfconsistency.py` | No natural UBT cutoff independent of m_e gives <1% error; best geometric cutoff (Λ = m_e/√α) gives 0.83%; pair-threshold (Λ = 2m_e) gives 0.22% but uses m_e as input — [HYPOTHESIS] pending independent derivation of Λ ≈ 1.90·m_e |
| m_0 from torus geometry (U_geom = −C/(R_t·R_ψ)) | **Semi-empirical** [L1] | `appendix_E_m0_derivation_strict.tex §E.4`, `tools/m0_from_torus.py` | α_predicted = C/(2A) derived from stationarity without α as input [SKETCH]; m_0 trivially zero for n=1; requires C computed from ℒ_geom |
| R_ψ independent topological fixation | **Dead End** [L0] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §2`, `docs/ALPHA_FROM_ME_ANALYSIS.md §6.2` | All three candidates (self-duality, winding consistency, modularity) fail; R_ψ = ℏ/(m_e·c) remains [CALIBRATED] |

---

## Standard Model Gauge Group

| Result | Status | File | Notes |
|--------|--------|------|-------|
| B = ℂ⊗ₐℍ ≅ Mat(2,ℂ) | **Proven** [L0] | `consolidation_project/appendix_E2_SM_geometry.tex §1` | Standard algebra isomorphism |
| Aut(B) ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂ | **Proven** [L0] | `consolidation_project/appendix_E2_SM_geometry.tex §1` | Standard result |
| SU(2)_L from left action | **Proven** [L0] | `consolidation_project/appendix_E2_SM_geometry.tex §6` | Generators T^a: M → (iσ^a/2)M |
| [T^a, T^b] = ε^{abc}T^c | **Proven** [L0] | `consolidation_project/appendix_E2_SM_geometry.tex §6` | Direct computation |
| U(1)_Y from right action | **Proven** [L0] | `consolidation_project/appendix_E2_SM_geometry.tex §6` | Θ → e^{-iθ}Θ |
| U(1)_EM from ψ-cycle phase | **Proven** [L0] | `canonical/interactions/qed.tex` | Phase of Θ on ψ-circle |
| SU(3) from ℂ⊗ₐ𝕆 extension | **Semi-empirical** [Track B] | `consolidation_project/appendix_E2_SM_geometry.tex §2` | Octonionic completion hypothesis |
| Weinberg angle θ_W fixed | **Semi-empirical** | `consolidation_project/appendix_E2_SM_geometry.tex §6` | Cannot be fixed by ℂ⊗ℍ alone |
| SU(2)_L chirality (not SU(2)_L×SU(2)_R) | **Semi-empirical** | `consolidation_project/appendix_E2_SM_geometry.tex §6` | ψ-parity Option A; not yet derived |

---

## Three Fermion Generations

| Result | Status | File | Notes |
|--------|--------|------|-------|
| ψ-modes as independent B-fields | **Proven** [L0] | `research_tracks/three_generations/st3_complex_time_generations.tex §3` | From power-series structure |
| Modes carry same SU(3) quantum numbers | **Proven** [L0] | `research_tracks/three_generations/st3_complex_time_generations.tex §3` | SU(3) commutes with ψ |
| ψ-parity forbids even↔odd mixing | **Proven** [L0] | `research_tracks/three_generations/st3_complex_time_generations.tex §4` | Symmetry argument |
| KK mismatch (ratio 1:2 vs 207:3477) | **Proven** [L0] | `research_tracks/three_generations/st3_complex_time_generations.tex §7` | [DERIVED — mismatch is a theorem] |
| Option A (linear mixing) reproduces ratios | **Dead End** | `research_tracks/three_generations/st3_complex_time_generations.tex §7` | Max ratio ~461, far below 3477 |
| Option B (linear Yukawa) reproduces ratios | **Dead End** | `research_tracks/three_generations/st3_complex_time_generations.tex §7` | Ratio 1:2:3 only |
| Option C (ψ-instantons) reproduces ratios | **Open Hard Problem** | `research_tracks/three_generations/st3_complex_time_generations.tex §7` | Calibrated to muon; tau off by factor ~6 |
| Identification Θ₀/Θ₁/Θ₂ ↔ e/μ/τ | **Conjecture** | `research_tracks/three_generations/st3_complex_time_generations.tex §5` | Mass ratios not reproduced |
| Mass ratio script (Options A/B/C) | Documented | `tools/reproduce_lepton_ratios.py` | Exit code 1 = no mechanism works |
| Hecke eigenvalue conjecture (k=2,4,6) | **Supported by numerical evidence (p=137: 0.4%+3.1%, p=139: 0.05%+1.6%)** | `research_tracks/three_generations/step6_hecke_matches.tex` | SageMath found matching triples at both p=137 and p=139; LMFDB verification pending |
| CM k=6 forms at any level | **Dead End** | `research_tracks/three_generations/step5_hecke_search_results.tex §5.2`, `research_tracks/three_generations/step6_nonCM_search.tex` | \|a_137\| ~ 439371 ≫ 81400; structural impossibility |
| Non-CM k=6 forms, N≤4 | **Dead End** | `research_tracks/three_generations/step5_hecke_search_results.tex` | No non-CM forms exist at these levels |
| Non-CM k=6 forms, N∈[50,500] | **Extended Dead End** | `research_tracks/three_generations/step6_nonCM_search.tex`, `research_tracks/three_generations/nonCM_search_results.json` | Structurally possible (Sato-Tate); ~0.84 matches expected; unsearched pending LMFDB/SageMath access |

---

---

## Prime Attractor Theorem

| Result | Status | File | Notes |
|--------|--------|------|-------|
| Prime selection by V_eff(n) minimum | **Proven** [L1] | `STATUS_ALPHA.md §4`, `Appendix_H_Theta_Phase_Emergence.tex §H.7a` | Robust regardless of coupling type |
| Coupling type from ∇†∇Θ = κ𝒯 | **Derived** [L1] | `Appendix_H_Theta_Phase_Emergence.tex §H.7a`, `tests/test_prime_attractor_stability.py` | Substitution gives ADDITIVE coupling j+m-k=n (three-index constraint) |
| Multiplicative coupling k·m=n | **Dead End** (standard QFT) | `Appendix_H_Theta_Phase_Emergence.tex §H.7a` | Not from ∇†∇Θ with standard self-interaction |
| Topological winding interaction | **Conjecture** | `Appendix_H_Theta_Phase_Emergence.tex §H.7a §H.7a.2` | Could give multiplicative coupling; no derivation |
| Prime attractor (mode coupling) | **Dead End** (additive coupling) | `Appendix_H_Theta_Phase_Emergence.tex §H.7a`, `tests/test_prime_attractor_stability.py` | Additive coupling gives no prime preference |
| Prime selection (V_eff minimum) | **Proven** | `STATUS_ALPHA.md §4` | Independent of coupling type; robust claim |

---

## φ-Universe Parameter and h_μν Vacuum

| Result | Status | File | Notes |
|--------|--------|------|-------|
| φ-projection theorem (P_φ[𝒢_μν] satisfies GR) | **Proven** [L1] | `canonical/geometry/phase_projection.tex` | U(1) automorphism of ℂ⊗ℍ |
| ∂α/∂φ = 2ρr·α(0) formula | **Proven** [L1] | `canonical/geometry/phi_gauge_vs_physical.tex` | Analytic derivation; result depends on vacuum |
| h_μν = 0 for single-mode winding vacuum | **Proven** [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §1.2` | Dead End documented |
| h_μν ≠ 0 two-mode winding vacuum | **Proven** [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §1.3` | h_ψψ = (2/R_ψ²)sin(ψ/R_ψ)·Im[Sc(Θ₀Θ₁†)] |
| r ≈ 4.66 for canonical two-mode vacuum | **Proven** [L1] | `tools/compute_h_munu_vacuum.py` | Numerical; gauge potential formula is SKETCH |
| φ is physical (not pure gauge) for two-mode vacuum | **Proven** [L1] | `docs/PHI_UNIVERSE_PARAMETER.md §4a` | r ≠ 0 → φ is physical |
| ψ↔φ are distinct operations (not equivalent) | **Proven** [L1] | `docs/PHI_UNIVERSE_PARAMETER.md §5a` | Both indexed by primes; different geometric mechanisms |
| dim(ℳ_UBT) ≥ 1 (U(1) moduli) | **Proven** [L1] | `docs/PHI_UNIVERSE_PARAMETER.md §5b` | Scalar phase rotation |
| dim(ℳ_UBT) = 4 (U(1)×Sp(1)) | **Conjecture** | `docs/PHI_UNIVERSE_PARAMETER.md §5b` | Quaternionic extension; gauge vs. physical TBD |

---

## Cross-Gap Consistency Checks

| Check | Status | Notes |
|-------|--------|-------|
| CC1: R_ψ = ℏ/(m_e·c) used consistently | To verify | Gap 1, Gap 4, Gap 6 must use same value |
| CC2: B coefficient layer discipline | OPEN | B needs [L1] derivation; currently uses N_eff from SM (Gap 5) |
| CC3: Prime chain V(ψ) → prime attractor → φ_p | **Partially verified** | ψ_p = φ_p = 2π/p share index structure; distinct geometric mechanisms (see §5a) |

---

*Last updated: 2026-03-05. See STATUS_ALPHA.md, docs/PROOFKIT_ALPHA.md for details.*
