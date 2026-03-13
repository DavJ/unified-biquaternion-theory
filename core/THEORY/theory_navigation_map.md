# UBT Theory Navigation Map

**Purpose**: Help external physicists and reviewers find every major derivation
in the repository without reading all 270+ LaTeX files.  
**Date**: 2026-03-10  
**Scope**: Core theory only. Speculative extensions (consciousness, CTCs) are
in `speculative_extensions/` and are not mapped here.

---

## Quick Start: Where to Begin

| Your goal | Start here |
|-----------|-----------|
| Understand the theory in 5 minutes | `THEORY/README.md` |
| Read the canonical presentation | `canonical/UBT_canonical_main.tex` |
| Understand GR recovery | `canonical/bridges/GR_chain_bridge.tex` |
| Understand QED/Maxwell | `canonical/bridges/QED_limit_bridge.tex` and `canonical/bridges/Maxwell_limit_bridge.tex` |
| Understand gauge groups | `canonical/bridges/gauge_emergence_bridge.tex` |
| See what's proved vs open | `THEORY/status_overview.md` |
| See all claim sources | `AUDITS/repository_claim_map.md` |
| See full audit report | `AUDITS/copilot_repo_verification_and_gap_report.md` |

---

## Repository Layer Map

The repository has four content layers:

```
Layer 0 — Axioms (never change)
  THEORY/canonical/canonical_axioms.tex
  THEORY/axioms/core_assumptions.tex

Layer 1 — Canonical Definitions (stable)
  canonical/                     ← single source of truth
  THEORY/canonical/              ← clean canonical presentations

Layer 2 — Derivations and Proofs (version-controlled)
  consolidation_project/         ← compact structured presentation
  unified_biquaternion_theory/   ← original comprehensive derivations

Layer 3 — Navigation and Audits (documentation)
  THEORY/                        ← theory documentation
  AUDITS/                        ← verification reports
  canonical/bridges/             ← cross-reference bridge documents
```

---

## Navigation by Physics Topic

### 1. Foundations and Axioms

| Document | Content | Location |
|----------|---------|----------|
| Core axioms (A1–A6) | Biquaternion algebra, complex time, field equation | `THEORY/canonical/canonical_axioms.tex` |
| Full axiom discussion | Assumptions, disclaimers, out-of-scope | `THEORY/README.md` |
| Biquaternion algebra | ℂ⊗ℍ structure, involutions, Z₂³ grading | `canonical/fields/biquaternion_algebra.tex` |
| Complex time | τ = t + iψ, fiber structure | `canonical/fields/biquaternion_time.tex` |
| Θ field definition | Matrix representation, DoF counting | `canonical/fields/theta_field.tex` |

### 2. Action Principle

| Document | Content | Location |
|----------|---------|----------|
| Canonical action | S[Θ] decomposition, variation | `THEORY/canonical/canonical_action.tex` |
| Hilbert variation | Derivation of Einstein equations | `canonical/geometry/gr_as_limit.tex` §3 |
| Biquaternionic action | Original biquaternionic form | `unified_biquaternion_theory/ubt_appendix_1_biquaternion_gravity.tex` §1 |

### 3. Geometry and GR Recovery

| Document | Content | Location |
|----------|---------|----------|
| **Navigation bridge** | Steps 1–6 with file refs | `canonical/bridges/GR_chain_bridge.tex` |
| Biquaternionic metric | Definition, decomposition | `canonical/geometry/biquaternion_metric.tex` |
| Metric definition | g_μν = Re(G_μν[Θ]) | `canonical/geometry/metric.tex` |
| Metric definition (canonical) | Concise canonical form | `THEORY/canonical/canonical_metric_definition.tex` |
| Metric equivalence proof | Derivative ≡ tetrad definition | `consolidation_project/GR_closure/step1_metric_bridge.tex` |
| Non-degeneracy | det(g) ≠ 0 proof | `consolidation_project/GR_closure/step2_nondegeneracy.tex` |
| Signature theorem | (-,+,+,+) proof | `consolidation_project/GR_closure/step3_signature_theorem.tex` |
| T_μν off-shell | Off-shell stress-energy derivation | `consolidation_project/GR_closure/step4_offshell_Tmunu.tex` |
| GR limit | Einstein equations (any φ) | `canonical/geometry/gr_as_limit.tex` |
| Phase projection | Phase frame bundle, U(1) symmetry | `canonical/geometry/phase_projection.tex` |
| Connection | Γ^λ_μν derivation | `canonical/geometry/connection.tex` |
| Curvature | Riemann, Ricci tensors | `canonical/geometry/curvature.tex` |
| Stress-energy | T_μν derivation | `canonical/geometry/stress_energy.tex` |
| GR chain summary | Steps 1–6 with proof status | `consolidation_project/GR_closure/GR_chain_summary.tex` |
| Original GR appendix | Full original derivation | `unified_biquaternion_theory/ubt_appendix_1_biquaternion_gravity.tex` |
| Consolidated GR | Compact presentation | `consolidation_project/appendix_A_biquaternion_gravity_consolidated.tex` |

### 4. Electromagnetism and QED

| Document | Content | Location |
|----------|---------|----------|
| **Maxwell bridge** | Maxwell limit derivation chain | `canonical/bridges/Maxwell_limit_bridge.tex` |
| **QED bridge** | QED limit, α status, open gaps | `canonical/bridges/QED_limit_bridge.tex` |
| QED canonical | U(1), Maxwell, Dirac, B₀, B_α | `canonical/interactions/qed.tex` |
| Maxwell in UBT | F_μν = (E+iB)·σ, duality | `consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex` |
| QED extended | Renormalization, curved spacetime | `consolidation_project/appendix_D_qed_consolidated.tex` |
| α one-loop | One-loop fine structure constant | `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` |
| α p-adic | p-adic derivation of α | `consolidation_project/appendix_ALPHA_padic_derivation.tex` |
| New α derivations | 22+ approaches to B_base | `consolidation_project/new_alpha_derivations/` |

### 5. Gauge Group Emergence

| Document | Content | Location |
|----------|---------|----------|
| **Gauge bridge** | SU(3)×SU(2)_L×U(1)_Y status | `canonical/bridges/gauge_emergence_bridge.tex` |
| SM gauge canonical | Theorems G.A–G.D, generations | `canonical/interactions/sm_gauge.tex` |
| QCD canonical | SU(3) color details | `canonical/interactions/qcd.tex` |
| Algebra involutions | Z₂³ grading, ℂ⊗ℍ ≅ Mat(2,ℂ) | `canonical/algebra/involutions_Z2xZ2xZ2.tex` |
| SU(3) derivation | Explicit SU(3) construction | `consolidation_project/SU3_derivation/` |
| SM full embedding | SU(3)×SU(2)×U(1) embedding | `consolidation_project/appendix_E_SM_QCD_embedding.tex` |
| Chirality | ψ-parity mechanism | `consolidation_project/chirality_derivation/` |
| Original SM appendix | Original SM derivation | `unified_biquaternion_theory/ubt_appendix_10_standard_model.tex` |

### 6. Fermion Sector and Particle Masses

| Document | Content | Location |
|----------|---------|----------|
| Fermion mass derivation | Main mass formula | `unified_biquaternion_theory/fermion_mass_derivation_complete.tex` |
| Electron mass | m_e prediction (0.22% accuracy) | `consolidation_project/electron_mass/` |
| Particle masses | Mass hierarchy | `consolidation_project/masses/` |
| Quarks and CKM | Quark masses, CKM matrix | `consolidation_project/appendix_QA2_quarks_CKM.tex` |
| N_eff derivation | Effective d.o.f. count | `consolidation_project/N_eff_derivation/` |
| Theta-particle model | Original P2 solution | `unified_biquaternion_theory/solution_theta_particle_model_P2/` |

### 7. Fine Structure Constant

| Document | Content | Location |
|----------|---------|----------|
| Program status | Current status, open problems | `research/alpha_program_status.md` |
| QED bridge | α formula and open gaps | `canonical/bridges/QED_limit_bridge.tex` |
| α formula | B₀/(B_base+B_α) | `canonical/interactions/qed.tex` §5 |
| One-loop calculation | B_α numerical | `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` |
| p-adic approach | B_base via p-adic | `consolidation_project/appendix_ALPHA_padic_derivation.tex` |
| Original P4 solution | First derivation attempt | `unified_biquaternion_theory/solution_P4_fine_structure_constant/` |
| Python calculator | Numerical α computation | `unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_running_calculator.py` |

### 8. Cosmology and Dark Sector

| Document | Content | Location |
|----------|---------|----------|
| Testable predictions | CMB, cosmological constants | `consolidation_project/appendix_W_testable_predictions.tex` |
| Dark matter (Hopfion) | Hopfion soliton model | `unified_biquaternion_theory/solution_P5_dark_matter/dark_matter_hopfion_solution.tex` |
| Dark energy | Imaginary curvature model | `unified_biquaternion_theory/solution_P6_dark_energy/` |
| Holographic cosmology | Verlinde/de Sitter | `consolidation_project/appendix_N_holographic_verlinde_desitter.tex` |
| Quantum gravity | UBT quantum gravity | `consolidation_project/appendix_QG_quantum_gravity_unification.tex` |

### 9. Projection Rules

| Document | Content | Location |
|----------|---------|----------|
| Canonical projection rules | P1–P6 with sources | `THEORY/canonical/canonical_projection_rules.tex` |
| Phase projection | Phase frame bundle | `canonical/geometry/phase_projection.tex` |
| Full metric definition | Both equivalent forms | `THEORY/canonical/canonical_metric_definition.tex` |

---

## Full Document Inventory by Directory

### `THEORY/canonical/` — Compact canonical presentations

| File | Content |
|------|---------|
| `canonical_axioms.tex` | Core axioms A1–A6 |
| `canonical_action.tex` | Action principle and variational structure |
| `canonical_metric_definition.tex` | Metric derivation and rules |
| `canonical_field_equations.tex` | All field equations with status |
| `canonical_projection_rules.tex` | Rules P1–P6 for extracting observables |

### `canonical/bridges/` — Navigation bridge documents

| File | Content |
|------|---------|
| `GR_chain_bridge.tex` | GR recovery chain, Steps 1–6 |
| `QED_limit_bridge.tex` | QED limit, running α, open B_base |
| `Maxwell_limit_bridge.tex` | Maxwell equations as QED limit |
| `gauge_emergence_bridge.tex` | SU(3)×SU(2)_L×U(1)_Y status |

### `AUDITS/` — Verification and audit reports

| File | Content |
|------|---------|
| `repository_claim_map.md` | Map of files → physics claims |
| `claim_evidence_matrix.md` | Claim-by-claim evidence with status |
| `copilot_repo_verification_and_gap_report.md` | Full audit report |
| `minimal_completion_plan.md` | Minimal actions to close gaps |

### `THEORY/` — Theory status and navigation

| File | Content |
|------|---------|
| `README.md` | Theory overview and disclaimers |
| `theory_navigation_map.md` | **This file** |
| `status_overview.md` | Solved vs open problems |
| `axioms/core_assumptions.tex` | α-program core assumptions |
| `math/fields/` | Foundational field definitions |
| `architecture/geometry/` | Geometry definitions |

---

## Notation Reference

See `canonical/appendices/symbol_dictionary.tex` for the complete symbol dictionary.

Key symbols:
- `Θ(q,τ)` — fundamental biquaternionic field
- `τ = t + iψ` — complex time
- `G_μν` — biquaternionic metric
- `g_μν` — projected (real) metric
- `φ` — phase angle (gauge parameter)
- `κ = 8πG/c⁴` — gravitational coupling
- `B₀ = 8π` — bare electromagnetic coupling
- `B_base ≈ 41.57` — open parameter in α formula
- `N_eff ≈ 11.53` — effective BRST mode count

---

*This navigation map references files that exist in the repository as of 2026-03-10.
File paths are relative to the repository root.*
