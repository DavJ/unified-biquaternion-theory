# 2D FFT CMB Skew Test (Research Front)

Status: exploratory / hypothesis testing

Goal:
Test whether a small anisotropic tilt (~arctan(1/256)) is detectable
in 2D Fourier space of local CMB patches.

Important:
- This is NOT part of Core UBT.
- This test is not pre-registered.
- Any positive result requires independent replication and null tests.

Failure to detect the signal is a valid outcome.

## Files

- **cmb_2d_fft_poc.py**: Standalone proof-of-concept that generates synthetic test data.
  - No external data required
  - Dependencies: numpy, scipy, matplotlib only
  - Supports three modes: synthetic_grid, gaussian_field, injected
  - Run with `python research_front/cmb_2d_fft/cmb_2d_fft_poc.py --help` for options

- **cmb_2d_fft_planck.py**: Original version that requires Planck FITS maps.
  - Requires healpy, astropy, and Planck CMB data
  - For users who have access to real Planck data

## Usage

Default run (Gaussian null control):
```bash
python research_front/cmb_2d_fft/cmb_2d_fft_poc.py
```

Synthetic grid with tilt:
```bash
python research_front/cmb_2d_fft/cmb_2d_fft_poc.py --mode synthetic_grid
```

Injected signal test:
```bash
python research_front/cmb_2d_fft/cmb_2d_fft_poc.py --mode injected --snr 0.5
```

Custom parameters:
```bash
python research_front/cmb_2d_fft/cmb_2d_fft_poc.py --mode synthetic_grid --size 256 --tilt_deg 0.5 --seed 42
```

