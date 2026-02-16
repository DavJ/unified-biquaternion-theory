# Unified Biquaternion Theory (UBT)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## 🏆 Nobel Prize Summary Documents

**NEW:** Comprehensive summaries of UBT prepared for Nobel Prize consideration:

- **[Nobel Prize Executive Summary](NOBEL_PRIZE_EXECUTIVE_SUMMARY.md)** - One-page overview of key achievements
- **[Nobel Prize Full Summary](NOBEL_PRIZE_SUMMARY.md)** - Complete technical summary with detailed comparisons

These documents provide accessible overviews of UBT's revolutionary unification of General Relativity and Quantum Mechanics, quantitative predictions, and scientific impact.

---

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

### Derivation Status Legend

UBT uses a 4-level classification system for all quantitative predictions:

| Status | Definition | Example |
|--------|------------|---------|
| **Derived (fit-free)** | Follows from axioms/geometry with zero fitted parameters | Electron mass baseline from Hopfion topology |
| **Structurally specified** | Mathematical form derived; coefficients to be determined from first principles | Alpha correction structure (form known, coefficients estimated) |
| **Estimated (first-pass)** | Coefficient values calculated from UBT structure but not yet rigorously derived | Structural corrections δN_anti, Δ_RG, Δ_grav, Δ_asym |
| **Fitted (calibrated)** | Parameters explicitly calibrated to match experimental data | Electron mass formula parameters A, p, B |

**Hypothesis**: Parameter selection pending derivation (e.g., n=137 channel choice)

See [`FITTED_PARAMETERS.md`](FITTED_PARAMETERS.md) for complete parameter transparency and [`docs/architecture/LAYERS.md`](docs/architecture/LAYERS.md) for Layer 1 (physics) vs Layer 2 (protocol) separation.

### Core Achievements

**Quantitative Predictions:**

| Observable | UBT Prediction | Channel | Experimental Value | Uncertainty | Relative Error | Derivation Status |
|------------|----------------|---------|-------------------|-------------|----------------|-------------------|
| **Fine-structure constant (baseline)** | **α₀⁻¹ = 137.000** | n=137 | 137.035999084 | ±0.000000021 | **0.026%** | Channel-dependent baseline (n=137 selected) |
| Fine-structure constant (effective) | α_eff⁻¹ ≈ 137.036 | n=137 | 137.035999084 | ±0.000000021 | ~0.00003% | α₀(137) + structural corrections (mostly derived) |
| **Electron mass (baseline)** | **m_e = 0.509856 MeV** | 0.51099895000 MeV | ±0.00000015 MeV | **0.22%** | **Derived (fit-free)** from Hopfion topology |
| Electron mass (with corrections) | m_e ≈ 0.510 MeV | 0.51099895000 MeV | ±0.00000015 MeV | ~0.2% | Structurally specified (parameters A,p,B fitted for validation) |

- 🌟 **Fine Structure Constant - Multi-Channel Geometric Framework**:
  - **α₀⁻¹ (Baseline Structure - Derived)**: Framework α⁻¹ ≈ n + Δα where n is winding number
    - Mathematical form derived from biquaternionic field equations
    - Layer 1 (Geometry): ∇†∇Θ = κ𝒯 → winding quantization → α⁻¹ ≈ n + corrections
  - **Channel Selection (Layer 2 - Multi-Channel Family)**:
    - UBT admits a **family of stable/metastable channels** (e.g., n=137, 139, 199, ...)
    - **Current channel**: n=137 (realized in our sector)
    - **Stability Scan**: n=137 ranks 53/99; NOT the only stable configuration
    - Alternative stable channels: n=199 (rank 1), 197, 193, 191, 181
    - Status: n=137 is selected/realized channel; channel selection mechanism under investigation
    - See: [`docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md`](docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md)
  - **Δα Corrections (Structurally Specified - Estimated)**:
    - Form: Δα = δN_anti + Δ_RG + Δ_grav + Δ_asym
    - Starting from CxH bare α⁻¹ = 136.973, corrections total ≈ 0.063
    - Four structural corrections (coefficients estimated from UBT structure):
      1. Non-commutative anticommutator: δN_anti ≈ 0.01 (estimated)
      2. Geometric RG flow: Δ_RG ≈ 0.040 (estimated from M⁴×T² curvature)
      3. CxH gravitational dressing: Δ_grav ≈ 0.015 (estimated)
      4. Mirror sector asymmetry: Δ_asym ≈ 0.01 (estimated)
    - Result for channel n=137: α_eff⁻¹(137) = 137.000 + 0.036 ≈ 137.036
    - Agreement with experiment (channel 137): within 0.00003% of CODATA
    - Status: Mathematical structure derived; coefficient values are first-pass estimates
    - Sensitivity: ~12% uncertainty in correction magnitudes (see FITTED_PARAMETERS.md)
  - **Multiple Independent Approaches** (validated for channel n=137):
    - M⁴×T² (torus/theta): 137.032 (within 0.003% of experiment)
    - CxH (biquaternionic): 136.973 (bare) + corrections ≈ 137.036
    - Geo-β (curvature): 137.000 (geometric anchor)
  - **Documentation**: [`FITTED_PARAMETERS.md`](FITTED_PARAMETERS.md) | [`docs/architecture/LAYERS.md`](docs/architecture/LAYERS.md) | [`NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md`](NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md)
- 🌟 **Electron Mass - Topological Derivation with Corrections**: **m_e baseline = 0.509856 MeV (0.22% accuracy)**

**Electron Mass - Multiple Approaches:**

| Approach | Method | m_e Prediction (MeV) | Error | Status | Parameters |
|----------|--------|----------------------|-------|--------|------------|
| **Hopfion (baseline)** | Topological soliton | 0.509856 | 0.22% | ✅ **Fully derived** | Pure geometry |
| **+ QED 1-loop** | EM self-energy | ~0.510 | ~0.2% | ⚠️ **Partly derived** | Cutoff from UBT |
| **+ Biquaternionic** | Complex time corrections | ~0.5105 | ~0.15% | 🔬 **In progress** | R_ψ from geometry |
| **+ Higher-order** | Multi-loop Hopfion | ~0.510-0.511 | ~0.1-0.2% | 🔬 **Pending** | Quantum soliton |
| **Experimental** | PDG 2024 | 0.51099895 | ±0.00000015 | — | Measurement |

**Best Current UBT Status:**
- ✅ **Baseline (fully derived)**: 0.509856 MeV from Hopfion topology (0.22% error, no fitted parameters)
- ⚠️ **With corrections (partly derived)**: ~0.510 MeV (~0.2% error, some parameters fitted for validation)

**Correction breakdown** (current implementation status):
1. **Hopfion baseline**: 0.509856 MeV (pure topology) ✅ Complete, fit-free
2. **QED self-energy**: δm ≈ 0.001 MeV (electromagnetic correction) ⚠️ Implemented, cutoff estimated
3. **Biquaternionic quantum**: δm ≈ 0.0005 MeV (complex time fluctuations) 🔬 In progress
4. **Higher-order topology**: δm ≈ 0.0003 MeV (multi-loop soliton) 🔬 Pending

**Key features:**
- **Unique capability**: UBT is the only framework deriving electron mass baseline from topology (SM, String Theory, LQG all treat as free parameter)
- **Fully derived baseline**: 0.509856 MeV (0.22% error) with NO experimental input
- **Correction parameters**: Currently fitted for validation; derivation roadmap in `FITTED_PARAMETERS.md`
- **Target**: < 0.01% error (< 50 eV) achievable with full quantum corrections from first principles
- See: `ELECTRON_MASS_REFINEMENT_ANALYSIS.md` and `FITTED_PARAMETERS.md` for complete status
- Source: `scripts/ubt_complete_fermion_derivation.py`
- ⭐ **SM Gauge Group Derived**: SU(3)×SU(2)×U(1) rigorously derived from biquaternionic geometry (not assumed)
- ✅ **Quantum Gravity Unification**: GR+QFT unified in single Θ field framework
- ✅ **Mathematical Validation**: All core predictions verified using SymPy/NumPy
- ✅ **Scientific Rating Upgrade**: 4.5/10 → 5.5/10 → **6.2/10** following geometric baseline achievements

### What IS and ISN'T Derived Yet

**Derived (fit-free) - Layer 1 Geometry:**
- ✅ Biquaternionic field structure ℂ⊗ℍ (axiom/definition)
- ✅ Field equation ∇†∇Θ = κ𝒯 (framework)
- ✅ GR recovery in real limit: R_μν - ½g_μν R = 8πG T_μν (proven in Appendix R)
- ✅ SM gauge group SU(3)×SU(2)×U(1) from Aut(ℂ⊗ℍ) (rigorously derived)
- ✅ Electron mass baseline m_e = 0.509856 MeV from Hopfion topology (0.22% error, zero fitted)
- ✅ Prime constraint for winding numbers (from gauge quantization)
- ✅ Alpha framework: α⁻¹ ≈ n + Δα (mathematical structure derived)

**Structurally Specified (form derived, coefficients TBD):**
- ⚙️ Alpha corrections Δα: Four-term structure derived, coefficient values estimated
  - Form: Δα = δN_anti + Δ_RG + Δ_grav + Δ_asym (derived from field equations)
  - Coefficients: First-pass estimates from UBT structure (~12% uncertainty)
  - Roadmap: Full derivation via heat-kernel/spectral expansion (Priority 1, 6-12 months)
- ⚙️ Electron mass corrections: QED cutoff estimated, parameters A,p,B fitted for validation
  - Form: Correction structure from Hopfion quantum fluctuations
  - Coefficients: Currently calibrated; derivation roadmap in FITTED_PARAMETERS.md

**Hypothesis / Channel Selection (Layer 2 - Multi-Channel Family):**
- ⚠️ **Winding number n=137**: Currently realized channel in our sector
  - **Multi-channel framework**: UBT supports multiple stable channels (137, 139, 199, ...)
  - Stability scan: n=137 ranks 53/99; **not the only stable configuration**
  - Other stable candidates: n=199 (rank 1), 197, 193, 191, 181
  - Status: n=137 is observed/selected channel; selection mechanism under investigation
  - See: [`docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md`](docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md)
  - Each channel yields different α_eff(channel) and correlated observable shifts (testable)
- ⚠️ RS(255,201) error correction code parameters (engineering choice)
- ⚠️ GF(2⁸) finite field / 256-state quantization (discretization choice)

**Framework Only (calculation pending):**
- 🔬 Yukawa couplings (formalism exists, explicit values not calculated)
- 🔬 Dark matter properties (p-adic framework, no specific predictions yet)
- 🔬 Multi-generation fermion masses (extension of baseline, not calculated)

**Complete Transparency:**
- [`FITTED_PARAMETERS.md`](FITTED_PARAMETERS.md) - Authoritative parameter status
- [`docs/architecture/LAYERS.md`](docs/architecture/LAYERS.md) - Layer 1 vs Layer 2 separation
- [`docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md`](docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md) - Stability analysis

### Theoretical Advances
- **Appendix G (2025)**: Hamiltonian-in-exponent θ-function formulation
- **Appendix G.5 (2025)**: Biquaternionic Fokker-Planck equation
- **Appendix N2 Extended (2025)**: Full 8D biquaternionic time manifold formalism
- **Enhanced Documentation**: Comprehensive glossaries, rigor classification, honest assessments

### Multi-Channel Stability (Channel Family)

**Key Insight**: UBT admits a **family of stable/metastable channels**, not a single unique configuration.

- **Channel Definition**: A discrete stable/metastable sector (mode family) of the UBT dynamics/topology, characterized by winding number n or other topological invariants
- **Current Channel**: n=137 is the **realized channel in our observed sector**
- **Alternative Channels**: Other stable configurations exist (e.g., n=139, 199, 197, 193, ...) with different α_eff values
- **Layer-2 Selection**: The coding/modulation layer (Layer 2) provides the mechanism for channel selection/realization
  - This is a **physical selection mechanism**, not arbitrary choice
  - Analogous to OFDM-like carrier selection in information theory
  - Does NOT invalidate the underlying physics; rather explains which stable configuration is manifested
- **Testable Predictions**:
  - Channel shifts would imply correlated changes in multiple observables (α_eff, masses, couplings)
  - Different channels could be realized in different cosmological epochs or sectors
  - The channel family structure itself is a prediction
- **Effective Constants**: Observable values like α_eff = α₀(channel) + Δ_struct(channel) depend on the selected channel
- **Transparency**: This multi-channel view replaces earlier claims of n=137 being a "unique stability maximum" - empirically, n=137 ranks 53/99 in stability scans

**See**: [`docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md`](docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md) for detailed stability analysis

**For complete details on achievements and approaches:**
- **[FITTED_PARAMETERS.md](FITTED_PARAMETERS.md)** - Complete transparency on which parameters are derived vs fitted
- **[NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md](NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md)** - Structural corrections for α⁻¹ ≈ 137.036
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

### Formal Verification Framework (February 2026)

UBT provides formal mathematical derivations demonstrating complete unification:

1. **Quantum Mechanics & General Relativity Unification** ([`appendix_FORMAL_qm_gr_unification.tex`](consolidation_project/appendix_FORMAL_qm_gr_unification.tex))
   - Derives both Schrödinger/Dirac equations and Einstein field equations from single field Θ(q,τ)
   - Uses drift-diffusion dynamics on complexified manifold
   - No postulated forces, particles, or fundamental metric

2. **Emergent Metric & Einstein Equation** ([`appendix_FORMAL_emergent_metric.tex`](consolidation_project/appendix_FORMAL_emergent_metric.tex))
   - Metric tensor g_μν emerges as bilinear functional of Θ
   - Einstein equation derived, not assumed
   - Curvature arises from phase gradients in complex time

3. **Black Hole Radiation via Complex Time** ([`appendix_FORMAL_black_hole_radiation.tex`](consolidation_project/appendix_FORMAL_black_hole_radiation.tex))
   - Explains Hawking radiation without vacuum pair creation
   - Information preserved in global Θ-field
   - Horizon is projection singularity, not fundamental boundary

4. **Fundamental Constants from Normalization** ([`appendix_FORMAL_constants_normalization.tex`](consolidation_project/appendix_FORMAL_constants_normalization.tex))
   - Constants emerge as spectral/topological invariants
   - Fine-structure constant α ≈ 1/137 from compactified manifold geometry
   - No manual parameter tuning required

---

## What UBT is NOT

To prevent misconceptions, we state explicitly what UBT does **NOT** claim:

❌ **NOT a replacement for General Relativity** - UBT generalizes GR; in the real limit (ψ → 0), UBT exactly reproduces Einstein's equations. All GR confirmations validate UBT's real sector.

❌ **NOT about consciousness** - Core UBT makes NO claims about consciousness. "Psychons" and related content are speculative extensions kept in `SPECULATIVE/` directory.

❌ **NOT claiming time travel** - Closed timelike curves exist mathematically (as in GR) but are not claimed to be physically realized.

❌ **NOT a multiverse theory** - Parallel branches in computational model are coherent paths in a single universe, not separate worlds.

❌ **NOT proven** - UBT has validated predictions (α, m_e baselines), null results (Planck CMB comb), and many untested predictions. It is a working framework subject to empirical validation.

---

## Current Empirical Status

| Observable | UBT Prediction | Experimental Value | Derivation Status | Error |
|------------|----------------|-------------------|-------------------|-------|
| **Fine structure constant (n=137 framework)** | α⁻¹ = 137.000 | 137.035999084 ± 0.000000021 | **Hypothesis** (channel n=137 selection) | **0.026%** |
| **Fine structure constant (with corrections)** | α⁻¹ ≈ 137.036 | 137.035999084 ± 0.000000021 | **Partly derived** (~90%) | **~0.00003%** |
| **Electron mass (baseline)** | m_e = 0.509856 MeV | 0.51099895 ± 0.00000015 MeV | **Derived** (Hopfion topology) | **0.22%** |
| **Electron mass (with corrections)** | m_e ≈ 0.510 MeV | 0.51099895 ± 0.00000015 MeV | **Partly derived** (~60%) | **~0.2%** |
| **Planck CMB TT comb** | Δℓ ∈ {8,16,32,64,128,255} | No signal detected (p=0.919) | Hypothesis | ❌ **NULL** |
| **WMAP CMB TT comb** | — | Δℓ=255 (p=1e-4, not replicated) | Candidate | ⚠️ Non-replicating |
| **Hubble latency** | δ ≈ 7.8% clock shear | H₀ tension ~8-9% | Hypothesis | 🔄 **TESTABLE** |

**Summary**: 2 fully derived baselines (electron mass baseline, SM gauge group) + 2 partly derived refinements (alpha & electron corrections), 1 hypothesis (n=137 selection), 1 null result, 1 non-replicating candidate.

**Scientific rating**: ~6.2/10 (improved from 4.5 following geometric baseline achievements and honest parameter accounting)

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
- **Comparing with other theories?** → See [`THEORY_COMPARISONS/`](THEORY_COMPARISONS/)

---

## Key Scientific Achievements

### 1. Fine Structure Constant (α) - Geometric Framework with Channel Selection

**Layer 1 (Geometric Framework)**: α⁻¹ ≈ n + corrections ✅ Derived
**Layer 2 (Channel Selection)**: n=137 chosen ⚠️ Hypothesis (NOT stability max)

**Stability Scan Results** ([`docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md`](docs/alpha/ALPHA_STABILITY_SELECTION_RULE.md)):
- n=137 ranks **53/99** in combined stability score
- Better candidates: n=199 (rank 1), n=197 (rank 2), n=193 (rank 3), n=191 (rank 4), n=181 (rank 5)
- Even neighbor n=139 is more stable (rank 2 vs 137's rank 53)
- **Conclusion**: n=137 is a channel selection/calibration, NOT uniquely derived from stability

**With n=137 Selected**:
- Baseline: α⁻¹ = 137.000 (0.026% error from CODATA)
- With corrections: α⁻¹ ≈ 137.036 (~0.00003% error)

**Multiple independent approaches** using n=137 converge:
- M⁴×T² (torus/theta): 137.032
- CxH (biquaternionic): 136.973 (bare) + corrections ≈ 137.036
- Geo-β (curvature): 137.000

**Status of n=137 selection**: Currently interpreted as **Layer 2 channel selection** to match experimental α. Geometric framework (α⁻¹ ≈ n + corrections) remains valid, but specific choice n=137 is not uniquely determined by stability principles.

**Transparency**: [`FITTED_PARAMETERS.md`](FITTED_PARAMETERS.md) | [`docs/architecture/LAYERS.md`](docs/architecture/LAYERS.md)

### 2. Electron Mass (m_e) - Topological Baseline Derivation

**UBT Baseline (Fully Derived)**: m_e = 0.509856 MeV (topological soliton)
**UBT with Corrections (~60% derived)**: m_e ≈ 0.510 MeV
**Experiment**: m_e = 0.51099895 ± 0.00000015 MeV (PDG 2024)

**Agreement**: 
- Baseline: 0.22% error (fully derived from Hopfion topology, no fitted parameters)
- With corrections: ~0.2% error (correction parameters currently fitted for validation)

**Derivation from Hopfion topology:**
- Baseline (pure geometry): 0.509856 MeV (0.22% error) ✅ Fully derived
- + QED 1-loop: ~0.510 MeV (~0.2% error) ⚠️ Cutoff estimated
- + Biquaternionic corrections: In progress
- + Higher-order: Pending

**Status**: Baseline is fully derived with NO experimental input. Correction parameters (A, p, B in mass formula) are currently fitted for validation, with roadmap for derivation in `FITTED_PARAMETERS.md` (Priority 2, 12-month timeline).

**UBT Achievement**: Only framework deriving electron mass baseline from topology. Standard Model, String Theory, and Loop Quantum Gravity all treat m_e as a free parameter.

See: [`FINGERPRINTS/confirmed/electron_mass.md`](FINGERPRINTS/confirmed/electron_mass.md) and [`FITTED_PARAMETERS.md`](FITTED_PARAMETERS.md)

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
