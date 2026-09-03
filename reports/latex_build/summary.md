<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# LaTeX build audit

> This directory is generated from scratch by `tools/latex_audit.py`. Do not append manual results; the next run deletes the directory first.

- Started (UTC): `2026-09-03T17:03:37+00:00`
- Commit: `8448bc793c5a7ff464491e634096c3a66ad4bf67`
- Ref: `master`
- Scope: `active standalone roots`
- Roots attempted: **357**
- PDFs produced: **252**
- Failed: **105**
- Timed out: **0**

A failed document does not stop later builds. Successful PDFs are uploaded as a workflow artifact; only curated publication PDFs are committed to `docs/pdfs/`.

## Failed roots

| Status | Root | Engine | Seconds | Failure log |
|---|---|---:|---:|---|
| failed | `ALPHA_BEST_ROUTE.tex` | `pdflatex` | 3.9 | `reports/latex_build/logs/ALPHA_BEST_ROUTE.tex__589d4d0ee6.txt` |
| failed | `canonical/alpha/alpha_equation_matrix.tex` | `pdflatex` | 4.0 | `reports/latex_build/logs/canonical__alpha__alpha_equation_matrix.tex__d87dd6c173.txt` |
| failed | `canonical/alpha/best_candidate_derivation.tex` | `pdflatex` | 3.7 | `reports/latex_build/logs/canonical__alpha__best_candidate_derivation.tex__960f2b529e.txt` |
| failed | `canonical/alpha/nlogn_origin_analysis.tex` | `pdflatex` | 3.7 | `reports/latex_build/logs/canonical__alpha__nlogn_origin_analysis.tex__95cd85ef37.txt` |
| failed | `canonical/alpha/prime_stability_set.tex` | `pdflatex` | 4.1 | `reports/latex_build/logs/canonical__alpha__prime_stability_set.tex__f93542811d.txt` |
| failed | `canonical/alpha/symmetry_breaking_alpha_attempt.tex` | `pdflatex` | 3.6 | `reports/latex_build/logs/canonical__alpha__symmetry_breaking_alpha_attempt.tex__c0853dc650.txt` |
| failed | `canonical/alpha/veff_corrected.tex` | `pdflatex` | 4.1 | `reports/latex_build/logs/canonical__alpha__veff_corrected.tex__984f012719.txt` |
| failed | `canonical/appendices/appendix_ACTION_review.tex` | `pdflatex` | 3.3 | `reports/latex_build/logs/canonical__appendices__appendix_ACTION_review.tex__ebb0de13e5.txt` |
| failed | `canonical/appendices/appendix_alpha_geometry.tex` | `pdflatex` | 3.6 | `reports/latex_build/logs/canonical__appendices__appendix_alpha_geometry.tex__189a47cb2e.txt` |
| failed | `canonical/appendices/appendix_fermions_completion.tex` | `pdflatex` | 3.4 | `reports/latex_build/logs/canonical__appendices__appendix_fermions_completion.tex__e8a6ec7116.txt` |
| failed | `canonical/bridges/su3_gauge_qubit_equivalence.tex` | `pdflatex` | 3.3 | `reports/latex_build/logs/canonical__bridges__su3_gauge_qubit_equivalence.tex__1e14a0d8a2.txt` |
| failed | `canonical/chirality/step2_chirality_result.tex` | `pdflatex` | 2.8 | `reports/latex_build/logs/canonical__chirality__step2_chirality_result.tex__4a0e39e37d.txt` |
| failed | `canonical/chirality/step4_no_wr_derivation.tex` | `pdflatex` | 2.8 | `reports/latex_build/logs/canonical__chirality__step4_no_wr_derivation.tex__57a2667714.txt` |
| failed | `canonical/complex_phase_extension.tex` | `pdflatex` | 3.7 | `reports/latex_build/logs/canonical__complex_phase_extension.tex__5f1b6ee724.txt` |
| failed | `canonical/geometry/Rpsi_dynamical_fix.tex` | `pdflatex` | 3.4 | `reports/latex_build/logs/canonical__geometry__Rpsi_dynamical_fix.tex__bbaddff4eb.txt` |
| failed | `canonical/gr_closure/frw_cosmological_solutions.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/canonical__gr_closure__frw_cosmological_solutions.tex__a2130dbf85.txt` |
| failed | `canonical/gr_closure/linearised_gravity.tex` | `pdflatex` | 2.5 | `reports/latex_build/logs/canonical__gr_closure__linearised_gravity.tex__b165fac769.txt` |
| failed | `canonical/gr_closure/zerilli_derivation.tex` | `pdflatex` | 5.0 | `reports/latex_build/logs/canonical__gr_closure__zerilli_derivation.tex__b1615d1fc5.txt` |
| failed | `canonical/interactions/B_base_derivation_complete.tex` | `pdflatex` | 3.6 | `reports/latex_build/logs/canonical__interactions__B_base_derivation_complete.tex__5a86e9c281.txt` |
| failed | `canonical/interactions/colour_charge_lattice.tex` | `pdflatex` | 4.2 | `reports/latex_build/logs/canonical__interactions__colour_charge_lattice.tex__b5e28d8b5e.txt` |
| failed | `canonical/interactions/hypercharge_assignments.tex` | `pdflatex` | 5.0 | `reports/latex_build/logs/canonical__interactions__hypercharge_assignments.tex__5d27954b87.txt` |
| failed | `canonical/n_eff/neff_reconciliation.tex` | `pdflatex` | 4.2 | `reports/latex_build/logs/canonical__n_eff__neff_reconciliation.tex__c370756446.txt` |
| failed | `canonical/n_eff/nhelicity_derivation.tex` | `pdflatex` | 4.2 | `reports/latex_build/logs/canonical__n_eff__nhelicity_derivation.tex__7be98f5b41.txt` |
| failed | `canonical/n_eff/step1_mode_decomposition.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/canonical__n_eff__step1_mode_decomposition.tex__be7bf7f62d.txt` |
| failed | `canonical/n_eff/step2_vacuum_polarization.tex` | `pdflatex` | 2.8 | `reports/latex_build/logs/canonical__n_eff__step2_vacuum_polarization.tex__f6eda8948e.txt` |
| failed | `canonical/qed_phi_const/step3_beta_function.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/canonical__qed_phi_const__step3_beta_function.tex__d9d2dd1366.txt` |
| failed | `canonical/qed_phi_const/step4_schwinger_term.tex` | `pdflatex` | 2.6 | `reports/latex_build/logs/canonical__qed_phi_const__step4_schwinger_term.tex__2618c9000a.txt` |
| failed | `canonical/qm_emergence/step2_schrodinger_emergence.tex` | `pdflatex` | 2.3 | `reports/latex_build/logs/canonical__qm_emergence__step2_schrodinger_emergence.tex__8e97bea82f.txt` |
| failed | `canonical/qm_emergence/step4_fpe_equivalence.tex` | `pdflatex` | 3.1 | `reports/latex_build/logs/canonical__qm_emergence__step4_fpe_equivalence.tex__36c306095b.txt` |
| failed | `canonical/symmetry/chirality_and_parity_breaking.tex` | `pdflatex` | 3.1 | `reports/latex_build/logs/canonical__symmetry__chirality_and_parity_breaking.tex__281a13f713.txt` |
| failed | `canonical/symmetry/cp_phase_sector.tex` | `pdflatex` | 3.1 | `reports/latex_build/logs/canonical__symmetry__cp_phase_sector.tex__2513011486.txt` |
| failed | `canonical/THEORY/canonical/canonical_projection_rules.tex` | `pdflatex` | 0.7 | `reports/latex_build/logs/canonical__THEORY__canonical__canonical_projection_rules.tex__fd5e8e13be.txt` |
| failed | `docs/papers/papers/generated/neff_biquaternion.tex` | `pdflatex` | 2.5 | `reports/latex_build/logs/docs__papers__papers__generated__neff_biquaternion.tex__638216d52a.txt` |
| failed | `docs/papers/papers/generated/ubt_action_and_alpha.tex` | `pdflatex` | 2.0 | `reports/latex_build/logs/docs__papers__papers__generated__ubt_action_and_alpha.tex__9e6e532aae.txt` |
| failed | `docs/papers/papers/generated/ubt_cosmo_hecke_neff.tex` | `pdflatex` | 1.9 | `reports/latex_build/logs/docs__papers__papers__generated__ubt_cosmo_hecke_neff.tex__e8acfffd8a.txt` |
| failed | `docs/papers/papers/su3_triplet/arxiv_version.tex` | `pdflatex` | 1.9 | `reports/latex_build/logs/docs__papers__papers__su3_triplet__arxiv_version.tex__e38d2172d4.txt` |
| failed | `docs/papers/papers/su3_triplet/main.tex` | `pdflatex` | 1.9 | `reports/latex_build/logs/docs__papers__papers__su3_triplet__main.tex__3d050075d4.txt` |
| failed | `docs/papers/papers/su3_triplet/noether_current_paper.tex` | `pdflatex` | 1.9 | `reports/latex_build/logs/docs__papers__papers__su3_triplet__noether_current_paper.tex__c70cff2cc4.txt` |
| failed | `docs/papers/papers/unified_biquaternion_theory_full.tex` | `pdflatex` | 4.0 | `reports/latex_build/logs/docs__papers__papers__unified_biquaternion_theory_full.tex__81d57ba259.txt` |
| failed | `docs/phase/ubt_planck_constant_derivation.tex` | `pdflatex` | 2.5 | `reports/latex_build/logs/docs__phase__ubt_planck_constant_derivation.tex__18c65eca65.txt` |
| failed | `docs/phase/ubt_planck_constant_next_steps.tex` | `pdflatex` | 2.6 | `reports/latex_build/logs/docs__phase__ubt_planck_constant_next_steps.tex__25e67da656.txt` |
| failed | `docs/publication/arxiv/main.tex` | `pdflatex` | 2.1 | `reports/latex_build/logs/docs__publication__arxiv__main.tex__71916730bd.txt` |
| failed | `docs/textbook/indices_torsion_anticommutator_rot_student_paper_cs.tex` | `pdflatex` | 0.7 | `reports/latex_build/logs/docs__textbook__indices_torsion_anticommutator_rot_student_paper_cs.tex__aedfa21ad1.txt` |
| failed | `docs/textbook/main.cs.tex` | `pdflatex` | 0.9 | `reports/latex_build/logs/docs__textbook__main.cs.tex__65d99b9ea5.txt` |
| failed | `docs/textbook/main.en.tex` | `pdflatex` | 1.0 | `reports/latex_build/logs/docs__textbook__main.en.tex__a1f68bc2ec.txt` |
| failed | `docs/UBT_VERIFICATION_REPORT.tex` | `pdflatex` | 2.4 | `reports/latex_build/logs/docs__UBT_VERIFICATION_REPORT.tex__a095ac677d.txt` |
| failed | `experiments/research_tracks/three_generations/st2_obstruction.tex` | `pdflatex` | 2.0 | `reports/latex_build/logs/experiments__research_tracks__three_generations__st2_obstruction.tex__2b502b6b7f.txt` |
| failed | `experiments/research_tracks/three_generations/st3_complex_time_generations.tex` | `pdflatex` | 1.9 | `reports/latex_build/logs/experiments__research_tracks__three_generations__st3_complex_time_generations.tex__2dac9870d0.txt` |
| failed | `experiments/research_tracks/three_generations/step1_fourier_vs_taylor.tex` | `pdflatex` | 1.9 | `reports/latex_build/logs/experiments__research_tracks__three_generations__step1_fourier_vs_taylor.tex__0dbb253395.txt` |
| failed | `experiments/research_tracks/three_generations/step2_modular_symmetry.tex` | `pdflatex` | 2.0 | `reports/latex_build/logs/experiments__research_tracks__three_generations__step2_modular_symmetry.tex__b257b9c4bd.txt` |
| failed | `experiments/research_tracks/three_generations/step3_mass_from_psi_energy.tex` | `pdflatex` | 1.9 | `reports/latex_build/logs/experiments__research_tracks__three_generations__step3_mass_from_psi_energy.tex__2f2dcdacd5.txt` |
| failed | `experiments/research_tracks/three_generations/step4_modular_forms.tex` | `pdflatex` | 2.5 | `reports/latex_build/logs/experiments__research_tracks__three_generations__step4_modular_forms.tex__d3ce80263a.txt` |
| failed | `experiments/research_tracks/three_generations/step5_hecke_search_results.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/experiments__research_tracks__three_generations__step5_hecke_search_results.tex__91771329a6.txt` |
| failed | `papers/old_releases/UBT_GR_RC2.tex` | `pdflatex` | 5.7 | `reports/latex_build/logs/papers__old_releases__UBT_GR_RC2.tex__e77ce2acd8.txt` |
| failed | `research_tracks/alpha_spectral/b_coefficient_gap_resolution.tex` | `pdflatex` | 5.3 | `reports/latex_build/logs/research_tracks__alpha_spectral__b_coefficient_gap_resolution.tex__5c40d893fd.txt` |
| failed | `research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex` | `pdflatex` | 5.4 | `reports/latex_build/logs/research_tracks__alpha_spectral__hecke_equivariant_path_integral.tex__a5b2ba4ac1.txt` |
| failed | `research_tracks/alpha_spectral/self_dual_torus_derivation.tex` | `pdflatex` | 3.4 | `reports/latex_build/logs/research_tracks__alpha_spectral__self_dual_torus_derivation.tex__a6cef2356a.txt` |
| failed | `research_tracks/canonical_relation_generalized_dirac/action_origin_obstruction.tex` | `pdflatex` | 4.2 | `reports/latex_build/logs/research_tracks__canonical_relation_generalized_dirac__action_origin_obstruction.tex__9780545432.txt` |
| failed | `research_tracks/coupling_spectrum/rg_prime_checkpoints.tex` | `pdflatex` | 3.6 | `reports/latex_build/logs/research_tracks__coupling_spectrum__rg_prime_checkpoints.tex__b92ca34bd2.txt` |
| failed | `research_tracks/EW/rpsi_from_action.tex` | `pdflatex` | 3.5 | `reports/latex_build/logs/research_tracks__EW__rpsi_from_action.tex__78fea6f21c.txt` |
| failed | `research_tracks/hecke_bridge/motivation.tex` | `pdflatex` | 5.3 | `reports/latex_build/logs/research_tracks__hecke_bridge__motivation.tex__43280cdcf2.txt` |
| failed | `research_tracks/prime_stability/rigorous_bounds.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/research_tracks__prime_stability__rigorous_bounds.tex__1ab5c9484b.txt` |
| failed | `research_tracks/qed_alpha_derivation/gauge_kinetic_normalization.tex` | `pdflatex` | 1.0 | `reports/latex_build/logs/research_tracks__qed_alpha_derivation__gauge_kinetic_normalization.tex__ac1f407fcf.txt` |
| failed | `research_tracks/quantum_ubt/fermionic_action_derivation.tex` | `pdflatex` | 3.6 | `reports/latex_build/logs/research_tracks__quantum_ubt__fermionic_action_derivation.tex__4bc94dfec4.txt` |
| failed | `research_tracks/quantum_ubt/fermionic_sector_derivation.tex` | `pdflatex` | 3.6 | `reports/latex_build/logs/research_tracks__quantum_ubt__fermionic_sector_derivation.tex__1dcd10ba40.txt` |
| failed | `research_tracks/quantum_ubt/frw_from_ubt.tex` | `pdflatex` | 5.2 | `reports/latex_build/logs/research_tracks__quantum_ubt__frw_from_ubt.tex__0a417648ba.txt` |
| failed | `research_tracks/quantum_ubt/ncg_spectral_triple.tex` | `pdflatex` | 2.5 | `reports/latex_build/logs/research_tracks__quantum_ubt__ncg_spectral_triple.tex__146a712ade.txt` |
| failed | `research_tracks/research/B_base_spectral_determinant.tex` | `pdflatex` | 2.6 | `reports/latex_build/logs/research_tracks__research__B_base_spectral_determinant.tex__b79e579fe7.txt` |
| failed | `research_tracks/research/graviton_schwarzschild.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/research_tracks__research__graviton_schwarzschild.tex__0f5d5303f0.txt` |
| failed | `research_tracks/research/hecke_generation_structure.tex` | `pdflatex` | 2.6 | `reports/latex_build/logs/research_tracks__research__hecke_generation_structure.tex__dd450108e4.txt` |
| failed | `research_tracks/research/hosotani_higgs.tex` | `pdflatex` | 2.8 | `reports/latex_build/logs/research_tracks__research__hosotani_higgs.tex__9e6ab5c1c0.txt` |
| failed | `research_tracks/research/mirror_sector_dynamics.tex` | `pdflatex` | 2.6 | `reports/latex_build/logs/research_tracks__research__mirror_sector_dynamics.tex__c6d70b3fe6.txt` |
| failed | `research_tracks/research/modular_dynamics.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/research_tracks__research__modular_dynamics.tex__ef47fd9f13.txt` |
| failed | `research_tracks/research/moduli_space_ads_vs_physical_ds.tex` | `pdflatex` | 2.5 | `reports/latex_build/logs/research_tracks__research__moduli_space_ads_vs_physical_ds.tex__1b3a33f971.txt` |
| failed | `research_tracks/research/r_factor_two_loop.tex` | `pdflatex` | 2.6 | `reports/latex_build/logs/research_tracks__research__r_factor_two_loop.tex__1546864abd.txt` |
| failed | `research_tracks/research/theta_dynamics_equations.tex` | `pdflatex` | 2.6 | `reports/latex_build/logs/research_tracks__research__theta_dynamics_equations.tex__ea265bb7a2.txt` |
| failed | `research_tracks/research/theta_fermion_emergence.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/research_tracks__research__theta_fermion_emergence.tex__5d21f51f63.txt` |
| failed | `research_tracks/research/theta_modular_geometry.tex` | `pdflatex` | 2.5 | `reports/latex_build/logs/research_tracks__research__theta_modular_geometry.tex__e656368a18.txt` |
| failed | `research_tracks/research/theta_quantum_field.tex` | `pdflatex` | 2.7 | `reports/latex_build/logs/research_tracks__research__theta_quantum_field.tex__b06e81579e.txt` |
| failed | `research_tracks/rg_B46/one_loop_rg_derivation.tex` | `pdflatex` | 2.8 | `reports/latex_build/logs/research_tracks__rg_B46__one_loop_rg_derivation.tex__bd1d8af477.txt` |
| failed | `research_tracks/T1_GR/GR_paper_v1.tex` | `pdflatex` | 6.6 | `reports/latex_build/logs/research_tracks__T1_GR__GR_paper_v1.tex__5042e7d545.txt` |
| failed | `research_tracks/T1_GR/ubt_gr_flagship.tex` | `pdflatex` | 4.9 | `reports/latex_build/logs/research_tracks__T1_GR__ubt_gr_flagship.tex__30191ff889.txt` |
| failed | `research_tracks/T1_GR/ubt_gr_paper.tex` | `pdflatex` | 6.7 | `reports/latex_build/logs/research_tracks__T1_GR__ubt_gr_paper.tex__185f71aa01.txt` |
| failed | `research_tracks/T2_GAUGE/gauge_paper_draft.tex` | `pdflatex` | 5.6 | `reports/latex_build/logs/research_tracks__T2_GAUGE__gauge_paper_draft.tex__c4329718e6.txt` |
| failed | `research_tracks/T3_ALPHA/a4_explicit_computation.tex` | `pdflatex` | 3.8 | `reports/latex_build/logs/research_tracks__T3_ALPHA__a4_explicit_computation.tex__7b14117839.txt` |
| failed | `research_tracks/T3_ALPHA/bootstrap_step_m1_conformal.tex` | `pdflatex` | 5.3 | `reports/latex_build/logs/research_tracks__T3_ALPHA__bootstrap_step_m1_conformal.tex__5ae58d3853.txt` |
| failed | `research_tracks/T3_ALPHA/bootstrap_step_m2_4point.tex` | `pdflatex` | 5.3 | `reports/latex_build/logs/research_tracks__T3_ALPHA__bootstrap_step_m2_4point.tex__7c7dde2094.txt` |
| failed | `research_tracks/T3_ALPHA/chowla_selberg_B_derivation.tex` | `pdflatex` | 4.0 | `reports/latex_build/logs/research_tracks__T3_ALPHA__chowla_selberg_B_derivation.tex__39e1ce0612.txt` |
| failed | `research_tracks/T3_ALPHA/conditional_alpha_note_draft.tex` | `pdflatex` | 6.8 | `reports/latex_build/logs/research_tracks__T3_ALPHA__conditional_alpha_note_draft.tex__0c38280260.txt` |
| failed | `research_tracks/T3_ALPHA/hecke_alpha_connection.tex` | `pdflatex` | 6.2 | `reports/latex_build/logs/research_tracks__T3_ALPHA__hecke_alpha_connection.tex__92be42bc1e.txt` |
| failed | `research_tracks/T3_ALPHA/hecke_lepton_mass_verification.tex` | `pdflatex` | 2.0 | `reports/latex_build/logs/research_tracks__T3_ALPHA__hecke_lepton_mass_verification.tex__8c9d08f913.txt` |
| failed | `research_tracks/T3_ALPHA/integer_137_note.tex` | `pdflatex` | 5.1 | `reports/latex_build/logs/research_tracks__T3_ALPHA__integer_137_note.tex__bd8b9177b6.txt` |
| failed | `research_tracks/T3_ALPHA/modular_bootstrap_attempt.tex` | `pdflatex` | 6.0 | `reports/latex_build/logs/research_tracks__T3_ALPHA__modular_bootstrap_attempt.tex__e2f2273ca7.txt` |
| failed | `research_tracks/T3_ALPHA/neff_protocol_derivation.tex` | `pdflatex` | 5.8 | `reports/latex_build/logs/research_tracks__T3_ALPHA__neff_protocol_derivation.tex__8b32fd54a2.txt` |
| failed | `research_tracks/T3_ALPHA/vcw_exact_minimum.tex` | `pdflatex` | 6.2 | `reports/latex_build/logs/research_tracks__T3_ALPHA__vcw_exact_minimum.tex__67ed15f7f9.txt` |
| failed | `research_tracks/T3_ALPHA/zeta_regularisation_B.tex` | `pdflatex` | 6.0 | `reports/latex_build/logs/research_tracks__T3_ALPHA__zeta_regularisation_B.tex__88ae2672b0.txt` |
| failed | `speculative_extensions/causality/ctc_conditions.tex` | `pdflatex` | 5.0 | `reports/latex_build/logs/speculative_extensions__causality__ctc_conditions.tex__13bcb8fd6c.txt` |
| failed | `speculative_extensions/emergent_alpha_executive_summary.tex` | `pdflatex` | 3.8 | `reports/latex_build/logs/speculative_extensions__emergent_alpha_executive_summary.tex__9d8226c955.txt` |
| failed | `speculative_extensions/invisibility/st3_stability.tex` | `pdflatex` | 5.1 | `reports/latex_build/logs/speculative_extensions__invisibility__st3_stability.tex__2c52af72f2.txt` |
| failed | `speculative_extensions/priority_P3_consciousness_model/P3_toy_model_decision.tex` | `pdflatex` | 0.8 | `reports/latex_build/logs/speculative_extensions__priority_P3_consciousness_model__P3_toy_model_decision.tex__3d08641ca1.txt` |
| failed | `speculative_extensions/solution_consciousness_model_P3/consciousness_model_solution.tex` | `pdflatex` | 3.4 | `reports/latex_build/logs/speculative_extensions__solution_consciousness_model_P3__consciousness_model_solution.tex__13a85885e6.txt` |
| failed | `speculative_extensions/solution_consciousness_model_P3/fp_stationary_analysis.tex` | `pdflatex` | 0.4 | `reports/latex_build/logs/speculative_extensions__solution_consciousness_model_P3__fp_stationary_analysis.tex__322d9b0142.txt` |
| failed | `speculative_extensions/solution_consciousness_model_P3/fp_time_dynamics.tex` | `pdflatex` | 0.4 | `reports/latex_build/logs/speculative_extensions__solution_consciousness_model_P3__fp_time_dynamics.tex__a4237efa4b.txt` |
| failed | `speculative_extensions/solution_consciousness_model_P3/toy_model_decision.tex` | `pdflatex` | 0.4 | `reports/latex_build/logs/speculative_extensions__solution_consciousness_model_P3__toy_model_decision.tex__248ae3ed9c.txt` |
| failed | `speculative_extensions/UBT_HeckeWorlds_theta_zeta_primes_appendix.tex` | `pdflatex` | 3.4 | `reports/latex_build/logs/speculative_extensions__UBT_HeckeWorlds_theta_zeta_primes_appendix.tex__a4220eea4a.txt` |
