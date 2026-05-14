# Forensic Fingerprint Pipeline - Master Index

**Purpose**: Central navigation for all forensic fingerprint search documentation and tools  
**Version**: 1.0  
**Date**: 2026-01-12  
**License**: MIT License (code) / CC BY-NC-ND 4.0 (documentation)

---

## Quick Navigation

### 🎯 Start Here
- **New to the project?** → Read [OVERVIEW.md](#overview) first
- **Ready to run tests?** → See [Quick Start Guide](#quick-start)
- **Looking for results?** → Check [Reports Directory](reports/)

### 📚 Core Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [SEARCH_SPACE.md](SEARCH_SPACE.md) | Complete catalog of all candidate observable channels | Everyone |
| [PROTOCOL.md](PROTOCOL.md) | Court-grade testing protocol (legacy tests) | Technical |
| [RUNBOOK_PHASE_COHERENCE.md](RUNBOOK_PHASE_COHERENCE.md) | **Phase coherence workflow** (exploratory → confirmatory) | Users |
| [INTERPRETATION_NOTES.md](INTERPRETATION_NOTES.md) | Template for post-confirmation interpretation | Theorists |

### 📊 Results & Reports

| Document | Status | Summary |
|----------|--------|---------|
| [CMB_TT_NEGATIVE_BENCHMARK.md](reports/CMB_TT_NEGATIVE_BENCHMARK.md) | **CLOSED** | TT power spectrum comb: NULL (p ≈ 0.92) |
| [CMB_COMB_REPORT_2026-01-12.md](reports/CMB_COMB_REPORT_2026-01-12.md) | Archive | Full CMB comb test report (Planck + WMAP) |

### 🔬 Analysis Scripts

#### Phase Coherence Tests (NEW)
- `run_exploratory_phase_scan.py` - Exploratory phase-locking scan
- `run_real_data_cmb_phase_confirm.py` - Confirmatory test with pre-registration

#### Legacy Tests
- `run_real_data_cmb_comb.py` - CMB amplitude comb test
- `run_real_data_cmb_phase_comb.py` - Phase comb test (older version)
- `run_robustness_campaign.py` - Comprehensive falsification campaign
- `run_audit_suite.py` - Audit and validation suite

### 📁 Directory Structure

```
forensic_fingerprint/
├── SEARCH_SPACE.md                    # Master catalog of all channels
├── PROTOCOL.md                        # Legacy test protocol
├── RUNBOOK_PHASE_COHERENCE.md         # Phase coherence workflow guide
├── INTERPRETATION_NOTES.md            # Post-confirmation interpretation template
│
├── reports/                           # Test results and benchmarks
│   ├── CMB_TT_NEGATIVE_BENCHMARK.md  # CLOSED: TT power spectrum NULL
│   └── CMB_COMB_REPORT_2026-01-12.md # Archive: Full comb test report
│
├── pre_registration/                  # Court-grade pre-registrations
│   ├── README.md                      # Pre-registration workflow
│   └── PHASE_TEST_v1_TEMPLATE.json   # Template for phase tests
│
├── cmb_phase_comb/                    # Phase coherence module
│   ├── phase_comb.py                  # Core R(P) statistic
│   ├── nulls.py                       # Phase-randomized surrogates
│   └── io_healpix.py                  # FITS I/O utilities
│
├── cmb_comb/                          # Legacy amplitude comb module
├── grid_255/                          # Parameter quantization test
├── invariance/                        # Cross-dataset invariance test
├── stats/                             # Statistical utilities
├── loaders/                           # Data loading utilities
└── tests/                             # Unit tests
```

---

## Overview

This system implements a **disciplined forensic search** for "fingerprints" of discrete/relational structure in physical observables.

### Key Principles

1. **Unknown target**: We do NOT know:
   - Exact observable
   - Exact location
   - Exact shape

2. **Avoid data dredging**:
   - Pre-register confirmatory tests
   - Separate exploratory from confirmatory
   - Document all channels tested

3. **Court-grade rigor**:
   - Every result has null model
   - P-values mandatory
   - SHA-256 data validation
   - Reproducible (fixed seeds, versioned code)

4. **Progressive narrowing**:
   - Start broad (exploratory)
   - Narrow to candidates
   - Confirm with pre-registration
   - Replicate across datasets

---

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/DavJ/unified-biquaternion-theory.git
cd unified-biquaternion-theory/forensic_fingerprint

# Install dependencies
pip install numpy scipy matplotlib healpy pytest

# Verify installation
python -c "import healpy as hp; print('healpy OK')"
```

### Phase Coherence Test (NEW)

**Exploratory scan**:
```bash
python run_exploratory_phase_scan.py \
    --alm_file ../data/planck_pr3/alm/planck_pr3_temperature_alm.fits \
    --lmax 2048 \
    --periods 255 256 137 139 \
    --n_surrogates 10000 \
    --output_dir out/exploratory_phase_scan
```

**Review results**:
```bash
cat out/exploratory_phase_scan/EXPLORATORY_PHASE_SCAN.md
```

**If candidate found** → Pre-register and run confirmatory test (see [RUNBOOK_PHASE_COHERENCE.md](RUNBOOK_PHASE_COHERENCE.md))

### Legacy Amplitude Comb Test

```bash
python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model ../data/planck_pr3/raw/COM_PowerSpect_CMB-TT-model_R3.01.txt \
    --variant C \
    --mc_samples 10000
```

---

## Channel Status Summary

### CLOSED Channels (NULL Results)
- ✅ **CMB TT power spectrum amplitude** (p ≈ 0.92) - See [CMB_TT_NEGATIVE_BENCHMARK.md](reports/CMB_TT_NEGATIVE_BENCHMARK.md)

### HIGH PRIORITY Open Channels
1. **CMB map-level phases** (a_ℓm phase coherence) ← **CURRENT FOCUS**
2. Atomic clock Allan deviation
3. Optical interferometer phase noise
4. Pulsar timing residuals
5. LIGO/Virgo GW waveform phases
6. CMB E-mode polarization phases

### MEDIUM Priority
7. CMB bispectrum
8. FRB arrival time statistics
9. Laser frequency comb stability
10. GPS satellite clock phase drift

See [SEARCH_SPACE.md](SEARCH_SPACE.md) for complete channel catalog.

---

## Workflow Decision Tree

```
START
  │
  ├─> Have CMB alm data? ──YES──> Run exploratory_phase_scan.py
  │                                  │
  │                                  ├─> All NULL? ──> Try different ℓ-range or observable
  │                                  │
  │                                  └─> CANDIDATE found?
  │                                         │
  │                                         └─> Create pre-registration
  │                                                │
  │                                                └─> Run confirmatory test
  │                                                       │
  │                                                       ├─> NULL? ──> Report NULL
  │                                                       │
  │                                                       └─> PASS?
  │                                                              │
  │                                                              └─> Run replication
  │                                                                     │
  │                                                                     ├─> Inconsistent? ──> Report NULL
  │                                                                     │
  │                                                                     └─> Consistent?
  │                                                                            │
  │                                                                            └─> Fill INTERPRETATION_NOTES.md
  │                                                                                   │
  │                                                                                   └─> Prepare publication
  │
  ├─> Have CMB power spectra? ──YES──> Run cmb_comb (legacy test)
  │                                       │
  │                                       └─> See RUNBOOK_REAL_DATA.md
  │
  └─> Want to explore search space? ──YES──> Read SEARCH_SPACE.md
                                                 │
                                                 └─> Identify high-priority channel
                                                        │
                                                        └─> Obtain data
                                                               │
                                                               └─> START
```

---

## Testing Philosophy

### Exploratory vs Confirmatory

| Aspect | Exploratory | Confirmatory |
|--------|-------------|--------------|
| **Goal** | Detect candidates | Validate signal |
| **Commitment** | Low | High |
| **Language** | "Candidate" | "PASS/NULL" |
| **Parameters** | Flexible | **LOCKED** |
| **Pre-registration** | No | **YES** |
| **Replication** | Not required | **REQUIRED** |
| **Publication** | Internal only | Court-grade |

### Significance Levels

| p-value | Exploratory | Confirmatory |
|---------|-------------|--------------|
| p ≥ 0.01 | NULL ⚪ | NULL ⚪ |
| 0.001 ≤ p < 0.01 | CANDIDATE 🟡 | PASS ✅ (if α=0.01) |
| p < 0.001 | STRONG CANDIDATE 🔴 | PASS ✅ |
| p < 2.9e-7 | VERY STRONG 🔴🔴 | STRONG PASS ✅✅ |

---

## Success Criteria

We can say:

> "We do not know where the fingerprint is, but we know:
> - Which channels we tested
> - How we tested them  
> - Which ones are CLOSED (NULL)
> - Which ones remain OPEN
> - The pipeline can run again in 6 months and produce identical results"

---

## Contributing

### Adding New Test Types

1. Create module in appropriate directory (e.g., `new_test/`)
2. Implement test with same structure:
   - Null model with surrogates
   - P-value computation
   - Metadata tracking
   - JSON + Markdown output

3. Add to SEARCH_SPACE.md
4. Create runbook (e.g., `RUNBOOK_NEW_TEST.md`)
5. Write unit tests in `tests/`

### Reporting Results

1. **Exploratory**: Save to `out/` (gitignored)
2. **Confirmatory NULL**: Create benchmark in `reports/`
3. **Confirmatory PASS**: Create detailed report in `reports/`, update SEARCH_SPACE.md

### Closing Channels

When a test yields NULL:

1. Create benchmark document (e.g., `CMB_TT_NEGATIVE_BENCHMARK.md`)
2. Update SEARCH_SPACE.md status to **CLOSED**
3. Add row to this index under "CLOSED Channels"
4. Do NOT re-test without new data or methods

---

## Data Provenance

### SHA-256 Validation

All confirmatory tests MUST validate data with SHA-256:

```bash
# Compute hash
sha256sum your_data_file.fits

# Store in pre-registration JSON
"alm_sha256": "a1b2c3d4e5f6..."

# Confirmatory runner verifies before running
```

### Manifests

Alternative to inline SHA-256: use manifest files:

```json
{
  "files": [
    {
      "filename": "planck_pr3_temperature_alm.fits",
      "path": "data/planck_pr3/alm/planck_pr3_temperature_alm.fits",
      "sha256": "a1b2c3d4e5f6...",
      "size": 12345678
    }
  ]
}
```

---

## References

### Core Papers
- Planck Collaboration (2020). "Planck 2018 results. I. Overview." *A&A* 641, A1.
- Bennett et al. (2013). "Nine-year WMAP Observations." *ApJS* 208, 20.

### Statistical Methods
- Pre-registration protocols in particle physics (PDG)
- Multiple-testing corrections (Bonferroni, max-statistic)
- Monte Carlo null models (surrogate data testing)

### UBT Theory
- See main repository documentation
- PRIORITY.md for author claims
- RESEARCH_PRIORITIES.md for current focus

---

## Version History

- **v1.0** (2026-01-12): Initial forensic fingerprint pipeline
  - Phase coherence exploratory and confirmatory tests
  - Pre-registration system
  - SEARCH_SPACE catalog
  - CMB TT benchmark (CLOSED)

---

## Support

**Questions?** 
- Check runbooks first: `RUNBOOK_*.md`
- Review SEARCH_SPACE.md for channel classification
- See test examples in `tests/`

**Found a bug?**
- Check unit tests: `pytest tests/ -v`
- Review error messages carefully
- Ensure data files are correct format

**Ready to publish results?**
- Ensure replication across ≥2 datasets
- Fill INTERPRETATION_NOTES.md
- Prepare both empirical and theoretical papers

---

**Last Updated**: 2026-01-12  
**Maintainer**: UBT Research Team
