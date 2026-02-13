# UBT CMB Spectral Forensic Analysis Tools

This directory contains tools for spectral forensic analysis of CMB (Cosmic Microwave Background) data to verify predictions of the Unified Biquaternion Theory (UBT).

## Overview

According to UBT, the universe's structure is a projection of an 8D toroidal substrate governed by a biquaternion field Θ. The theory predicts specific spectral signatures in CMB data:

- **Twin-prime resonances** at k=137 and k=139
- **Jacobi theta function structure** in the dispersive sector (TT channel)
- **Phase coherence** between temperature (TT) and polarization (BB) channels

## New Analysis Tools

### 1. `jacobi_cluster_fit.py` - Jacobi Theta Function Fitting

Fits Jacobi theta function θ₃ to the measured k-cluster (k=134-143) in CMB TT channel data.

**Theory:**
The dispersive imaginary scalar sector Θ̃_S evolves via:
```
∂_τ Θ̃_S = L_disp Θ̃_S
```
Solutions on the 8D torus are Jacobi theta functions:
```
θ₃(z, q) = Σ_{n=-∞}^{∞} q^{n²} exp(2πinz)
```
where q = exp(-D·τ), D is the diffusion coefficient, and τ is the dispersive evolution parameter.

**Usage:**
```bash
# First, generate radial spectrum from cmb_fft2d_scan.py
python -m forensic_fingerprint.tools.cmb_fft2d_scan \
    --tt-map data/planck_pr3_smica_tt.fits \
    --channels TT \
    --nside-out 256 --nlat 512 --nlon 1024 \
    --projection torus \
    --window2d none \
    --radial \
    --dump-radial-csv scans/tt_radial_spectrum.csv

# Then fit Jacobi theta function
python -m forensic_fingerprint.tools.jacobi_cluster_fit \
    --input scans/tt_radial_spectrum.csv \
    --channel TT \
    --k-min 134 --k-max 143 \
    --n-terms 50 \
    --output results/jacobi_fit_report.txt \
    --plot results/jacobi_fit.png
```

**Outputs:**
- Text report with fitted parameters: k₀, D, τ, amplitude
- Diagnostic plot showing data vs model
- Physical interpretation of diffusion coefficient

**Test:**
```bash
python forensic_fingerprint/tools/test_jacobi_cluster_fit.py
```

### 2. `cross_channel_phase_coherence.py` - Phase Coherence Analyzer

Analyzes phase coherence between TT and BB channels to test if they originate from a unified field.

**Theory:**
TT and BB channels represent different sectors of the unified biquaternion field Θ:
- TT: Dispersive imaginary scalar Θ̃_S (measures k=137 cluster)
- BB: Biquaternion/spinor sector Θ_V (measures k=139 peak)

If both are projections of a single field, they must exhibit non-random phase lock:
```
Γ(k₁,k₂) = |⟨exp(i(φ_TT(k₁) - φ_BB(k₂)))⟩|
```

**Usage:**
```bash
python -m forensic_fingerprint.tools.cross_channel_phase_coherence \
    --tt-map data/planck_pr3_smica_tt.fits \
    --q-map data/planck_pr3_smica_q.fits \
    --u-map data/planck_pr3_smica_u.fits \
    --k-tt 137 --k-bb 139 \
    --nside-out 256 --nlat 512 --nlon 1024 \
    --mc 1000 \
    --output results/phase_coherence_report.txt \
    --plot results/phase_coherence.png
```

**Outputs:**
- Text report with coherence metrics: Γ, mean phase difference, concentration
- Monte Carlo p-value testing significance
- Diagnostic plots: phase distributions, correlation, polar representation

**Test:**
```bash
python forensic_fingerprint/tools/test_cross_channel_phase_coherence.py
```

## Integration with Existing Tools

These tools integrate with the existing `cmb_fft2d_scan.py` workflow:

```bash
# 1. Run 2D FFT scan on TT and BB channels
python -m forensic_fingerprint.tools.cmb_fft2d_scan \
    --tt-map data/planck_pr3_smica_tt.fits \
    --q-map data/planck_pr3_smica_q.fits \
    --u-map data/planck_pr3_smica_u.fits \
    --channels TT,BB \
    --projection torus \
    --window2d none \
    --radial \
    --targets 137,139 \
    --mc 2000 \
    --dump-radial-csv scans/radial_dump.csv \
    --report-csv scans/targets_report.csv

# 2. Fit Jacobi theta to TT cluster
python -m forensic_fingerprint.tools.jacobi_cluster_fit \
    --input scans/radial_dump_TT.csv \
    --output results/jacobi_fit.txt \
    --plot results/jacobi_fit.png

# 3. Analyze cross-channel phase coherence
python -m forensic_fingerprint.tools.cross_channel_phase_coherence \
    --tt-map data/planck_pr3_smica_tt.fits \
    --q-map data/planck_pr3_smica_q.fits \
    --u-map data/planck_pr3_smica_u.fits \
    --k-tt 137 --k-bb 139 \
    --mc 1000 \
    --output results/phase_coherence.txt \
    --plot results/phase_coherence.png
```

## Theoretical Context

### Dispersive Evolution in Complex Time

UBT extends time to the complex plane: τ = t + iψ, where:
- t = real causal time
- ψ = imaginary dispersive parameter

The field Θ decomposes as:
```
Θ = Θ_S + Θ_V + i(Θ̃_S + Θ̃_V)
```

### Jacobi Analytics on 8D Torus

The dispersive sector evolves as:
```
Θ̃_S(θ, τ) = Σ_n c_n θ₃(n·θ, exp(-D·τ))
```

This structure emerges naturally from Feynman path integrals on the toroidal configuration space, where winding numbers n ∈ ℤ^N contribute terms that sum to θ₃.

### Experimental Predictions

1. **TT Channel (Dispersive Sector)**:
   - Broad cluster at k=134-143
   - Composite numbers (141, 142) show higher amplitude than twin primes
   - Jacobi theta function fit yields diffusion coefficient D

2. **BB Channel (Biquaternion Sector)**:
   - Sharp resonance at k=139
   - Lorentz-covariant spinor dynamics

3. **Cross-Channel Coherence**:
   - Non-random phase lock between TT(k=137) and BB(k=139)
   - Unified field hypothesis: both channels from same Θ
   - Phase coherence Γ ≈ 1 with p < 0.01

## References

- Main analysis script: `cmb_fft2d_scan.py`
- Paper: `papers/twin_prime_spectral_stability/twin_prime_spectral_stability.tex`
- Data: Planck PR3/PR4 SMICA maps
- Method: Toroidal projection + 2D FFT + radial averaging

## License

See repository LICENSE.md for licensing information.

---

**Contact**: David Jaroš  
**Repository**: DavJ/unified-biquaternion-theory
