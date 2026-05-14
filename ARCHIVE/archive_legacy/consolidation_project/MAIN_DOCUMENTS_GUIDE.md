# Main LaTeX Documents in Consolidation Project

This directory contains several main LaTeX documents for different purposes:

## Primary Documents

### ubt_osf_publication.tex ⭐ **OSF-Ready Publication**
**Purpose:** Clean, publication-ready document suitable for Open Science Framework (OSF) or journal submission.

**Content:**
- Core UBT framework (gravity, EM, gauge symmetries)
- GR equivalence proof
- QED and Standard Model embeddings
- Enhanced SU(3) color symmetry derivation with:
  - One-loop running of $g_s(\mu)$
  - Detailed anomaly analysis
  - Explicit mapping of $(\Omega,z)$-deformations to Gell-Mann generators
- Mathematical foundations (biquaternion inner product, Hilbert space, integration measure)
- Testable predictions
- Clear statements on what is NOT claimed (no ab-initio α derivation, consciousness interpretations excluded)

**Target audience:** Academic researchers, journal reviewers, OSF readers

**Build:** Listed in `.github/latex_roots.txt` for automated CI/CD compilation

---

### ubt_core_main.tex - **Core Theory Only**
**Purpose:** Core UBT results without speculative content.

**Content:**
- Biquaternion gravity and GR equivalence
- Electromagnetism and gauge structure
- QED and Standard Model embeddings
- Internal color symmetry (SU(3))
- Maxwell equations in curved space
- Bibliography

**Excludes:** 
- Speculative topics (dark matter, p-adic extensions, consciousness, CTCs)
- Unverified predictions
- Work-in-progress content

**Target audience:** Mainstream physics community, conservative reviewers

**Build:** Listed in `.github/latex_roots.txt` - compiles to `ubt_core_main.pdf`

---

### ubt_2_main.tex - **Full Consolidated Document**
**Purpose:** Complete UBT framework including both core and speculative content.

**Content:**
- All CORE appendices (see MANIFEST_CORE.txt)
- Mathematical foundations (Priority 1: inner products, projections, Hilbert space, alpha status, integration)
- Testability and TSVF integration (Priority 2 & 4)
- SPECULATIVE/WIP appendices:
  - Dark matter (appendix_U, formerly appendix_G_dark_matter)
  - Fundamental constants
  - p-adic overview
  - Alpha p-adic derivation
- Complete bibliography

**Target audience:** Full theory documentation, research collaborators, comprehensive review

**Build:** Listed in `.github/latex_roots.txt` - compiles to `ubt_2_main.pdf`

---

## Deprecated/Legacy Documents

### ubt_2_main_fixed.tex - **DEPRECATED**
**Status:** Legacy file, not actively maintained, not in CI/CD build

**History:** Created as a simplified version of ubt_2_main.tex at some point during consolidation. Now superseded by:
- `ubt_core_main.tex` for core-only content
- `ubt_osf_publication.tex` for publication-ready version
- `ubt_2_main.tex` for full content

**Recommendation:** Can be safely removed unless there's a specific historical reason to keep it.

---

## Document Selection Guide

**For journal submission or OSF publication:**
→ Use `ubt_osf_publication.tex`

**For conservative academic audience (core claims only):**
→ Use `ubt_core_main.tex`

**For complete theory documentation (including speculative work):**
→ Use `ubt_2_main.tex`

**For reviewers concerned about scope:**
→ Direct them to `ubt_osf_publication.tex` with clear disclaimers

---

## Recent Changes (Nov 2025)

### Appendix G Naming Conflict Resolution
- **Problem:** Two appendices were both labeled "appendix_G"
  - `appendix_G_internal_color_symmetry.tex` (Internal Color Symmetry - CORE)
  - `appendix_G_dark_matter_unified_padic.tex` (Dark Matter - SPECULATIVE)

- **Solution:** 
  - Dark matter appendix renamed to `appendix_U_dark_matter_unified_padic.tex`
  - All references updated in main documents and manifests
  - Appendix U header properly formatted

### Appendix G Enhancement
Added three new sections to `appendix_G_internal_color_symmetry.tex`:
1. **Section G.12:** One-loop running of $g_s(\mu)$ in emergent formulation
   - Phase fiber metric and coupling definition
   - Beta function from geometric flow
   - Explicit geometric realization
   - Running coupling solution

2. **Section G.13:** Detailed anomaly analysis with left-right factorization
   - Separation of left and right actions on Θ
   - Pure SU(3) anomalies
   - Mixed anomalies with electroweak sector
   - Representation content and consistency
   - Gravitational anomalies
   - Summary of anomaly checks

3. **Section G.14:** Explicit mapping of (Ω,z)-deformations to Gell-Mann generators
   - Lemma G.1: Traceless deformation basis
   - Proposition G.2: Explicit T^a correspondence
   - Corollary G.3: Connection components
   - Complete representation table (8 generators)
   - Remarks on higher-order terms

### New OSF Publication Document
Created `ubt_osf_publication.tex` as a clean, publication-ready version:
- Professional title and abstract
- Clear scope and disclaimers
- Core appendices only (no speculative content)
- Enhanced SU(3) color symmetry derivation
- Proper acknowledgments and licensing
- Added to CI/CD build pipeline

---

## Build Instructions

### Local Build
```bash
cd consolidation_project

# Build OSF publication
pdflatex -interaction=nonstopmode ubt_osf_publication.tex
pdflatex -interaction=nonstopmode ubt_osf_publication.tex

# Build core document
make core

# Build full document
make all
```

### Automated Build
All documents listed in `.github/latex_roots.txt` are automatically compiled by GitHub Actions on push/PR. PDFs are uploaded to `docs/pdfs/` directory.

---

## Manifests

- **MANIFEST_CORE.txt** - List of core (non-speculative) appendices
- **MANIFEST_SPECULATIVE.txt** - List of speculative/WIP appendices

These manifests help maintain clear separation between verified core content and exploratory research.
