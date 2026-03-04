<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT Global Derivation Index

> **Purpose**: Scan of the repository listing every major derivation with location, mathematical status, and reproducibility.

---

## How to Read This Index

| Column | Meaning |
|---|---|
| **Claim** | Physics or mathematical statement |
| **Location** | File path(s) in the repository |
| **Math Status** | `Proven` / `Semi-empirical` / `Hypothesis` / `Sketch` |
| **Numeric Repro** | `Yes` / `Partial` / `No` — whether a script exists |
| **Free Parameters** | Number of fitted/assumed parameters |

---

## Domain: General Relativity Recovery

| Claim | Location | Math Status | Numeric Repro | Free Params |
|---|---|---|---|---|
| GR metric emerges as real projection of biquaternionic metric | [`core/AXIOMS.md`](../core/AXIOMS.md) (Axiom C), [`consolidation_project/appendix_R_GR_equivalence.tex`](../consolidation_project/appendix_R_GR_equivalence.tex) | Proven (analytic) | No | 0 |
| Einstein–Hilbert action from spectral invariants of Θ | [`FORMAL_INVARIANT_EXTRACTION_LAYER0.tex`](../FORMAL_INVARIANT_EXTRACTION_LAYER0.tex), [`Appendix_F_Hermitian_Limit.tex`](../Appendix_F_Hermitian_Limit.tex) | Proven (analytic) | No | 0 |
| GR field equations `G_{μν} = κ T_{μν}` from UBT in ψ→0 limit | [`consolidation_project/appendix_F_Hermitian_Limit.tex`](../consolidation_project/appendix_F_Hermitian_Limit.tex) | Proven (analytic) | No | 0 |
| FRW cosmology embedded in UBT | [`consolidation_project/appendix_M_dark_energy_UBT.tex`](../consolidation_project/appendix_M_dark_energy_UBT.tex) | Semi-empirical | No | 1 (Λ) |
| Black hole radiation (Hawking-like) from UBT | [`consolidation_project/appendix_FORMAL_black_hole_radiation.tex`](../consolidation_project/appendix_FORMAL_black_hole_radiation.tex) | Sketch | No | 0 |

---

## Domain: SU(3) Colour Emergence

| Claim | Location | Math Status | Numeric Repro | Free Params |
|---|---|---|---|---|
| SU(3) colour from Aut(𝕆) ⊃ G₂ ⊃ SU(3) | [`Appendix_G_Emergent_SU3.tex`](../Appendix_G_Emergent_SU3.tex), [`consolidation_project/appendix_G_internal_color_symmetry.tex`](../consolidation_project/appendix_G_internal_color_symmetry.tex) | Semi-empirical | No | 0 |
| Gluon field as biquaternionic gauge connection | [`consolidation_project/appendix_E_SM_QCD_embedding.tex`](../consolidation_project/appendix_E_SM_QCD_embedding.tex) | Semi-empirical | No | 0 |
| Yang–Mills kinetic term from UBT curvature | [`consolidation_project/appendix_E_SM_QCD_embedding.tex`](../consolidation_project/appendix_E_SM_QCD_embedding.tex) | Semi-empirical | No | 0 |
| SU(3) associative realisation from involutions | [`research_tracks/associative_su3/from_involutions.md`](../research_tracks/associative_su3/from_involutions.md) | Sketch | No | 0 |
| Three fermion generations from complex-time | [`research_tracks/three_generations/st3_complex_time_generations.tex`](../research_tracks/three_generations/st3_complex_time_generations.tex) | Sketch | No | 0 |

---

## Domain: Standard Model Limit

| Claim | Location | Math Status | Numeric Repro | Free Params |
|---|---|---|---|---|
| SU(3)×SU(2)×U(1) from Aut(ℂ⊗ℍ) | [`QED_SM_FROM_UBT_ANALYSIS.md`](../QED_SM_FROM_UBT_ANALYSIS.md), [`SM_GEOMETRIC_EMERGENCE_DRAFT.md`](../SM_GEOMETRIC_EMERGENCE_DRAFT.md) | Semi-empirical | No | 0 |
| SU(2)_L weak sector from quaternionic left-action | [`consolidation_project/appendix_E2_SM_geometry.tex`](../consolidation_project/appendix_E2_SM_geometry.tex) | Semi-empirical | No | 0 |
| U(1) EM from complex phase | [`consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex`](../consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex) | Proven | No | 0 |
| QED recovered as ∂_ψ=0 limit | [`consolidation_project/appendix_D_qed_consolidated.tex`](../consolidation_project/appendix_D_qed_consolidated.tex) | Proven | No | 0 |
| Electroweak mixing angle from biquaternionic geometry | [`consolidation_project/appendix_K2_fundamental_constants_consolidated.tex`](../consolidation_project/appendix_K2_fundamental_constants_consolidated.tex) | Sketch | No | 1 |

---

## Domain: Fine Structure Constant α

| Claim | Location | Math Status | Numeric Repro | Free Params |
|---|---|---|---|---|
| Bare α⁻¹ = 137 from ψ-cycle compactification | [`unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex`](../unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation_precise.tex), [`STATUS_ALPHA.md`](../STATUS_ALPHA.md) | Semi-empirical | Yes | 1 (B coeff.) |
| Prime stability selects n=137 among all primes | [`STATUS_ALPHA.md`](../STATUS_ALPHA.md) §3, [`ubt/quantization/winding_quantization.tex`](../ubt/quantization/winding_quantization.tex) | Semi-empirical | Yes | 1 (B coeff.) |
| B coefficient from SM gauge-boson content (N_eff=12) | [`STATUS_ALPHA.md`](../STATUS_ALPHA.md) §5 | Semi-empirical | Partial | 1 (R factor) |
| Quantum correction +0.036 from two-loop QED | [`consolidation_project/appendix_CT_two_loop_baseline.tex`](../consolidation_project/appendix_CT_two_loop_baseline.tex), [`alpha_core_repro/alpha_two_loop.py`](../alpha_core_repro/alpha_two_loop.py) | Proven (by QED) | Yes | 0 |
| p-adic route to α⁻¹ | [`consolidation_project/appendix_ALPHA_padic_derivation.tex`](../consolidation_project/appendix_ALPHA_padic_derivation.tex), [`consolidation_project/appendix_H_alpha_padic_combined.tex`](../consolidation_project/appendix_H_alpha_padic_combined.tex) | Semi-empirical | Partial | 0 |
| Hecke-Worlds: α⁻¹ = p + Δ_CT,p (p=137) | [`UBT_HeckeWorlds_theta_zeta_primes_appendix.tex`](../UBT_HeckeWorlds_theta_zeta_primes_appendix.tex) | Hypothesis | Yes | 0 |

---

## Domain: Electron Mass

| Claim | Location | Math Status | Numeric Repro | Free Params |
|---|---|---|---|---|
| Fermion mass formula `m(n) = A·nᵖ − B_m·n·ln(n)` | [`appendix_E_m0_derivation_strict.tex`](../appendix_E_m0_derivation_strict.tex), [`consolidation_project/appendix_E2_fermion_masses.tex`](../consolidation_project/appendix_E2_fermion_masses.tex) | Semi-empirical | Yes | 2 (A, B_m) |
| m_e ≈ 0.5099 MeV (0.22% from experiment) | [`STATUS_FERMIONS.md`](../STATUS_FERMIONS.md) | Semi-empirical | Yes | 2 |
| Quark masses from same spectral formula | [`ubt_with_chronofactor/papers/ubt_quark_mass_estimation.tex`](../ubt_with_chronofactor/papers/) | Semi-empirical | Yes | 2 |
| Neutrino masses from biquaternionic complex-time | [`consolidation_project/appendix_E3_neutrino_masses.tex`](../consolidation_project/appendix_E3_neutrino_masses.tex), [`consolidation_project/appendix_G6_neutrino_mass_biquaternionic_time.tex`](../consolidation_project/appendix_G6_neutrino_mass_biquaternionic_time.tex) | Hypothesis | No | 2 |

---

## Domain: Hubble Tension

| Claim | Location | Math Status | Numeric Repro | Free Params |
|---|---|---|---|---|
| Hubble tension as effective metric latency δ ≈ 8% | [`speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex`](../speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex), [`research_front/hubble_latency/appendix_hubble_latency.md`](../research_front/hubble_latency/appendix_hubble_latency.md) | Hypothesis | Yes | 0 |
| Information-theoretic overhead O/F ≈ 20/256 ≈ 8% | [`research_front/hubble_latency/appendix_hubble_latency.md`](../research_front/hubble_latency/appendix_hubble_latency.md) | Hypothesis | Yes | 2 (F, N) |
| δ constant in cosmic time (not dynamical dark energy) | [`speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex`](../speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex) | Hypothesis | No | 0 |

---

## Domain: Cosmology / CMB

| Claim | Location | Math Status | Numeric Repro | Free Params |
|---|---|---|---|---|
| CMB acoustic peaks with UBT phase corrections | [`consolidation_project/appendix_CERN_BSM_predictions.tex`](../consolidation_project/appendix_CERN_BSM_predictions.tex) | Hypothesis | No | 1 |
| Dark energy from imaginary curvature of Θ | [`consolidation_project/appendix_M_dark_energy_UBT.tex`](../consolidation_project/appendix_M_dark_energy_UBT.tex) | Hypothesis | No | 1 |
| Dark matter from p-adic biquaternionic modes | [`consolidation_project/appendix_U_dark_matter_unified_padic.tex`](../consolidation_project/appendix_U_dark_matter_unified_padic.tex) | Sketch | No | 0 |
| Baryon fraction Ω_b from biquaternionic gauge count | [`STATUS_OBSERVATIONAL.md`](../STATUS_OBSERVATIONAL.md) | Hypothesis | No | 1 |

---

## Summary Statistics

| Domain | Total Claims | Proven | Semi-empirical | Hypothesis/Sketch | Numeric Scripts |
|---|---|---|---|---|---|
| GR recovery | 5 | 3 | 1 | 1 | 0 |
| SU(3) emergence | 5 | 0 | 2 | 3 | 0 |
| Standard Model | 5 | 2 | 2 | 1 | 0 |
| Fine structure α | 6 | 1 | 3 | 2 | 4 |
| Electron mass | 4 | 0 | 2 | 2 | 2 |
| Hubble tension | 3 | 0 | 0 | 3 | 2 |
| Cosmology / CMB | 4 | 0 | 0 | 4 | 0 |

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
