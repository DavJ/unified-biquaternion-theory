# UBT Repository Claim Map

**Purpose**: Map of all repository files relevant to each major physics claim.  
**Generated**: 2026-03-10  
**Mode**: verify_then_complete — sources verified against repository file content.

---

## How to Use This Map

Each claim section lists:
- **Status** — current proof level (PROVED / SEMI-EMPIRICAL / PARTIALLY_PRESENT / OPEN)
- **Primary sources** — authoritative files containing the derivation
- **Supporting sources** — files with background, motivation, or alternate derivations
- **Bridge document** — navigation file cross-referencing all relevant pieces

Proof-level labels:
- `[L0]` — exact algebraic/geometric identity, no free parameters
- `[L1]` — proved given verified assumptions
- `[L2]` — requires additional lemmas not yet proved
- `[SE]` — semi-empirical: result matches observation but derivation has open parameter
- `[P]`  — partially present: framework exists but derivation is incomplete
- `[O]`  — open problem: no complete derivation yet in repository

---

## 1. GR Recovery

**Status**: PROVED [L1] (Steps 1–5); OPEN [L2] (Step 6)

| Step | Claim | Primary Source | Status |
|------|-------|---------------|--------|
| 1 | Metric emergence: Θ → g_μν | `canonical/geometry/metric.tex` §2; `canonical/geometry/biquaternion_metric.tex` | PROVED [L1] |
| 1b | Equivalence of derivative and tetrad definitions | `consolidation_project/GR_closure/step1_metric_bridge.tex` | PROVED [L0] |
| 2 | Non-degeneracy of projected metric | `consolidation_project/GR_closure/step2_nondegeneracy.tex` | PROVED [L0] |
| 3 | Lorentzian signature | `consolidation_project/GR_closure/step3_signature_theorem.tex` | PROVED [L0] |
| 4 | Levi-Civita connection and Riemann curvature | `canonical/geometry/connection.tex`; `canonical/geometry/curvature.tex` | Standard |
| 5 | Einstein field equations via Hilbert variation | `canonical/geometry/gr_as_limit.tex`; `consolidation_project/GR_closure/GR_chain_summary.tex` | PROVED [L1] |
| 6 | Off-shell Θ-only closure | `canonical/geometry/gr_completion_attempt.tex` | OPEN [L2] |

**Bridge**: `canonical/bridges/GR_chain_bridge.tex`

**Supporting sources**:
- `THEORY/architecture/geometry/biquaternion_curvature.tex`
- `THEORY/architecture/geometry/biquaternion_stress_energy.tex`
- `consolidation_project/appendix_A_biquaternion_gravity_consolidated.tex`
- `unified_biquaternion_theory/ubt_appendix_1_biquaternion_gravity.tex`

---

## 2. Action Principle

**Status**: PROVED [L1]

| Claim | Primary Source | Status |
|-------|---------------|--------|
| Biquaternionic action functional | `unified_biquaternion_theory/ubt_appendix_1_biquaternion_gravity.tex` §1 | PROVED [L1] |
| Hilbert variation of action | `canonical/geometry/gr_as_limit.tex` §3 | PROVED [L1] |
| Matter coupling via covariant derivative | `canonical/interactions/qed.tex` §2 | PROVED [L1] |

**Supporting sources**:
- `consolidation_project/T_munu_derivation/`
- `THEORY/architecture/geometry/biquaternion_stress_energy.tex`

---

## 3. Stress-Energy Tensor Derivation

**Status**: PROVED [L1]

| Claim | Primary Source | Status |
|-------|---------------|--------|
| T_μν definition from Lagrangian variation | `canonical/geometry/stress_energy.tex` | PROVED [L1] |
| Off-shell T_μν closure | `consolidation_project/GR_closure/step4_offshell_Tmunu.tex` | PROVED [L1] |
| Biquaternionic stress-energy | `canonical/geometry/biquaternion_stress_energy.tex` | PROVED [L1] |

**Supporting sources**:
- `THEORY/architecture/geometry/stress_energy.tex`
- `consolidation_project/T_munu_derivation/`

---

## 4. QED Limit

**Status**: PARTIALLY_PROVED — U(1), Maxwell, Lagrangian PROVED; B_base OPEN

| Claim | Primary Source | Status |
|-------|---------------|--------|
| QED Lagrangian from UBT | `canonical/interactions/qed.tex` §1 | PROVED [L1] |
| U(1) gauge invariance | `canonical/interactions/qed.tex` §2; `canonical/interactions/sm_gauge.tex` | PROVED [L1] |
| Massless photon | `canonical/interactions/qed.tex` §3 | PROVED [L1] |
| B₀ = 8π (bare coupling) | `canonical/interactions/qed.tex` §4 | PROVED [L1] |
| B_α ≈ 46.3 (radiative correction) | `canonical/interactions/qed.tex` §5 | SEMI-EMPIRICAL [SE] |
| B_base = N_eff^(3/2) = 41.57 exponent | *(22 approaches tested, none complete)* | OPEN [O] |
| Anomalous magnetic moment g−2 | `canonical/interactions/qed.tex` §7 | SEMI-EMPIRICAL [SE] |

**Bridge**: `canonical/bridges/QED_limit_bridge.tex`

**Supporting sources**:
- `consolidation_project/appendix_D_qed_consolidated.tex`
- `consolidation_project/appendix_ALPHA_one_loop_biquat.tex`
- `consolidation_project/new_alpha_derivations/`
- `unified_biquaternion_theory/solution_P4_fine_structure_constant/`

---

## 5. Maxwell Limit

**Status**: PROVED [L1] (follows from QED sector)

| Claim | Primary Source | Status |
|-------|---------------|--------|
| Electromagnetic field tensor F_μν | `canonical/interactions/qed.tex` §2 | PROVED [L1] |
| Maxwell equations (source-free) | `canonical/interactions/qed.tex` §3 | PROVED [L1] |
| Maxwell equations (with current) | `consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex` §2 | PROVED [L1] |
| EM tensor from biquaternion decomposition | `THEORY/math/fields/biquaternion_algebra.tex` | PROVED [L1] |

**Bridge**: `canonical/bridges/Maxwell_limit_bridge.tex`

**Supporting sources**:
- `consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex`
- `THEORY/architecture/geometry/exotic_regimes.tex`

---

## 6. Gauge Group Emergence

**Status**: SU(3)×SU(2)_L×U(1)_Y PROVED [L0]; Weinberg angle SEMI-EMPIRICAL [SE]

| Claim | Primary Source | Status |
|-------|---------------|--------|
| SU(3)_c from ℂ⊗ℍ involutions | `canonical/interactions/sm_gauge.tex` Theorems G.A–G.D | PROVED [L0] |
| SU(2)_L from norm-preserving left action | `canonical/interactions/sm_gauge.tex` §2 | PROVED [L0] |
| U(1)_Y from scalar phase right action | `canonical/interactions/sm_gauge.tex` §3 | PROVED [L0] |
| ℂ⊗ℍ ≅ Mat(2,ℂ) algebraic identity | `canonical/interactions/sm_gauge.tex` §1 | PROVED [L0] |
| Three generations from ψ-winding | `canonical/interactions/sm_gauge.tex` §4 | PROVED [L0] |
| Weinberg angle θ_W ≈ 0.23122 | `canonical/interactions/sm_gauge.tex` §5 | SEMI-EMPIRICAL [SE] |
| Chirality (left-handed only) | `canonical/interactions/sm_gauge.tex` §2b | MOTIVATED [L2] |
| Color confinement | `consolidation_project/confinement/`; `consolidation_project/appendix_K5_Lambda_QCD.tex` | CONJECTURED [L2] |

**Bridge**: `canonical/bridges/gauge_emergence_bridge.tex`

**Supporting sources**:
- `consolidation_project/appendix_E_SM_QCD_embedding.tex`
- `consolidation_project/SU3_derivation/`
- `consolidation_project/chirality_derivation/`
- `unified_biquaternion_theory/ubt_appendix_10_standard_model.tex`

---

## 7. Fermion Sector

**Status**: PARTIALLY_PRESENT [P] — Dirac equation present; masses semi-empirical

| Claim | Primary Source | Status |
|-------|---------------|--------|
| Dirac equation from UBT | `canonical/interactions/qed.tex` §4 | PRESENT [P] |
| Fermion mass formula | `unified_biquaternion_theory/fermion_mass_derivation_complete.tex` | SEMI-EMPIRICAL [SE] |
| Electron mass m_e ≈ 0.511 MeV (0.22% accuracy) | `consolidation_project/electron_mass/`; `consolidation_project/masses/` | SEMI-EMPIRICAL [SE] |
| Quark masses and CKM | `consolidation_project/appendix_QA2_quarks_CKM.tex` | PARTIAL [P] |
| Neutrino sector | *(see consolidation_project/appendix neutrino files)* | PARTIAL [P] |

**Supporting sources**:
- `consolidation_project/electron_mass/`
- `consolidation_project/masses/`
- `unified_biquaternion_theory/solution_theta_particle_model_P2/`
- `unified_biquaternion_theory/priority_P2_electron_model/`

---

## 8. Fine Structure Constant (α program)

**Status**: SEMI-EMPIRICAL [SE] — B₀ proved; B_base exponent OPEN

| Claim | Primary Source | Status |
|-------|---------------|--------|
| α formula: α = B₀/(B_base + B_α) | `canonical/interactions/qed.tex` §5 | PROVED structure [L1] |
| B₀ = 8π | `canonical/interactions/qed.tex` §4 | PROVED [L1] |
| B_α ≈ 46.3 (running correction) | `consolidation_project/alpha_derivation/` | SEMI-EMPIRICAL [SE] |
| B_base ≈ 41.57 numerical value | `consolidation_project/appendix_ALPHA_padic_derivation.tex` | PRESENT [P] |
| B_base = N_eff^(3/2) exponent = 3/2 | *(22 approaches tested; none complete)* | OPEN [O] |
| N_eff = 11.53 from BRST | `THEORY/axioms/core_assumptions.tex` A1–A3 | MOTIVATED [L2] |
| R ≈ 1.114 geometric factor | *(8 approaches tested; none complete)* | OPEN [O] |

**Supporting sources**:
- `consolidation_project/appendix_ALPHA_one_loop_biquat.tex`
- `consolidation_project/new_alpha_derivations/`
- `unified_biquaternion_theory/solution_P4_fine_structure_constant/`
- `unified_biquaternion_theory/priority_P4_fine_structure/`

---

## 9. Cosmology Predictions

**Status**: PARTIALLY_PRESENT [P] — framework present; predictions not yet empirically confirmed

| Claim | Primary Source | Status |
|-------|---------------|--------|
| Dark matter as Hopfion soliton | `unified_biquaternion_theory/solution_P5_dark_matter/dark_matter_hopfion_solution.tex` | CONJECTURED [L2] |
| Dark energy from imaginary curvature | `unified_biquaternion_theory/solution_P6_dark_energy/` | PARTIAL [P] |
| Effective N_eff predictions | `consolidation_project/N_eff_derivation/` | PARTIAL [P] |
| CMB TT-spectrum | `consolidation_project/appendix_W_testable_predictions.tex` | PARTIAL; NULL result vs data [P] |
| Holographic dark energy | `consolidation_project/appendix_N_holographic_verlinde_desitter.tex` | CONJECTURED [L2] |

**Supporting sources**:
- `unified_biquaternion_theory/priority_P5_dark_matter/`
- `unified_biquaternion_theory/priority_P6_dark_energy/`
- `consolidation_project/appendix_B_scalar_imaginary_fields_consolidated.tex`

---

## 10. Additional Claims

| Claim | Primary Source | Status |
|-------|---------------|--------|
| Quantum gravity unification | `consolidation_project/appendix_QG_quantum_gravity_unification.tex` | PARTIAL [P] |
| S-matrix / perturbative QFT dynamics | *(no source found)* | ABSENT [O] |
| Closed Timelike Curves | `speculative_extensions/appendices/` | SPECULATIVE |
| Consciousness field (psychons) | `canonical/consciousness/psychons.tex`; `speculative_extensions/complex_consciousness/` | SPECULATIVE |
| Riemann Hypothesis connection | `research/rh_biquaternion_extension/` | SPECULATIVE |

---

## File Index by Claim Area

| Area | Canonical | Consolidation | Original | Bridge |
|------|-----------|---------------|---------|--------|
| GR | `canonical/geometry/*.tex` | `consolidation_project/GR_closure/` | `ubt_appendix_1_biquaternion_gravity.tex` | `GR_chain_bridge.tex` |
| Action | `canonical/geometry/gr_as_limit.tex` | `consolidation_project/T_munu_derivation/` | `ubt_appendix_1_biquaternion_gravity.tex` | — |
| QED | `canonical/interactions/qed.tex` | `appendix_D_qed_consolidated.tex` | `solution_P4_fine_structure_constant/` | `QED_limit_bridge.tex` |
| Maxwell | `canonical/interactions/qed.tex` §3 | `appendix_C_electromagnetism_gauge_consolidated.tex` | — | `Maxwell_limit_bridge.tex` |
| Gauge | `canonical/interactions/sm_gauge.tex` | `appendix_E_SM_QCD_embedding.tex` | `ubt_appendix_10_standard_model.tex` | `gauge_emergence_bridge.tex` |
| Fermion | `canonical/interactions/qed.tex` §4 | `electron_mass/`; `masses/` | `fermion_mass_derivation_complete.tex` | — |
| α | `canonical/interactions/qed.tex` §5 | `appendix_ALPHA_*.tex` | `solution_P4_fine_structure_constant/` | `QED_limit_bridge.tex` |
| Cosmology | — | `appendix_W_testable_predictions.tex` | `solution_P5_dark_matter/` | — |

---

*This map was generated by audit against repository file content.  
Do not modify claims without updating corresponding source files.*
