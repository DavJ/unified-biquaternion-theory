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

File role labels (see `docs/AUDITS/repo_overlap_and_canonicalization_report.md`):
- ⭐ **CANONICAL** — single authoritative source; start here
- **supporting** — valid derivation referenced by canonical source
- **heuristic** — intuitive sketch; not a proof
- **sandbox** — exploratory; outputs captured elsewhere
- **speculative** — extrapolates beyond current evidence
- **historical** — superseded; preserved for reference

**Topic index files** (one canonical entry point per topic):
- Fine structure constant: `canonical/THEORY/topic_indexes/alpha_index.md`
- SU(3) color symmetry: `canonical/THEORY/topic_indexes/SU3_index.md`
- GR recovery: `canonical/THEORY/topic_indexes/GR_index.md`
- Hecke / 137–139: `canonical/THEORY/topic_indexes/hecke_index.md`
- Mirror sector: `canonical/THEORY/topic_indexes/mirror_sector_index.md`

---

## Fine Structure Constant (α)

> ⭐ **Canonical source**: `docs/STATUS_ALPHA.md` — complete derivation chain with explicit gap inventory.  
> Topic index: `canonical/THEORY/topic_indexes/alpha_index.md`

| Result | Status | File | Notes |
|--------|--------|------|-------|
| Complex time compactification | **Proven** [L0] | `docs/STATUS_ALPHA.md §2` | From unitarity + gauge consistency |
| Dirac quantisation condition | **Proven** [L0] | `docs/STATUS_ALPHA.md §2` | Single-valuedness of charged fields |
| Effective potential V_eff(n) form | **Proven** [L1] | `docs/STATUS_ALPHA.md §4` | One-loop structure |
| Prime stability constraint | **Proven** [L0] | `docs/STATUS_ALPHA.md §3` | Homotopy theory |
| N_eff = 12 from ℂ⊗ℍ algebra (N_phases = dim Im(ℍ) = 3) | **Proven** [L0] | `docs/STATUS_ALPHA.md §5`, `canonical/n_eff/step1_mode_decomposition.tex` (Theorem 1.4), `canonical/n_eff/step3_N_eff_result.tex` | 3×2×2 = N_phases × N_helicity × N_charge; N_phases = 3 from dim Im(ℍ) = 3 (not from SU(3)); zero free parameters; derived from ℂ⊗ℍ algebra alone — see N_eff_derivation/ chain |
| B₀ = 25.1 (one-loop baseline) | **Proven** [L1] | `docs/STATUS_ALPHA.md §5`, `canonical/n_eff/step2_vacuum_polarization.tex` (Theorem 3.1), `ARCHIVE/archive_legacy/consolidation_project/N_eff_derivation/verify_N_eff.py` | B₀ = 2π·N_eff/3 = 8π ≈ 25.133; zero-free-parameter result from S_kin[Θ]; QED limit N_eff=1 → B₀=2π/3 verified |
| B_base = N_eff^{3/2} = 41.57 | **Partially Proved [L1]** — exponent 3/2 from T³ heat kernel [L0]; N_eff=12 [L1]; C_gauge=1 [L1]; ab initio beta-fn coefficient: **[Open]** | `canonical/interactions/B_base_derivation_complete.tex`, `docs/STATUS_ALPHA.md §9`, `ARCHIVE/archive_legacy/consolidation_project/appendix_ALPHA_one_loop_biquat.tex §B.3`, `tools/compute_B_KK_sum.py`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/b_base_spinor_approach.tex`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/b_base_hausdorff.tex`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/b_base_delta_d.tex`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/b_base_nonpert.tex`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/b_base_new_directions.tex`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/b_base_ncg_a4.tex`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/b_base_g_approaches.tex`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/b_base_kac_moody_level.tex`, `tools/explore_b_exponent.py`, `tools/compute_B_effective_dimension.py` | v48: **Scientific Task 1 — r²_vac = 1/(2π) from canonical norm: [CONFIRMED DEAD END].** Specific question: can ||Θ||²=1 on ψ-circle fix r²_vac=1/(2π) independently of n*? Answer: No — three reasons. (1) The canonical norm Sc[Θ†Θ]=1 directly gives r²=1, not 1/(2π); k=2π·1=2π∉ℤ (non-integer KM level — algebraically inadmissible). (2) No other natural normalisation from ℂ⊗ℍ algebra selects r²=1/(2π): the only dimensionless scale in ℂ⊗ℍ is 1 (unit algebra); 1/(2π) has no origin in the algebraic structure. (3) The only route to r²_vac=1/(2π) proceeds through V_eff minimum at n*=137 (circular). Conclusion: k=1 cannot be derived from canonical norm alone. Status of Gap G3-k: **[CONFIRMED DEAD END — canonical norm route]**; k=1 remains [MOTIVATED CONJECTURE (H2)] but not derived. B_base remains **Partially Proved [L1]** — no upgrade. v67: **Approaches H1/H2/H3 (b_base_kac_moody_level.tex) — Gap G3-k:** Direct computation of Kac-Moody level k from S[Θ]. H1 (WZW normalization): k=2π·r²_vac derived exactly; via V_eff minimum → circular (r²_vac=f(n*)=f(137)); via canonical norm r²=1 → k=2π∉ℤ → [DEAD END (both routes)]. H2 (absence of CS term): CS term proved absent (parity symmetry of mirror sectors n*=137/n**=139 + trivial holonomy); k from free kinetic action alone; minimality principle → k=1 is the unique level of the free-boson/WZW fixed point → [MOTIVATED CONJECTURE: k=1]. H3 (Dynkin index): adjoint rep (natural) → k=3×2=6, c=9/4, B≈93.5≠41.57 [DEAD END]; fundamental rep → k=3×½=3/2, c=9/7≈1.286, B≈53.4≠41.57 [DEAD END]; no natural assignment from ℂ⊗ℍ gives k=1 [DEAD END]. Status upgrade: Gap (G3-k) remains [OPEN] but k=1 is now [MOTIVATED CONJECTURE (H2)], stronger than [PARTIAL] in v65. Formula k=2π·r²_vac proved; CS absence proved; k=1 requires r²_vac=1/(2π) from an independent argument that avoids n*. v65: **Approaches G3/G2/G4/G7/F (b_base_g_approaches.tex):** G3 (Kac-Moody modular anomaly, k=1) → [PARTIAL]: c_{SU(2),1}=1; B = c·N_eff^{3/2} = 41.57 exact; k=1 motivated by free-boson / minimal-coupling but not uniquely forced by UBT axioms; k=N_eff gives c=18/7≈2.571, requires unnatural coeff≈1.35 → [DEAD END]. G2 (Weyl anomaly coefficient) → [DEAD END]: c̃=1/15 rational; required exponent p≈2.65 unnatural. G4 (Fueter mode count) → [DEAD END]: cumulative count 650 or single-degree 36/49; neither equals 41.57. G7 (QK index, ℂ⊗ℍ adjoint over ℍ) → [DEAD END]: ind=4 (flat); dimension-controlled, N_eff-independent. F (non-isotropic D_int=diag(0,1,1,1)) → [DEAD END]: tr(M⁴)=3; no natural combination equals 41.57, confirming prior expectation. New Gap (G3-k): compute Kac-Moody level k from quantisation of S[Θ] on ψ-circle. New Gap (G8): identify modular weight of UBT partition function Ẑ(τ). Overall: 22 approaches tested; A2 [MOTIVATED CONJECTURE] and G3 k=1 [PARTIAL] remain the only positive results. v64: **Approaches F1–F4 (b_base_ncg_a4.tex):** Key correction vs E4: UBT ≠ standard Connes–Lott SM; A = ℂ⊗ℍ ≅ Mat(2,ℂ) alone (not ℂ⊕ℍ⊕Mat(3,ℂ)); H_F = ℂ⁴ (left-regular / adjoint rep), not ℂ^96. F1 (UBT spectral triple, H=ℂ⁴) → [PARTIAL]: a₄^{gauge} = (1/3)tr(F²) for adjoint rep; ratio [a₄]_{ℂ⁴}/[a₄]_{ℂ²} = 4; sign positive (IR-free, consistent with UBT); B_F1 ≈ 4B₀ ≈ 100 ≠ 41.57; next step: non-isotropic D_int. F2 (product spacetime × ℂ⊗ℍ) → [PARTIAL]: a₀^{int}=4 multiplies gauge coupling; N_eff^{(F2)} = 8 ≠ 12; curvature-mass cross-term vanishes on flat spacetime; spectral-action product formula alone insufficient to recover N_eff=12. F3 (Wodzicki residue) → [DEAD END]: Res(D^{-2}) ∝ dim(H_F)=4 on flat space; reduces to same a₄ computation; no new invariant. F4 (spectral invariant search, systematic) → [PARTIAL]: unique exact candidate [dim_ℝ(ℍ)×dim_ℝ(Im ℍ)]^{3/2} = (4×3)^{3/2} = 41.57; algebraic identity only (restatement of N_eff=12 + 3/2 exponent from Gaussian measure); no purely algebraic formula derives the 3/2 exponent. Gap (a) [det(S'')] OPEN. Gap (b) [3/2 exponent protection] PARTIAL from E3. New Gap (F) [non-isotropic D_int]: next concrete step. v61: **Approaches E1–E4 (b_base_new_directions.tex):** E1 (instantons on SU(2)) → [DEAD END]: B_base/B₀ = 1.6540 > 1 requires S_inst = -ln(1.654) ≈ -0.503 < 0; negative instanton action is physically impossible; E2 (index theorem / anomaly on Im(ℍ)) → [DEAD END]: ind(𝒟_{S³}) = 0 (odd-dimensional manifold); chiral anomaly requires non-integer N_f = 4√3 ≈ 6.93 for √N_eff; E3 (holomorphic factorisation) → [DEAD END as new path, STRUCTURAL CONFIRMATION]: Im(ℍ) has odd real dimension 3, admits no complex structure (Prop. E3.1); holomorphic integration over complexification ℂ³ gives exponent d_ℂ = 3 → B = N_eff³ = 1728 (wrong by factor 41.57); confirms real Gaussian (Hausdorff approach) is structurally forced; provides structural argument for Gap (b): 1/2 factor protected by real structure of Im(ℍ) — algebraic fact, not quantum correction; E4 (NCG spectral triple) → [PARTIAL]: N_gen = N_phases = 3 = dim_ℝ(Im ℍ) (same algebraic origin); a₄ ~ N_gen² = 9 from Yukawa; B_base/N_gen² = 4.619 ≈ 3π/2 = 4.712 (2% error) [NUMERICAL OBSERVATION]; explicit a₄ computation for ℂ⊗ℍ spectral triple not yet done. Gap (a) remains OPEN. Gap (b) has PARTIAL PROGRESS from E3. Next direction: explicit a₄ computation in NCG (Gap E4 in b_base_new_directions.tex §6). v60: **Approaches D1–D3 (b_base_nonpert.tex):** D1 (unitarity constraint on Im(ℍ)) → [DEAD END]: constraint reduces N_eff 12→8, moves B in wrong direction; target effective mode count < 1 is algebraically impossible; D2 (dimensional transmutation on Im(ℍ)) → [DEAD END]: requires R_ψ as free parameter (calibrated, not algebraically fixed); D3 (Cartan–Killing metric on su(2)) → [DEAD END]: normalised Killing form = Euclidean (no correction); unnormalised gives B/2 or 2.4×B_base depending on convention. Gap (a) remains OPEN after 8 dead ends. v59: A4 (effective dimension) added: d_eff(B₀) ≈ 2.595 (non-integer, from proved B₀); d_eff(B_base) = 3.000 exactly (= dim_ℝ(Im ℍ)); Gap (a) = explain Δd = 0.405. **Approach C (b_base_delta_d.tex):** C1 (Seeley–DeWitt curvature on Im(ℍ)) → [DEAD END]: correction ∝ Λ⁻² → 0 in UV; C2 (mode pair interference) → [DEAD END]: algebraic identity restatement. Gap (a) remains OPEN. N* = 4π²/9 ≈ 4.39 is N_eff for which d_eff(B₀) = 3 exactly; for N_eff = 12 (UBT) Δd = 0.405 is a derived consequence. v58: A2 (Hausdorff): Lemma (mode space Im(ℍ), d=3, PROVED), Proposition (Gaussian det^{-1/2}, identity), Conjecture (exponent = d/2 = 3/2, MOTIVATED CONJECTURE), Gap §4 ((a) det(S'') not computed; (b) higher-loop protection — both OPEN). Factor 3 = dim_ℝ(Im ℍ); factor 2 = Gaussian. Dead ends: KK sum, zeta, gauge orbit volume. A3 (numerical: x = log(46.284)/log(12) = 1.543, nearest fraction 17/11, deviation from 3/2 explained by R ≠ 1) |
| R ≈ 1.114 (correction factor) | **Open Hard Problem** | `docs/PROOFKIT_ALPHA.md §5`, `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/r_factor_geometry.tex`, `tools/explore_r_factor.py` | v56 results: B1 volume ratios → [DEAD END]; B2 algebraic search: best candidate 1+α(N_eff+π+1/4) ≈ 1.1123, err 0.15% [NUMERICAL OBSERVATION]; 2^(1/6) ≈ 1.1225, err 0.76% [CLOSE]; B3 two-loop on ψ-circle: correct qualitative structure, coefficient c not derived — OPEN PROBLEM B persists |
| α⁻¹ = 137 (bare value) | **Semi-empirical** | `docs/STATUS_ALPHA.md` | Follows from framework given B=46.3 |
| α⁻¹ = 137.036 (full value) | **Semi-empirical** | `docs/STATUS_ALPHA.md` | + two-loop QED correction |
| Non-circularity test | **Verified** | `experiments/validation/validate_B_coefficient.py` | Different N_eff → different n* |
| Self-consistency equation n\*·α + g(α) = 1 | **Dead End** [L2] | `ARCHIVE/archive_legacy/tex/appendix_E_m0_derivation_strict.tex §E.8`, `tools/alpha_selfconsistency.py` | No natural UBT cutoff independent of m_e gives <1% error; best geometric cutoff (Λ = m_e/√α) gives 0.83%; pair-threshold (Λ = 2m_e) gives 0.22% but uses m_e as input — [HYPOTHESIS] pending independent derivation of Λ ≈ 1.90·m_e |
| m_0 from torus geometry (U_geom = −C/(R_t·R_ψ)) | **Semi-empirical** [L1] | `ARCHIVE/archive_legacy/tex/appendix_E_m0_derivation_strict.tex §E.4`, `tools/m0_from_torus.py` | α_predicted = C/(2A) derived from stationarity without α as input [SKETCH]; m_0 trivially zero for n=1; requires C computed from ℒ_geom |
| R_ψ independent topological fixation | **Mechanism [L1]** — T-duality selects self-dual point R_psi = R_t [L1]; physical units require beyond-one-loop: **[Open L2]** | `canonical/geometry/Rpsi_dynamical_fix.tex`, `canonical/geometry/biquaternionic_vacuum_solutions.tex §2`, `docs/ALPHA_FROM_ME_ANALYSIS.md §6.2` | T-duality mechanism [L1]: self-dual point R_psi = R_t is the unique T-duality-invariant extremum of the moduli potential. Physical value in GeV: R_ψ = ℏ/(m_e·c) is [CALIBRATED] — beyond-one-loop derivation needed to fix R_t in physical units [Open L2]. |

---

## Standard Model Gauge Group

> ⭐ **Canonical source for SU(3)**: `canonical/su3_derivation/su3_from_involutions.tex`  
> Topic index: `canonical/THEORY/topic_indexes/SU3_index.md`

| Result | Status | File | Notes |
|--------|--------|------|-------|
| B = ℂ⊗ₐℍ ≅ Mat(2,ℂ) | **Proven** [L0] | `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex §1` | Standard algebra isomorphism |
| Aut(B) ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂ | **Proven** [L0] | `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex §1` | Standard result |
| SU(2)_L from left action | **Proven** [L0] | `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex §6` | Generators T^a: M → (iσ^a/2)M |
| [T^a, T^b] = ε^{abc}T^c | **Proven** [L0] | `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex §6` | Direct computation |
| U(1)_Y from right action | **Proven** [L0] | `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex §6` | Θ → e^{-iθ}Θ |
| U(1)_EM from ψ-cycle phase | **Proven** [L0] | `canonical/interactions/qed.tex` | Phase of Θ on ψ-circle |
| SU(3)_c from involutions on ℂ⊗ℍ | **Proved [L0]** ⭐ **CANONICAL** | `canonical/su3_derivation/su3_from_involutions.tex`, `canonical/su3_derivation/step1_involution_summary.tex` | Theorems G.A–G.D: Lie algebra 𝔰𝔲(3), fundamental rep (quarks), adjoint rep (gluons), EW decoupling — all proved; confinement gap remains (Clay Millennium Problem) |
| SU(3)_c from quantum superposition over {I,J,K} | **Proved [L0]** | `canonical/su3_derivation/step1_superposition_approach.tex`, `tools/verify_su3_superposition.py` | Complementary to involution approach (v46); Θ_color = α·I+β·J+γ·K ∈ ℂ³; U(3) symmetry → SU(3) after U(1)_Y; involutions P_I,P_J,P_K give ℤ₂×ℤ₂ skeleton; all 8 Gell-Mann generators verified numerically; dim(Im ℍ)=3 forces SU(3) with zero free parameters |
| SU(3)_c via i,j,k → r,g,b axis mapping | **[HEURISTIC / MOTIVATING SKETCH]** | `ARCHIVE/archive_legacy/tex/Appendix_G_Emergent_SU3.tex` | Intuitive correspondence only; NOT an algebraic proof; see disclaimer at top of that file; canonical derivation is involution approach above |
| SU(3) via one-hot qubit embedding φ: su(3)→End(ℂ⁸) | **[MATHEMATICAL SANDBOX]** | `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/` | Valid Lie algebra homomorphism (51 tests pass); separate from mainline UBT derivation; does not derive SU(3) from ℂ⊗ℍ first principles |
| Color confinement (algebraic) | **[CONJECTURED WITH EXPERIMENTAL SUPPORT L0]** | `ARCHIVE/archive_legacy/consolidation_project/confinement/algebraic_confinement.tex`, `ARCHIVE/archive_legacy/consolidation_project/confinement/confinement_verification.py` | H_phys = Im(Π_color) in ℂ²⊗ℂ²⊗ℂ²; free quark algebraically inadmissible (not a colour singlet, ⟨C₂⟩=4/3≠0); all hadrons (baryon, meson, tetraquark, pentaquark) verified to satisfy ⟨C₂⟩=0; distinct from Clay Prize (YM mass gap) — see §5; exotic hadrons at LHCb consistent (§6); needs peer review |
| Weinberg angle θ_W fixed | **Semi-empirical** | `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex §6` | Cannot be fixed by ℂ⊗ℍ alone. Structural argument (v47): ℂ⊗ℍ automorphism group provides SU(2)_L × U(1)_Y but g/g' ratio is a free parameter of the embedding; no algebraic constraint on sin²θ_W arises from ℂ⊗ℍ geometry. |
| SU(2)_L chirality (not SU(2)_L×SU(2)_R) | **Proved [L1]** | `canonical/chirality/step1_psi_parity.tex`, `canonical/chirality/step2_chirality_result.tex`, `canonical/chirality/step3_gap_C1_resolution.tex` | ψ-parity P_ψ acts as γ⁵ (Proved); odd winding n>0 = left-handed (Proved); Gap C1 closed: W± vertex P_ψ-odd because no W_R coupling in S[Θ] (Thm. gap_C1) — see step3 |

---

## Three Fermion Generations

> ⭐ **Canonical Hecke sources**: `docs/reports/hecke_lepton/` (numerical) + `research_tracks/hecke_bridge/motivation.tex` (theoretical)  
> Topic index: `canonical/THEORY/topic_indexes/hecke_index.md`

| Result | Status | File | Notes |
|--------|--------|------|-------|
| ψ-modes as independent B-fields | **Proven** [L0] | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex §3` | From power-series structure |
| Modes carry same SU(3) quantum numbers | **Proven** [L0] | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex §3` | SU(3) commutes with ψ |
| ψ-parity forbids even↔odd mixing | **Proven** [L0] | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex §4` | Symmetry argument |
| KK mismatch (ratio 1:2 vs 207:3477) | **Proven** [L0] | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex §7` | [DERIVED — mismatch is a theorem] |
| Option A (linear mixing) reproduces ratios | **Dead End** | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex §7` | Max ratio ~461, far below 3477 |
| Option B (linear Yukawa) reproduces ratios | **Dead End** | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex §7` | Ratio 1:2:3 only |
| Option C (ψ-instantons) reproduces ratios | **Open Hard Problem** | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex §7` | Calibrated to muon; tau off by factor ~6. v47 scan: ±20% variation of S_inst is a Dead End — S_inst required for muon (5.332) and for tau (4.424) differ by 17%; no single S_inst in [4.266, 6.398] simultaneously fits both within 1%. Simple modification of the dilute-gas S_inst is insufficient; non-perturbative resummation or modified instanton action required. |
| Identification Θ₀/Θ₁/Θ₂ ↔ e/μ/τ | **Conjecture** | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex §5` | Mass ratios not reproduced |
| Mass ratio script (Options A/B/C) | Documented | `tools/reproduce_lepton_ratios.py` | Exit code 1 = no mechanism works |
| Hecke conjecture p=137 | **STRONG NUMERICAL SUPPORT** | `docs/reports/hecke_lepton/` | Set A (76.2, 7.4, 208.6): unique global hit p=137 in 50–300; mu_err=0.02%, tau_err=0.10%; 47 other primes far off |
| Hecke twin prime p=139 (mirror sector) | **NUMERICAL OBSERVATION** | `docs/reports/hecke_lepton/mirror_world_139.md` | Set B (195.2, 50.4, 54.6): unique global hit p=139 in 50–300; Sets A and B mutually exclusive on twin primes (137, 139) |
| CM k=6 forms at any level | **Dead End** | `experiments/research_tracks/three_generations/step5_hecke_search_results.tex §5.2`, `experiments/research_tracks/three_generations/step6_nonCM_search.tex` | \|a_137\| ~ 439371 ≫ 81400; structural impossibility |
| Non-CM k=6 forms, N≤4 | **Dead End** | `experiments/research_tracks/three_generations/step5_hecke_search_results.tex` | No non-CM forms exist at these levels |
| Non-CM k=6 forms, N∈[50,500] | **Partially Searched — Open** | `experiments/research_tracks/three_generations/step6_nonCM_search.tex`, `experiments/research_tracks/three_generations/nonCM_search_results.json` | Structurally possible (Sato-Tate); ~0.84 matches expected; unsearched pending LMFDB/SageMath access |

### Lepton Sector Parameter Audit

The following table classifies every parameter appearing in the two lepton-mass
formulas by whether it is **Structural** (fixed by algebra/topology, no fit) or
**Semi-empirical** (requires ≥1 calibration to experiment).
Full justification: `docs/reports/lepton_audit/publication_readiness.md`.

| Parameter / Result | Label | File | Notes |
|--------------------|-------|------|-------|
| KK eigenvalue formula form E_{n,m} = (1/R)√[(n+δ)²+m²] | **Structural** | `ARCHIVE/archive_legacy/consolidation_project/appendix_W2_lepton_spectrum.tex` | Form of Dirac operator on T² with Hosotani shift; no fit |
| Hosotani shift δ = ½ | **Structural** | `ARCHIVE/archive_legacy/consolidation_project/appendix_W2_lepton_spectrum.tex §W.4` | Fixed by Q=−1, θ_H=π; derived from U(1)_EM coupling |
| R = 1/m_e (torus radius) | **Semi-empirical** | `docs/reports/lepton_audit/canonical_derivation.md` | One calibration to set overall mass scale |
| KK mismatch (E_{0,2}/E_{0,1} ≈ 1.844 ≠ 207) | **Structural** | `docs/reports/lepton_audit/status_summary.md` | Theorem: ratio ≤ 2 for any real modulus; not a failure but an honest gap |
| Hopfion formula form m(n) = A·n^p − B_m·n·ln(n) | **Structural** | `ARCHIVE/archive_legacy/historical_versions/status/STATUS_FERMIONS.md §4`, `docs/reports/lepton_audit/equations.md` | Functional form motivated by one-loop effective potential; no free parameters in the form |
| A (hopfion mass scale) | **Semi-empirical** | `docs/reports/lepton_audit/parameter_table.csv` | Fitted to m_e; Gap M1: derive from soliton tension |
| p (topological winding exponent) | **Semi-empirical** | `docs/reports/lepton_audit/parameter_table.csv` | Fitted to (m_μ, m_τ); Gap M2: derive from soliton stability |
| B_m (log correction in mass formula) | **Semi-empirical** | `docs/reports/lepton_audit/parameter_table.csv` | Fitted to (m_μ, m_τ); Gap M3: derive from loop corrections. **Note:** B_m (fermion masses, ≈ −14.099 MeV, dimensionful) is distinct from B_base (α derivation, ≈ 41.57, dimensionless) — different objects, different physics. |
| m_e prediction at 0.22% | **Semi-empirical** | `docs/reports/lepton_audit/reproduction.md` | Post-fit cross-check, not a zero-parameter prediction |
| m_μ/m_e ≈ 207, m_τ/m_μ ≈ 16.8 | **Not reproduced** | `docs/reports/lepton_audit/status_summary.md` | KK mismatch theorem forbids reproduction from W2 formula; Gap M4 |

---

---

## Prime Attractor Theorem

| Result | Status | File | Notes |
|--------|--------|------|-------|
| Prime selection by V_eff(n) minimum | **Proven** [L1] | `docs/STATUS_ALPHA.md §4`, `ARCHIVE/archive_legacy/tex/Appendix_H_Theta_Phase_Emergence.tex §H.7a` | Robust regardless of coupling type |
| Coupling type from ∇†∇Θ = κ𝒯 | **Derived** [L1] | `ARCHIVE/archive_legacy/tex/Appendix_H_Theta_Phase_Emergence.tex §H.7a`, `tests/test_prime_attractor_stability.py` | Substitution gives ADDITIVE coupling j+m-k=n (three-index constraint) |
| Multiplicative coupling k·m=n | **Dead End** (standard QFT) | `ARCHIVE/archive_legacy/tex/Appendix_H_Theta_Phase_Emergence.tex §H.7a` | Not from ∇†∇Θ with standard self-interaction |
| Topological winding interaction | **Conjecture** | `ARCHIVE/archive_legacy/tex/Appendix_H_Theta_Phase_Emergence.tex §H.7a §H.7a.2` | Could give multiplicative coupling; no derivation |
| Prime attractor (mode coupling) | **Dead End** (additive coupling) | `ARCHIVE/archive_legacy/tex/Appendix_H_Theta_Phase_Emergence.tex §H.7a`, `tests/test_prime_attractor_stability.py` | Additive coupling gives no prime preference |
| Prime selection (V_eff minimum) | **Proven** | `docs/STATUS_ALPHA.md §4` | Independent of coupling type; robust claim |

---

## φ-Universe Parameter and h_μν Vacuum

| Result | Status | File | Notes |
|--------|--------|------|-------|
| φ-projection theorem (P_φ[𝒢_μν] satisfies GR) | **Proven** [L1] | `canonical/geometry/phase_projection.tex` | U(1) automorphism of ℂ⊗ℍ |
| ∂α/∂φ = 2ρr·α(0) formula | **Proven** [L1] | `canonical/geometry/phi_gauge_vs_physical.tex` | Analytic derivation; result depends on vacuum |
| h_μν = 0 for single-mode winding vacuum | **Proven** [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §1.2` | Proved [L1]. Earlier approaches were dead ends; current result from biquaternionic_vacuum_solutions.tex §1.2 |
| h_μν ≠ 0 two-mode winding vacuum | **Proven** [L1] | `canonical/geometry/biquaternionic_vacuum_solutions.tex §1.3` | h_ψψ = (2/R_ψ²)sin(ψ/R_ψ)·Im[Sc(Θ₀Θ₁†)] |
| r ≈ 4.66 for canonical two-mode vacuum | **Proven** [L1] | `tools/compute_h_munu_vacuum.py` | Numerical; gauge potential formula is SKETCH |
| φ is physical (not pure gauge) for two-mode vacuum | **Proven** [L1] | `docs/PHI_UNIVERSE_PARAMETER.md §4a` | r ≠ 0 → φ is physical |
| ψ↔φ are distinct operations (not equivalent) | **Proven** [L1] | `docs/PHI_UNIVERSE_PARAMETER.md §5a` | Both indexed by primes; different geometric mechanisms |
| dim(ℳ_UBT) ≥ 1 (U(1) moduli) | **Proven** [L1] | `docs/PHI_UNIVERSE_PARAMETER.md §5b` | Scalar phase rotation |
| dim(ℳ_UBT) = 4 (U(1)×Sp(1)) | **Conjecture** | `docs/PHI_UNIVERSE_PARAMETER.md §5b` | Quaternionic extension; gauge vs. physical TBD |

---

## UBT–Twistor Bridge

> ⭐ **Canonical source**: `research_tracks/THEORY_COMPARISONS/penrose_twistor/STATUS.md`
> Hard rule: UBT is NOT twistor theory. Results below establish a compatible substructure
> over flat Minkowski space only.

| Result | Status | File | Notes |
|--------|--------|------|-------|
| σ_μ matrices derived from ℂ⊗ℍ biquaternion basis | **Proved [L0]** | `penrose_twistor/twistor_core/ubt_generators.py` | 15 tests pass; no external Pauli import needed |
| det(X) = Minkowski interval for X = x^μ σ_μ | **Proved [L0]** | `penrose_twistor/twistor_core/minkowski_spinor.py` | Symbolic verification |
| Bijection x ↔ X^{AA'} well-defined and invertible | **Proved [L0]** | `penrose_twistor/twistor_core/minkowski_spinor.py` | Roundtrip tests pass |
| Null vectors ↔ rank-1 Hermitian matrices | **Proved [L0]** | `penrose_twistor/tests/test_light_cone.py` | det X = 0 iff s² = 0 |
| Incidence relation ω^A = iX^{AA'}π_{A'} (flat Minkowski) | **Proved [L0]** | `penrose_twistor/twistor_core/twistor.py` | Flat space only; ψ not carried through |
| SU(2,2) Hermitian form and group action | **Proved [L0]** | `penrose_twistor/twistor_core/su22.py` | Signature (2,2) verified |
| Conformal (Möbius) action on X-space | **Computationally verified** | `penrose_twistor/twistor_core/conformal.py` | Numerical; analytic proof pending |
| UBT generator closure → 15D Lie algebra | **Computationally verified** | `penrose_twistor/twistor_core/lie_audit.py` | Killing form (8,7,0); semisimple |
| X^{AA'}(Θ) in curved UBT sector | **Open** | `penrose_twistor/curved_bridge_todo.md` | Requires nonlinear graviton extension |
| ψ (imaginary time) ↔ twistor geometry | **Open** | `penrose_twistor/tau_phase_mapping.md` | No candidate mapping found |

---

## Cross-Gap Consistency Checks

| Check | Status | Notes |
|-------|--------|-------|
| CC1: R_ψ = ℏ/(m_e·c) used consistently | To verify | Gap 1, Gap 4, Gap 6 must use same value |
| CC2: B coefficient layer discipline | OPEN | B needs [L1] derivation; currently uses N_eff from SM (Gap 5) |
| CC3: Prime chain V(ψ) → prime attractor → φ_p | **Partially verified** | ψ_p = φ_p = 2π/p share index structure; distinct geometric mechanisms (see §5a) |

---

## QM Emergence from Complex Time (Track: CORE)

*Added 2026-03-06. Source verification: `canonical/qm_emergence/`*

| Result | Status | File | Notes |
|--------|--------|------|-------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) algebra isomorphism | **Proven** [L0] | `canonical/qm_emergence/step3_dirac_emergence.tex §2` | Standard algebra; generators map to Pauli matrices |
| Pauli matrices σᵢ from quaternion generators | **Proven** [L0] | `canonical/qm_emergence/step3_dirac_emergence.tex §3` | Direct from isomorphism; not postulated |
| Dirac γ^μ from ℂ⊗ℍ ⊗ ℂ⊗ℍ tensor product | **Proven** [L0] | `canonical/qm_emergence/step3_dirac_emergence.tex §4` | γ^μ in Weyl rep. = σ₁⊗𝟙, iσ₂⊗σᵢ; Clifford relation verified |
| Dirac-like operator 𝒟 = iγ^μ∇_μ uniquely determined | **Proven** [L0] | `research_tracks/legacy_theory_variants/ubt/operators/dirac_like_operator.tex Thm. 2.1` | Unique up to gauge equivalence from bundle structure |
| Schrödinger structure from Im(∂_τΘ = □Θ) | **Sketch** [L0] | `canonical/qm_emergence/step2_schrodinger_emergence.tex §5` | ∂_ψΦ = −2i∇²Φ follows analytically; diffusion coeff. 𝒟=ℏ/(2m) is assumed (Gap S1) |
| UBT ψ is physical — NOT a Wick rotation | **Proven** [L0] | `canonical/THEORY/math/fields/biquaternion_time.tex §5.1` | ψ∈ℝ is dynamical; Wick rotation is formal analytic continuation only |
| Biquaternionic FPE with Θ = Σ exp[πB(n)·H(T)] | **Sketch** [L0] | `canonical/qm_emergence/step1_fpe_check.tex` | Scalar sector numerically verified (see tools/verify_fpe.py); three gaps remain: G1 (A(Q) assumed), G2 (consistency condition on H), G3 (non-commutativity) |
| Massless Dirac equation from 𝒟Θ = 0 (spinorial sector) | **Proved [L1]** | `canonical/qm_emergence/step3_dirac_emergence.tex §6`, `canonical/qm_emergence/step6_spinorial_subspace.tex` | Algebraic structure proved; Gap D1 (spinorial subspace) closed by step6: Θ₁ (n=1 ψ-mode) transforms as Dirac spinor via winding + SL(2,ℂ) double cover (Thm. D1); massless case has zero free parameters |
| Born rule: Θ†Θ is probability density | **Proved [L0]** | `canonical/qm_emergence/step7_born_rule.tex` | Sc[Θ†Θ] is conserved by FPE (∂_T∫P dQ=0); Born rule follows without postulate; see step7 |
| QM unification via drift-diffusion | **Sketch** [L0] | `ARCHIVE/archive_legacy/consolidation_project/appendix_FORMAL_qm_gr_unification.tex` | Madelung equations reproduced; specific parameter choices needed (see Step 2) |
| FPE ↔ Euler–Lagrange equivalence (scalar sector) | **Proven** [L0] | `canonical/qm_emergence/step4_fpe_equivalence.tex` | Algebraic identity under conditions C1 (∇²H=0) and C2 (∇H⊥∇Θ); script tools/verify_fpe_equivalence.py — ALL CHECKS PASSED |
| Three projections: GR, QM, statistical mechanics | **Proven** [L0] | `canonical/qm_emergence/step4_fpe_equivalence.tex §4` | Re(∂_tΘ=□Θ) → GR/KG; Im(∂_ψΘ=□Θ) → QM/Schrödinger; full FPE → stat.mech. Definitionally equivalent projections of one field equation, not emergent |

### Open Sub-Tasks (QM Emergence Gaps)

| Gap | Description | Priority |
|-----|-------------|----------|
| G1 | Derive drift A(Q) = −∇H from S[Θ] via Euler-Lagrange | HIGH |
| G2 | Prove consistency condition on H for general biquaternionic case | HIGH |
| G3 | Non-commutative FPE ordering: **PARTIALLY RESOLVED** — [∂_T, ∇_Q²]=0 proved; left FPE from S[Θ]; scalar-Hamiltonian case closed; vector potential case checked separately | MEDIUM |
| S1 | Derive diffusion coefficient 𝒟_eff = ℏ/(2m) from S[Θ] | HIGH |
| D1 | Spinorial subspace: **CLOSED** — Θ₁ (n=1 mode) transforms as Dirac spinor via winding + SL(2,C) spinor rep; see step6_spinorial_subspace.tex | HIGH |

---

## Fermionic Statistics

| Result | Status | File | Notes |
|--------|--------|------|-------|
| Grassmannian path-integral measure for odd-winding KK modes | **Proved [L1]** | `canonical/bridges/fermionic_statistics_bridge.tex` | Exchange-phase calculation yields −1 for odd-n modes; Berezin measure required |
| Spin from Noether angular-momentum operator (KK soliton) | **[Open L2]** | `canonical/bridges/fermionic_statistics_bridge.tex §Gap` | Grassmannian measure proved [L1]; spin eigenvalue computation pending |

---

## QED Reproducibility at φ = const (Track: CORE)

*Added 2026-03-06. Task: UBT\_v29\_task7\_qed\_phi\_const.*
*Source: `canonical/qed_phi_const/` Script: `tools/verify_qed_phi_const.py`.*

This section tracks the stronger QED constraint: UBT must reproduce standard QED not
only at φ=0 (vacuum limit, previously verified) but for any constant scalar background
φ = const ≠ 0 (cosmological background, Higgs-vev analog).

| Result | Status | File | Notes |
|--------|--------|------|-------|
| U(1)\_EM unbroken at φ=const | **Proven** [L0] | `canonical/qed_phi_const/step1_u1_protection.tex` | q\_φ=0 (neutral scalar); m²\_γ=0 exact; no Higgs mechanism for EM |
| Electron mass m\_e=y·v at φ=const | **Sketch** [L1] | `canonical/qed_phi_const/step2_electron_mass.tex` | Structural: identical to SM Higgs; Gaps Y1 (derive y) and Y2 (derive v) open |
| δB(φ)=0 at one loop — α(μ) running unchanged | **Proven** [L1] | `canonical/qed_phi_const/step3_beta_function.tex` | Outcome A: UV divergence mass-independent; φ-loop absent (q\_φ=0); standard QED running exact |
| Schwinger term a\_e=α/(2π) at φ=const | **Proven** [L1] | `canonical/qed_phi_const/step4_schwinger_term.tex` | Massless photon (Step 1) + Dirac vertex (Step 2) → identical 1-loop diagram; φ-correction ~10⁻¹⁶ (unobservable) |
| Lamb shift 1057.8 MHz at φ=const | **Sketch** [L1] | `canonical/qed_phi_const/step5_lamb_shift.tex` | Structural: reduction to Steps 1–4 complete; explicit UBT path-integral computation lacking (Gap L1) |
| QED reproducibility summary | **Substantially Proved** [L1] | `canonical/qed_phi_const/step6_qed_summary.tex` | 3 proved + 2 sketch; minimum criterion (U(1)\_EM unbroken) met; script passes all checks |

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

*Added 2026-03-06. Task: UBT_v29_task2_chirality. Source: `canonical/chirality/`*

| Result | Status | File | Notes |
|--------|--------|------|-------|
| ℍ gives SU(2)_L × SU(2)_R from left/right actions | **Proven** [L0] | `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex §5` | Inn(ℍ)_L × Inn(ℍ)_R ≅ Spin(4); selection mechanism needed |
| P_ψ maps modes n → -n (ψ-parity) | **Proven** [L0] | `canonical/chirality/step1_psi_parity.tex §2` | Def. 1; exact algebraic statement |
| ∂_ψ anti-commutes with P_ψ | **Proven** [L0] | `canonical/chirality/step1_psi_parity.tex §3` | Lem. 2; direct calculation |
| P_ψ acts as γ⁵ in ψ-sector | **Proven** [L0] | `canonical/chirality/step1_psi_parity.tex §4` | Prop. 3; [P_ψ, γ^μ∇_μ]=0 and {P_ψ, γ⁵∂_ψ}=0 |
| Preferred ψ-circle orientation (matter n>0 by CPT) | **Proven** [L0] | `canonical/chirality/step1_psi_parity.tex §5` | Lem. 4; P_ψ = CP in ψ-sector |
| SU(2)_L on odd modes ℋ₋ | **Proved [L1]** | `canonical/chirality/step1_psi_parity.tex §6`, `canonical/chirality/step3_gap_C1_resolution.tex` | Thm. 5; Gap C1 closed (no W_R in S[Θ]) — proved from S[Θ] action |

### Open Sub-Tasks (Chirality Gaps)

| Gap | Description | Priority |
|-----|-------------|----------|
| C1 | W± vertex P_ψ-odd from S[Θ]: **CLOSED** — no W_R in S[Θ]; see step3_gap_C1_resolution.tex | HIGH |

---

## 8π Common Origin (Track: CORE)

*Added 2026-03-06. Task: UBT_v29_task3_8pi. Source: `canonical/8pi_common_origin.tex`. Script: `tools/verify_8pi_connection.py`.*

| Result | Status | File | Notes |
|--------|--------|------|-------|
| 8π in G_μν = 8πG T_μν from dim(ℍ) | **Structural** [L0] | `canonical/8pi_common_origin.tex §2` | 16πG = dim_ℝ(ℍ) × vol(S²) × G = 4 × 4π × G; structural not coincidental |
| B₀ = 8π from dim_ℂ(ℂ⊗ℍ) = 4 | **Proven** [L1] | `canonical/8pi_common_origin.tex §3`, `canonical/n_eff/step2_vacuum_polarization.tex` | B₀ = 2π × dim_ℂ(ℂ⊗ℍ) = 8π; script verify_8pi_connection.py ALL PASS |
| Common algebraic ancestor: dim 4 | **Structural** [L0] | `canonical/8pi_common_origin.tex §4` | dim_ℝ(ℍ) = dim_ℂ(Mat(2,ℂ)) = 4; both 8π's share this factor |
| N_phases = 3 and spin-trace = 1/3: algebraically independent | **Proven** [L0] | `canonical/8pi_common_origin.tex §3 Thm. 3` | Numerical equality in d=4 is coincidental; cancellation gives dim_ℂ(ℂ⊗ℍ) = 4 |
| Unified theorem: single origin for both 8π's | **Motivated Conjecture [Open L2]** | `canonical/8pi_common_origin.tex §5` | Common algebraic ancestor dim_ℝ(ℍ) = 4 identified; MOTIVATED CONJECTURE: both 8π's trace to quaternionic dimension 4; rigorous unification would require deriving 1/(16πG) from S[Θ] directly — deep [L2] open problem |

---

## FPE Equivalence — QM/GR/Stat-Mech Unification (Track: CORE)

*Added 2026-03-06. Task: UBT_v29_task1_fpe_equivalence. Source: `canonical/qm_emergence/step4_fpe_equivalence.tex`. Script: `tools/verify_fpe_equivalence.py`.*

| Result | Status | File | Notes |
|--------|--------|------|-------|
| FPE ↔ E-L equivalence (scalar, free field) | **Proven** [L0] | `canonical/qm_emergence/step4_fpe_equivalence.tex Thm. 1` | Algebraic identity: both reduce to ∂_TΘ = D∇²Θ under C1,C2 |
| Norm conservation from FPE | **Proven** [L0] | `canonical/qm_emergence/step4_fpe_equivalence.tex Prop. 2` | d/dT ∫\|Θ\|² dQ = 0; Born rule consistent without extra postulate |
| Projection A: Re sector → GR/KG | **Proven** [L0] | `canonical/qm_emergence/step4_fpe_equivalence.tex §4` | Re(∂_tΘ=□Θ) = GR sector; confirmed numerically |
| Projection B: Im sector → QM/Schrödinger | **Sketch** | `canonical/qm_emergence/step4_fpe_equivalence.tex §4` | Im(∂_ψΘ=□Θ) → QM; Gap S1 (D=ℏ/2m) PARTIALLY CLOSED via dimensional analysis (step2_schrodinger_emergence.tex §2.5) |
| Projection C: Full FPE → statistical mechanics | **Proven** [L0] | `canonical/qm_emergence/step4_fpe_equivalence.tex §4` | FPE IS stat.mech. by construction |
| FPE ↔ E-L (full biquaternionic) | **Partially Proved** | `canonical/qm_emergence/step4_fpe_equivalence.tex §6`, `ARCHIVE/archive_legacy/consolidation_project/FPE_verification/step5_noncommutativity.tex` | [∂_T,∇_Q²]=0; left FPE from S[Θ]; scalar-H case closed; Gap G3 reduced; Gap G1 CLOSED for scalar sector (step1_fpe_check.tex §1.3.1) |

**Strongest unification result**: QM, GR, and statistical mechanics are definitionally equivalent projections of ∂_TΘ = D∇²Θ — not emergent from a deeper layer.

---

## GR Recovery Status (v48+, updated 2026-03-11)

> ⭐ **Canonical source**: `canonical/bridges/GR_chain_bridge.tex` + `canonical/gr_closure/` chain  
> Topic index: `canonical/THEORY/topic_indexes/GR_index.md`

*Updated 2026-03-11 to align language with the UBT-vs-GR clarification.
**There is no contradiction between UBT and GR.** UBT reproduces GR on the admissible
sector A_UBT (Level 2 = constrained_sector_recovery) while admitting additional non-GR
degrees of freedom.  The combined variational condition E_Θ + J*E_g = 0 is fundamental;
termwise separation is not automatic.  See `docs/reports/gr_recovery_levels.md` for the
three-level taxonomy and `canonical/gr_closure/theta_vs_metric_variation_note.tex`
for the variational analysis.*

```
GR RECOVERY STATUS (v48+):
"UBT admits an exact variational GR sector (metric+Θ formulation)
and an emergent-metric construction strongly connected to Θ.
```

### Proved

| Result | Status | File | Notes |
|--------|--------|------|-------|
| G_μν = 8πG T_μν from δS_total[g,Θ]/δg^μν = 0 | **Proven** [L1] | `canonical/t_munu/step3_einstein_with_matter.tex` | Hilbert variation; standard variational GR sector |
| T_μν from Hilbert prescription | **Proven** [L1] | `canonical/t_munu/step3_einstein_with_matter.tex` | δS_matter/δg^μν = -(√-g/2)T_μν |
| ∇^μ T_μν = 0 from Bianchi identity | **Proven** [L1] | `canonical/t_munu/step3_einstein_with_matter.tex` | Contracted Bianchi; no free parameters |
| Lorentzian signature (-,+,+,+) from AXIOM B | **Proven** [L0] | `canonical/gr_closure/step3_signature_theorem.tex §Lorentzian Signature from AXIOM B` | Complex time τ=t+iψ → Cl_{1,3}(ℝ) → e₀²=-1 → g₀₀<0; signature is theorem not choice |
| Metric non-degeneracy for A_UBT class | **Proven** [L0] | `canonical/gr_closure/step2_nondegeneracy.tex` | Linear independence of ∂_μΘ ↔ det(g)≠0; degenerate configs explicitly identified |
| Derivative-based ≡ tetrad-based metric formula | **Proven** [L0] | `canonical/gr_closure/step1_metric_bridge.tex` | Under E_μ = ∂_μΘ; single canonical metric definition |
| GR chain summary (Θ→g→Γ→R→Einstein) | **Proved [L1]** | `canonical/gr_closure/GR_chain_summary.tex` | Steps 1-5 proved; Step 6 off-shell open [L2]; see summary doc |
| N is scale-fixing, not signature-fixing | **Proved [L0]** | `canonical/gr_closure/step3_signature_theorem.tex` | Explicitly documented in step1_metric_bridge.tex remark |
| UBT vs sigma model distinction | **Documented** | `canonical/gr_closure/step1_metric_bridge.tex` | Three key differences stated |

### Conditional (under assumptions A1–A3)

| Result | Status | File | Notes |
|--------|--------|------|-------|
| GR equivalence via tetrad pipeline | **Conditional** | `ARCHIVE/archive_legacy/consolidation_project/appendix_R_GR_equivalence.tex` | Requires Hermitian tetrad (A1), torsion-free (A2), invertible tetrad (A3) |
| Θ-only closure (on-shell) | **GR-compatible sector recovered (Level 2)** | `canonical/gr_closure/step2_theta_only_closure.tex` | Equivalent to Einstein eq. at Θ satisfying E-L; rank condition (non-degeneracy of δg/δΘ on admissible sector) proved for A_UBT class (§1.5); off-shell requires global rank argument [L2 OPEN; GAP-01, GAP-10] |

### Not Yet Proved

| Result | Status | Notes |
|--------|--------|-------|
| Pure Θ-only closure (g[Θ] substitution before variation, off-shell) | **Open** | Requires global rank argument for J=δg/δΘ; not merely injectivity (see GAP-10). Correct claim: Level-2 sector recovery. See `research_tracks/research/gr_offshell_gap.md` for precise gap statement. Missing lemma: global rank of J=δg^μν/δΘ off the metric-generating sector. On-shell recovery (GR-compatible sector Level 2) is proved. |
| Metric uniqueness beyond A_UBT | **Open** | No proof that g[Θ] is unique outside admissible class |

---

## Mirror Sector (Twin Prime Vacuum)

> ⭐ **Canonical sources**: `research_tracks/mirror_sector/README.md` + `docs/reports/hecke_lepton/mirror_world_139.md`  
> Topic index: `canonical/THEORY/topic_indexes/mirror_sector_index.md`

| Result | Status | File | Notes |
|--------|--------|------|-------|
| V_eff(137) < V_eff(139) for same B | **NUMERICAL OBSERVATION** | `research_tracks/mirror_sector/vacuum_stability.tex` | Calibrated to our sector |
| n=139 is NOT a discrete local min of V_{B_137} | **PROVED NUMERICALLY** | `research_tracks/mirror_sector/vacuum_stability.tex` | V(138) < V(139); ascending branch |
| n*=139 is global min of branch B'=B_139 | **MOTIVATED CONJECTURE** | `research_tracks/mirror_sector/vacuum_stability.tex` | ΔB/B=1.21%; two independent sectors |
| Mirror sector is fully stable | **FOLLOWS FROM CONJECTURE** | `research_tracks/mirror_sector/vacuum_stability.tex` | No false vacuum; no Coleman tunnelling |
| Set A and Set B algebraically independent | **NUMERICAL OBSERVATION** | `docs/reports/hecke_lepton/` | Different levels/weights/eigenvalues |
| Mirror sector α⁻¹ = 139 | **NUMERICAL OBSERVATION** | `docs/reports/hecke_lepton/mirror_world_139.md` | Set B globally unique at p=139 |
| Mirror sector is habitable | **DERIVED** | — | α⁻¹=139 within anthropic bounds (95-195) |
| Mirror matter as dark matter candidate | **CONJECTURE** | `research_tracks/mirror_sector/README.md` | Gravitational coupling only; Foot-Volkas precedent |

---

## Hecke Bridge (ℂ⊗ℍ ↔ Modular Forms)

> ⭐ **Canonical sources**: `docs/reports/hecke_lepton/` + `research_tracks/hecke_bridge/motivation.tex`  
> Topic index: `canonical/THEORY/topic_indexes/hecke_index.md`

| Result | Status | File | Notes |
|--------|--------|------|-------|
| Weights k=2,4,6 from n-th ψ-mode | **MOTIVATED CONJECTURE** | `research_tracks/hecke_bridge/motivation.tex §2` | k=2n for n-th generation; kinetic/quartic/sextic terms in S[Θ] |
| Level N=7, μ(Γ₀(7))=8 = dim_ℝ(ℂ⊗ℍ) | **MOTIVATED CONJECTURE** | `research_tracks/hecke_bridge/motivation.tex §3` | Index coincidence suggestive; not proved |
| Trivial character χ=1 from ℤ-rationality | **MOTIVATED CONJECTURE** | `research_tracks/hecke_bridge/motivation.tex §4` | ℂ⊗ℍ over ℤ → ℚ-rational forms |
| Three forms (not one, not five) | **MOTIVATED CONJECTURE** | `research_tracks/hecke_bridge/motivation.tex §5` | Three ψ-modes; algebraic derivation OPEN |
| Derivation of specific forms from ℂ⊗ℍ | **OPEN** | — | Requires identifying L-function of ℂ⊗ℍ/ℤ |

---

## Holography and de Sitter Structure

| Result | Status | File | Notes |
|--------|--------|------|-------|
| Physical M⁴ is de Sitter (Λ>0) | **Proved [L1]** | `canonical/gr_limit/GR_limit_of_UBT.tex` | Follows from GR recovery + observational Λ>0 |
| ψ-circle S¹(R_ψ) is flat (zero curvature) | **Proved [L0]** | `research_tracks/research/moduli_space_ads_vs_physical_ds.tex §3` | Standard diff.geom.; no AdS factor |
| Moduli space ℍ has hyperbolic geometry K=−1 | **Proved [L0]** | `research_tracks/research/moduli_space_ads_vs_physical_ds.tex §4` | Parameter space, not physical spacetime |
| AdS/CFT-like informational encoding analogy | **[O] Open Research** | `research_tracks/THEORY_COMPARISONS/ads_cft_like_encoding_in_ubt.md` | Structural analogy only; not a duality |
| Λ_eff from V_eff(Θ) direct identification | **Dead End [L2]** | `ARCHIVE/archive_legacy/consolidation_project/new_alpha_derivations/ubt_alpha_minimizer.py` | v47 numerical check: V_eff(n*=137) = A·137²−B·137·ln(137) ≈ −12428 (dimensionless winding-sector potential). Direct identification V_eff(n*) = Λ_eff gives wrong units and magnitude (≠ 10⁻¹²² in Planck units by many orders of magnitude). Dead End for direct identification. |
| Λ_eff via UV cut-off bridge from V_eff | **Open [L2]** | `ARCHIVE/archive_legacy/consolidation_project/new_alpha_derivations/ubt_alpha_minimizer.py` | A unit-conversion bridge from the winding potential to vacuum energy density via an independent UV cut-off argument is not yet present in the framework; route is open. |
| Verlinde / dS holographic principle | **[S] Speculative** | `ARCHIVE/archive_legacy/consolidation_project/appendix_N_holographic_verlinde_desitter.tex` | General connections; no quantitative derivation |


