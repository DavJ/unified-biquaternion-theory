# Diagnostic Sub-segment Scan on Planck PR3 Residuals

This tool performs a detailed diagnostic analysis to test whether the detected period Δℓ = 16 in CMB residuals is a sub-harmonic of the predicted period Δℓ = 256 (Reed-Solomon code multiplex scaling).

## Purpose

The Unified Biquaternion Theory (UBT) predicts a periodic "comb" signature in CMB power spectrum residuals with period Δℓ = 256 (or 255 for RS(255,223) codes). Previous analysis detected a signal at Δℓ = 16. This tool investigates whether:

1. **Sub-harmonic relationship exists**: Is Δℓ = 16 a sub-harmonic of Δℓ = 256? (Yes: 256 = 16 × 16)
2. **Signal strength varies with multipole**: Does the periodic signal strength change across different multipole ranges?
3. **Phase drift is present**: Does the phase of the oscillation drift linearly with ℓ?

## Usage

### Basic Usage

```bash
python diagnostic_subsegment_scan.py \
    --planck_obs path/to/observed_spectrum.txt \
    --planck_model path/to/model_spectrum.txt
```

### Full Options

```bash
python diagnostic_subsegment_scan.py \
    --planck_obs DATA/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model DATA/planck_pr3/raw/model_lcdm.txt \
    --planck_cov DATA/planck_pr3/raw/covariance.dat \
    --ell_min 30 \
    --ell_max 1500 \
    --whiten_mode diagonal \
    --window_size 200 \
    --window_step 200 \
    --output_dir ./diagnostic_results
```

### Arguments

- `--planck_obs`: Path to Planck observed power spectrum file (required)
- `--planck_model`: Path to Planck model power spectrum file (required)
- `--planck_cov`: Path to covariance matrix (optional)
- `--ell_min`: Minimum multipole (default: 30)
- `--ell_max`: Maximum multipole (default: 1500)
- `--whiten_mode`: Whitening mode - `none`, `diagonal`, `covariance`, `cov_diag` (default: diagonal)
- `--window_size`: Window size for windowed analysis in multipoles (default: 200)
- `--window_step`: Step size for sliding windows (default: same as window_size)
- `--output_dir`: Output directory for JSON results (default: ./diagnostic_results)

## Analysis Components

### 1. Sub-harmonic Relationship Testing

Tests mathematical relationship between periods:
- **256 vs 16**: Tests if 256 = n × 16 for integer n (Answer: Yes, n=16)
- **255 vs 16**: Tests if 255 = n × 16 for integer n (Answer: No, 255/16 = 15.9375)

A sub-harmonic relationship indicates that the detected period may be a higher-order harmonic of the fundamental RS code period.

### 2. Period Strength Comparison (Full Range)

Computes Δχ² improvement for candidate periods:
- **Δℓ = 16**: Previously detected period
- **Δℓ = 255**: RS(255,223) code length
- **Δℓ = 256**: Predicted RS code period (2^8)

Reports:
- Δχ²: χ² improvement from adding sinusoid
- Amplitude: Best-fit amplitude of oscillation
- Phase: Best-fit phase offset

### 3. ℓ-Windowed Analysis

Divides multipole range into windows of specified size and tests period strength in each window.

**Purpose**: Detect if periodic signal:
- Is uniform across all multipoles
- Is stronger at low-ℓ (large angular scales)
- Is stronger at high-ℓ (small angular scales)
- Has localized peaks or gaps

**Output**:
- Window-by-window Δχ², amplitude, and χ²/dof
- Signal strength variation (standard deviation of Δχ² across windows)

### 4. Phase-Drift Analysis

Tests if the phase of the periodic oscillation drifts linearly with ℓ:

**Model without drift**: r_ℓ = A sin(2πℓ/Δℓ + φ)

**Model with drift**: r_ℓ = A sin(2πℓ/Δℓ + φ₀ + φ₁·ℓ)

Reports:
- Base amplitude A
- Initial phase φ₀
- Phase drift rate φ₁ (radians per multipole)
- χ² improvement from adding drift term
- F-statistic for significance test

**Interpretation**:
- F > 5: Phase drift is SIGNIFICANT
- F > 2: Phase drift is MARGINAL
- F < 2: Phase drift is NOT SIGNIFICANT

## Output

Results are saved as JSON with timestamp:
```
diagnostic_results/diagnostic_scan_20260113_123456.json
```

Structure:
```json
{
  "timestamp": "2026-01-13T12:34:56",
  "ell_range": [30, 1500],
  "n_multipoles": 1470,
  "whiten_mode": "diagonal",
  "chi2_per_dof_residuals": 1.04,
  "subharmonic_tests": {
    "256_vs_16": {
      "is_subharmonic": true,
      "harmonic_ratio": 16.0,
      "harmonic_order": 16,
      "relationship_desc": "256 = 16 × 16"
    },
    "255_vs_16": { ... }
  },
  "period_comparison": {
    "16": {"delta_chi2": 0.57, "amplitude": 0.028, "phase": 2.65},
    "255": {"delta_chi2": 97.41, "amplitude": 0.359, "phase": -0.16},
    "256": {"delta_chi2": 97.34, "amplitude": 0.359, "phase": -0.08}
  },
  "windowed_analysis": {
    "windows": [ ... ],
    "signal_strength_variation": 7.97
  },
  "phase_drift_analysis": {
    "amplitude": 0.362,
    "phase_0": 1.716,
    "phase_drift": 0.000017,
    "chi2_improvement": 0.0
  },
  "phase_drift_f_stat": 0.0
}
```

## Testing

Run the test suite to validate the implementation:

```bash
python test_diagnostic_scan.py
```

Tests include:
1. Sub-harmonic detection with known period pairs
2. Windowed analysis with synthetic decaying signal
3. Phase drift detection with synthetic drifting signal
4. Full integration test with synthetic CMB data

## Integration with Existing Tools

This tool builds on the existing `forensic_fingerprint` infrastructure:

- **Data loading**: Uses `loaders/planck.py` for consistent data handling
- **Residual computation**: Uses `cmb_comb/cmb_comb.py` functions
- **Whitening**: Supports same whitening modes as main CMB comb test
- **Provenance**: Compatible with existing JSON result format

## Interpretation Guidelines

### Sub-harmonic Detection

If 256 = n × 16 for integer n:
- **Positive interpretation**: Detected period is a higher-order harmonic
- **Implies**: Fundamental period may still be 256, but manifests as 16 in observations
- **Physical meaning**: RS code structure may have hierarchical sub-levels

### Signal Strength Variation

If signal varies significantly across windows:
- **Low-ℓ dominance**: May indicate large-scale cosmic structure
- **High-ℓ dominance**: May indicate small-scale physics
- **Uniform strength**: Suggests fundamental property independent of scale
- **Localized peaks**: May indicate specific physical transitions

### Phase Drift

If phase drift is significant (F > 5):
- **Physical interpretation**: Non-stationary periodicity
- **Could indicate**: Transition between period regimes
- **Could indicate**: Frequency chirp in quantum geometry
- **Could indicate**: Evolution of RS code parameters with scale

If no phase drift (F < 2):
- **Interpretation**: Period is stationary across multipole range
- **Supports**: Fundamental discrete architecture hypothesis
- **Implies**: Same RS code applies at all scales tested

## References

- **UBT Architecture Variants**: `forensic_fingerprint/ARCHITECTURE_VARIANTS.md`
- **CMB Comb Protocol**: `forensic_fingerprint/PROTOCOL.md`
- **Planck Data**: ESA Planck Legacy Archive (https://pla.esac.esa.int/)
- **RS Codes**: Reed-Solomon error correction codes, RS(255,223)

## License

MIT License - See repository LICENSE.md

## Author

UBT Research Team, January 2026
