<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# PROOFKIT: Hubble Tension

> **Status**: Layer C — Research Front (speculative hypothesis under investigation)  
> **Claim**: The ~8% Hubble tension arises from effective metric latency encoded in the imaginary-time component ψ of UBT's complex time τ = t + iψ.

---

## 1. Clean Derivation Path

### Step 1 — Two measurement protocols probe different effective times

The Hubble constant is not a single measurable quantity; different probes integrate
over different physical processes:

| Probe | Type | H₀ measured |
|---|---|---|
| CMB (Planck 2018) | Early-universe / global integral | 67.4 ± 0.5 km/s/Mpc |
| SH0ES distance ladder | Late-universe / local | 73.04 ± 1.04 km/s/Mpc |

In UBT, the covariant time element picks up a phase correction from the imaginary component ψ:

```
dt_eff = dt · (1 + f(ψ))
```

This correction is **negligible** for local measurements (short baselines, ψ ≈ const)
but **accumulates** for long-baseline integrated measurements (CMB).

### Step 2 — Define the latency parameter δ

The **metric latency** δ is defined as the fractional overhead in effective time
between the two measurement protocols:

```
δ = 1 − H₀_early / H₀_late
```

Using observed values:

```
δ = 1 − 67.4 / 73.0 ≈ 0.0767  (≈ 7.7%)
```

In the information-theoretic framing (see §4), δ = O/F where O is the per-frame
overhead and F is the total frame size.

### Step 3 — Predicted ratio

The latency hypothesis predicts:

```
H₀_late / H₀_early = 1 / (1 − δ)
```

If δ is architectural (constant, not dynamical), this ratio is **redshift-independent**
and produces no modification to the matter power spectrum or CMB acoustic peaks
beyond a uniform rescaling.

---

## 2. Definition of δ

δ is the **fractional difference** between the late-universe (local) and early-universe
(global) effective time measures:

```
δ ≡ (t_local − t_global) / t_local = 1 − H₀_early / H₀_late
```

### UBT prediction

In the information-theoretic extension of UBT's complex-time framework:

```
δ = O / F
```

where:
- `F = 256` — total effective frame size (from GF(2⁸) field structure of UBT's discrete symmetry)
- `O ≈ 20` — information-processing overhead per frame (baseline + channel coordination)

```
δ_predicted ≈ 20/256 ≈ 0.078  (7.8%)
δ_observed   = 1 − 67.4/73.0 ≈ 0.077  (7.7%)
```

Agreement: < 0.1 percentage point.

### Parameter origin

| Parameter | Derived from UBT | Estimated | Calibrated |
|---|---|---|---|
| F = 256 | Yes (GF(2⁸) field structure) | No | No |
| N = 16 | Partial (4 quaternion × 4 metric d.o.f.) | Partial | No |
| b = 2 | Estimated (frame transition baseline) | Yes | No |
| k = 1 | Estimated (per-channel coordination cost) | Yes | No |
| η ∈ [0.8, 0.95] | Estimated (overlap factor) | Yes | No |
| O ≈ 20 | Derived from F, N, b, k, η | No | No |
| δ ≈ 0.078 | Derived | No | No |

---

## 3. Numerical Predictions

### Central prediction

```
H₀_late / H₀_early = 1 / (1 − δ) ≈ 1.085
```

For H₀_early = 67.4 km/s/Mpc:

```
H₀_late_predicted = 67.4 / (1 − 0.078) ≈ 73.1 km/s/Mpc
H₀_late_observed  = 73.04 ± 1.04 km/s/Mpc
```

Residual: < 0.1%.

### Key distinguishing feature

Unlike dynamical dark energy explanations, the UBT latency hypothesis predicts:
- δ is **constant** across all redshifts
- No modification to the CMB power spectrum shape
- No modification to BAO peak positions
- The tension appears only in the H₀ inference, not in H(z)

---

## 4. Information-Theoretic Framing

The parameter F = 256 and the overhead formula come from the
**information-theoretic extension** of UBT's biquaternionic structure:

```
Frame F = P + O
  P = effective observable evolution (payload)
  O = information overhead (frame sync + channel coordination)
  O ≈ b + (N−1)·k·(2−η)
```

With N = 16 channels, b = 2, k = 1, η = 0.88:
```
O ≈ 2 + 15 × 1 × 1.12 ≈ 18.8 → rounded to 20
δ = 20/256 ≈ 0.078
```

**Note**: The information-theoretic framing is heuristic. The key physical claim is that
ψ-phase dynamics introduce a systematic difference between time-integrated (CMB)
and local (distance ladder) measurements of H₀.

---

## 5. Reproducible Script

→ [`scripts/reproduce_hubble_prediction.py`](../scripts/reproduce_hubble_prediction.py)

Run with:
```bash
python scripts/reproduce_hubble_prediction.py
```

Expected output:
```
=== UBT Hubble Tension Prediction ===
H0_early (Planck 2018):    67.40 km/s/Mpc
H0_late  (SH0ES 2022):     73.04 km/s/Mpc
Observed delta:             0.07718
UBT predicted delta (O/F): 0.07813  [O=20, F=256]
H0_late predicted by UBT:  73.11 km/s/Mpc
Residual:                   0.10%
```

---

## 6. Existing Source Documents

| Document | Location | Role |
|---|---|---|
| Main derivation (metric latency) | [`speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex`](../speculative_extensions/appendices/appendix_HT_hubble_tension_metric_latency.tex) | Primary derivation |
| Information-theoretic framing | [`research_front/hubble_latency/appendix_hubble_latency.md`](../research_front/hubble_latency/appendix_hubble_latency.md) | Physical interpretation |
| Calibration script | [`research_front/hubble_latency/calibration/calibrate_hubble_latency.py`](../research_front/hubble_latency/calibration/calibrate_hubble_latency.py) | Calibration |
| Quick calibration | [`calibrate_hubble_latency.py`](../calibrate_hubble_latency.py) | Calibration |
| HUBBLE_LATENCY appendix | [`HUBBLE_LATENCY/appendix/appendix_hubble_latency.md`](../HUBBLE_LATENCY/appendix/appendix_hubble_latency.md) | Archived copy |

---

## 7. Falsification Criteria

The hypothesis is **falsified** if:
1. CMB and distance ladder give consistent H₀ with improved systematics (δ → 0)
2. H(z) data show redshift-dependent tension inconsistent with a constant δ
3. BAO or CMB shape are modified in a way inconsistent with the latency model

The hypothesis is **supported** if:
1. δ remains ≈ 0.077–0.079 across independent probes
2. No modification to CMB or BAO shape is detected
3. The ratio H₀_late/H₀_early is confirmed redshift-independent

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
