<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Concept Inventory and Triage

This document provides a full inventory of the major theory concepts in UBT,
their current file locations, authority layer status, and recommendations.

It is produced as part of the repository governance and content triage task
(March 2026). The primary status authority for derivation results is
`DERIVATION_INDEX.md`.

---

## Status Key

| Status | Meaning |
|--------|---------|
| ✅ CANONICAL | In canonical/, authoritative, correctly placed |
| 🔬 RESEARCH | In research_tracks/, active and correctly placed |
| 🔮 SPECULATIVE | In speculative_extensions/, correctly placed |
| 📦 ARCHIVED | In ARCHIVE/, correctly placed |
| ⚠️ MISPLACED | In wrong layer — see recommendation |

---

## Concept Inventory

### 1. Action Principle / Variational Structure

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| Action S[Θ,g] | `canonical/appendices/appendix_ACTION_review.tex` | ✅ CANONICAL | Proven [L0] | Keep |
| Θ-variation equation | `canonical/gr_closure/GR_chain_summary.tex` | ✅ CANONICAL | Proven [L0] | Keep |
| Metric variation | `canonical/gr_limit/GR_limit_of_UBT.tex` | ✅ CANONICAL | Proven [L1] | Keep |
| GR-sector conditions | `ARCHIVE/archive_legacy/consolidation_project/GR_closure/gr_sector_conditions.tex` | 📦 ARCHIVED | Referenced from DERIVATION_INDEX | Archive correct; add note |
| Theta-only closure step2 | `ARCHIVE/archive_legacy/consolidation_project/GR_closure/step2_theta_only_closure.tex` | 📦 ARCHIVED | Referenced | Archive correct |

**Verdict:** Action principle is canonically well-covered. Archived GR-closure
material is correctly archived; referenced in tests and DERIVATION_INDEX with
correct paths.

---

### 2. Emergent Metric / Metric Construction

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| Metric definition 𝒢_{μν} | `canonical/geometry/biquaternion_metric.tex` | ✅ CANONICAL | Proven [L0] | Keep |
| Projection rule g_{μν} := Re(𝒢_{μν}) | `canonical/geometry/metric.tex` | ✅ CANONICAL | Proven [L0] | Keep |
| Phase projection | `canonical/geometry/phase_projection.tex` | ✅ CANONICAL | Proven [L0] | Keep |
| AXIOMS metric lock (Axiom C) | `canonical/AXIOMS.md` | ✅ CANONICAL | Proven [L0] | Keep |

**Verdict:** Metric construction is canonically solid. The unique-metric axiom
is enforced by `tests/test_metric_lock.py`.

---

### 3. GR Closure / Einstein Recovery Chain

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| GR limit derivation | `canonical/gr_limit/GR_limit_of_UBT.tex` | ✅ CANONICAL | Proven [L1] | Keep |
| GR chain summary | `canonical/gr_closure/GR_chain_summary.tex` | ✅ CANONICAL | Proven [L1] | Keep |
| GR recovery levels | `docs/reports/gr_recovery_levels.md` | ✅ CANONICAL | Reference | Keep |
| UBT-GR relationship | `docs/ubt_gr_relationship.md` | ✅ CANONICAL | Reference | Keep |
| gr_as_limit.tex | `canonical/geometry/gr_as_limit.tex` | ✅ CANONICAL | Supporting | Keep |
| GR sector conditions (archived) | `ARCHIVE/archive_legacy/consolidation_project/GR_closure/gr_sector_conditions.tex` | 📦 ARCHIVED | Referenced | Archive correct |
| Theta variation note (archived) | `ARCHIVE/archive_legacy/consolidation_project/GR_closure/theta_vs_metric_variation_note.tex` | 📦 ARCHIVED | Referenced | Archive correct |

**Verdict:** GR closure chain is well-structured. Archived files are correctly
placed and referenced with updated paths.

---

### 4. QED for φ = const (Step-by-Step Chain)

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| U(1) protection | `canonical/qed_phi_const/step1_u1_protection.tex` | ✅ CANONICAL | Proven [L0] | Keep |
| Electron mass | `canonical/qed_phi_const/step2_electron_mass.tex` | ✅ CANONICAL | Proven [L1] | Keep |
| Beta function | `canonical/qed_phi_const/step3_beta_function.tex` | ✅ CANONICAL | Proven [L1] | Keep |
| Schwinger term | `canonical/qed_phi_const/step4_schwinger_term.tex` | ✅ CANONICAL | Proven [L1] | Keep |
| Lamb shift | `canonical/qed_phi_const/step5_lamb_shift.tex` | ✅ CANONICAL | Proven [L1] | Keep |
| QED summary | `canonical/qed_phi_const/step6_qed_summary.tex` | ✅ CANONICAL | Proven [L1] | Keep |

**Verdict:** QED φ=const chain is complete and canonically placed.

---

### 5. SU(3) / Triqubit Mapping

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| SU(3) from involutions (canonical) | `canonical/su3_derivation/su3_from_involutions.tex` | ✅ CANONICAL | Proven [L0] ⭐ | Keep — canonical source |
| Involution summary | `canonical/su3_derivation/step1_involution_summary.tex` | ✅ CANONICAL | Proven [L0] | Keep |
| Superposition approach | `canonical/su3_derivation/step1_superposition_approach.tex` | ✅ CANONICAL | Proven [L0] | Keep |
| SU(3) topic index | `canonical/THEORY/topic_indexes/SU3_index.md` | ✅ CANONICAL | Index | Keep |
| Qubit mapping sandbox | `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/` | 🔬 RESEARCH | Mathematical Sandbox | Keep — independent homomorphism |
| QCD embedding (archived) | `ARCHIVE/archive_legacy/consolidation_project/appendix_E_SM_QCD_embedding.tex` | 📦 ARCHIVED | Supporting | Archive correct |

**Verdict:** SU(3) derivation is canonically well-covered. The qubit sandbox
is correctly in research_tracks as an independent alternative mapping.

---

### 6. Twistor Bridge (Penrose Twistor)

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| UBT↔twistor generators | `research_tracks/THEORY_COMPARISONS/penrose_twistor/twistor_core/ubt_generators.py` | 🔬 RESEARCH | Proven [L0] | Keep |
| Minkowski spinor | `research_tracks/THEORY_COMPARISONS/penrose_twistor/twistor_core/minkowski_spinor.py` | 🔬 RESEARCH | Proven [L0] | Keep |
| SU(2,2) structure | `research_tracks/THEORY_COMPARISONS/penrose_twistor/twistor_core/su22.py` | 🔬 RESEARCH | Proven [L0] | Keep |
| Conformal action | `research_tracks/THEORY_COMPARISONS/penrose_twistor/twistor_core/conformal.py` | 🔬 RESEARCH | Computed | Keep |
| Curved sector bridge | `research_tracks/THEORY_COMPARISONS/penrose_twistor/curved_bridge_todo.md` | 🔬 RESEARCH | Open | Keep |
| Status | `research_tracks/THEORY_COMPARISONS/penrose_twistor/STATUS.md` | 🔬 RESEARCH | Index | Keep |

**Verdict:** Twistor bridge is correctly placed in research_tracks as an active
comparison study. DERIVATION_INDEX.md paths were fixed (now include full path
prefix `research_tracks/THEORY_COMPARISONS/penrose_twistor/`).

---

### 7. Holography / AdS Material

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| Hubble latency / holography | `canonical/HUBBLE_LATENCY/` | ✅ CANONICAL | Reference | Keep |

**Verdict:** Holography material is limited in scope. AdS/CFT connections are
not a primary development track currently.

---

### 8. Alpha Derivation Lines

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| Alpha topic index | `canonical/THEORY/topic_indexes/alpha_index.md` | ✅ CANONICAL | Index | Keep |
| Alpha geometry appendix | `canonical/appendices/appendix_alpha_geometry.tex` | ✅ CANONICAL | Supporting | Keep |
| B_base derivation | `canonical/interactions/B_base_derivation_complete.tex` | ✅ CANONICAL | Partial [L1] | Keep |
| N_eff derivation chain | `canonical/n_eff/` | ✅ CANONICAL | Proven [L0] | Keep |
| PROOFKIT_ALPHA | `docs/PROOFKIT_ALPHA.md` | ✅ CANONICAL | Status doc | Keep |
| Multi-channel α framework | `docs/OVERVIEW.md`, `docs/FITTED_PARAMETERS.md` | ✅ CANONICAL | Reference | Keep |
| Alpha two-loop grid | `data/alpha_two_loop_grid.csv` | ✅ CANONICAL | Generated output | Keep |
| Alpha derivation archive (various) | `ARCHIVE/archive_legacy/consolidation_project/alpha_derivation/` | 📦 ARCHIVED | Historical | Archive correct |
| NCG appendix (archived) | `ARCHIVE/archive_legacy/consolidation_project/appendix_ALPHA_one_loop_biquat.tex` | 📦 ARCHIVED | Referenced | Archive correct |

**Verdict:** Alpha derivation is split across canonical (structure) and
research_tracks (numerical explorations). Archived derivation attempts are
correctly placed.

---

### 9. Fermion / Standard Model Bridge

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| SM gauge structure | `canonical/interactions/sm_gauge.tex` | ✅ CANONICAL | Reference | Keep |
| QCD embedding | `canonical/interactions/qcd.tex` | ✅ CANONICAL | Proven [L1] | Keep |
| Chirality chain | `canonical/chirality/` | ✅ CANONICAL | Proven [L1] | Keep |
| QM emergence chain | `canonical/qm_emergence/` | ✅ CANONICAL | Proven [L1] | Keep |
| Three generations | `experiments/research_tracks/three_generations/` | 🔬 RESEARCH | Open Hard Problem | Keep |
| Fermion emergence | `research_tracks/research/theta_fermion_emergence.tex` | 🔬 RESEARCH | Structural | Keep |
| SM completion appendix | `canonical/appendices/appendix_SM_completion.tex` | ✅ CANONICAL | Reference | Keep |
| Fermion mass report | `docs/reports/lepton_audit/` | ✅ CANONICAL | Status docs | Keep |

**Verdict:** Fermion/SM bridge is partially canonical (gauge symmetry, chirality,
QM emergence) and partially research_tracks (fermion mass hierarchy, generation
structure). This is appropriate given the current proof status.

---

### 10. Consciousness / Psychon Models

| Item | Location | Status | DERIVATION_INDEX | Recommendation |
|------|----------|--------|-----------------|----------------|
| Complex Consciousness Theory | `speculative_extensions/complex_consciousness/` | 🔮 SPECULATIVE | Not indexed | Keep in speculative |
| Psychon appendices | `speculative_extensions/appendices/` | 🔮 SPECULATIVE | Not indexed | Keep in speculative |

**Verdict:** Consciousness material is correctly isolated in
`speculative_extensions/`. It must not migrate to canonical or research_tracks.

---

## Summary of Actions Taken

1. **DERIVATION_INDEX.md paths repaired** — penrose_twistor file references
   corrected from bare `penrose_twistor/...` to
   `research_tracks/THEORY_COMPARISONS/penrose_twistor/...`

2. **All archive references updated** — test files and shim scripts updated
   from `archive/` (obsolete path) to `ARCHIVE/archive_legacy/` (correct path)

3. **Validation boundary enforced** — ARCHIVE/ is now excluded from all
   canonical validation checks (test_ubt_tex_invariants, test_no_hardcoded_constants,
   test_no_core_hardcoded_after_snippets, test_metric_lock, audit_computed_not_reference)

4. **No concepts found to promote** — all significant theory content is already
   in the correct layer

5. **No concepts found to demote** — no misplaced content detected in canonical/
   or research_tracks/

---

## Remaining Open Issues

1. **Fine structure constant α** — derivation of α from first principles
   remains an open problem. The multi-channel stability framework provides
   strong numerical support for n=137 but not a complete first-principles proof.
   Status: OPEN HARD PROBLEM (correctly documented in DERIVATION_INDEX.md).

2. **B_base coefficient k=1** — the Kac-Moody level k=1 argument is a
   motivated conjecture. Status: PARTIAL [L1] (correctly documented).

3. **Fermion mass hierarchy** — the instanton-mediated mixing mechanism for
   lepton mass ratios remains an open problem. Status: OPEN (correctly documented).

4. **Θ-only termwise separation** — the full Θ-only derivation of Einstein
   equations (without sector conditions) is not yet proved. Status: documented
   in `docs/reports/gr_recovery_levels.md`.

---

*This inventory was produced March 2026 as part of the repository governance task.*  
*For derivation status, see `DERIVATION_INDEX.md`.*  
*For layer definitions, see `docs/REPO_LAYERS.md`.*
