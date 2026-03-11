# UBT Forensic Fingerprint Protocol

Court-grade statistical tests for digital architecture signatures in cosmological data.

## Overview

This directory contains three pre-registered statistical tests designed to search for potential signatures of discrete spacetime architecture that might be consistent with certain interpretations of the Unified Biquaternion Theory (UBT).

**Important**: This is **not** a discovery claim. These are falsification protocols using neutral, pre-committed analysis methods.

## Three Tests

1. **CMB Comb Signature** (`cmb_comb/`)
   - Searches for periodic oscillations in CMB power spectrum residuals
   - Tests candidate periods: 8, 16, 32, 64, 128, 255
   - See `cmb_comb/README.md` for details

2. **Grid 255 Quantization** (`grid_255/`)
   - Tests if cosmological parameters cluster near m/255 grid points
   - Fixed grid denominator: 255 (byte-like structure)
   - See `grid_255/README.md` for details

3. **Cross-Dataset Invariance** (`invariance/`)
   - Checks if UBT-predicted invariants agree across datasets
   - Tests Planck, BAO, SNe, lensing consistency
   - See `invariance/README.md` for details

## Quick Start

**NEW (2026-01)**: For comprehensive robustness testing with falsification campaign, see [Robustness & Falsification Campaign](#robustness--falsification-campaign) below.

### Installation

```bash
pip install numpy scipy matplotlib pytest
```

### Robustness & Falsification Campaign

**Recommended approach for publication-grade analysis**. Runs all stress tests systematically to attempt to invalidate the signal:

```bash
# Minimum required (3 core tests: whitening, ΛCDM null, ablation)
python forensic_fingerprint/run_robustness_campaign.py \
    --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model data/planck_pr3/raw/COM_PowerSpect_CMB-TT-model_R3.01.txt

# Full campaign (includes polarization and phase coherence if data available)
python forensic_fingerprint/run_robustness_campaign.py \
    --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model data/planck_pr3/raw/COM_PowerSpect_CMB-TT-model_R3.01.txt \
    --planck_cov data/planck_pr3/raw/COM_PowerSpect_CMB-TT-covariance_R3.01.txt \
    --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_model data/wmap/raw/wmap_tt_model_9yr_v5.txt \
    --include_phase_coherence
```

**Output**: Generates `ROBUSTNESS_AND_FALSIFICATION.md` with:
- Overall campaign verdict (PASS/FAIL/INCOMPLETE)
- Individual test results with explicit pass/fail
- Machine-readable JSON results
- Diagnostic plots

See `ROBUSTNESS_CAMPAIGN_README.md` for complete documentation.

### One-Command Real Data Analysis

Alternative: Run single CMB comb test with real data:

```bash
cd forensic_fingerprint

# Minimal (Planck only)
python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/spectrum.txt \
    --planck_model ../data/planck_pr3/raw/model.txt

# Full (Planck + WMAP with validation)
python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/spectrum.txt \
    --planck_model ../data/planck_pr3/raw/model.txt \
    --planck_manifest ../data/planck_pr3/manifests/planck_pr3_tt_manifest.json \
    --wmap_obs ../data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_manifest ../data/wmap/manifests/wmap_tt_manifest.json \
    --variant C --mc_samples 10000
```

**Note**: The runner automatically falls back to `sha256.json` or `manifest.json` if the standard manifest names are not found.

**Output**: Creates timestamped directory with:
- `planck_results.json` - Full statistical results
- `wmap_results.json` - Full statistical results (if WMAP provided)
- `combined_verdict.md` - **Court-grade PASS/FAIL report**
- `figures/*.png` - Diagnostic plots

See `RUNBOOK_REAL_DATA.md` for complete documentation.

### Running Individual Tests

Each test has its own directory with standalone implementation:

```bash
# Test 1: CMB Comb
cd cmb_comb
python cmb_comb.py observed.txt model.txt ../out/

# Test 2: Grid 255
cd grid_255
python grid_255.py chain_file.txt 0 ../out/

# Test 3: Invariance
cd invariance
python invariance.py ../out/
```

See individual README files for detailed usage instructions.

### Automated Testing

Run the test suite to verify implementations:

```bash
pytest tests/test_forensic_fingerprint.py -v
```

## Protocol

Complete protocol specification: `PROTOCOL.md`

Key principles:
- **Pre-registration**: All parameters, thresholds, and methods fixed before data analysis
- **Neutral language**: "Candidate signal" not "detection", "replication required" not "confirmed"
- **Reproducibility**: Fixed random seeds, dataset hashes, versioned outputs
- **Falsifiability**: Clear criteria for rejecting digital-architecture interpretation

## Significance Thresholds

| Level | P-value | Interpretation |
|-------|---------|----------------|
| Null | p ≥ 0.01 | No significant signal (H₀ not rejected) |
| Candidate | 0.01 > p ≥ 2.9×10⁻⁷ | Candidate signal — **replication required** |
| Strong | p < 2.9×10⁻⁷ | Strong signal (~5σ) — **immediate verification needed** |

**Note**: For invariance test (Test #3), the interpretation is reversed: high p-values support UBT, low p-values falsify it.

## Data Requirements

### Test 1: CMB Comb
- Planck 2018 power spectra (TT, TE, EE)
- WMAP 9-year (replication)
- Best-fit ΛCDM model predictions
- Download from: https://pla.esac.esa.int/

### Test 2: Grid 255
- Planck 2018 MCMC chains
- Parameters: Ω_b h², Ω_c h², θ_s, τ, n_s, ln(10¹⁰ A_s)
- Download from: https://pla.esac.esa.int/

### Test 3: Invariance
- Parameter estimates from published papers
- Datasets: Planck, BAO, Pantheon SNe, lensing
- See PROTOCOL.md for references

## Output Structure

### One-Command Runner Output

When using `run_real_data_cmb_comb.py`:

```
out/real_runs/cmb_comb_<timestamp>/
├── planck_results.json          # Full Planck results (machine-readable)
├── wmap_results.json            # Full WMAP results (if provided)
├── combined_verdict.md          # ★ Court-grade PASS/FAIL report ★
└── figures/
    ├── residuals_with_fit.png   # Planck residuals + fitted comb
    ├── null_distribution.png    # Planck p-value visualization
    ├── residuals_with_fit_1.png # WMAP residuals (if run)
    └── null_distribution_1.png  # WMAP p-value (if run)
```

### Individual Test Outputs

```
out/
├── cmb_comb_results.txt
├── residuals_with_fit.png
├── null_distribution.png
├── grid_255_param_0_results.txt
├── grid_255_param_0_distances.png
├── invariance_kappa_results.txt
└── invariance_kappa_forest.png
```

All outputs include:
- Summary statistics
- P-values
- Diagnostic plots
- Metadata (seeds, hashes, timestamps)

## Interpretation Guidelines

### Positive Result
If a test shows p < 0.01:
1. **DO NOT** claim discovery
2. **DO** label as "candidate signal"
3. **MUST** replicate in independent dataset
4. **MUST** rule out instrumental/systematic artifacts
5. **SHOULD** seek independent verification

### Null Result
If a test shows p ≥ 0.01:
1. Report openly with equal prominence
2. No post-hoc parameter changes allowed
3. Null result has equal scientific value
4. Consider alternative UBT formulations (new protocol)

### Replication Failure
If initial signal does not replicate:
1. Report as likely statistical fluctuation
2. Archive all results (positive and negative)
3. Update protocol if systematic issues found

## Falsifiability

The digital-architecture interpretation of UBT is **falsified** if:
- All three tests yield null results (p ≥ 0.01) in:
  - Planck 2018 full mission data
  - Independent CMB datasets (WMAP, ACT, SPT)
  - Multiple MCMC chains from different codes
  - All recommended parameter combinations

Alternative formulations require new pre-registered protocol (v2.0).

## Stress Tests (Robustness & Falsification)

Beyond the initial protocol, the **stress tests** actively attempt to falsify candidate signals using standard CMB analysis counter-arguments. See `stress_tests/README.md` for complete details.

### Five Independent Stress Tests

1. **Whitening / Full Covariance** (`test_1_whitening.py`)
   - Tests if signal survives proper covariance-aware whitening
   - CRITICAL: Signal must persist across all whitening modes
   
2. **Synthetic ΛCDM Null Controls** (`test_4_lcdm_null.py`)
   - Verifies Δℓ = 255 is rare in pure ΛCDM simulations
   - Anti-overfitting: Must appear in ≤1% of realizations
   
3. **ℓ-Range Ablation** (`test_3_ablation.py`)
   - Tests if signal is global or localized artifact
   - Must appear in ≥2 disjoint multipole ranges
   
4. **Polarization Channels** (`test_2_polarization.py`) - OPTIONAL
   - Tests cross-channel coherence (TT vs EE vs TE)
   - High-impact if data available
   
5. **Phase Coherence** (`test_5_phase_coherence.py`) - OPTIONAL
   - Tests phase stability across datasets
   - Requires WMAP data for cross-validation

### Running the Full Campaign

Use the master runner for systematic execution:

```bash
python forensic_fingerprint/run_robustness_campaign.py \
    --planck_obs data/planck_pr3/raw/TT_spectrum.txt \
    --planck_model data/planck_pr3/raw/TT_model.txt \
    --planck_cov data/planck_pr3/raw/TT_covariance.txt  # Optional but recommended
```

**Output**: `ROBUSTNESS_AND_FALSIFICATION.md` with overall PASS/FAIL verdict.

**Philosophy**: 
- This task is **successful even if the signal FAILS**
- Scientific integrity > confirmation
- A failed signal is better than a false positive

See `ROBUSTNESS_CAMPAIGN_README.md` and `stress_tests/COMPLETE_GUIDE.md` for full documentation.

## Ethical Standards

- **No cherry-picking**: All datasets examined, all results reported
- **No p-hacking**: No post-hoc parameter tuning
- **Open science**: All code, data, outputs publicly archived
- **Independent replication**: Encouraged and facilitated

## Code Structure

```
forensic_fingerprint/
├── PROTOCOL.md                      # Complete protocol specification
├── README.md                        # This file
├── ROBUSTNESS_CAMPAIGN_README.md    # Campaign execution guide
├── UBT_STRESS_TESTS.md             # Stress test results template
├── run_real_data_cmb_comb.py       # One-command CMB comb runner
├── run_robustness_campaign.py      # Master stress test runner ★
├── cmb_comb/
│   ├── cmb_comb.py                 # Test #1 implementation
│   └── README.md
├── grid_255/
│   ├── grid_255.py                 # Test #2 implementation
│   └── README.md
├── invariance/
│   ├── invariance.py               # Test #3 implementation
│   └── README.md
├── stress_tests/                    # Robustness & falsification tests
│   ├── README.md                    # Stress test overview
│   ├── COMPLETE_GUIDE.md            # Detailed methodology
│   ├── test_1_whitening.py          # Covariance whitening test
│   ├── test_2_polarization.py       # Cross-channel test
│   ├── test_3_ablation.py           # ℓ-range ablation test
│   ├── test_4_lcdm_null.py          # ΛCDM null controls
│   └── test_5_phase_coherence.py    # Phase stability test
├── loaders/                         # Dataset loaders
│   ├── planck.py                    # Planck PR3 loader
│   └── wmap.py                      # WMAP 9yr loader
├── tests/                           # Test suite
│   └── test_*.py
└── out/                             # Output directory (auto-created)
    ├── real_runs/                   # Real data analysis results
    ├── stress_tests/                # Stress test results
    └── robustness_campaign/         # Campaign results ★
```

## Testing

Automated test suite in `tests/test_forensic_fingerprint.py`:
- Validates all three implementations
- Uses synthetic data (no real Planck files required)
- Checks numerical correctness
- Verifies output file generation

Run with:
```bash
pytest tests/test_forensic_fingerprint.py -v
```

CI/CD via GitHub Actions: `.github/workflows/forensic_fingerprint.yml`

## Related Documentation

### Core Protocol
- **PROTOCOL.md** - Complete pre-registered protocol specification (LOCKED parameters)
- **REPO_GOVERNANCE.md** - Repository governance and "No-Fit / No Post-Hoc" policy

### Implementation

 - **tools/planck_validation/** - Planck 2018 parameter mapping implementation
  - `constants.py` - LOCKED architecture parameters (RS_N=255, RS_K=200, OFDM_CHANNELS=16)
  - `mapping.py` - Pre-registered mappings (M_payload, M_parity, M_ns)
  - `metrics.py` - Statistical evaluation (z-scores, chi-square, p-values)
  - `report.py` - Report generation (markdown, CSV, JSON)
- **tools/data_provenance/** - Dataset verification tools
  - `hash_dataset.py` - Compute SHA-256 hashes for court-grade provenance
  - `validate_manifest.py` - Validate files against pre-registered hashes

### Data Scaffolding
- **data/README.md** - Data directory overview
- **data/planck_2018/README.md** - Planck 2018 download instructions and hashes
- **data/wmap_9yr/README.md** - WMAP 9-year download instructions and hashes

### Testing
- **tests/test_forensic_fingerprint.py** - Tests for CMB comb, grid 255, invariance
- **tests/test_planck_validation_mapping.py** - Tests for Planck mapping (enforces locked values)
- **.github/workflows/forensic_fingerprint.yml** - CI/CD for forensic tests
- **.github/workflows/planck_validation.yml** - CI/CD for Planck validation

### LaTeX Appendices
- **speculative_extensions/appendices/appendix_F_fingerprint_protocol.tex** - Protocol LaTeX
- **speculative_extensions/appendices/appendix_PX_planck_validation.tex** - Planck mapping LaTeX

## Version History

- **v1.0** (2026-01-10): Initial pre-registered protocol
  - Three tests defined
  - Thresholds fixed
  - Datasets specified
  - Code implemented and tested

## Contributing

External researchers are encouraged to:
- Run this protocol on same/different datasets
- Propose alternative UBT invariants for Test #3
- Suggest improvements for protocol v2.0
- Report bugs or implementation issues

Submit via GitHub issues: https://github.com/DavJ/unified-biquaternion-theory/issues

## License

- **Code** (Python scripts): MIT License
- **Documentation** (Markdown, LaTeX): CC BY-NC-ND 4.0
- See repository LICENSE files

## Contact

- **Repository**: https://github.com/DavJ/unified-biquaternion-theory
- **Issues**: Submit via GitHub issue tracker
- **Protocol questions**: See PROTOCOL.md or open GitHub discussion

## Disclaimer

This protocol describes a **proposed** falsification framework. It does not claim any detection or discovery. The digital-architecture interpretation of UBT remains speculative and requires rigorous testing, replication, and independent verification before any scientific claims can be made.

**All results—positive or negative—have equal scientific value and will be reported transparently.**
