> **GEOMETRY STATUS (2026-07-15):** Projection-based metric statements in this historical planning/audit document are superseded by the central covariant-tetrad metric.

<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT Phase 1 Consolidation Roadmap

**Date**: 2025-11-14  
**Status**: Phase 1 Complete  
**Next**: Phase 2-3 Implementation

---

## Overview

This document provides a detailed roadmap for completing the UBT consolidation according to COPILOT_INSTRUCTIONS_CONSOLIDATION.md. Phase 1 (directory structure and canonical definitions) is complete. This roadmap outlines the remaining work.

---

## Phase 1: Directory Restructuring ✅ COMPLETE

### Completed Tasks

- [x] Created `canonical/` directory with subdirectories:
  - [x] `canonical/fields/`
  - [x] `canonical/geometry/`
  - [x] `canonical/interactions/`
  - [x] `canonical/consciousness/`
  - [x] `canonical/appendices/`

- [x] Created master documentation:
  - [x] `CANONICAL_DEFINITIONS.md` - Master definitions document
  - [x] `README.md` - Canonical directory documentation

- [x] Created canonical LaTeX files:
  - [x] `fields/theta_field.tex` - Θ(q,τ) field definition
  - [x] `fields/complex_time.tex` - Complex time τ = t + iψ
  - [x] `geometry/metric.tex` - Metric tensor g_μν
  - [x] `geometry/stress_energy.tex` - Stress-energy T_μν
  - [x] `interactions/qed.tex` - QED Lagrangian
  - [x] `interactions/qcd.tex` - QCD Lagrangian
  - [x] `interactions/sm_gauge.tex` - Full SM gauge structure
  - [x] `appendices/symbol_dictionary.tex` - Symbol standardization

- [x] Created main article template:
  - [x] `UBT_canonical_main.tex` - 12-section structure

### Key Achievements

1. **Conflict Resolution**: Resolved 10+ major conflicts in definitions (complex time, field dimension, metric, stress-energy, QED, QCD, notation)

2. **Symbol Standardization**: Established unique meaning for all symbols (α, ψ, τ, Θ, etc.)

3. **Mathematical Rigor**: All definitions include:
   - Explicit mathematical formulas
   - Properties and derivations
   - Conflict resolution notes
   - Connection to standard physics

4. **Documentation**: Comprehensive LaTeX files ready for Phase 2-3 consolidation

---

## Phase 2: Canonical Definitions 🚧 IN PROGRESS

### Remaining Tasks

- [ ] Complete remaining canonical files:
  - [ ] `fields/electron_mass.tex` - Unified electron mass (resolve 3-method conflict)
  - [ ] `geometry/curvature.tex` - Riemann tensor, Christoffel symbols
  - [ ] `consciousness/psychons.tex` - Psychon field definition
  - [ ] `consciousness/theta_resonator.tex` - Experimental design
  - [ ] `fields/biquaternion_algebra.tex` - Mathematical foundations

- [ ] Verify all canonical definitions:
  - [ ] Mathematical consistency checks
  - [ ] Cross-reference validation
  - [ ] Unit and dimension checks
  - [ ] Notation consistency

### Priority Order

1. **High Priority**:
   - Electron mass consolidation (resolve conflict)
   - Curvature tensors (needed for GR equivalence)
   - Biquaternion algebra (mathematical foundation)

2. **Medium Priority**:
   - Psychon formalization
   - Theta-resonator design

---

## Phase 3: Consolidation of Existing Content 📝 PLANNED

### Strategy

Use canonical definitions to consolidate existing appendices from `consolidation_project/`.

### Appendix Consolidation Plan

Based on `consolidation_project/metadata/todos.md`:

| Appendix | Target | Source Files | Status | Priority |
|----------|--------|--------------|--------|----------|
| A | Biquaternion Gravity | ubt_appendix_1, solution_P7 | To consolidate | High |
| B | Scalar Equations | ubt_appendix_2-4, solution_P1 | To consolidate | Medium |
| C | Electromagnetism | ubt_appendix_5-9 | To consolidate | High |
| D | QED/Dirac | ubt_appendix_10, solution_P2 | To consolidate | High |
| E | SM/QCD | appendix_E_SM_QCD_embedding.tex | ✅ Done | - |
| F | Psychons | ubt_appendix_12-13, solution_P3 | To consolidate | Medium |
| G | Dark Matter | appendix_U_dark_matter_unified_padic.tex | ✅ Done | - |
| H | Simulations | ubt_appendix_15, 18 | To consolidate | Medium |
| I | New Fields | ubt_appendix_16-17 | To consolidate | Medium |
| J | Visual Maps | ubt_appendix_19 | To consolidate | High |
| K | Constants | ubt_appendix_20, P4 solutions, alpha_* | To consolidate | Highest |
| M | Dark Energy | solution_P6 | To consolidate | Medium |
| O | p-adic | appendix_P_padic_rigorous.tex | To consolidate | Medium |
| P | Bibliography | ubt_appendix_21, references.bib | To consolidate | High |

### Consolidation Process

For each appendix:

1. **Review source files** - Identify all relevant content
2. **Extract canonical content** - Keep only material consistent with canonical definitions
3. **Rewrite using canonical notation** - Apply symbol dictionary
4. **Remove duplicates** - Eliminate redundant derivations
5. **Add cross-references** - Link to canonical sections
6. **Validate** - Check mathematical consistency

### Estimated Work

- **Appendix A (Gravity)**: 2-3 hours consolidation
- **Appendix C (EM)**: 3-4 hours (merge 5 files)
- **Appendix D (QED)**: 2-3 hours
- **Appendix K (Constants)**: 4-5 hours (critical, many sources)
- **Appendix J (Visual Maps)**: 1-2 hours
- **Others**: 1-2 hours each

**Total estimated**: ~25-30 hours for full consolidation

---

## Phase 4: Symbol Unification 🎯 PARTIALLY COMPLETE

### Completed

- [x] Created comprehensive symbol dictionary
- [x] Defined unique meanings for all major symbols
- [x] Documented forbidden uses
- [x] Established index conventions

### Remaining Tasks

- [ ] Global symbol replacement in existing files:
  - [ ] Scan all consolidation_project appendices
  - [ ] Identify conflicting symbol uses
  - [ ] Automated or manual replacement
  - [ ] Validation pass

- [ ] Cross-reference validation:
  - [ ] Check all \ref commands
  - [ ] Update section/equation references
  - [ ] Fix broken links

### Tools Needed

- Regex search/replace for symbols
- LaTeX reference checker
- Compilation validation

---

## Phase 5: Main Article Assembly 📖 TEMPLATE READY

### Current Status

- [x] 12-section template created (`UBT_canonical_main.tex`)
- [x] Structure follows COPILOT_INSTRUCTIONS
- [x] Canonical files ready to include

### Remaining Tasks

- [ ] Fill section content:
  1. [x] Introduction - Template exists
  2. [ ] Biquaternion algebra - Need to create
  3. [x] Theta field - Canonical file ready
  4. [x] Complex time - Canonical file ready
  5. [x] Geometry/metric - Canonical file ready
  6. [x] Stress-energy - Canonical file ready
  7. [ ] Einstein equation - Need derivation
  8. [x] QED - Canonical file ready
  9. [x] QCD - Canonical file ready
  10. [ ] Theta-functions - Need to consolidate
  11. [ ] Psychons - Need to create
  12. [ ] Experimental - Need to consolidate

- [ ] Add transitions between sections
- [ ] Write introduction and conclusions
- [ ] Create abstract
- [ ] Add figures/diagrams
- [ ] Compile and debug

---

## Phase 6: Research Extensions 🔬 PLANNED

### Strategy

Move speculative/experimental content to `research_extensions/` directory.

### Content to Move

From COPILOT_INSTRUCTIONS Phase 6:

- Holography content
- p-adic extensions (beyond canonical)
- Dark energy models (beyond basic)
- Multiverse speculation
- Experimental designs (beyond theta-resonator)

### Directory Structure

```
research_extensions/
├── holography/
│   ├── holographic_verlinde.tex
│   └── ads_cft_connection.tex
├── padic/
│   ├── padic_dark_matter.tex
│   └── padic_qcd.tex
├── dark_energy/
│   └── cosmological_models.tex
├── consciousness/
│   ├── ctc_time_travel.tex
│   └── multiverse_consciousness.tex
└── experimental/
    └── advanced_tests.tex
```

### Not to Move

Keep in main theory:
- Core p-adic results (Λ_QCD prediction)
- Basic dark matter/energy formulations
- Theta-resonator (primary experimental test)

---

## Conflict Resolution Tracking

### Resolved Conflicts ✅

1. **Complex time** - 3 versions → Canonical: τ = t + iψ (dynamic)
2. **Θ field dimension** - 3 versions → Canonical: C^(4×4) extendable to C^(8×8)
3. **Metric g_μν** - 3 derivations → Canonical: Re Tr(∂_μΘ ∂_νΘ†)
4. **T_μν** - 3 definitions → Canonical: Field-theoretic form
5. **QED** - Inconsistent → Canonical Lagrangian with curved spacetime
6. **QCD** - 3 versions → Canonical with emergent SU(3)
7. **SM gauge** - Inconsistent → Canonical SU(3)×SU(2)×U(1)
8. **α notation** - 4 meanings → Coupling constant ONLY
9. **ψ notation** - 4 uses → Imaginary time ONLY
10. **Theta functions** - 2 normalizations → Jacobi standard

### Remaining Conflicts 🚧

1. **Electron mass** - 3 calculation methods need unification
2. **Θ-resonance** - Needs mathematical formalization (Lagrangian)
3. **Minor notation** - Some appendices may still have local conflicts

---

## File Organization

### Do NOT Modify

Files in these directories are original research and must NOT be changed:

- `unified_biquaternion_theory/` - Original UBT documents
- `unified_biquaternion_theory/solution_*/` - Original solutions
- Any file with historical value

### Active Consolidation

Files being consolidated:

- `consolidation_project/appendix_*.tex` - Working appendices
- `consolidation_project/ubt_2_main.tex` - Full document
- `consolidation_project/ubt_core_main.tex` - Core theory

### Canonical Output

Final consolidated files:

- `canonical/` - All canonical definitions
- `canonical/UBT_canonical_main.tex` - Main article
- Future: `canonical/appendices/` - Consolidated appendices

---

## Timeline Estimate

### Phase 2 Completion
- **Remaining canonical files**: 1-2 days
- **Verification**: 1 day
- **Total**: 2-3 days

### Phase 3 Completion
- **High-priority appendices** (A, C, D, K, J, P): 2-3 weeks
- **Medium-priority appendices** (B, F, H, I, M, O): 1-2 weeks
- **Validation**: 1 week
- **Total**: 4-6 weeks

### Phase 4 Completion
- **Global symbol replacement**: 1 week
- **Cross-reference fixes**: 3-4 days
- **Total**: 1.5-2 weeks

### Phase 5 Completion
- **Content filling**: 2-3 weeks
- **Compilation/debugging**: 1 week
- **Total**: 3-4 weeks

### Phase 6 Completion
- **Organization**: 1 week
- **Content review**: 1 week
- **Total**: 2 weeks

**Grand Total**: 3-4 months for complete consolidation

---

## Success Criteria

### Phase 1 ✅
- [x] Directory structure created
- [x] Canonical definitions documented
- [x] Core TeX files created
- [x] No conflicts in canonical files

### Phase 2
- [ ] All canonical files complete
- [ ] Mathematical consistency verified
- [ ] All cross-references valid
- [ ] Compilation successful

### Phase 3
- [ ] All appendices consolidated
- [ ] No duplicate content
- [ ] Consistent notation throughout
- [ ] Proper citations

### Phase 4
- [ ] Symbol dictionary enforced
- [ ] No conflicting definitions
- [ ] All references updated
- [ ] Clean compilation

### Phase 5
- [ ] Main article complete
- [ ] All 12 sections filled
- [ ] Introduction and conclusions written
- [ ] Figures and tables included
- [ ] Bibliography complete
- [ ] Final PDF compiles

### Phase 6
- [ ] Research extensions organized
- [ ] Clear separation core/speculative
- [ ] Documentation complete

---

## Next Actions

### Immediate (This Week)
1. Create `fields/electron_mass.tex` (resolve 3-method conflict)
2. Create `geometry/curvature.tex`
3. Create `fields/biquaternion_algebra.tex`
4. Begin Appendix K consolidation (constants)

### Short-term (2-4 Weeks)
1. Complete remaining canonical files
2. Consolidate high-priority appendices (A, C, D, K, J, P)
3. Begin main article content filling

### Medium-term (1-2 Months)
1. Complete all appendix consolidations
2. Global symbol unification
3. Complete main article
4. Compilation and validation

### Long-term (3-4 Months)
1. Phase 6 organization
2. Final review and polish
3. Release preparation

---

## Questions and Decisions Needed

### Technical
1. Should electron mass use geometric, phase, or self-energy method? Or combine all three?
2. What level of detail for mathematical derivations in main article?
3. Include or exclude speculative consciousness content from core theory?

### Organizational
1. Create separate compilation targets for core vs. full theory?
2. Version numbering scheme for canonical files?
3. Changelog format and location?

---

## References

- `COPILOT_INSTRUCTIONS_CONSOLIDATION.md` - Master instructions
- `consolidation_project/metadata/todos.md` - Original consolidation plan
- `consolidation_project/metadata/consolidation_map.md` - File mapping
- `canonical/CANONICAL_DEFINITIONS.md` - Definitions reference
- `canonical/README.md` - Directory guide

---

**Last Updated**: 2025-11-14  
**Phase**: 1 Complete, 2 In Progress  
**Status**: Active Development
