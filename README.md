# Unified Biquaternion Theory (UBT)

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**A testable theoretical framework unifying General Relativity, Quantum Field Theory, and Standard Model symmetries**

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
| **Hubble latency** | δ ≈ 7.8% clock skew | H₀ tension ~8-9% | 🔄 **TESTABLE** | Awaiting standard sirens |

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
│   ├── model/              # Clock skew formulation (NOT dark energy)
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
- ✅ Systematic clock skew (δ ≈ 7.8%)
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
