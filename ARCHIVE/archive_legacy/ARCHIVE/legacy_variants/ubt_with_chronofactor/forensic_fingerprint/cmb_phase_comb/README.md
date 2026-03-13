# CMB Phase-Comb Test Module

Court-grade test for periodic phase-locking in CMB spherical harmonics.

## Overview

This module implements a **phase-based fingerprint test** that complements the existing TT power spectrum comb test by examining **phase coherence** in spherical harmonic coefficients a_ℓm.

### Key Difference from TT Spectrum Test

| Feature | TT Spectrum Test | Phase-Comb Test (This Module) |
|---------|------------------|-------------------------------|
| **Input** | C_ℓ power spectrum | HEALPix map → a_ℓm |
| **Measures** | Amplitude oscillations | Phase coherence |
| **Information** | |a_ℓm|² (averaged over m) | arg(a_ℓm) (phases) |
| **Null model** | ΛCDM synthetic | Phase-randomized preserving C_ℓ |

**Important**: These tests are **complementary**. A null in TT does NOT preclude a signal in phases.

## Module Structure

```
cmb_phase_comb/
├── __init__.py           # Module exports
├── phase_comb.py         # Core statistic + surrogates + p-values
├── io_healpix.py         # HEALPix map I/O (requires healpy)
├── nulls.py              # Phase randomization + validation
├── report.py             # JSON + Markdown output
├── plots.py              # Diagnostic plots
└── README.md             # This file
```

## Dependencies

**Required**:
- `numpy`, `scipy` (standard scientific Python)
- **`healpy`** - For HEALPix I/O and spherical harmonic transforms

**Optional**:
- `matplotlib` - For plotting
- `astropy` - For advanced FITS handling

Install healpy:
```bash
pip install healpy
```

## Quick Start

```python
from cmb_phase_comb import (
    load_healpix_map, 
    compute_alm,
    run_phase_comb_test,
)

# Load CMB map
map_data, mask, metadata = load_healpix_map(
    'path/to/planck_cmb_map.fits',
    mask_path='path/to/mask.fits'
)

# Compute spherical harmonics
alm = compute_alm(map_data, lmax=1500)

# Run phase-comb test
results = run_phase_comb_test(
    alm=alm,
    lmax=1500,
    ell_min=30,
    ell_max=1500,
    periods=[255, 256, 137, 139],  # Pre-registered
    n_mc_samples=10000,
    seed=42
)

# Check results
print(f"Best period: {results['best_period']}")
print(f"P-value: {results['best_p_value']:.6e}")
print(f"Significance: {results['significance']}")
```

## Pre-Registered Periods

Default periods (pre-registered, no look-elsewhere correction needed):
- **255, 256**: Reed-Solomon code related
- **137, 139**: Fine structure constant vicinity

## Theory

### Phase Coherence Statistic

For each period P:

```
R(P) = |⟨exp(i Δφ_ℓm(P))⟩|
```

where:
- Δφ_ℓm(P) = arg(a_{ℓ+P,m}) - arg(a_{ℓ,m})
- ⟨·⟩ denotes average over (ℓ,m) pairs

**Interpretation**:
- R(P) = 0: Random phases (no structure)
- R(P) > 0: Phase-locking detected

### Null Model

Phase-randomized surrogates preserving C_ℓ:

```
a'_ℓm = |a_ℓm| exp(i θ_ℓm)
```

where θ_ℓm ~ Uniform(0, 2π) with reality constraints:
- a_ℓ,0 is real (m=0 modes)
- a_ℓ,-m = (-1)^m conj(a_ℓm)

This preserves the power spectrum while destroying phase structure.

## Court-Grade Features

1. **Deterministic**: Fixed seed for reproducibility
2. **Pre-registered**: Fixed periods before data analysis
3. **Provenance**: Full metadata tracking
4. **Validation**: Sanity checks on surrogates
5. **Documentation**: Complete audit trail

## Documentation

- **Usage**: `forensic_fingerprint/RUNBOOK_PHASE_COMB.md`
- **Theory**: `forensic_fingerprint/reports/PHASE_COMB_TEST_PLAN.md`
- **One-command runner**: `forensic_fingerprint/run_real_data_cmb_phase_comb.py`

## Performance

Phase-comb test is computationally intensive:

**Typical runtime** (NSIDE=2048, lmax=1500):
- 10k surrogates: ~30 minutes
- 100k surrogates: ~5 hours

**Optimization**:
- Reduce lmax: `--alm_lmax 1000`
- Fewer surrogates: `--mc_samples 1000` (exploratory)
- Downgrade map: Use NSIDE=1024 or 512

## License

MIT License - See repository LICENSE file

## Author

UBT Research Team, 2026
