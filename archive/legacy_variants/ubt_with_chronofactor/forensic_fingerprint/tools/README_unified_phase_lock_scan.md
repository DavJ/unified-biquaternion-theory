# Unified Phase-Lock Scan Tool

## Overview

The **Unified Phase-Lock Scan** is a tool for verifying phase synchronization between TT (temperature) and BB (B-mode polarization) channels in CMB data, as predicted by the Unified Biquaternion Theory (UBT).

## Theoretical Background

According to UBT, the cosmic microwave background represents projections of a unified biquaternion field Θ defined over complex time τ = t + iψ:

```
D(∂μ, ∂τ)Θ = 0
```

The field has scalar and spinor components:
- **TT channel (k≈137)**: Dispersive imaginary scalar sector Θ̃_S (Jacobi cluster 134-143)
- **BB channel (k≈139)**: Biquaternion vector/spinor sector Θ_V

If both channels are projections of a single unified field, they must exhibit **non-random phase relationships** (phase-lock) at their respective resonances.

## Method

The phase-lock scan implements a segment-based cross-channel coherence analysis:

1. **Segmentation**: Divide toroidal projection into N identical W×W windows with stride=W/2 (Welch method)
2. **FFT**: Compute 2D FFT for both TT and BB channels in each window
3. **Cross-Spectrum**: For each segment and frequency k, compute normalized cross-spectrum:
   ```
   S_xy = (X * Y*) / (|X| * |Y|)
   ```
   This extracts the pure phase relationship between channels.

4. **Phase Coherence (PC)**: Accumulate phasors across all segments:
   ```
   PC(k) = |⟨S_xy⟩| ∈ [0, 1]
   ```
   - PC = 1.0 means perfect phase lock (all segments coherent)
   - PC = 0.0 means total phase chaos (random phases)

5. **Monte Carlo Validation**: Test significance via phase-shuffle null model

## Installation

Requires:
- Python 3.7+
- numpy
- healpy
- matplotlib (optional, for plots)

```bash
pip install numpy healpy matplotlib
```

## Usage

### Basic Usage

```bash
python -m forensic_fingerprint.tools.unified_phase_lock_scan \
    --tt-map data/planck_pr3_tt.fits \
    --q-map data/planck_pr3_q.fits \
    --u-map data/planck_pr3_u.fits \
    --targets 137,139 \
    --report-csv results/phase_lock.csv
```

### With Monte Carlo Validation

```bash
python -m forensic_fingerprint.tools.unified_phase_lock_scan \
    --tt-map data/planck_pr3_tt.fits \
    --q-map data/planck_pr3_q.fits \
    --u-map data/planck_pr3_u.fits \
    --targets 137,139 \
    --window-size 128 \
    --window none \
    --mc 1000 \
    --null phase-shuffle \
    --report-csv results/phase_lock_mc.csv \
    --plot results/phase_lock_mc.png
```

### Full Spectrum Analysis

```bash
python -m forensic_fingerprint.tools.unified_phase_lock_scan \
    --tt-map data/planck_pr3_tt.fits \
    --q-map data/planck_pr3_q.fits \
    --u-map data/planck_pr3_u.fits \
    --targets 137,139 \
    --window-size 128 \
    --mc 2000 \
    --dump-full-csv results/full_spectrum.csv \
    --plot results/phase_lock_full.png
```

## Command-Line Options

### Input Maps
- `--tt-map PATH`: HEALPix FITS file for TT (temperature) channel [required]
- `--q-map PATH`: HEALPix FITS file for Q polarization [required]
- `--u-map PATH`: HEALPix FITS file for U polarization [required]

### Target Frequencies
- `--targets K1,K2,...`: Comma-separated target k values (default: 137,139)

### Map Processing
- `--nside-out N`: Degrade maps to this NSIDE (default: 256)
- `--lmax-alm N`: lmax for E/B decomposition (default: 512)
- `--nlat N`: Grid height for projection (default: 512)
- `--nlon N`: Grid width for projection (default: 1024)
- `--projection TYPE`: Projection type: lonlat|torus (default: torus)

### Segmentation
- `--window-size W`: Segment window size W×W (default: 128)
- `--stride S`: Window stride (default: W/2 for Welch overlap)
- `--window FUNC`: Window function: none|hann|hamming (default: none)

**Note**: The default `--window none` is used for initial analyses. Sensitivity to different windowing functions should be tested to assess robustness of results.

### Monte Carlo
- `--mc N`: Number of Monte Carlo samples (default: 0, no MC)
- `--null METHOD`: Null model: phase-shuffle|phi-roll|segment-permute (default: phase-shuffle)
- `--pvalue-mode MODE`: P-value computation: local|maxstat|fdr (default: local)
- `--k-range KMIN,KMAX`: K range for full spectrum and maxstat (e.g., 130,150)
- `--pair-mode`: Enable pair metrics (harmonic mean PC for pairs)
- `--seed N`: Random seed (default: 0)

### Output
- `--report-csv PATH`: Output CSV for target results
- `--plot PATH`: Output PNG for diagnostic plot
- `--dump-full-csv PATH`: Output CSV with full spectrum (all k values)

## Output Files

### Multiple Testing Correction

When testing multiple target frequencies, the risk of false positives increases. Three p-value modes are available:

1. **Local (pointwise)**: Tests each k independently. P(null[k] >= observed[k])
   - Simple but doesn't account for multiple comparisons
   - Use when testing a single pre-specified frequency

2. **Maxstat**: Accounts for "look-elsewhere" effect across k-range
   - P(max_null[k_range] >= observed[k])
   - More conservative than local p-values
   - Recommended when scanning a frequency range

3. **FDR (Benjamini-Hochberg)**: Controls false discovery rate
   - Adjusts p-values to limit expected proportion of false positives
   - Balances power and false positive control
   - Recommended when testing multiple pre-specified targets

**Recommendation**: Always report both local and corrected p-values. Use maxstat or FDR when testing multiple frequencies.

### Target Results CSV

Contains phase coherence results for specified target k values:

```csv
k_target,phase_coherence,mc_mean,mc_std,z_score,p_value,window_size,stride,window_func,projection,mc_samples
137,0.734521,0.123456,0.045678,13.37,0.000012,128,64,none,torus,1000
139,0.689234,0.119876,0.043210,13.18,0.000015,128,64,none,torus,1000
```

### Full Spectrum CSV

Contains PC values for all k from 0 to k_max:

```csv
k,phase_coherence
0,0.012345
1,0.023456
2,0.034567
...
137,0.734521
...
```

### Diagnostic Plot

The PNG output shows:
1. Full spectrum: PC vs k for entire range
2. Zoom view: Jacobi cluster region with target annotations

## Interpretation

### Phase Coherence Values
- **PC > 0.7**: Strong phase-lock, suggests unified field structure
- **PC 0.3-0.7**: Moderate coherence, may indicate partial coupling
- **PC < 0.3**: Weak coherence, consistent with independent fields

### Statistical Significance
With Monte Carlo validation:
- **p < 0.001**: Highly significant (***), strong evidence for phase-lock
- **p < 0.01**: Significant (**), good evidence
- **p < 0.05**: Marginally significant (*), weak evidence
- **p ≥ 0.05**: Not significant, no evidence for phase-lock

### UBT Prediction

According to UBT, if the universe is a "biquaternion machine", the phase difference between TT and BB at k=137/139 should NOT be random. Specifically:

- Expected: PC(137) and PC(139) significantly higher than null baseline
- Expected: p-values < 0.001 for both target frequencies
- Expected: Similar PC values for twin-prime pair (137, 139)

## Technical Notes

### Why Toroidal Projection?

The `--projection torus` option enforces 2D periodicity by mirroring the latitude axis. This is theoretically motivated by UBT's 8D toroidal substrate structure.

### Why No Windowing?

The `--window none` default is critical. UBT predicts that phase information is encoded at sector boundaries (transitions between Θ_V and Θ̃_S). Standard window functions (Hann, Hamming) suppress edge information, masking these transitions.

### Welch Method Overlap

The default stride=W/2 provides 50% overlap between windows (Welch method), which:
- Increases statistical robustness
- Reduces variance in spectral estimates
- Captures phase information across segment boundaries

## Examples

### Example 1: Quick Check

```bash
python -m forensic_fingerprint.tools.unified_phase_lock_scan \
    --tt-map smica_tt_256.fits \
    --q-map smica_q_256.fits \
    --u-map smica_u_256.fits \
    --targets 137,139 \
    --window-size 64 \
    --report-csv quick_check.csv
```

### Example 2: Analysis with Multiple Testing Correction

```bash
python -m forensic_fingerprint.tools.unified_phase_lock_scan \
    --tt-map planck_smica_iqu_2048.fits \
    --q-map planck_smica_iqu_2048.fits \
    --u-map planck_smica_iqu_2048.fits \
    --targets 137,139 \
    --k-range 130,150 \
    --nside-out 512 \
    --nlat 1024 \
    --nlon 2048 \
    --window-size 256 \
    --window none \
    --mc 5000 \
    --null phase-shuffle \
    --pvalue-mode maxstat \
    --seed 42 \
    --report-csv analysis/phase_lock_maxstat.csv \
    --dump-full-csv analysis/full_spectrum.csv \
    --plot analysis/phase_lock_diagnostic.png
```

## Testing

Run the basic test suite:

```bash
python test_phase_lock_basic.py
```

Expected output:
```
✓ ALL TESTS PASSED
```

## References

- Unified Biquaternion Theory: See repository `THEORY/` directory
- Planck PR3 data: https://pla.esac.esa.int/
- Jacobi cluster analysis: See `FINGERPRINTS/candidate/`

## License

See repository LICENSE.md

## Author

UBT Team (implementation of David Jaroš's theoretical framework)
