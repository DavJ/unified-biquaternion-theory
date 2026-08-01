<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# PRIME_MOD24_RESONANCE_EXPERIMENT

**Project root:** `projects/prime_mod24_resonance/`  
**Author:** Ing. David Jaroš  
**License:** MIT (code), CC BY-NC-ND 4.0 (theoretical content)

> **This is an experimental project. No physical interpretation is assumed.**

---

## Hypothesis

For every prime $p > 3$, the congruence

$$p^2 \equiv 1 \pmod{24}$$

holds exactly (since $p \equiv 1$ or $5 \pmod{6}$ implies $p^2 \equiv 1 \pmod{24}$).

The **k-sequence** is defined as:

$$k = \frac{p^2 - 1}{24} \in \mathbb{N}$$

This experiment investigates whether this sequence carries non-random structure
detectable via statistics, spectral analysis, and comparison with Riemann zeta zeros.

---

## Scripts

| Script | Description |
|--------|-------------|
| `prime_sequence.py` | Generates all primes up to N using a sieve, filters p > 3, computes k = (p²−1)//24, and saves a Parquet dataset with columns p, p_sq, k, log_p, gap_to_next. |
| `stats_analysis.py` | Loads the dataset and computes: k histogram, residues k mod {2,3,5,7,11,13} with chi² uniformity tests, autocorrelation of k, and Pearson correlations of k vs log(p) and k vs index. |
| `spectrum_analysis.py` | Z-scores and Hann-windows the k sequence, computes the FFT power spectrum, detects dominant peaks, and tests stability under 50%/25% subsampling and half-window. |
| `compare_zeta.py` | Loads the first n Riemann zeta zeros (via mpmath), compares FFT power spectra of k and the zeta imaginary parts, and computes cross-correlation with a shuffled null z-score. |
| `null_models.py` | Generates three null baselines (random primes-form, shuffled k, random quadratic) and compares their spectral statistics to the real k sequence across 50 realisations each. |

---

## How to Run

```bash
cd projects/prime_mod24_resonance

python prime_sequence.py
python stats_analysis.py
python spectrum_analysis.py
python compare_zeta.py
python null_models.py
```

All scripts read from `config.yaml` for defaults (N=100000, seed=42, fft_window=hann).

---

## Outputs

| Path | Description |
|------|-------------|
| `DATA/prime_mod24/primes_mod24.parquet` | Prime sequence dataset |
| `reports/prime_mod24/stats_summary.json` | Descriptive stats, mod-base chi², autocorrelation |
| `reports/prime_mod24/k_distribution.png` | k distribution and mod-base histograms |
| `reports/prime_mod24/k_autocorr.png` | k autocorrelation function |
| `reports/prime_mod24/fft_peaks.json` | FFT peaks and stability |
| `reports/prime_mod24/fft_spectrum.png` | FFT power spectra (full + subsamples) |
| `reports/prime_mod24/zeta_correlation.json` | Zeta-zero cross-correlation results |
| `reports/prime_mod24/zeta_fft_compare.png` | k vs zeta-zero spectral comparison |
| `reports/prime_mod24/null_comparison.json` | Null model baselines |
| `reports/prime_mod24/null_comparison.png` | Null model distributions |

---

## Requirements

```
numpy
scipy
pandas
pyarrow
mpmath
matplotlib
```

Install with: `pip install numpy scipy pandas pyarrow mpmath matplotlib`

---

## Rules

- Results must not be interpreted beyond the data.
- Null result (z < 2 everywhere) is a valid and valuable finding.
- All seeds are fixed for reproducibility.
- Do **not** modify files outside this project directory.
