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
| SU(3)_c from involutions on ℂ⊗ℍ | **Proved [L0]** ⭐ **CANONICAL** | `consolidation_project/appendix_G_internal_color_symmetry.tex`, `consolidation_project/SU3_derivation/step1_involution_summary.tex` | Theorems G.A–G.D: Lie algebra 𝔰𝔲(3), fundamental rep (quarks), adjoint rep (gluons), EW decoupling — all proved; confinement gap remains (Clay Millennium Problem) |
| SU(3)_c from quantum superposition over {I,J,K} | **Proved [L0]** | `consolidation_project/SU3_derivation/step1_superposition_approach.tex`, `tools/verify_su3_superposition.py` | Complementary to involution approach (v46); Θ_color = α·I+β·J+γ·K ∈ ℂ³; U(3) symmetry → SU(3) after U(1)_Y; involutions P_I,P_J,P_K give ℤ₂×ℤ₂ skeleton; all 8 Gell-Mann generators verified numerically; dim(Im ℍ)=3 forces SU(3) with zero free parameters |
| SU(3)_c via i,j,k → r,g,b axis mapping | **[HEURISTIC / MOTIVATING SKETCH]** | `Appendix_G_Emergent_SU3.tex` | Intuitive correspondence only; NOT an algebraic proof; see disclaimer at top of that file; canonical derivation is involution approach above |
| SU(3) via one-hot qubit embedding φ: su(3)→End(ℂ⁸) | **[MATHEMATICAL SANDBOX]** | `THEORY_COMPARISONS/su3_qubit_mapping/` | Valid Lie algebra homomorphism (51 tests pass); separate from mainline UBT derivation; does not derive SU(3) from ℂ⊗ℍ first principles |
| Color confinement (algebraic) | **[CONJECTURED L0]** | `consolidation_project/confinement/algebraic_confinement.tex`, `consolidation_project/confinement/confinement_verification.py` | H_phys = Im(Π_color) in ℂ²⊗ℂ²⊗ℂ²; free quark algebraically inadmissible (not a colour singlet, ⟨C₂⟩=4/3≠0); all hadrons (baryon, meson, tetraquark, pentaquark) verified to satisfy ⟨C₂⟩=0; distinct from Clay Prize (YM mass gap) — see §4 of tex file; needs peer review |
| Weinberg angle θ_W fixed | **Semi-empirical** | `consolidation_project/appendix_E2_SM_geometry.tex §6` | Cannot be fixed by ℂ⊗ℍ alone |
| SU(2)_L chirality (not SU(2)_L×SU(2)_R) | **Proved [L1]** | `consolidation_project/chirality_derivation/step1_psi_parity.tex`, `step2_chirality_result.tex`, `step3_gap_C1_resolution.tex` | ψ-parity P_ψ acts as γ⁵ (Proved); odd winding n>0 = left-handed (Proved); Gap C1 closed: W± vertex P_ψ-odd because no W_R coupling in S[Θ] (Thm. gap_C1) — see step3 |

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
| Hecke eigenvalue conjecture (k=2,4,6) | **Supported by numerical evidence (p=137: 0.4%+3.1%, p=139: 0.05%+1.6%)** | `research_tracks/three_generations/step6_hecke_matches.tex` | SageMath found matching triples at both p=137 and p=139; LMFDB scripts written: identify_lmfdb_labels.py, check_shimura_lift.py; David runs locally |
| CM k=6 forms at any level | **Dead End** | `research_tracks/three_generations/step5_hecke_search_results.tex §5.2`, `research_tracks/three_generations/step6_nonCM_search.tex` | \|a_137\| ~ 439371 ≫ 81400; structural impossibility |
| Non-CM k=6 forms, N≤4 | **Dead End** | `research_tracks/three_generations/step5_hecke_search_results.tex` | No non-CM forms exist at these levels |
| Non-CM k=6 forms, N∈[50,500] | **Extended Dead End** | `research_tracks/three_generations/step6_nonCM_search.tex`, `research_tracks/three_generations/nonCM_search_results.json` | Structurally possible (Sato-Tate); ~0.84 matches expected; unsearched pending LMFDB/SageMath access |

### Lepton Sector Parameter Audit

The following table classifies every parameter appearing in the two lepton-mass
formulas by whether it is **Structural** (fixed by algebra/topology, no fit) or
**Semi-empirical** (requires ≥1 calibration to experiment).
Full justification: `reports/lepton_audit/publication_readiness.md`.

| Parameter / Result | Label | File | Notes |
|--------------------|-------|------|-------|
| KK eigenvalue formula form E_{n,m} = (1/R)√[(n+δ)²+m²] | **Structural** | `consolidation_project/appendix_W2_lepton_spectrum.tex` | Form of Dirac operator on T² with Hosotani shift; no fit |
| Hosotani shift δ = ½ | **Structural** | `consolidation_project/appendix_W2_lepton_spectrum.tex §W.4` | Fixed by Q=−1, θ_H=π; derived from U(1)_EM coupling |
| R = 1/m_e (torus radius) | **Semi-empirical** | `reports/lepton_audit/canonical_derivation.md` | One calibration to set overall mass scale |
| KK mismatch (E_{0,2}/E_{0,1} ≈ 1.844 ≠ 207) | **Structural** | `reports/lepton_audit/status_summary.md` | Theorem: ratio ≤ 2 for any real modulus; not a failure but an honest gap |
| Hopfion formula form m(n) = A·n^p − B_m·n·ln(n) | **Structural** | `STATUS_FERMIONS.md §4`, `reports/lepton_audit/equations.md` | Functional form motivated by one-loop effective potential; no free parameters in the form |
| A (hopfion mass scale) | **Semi-empirical** | `reports/lepton_audit/parameter_table.csv` | Fitted to m_e; Gap M1: derive from soliton tension |
| p (topological winding exponent) | **Semi-empirical** | `reports/lepton_audit/parameter_table.csv` | Fitted to (m_μ, m_τ); Gap M2: derive from soliton stability |
| B_m (log correction in mass formula) | **Semi-empirical** | `reports/lepton_audit/parameter_table.csv` | Fitted to (m_μ, m_τ); Gap M3: derive from loop corrections |
| m_e prediction at 0.22% | **Semi-empirical** | `reports/lepton_audit/reproduction.md` | Post-fit cross-check, not a zero-parameter prediction |
| m_μ/m_e ≈ 207, m_τ/m_μ ≈ 16.8 | **Not reproduced** | `reports/lepton_audit/status_summary.md` | KK mismatch theorem forbids reproduction from W2 formula; Gap M4 |

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

## QM Emergence from Complex Time (Track: CORE)

*Added 2026-03-06. Source verification: `consolidation_project/FPE_verification/`.*

| Result | Status | File | Notes |
|--------|--------|------|-------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) algebra isomorphism | **Proven** [L0] | `consolidation_project/FPE_verification/step3_dirac_emergence.tex §2` | Standard algebra; generators map to Pauli matrices |
| Pauli matrices σᵢ from quaternion generators | **Proven** [L0] | `consolidation_project/FPE_verification/step3_dirac_emergence.tex §3` | Direct from isomorphism; not postulated |
| Dirac γ^μ from ℂ⊗ℍ ⊗ ℂ⊗ℍ tensor product | **Proven** [L0] | `consolidation_project/FPE_verification/step3_dirac_emergence.tex §4` | γ^μ in Weyl rep. = σ₁⊗𝟙, iσ₂⊗σᵢ; Clifford relation verified |
| Dirac-like operator 𝒟 = iγ^μ∇_μ uniquely determined | **Proven** [L0] | `ubt/operators/dirac_like_operator.tex Thm. 2.1` | Unique up to gauge equivalence from bundle structure |
| Schrödinger structure from Im(∂_τΘ = □Θ) | **Sketch** [L0] | `consolidation_project/FPE_verification/step2_schrodinger_emergence.tex §5` | ∂_ψΦ = −2i∇²Φ follows analytically; diffusion coeff. 𝒟=ℏ/(2m) is assumed (Gap S1) |
| UBT ψ is physical — NOT a Wick rotation | **Proven** [L0] | `THEORY/math/fields/biquaternion_time.tex §5.1` | ψ∈ℝ is dynamical; Wick rotation is formal analytic continuation only |
| Biquaternionic FPE with Θ = Σ exp[πB(n)·H(T)] | **Sketch** [L0] | `consolidation_project/FPE_verification/step1_fpe_check.tex` | Scalar sector numerically verified (see tools/verify_fpe.py); three gaps remain: G1 (A(Q) assumed), G2 (consistency condition on H), G3 (non-commutativity) |
| Massless Dirac equation from 𝒟Θ = 0 (spinorial sector) | **Sketch** [L0] | `consolidation_project/FPE_verification/step3_dirac_emergence.tex §6` | Algebraic structure proved; spinorial subspace constraint not derived from S[Θ] (Gap D1) |
| Born rule |Θ|² = probability density | **Proved [L0]** | `consolidation_project/FPE_verification/step7_born_rule.tex` | Sc[Θ†Θ] is conserved by FPE (∂_T∫P dQ=0); Born rule follows without postulate; see step7 |
| QM unification via drift-diffusion | **Sketch** [L0] | `consolidation_project/appendix_FORMAL_qm_gr_unification.tex` | Madelung equations reproduced; specific parameter choices needed (see Step 2) |
| FPE ↔ Euler–Lagrange equivalence (scalar sector) | **Proven** [L0] | `consolidation_project/FPE_verification/step4_fpe_equivalence.tex` | Algebraic identity under conditions C1 (∇²H=0) and C2 (∇H⊥∇Θ); script tools/verify_fpe_equivalence.py — ALL CHECKS PASSED |
| Three projections: GR, QM, statistical mechanics | **Proven** [L0] | `consolidation_project/FPE_verification/step4_fpe_equivalence.tex §4` | Re(∂_tΘ=□Θ) → GR/KG; Im(∂_ψΘ=□Θ) → QM/Schrödinger; full FPE → stat.mech. Definitionally equivalent projections of one field equation, not emergent |

### Open Sub-Tasks (QM Emergence Gaps)

| Gap | Description | Priority |
|-----|-------------|----------|
| G1 | Derive drift A(Q) = −∇H from S[Θ] via Euler-Lagrange | HIGH |
| G2 | Prove consistency condition on H for general biquaternionic case | HIGH |
| G3 | Non-commutative FPE ordering: **PARTIALLY RESOLVED** — [∂_T, ∇_Q²]=0 proved; left FPE from S[Θ]; scalar-Hamiltonian case closed; vector potential case checked separately | MEDIUM |
| S1 | Derive diffusion coefficient 𝒟_eff = ℏ/(2m) from S[Θ] | HIGH |
| D1 | Spinorial subspace: **CLOSED** — Θ₁ (n=1 mode) transforms as Dirac spinor via winding + SL(2,C) spinor rep; see step6_spinorial_subspace.tex | HIGH |

---

## QED Reproducibility at φ = const (Track: CORE)

*Added 2026-03-06. Task: UBT\_v29\_task7\_qed\_phi\_const.*
*Source: `consolidation_project/qed_phi_const/`. Script: `tools/verify_qed_phi_const.py`.*

This section tracks the stronger QED constraint: UBT must reproduce standard QED not
only at φ=0 (vacuum limit, previously verified) but for any constant scalar background
φ = const ≠ 0 (cosmological background, Higgs-vev analog).

| Result | Status | File | Notes |
|--------|--------|------|-------|
| U(1)\_EM unbroken at φ=const | **Proven** [L0] | `consolidation_project/qed_phi_const/step1_u1_protection.tex` | q\_φ=0 (neutral scalar); m²\_γ=0 exact; no Higgs mechanism for EM |
| Electron mass m\_e=y·v at φ=const | **Sketch** [L1] | `consolidation_project/qed_phi_const/step2_electron_mass.tex` | Structural: identical to SM Higgs; Gaps Y1 (derive y) and Y2 (derive v) open |
| δB(φ)=0 at one loop — α(μ) running unchanged | **Proven** [L1] | `consolidation_project/qed_phi_const/step3_beta_function.tex` | Outcome A: UV divergence mass-independent; φ-loop absent (q\_φ=0); standard QED running exact |
| Schwinger term a\_e=α/(2π) at φ=const | **Proven** [L1] | `consolidation_project/qed_phi_const/step4_schwinger_term.tex` | Massless photon (Step 1) + Dirac vertex (Step 2) → identical 1-loop diagram; φ-correction ~10⁻¹⁶ (unobservable) |
| Lamb shift 1057.8 MHz at φ=const | **Sketch** [L1] | `consolidation_project/qed_phi_const/step5_lamb_shift.tex` | Structural: reduction to Steps 1–4 complete; explicit UBT path-integral computation lacking (Gap L1) |
| QED reproducibility summary | **Substantially Proved** [L1] | `consolidation_project/qed_phi_const/step6_qed_summary.tex` | 3 proved + 2 sketch; minimum criterion (U(1)\_EM unbroken) met; script passes all checks |

### Open Sub-Tasks (QED φ=const Gaps)

| Gap | Description | Priority |
|-----|-------------|----------|
| Y1 | Derive Yukawa coupling y from S[Θ] | HIGH |
| Y2 | Derive VEV v from V\_eff(θ₀) on ψ-circle | HIGH |
| L1 | Explicit UBT path-integral Lamb-shift computation at φ=const | MEDIUM |

### UBT Predictions from φ-Background

| Prediction | Value | Observable | Notes |
|------------|-------|-----------|-------|
| P-QED-1 | δα/α ~ 10⁻²¹ at 2-loop | α running | Spatial variation of α in cosmological φ-background |
| P-QED-2 | δa\_e ~ 10⁻¹⁶ | electron g-2 | Below current sensitivity ~10⁻¹³ |

---

*Last updated: 2026-03-06. See STATUS_ALPHA.md, docs/PROOFKIT_ALPHA.md for details.*

---

## Chirality Derivation — SU(2)_L Selection (Track: CORE)

*Added 2026-03-06. Task: UBT_v29_task2_chirality. Source: `consolidation_project/chirality_derivation/`.*

| Result | Status | File | Notes |
|--------|--------|------|-------|
| ℍ gives SU(2)_L × SU(2)_R from left/right actions | **Proven** [L0] | `consolidation_project/appendix_E2_SM_geometry.tex §5` | Inn(ℍ)_L × Inn(ℍ)_R ≅ Spin(4); selection mechanism needed |
| P_ψ maps modes n → -n (ψ-parity) | **Proven** [L0] | `consolidation_project/chirality_derivation/step1_psi_parity.tex §2` | Def. 1; exact algebraic statement |
| ∂_ψ anti-commutes with P_ψ | **Proven** [L0] | `consolidation_project/chirality_derivation/step1_psi_parity.tex §3` | Lem. 2; direct calculation |
| P_ψ acts as γ⁵ in ψ-sector | **Proven** [L0] | `consolidation_project/chirality_derivation/step1_psi_parity.tex §4` | Prop. 3; [P_ψ, γ^μ∇_μ]=0 and {P_ψ, γ⁵∂_ψ}=0 |
| Preferred ψ-circle orientation (matter n>0 by CPT) | **Proven** [L0] | `consolidation_project/chirality_derivation/step1_psi_parity.tex §5` | Lem. 4; P_ψ = CP in ψ-sector |
| SU(2)_L on odd modes ℋ₋ | **Proved [L1]** | `consolidation_project/chirality_derivation/step1_psi_parity.tex §6`, `step3_gap_C1_resolution.tex` | Thm. 5; Gap C1 closed (no W_R in S[Θ]) — proved from S[Θ] action |

### Open Sub-Tasks (Chirality Gaps)

| Gap | Description | Priority |
|-----|-------------|----------|
| C1 | W± vertex P_ψ-odd from S[Θ]: **CLOSED** — no W_R in S[Θ]; see step3_gap_C1_resolution.tex | HIGH |

---

## 8π Common Origin (Track: CORE)

*Added 2026-03-06. Task: UBT_v29_task3_8pi. Source: `consolidation_project/8pi_common_origin.tex`. Script: `tools/verify_8pi_connection.py`.*

| Result | Status | File | Notes |
|--------|--------|------|-------|
| 8π in G_μν = 8πG T_μν from dim(ℍ) | **Structural** [L0] | `consolidation_project/8pi_common_origin.tex §2` | 16πG = dim_ℝ(ℍ) × vol(S²) × G = 4 × 4π × G; structural not coincidental |
| B₀ = 8π from dim_ℂ(ℂ⊗ℍ) = 4 | **Proven** [L1] | `consolidation_project/8pi_common_origin.tex §3`, `consolidation_project/N_eff_derivation/step2_vacuum_polarization.tex` | B₀ = 2π × dim_ℂ(ℂ⊗ℍ) = 8π; script verify_8pi_connection.py ALL PASS |
| Common algebraic ancestor: dim 4 | **Structural** [L0] | `consolidation_project/8pi_common_origin.tex §4` | dim_ℝ(ℍ) = dim_ℂ(Mat(2,ℂ)) = 4; both 8π's share this factor |
| N_phases = 3 and spin-trace = 1/3: algebraically independent | **Proven** [L0] | `consolidation_project/8pi_common_origin.tex §3 Thm. 3` | Numerical equality in d=4 is coincidental; cancellation gives dim_ℂ(ℂ⊗ℍ) = 4 |
| Unified theorem: single origin for both 8π's | **Open** | `consolidation_project/8pi_common_origin.tex §5` | Would require deriving 1/(16πG) from S[Θ] directly; deep unification OPEN |

---

## FPE Equivalence — QM/GR/Stat-Mech Unification (Track: CORE)

*Added 2026-03-06. Task: UBT_v29_task1_fpe_equivalence. Source: `consolidation_project/FPE_verification/step4_fpe_equivalence.tex`. Script: `tools/verify_fpe_equivalence.py`.*

| Result | Status | File | Notes |
|--------|--------|------|-------|
| FPE ↔ E-L equivalence (scalar, free field) | **Proven** [L0] | `step4_fpe_equivalence.tex Thm. 1` | Algebraic identity: both reduce to ∂_TΘ = D∇²Θ under C1,C2 |
| Norm conservation from FPE | **Proven** [L0] | `step4_fpe_equivalence.tex Prop. 2` | d/dT ∫\|Θ\|² dQ = 0; Born rule consistent without extra postulate |
| Projection A: Re sector → GR/KG | **Proven** [L0] | `step4_fpe_equivalence.tex §4` | Re(∂_tΘ=□Θ) = GR sector; confirmed numerically |
| Projection B: Im sector → QM/Schrödinger | **Sketch** | `step4_fpe_equivalence.tex §4` | Im(∂_ψΘ=□Θ) → QM; Gap S1 (D=ℏ/2m) remains |
| Projection C: Full FPE → statistical mechanics | **Proven** [L0] | `step4_fpe_equivalence.tex §4` | FPE IS stat.mech. by construction |
| FPE ↔ E-L (full biquaternionic) | **Partially Proved** | `step4_fpe_equivalence.tex §6`, `step5_noncommutativity.tex` | [∂_T,∇_Q²]=0; left FPE from S[Θ]; scalar-H case closed; Gap G3 reduced |

**Strongest unification result**: QM, GR, and statistical mechanics are definitionally equivalent projections of ∂_TΘ = D∇²Θ — not emergent from a deeper layer.

---

## GR Recovery Status (v48+, updated 2026-03-06)

*Updated 2026-03-06 after v48 review.  Tasks: GR_closure Tasks 1–4 (step1_metric_bridge, step2_nondegeneracy, step3_signature_theorem with AXIOM B section).*

```
GR RECOVERY STATUS (v48+):
"UBT admits an exact variational GR sector (metric+Θ formulation)
and an emergent-metric construction strongly connected to Θ.
```

### Proved

| Result | Status | File | Notes |
|--------|--------|------|-------|
| G_μν = 8πG T_μν from δS_total[g,Θ]/δg^μν = 0 | **Proven** [L1] | `consolidation_project/T_munu_derivation/step3_einstein_with_matter.tex` | Hilbert variation; standard variational GR sector |
| T_μν from Hilbert prescription | **Proven** [L1] | `consolidation_project/T_munu_derivation/step3_einstein_with_matter.tex` | δS_matter/δg^μν = -(√-g/2)T_μν |
| ∇^μ T_μν = 0 from Bianchi identity | **Proven** [L1] | `consolidation_project/T_munu_derivation/step3_einstein_with_matter.tex` | Contracted Bianchi; no free parameters |
| Lorentzian signature (-,+,+,+) from AXIOM B | **Proven** [L0] | `consolidation_project/GR_closure/step3_signature_theorem.tex §Lorentzian Signature from AXIOM B` | Complex time τ=t+iψ → Cl_{1,3}(ℝ) → e₀²=-1 → g₀₀<0; signature is theorem not choice |
| Metric non-degeneracy for A_UBT class | **Proven** [L0] | `consolidation_project/GR_closure/step2_nondegeneracy.tex` | Linear independence of ∂_μΘ ↔ det(g)≠0; degenerate configs explicitly identified |
| Derivative-based ≡ tetrad-based metric formula | **Proven** [L0] | `consolidation_project/GR_closure/step1_metric_bridge.tex` | Under E_μ = ∂_μΘ; single canonical metric definition |

### Conditional (under assumptions A1–A3)

| Result | Status | File | Notes |
|--------|--------|------|-------|
| GR equivalence via tetrad pipeline | **Conditional** | `consolidation_project/appendix_R_GR_equivalence.tex` | Requires Hermitian tetrad (A1), torsion-free (A2), invertible tetrad (A3) |
| Θ-only closure (on-shell) | **Proved on-shell** | `consolidation_project/GR_closure/step2_theta_only_closure.tex` | Equivalent to Einstein eq. at Θ satisfying E-L; off-shell requires injectivity of g[Θ] |

### Not Yet Proved

| Result | Status | Notes |
|--------|--------|-------|
| Pure Θ-only closure (g[Θ] substitution before variation, off-shell) | **Open** | Requires proving injectivity of Θ↦g[Θ] globally; genericity argument only |
| Metric uniqueness beyond A_UBT | **Open** | No proof that g[Θ] is unique outside admissible class |

