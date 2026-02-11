# Carrier-137 Prime-Gated Results (Planck PR3 / SMICA 2048) — Synthesis

## Scope
This note summarizes a series of “prime-gated” tests performed with
`forensic_fingerprint.tools.spectral_parity_test` on Planck PR3 SMICA 2048 full-sky maps.
The goal is to compare a per-ℓ “Hamming purity” proxy between prime multipoles (P) and composite multipoles (C)
within selected ℓ-windows, with two complementary null models:

1) **Permutation null (label shuffling):** randomizes the prime/composite assignment across ℓ values in-window.
2) **Phase-randomization MC null:** randomizes phases per-ℓ while preserving |a_{ℓm}|, then repeats the same statistic.

We report Δmean(P−C) = mean(purity | ℓ prime) − mean(purity | ℓ composite), with two-sided p-values.

**Important:** A small p-value under the permutation null does not automatically imply significance under the
phase-randomization null; these nulls test different hypotheses.

## Data & inputs
- Map: `data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits`
- Extracted Q/U (field=1/2) written to:
  - `data/planck_pr3/maps/extracted/SMICA_Q.fits`
  - `data/planck_pr3/maps/extracted/SMICA_U.fits`
- E/B derived from Q/U via `healpy.map2alm_spin`, then analyzed as EE and BB.

Common runtime parameters in the runs below:
- `--step 255` (near non-overlapping framing)
- `--max-frames 2048` (or 4096 for the narrower window)
- Prime-gated enabled: `--prime-gated`
- Prime permutation samples: typically 20k–30k

## Key result: BB is locally prime-biased near ℓ≈137 under permutation null

### Window A: ℓ ∈ [128, 146] (narrow “core”)
Run:
`scans/E_carrier_137_128_146` (TT map + Q/U → EE/BB), with `mc=2000`, `prime-perm=30000`, `max-frames=4096`.

Prime-gated (Real):
- TT: Δ = −0.01143, perm p = 0.342
- EE: Δ = +0.00441, perm p = 0.615
- **BB: Δ = +0.01546, perm p = 0.0485**

Phase-randomization MC (Prime-gated null):
- TT: mc p = 0.317
- EE: mc p = 0.696
- **BB: mc p = 0.156** (two-sided)

Interpretation:
- In this narrow window, BB shows a consistent positive Δ (prime multipoles slightly “cleaner” than composite)
  at the ~1–1.5% level, which is **borderline-significant under the permutation null**.
- The same Δ is **not significant under the phase-randomization MC null** for this run (p≈0.156).

### Window B: ℓ ∈ [124, 154] (shifted, wider)
Prime-gated (Real):
- BB: Δ = +0.01141, perm p = 0.0397
Phase-randomization MC (Prime-gated null):
- BB: mc p = 0.167

Interpretation:
- The BB sign (Δ>0) persists after shifting the window,
  but significance is weaker vs the phase-randomization null.

### Window C: ℓ ∈ [120, 150] (original)
Prime-gated (Real):
- BB: Δ ≈ +0.01496, perm p ≈ 0.0131
Phase-randomization MC (Prime-gated null):
- BB: mc p ≈ 0.0799

Interpretation:
- This window gives the strongest permutation p-value for BB, but MC support remains moderate.

## Negative control (“Void”)
### Window V: ℓ ∈ [200, 218]
Prime-gated (Real):
- **BB: Δ = −0.00367, perm p = 0.792**

Interpretation:
- No evidence of a BB prime–composite split in this control window.
- This argues against a simple global prime/composite bias in the estimator.

## Current status (conservative summary)
Across multiple windows around ℓ≈137, BB exhibits:
- **Stable sign** (Δ>0 near 137, Δ≈0 in the void window),
- **Small magnitude** (Δ ~ 0.011–0.015),
- **Permutation-null significance** in some windows (p < 0.05),
- **Weaker support under the phase-randomization MC null** (typically p ~ 0.08–0.17 so far).

Thus, the result should be treated as a **localized candidate anomaly** rather than a definitive discovery.
The most critical open question is whether a physically motivated null (phase-randomization) can be rejected
in a robust, window-stable way.

## Pre-registered follow-ups
1) **Far control band** (e.g., ℓ ∈ [400, 430]) to further test locality.
2) **Harmonic test** (hypothesis-driven, not window-tuned):
   - First harmonic window around 2×137 ≈ 274, e.g. ℓ ∈ [265, 283]
   - Evaluate BB Δ and p-values under both null models.
3) Replication on alternative component-separated maps (if available in-repo):
   - NILC / SEVEM / Commander (same analysis pipeline).

## Notes on interpretation
- A permutation p-value (prime/composite label shuffle) tests whether the observed prime-vs-composite split
  is unusual given the set of ℓ values in the window.
- Phase-randomization MC tests a stronger null that preserves the power spectrum per ℓ and scrambles phases;
  it is closer to “random field with the same spectrum” and may be more physically relevant.
- Claims should be phrased accordingly: “permutation-significant but not phase-randomization-significant yet”.

## References (internal)
- Scripts: `forensic_fingerprint/tools/spectral_parity_test.py`
- Output plots: `scans/E_carrier_137_*` and `scans/BB_VOID_*`

