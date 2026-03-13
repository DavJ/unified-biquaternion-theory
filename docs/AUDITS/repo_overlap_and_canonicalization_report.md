<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Repository Overlap and Canonicalization Report

**Date**: 2026-03-10  
**Author**: GitHub Copilot (verify-first mode)  
**Status**: Complete — covers all five target topics  
**Purpose**: Audit document mapping overlapping files, assigning roles, and recording
canonicalization decisions. This file is a **navigation map**, not a theory document.

---

## Summary

| Topic | Files audited | Canonical source | Overlapping duplicates | Open conflicts removed |
|-------|--------------|-----------------|----------------------|----------------------|
| SU(3) | 10 | `consolidation_project/appendix_G_internal_color_symmetry.tex` | 4 labelled | Yes |
| GR | 12 | `canonical/bridges/GR_chain_bridge.tex` + chain | 4 labelled | Yes |
| α (alpha) | 25+ | `STATUS_ALPHA.md` | ~12 labelled | Yes |
| Hecke / 137–139 | 20+ | `reports/hecke_lepton/` | 8 labelled | Yes |
| Mirror sector | 5 | `consolidation_project/mirror_sector/README.md` | 2 labelled | Yes |

Topic index files created in `THEORY/topic_indexes/`:
- `SU3_index.md`
- `GR_index.md`
- `alpha_index.md`
- `hecke_index.md`
- `mirror_sector_index.md`

---

## 1. SU(3) Color Symmetry

### Canonical Source
**`consolidation_project/appendix_G_internal_color_symmetry.tex`** ⭐

Contains the complete proof (Theorems G.A–G.D) in one place with zero free parameters.

### Overlapping / Duplicate Files

| File | Assigned Role | Notes |
|------|--------------|-------|
| `consolidation_project/SU3_derivation/step1_involution_summary.tex` | **supporting** | Abbreviated version of the canonical proof |
| `consolidation_project/SU3_derivation/step1_superposition_approach.tex` | **supporting** | Complementary derivation; valid but not the canonical derivation |
| `consolidation_project/SU3_derivation/step3_SU3_result.tex` | **supporting** | Result compilation; cross-references canonical |
| `Appendix_G_Emergent_SU3.tex` | **heuristic / motivating sketch** | Intuitive i,j,k → r,g,b sketch; file-level disclaimer present; NOT a proof |
| `THEORY_COMPARISONS/su3_qubit_mapping/` | **mathematical sandbox** | Independent Lie algebra homomorphism; separate from UBT first-principles derivation |

### Conflict Removed
Previous versions of status documents used "PROVEN" and "PROVED" inconsistently.
`DERIVATION_INDEX.md` now marks `appendix_G_internal_color_symmetry.tex` as
**CANONICAL ⭐** and labels the heuristic file explicitly.

---

## 2. General Relativity Recovery

### Canonical Source
**`canonical/bridges/GR_chain_bridge.tex`** (navigation) +  
Steps 1–5 in `consolidation_project/GR_closure/` + `canonical/geometry/`

### Overlapping / Duplicate Files

| File | Assigned Role | Notes |
|------|--------------|-------|
| `consolidation_project/appendix_A_biquaternion_gravity_consolidated.tex` | **historical** | Earlier consolidation; superseded by GR_closure/ chain |
| `docs/ubt_gr_recovery/gr_recovery_status.md` | **historical** | Older status snapshot; current state is in `AUDITS/repository_claim_map.md` |
| `reports/gr_recovery_final_status.md` | **historical** | Earlier status file |
| `QUANTUM_GRAVITY_IMPLEMENTATION_SUMMARY.md` | **historical** | Broader implementation summary; GR sub-claim covered by canonical chain |
| `docs/papers/appendix_GR_embedding.tex` | **supporting** | Hilbert variation; valid derivation reference but not the canonical entry |

### Conflict Removed
Multiple files contained "GR Recovery COMPLETE" without clearly stating that
Step 6 (off-shell Θ-only closure) is open at [L2]. The `GR_index.md` now
clarifies Steps 1–5 are proved and Step 6 is open, removing the ambiguity.

---

## 3. Fine Structure Constant (α)

### Canonical Source
**`STATUS_ALPHA.md`** — single master document covering the full derivation chain
and the complete gap landscape.

### Overlapping / Duplicate Files

| File | Assigned Role | Notes |
|------|--------------|-------|
| `emergent_alpha_calculations.tex` | **sandbox** | Exploratory; superseded by STATUS_ALPHA.md |
| `emergent_alpha_from_ubt.tex` | **sandbox** | Earlier narrative; superseded |
| `emergent_alpha_executive_summary.tex` | **sandbox** | Old executive summary |
| `appendix_C_geometry_alpha.tex` | **historical** | Earlier geometry approach; not current |
| `appendix_C_geometry_alpha_v2.tex` | **historical** | V2 of same |
| `alpha_padic_executive_summary.tex` | **sandbox** | p-adic extension; speculative |
| `reports/alpha_derivation_trace.md` | **historical** | Superseded by STATUS_ALPHA.md §9 |
| `reports/alpha_audit/alpha_paths.md` | **historical** | Path map superseded by STATUS_ALPHA.md §9 |
| `docs/ALPHA_FROM_ME_ANALYSIS.md` | **supporting** | Narrow specific analysis of matrix elements |
| `docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md` | **supporting** | Subset of STATUS_ALPHA material |
| `reports/ALPHA_FINDINGS.md` | **historical** | Findings report; current state in STATUS_ALPHA.md |
| `reports/ALPHA_IMPLEMENTATION_COMPLETE.md` | **historical** | Misleading title — implementation is partial (B_base open); see STATUS_ALPHA.md |

### Conflict Removed
`reports/ALPHA_IMPLEMENTATION_COMPLETE.md` has a title that could mislead readers
into thinking α derivation is fully complete. This is **not the case** — B_base and
R remain open. The file is labelled **historical** here, and `STATUS_ALPHA.md` is
the authoritative source with an honest gap inventory.

---

## 4. Hecke Operators and Twin Primes 137/139

### Canonical Source
**`reports/hecke_lepton/`** (numerical results) +  
**`consolidation_project/hecke_bridge/motivation.tex`** (theoretical motivation)

### Overlapping / Duplicate Files

| File | Assigned Role | Notes |
|------|--------------|-------|
| `research_tracks/three_generations/run_hecke_sage.py` | **sandbox** | Automation; outputs captured in canonical reports |
| `research_tracks/three_generations/run_hecke_lmfdb_search.py` | **sandbox** | LMFDB web search |
| `research_tracks/three_generations/search_hecke_lmfdb_api.py` | **sandbox** | LMFDB API variant |
| `research_tracks/three_generations/search_hecke_lmfdb_local.py` | **sandbox** | Local LMFDB variant |
| `research_tracks/three_generations/TASK_NEXT_HECKE.md` | **sandbox** | Research notes |
| `tex/UBT_hecke_L_route.tex` | **sandbox** | Earlier L-route narrative; superseded by `hecke_bridge/motivation.tex` |
| `papers/generated/ubt_cosmo_hecke_neff.tex` | **sandbox** | Generated paper sketch |
| `UBT_HeckeWorlds_theta_zeta_primes_appendix.tex` | **speculative** | Extends to multiverse; treat with caution |
| `speculative_extensions/UBT_HeckeWorlds_theta_zeta_primes_appendix.tex` | **speculative** | Duplicate of root file; placed in speculative_extensions/ directory |
| `consolidation_project/gap_A_resolution/A4_hecke_connection.tex` | **sandbox** | Speculative connection to alpha gap; not canonical |
| `consolidation_project/electron_mass/step1_hecke_conditional.tex` | **sandbox** | Conditional on unproved Hecke–mass link |

### Conflict Removed
The scan data in `scans/raw/` (20+ CSV files for k=137,139 channels) and the
CMB analysis scripts were competing with the theory documents for attention.
These are now clearly labelled **data** files that support (but do not constitute)
the Hecke theoretical claims. The canonical Hecke evidence is the SageMath
eigenvalue computation, not the CMB channel scans.

---

## 5. Mirror Sector

### Canonical Source
**`consolidation_project/mirror_sector/README.md`** +  
**`consolidation_project/mirror_sector/vacuum_stability.tex`** +  
**`reports/hecke_lepton/mirror_world_139.md`**

### Overlapping / Duplicate Files

| File | Assigned Role | Notes |
|------|--------------|-------|
| `UBT_HeckeWorlds_theta_zeta_primes_appendix.tex` | **speculative** | Contains mirror sector discussion but in a speculative multi-sector framework |
| `speculative_extensions/UBT_HeckeWorlds_theta_zeta_primes_appendix.tex` | **speculative** | Same file duplicated |

### Conflict Removed
The mirror sector was previously discussed in three separate places at varying
levels of speculation (vacuum stability, Hecke evidence, Hecke worlds). The
`mirror_sector_index.md` now unifies these and clearly separates the numerical
observation (Set B at p=139) from the speculative extrapolation (Hecke worlds
multiverse interpretation).

---

## 6. Audits vs. Theory: Separation of Concerns

A recurring problem was that audit documents (`AUDITS/`) competed with theory
documents for attention, and some contained partial derivations or conclusions
that overlapped with canonical theory files.

### Rule Applied
Audit files are **navigation maps and verification records**, not primary theory.
They should:
- Point to canonical sources
- Record verification status
- NOT contain new derivations or primary claims

| Audit File | Role | Status |
|-----------|------|--------|
| `AUDITS/claim_evidence_matrix.md` | **audit** | Maps claims → files; does NOT derive anything |
| `AUDITS/repository_claim_map.md` | **audit** | Maps claims → proof steps; does NOT derive anything |
| `AUDITS/copilot_repo_verification_and_gap_report.md` | **audit** | Verification report; does NOT derive anything |
| `AUDITS/minimal_completion_plan.md` | **audit** | Planning document |
| `AUDITS/repo_overlap_and_canonicalization_report.md` | **audit** | This file; navigation map only |

---

## 7. DERIVATION_INDEX Update

`DERIVATION_INDEX.md` has been updated to:
1. List canonical sources **first** in each table row
2. Apply consistent labelling: CANONICAL ⭐, supporting, heuristic, sandbox, speculative
3. Add cross-references to `THEORY/topic_indexes/` for each major topic

The update is targeted — only the labelling and ordering of existing entries was
changed, not the proof status of any claim.

---

## 8. Role Classification Legend

| Label | Meaning |
|-------|---------|
| **canonical ⭐** | Single authoritative source for this topic; start here |
| **supporting** | Valid derivation or data referenced by canonical source |
| **sandbox** | Exploratory code or text; outputs captured elsewhere |
| **heuristic** | Intuitive sketch or motivating argument; not a proof |
| **speculative** | Extrapolates beyond current evidence; clearly labelled |
| **historical** | Superseded by canonical source; preserved for reference |
| **data** | Raw numerical data or scan results |
| **audit** | Navigation map or verification record; not primary theory |

---

## 9. Files That Could Be Moved to `historical/`

The following files are candidates for archiving in a `historical/` directory
in a future cleanup pass. They are **not deleted** here per the
`do_not_delete_results_without_archiving` rule.

| File | Reason |
|------|--------|
| `emergent_alpha_calculations.tex` | Superseded by STATUS_ALPHA.md |
| `emergent_alpha_from_ubt.tex` | Superseded by STATUS_ALPHA.md |
| `emergent_alpha_executive_summary.tex` | Superseded by STATUS_ALPHA.md |
| `reports/ALPHA_IMPLEMENTATION_COMPLETE.md` | Misleading title; not complete |
| `reports/alpha_derivation_trace.md` | Superseded by STATUS_ALPHA.md §9 |
| `tex/UBT_hecke_L_route.tex` | Superseded by hecke_bridge/motivation.tex |
| `docs/ubt_gr_recovery/gr_recovery_status.md` | Superseded by AUDITS/repository_claim_map.md |
| `reports/gr_recovery_final_status.md` | Superseded by AUDITS/repository_claim_map.md |

Moving these files requires a dedicated archiving pass. This report documents
the intent; execution is deferred to preserve git history and avoid accidental loss.

---

## 10. Success Criteria Check

| Criterion | Met? | Evidence |
|-----------|------|----------|
| Each major topic has one canonical entry point | ✅ | `THEORY/topic_indexes/` created with one canonical per topic |
| Duplicate derivation paths are clearly labelled | ✅ | Role labels applied in all five topic indexes |
| Audits no longer compete with theory documents | ✅ | `AUDITS/` files are maps/records; theory stays in `canonical/`, `consolidation_project/` |
| External reader can find official UBT status in under 2 minutes | ✅ | Each index gives a "What a New Reader Should Do" section with ≤5 steps |

---

*This report is an audit document. It contains no new derivations or theoretical claims.*  
*All file status labels are documented here for navigational purposes only.*
