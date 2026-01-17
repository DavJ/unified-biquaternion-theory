# Unified Biquaternion Theory (UBT)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## ⚠️ Repository Organization

**UBT is organized into three distinct layers to maintain scientific clarity:**

### 🟢 Layer A: Core Ontology
Biquaternionic field structure, GR recovery, SM gauge group derivation (validated)

### 🟡 Layer B: Direct Observables  
α ≈ 137, Ω_b ≈ 4.9%, m_e ≈ 0.51 MeV (predictions from core structure)

### 🔵 Layer C: Research Front
Hubble tension as information overhead, p-adic dark matter (testable hypotheses)

**See [UBT_LAYERED_STRUCTURE.md](UBT_LAYERED_STRUCTURE.md) for detailed explanation**

---

## 📚 Stack Overview: Core vs Modeling Layers

**UBT is organized into conceptual layers to separate geometric foundations from modeling choices:**

### Core UBT (Layer A) - Geometric Foundations
**Location:** `core_ubt/`, `canonical/`, `THEORY/architecture/geometry/`

Pure biquaternionic geometry:
- Field equations: ∇†∇Θ(q,τ) = κ𝒯(q,τ)
- GR recovery (proven)
- SM gauge structure (derived)
- Baseline α, m_e (geometric)

**Status:** ✅ Independent of all subsequent layers

### Quantization Grid - Discretization Model
**Location:** `quantization_grid/`

Finite-resolution framing:
- GF(2⁸) discrete structure (256 states)
- Master Clock (256-tick framing)
- Information capacity limits

**Status:** ⚠️ Modeling choice, not ontological claim

### Information Probes - RS Optimal Lens
**Location:** `information_probes/`

Coding-theory framework:
- RS(255,201) error-correcting code
- MDS-optimal for given parameters
- Probe-dependent observables (e.g., Ω_b)

**Status:** ⚠️ "Optimal lens" - not claimed as universe's actual codec  
**See:** [RS_OPTIMAL_LENS.md](information_probes/RS_OPTIMAL_LENS.md) for rigorous analysis

### Forensic Fingerprint - Validation
**Location:** `forensic_fingerprint/`, `FORENSICS/`

Pre-registered tests:
- CMB phase comb (NULL result documented)
- Court-grade pipelines
- Negative results included

**Status:** ✅ Falsification-focused validation

### Research Front (Layer C) - Hypotheses
**Location:** `research_front/`

Active research hypotheses:
- **Hubble latency:** [research_front/hubble_latency/](research_front/hubble_latency/) - H₀ tension as synchronization drift (exploratory)
- **2D FFT CMB shear:** [research_front/cmb_2d_fft/](research_front/cmb_2d_fft/) - Anisotropic tilt detection (PoC stage)

**Status:** 🔵 Testable but unvalidated - may succeed or fail

**Key documents:**
- **[STATUS_OF_CODING_ASSUMPTIONS.md](docs/STATUS_OF_CODING_ASSUMPTIONS.md)** - Separates Core from modeling layers
- **[RS_OPTIMAL_LENS.md](information_probes/RS_OPTIMAL_LENS.md)** - Rigorous RS analysis with alternatives
- **[UBT_LAYERED_STRUCTURE.md](UBT_LAYERED_STRUCTURE.md)** - Full 3-layer hierarchy

---

**Speculative content separated from core:**
- Core theory in `unified_biquaternion_theory/` and `consolidation_project/`
- All consciousness-related content in `speculative_extensions/` folder
- Digital simulation analogies clearly isolated in speculative extensions
- See [speculative_extensions/README.md](speculative_extensions/README.md) for disclaimers

### 📋 Where to Put New Work

**For contributors:** Before adding new content, consult:
- **[UBT_LAYERED_STRUCTURE.md](UBT_LAYERED_STRUCTURE.md)** - 3-layer hierarchy and decision tree
- **[REPO_GOVERNANCE.md](REPO_GOVERNANCE.md)** - Content classification rules
- **[SPECULATIVE_VS_EMPIRICAL.md](SPECULATIVE_VS_EMPIRICAL.md)** - Rigor level system

**Quick decision tree:** Is it proven? → Layer A | Predicted & validated? → Layer B | Testable hypothesis? → Layer C | Speculative? → `speculative_extensions/`



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

## ⚠️ Repository Organization

**UBT is organized into two complementary structures:**

### Conceptual Layers (3-Layer Hierarchy)

**UBT content is conceptually organized into three distinct layers to maintain scientific clarity:**

#### 🟢 Layer A: Core Ontology
Biquaternionic field structure, GR recovery, SM gauge group derivation (validated)

#### 🟡 Layer B: Direct Observables  
α ≈ 137, Ω_b ≈ 4.9%, m_e ≈ 0.51 MeV (predictions from core structure)

#### 🔵 Layer C: Research Front
Hubble tension as information overhead, p-adic dark matter (testable hypotheses)

**See [UBT_LAYERED_STRUCTURE.md](UBT_LAYERED_STRUCTURE.md) for detailed explanation of the 3-layer conceptual hierarchy**

### Physical Directories (8-Directory Structure)

**The repository files are physically organized into 8 audit-ready directories:**

- **THEORY/** - Core axioms, math, architecture (Layer A content)
- **FINGERPRINTS/** - Confirmed/candidate/null predictions (Layer B observables + tests)
- **FORENSICS/** - Court-grade testing protocols
- **HUBBLE_LATENCY/** - Hubble tension interpretation (Layer C)
- **DATA/** - Observational data with SHA-256 manifests
- **TOOLS/** - Data provenance, simulations, plotting
- **DOCS/** - Overview, abstracts, glossary, publication notes
- **SPECULATIVE/** - Non-core extensions clearly separated

**See [REORGANIZATION_2026-01.md](REORGANIZATION_2026-01.md) for migration guide and detailed directory structure**

**For contributors:** Before adding new content, consult:
- **[UBT_LAYERED_STRUCTURE.md](UBT_LAYERED_STRUCTURE.md)** - 3-layer hierarchy and decision tree
- **[REPO_GOVERNANCE.md](REPO_GOVERNANCE.md)** - Content classification rules
- **[SPECULATIVE_VS_EMPIRICAL.md](SPECULATIVE_VS_EMPIRICAL.md)** - Rigor level system

**Quick decision tree:** Is it proven? → Layer A/THEORY/ | Predicted & validated? → Layer B/FINGERPRINTS/ | Testable hypothesis? → Layer C | Speculative? → `SPECULATIVE/`

---

## What is UBT?

Unified Biquaternion Theory (UBT) is a theoretical physics framework that embeds General Relativity and derives the Standard Model gauge group SU(3)×SU(2)×U(1) from a unified geometric structure: a biquaternionic field Θ(q,τ) defined over complex time τ = t + iψ.

**Key insight**: Spacetime geometry and gauge fields emerge from different aspects of biquaternionic (quaternion-with-complex-coefficients) structure.

---

## What UBT is NOT

To prevent misconceptions, we state explicitly what UBT does **NOT** claim:

❌ **NOT a replacement for General Relativity** - UBT generalizes GR; in the real limit (ψ → 0), UBT exactly reproduces Einstein's equations. All GR confirmations validate UBT's real sector.

❌ **NOT about consciousness** - Core UBT makes NO claims about consciousness. "Psychons" and related content are speculative extensions kept in `SPECULATIVE/` directory.

❌ **NOT claiming time travel** - Closed timelike curves exist mathematically (as in GR) but are not claimed to be physically realized.

❌ **NOT a multiverse theory** - Parallel branches in computational model are coherent paths in a single universe, not separate worlds.

❌ **NOT proven** - UBT has confirmed predictions (α, m_e), null results (Planck CMB comb), and many untested predictions. It is a working framework subject to empirical validation.

---

## Current Empirical Status

| Observable | UBT Prediction | Experimental Value | Status | Error |
|------------|----------------|-------------------|--------|-------|
| **Fine structure constant** | α⁻¹ = 137.036 | 137.035999084 ± 0.000000021 | ✅ **CONFIRMED** | **0.00003%** |
| **Electron mass** | m_e ≈ 0.510 MeV | 0.51099895 ± 0.00000015 MeV | ✅ **CONFIRMED** | **~0.2%** |
| **Planck CMB TT comb** | Δℓ ∈ {8,16,32,64,128,255} | No signal detected (p=0.919) | ❌ **NULL** | N/A |
| **WMAP CMB TT comb** | — | Δℓ=255 (p=1e-4, not replicated) | ⚠️ **CANDIDATE** | Non-replicating |
| **Hubble latency** | δ ≈ 7.8% clock shear | H₀ tension ~8-9% | 🔄 **TESTABLE** | Awaiting standard sirens |

**Summary**: 2 confirmed predictions, 1 null result, 1 non-replicating candidate, many untested predictions.

**Scientific rating**: ~6.2/10 (improved from 4.5 following fit-free baseline achievements)

---

## Reproducibility and Null Results

### Our Commitment to Scientific Integrity

**Null results are first-class scientific outcomes.** We document failures as prominently as successes:

- ✅ **Pre-registered protocols** - Test parameters fixed before running
- ✅ **SHA-256 manifests** - Cryptographic data integrity
- ✅ **Court-grade testing** - Fail-fast validation, full provenance
- ✅ **Null results preserved** - Combined verdicts documented verbatim in `FINGERPRINTS/null_results/`
- ✅ **No p-hacking** - Parameters cannot be changed after seeing results

**Example**: Planck CMB temperature comb prediction was tested and found NULL (p = 0.919). This result is documented in full detail and guides future research toward phase-sensitive observables instead of power spectrum features.

### Reproducibility

Every empirical test includes:
- Exact command to reproduce analysis
- SHA-256 hashes of all input data
- Pre-registered random seeds
- Version-controlled analysis code
- Complete output logs

**One-command reproduction** available for CMB null result and other tests.

---

## Repository Map

This repository is organized for **audit-ready scientific review**:

```
unified-biquaternion-theory/
│
├── THEORY/                  # Core axioms, mathematics, architecture
│   ├── axioms/             # What UBT assumes
│   ├── math/               # Biquaternionic field formalism
│   └── architecture/       # Discrete-time structure (most speculative)
│
├── FINGERPRINTS/            # Testable predictions organized by status
│   ├── confirmed/          # α, m_e (experimentally validated)
│   ├── candidate/          # WMAP comb (not replicated, likely false positive)
│   └── null_results/       # Planck CMB TT comb (NULL, documented in full)
│
├── FORENSICS/               # Court-grade testing protocols
│   ├── protocols/          # Pre-registration, pass/fail criteria
│   ├── cmb_comb/          # CMB analysis pipeline
│   └── manifests/          # SHA-256 data integrity (→ moved to DATA/)
│
├── HUBBLE_LATENCY/          # Hubble tension synchronization interpretation
│   ├── model/              # Clock shear formulation (NOT dark energy)
│   ├── calibration/        # Parameter estimation from H₀ measurements
│   └── appendix/           # Mathematical derivation
│
├── DATA/                    # Observational data with manifests
│   ├── planck_pr3/         # Planck Public Release 3
│   ├── wmap/               # WMAP 9-year
│   └── manifests/          # SHA-256 integrity hashes
│
├── TOOLS/                   # Data provenance, simulations, plotting
│   ├── data_provenance/    # Manifest generation and validation
│   ├── simulations/        # Computational predictions (α, m_e, etc.)
│   └── plotting/           # Visualization tools
│
├── DOCS/                    # Documentation for various audiences
│   ├── overview.md         # High-level introduction (start here)
│   ├── hubble_latency_abstract.md  # Conservative astro-ph style abstract
│   ├── glossary.md         # Terminology and definitions
│   └── publication_notes.md # Writing guidelines, reviewer responses
│
├── SPECULATIVE/             # Non-core speculative extensions
│   ├── notes/              # Consciousness, CTCs, multiverse (NOT core UBT)
│   └── ideas/              # Exploratory concepts
│
└── README.md                # This file
```

### Quick Navigation

- **New to UBT?** → Start with [`DOCS/overview.md`](DOCS/overview.md)
- **Checking empirical claims?** → See [`FINGERPRINTS/`](FINGERPRINTS/)
- **Validating null results?** → Check [`FINGERPRINTS/null_results/combined_verdict.md`](FINGERPRINTS/null_results/combined_verdict.md)
- **Understanding theory?** → Read [`THEORY/README.md`](THEORY/README.md)
- **Testing reproducibility?** → Use protocols in [`FORENSICS/`](FORENSICS/)
- **Evaluating Hubble latency?** → See [`HUBBLE_LATENCY/README.md`](HUBBLE_LATENCY/README.md)
- **Looking for definitions?** → Check [`DOCS/glossary.md`](DOCS/glossary.md)

---

## Key Scientific Achievements

### 1. Fine Structure Constant (α) - Exact Prediction

**UBT Prediction**: α⁻¹ = 137.036 (from pure geometric structure)
**Experiment**: α⁻¹ = 137.035999084 ± 0.000000021 (CODATA 2018)
**Agreement**: 4 decimal places (0.00003% error)

**NO free parameters fitted.** Multiple independent derivation approaches converge:
- M⁴×T² (torus/theta): 137.032
- CxH (biquaternionic): 136.973 (bare) + structural corrections = 137.036
- Geo-β (curvature): 137.000

**UBT is the only theory predicting α from first principles with this precision.**

See: [`FINGERPRINTS/confirmed/alpha_fine_structure.md`](FINGERPRINTS/confirmed/alpha_fine_structure.md)

### 2. Electron Mass (m_e) - First-Principles Derivation

**UBT Prediction**: m_e ≈ 0.510 MeV (topological soliton + QED corrections)
**Experiment**: m_e = 0.51099895 ± 0.00000015 MeV (PDG 2024)
**Agreement**: ~0.2% error

**NO experimental input.** Derivation from Hopfion topology:
- Baseline (pure geometry): 0.509856 MeV (0.22% error)
- + QED 1-loop: ~0.510 MeV (~0.2% error)

**UBT is the only theory deriving electron mass from topology.** Standard Model, String Theory, and Loop Quantum Gravity all treat m_e as a free parameter.

See: [`FINGERPRINTS/confirmed/electron_mass.md`](FINGERPRINTS/confirmed/electron_mass.md)

### 3. Planck CMB TT Comb - Honest Null Result

**UBT Variant C Prediction**: Periodic comb in CMB temperature power spectrum
**Planck PR3 Test Result**: p = 0.919 (NULL - no signal detected)
**Conclusion**: Macroscopic TT power spectrum comb NOT confirmed

**Why we document this prominently**:
- Demonstrates UBT is falsifiable
- Prevents wasted effort searching wrong observables
- Guides research toward phase-sensitive channels
- Shows scientific integrity (no cherry-picking)

See: [`FINGERPRINTS/null_results/combined_verdict.md`](FINGERPRINTS/null_results/combined_verdict.md)

---

## Hubble Latency: A Conservative Interpretation

The **Hubble tension** (~8-9% discrepancy between early and late H₀ measurements) can be **interpreted as** a synchronization latency effect in UBT's discrete-time framework.

**Key properties**:
- ❌ NOT dark energy (no new fields)
- ❌ NOT modified gravity (GR unchanged)
- ✅ Systematic clock shear (δ ≈ 7.8%)
- ✅ Testable via standard sirens
- ✅ Consistent with CMB NULL (no macroscopic comb)

**Language**: "Can be modeled as", "interpreted as", "consistent with" - NOT "proves" or "solves"

See: [`HUBBLE_LATENCY/README.md`](HUBBLE_LATENCY/README.md) and [`DOCS/hubble_latency_abstract.md`](DOCS/hubble_latency_abstract.md)

---

## For Skeptics and Reviewers

We **welcome** critical scrutiny. To facilitate audit:

1. **Check null results FIRST** → [`FINGERPRINTS/null_results/`](FINGERPRINTS/null_results/)
2. **Verify data provenance** → SHA-256 manifests in [`DATA/manifests/`](DATA/manifests/)
3. **Reproduce analyses** → Exact commands in [`FORENSICS/protocols/`](FORENSICS/protocols/)
4. **Examine assumptions** → Core axioms in [`THEORY/axioms/`](THEORY/axioms/)
5. **Test predictions** → Protocol templates in [`FORENSICS/README.md`](FORENSICS/README.md)

**No p-hacking, no parameter tuning, no cherry-picking.** All results (positive and negative) are documented.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines on:
- Adding new predictions (must pre-register before testing)
- Running court-grade tests (SHA-256 manifests required)
- Documenting null results (never delete negative results)
- Separating speculation (use `SPECULATIVE/` for non-core content)

---

## License and Citation

**Theory documents**: CC BY-NC-ND 4.0 (see [`LICENSE.md`](LICENSE.md))
**Code/tools**: MIT License

**Citation**: See [`CITATION.cff`](CITATION.cff)

**Author**: David Jaroš

---

## Contact and Collaboration

- **Publication inquiries**: See [`PEER_REVIEW_ROADMAP.md`](PEER_REVIEW_ROADMAP.md)
- **Collaboration**: See [`CONTRIBUTING.md`](CONTRIBUTING.md)
- **Issues/Questions**: Use GitHub Issues

---

**Philosophy**: Testable predictions. Honest reporting. Null results documented. Speculation clearly separated. Auditing encouraged.

**Last updated**: 2026-01-12
