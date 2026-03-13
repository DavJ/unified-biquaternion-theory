# Diagnostic Subsegment Scan - Quick Reference

## What It Does

Tests if the detected period Δℓ = 16 in CMB residuals is a sub-harmonic of the predicted Δℓ = 256 (Reed-Solomon code period).

## Quick Start

### Run Demonstration
```bash
cd forensic_fingerprint
python demo_diagnostic_scan.py
```

### Run Tests
```bash
python test_diagnostic_scan.py
```

### Analyze Real Data
```bash
python diagnostic_subsegment_scan.py \
  --planck_obs path/to/observed_spectrum.txt \
  --planck_model path/to/model_spectrum.txt \
  --output_dir ./results
```

## Key Results

### Sub-harmonic Relationship
- ✅ **256 = 16 × 16** (exact sub-harmonic)
- ❌ **255 ≠ n × 16** (not sub-harmonic, ratio = 15.9375)

### Analysis Outputs

1. **Period Strength**: Δχ², amplitude, phase for periods 16, 255, 256
2. **Windowed Analysis**: Signal strength in 200-multipole windows
3. **Phase Drift**: χ² improvement, F-statistic for drift significance

### Interpretation

**F-statistic thresholds:**
- F > 5: SIGNIFICANT phase drift
- F > 2: MARGINAL phase drift
- F < 2: NOT SIGNIFICANT

**Windowed analysis:**
- Signal variation indicates non-uniform distribution
- Can reveal scale-dependent physics

## Files

| File | Purpose | Lines |
|------|---------|-------|
| diagnostic_subsegment_scan.py | Main tool | 620 |
| test_diagnostic_scan.py | Tests | 260 |
| demo_diagnostic_scan.py | Demo | 240 |
| DIAGNOSTIC_SCAN_README.md | User guide | 230 |
| DIAGNOSTIC_SCAN_IMPLEMENTATION_SUMMARY.md | Technical docs | 350 |

## Example Output (Synthetic Demo)

```
Period Δℓ = 16:  Δχ² = 52.63,  A = 0.268
Period Δℓ = 255: Δχ² = 884.67, A = 1.088
Period Δℓ = 256: Δχ² = 884.38, A = 1.088

Windowed analysis: 8 windows, variation = 86.31
Phase drift: F = 54.34 → SIGNIFICANT
```

## Status

✅ All features implemented  
✅ All tests passing  
✅ Ready for real Planck PR3 data

## Documentation

- User guide: `DIAGNOSTIC_SCAN_README.md`
- Technical summary: `DIAGNOSTIC_SCAN_IMPLEMENTATION_SUMMARY.md`
- Code documentation: See function docstrings in Python files
