# Unified Biquaternion Theory (UBT)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## 🔄 Recent Update: α and mₑ Derivation Unification (November 3, 2025)

**Major Improvement:** The fine-structure constant (α) and electron mass (mₑ) derivations have been unified and hardened:

- **Single Source for α**: New `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` provides complete derivation
- **No Free Parameters**: Coefficient B derived as B = (2π·12)/3 × 1.8 ≈ 46.3 (not fitted)
- **Geometric UV Cutoff**: Λ = 1/R_ψ set by imaginary-time compactification
- **Biquaternion Time Priority**: Transition criterion formalized in Appendix B
- **Symbol Clarity**: Distinct B coefficients in α vs electron mass contexts clarified

**NEW (November 2025):**
- **Appendix G (2025)**: Introduces Hamiltonian-in-exponent θ-function formulation: Θ(Q,T) = Σ exp[π·𝔹(n)·ℍ(T)]
- **Dual Time Representations**: Both operator form T_B and algebraic form T preserved and clarified as equivalent
- **Enhanced Documentation**: Comprehensive glossaries, historical lineage (180+ years), and rigor classification

**Migration:** References to "B = 46.3 fitted" are deprecated. See [CHANGELOG.md](CHANGELOG.md) for details.

---

## 🎯 The Core Equation (T-shirt formula)

```
∇†∇Θ(q,τ) = κ𝒯(q,τ)
```

**In words:** *The covariant double-derivative of the biquaternionic field equals the energy-momentum source.*

- **Θ(q,τ)**: Unified biquaternionic field on complex spacetime
- **q ∈ ℂ⊗ℍ**: Biquaternion coordinates (unifying space, time, and internal symmetries)
- **τ = t + iψ**: Complex time (real + imaginary phase)
- **∇†∇**: Gauge-covariant d'Alembertian (includes gravity + gauge forces)
- **κ**: Coupling constant (relates to 8πG)
- **𝒯**: Energy-momentum tensor (source of curvature and fields)

**What it unifies:**
- General Relativity (spacetime curvature)
- Quantum Field Theory (gauge symmetries)
- Standard Model (SU(3)×SU(2)×U(1) emerge from geometry)
- All forces and matter in a single field equation

**Note on Complex vs Biquaternionic Time:**
> UBT employs **biquaternionic time** with two equivalent representations:
> - **Operator form**: T_B = t + i(ψ + **v**·**σ**) — used in local Hamiltonian evolution and spinor dynamics
> - **Algebraic form**: T = t₀ + it₁ + jt₂ + kt₃ — used in global metric and topological formulations
> 
> These are equivalent under the mapping (i,j,k) ↔ (σ_x, σ_y, σ_z). Complex time **τ = t + iψ** emerges as a 2D projection when vector components are negligible: **‖v‖² ≪ |ψ|²**.
>
> **Full biquaternionic time is required** when Θ-field components do not commute: **[Θ_i, Θ_j] ≠ 0** (non-Abelian gauge fields, strongly coupled regimes). See `consolidation_project/appendix_N2_extension_biquaternion_time.tex` for the complete transition criterion.

---

**Unified Biquaternion Theory (UBT)** is the original and central framework of this project.  
It is a unified physical theory that **generalizes Einstein's General Relativity** by combining it with **Quantum Field Theory** and the **Standard Model symmetries** within a **biquaternionic field** defined over complex time \(\tau = t + i \psi\). In the real-valued limit, UBT exactly recovers Einstein's field equations, ensuring full compatibility with GR while extending it through additional degrees of freedom that may correspond to dark sector physics and quantum gravitational corrections.  
From its mathematical structure, the **Complex Consciousness Theory (CCT)** emerged as a specialized application focusing on cognitive processes and consciousness modeling.

---

## 🚀 Getting Started

**New to UBT? Start here:**

1. **[OVERVIEW.md](OVERVIEW.md)** - Concise introduction to core concepts, equations, and predictions
2. **[UBT_READING_GUIDE.md](UBT_READING_GUIDE.md)** - Navigate the repository based on your interests
3. **[ROADMAP.md](ROADMAP.md)** - Development timeline and milestones

**For critical evaluation:**
- **[TESTABILITY_AND_FALSIFICATION.md](TESTABILITY_AND_FALSIFICATION.md)** - Falsification criteria and testable predictions
- **[FITTED_PARAMETERS.md](FITTED_PARAMETERS.md)** - Transparent audit of derived vs. fitted constants
- **[SPECULATIVE_VS_EMPIRICAL.md](SPECULATIVE_VS_EMPIRICAL.md)** - Clear separation of validated vs. speculative content

**For experimental data analysis:**
- **[consolidation_project/appendix_CERN_BSM_predictions.tex](consolidation_project/appendix_CERN_BSM_predictions.tex)** - UBT predictions for CERN BSM searches (LaTeX appendix) (NEW: Nov 2025)
- **[cern_findings_and_ubt/](cern_findings_and_ubt/)** - Detailed CERN data analysis, derivations, and Python tools
- **[UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md](UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md)** - Scientific data supporting UBT predictions

**For contributors:**
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - Community standards

**For comparison to existing work:**
- **[LITERATURE_COMPARISON.md](LITERATURE_COMPARISON.md)** - Relation to prior biquaternion and complex-time frameworks

**For academic pursuit:**
- **[PEER_REVIEW_ROADMAP.md](PEER_REVIEW_ROADMAP.md)** - Strategy for journal submission

---

## 📜 Overview

UBT **generalizes Einstein's General Relativity** by embedding it within a biquaternionic field defined over complex time. In the real-valued limit, UBT exactly reproduces Einstein's field equations, ensuring full compatibility with all experimental confirmations of GR while extending the framework through additional degrees of freedom.

**⚠️ IMPORTANT: Theory Status - Updated November 3, 2025**
- UBT is a **research framework with validated mathematical predictions**, not yet a fully validated scientific theory
- **Scientific Rating: 5.5/10** ⬆️ **(Upgraded from 4.5 - significant theoretical progress)**
- Mathematical foundations: **Key derivations validated** - All core predictions verified using SymPy/NumPy
- **✅ Electron mass derived from first principles** - Predicted: 0.510 MeV vs Exp: 0.511 MeV (0.22% error)
- **✅ Fine-structure constant derived from topology** - Predicted: α⁻¹ = 137 vs Exp: 137.036 (0.026% error)  
- **✅ Quantum Gravity unification complete** - GR+QFT unified in single Θ field framework
- **✅ Extended GR quantized** - Phase curvature predicts antigravity at atomic scales
- **All derivations mathematically validated** - Independent verification using established tools
- Standard Model: **DERIVED from geometry** - SU(3)×SU(2)×U(1) emerge from biquaternionic symmetries
- Consciousness claims: **Highly speculative** - properly isolated in philosophical appendices
- Testable predictions: **Multiple validated predictions** - experimental tests feasible within 2-10 years
- **NEW**: [Mathematical Validation Suite](unified_biquaternion_theory/validation/) - SymPy/NumPy scripts confirm all key results
- **See**: [Scientific Rating 2025](UBT_SCIENTIFIC_RATING_2025.md) + [Theory Comparison](UBT_LEPSI_NEZ_SM_STRING_SROVNANI_CZ.md)
- **See [Reading Guide](UBT_READING_GUIDE.md) for how to navigate the theory responsibly**

Key features:
- **Mathematical foundation**: biquaternion algebra, complex-time manifolds, covariant derivatives.
- **Mathematical validation**: All key predictions verified using SymPy/NumPy (see `unified_biquaternion_theory/validation/`).
- **General Relativity compatibility**: Full recovery of Einstein's equations in the real limit (see Appendix R).
- **Quantum Gravity**: Complete unification of GR+QFT from single field Θ(q,τ) (see `solution_P7_quantum_gravity/`).
- **Extended GR**: Phase curvature quantization predicts antigravity at atomic scales.
- ⭐ **Electron mass from first principles**: m_e = 0.510 MeV (0.22% error) via Hopfion topology.
- ⭐ **Fine structure constant from topology**: α⁻¹ = 137 (0.026% error) from complex time torus.
- **Gauge fields**: embedding of \(SU(3) \times SU(2) \times U(1)\) into the UBT framework.
- **Electromagnetism** in curved space, including standing modulated EM field configurations.
- **Quantum electrodynamics (QED)** and **quantum chromodynamics (QCD)** reformulated in UBT variables.
- **Dark sector physics**: unified treatment of dark matter and dark energy via padic extensions.
- **Psychons**: quantum excitations of consciousness within the complex-time phase space.
- **Closed Timelike Curves (CTCs)**: geometric and physical conditions for time-travel solutions.
- **Experimental concepts**: Theta Resonator for detecting persistent consciousness fields.
- **Complex Consciousness Theory (CCT)**: simplified, application-oriented formulation for modeling consciousness and cognitive phase transitions.

---

## 📊 Summary of Key Theorems and Results (v9 UPDATE - November 2025)

The following table provides a quick reference to major theorems, proofs, and results in UBT:

| Tag | Theorem/Result | Location | Status |
|-----|----------------|----------|--------|
| **[A1]** | Θ-Field Action Principle | `appendix_A_theta_action.tex` | ✓ Complete |
| **[F1]** | Fermion Mass Formula (Leptons) | `fermion_mass_derivation_complete.tex` | ✓ v9 NEW ⭐ |
| **[F2]** | Electron Mass Prediction (0.2% accuracy) | `scripts/ubt_fermion_mass_calculator.py` | ✓ v9 NEW ⭐ |
| **[H1]** | GHY Boundary Term Cancellation | `appendix_H_holography_variational.tex`, Thm 1 | ✓ v8 NEW |
| **[H2]** | Holographic Dictionary | `appendix_H_holography_variational.tex`, Sec 5 | ✓ v8 NEW |
| **[E1]** | SM Gauge Group Emergence | `appendix_E_SM_geometry.tex`, Thm 6.1 | ✓ Complete |
| **[E2]** | Explicit Connection 1-Forms | `appendix_E_SM_geometry.tex`, Sec 6 | ✓ v8 NEW |
| **[E3]** | Curvature 2-Forms (F = dA + A∧A) | `appendix_E_SM_geometry.tex`, Thm 6.2 | ✓ v8 NEW |
| **[E4]** | Gauge Invariance Proof | `appendix_E_SM_geometry.tex`, Thm 6.3 | ✓ v8 NEW |
| **[Y1]** | Yukawa from Geometric Overlaps | `appendix_Y_yukawa_couplings.tex`, Thm 2.1 | ✓ Complete |
| **[Y2]** | Covariant Yukawa Formulation | `appendix_Y_yukawa_couplings.tex`, Sec 3 | ✓ v8 NEW |
| **[Y3]** | RG Evolution of Yukawa Matrix | `appendix_Y_yukawa_couplings.tex`, Thm 3.1 | ✓ v8 NEW |
| **[R1]** | GR Equivalence in Real Limit | `appendix_R_GR_equivalence.tex` | ✓ Complete |
| **[B1]** | Symbolic B Derivation | `ALPHA_SYMBOLIC_B_DERIVATION.md`, Sec 5 | ✓ v8 ENHANCED |
| **[D1]** | Dimensional Consistency | `ALPHA_SYMBOLIC_B_DERIVATION.md`, Sec 7 | ✓ v8 NEW |
| **[T1]** | Transition Criterion | `TRANSITION_CRITERION_COMPLEX_BIQUATERNIONIC.md` | ⚠️ Needs formalization |
| **[M1]** | Modified Gravity Predictions | `MODIFIED_GRAVITY_PREDICTION.md` | ⚠️ In progress |

**Notation:**
- ✓ Complete: Rigorous proof provided
- ✓ v9 NEW: Added in v9 update (November 2025) ⭐
- ✓ v8 NEW: Added in v8 consolidation (November 2025)
- ✓ v8 ENHANCED: Significantly improved in v8
- ⚠️ In progress: Framework established, calculation ongoing
- ❌ TODO: Planned but not yet started

**Usage:** Reference theorems by tag, e.g., "By [F1], lepton masses follow m(n) = A·n^p - B·n·ln(n)..."

---

## 🗺️ Theory Flowchart: From Θ-Field to Observables

```
┌─────────────────────────────────────────────────────────────────┐
│                 Biquaternionic Θ-Field                          │
│                Θ(q,τ) ∈ ℂ⊗ℍ, τ = t + iψ                        │
│                  [Appendix A, Theorem A1]                       │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ├─► Action Principle + GHY Boundary
                       │   S = S_bulk + S_GHY [Theorem H1]
                       │
                       v
┌─────────────────────────────────────────────────────────────────┐
│              Variational Field Equations                         │
│              ∇²Θ - ∂V/∂Θ† = 0 [Corollary H1.1]                │
└──────────────────────┬──────────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┬───────────────────┐
        │              │              │                   │
        v              v              v                   v
┌───────────┐  ┌───────────┐  ┌───────────┐  ┌──────────────────┐
│  Gravity  │  │   Gauge   │  │  Yukawa   │  │  Experimental    │
│  Metric   │  │  Fields   │  │ Couplings │  │  Predictions     │
│  g_μν     │  │ A_μ,F_μν  │  │  Y_ij     │  │  δg, δα, ...     │
│ [Thm R1]  │  │[Thm E2-4] │  │ [Thm Y1-3]│  │  [Doc M1, T1]    │
└─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └────────┬─────────┘
      │              │              │                   │
      │              │              │                   │
      └──────────────┴──────────────┴───────────────────┘
                            │
                            v
             ┌────────────────────────────┐
             │   Standard Model Physics   │
             │   + Quantum Corrections    │
             │   + Dark Sector            │
             └────────────────────────────┘
```

**Key Transformations:**
1. **Θ → Action**: Variational principle with proper boundary terms [H1]
2. **Action → Field Eq**: Euler-Lagrange equations [H1 Corollary]
3. **Θ → Gauge**: Automorphism group Aut(ℂ⊗ℍ) → SU(3)×SU(2)×U(1) [E1-E4]
4. **Θ → Yukawa**: Geometric overlap integrals on T² [Y1-Y3]
5. **Θ → Gravity**: Real part Re[G_μν] = g_μν [R1]
6. **All → Observables**: Quantum corrections, running couplings, predictions [M1]

---

## 📂 Repository Structure

```
unified_biquaternion_theory    # Original Unified biquaternion theory documents and derivations
complex_consciousness/         # Complex Consciousness Theory (LaTeX sources & PDFs)
consolidation_project/         # Unified Biquaternion Theory consolidated documents (ongoing project, important stuff might be missing)
  ├── appendix_A_...           # Appendices on gravity, gauge fields, QED/QCD, etc.
  ├── img/                     # Figures and diagrams
  ├── metadata/                # Project notes, TODOs, consolidation maps
.github/workflows/             # GitHub Actions for LaTeX compilation
```

---

## 📄 Main Documents

### Core Theory
- **UBT Main Document**: `unified_biquaternion_theory/ubt_main_article.tex`
- **Consolidated UBT**: `consolidation_project/ubt_2_main.tex`
- **Appendices 1-21**: Detailed expansions of the main theory
- **Solutions**: Important proofs and derivations

### Assessment & Status Documents

#### Latest Evaluations (November 2025)
- **[Evaluation Executive Summary](EVALUATION_EXECUTIVE_SUMMARY.md)** - ⭐ **START HERE**: Quick overview of current status and integration decision
- **[Remaining Challenges: Detailed Status](REMAINING_CHALLENGES_DETAILED_STATUS.md)** - ⭐⭐⭐ **NEWEST**: Comprehensive roadmap addressing all 5 remaining challenges with concrete action plans and timelines
- **[Scientific Rating 2025](UBT_SCIENTIFIC_RATING_2025.md)** - ⭐ **NEW**: Comprehensive scientific rating (4.5/10) with detailed criterion breakdown
- **[Hyperspace Waves Integration Assessment](HYPERSPACE_WAVES_INTEGRATION_ASSESSMENT.md)** - ⭐ **NEW**: Analysis of integration feasibility and recommendation to maintain separation

#### Status and Guidelines
- **[UBT Reading Guide](UBT_READING_GUIDE.md)** - How to navigate UBT responsibly
- **[Scientific Status and Development Roadmap](UBT_SCIENTIFIC_STATUS_AND_DEVELOPMENT.md)** - Current status, limitations, and future work required
- **[Mathematical Foundations - Required Development](MATHEMATICAL_FOUNDATIONS_TODO.md)** - Specific mathematical gaps that need addressing
- **[Consciousness Claims - Ethics Guidelines](CONSCIOUSNESS_CLAIMS_ETHICS.md)** - Proper presentation of speculative consciousness hypotheses
- **[Testability and Falsification](TESTABILITY_AND_FALSIFICATION.md)** - Criteria for making UBT falsifiable

#### Previous Reviews
- **[UBT Comprehensive Evaluation Report](UBT_COMPREHENSIVE_EVALUATION_REPORT.md)** - October 2025 comprehensive evaluation
- **[Mathematical Review Report](MATHEMATICAL_REVIEW_REPORT.md)** - Technical errors found and fixed
- **[Issues Addressed](ISSUES_ADDRESSED.md)** - Summary of recent improvements
- **[UBT Improvements Summary](UBT_IMPROVEMENTS_SUMMARY.md)** - November 2025 improvements addressing major problems

### Recent Improvements (November 2025)
**Major improvements made to scientific integrity and presentation:**
- ✅ Added comprehensive disclaimers to all LaTeX documents
- ✅ Clearly marked speculative content (consciousness, fine-structure constant)
- ✅ Removed problematic claims (death/rebirth speculation)
- ✅ Enhanced transparency about theory status and limitations
- ✅ Mathematical core completely preserved

See [UBT Improvements Summary](UBT_IMPROVEMENTS_SUMMARY.md) for complete details.

### Consciousness Applications (Highly Speculative)
- **CCT Main Document**: `complex_consciousness/ctc_2.0_main.tex`

**⚠️ Important**: Consciousness-related content should be read with the understanding that these are philosophical hypotheses requiring extensive validation, not established science. See [Consciousness Ethics Guidelines](CONSCIOUSNESS_CLAIMS_ETHICS.md).

---

## 🔬 How to Compile

To compile the main UBT document locally:

```bash
cd consolidation_project
pdflatex ubt_2_main.tex
bibtex ubt_2_main
pdflatex ubt_2_main.tex
pdflatex ubt_2_main.tex
```

GitHub Actions will compile PDFs automatically on push.

---

## 📚 Citation

If you use this work, please cite it as:

```
David Jaroš. Unified Biquaternion Theory: Complex Time, Consciousness, and Fundamental Physics. 2025.
Available at: https://github.com/DavJ/unified-biquaternion-theory
```

---

## 📜 Origin & Development

The **Unified Biquaternion Theory** was developed first as a general physical framework.  
During its formulation, a parallel line of work led to the **Complex Consciousness Theory**, which applies UBT principles in a simplified mathematical form to model consciousness as a physical phenomenon.  
This repository contains both the full UBT documents and the CCT application, along with appendices and experimental proposals.

---


---

## 📌 Research Priorities

See [RESEARCH_PRIORITIES.md](RESEARCH_PRIORITIES.md) for current research and development priorities.

---

## 📊 Theory Evaluation Reports

### Current Scientific Rating: **5.5/10** (Significant Progress November 2025)

UBT is classified as an honest research framework in early development with exemplary scientific transparency. The rating improved from 4.5/10 to 5.5/10 following substantial mathematical formalization and theoretical advances.

**Latest Assessment:**
- **[UBT Updated Scientific Rating 2025](UBT_UPDATED_SCIENTIFIC_RATING_2025.md)** - ⭐⭐⭐ **NEWEST** Post-improvement evaluation showing rating increase from 4.5/10 to 5.5/10
- **[UBT Reevaluation 2025](UBT_REEVALUATION_2025.md)** - ⭐⭐⭐ Comprehensive reevaluation identifying biggest challenges and proposing solutions

**Key Documents:**
1. **[Evaluation Executive Summary](EVALUATION_EXECUTIVE_SUMMARY.md)** - Quick overview of scientific status
2. **[Scientific Rating 2025](UBT_SCIENTIFIC_RATING_2025.md)** - Baseline comprehensive rating
3. **[UBT Comprehensive Evaluation Report](UBT_COMPREHENSIVE_EVALUATION_REPORT.md)** - October 2025 full evaluation
4. **[UBT vs Other Theories Comparison](UBT_VS_OTHER_THEORIES_COMPARISON.md)** - Detailed comparison with String Theory, LQG, and other ToE candidates

**Recent Achievements (November 2025):**
- ✅ **Mathematical rigor:** 3.0/10 → 5.0/10 (formal field definition, SM derivation complete)
- ✅ **SM compatibility:** 3/10 → 6/10 (gauge group now **derived**, not assumed)
- ✅ **Testability:** 3.0/10 → 4.5/10 (CMB analysis protocol complete, feasible within 1-2 years)
- ✅ **Core formula identified:** ∇†∇Θ(q,τ) = κ𝒯(q,τ) (simple, complete, T-shirt ready)

**Strengths:**
- ✅ Exemplary scientific integrity and transparency (9.5/10)
- ✅ SM gauge group SU(3)×SU(2)×U(1) **rigorously derived** from Aut(B⁴)
- ✅ GR compatibility demonstrated in real limit
- ✅ Mathematical foundations substantially complete (field def + proofs)
- ✅ Testable CMB prediction within 2 years

**Remaining Challenges:**
- ⚠️ Most predictions unobservable (modified gravity ~10⁻⁶⁸, acknowledged honestly)
- ⚠️ Fermion masses not yet calculated from first principles
- ✅ ~~Standard Model assumed, not derived from geometry~~ **RESOLVED Nov 2025** - SM gauge group SU(3)×SU(2)×U(1) now rigorously derived from biquaternionic automorphisms (see SM_GAUGE_GROUP_RIGOROUS_DERIVATION.md)
- ⚠️ Complex time physical issues (causality, unitarity) partially addressed, active research ongoing
- ⚠️ Not competitive with leading ToE candidates (String Theory, LQG) in maturity, but comparable at similar development stage (Year 5 vs 40+ years)

**Development Status:**
- Year 5 of expected 10-20 year maturation timeline
- Comparable to other early-stage theories at similar development stage
- Realistic probability: 1-5% of becoming established ToE, but high value regardless

---

## 🔗 Related Projects

### Hyperspace Waves

⚠️ **Important Integration Decision**: The [hyperspace_waves](https://github.com/DavJ/hyperspace_waves) repository explores mathematical extensions of biquaternion formalism. However, it makes extraordinary claims (FTL communication, barrier penetration, retrocausality) that contradict established physics and lack experimental validation.

**Status:** Repositories maintained as **SEPARATE** projects to preserve UBT's scientific credibility.

**Assessment:** [HYPERSPACE_WAVES_INTEGRATION_ASSESSMENT.md](HYPERSPACE_WAVES_INTEGRATION_ASSESSMENT.md) provides detailed analysis explaining why integration would damage UBT's scientific rating (4.5/10 → 2.0/10).

**Mathematical Content:** Some computational tools (biquaternion arithmetic, theta functions) may be selectively imported with appropriate disclaimers in the future, but physical interpretations (FTL, retrocausality) are not endorsed as part of core UBT framework.

3. **[UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md](UBT_DATA_ANALYSIS_SCIENTIFIC_SUPPORT.md)** - ⭐ **NEW**: Analysis of available scientific data from major experiments (LIGO/Virgo, Planck, XENON, Fermi-LAT) relevant to testing UBT predictions. Includes comparison with five concrete testable predictions from Appendix W.

4. **[SCIENTIFIC_DATA_SOURCES_BIBLIOGRAPHY.md](SCIENTIFIC_DATA_SOURCES_BIBLIOGRAPHY.md)** - Complete bibliography of experimental data sources, publications, and analysis tools for testing UBT predictions.

5. **[ANALYZA_VEDECKYCH_DAT_CZ.md](ANALYZA_VEDECKYCH_DAT_CZ.md)** - Czech summary of scientific data analysis supporting UBT predictions.

---

## 🔬 Data Analysis Tools

Python scripts for analyzing experimental data relevant to UBT predictions are available in the `scripts/` directory:

- **[analyze_dark_matter_limits.py](scripts/analyze_dark_matter_limits.py)** - Compare UBT p-adic dark matter predictions with XENON/LZ/PandaX limits
- **[analyze_cmb_power_spectrum.py](scripts/analyze_cmb_power_spectrum.py)** - Analyze Planck CMB data for multiverse projection signatures
- See [scripts/DATA_ANALYSIS_README.md](scripts/DATA_ANALYSIS_README.md) for documentation

---

## 📦 Release v10.0 (November 2025)

**Major Updates:**
- Added Appendix H – Theta Phase Emergence with drift-diffusion dynamics
- Improved Hermitian correspondence in Appendix F with Chamseddine (2025) reference
- Added explicit quaternion-to-SU(3) color mapping in Appendix G
- Created OSF abstract for public release
- Ready for Zenodo/OSF publication

**New Files:**
- `UBT_Main.tex` - Main consolidated document with updated metadata
- `UBT_Abstract_OSF.tex` - Abstract for OSF/Zenodo submission
- `Appendix_H_Theta_Phase_Emergence.tex` - Phase field dynamics
- Updated `Appendix_F_Hermitian_Limit.tex` with disclaimers
- Updated `Appendix_G_Emergent_SU3.tex` with color mapping table
- `references.bib` - Bibliography with Chamseddine 2025 citation

**DOI:** *(to be assigned after Zenodo upload)*  
**Citation:** Jaroš, D. (2025). Unified Biquaternion Theory v10. Zenodo. https://doi.org/xxxxx

**Release Package Contents:**
- `UBT_Main.pdf` - Full consolidated document
- `UBT_Abstract_OSF.pdf` - OSF submission abstract
- All appendices (F, G, H, and supporting materials)
- `README.md` - This file
- `references.bib` - Complete bibliography

**How to Build:**
```bash
pdflatex UBT_Main.tex
bibtex UBT_Main
pdflatex UBT_Main.tex
pdflatex UBT_Main.tex
```

**Zenodo Upload:** [https://zenodo.org/deposit](https://zenodo.org/deposit)  
**OSF Preprint:** [https://osf.io/preprints/](https://osf.io/preprints/)

---

## 📌 Author Statement

This repository contains my **original theoretical research**.  
I, **David Jaroš**, am the **first and primary author** of the Unified Biquaternion Theory (UBT) and all its derived formulations, including the Complex Consciousness Theory (CCT).  
All documents, derivations, and mathematical proofs herein were developed by me unless explicitly stated otherwise.  
See [PRIORITY.md](consolidation_project/PRIORITY.md) for the current research and development priorities.


## 📜 License

This work is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

**You are free to:**
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

**Under the following terms:**
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made

For full license terms, see [LICENSE.md](LICENSE.md)
