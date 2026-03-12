<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# PUBLICATION GUIDE — Unified Biquaternion Theory

## 1. Overview: Publication Platforms and Strategy

Publishing UBT on multiple platforms maximizes reach, ensures long-term archival, and establishes scientific priority.

| Function | OSF | Zenodo |
|---|---|---|
| Type | Project + preprints | Archive repository |
| Preprints | ✅ Yes | ❌ No |
| GitHub integration | ✅ Yes | ✅ Yes (stronger) |
| DOI | CrossRef | DataCite |
| Recommendation | Preprints, discussion | Archival, citations |

**Recommendation: Publish on BOTH platforms.**

- **Zenodo** (https://zenodo.org/): CERN open repository; every upload gets a DOI; ideal for scientific archival, long-term access, and GitHub integration.
- **OSF / PhysArXiv** (https://osf.io/preprints/physarxiv): Preprint server + project management, operated by Center for Open Science. Offers preprint service, project repos with versioning, DOI (CrossRef), GitHub integration, peer moderation.

**Recommended preprint server for UBT:** PhysArXiv (https://osf.io/preprints/physarxiv)

### Repository Status

✅ Co je hotovo / What is ready:
- Email aktualizován / updated: jdavid.cz@gmail.com
- Zenodo guide completed
- OSF guide completed
- Repository release checklist completed
- Repozitář zkontrolován, 100% připraveno k publikaci / Repository checked, 100% ready for publication

---

## 2. Metadata Reference

Use the following metadata consistently across all platforms:

- **Title:** Unified Biquaternion Theory v10.0
- **Full title suggestion:** Unified Biquaternion Theory: Complex Time, Consciousness, and Field Unification
- **Author:** Ing. David Jaroš
- **Email:** jdavid.cz@gmail.com
- **Affiliation:** Independent Researcher (or institution if applicable)
- **ORCID:** (add if available)
- **Abstract:** use text from `UBT_Abstract_OSF.tex`
- **Keywords:** biquaternion algebra, complex time, unified field theory, General Relativity, quantum field theory, Standard Model, gauge unification, Hermitian gravity, SU(3) symmetry, theta functions, dark matter, dark energy, fermion masses
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Subject:** Physical Sciences → Physics → Theoretical Physics
- **Additional disciplines:** Mathematical Physics, Quantum Field Theory, Quantum Physics, Relativity and Gravitation, General Relativity
- **Conflict of Interest:** None
- **Funding:** leave empty or "Self-funded"

---

## 3. 4-Week Publication Checklist

### Týden / Week 1: GitHub Release

1. Go to https://github.com/DavJ/unified-biquaternion-theory → **Releases** → **Draft new release**
2. Tag version: `v10.0`
3. Title: `Unified Biquaternion Theory v10.0`
4. Description: see GitHub Release template in Section 4 below
5. Publish release

### Týden / Week 2: Zenodo

1. Go to https://zenodo.org/ → log in (or sign up via GitHub/ORCID)
2. Settings → GitHub → Connect (authorize)
3. Activate repository `DavJ/unified-biquaternion-theory`
4. Trigger from the GitHub release created in Week 1
5. Zenodo auto-creates record → add metadata (see Section 4) → publish → get DOI

### Týden / Week 3: OSF / PhysArXiv

1. Go to https://osf.io/preprints/physarxiv → **Submit a Preprint**
2. Upload `UBT_Main.pdf` or `UBT_Abstract_OSF.pdf`
3. Fill metadata (same as Zenodo; see Section 5)
4. Submit for moderation (1–3 days)
5. Get OSF DOI (format: `10.31219/osf.io/XXXXX`)

### Týden / Week 4: Connect and Announce

1. Update `README.md` with DOI badges (see Section 6)
2. Announce on: Twitter/X, LinkedIn, Physics Forums, Reddit r/Physics

---

## 4. Platform Guide: Zenodo

### Account Setup and GitHub Integration

- **Registration:** https://zenodo.org/ → Sign up (or login via GitHub/ORCID)
- **Krok / Step 1:** Create account
- **Krok / Step 2:** Connect GitHub: Settings → GitHub → Connect → authorize Zenodo
- **Krok / Step 3:** Activate the repository `DavJ/unified-biquaternion-theory` in the GitHub integration panel

### GitHub Release Template

When creating the GitHub release (Week 1), use the following description:

```
# Unified Biquaternion Theory v10.0 (November 2025)

## Major Updates
- Fermion masses derived from first principles with experimental validation
- SM gauge group SU(3)×SU(2)×U(1) rigorously derived from geometry
- Added comprehensive documentation and publication metadata

## Key Documents
- UBT_Main.pdf — Full consolidated theory document
- UBT_Abstract_OSF.pdf — Abstract for academic publication
- Complete appendices (F, G, H) with mathematical proofs

## Scientific Status
Research framework making first testable predictions. Scientific rating: 5.5/10.

## Citation
Jaroš, D. (2025). Unified Biquaternion Theory v10.0. Zenodo. https://doi.org/[DOI]

## License
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

### Step-by-Step Upload and Metadata

- **Krok / Step 4:** Zenodo auto-creates a record when a GitHub release is published (if GitHub integration is active)
- **Krok / Step 5:** Manual upload alternative: https://zenodo.org/deposit/new → Upload files

  **Files to upload:**
  - All PDFs from `docs/pdfs/`
  - `README.md`
  - `LICENSE.md`
  - `references.bib`
  - ZIP archive of the whole repository (optional but recommended)

- **Krok / Step 6:** Fill metadata:
  - **DOI:** leave empty — Zenodo assigns automatically
  - **Publication date:** November 2025
  - **Creators:** Jaroš, David + affiliation + ORCID
  - **Upload type:** Publication
  - **Publication type:** Preprint
  - **License:** CC Attribution 4.0 International
  - **Keywords:** (use the keyword list from Section 2)
  - **Subject:** Physics and Astronomy; sub-categories: Theoretical Physics, Mathematical Physics, Quantum Field Theory, General Relativity
  - **Related identifiers:** link to GitHub repository (`https://github.com/DavJ/unified-biquaternion-theory`)

- **Krok / Step 7:** Preview and publish → record receives a permanent DOI
- **Krok / Step 8:** After publication, update `README.md` with the Zenodo DOI badge (see Section 6)

**Manual upload checklist:** all PDFs, `README.md`, `LICENSE.md`, `references.bib`, ZIP archive

---

## 5. Platform Guide: OSF / PhysArXiv

### Option A: OSF Preprint (Recommended for Fast Publication)

1. Go to https://osf.io/preprints/physarxiv → **Submit a Preprint**
2. Upload main PDF: `UBT_Main.pdf` or `UBT_Abstract_OSF.pdf`
3. **Title:** Unified Biquaternion Theory: Complex Time, Consciousness, and Field Unification
4. **Authors:** David Jaroš; Affiliation: Independent Researcher (or institution); ORCID if available
5. **Abstract:** use text from `UBT_Abstract_OSF.tex`
6. **Discipline:** Physical Sciences and Mathematics → Physics → Theoretical Physics
   - Additional: Mathematical Physics, Quantum Physics, Relativity and Gravitation
7. **Tags:** same keyword list as in Section 2
8. **License:** CC-By Attribution 4.0 International
9. **Conflict of Interest:** None; **Funding:** leave empty or "Self-funded"
10. Submit for moderation → 1–3 days → DOI (format: `10.31219/osf.io/XXXXX`)

### Option B: OSF Project (For Comprehensive Management)

1. Go to https://osf.io/ → **Create Project** → name: "Unified Biquaternion Theory"
2. Connect GitHub repository (`DavJ/unified-biquaternion-theory`)
3. Upload documentation files
4. Create preprint from project

---

## 6. After Publication: Badges and Announcements

### README.md DOI Badges

After receiving DOIs from both platforms, update `README.md` with:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![OSF](https://img.shields.io/badge/OSF-Preprint-blue)](https://doi.org/10.31219/osf.io/XXXXX)
```

Replace `XXXXXXX` and `XXXXX` with the actual DOI identifiers received after publication.

### Announcement Channels

- Twitter/X
- LinkedIn
- Physics Forums
- Reddit r/Physics

---

## 7. Peer Review Roadmap

The peer review submission strategy is organized in phases, from mathematical foundations to specific physical predictions and extensions. Speculative content is excluded from near-term submission.

### Phase 1: Foundation Papers (Year 1)

#### Paper 1A: "Biquaternionic Field Theory: Mathematical Foundations"

- **Target journals:** Journal of Mathematical Physics, Communications in Mathematical Physics
- **Timeline:** 6–9 months
- **Content:**
  - Rigorous definition of B⁴ algebra
  - Inner product and Hilbert space structure
  - Covariant derivative
  - GR recovery proof
- **Prerequisites:** Complete mathematical foundations; independent verification of proofs

#### Paper 1B: "General Relativity as the Real Limit of Biquaternionic Field Theory"

- **Target journals:** Classical and Quantum Gravity, General Relativity and Gravitation
- **Timeline:** 3–6 months (Appendix R already exists)
- **Content:**
  - Einstein field equations recovery in the real limit
  - Compatibility with all GR tests
  - Observability of imaginary components
  - Comparison to other GR extensions
- **Expected challenges:** "What's new beyond GR?"; must address causality concerns

---

### Phase 2: Specific Predictions (Year 1–2)

#### Paper 2A: "Fine-Structure Constant from Complex Time Topology"

- **Target journals:** Physical Review D, Physics Letters B
- **Timeline:** 9–12 months
- **Content:**
  - Complete α⁻¹ = 137 derivation
  - B constant derivation
  - Geometric UV cutoff
  - Error analysis
  - Running to other energy scales
- **Prerequisites:** Eliminate all fitted parameters; calculate α⁻¹ at M_Z; address circular reasoning
- **Expected challenges:** High skepticism due to numerology concerns; must explain why N = 137 specifically
- **Alternative if full derivation is insufficient:** "Topological Constraints on Coupling Constants in Complex Time"

#### Paper 2B: "Electron Mass from Hopfion Topology in Biquaternionic Field Theory"

- **Target journals:** Physical Review D, European Physical Journal C
- **Timeline:** 6–9 months
- **Content:**
  - Hopfion soliton solution
  - Mass formula m(n) = A·nᵖ − B·n·ln(n)
  - Electron mass prediction (0.22% accuracy)
  - Topological stability analysis
- **Expected challenges:** Novel mass generation mechanism; referees may question stability; connection to Higgs mechanism needs clarification

---

### Phase 3: Extensions and Applications (Year 2–3)

#### Paper 3A: "Standard Model Gauge Group Emergence from Biquaternionic Automorphisms"

- **Target journals:** JHEP, Physical Review D
- **Timeline:** 9–12 months
- **Content:**
  - Proof that Aut(B⁴) ⊃ SU(3)×SU(2)×U(1)
  - Explicit connection 1-forms
  - Field strength tensors
  - Gauge invariance
  - Yukawa coupling emergence

#### Paper 3B: "Dark Sector Physics from p-adic Extensions"

- **Target journals:** Physical Review D, JCAP
- **Timeline:** 12–18 months
- **Content:**
  - p-adic extension of the biquaternionic framework
  - Dark matter candidate
  - Dark energy equation of state
  - Direct detection predictions

#### Paper 3C: "Modified Gravity Predictions at Quantum Scales"

- **Target journals:** Classical and Quantum Gravity
- **Timeline:** 12–15 months
- **Content:**
  - Phase curvature quantization effects
  - Comparison to quantum gravity phenomenology

---

### Speculative Content (NOT for Peer Review in the Near Term)

The following topics require substantial additional development before peer review submission:

- **Consciousness / Psychons:** Requires neuroscience foundation, quantitative predictions, brain imaging correlation, and ethics review. Realistic timeline: 5–10 years.
- **Closed Timelike Curves (CTCs):** Requires causality resolution, stability analysis, and energy conditions analysis. Timeline: 3–5 years.
- **Time Travel / Multiverse:** Highly speculative; unlikely publishable in mainstream physics journals in the foreseeable future.
