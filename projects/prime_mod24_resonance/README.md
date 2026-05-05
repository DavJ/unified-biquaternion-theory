# PRIME_MOD24_RESONANCE_EXPERIMENT

**Project root:** `projects/prime_mod24_resonance/`  
**Author:** Ing. David Jaroš  
**License:** MIT (code), CC BY-NC-ND 4.0 (theoretical content)

---

## Hypothesis

For every prime $p > 3$, the identity

$$k = \frac{p^2 - 1}{24} \in \mathbb{N}$$

holds exactly (since $p \equiv 1$ or $5 \pmod{6}$ implies $p^2 \equiv 1 \pmod{24}$).

This experiment investigates whether the **sequence of these $k$ values** carries
non-random structure detectable via:

- Statistical analysis (mod-base residues, autocorrelation, correlations)
- FFT spectral analysis (dominant frequencies, stability)
- Comparison with Riemann zeta zero imaginary parts
- Quadratic phase signal comparison
- CMB radial power spectrum alignment

---

## Pipeline (run in order)

```bash
cd projects/prime_mod24_resonance

# 1. Generate data
python prime_sequence.py --n 1e6

# 2. Statistical analysis
python stats_analysis.py

# 3. FFT spectral analysis
python spectrum_analysis.py

# 4. Compare with Riemann zeta zeros
python compare_zeta.py --n-zeros 500

# 5. Quadratic structure test
python quadratic_test.py --n 5000

# 6. CMB prime-mod24 probe (synthetic CMB)
python forensic_fingerprint/tools/cmb_fft2d_scan.py \
    --prime-mod24-probe --synthetic --n-primes 500 \
    --probe-report-csv reports/cmb_prime_mod24_hits.csv \
    --probe-plot plots/cmb_prime_overlay.png

# 7. Null models
python null_models.py --seed 42
```

---

## Outputs

| Path | Description |
|------|-------------|
| `data/primes_mod24.parquet` | Prime sequence dataset |
| `reports/stats_summary.json` | Descriptive stats, mod-base chi², autocorrelation |
| `reports/fft_peaks.json` | FFT peaks and stability |
| `reports/zeta_correlation.json` | Zeta-zero cross-correlation results |
| `reports/quadratic_similarity.json` | Quadratic signal comparison metrics |
| `reports/cmb_prime_mod24_hits.csv` | Per-bin CMB hit density |
| `reports/null_comparison.json` | Null model baselines |
| `plots/k_distribution.png` | k distribution and mod-base histograms |
| `plots/k_autocorrelation.png` | k autocorrelation function |
| `plots/fft_spectrum.png` | FFT power spectra (full + subsamples) |
| `plots/zeta_vs_k_fft.png` | k vs zeta-zero spectral comparison |
| `plots/quadratic_overlay.png` | k vs synthetic quadratic signals |
| `plots/cmb_prime_overlay.png` | CMB probe results |
| `plots/null_comparison.png` | Null model distributions |
| `report.md` | Final consolidated report (fill in after run) |

---

## Requirements

```
numpy
scipy
pandas
pyarrow
mpmath
matplotlib
sympy    # optional, used for prime checking
```

Install with:  `pip install numpy scipy pandas pyarrow mpmath matplotlib sympy`

---

## Rules

- Results must not be interpreted beyond the data.
- Null result (z < 2 everywhere) is a valid and valuable finding.
- All seeds are fixed for reproducibility.
- Do **not** modify files outside this project directory.
