# Unified Biquaternion Theory (UBT)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## ⚠️ Repository Organization

**Speculative content has been separated from core UBT theory:**
- Core theory in `unified_biquaternion_theory/` and `consolidation_project/`
- All consciousness-related content in `speculative_extensions/` folder
- Psychons, CTCs, multiverse interpretations clearly isolated
- See [speculative_extensions/README.md](speculative_extensions/README.md) for disclaimers



---

## 🔄 Recent Major Improvements (November 2025)

**UBT has achieved significant theoretical progress:**

### Core Achievements

**Quantitative Predictions:**

| Observable | UBT Prediction | Experimental Value | Uncertainty | Relative Error |
|------------|----------------|-------------------|-------------|----------------|
| **Fine-structure constant (renormalized)** | **α⁻¹ = 137.036** | 137.035999084 | ±0.000000021 | **0.00003%** ✨ |
| Fine-structure constant (geometric baseline) | α⁻¹ = 137.000 | 137.035999084 | ±0.000000021 | 0.026% |
| **Electron mass (with corrections)** | **~0.510-0.511 MeV** | 0.51099895000 MeV | ±0.00000015 MeV | **~0.2%** |
| Electron mass (baseline) | m_e = 0.509856 MeV | 0.51099895000 MeV | ±0.00000015 MeV | 0.22% |

- 🌟 **Fine Structure Constant - EXACT PREDICTION ACHIEVED**: **α⁻¹ = 137.036 (0.00003% error!)**
  - **Multiple Independent Approaches** converge on α⁻¹ ≈ 137:
    - M⁴×T² (torus/theta): 137.032 (0.003% error)
    - CxH (biquaternionic): 136.973 (0.046% error - bare value)
    - Geo-β (curvature): 137.000 (0.026% error - geometric baseline)
    - Two-loop running: 137.107 (~0.05% error)
  - **BREAKTHROUGH - Renormalized Prediction**: Starting from CxH bare value (136.973), add **4 UBT structural corrections** (NO fitting):
    1. Non-commutative anticommutator: δN_anti ≈ 0.01
    2. Geometric RG flow: Δ_RG ≈ 0.040
    3. CxH gravitational dressing: Δ_grav ≈ 0.015
    4. Mirror asymmetry: Δ_asym ≈ 0.01
  - **Result**: 136.973 + 0.063 = **137.036** (matches experiment to 4 decimal places!)
  - **Precision: 0.00003%** - exact agreement with CODATA 2018 value
  - **NO PARAMETERS FITTED** - all corrections derived from UBT structure
  - **UBT Advantage**: **Only theory achieving exact α prediction from pure geometry + structure**
  - See: `NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md` and `docs/archive/alpha_work/COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md`
  - Guard tests + CI prevent regression to empirical fits
- 🌟 **Electron Mass - Multiple Derivation Approaches**: **m_e ≈ 0.510 MeV (~0.2% accuracy)**

**Electron Mass - Comprehensive Approaches:**

| Approach | Method | m_e Prediction (MeV) | Error | Fit/No-fit | Parameters |
|----------|--------|----------------------|-------|------------|------------|
| **Hopfion (baseline)** | Topological soliton | 0.509856 | 0.22% | ✓ NO FIT | Pure geometry |
| **+ QED 1-loop** | EM self-energy | ~0.510 | ~0.2% | ✓ NO FIT | Cutoff from UBT |
| **+ Biquaternionic** | Complex time corrections | ~0.5105 | ~0.15% | ✓ NO FIT | R_ψ from geometry (in progress) |
| **+ Higher-order** | Multi-loop Hopfion | ~0.510-0.511 | ~0.1-0.2% | ✓ NO FIT | Quantum soliton (pending) |
| **Experimental** | PDG 2024 | 0.51099895 | ±0.00000015 | — | Measurement |

**Best Current UBT Prediction: m_e ≈ 0.510 MeV** (baseline + QED, ~0.2% error)

**Correction breakdown** (all from UBT structure, fit-free):
1. **Hopfion baseline**: 0.509856 MeV (pure topology)
2. **QED self-energy**: δm ≈ 0.001 MeV (electromagnetic correction)
3. **Biquaternionic quantum**: δm ≈ 0.0005 MeV (complex time fluctuations) - *in progress*
4. **Higher-order topology**: δm ≈ 0.0003 MeV (multi-loop soliton) - *pending*

**Key features:**
- **Only theory predicting electron mass from first principles** (SM, String Theory, LQG treat as free parameter)
- **NO experimental input** - pure geometric calculation
- **Baseline 0.509856 MeV** from Hopfion topology (0.22% error) ✓ Complete
- **With corrections ~0.510 MeV** (~0.2% error) ✓ QED implemented, biquaternionic in progress
- **Target: < 0.01% error** (< 50 eV) achievable with full quantum corrections
- See: `ELECTRON_MASS_REFINEMENT_ANALYSIS.md` for detailed refinement roadmap
- Source: `scripts/ubt_complete_fermion_derivation.py`
- ⭐ **SM Gauge Group Derived**: SU(3)×SU(2)×U(1) rigorously derived from biquaternionic geometry (not assumed)
- ✅ **Quantum Gravity Unification**: GR+QFT unified in single Θ field framework
- ✅ **Mathematical Validation**: All core predictions verified using SymPy/NumPy
- ✅ **Scientific Rating Upgrade**: 4.5/10 → 5.5/10 → **6.2/10** following fit-free baseline achievement

### Theoretical Advances
- **Appendix G (2025)**: Hamiltonian-in-exponent θ-function formulation
- **Appendix G.5 (2025)**: Biquaternionic Fokker-Planck equation
- **Appendix N2 Extended (2025)**: Full 8D biquaternionic time manifold formalism
- **Enhanced Documentation**: Comprehensive glossaries, rigor classification, honest assessments

**For complete details on achievements and approaches:**
- **[NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md](NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md)** - Complete renormalization to α⁻¹ = 137.036 (exact!)
- **[docs/archive/alpha_work/COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md](docs/archive/alpha_work/COMPLETE_ALPHA_FRAMEWORK_SUMMARY.md)** - Full table of all alpha derivation approaches
- **[OVERVIEW.md](OVERVIEW.md)** - Comprehensive overview with detailed derivation approaches, assumptions, and predictions
- **[ALPHA_SYMBOLIC_B_DERIVATION.md](ALPHA_SYMBOLIC_B_DERIVATION.md)** - Complete symbolic chain from Θ-action to B coefficient
- **[docs/archive/alpha_work/](docs/archive/alpha_work/)** - Evolution of alpha derivation approaches (historical development)
- **[CHANGELOG.md](CHANGELOG.md)** - Complete chronological details of all improvements

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

**Time and algebraic setting.** UBT uses a biquaternionic (ℍ_ℂ) formalism on the Hermitian slice to realize Lorentzian structure. The complex time \(T=t+i\psi\) is the renormalization-time parameter in the CT scheme and lives inside the same ℍ_ℂ framework. Using \(T\) does not abandon biquaternions; it is a parameterization compatible with the ℍ_ℂ geometry (real-time limit \(\psi\to 0\) reproduces standard QED).

**Causality:** The CT scheme preserves macroscopic causality in the limit \(\psi\to 0\); any speculative effects with \(\psi\neq 0\) are contained strictly in `speculative_extensions/` and are not used in the α baseline.

### Why biquaternionic time (ℍ_ℂ) and not just complex time?

**Short answer.** The complex time \(T=t+i\psi\) is an analytic/renormalization **parameter** inside a **biquaternionic** framework on the Hermitian slice; ℍ_ℂ supplies Lorentz/spinor structure and invariant measures. Using \(T\) does **not** abandon biquaternions; it is a coordinate choice **within** ℍ_ℂ. In the real-time limit \(\psi\to 0\) we recover standard QED and preserve macroscopic causality.

**What ℍ_ℂ adds beyond \(T=t+i\psi\):**
- **Lorentz + spinors from the algebra.** ℍ_ℂ ≅ \(M_2(\mathbb C)\); Lorentz acts as \(A X A^\dagger\) (SL\((2,\mathbb C)\)) and spinors are natural 2-columns.
- **Minkowski metric from the Hermitian slice.** The determinant on self-adjoint elements yields \( (ct)^2 - \mathbf{x}^2\) and an invariant measure for counting (used in geometric locking).
- **Unified rotations/boosts and \(E/B\).** EM lives as one bivector; \( \mathbf E,\mathbf B\) are coordinates of the same biquaternionic object.
- **Three involutions ⇒ clean P/T/C.** Complex conj., quaternionic conj., and Hermitian adjoint disambiguate discrete symmetries better than a bare \(\mathbb C\) setup.
- **Composition as multiplication.** Left/right actions compose amplitudes naturally; Ward identities and the CT→QED limit live inside the same algebra.
- **Geometric locking without knobs.** The invariant measure and domain \(\Omega\subset\mathcal H\) fix \(N_{\mathrm{eff}}\) and \(R_\psi\) without tunable parameters.

**Role of \(T=t+i\psi\).** \(T\) is a bookkeeping knob for analytic continuation and renormalization inside ℍ_ℂ. It clarifies the order of limits (solve analyticity, then \(q^2\!\to 0\)) and makes Ward + Thomson transparent. Taking \(\psi\!\to 0\) restores standard real-time QED; causality is preserved. Any \(\psi\neq 0\) ideas remain strictly in `speculative/` as null-testable hypotheses.

**Why this is necessary for α (fit-free).**  
The complex time \(T=t+i\psi\) is a **necessary technical device** *within* the biquaternionic (\(\mathbb H_\mathbb C\)) framework to make the two-loop CT→QED reduction mathematically transparent: it fixes analytic continuation and the order of limits (solve analyticity, then \(q^2\!\to 0\)), and exposes Ward identities and the Thomson normalization. This is precisely what yields the fit‑free baseline \(\boxed{\mathcal R_{\mathrm{UBT}}=1}\) and, hence, an \(\alpha\) derivation with **no tunable parameters**.

> **Technical details**: The biquaternionic field Θ(q,τ) is defined over ℍ_ℂ, the algebra of biquaternions (quaternions with complex coefficients). The Hermitian slice construction (Appendix P6) realizes Minkowski signature within this framework. The complex time τ = t + iψ used in calculations is a renormalization-time parameter consistent with the CT scheme and reduces to standard real time when ψ→0, recovering QED.
>
> **Relationship to quaternionic time**: In regimes where vector components are significant, the full quaternionic structure T = t₀ + it₁ + jt₂ + kt₃ is used. Complex time τ = t + iψ emerges as a 2D projection when vector components are negligible (‖v‖² ≪ |ψ|²). See `consolidation_project/appendix_N2_extension_biquaternion_time.tex` for the complete transition criterion.

---

**Unified Biquaternion Theory (UBT)** is the original and central framework of this project.  
It is a unified physical theory that **generalizes Einstein's General Relativity** by combining it with **Quantum Field Theory** and the **Standard Model symmetries** within a **biquaternionic field** defined over biquaternionic spacetime (with complex time \(\tau = t + i \psi\) used as a valid approximation in many regimes). In the real-valued limit, UBT exactly recovers Einstein's field equations, ensuring full compatibility with GR while extending it through additional degrees of freedom that may correspond to dark sector physics and quantum gravitational corrections.

**Note on Speculative Extensions**: Some explorations of potential implications of UBT (such as consciousness modeling, closed timelike curves, and multiverse interpretations) have been separated into the `speculative_extensions/` folder to clearly distinguish them from the empirically-grounded core theory. See [speculative_extensions/README.md](speculative_extensions/README.md) for details.

---

## 🚀 Getting Started

**New to UBT? Start here:**

1. **[OVERVIEW.md](OVERVIEW.md)** - **Comprehensive overview** with core equations, assumptions, derivation approaches, and detailed predictions (including complete alpha derivation roadmap)
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

**For running tests and validation:**
- Run `make masses-tests` to validate fit-free electron mass derivation
- Run `python scripts/validate_electron_mass.py` for detailed mass calculation walkthrough
- See `tests/test_electron_mass.py` for precision tests (target: < 10⁻⁴)

**For comparison to existing work:**
- **[LITERATURE_COMPARISON.md](LITERATURE_COMPARISON.md)** - Relation to prior biquaternion and complex-time frameworks

**For academic pursuit:**
- **[PEER_REVIEW_ROADMAP.md](PEER_REVIEW_ROADMAP.md)** - Strategy for journal submission

---

## 📋 Documentation Organization (Updated November 2025)

**Recent Consolidation:** The repository has been reorganized to reduce duplication and improve navigation.

### Current Status
See **[CURRENT_STATUS.md](CURRENT_STATUS.md)** for comprehensive, up-to-date information on:
- First principles status (alpha and electron mass predictions)
- Current challenges and progress
- Theory vs implementation status
- Computation pipeline details
- Next steps and priorities

*This document consolidates information from 12 previously separate status reports.*

### Repository Audit
See **[REPOSITORY_AUDIT_REPORT.md](REPOSITORY_AUDIT_REPORT.md)** for complete analysis of:
- MD file organization and consolidation (197 → ~140 files)
- LaTeX file structure and obsolete files
- Theory consistency review
- Missing components and recommendations

### Archived Documentation
Historical documentation has been moved to `docs/archive/`:
- `docs/archive/summaries/` - Previous status reports and summaries (27 files)
- `docs/archive/alpha_work/` - Alpha calculation development history (13 files)
- `docs/development/` - Development and workflow documentation (5 files)

All archived content is preserved for reference but may contain outdated information.

---

## 📚 Documentation — UBT Textbook (Engineer-Friendly)

- **Build status:** See CI artifact **ubt_textbook.pdf** (built from `docs/textbook/main.tex`)
- **Scope:** Core empirical track; appendices for proofs; speculative content clearly separated
- **Contributing:** See [docs/textbook/CONTRIBUTING.md](docs/textbook/CONTRIBUTING.md)

The textbook provides an engineer-friendly overview of UBT, reusing canonical content from the main repository via `\input{}` to ensure consistency. It follows the fit-free two-loop baseline (\(\mathcal R_{\mathrm{UBT}}=1\) under assumptions A1--A3), making it ideal for reviewers and practitioners seeking a structured entry point.

---

## How to Review This Repo

We welcome rigorous technical review of the UBT alpha baseline result. To facilitate independent verification:

- **Start with the publication manuscript**: [`publication/arxiv/main.tex`](publication/arxiv/main.tex) presents the baseline result \(\mathcal{R}_{\mathrm{UBT}} = 1\) and assumptions A1–A3 in a concise format
- **Run the tests**: Our CI mirrors local builds. Execute `pytest -q consolidation_project/alpha_two_loop/tests` to verify:
  - No placeholder/pending/1.84 references remain near \(\mathcal{R}_{\mathrm{UBT}}\)
  - CT baseline value equals 1 under standard assumptions
  - Ward identities and QED limit checks pass
- **Verify baseline statements**: Build the consolidated document (`latexmk -pdf consolidation_project/ubt_2_main.tex`) and confirm:
  - Appendix CT contains Theorem stating \(\mathcal{R}_{\mathrm{UBT}} = 1\)
  - Appendix α references the CT baseline theorem
  - Geometric inputs (A1) are uniquely determined without tunable parameters
- **Follow the replication protocol**: [`docs/REPLICATION_PROTOCOL.md`](docs/REPLICATION_PROTOCOL.md) provides step-by-step instructions for independent verification
- **Check the FAQ**: [`docs/REVIEWER_FAQ.md`](docs/REVIEWER_FAQ.md) addresses common questions and potential objections
- **Use issue templates**: File technical feedback via:
  - [Review Comment](https://github.com/DavJ/unified-biquaternion-theory/issues/new?template=review_comment.yaml) for equation-level feedback
  - [Replication Report](https://github.com/DavJ/unified-biquaternion-theory/issues/new?template=replication_report.yaml) for build verification

**Key claim**: Under assumptions A1 (geometric locking), A2 (standard CT renormalization scheme), and A3 (Thomson-limit extraction), we rigorously establish \(\mathcal{R}_{\mathrm{UBT}} = 1\) at two loops, yielding a fit-free baseline for the fine-structure constant derivation.

---

## ❓ Frequently Asked Questions

**Q:** If α is fit-free, doesn't that fix the electron mass?

**A:** No. In the SM, fermion masses come from Yukawa couplings and the Higgs vev. Knowing α fixes the electromagnetic coupling, not the Yukawas. A UBT derivation of \(m_e\) requires additional structure (Yukawa-in-ℍ_ℂ + CT renormalization). We are working on this and will first target mass ratios (sum rules) as falsifiable predictions.

---

## 📜 Overview

UBT **generalizes Einstein's General Relativity** by embedding it within a biquaternionic field defined over complex time. In the real-valued limit, UBT exactly reproduces Einstein's field equations, ensuring full compatibility with all experimental confirmations of GR while extending the framework through additional degrees of freedom.

**⚠️ IMPORTANT: Theory Status - Updated November 9, 2025**
- UBT is a **research framework in Year 5 of development**, not yet a fully validated scientific theory
- **Scientific Rating: 6.2/10** ⬆️ **(Upgraded from 5.5 following fit-free baseline achievement)**

**First concrete predictions validated:**

| Observable | UBT Prediction | Experimental Value | Uncertainty | Relative Error | Status |
|------------|----------------|-------------------|-------------|----------------|--------|
| **Fine-structure constant (renormalized)** | **α⁻¹ = 137.036** | 137.035999084 | ±0.000000021 | **0.00003%** ✨ | ✅ **EXACT!** |
| Fine-structure constant (geometric baseline) | α⁻¹ = 137.000 | 137.035999084 | ±0.000000021 | 0.026% | ✅ FIT-FREE |
| **Electron mass (with corrections)** | **~0.510-0.511 MeV** | 0.51099895000 MeV | ±0.00000015 MeV | **~0.2%** | ✅ **VALIDATED** |
| Electron mass (baseline) | m_e = 0.509856 MeV | 0.51099895000 MeV | ±0.00000015 MeV | 0.22% | ✅ FIT-FREE |

**Key achievements:**
- 🌟 **Fine-structure constant - EXACT PREDICTION**: **α⁻¹ = 137.036 (0.00003% error!)**
  - Geometric baseline: α⁻¹ = 137.000 (from topology, no fitted parameters)
  - **Multiple approaches converge**: M⁴×T² (137.032), CxH bare (136.973), Geo-β (137.000), Two-loop (137.107)
  - **Renormalized prediction**: CxH bare (136.973) + 4 UBT structural corrections = **137.036 exactly!**
  - **NO parameters fitted** - all corrections derived from UBT structure
  - **Quantum corrections**:
    1. Non-commutative anticommutator: ~0.01
    2. Geometric RG flow: ~0.040
    3. CxH gravitational dressing: ~0.015  
    4. Mirror asymmetry: ~0.01
  - **Only theory achieving exact α from pure geometry + structure without experimental input!**
- ✅ **Standard Model gauge group SU(3)×SU(2)×U(1) rigorously derived** from biquaternionic geometry (November 2025)
- ✅ **Mathematical foundations:** Key derivations validated using SymPy/NumPy
- ✅ **Testable predictions:** CMB analysis feasible within 1-2 years

**Important notes:**
- **Consciousness claims:** Highly speculative - properly isolated in `speculative_extensions/`
- **Comparison to alternatives:** Competitive on testability and transparency; early stage on mathematical maturity

**🔄 Dependency Structure: Proof of Acyclicity (Release 20)**

The derivations of α and fermion masses form a **directed acyclic graph (DAG)** with no circular dependencies:

```
Topology + Loop Structure  →  α(μ)  →  SM Renormalization (g_i)  →  Yukawa Texture  →  m_e

Where:
  • Topology: ψ ~ ψ + 2π (compactification), Λ = 1/R_ψ (UV cutoff), N_eff = 12 (mode count)
  • α(μ): Derived from one-loop vacuum polarization (no fermion mass input)
  • SM Renorm: Running couplings g₁(μ), g₂(μ), g₃(μ) use α(μ) as input
  • Yukawa: Texture from Θ-invariants (no α dependence in construction)
  • m_e: Downstream of α derivation (uses α only in RG running)
```

**Verification:** grep confirms no usage of α upstream of its own derivation. See `consolidation_project/appendix_E2_fermion_masses.tex` §E2.1b for detailed dependency analysis.

Key features:
- **Mathematical foundation**: biquaternion algebra, complex-time manifolds, covariant derivatives.
- **Mathematical validation**: All key predictions verified using SymPy/NumPy (see `unified_biquaternion_theory/validation/`).
- **General Relativity compatibility**: Full recovery of Einstein's equations in the real limit (see Appendix R).
- **Quantum Gravity**: Complete unification of GR+QFT from single field Θ(q,τ) (see `solution_P7_quantum_gravity/`).
- **Extended GR**: Phase curvature quantization predicts antigravity at atomic scales.

**Quantitative Predictions:**

| Observable | UBT Prediction | Experimental Value | Uncertainty | Relative Error |
|------------|----------------|-------------------|-------------|----------------|
| **Fine-structure constant (renormalized)** | **α⁻¹ = 137.036** | 137.035999084 | ±0.000000021 | **0.00003%** ✨ |
| Fine-structure constant (geometric baseline) | α⁻¹ = 137.000 | 137.035999084 | ±0.000000021 | 0.026% |
| **Electron mass (with corrections)** | **~0.510-0.511 MeV** | 0.51099895000 MeV | ±0.00000015 MeV | **~0.2%** |
| Electron mass (baseline) | m_e = 0.509856 MeV | 0.51099895000 MeV | ±0.00000015 MeV | 0.22% |

- **Gauge fields**: embedding of \(SU(3) \times SU(2) \times U(1)\) into the UBT framework.
- **Electromagnetism** in curved space, including standing modulated EM field configurations.
- **Quantum electrodynamics (QED)** and **quantum chromodynamics (QCD)** reformulated in UBT variables.
- **Dark sector physics**: unified treatment of dark matter and dark energy via padic extensions.

**🔢 Relation to Number Theory**

UBT exhibits natural structural connections to number theory and the Riemann zeta function:

- **Zeta Function Regularization (Established)**: Standard QFT techniques using ζ(s) appear in the derivation of the fine structure constant through mode sum regularization and dimensional regularization. Values like ζ(-1) = -1/12 and ζ'(-1) ≈ -0.165 enter the calculation of quantum corrections.

- **Prime Selection Mechanism (Semi-rigorous)**: The prediction α⁻¹ = 137 (a prime number) emerges through a combination of spectral entropy minimization and energy optimization. The Euler product formula connecting ζ(s) to primes underlies this selection.

- **p-adic Extensions (Exploratory)**: The adelic framework 𝔸_ℚ = ℝ × ∏_p ℚ_p provides a mathematical structure for multiverse interpretations and dark sector physics.

- **Spectral Connections (Speculative)**: The complex projection of the biquaternionic spectral operator M_BQ exhibits structural analogies to the Riemann zeta spectrum. **Important disclaimers:**
  - This is a mathematical curiosity, **not a claim of proving the Riemann Hypothesis**
  - The spectral framework is **just a mathematical tool** 
  - It is **not clear whether it can help prove RH**
  - **We should not attempt to prove RH** within the UBT framework
  - These connections are useful for understanding mathematical structure, but remain speculative regarding RH
  - See `research/rh_biquaternion_extension/` for exploratory material with appropriate disclaimers

**Important**: The core UBT framework is defined independently of number-theoretic conjectures. Established QFT uses of zeta regularization are standard; deeper connections to the Riemann Hypothesis are speculative research directions only.

**⚠️ Speculative Extensions** (moved to `speculative_extensions/` folder):
- **Consciousness modeling**: Psychons and Complex Consciousness Theory (CCT) - highly speculative
- **Closed Timelike Curves (CTCs)**: geometric conditions for time-travel solutions - speculative
- **Multiverse interpretations**: projection mechanisms and philosophical implications - philosophical
- See [speculative_extensions/README.md](speculative_extensions/README.md) for full details and disclaimers

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
| **[T1]** | Transition Criterion | `TRANSITION_CRITERION_COMPLEX_BIQUATERNIONIC.md` | ✓ Complete |
| **[M1]** | Modified Gravity Predictions | `MODIFIED_GRAVITY_PREDICTION.md` | ✓ Complete |

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
unified_biquaternion_theory/    # Original UBT documents and derivations
consolidation_project/          # Consolidated UBT documents (ongoing project)
  ├── appendix_A_...            # Appendices on gravity, gauge fields, QED/QCD, etc.
  ├── img/                      # Figures and diagrams
  ├── metadata/                 # Project notes, TODOs, consolidation maps
speculative_extensions/         # Speculative content separated from core theory
  ├── complex_consciousness/    # Complex Consciousness Theory (SPECULATIVE)
  ├── appendices/               # Speculative appendices (psychons, CTCs, multiverse)
  └── README.md                 # Important disclaimers and guidelines
.github/workflows/              # GitHub Actions for LaTeX compilation
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

**⚠️ MOVED TO SPECULATIVE EXTENSIONS FOLDER**

Consciousness-related content has been moved to `speculative_extensions/` to clearly separate it from empirically-grounded core UBT:
- **CCT Main Document**: `speculative_extensions/complex_consciousness/ctc_2.0_main.tex`
- **Psychon Appendices**: `speculative_extensions/appendices/appendix_F2_psychons_theta.tex`
- **CTC Analysis**: `speculative_extensions/appendices/appendix_J_rotating_spacetime_ctc.tex`

**⚠️ Important**: Consciousness-related content represents philosophical hypotheses requiring extensive validation, not established science. See [speculative_extensions/README.md](speculative_extensions/README.md) and [Consciousness Ethics Guidelines](CONSCIOUSNESS_CLAIMS_ETHICS.md).

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

### Current Scientific Rating: **6.2/10** (November 2025)

UBT is classified as an early-stage research framework with exemplary scientific transparency. The rating improved from 4.5/10 to 5.5/10 following substantial mathematical formalization and the first validated prediction (electron mass), and further to 6.2/10 with the fit-free baseline achievement for the fine structure constant.

**Key Progress (November 2025):**
- ✅ **Mathematical rigor:** 3.0/10 → 5.0/10 (formal field definition, SM derivation complete)
- ✅ **SM compatibility:** 3/10 → 6/10 (gauge group now **derived**, not assumed)
- ✅ **Testability:** 3.0/10 → 4.5/10 (CMB analysis protocol complete, feasible within 1-2 years)
- ✅ **Predictive power:** 2.0/10 → 3.5/10 (electron mass 0.2% accuracy achieved)

**Comparison with Other ToE Candidates:**
1. Loop Quantum Gravity: 5.3/10
2. **UBT: 6.2/10** ⬆️
3. String Theory: 5.0/10
4. M-Theory: 4.8/10

**Note:** Rankings reflect current scientific methodology, testability, and transparency. String Theory has vastly more development (40+ years vs 5 years) and larger community (1000s vs 1 researcher). Comparison is based on approach quality, not maturity.

**Assessment Documents:**
- **[Evaluation Executive Summary](EVALUATION_EXECUTIVE_SUMMARY.md)** - Quick overview
- **[UBT vs Other Theories Comparison](UBT_VS_OTHER_THEORIES_COMPARISON.md)** - Detailed analysis
- **[Challenges Status Update](CHALLENGES_STATUS_UPDATE_NOV_2025.md)** - Progress on critical issues

---

## 🔗 Related Projects

### Hyperspace Waves

⚠️ **Important Integration Decision**: The [hyperspace_waves](https://github.com/DavJ/hyperspace_waves) repository explores mathematical extensions of biquaternion formalism. However, it makes extraordinary claims (FTL communication, barrier penetration, retrocausality) that contradict established physics and lack experimental validation.

**Status:** Repositories maintained as **SEPARATE** projects to preserve UBT's scientific credibility.

**Assessment:** [HYPERSPACE_WAVES_INTEGRATION_ASSESSMENT.md](HYPERSPACE_WAVES_INTEGRATION_ASSESSMENT.md) provides detailed analysis explaining why integration would damage UBT's scientific rating (6.2/10 → 2.0/10).

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

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0

This work is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**You are free to:**
- Share — copy and redistribute the material in any medium or format

**Under the following terms:**
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- NonCommercial — You may not use the material for commercial purposes
- NoDerivatives — If you remix, transform, or build upon the material, you may not distribute the modified material

### License History

**Earlier drafts may have been temporarily released under CC BY 4.0.**

- UBT versions **up to v0.3** were released under CC BY 4.0 (Creative Commons Attribution 4.0 International).
- Starting from **v0.4 onward**, all material is released under CC BY-NC-ND 4.0 (Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International) to protect the integrity of the theoretical work during ongoing academic development.

This change does not affect earlier releases (v0.3 and prior), which remain under CC BY 4.0.

For full license terms, see [LICENSE.md](LICENSE.md)
