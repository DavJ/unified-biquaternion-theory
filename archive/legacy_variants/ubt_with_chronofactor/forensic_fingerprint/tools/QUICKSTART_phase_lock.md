# Unified Phase-Lock Scan - Quick Reference

## What It Does

Measures phase synchronization (phase-lock) between CMB TT and BB channels to test UBT predictions.

## One-Line Summary

**UBT predicts**: TT (k≈137) and BB (k≈139) should be phase-locked if they're projections of a unified biquaternion field.

## Quick Start

### Minimal Run
```bash
python -m forensic_fingerprint.tools.unified_phase_lock_scan \
    --tt-map smica_tt.fits \
    --q-map smica_q.fits \
    --u-map smica_u.fits \
    --targets 137,139
```

### With Monte Carlo (Recommended)
```bash
python -m forensic_fingerprint.tools.unified_phase_lock_scan \
    --tt-map smica_tt.fits \
    --q-map smica_q.fits \
    --u-map smica_u.fits \
    --targets 137,139 \
    --mc 1000 \
    --report-csv results.csv \
    --plot results.png
```

### Production Run (Publication-Grade)
```bash
python -m forensic_fingerprint.tools.unified_phase_lock_scan \
    --tt-map smica_tt_2048.fits \
    --q-map smica_q_2048.fits \
    --u-map smica_u_2048.fits \
    --targets 137,139 \
    --nside-out 512 \
    --nlat 1024 \
    --nlon 2048 \
    --window-size 256 \
    --mc 5000 \
    --report-csv publication_results.csv \
    --dump-full-csv full_spectrum.csv \
    --plot diagnostic.png
```

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--targets K1,K2` | 137,139 | Target k frequencies |
| `--window-size W` | 128 | Segment size (W×W) |
| `--window FUNC` | none | Window function (use 'none' for UBT) |
| `--mc N` | 0 | Monte Carlo samples (0 = no MC) |
| `--nside-out N` | 256 | Map resolution |

## Understanding Output

### Phase Coherence (PC)
- **PC ≈ 1.0**: Perfect phase-lock (UBT supported)
- **PC ≈ 0.5**: Moderate coherence
- **PC ≈ 0.0**: Random phases (UBT not supported)

### Statistical Significance (with --mc)
- **p < 0.001**: *** Highly significant (strong evidence)
- **p < 0.01**: ** Significant (good evidence)
- **p < 0.05**: * Marginally significant
- **p ≥ 0.05**: Not significant

## Expected UBT Results

If UBT is correct, you should observe:

1. ✓ PC(137) > 0.5 and PC(139) > 0.5
2. ✓ p-values < 0.01 for both targets
3. ✓ Similar PC values for twin primes (137, 139)

## Troubleshooting

### Error: "healpy is required"
```bash
pip install healpy
```

### Error: "No module named matplotlib"
```bash
pip install matplotlib
```

### Slow performance
- Reduce `--nside-out` (e.g., 128 or 256)
- Reduce `--window-size` (e.g., 64)
- Reduce `--mc` samples (e.g., 100 for testing)

### Out of memory
- Reduce `--nlat` and `--nlon`
- Reduce `--nside-out`

## Files Generated

| File | Contains |
|------|----------|
| `results.csv` | PC values, p-values, Z-scores for targets |
| `full_spectrum.csv` | PC for all k (0 to k_max) |
| `diagnostic.png` | Plots: full spectrum + Jacobi cluster zoom |

## Theory Primer

According to UBT:
- **TT channel**: Represents scalar sector Θ̃_S of biquaternion field
- **BB channel**: Represents spinor sector Θ_V
- **Prediction**: Both sectors are coupled via D(∂μ,∂τ)Θ=0
- **Test**: If coupled, phases must be synchronized at resonant k

The phase-lock scan tests this prediction by measuring cross-channel phase coherence.

## Citation

If you use this tool in research, please cite the UBT repository and original papers.

## More Information

See full documentation: `README_unified_phase_lock_scan.md`
