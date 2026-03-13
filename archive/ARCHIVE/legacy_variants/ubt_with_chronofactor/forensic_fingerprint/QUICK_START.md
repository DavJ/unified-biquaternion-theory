# Quick Start Guide - UBT Forensic Fingerprints

Get started with the forensic fingerprint tests in 5 minutes.

## Installation

```bash
pip install numpy scipy matplotlib pytest
```

## Run Example (Synthetic Data)

```bash
cd forensic_fingerprint
python run_examples.py
```

This runs all three tests with synthetic data and saves outputs to `out/example_*/`.

## What Gets Created

```
out/
├── example_cmb/
│   ├── cmb_comb_results.txt
│   ├── residuals_with_fit.png
│   └── null_distribution.png
├── example_grid/
│   ├── grid_255_omega_b_h2_results.txt
│   ├── grid_255_omega_b_h2_distances.png
│   └── grid_255_omega_b_h2_null.png
└── example_invariance/
    ├── invariance_kappa_results.txt
    └── invariance_kappa_forest.png
```

## Interpreting Results

### Test #1: CMB Comb
Look at the p-value in `cmb_comb_results.txt`:
- **p ≥ 0.01**: No signal (expected for synthetic null data)
- **p < 0.01**: Candidate signal - requires replication
- **p < 2.9×10⁻⁷**: Strong signal (~5σ)

### Test #2: Grid 255
Look at p-values in `grid_255_*_results.txt`:
- **p ≥ 0.01**: No grid alignment (expected for smooth Gaussian)
- **p < 0.01**: Candidate quantization
- **p < 2.9×10⁻⁷**: Strong quantization

### Test #3: Invariance
Look at p-value in `invariance_*_results.txt`:
- **p > 0.05**: Datasets consistent (supports UBT)
- **p < 0.05**: Datasets inconsistent
- **p < 0.01**: Strong inconsistency (falsifies UBT)

Note: This test is "backwards" - high p-values are good!

## Next Steps

1. **Review outputs**: Check the generated text files and plots
2. **Read documentation**: See `PROTOCOL.md` for complete details
3. **Try real data**: Download Planck data and run on actual observations
4. **Run tests**: `pytest tests/test_forensic_fingerprint.py -v`

## Individual Tests

### CMB Comb Only
```bash
cd cmb_comb
# Need: observed.txt and model.txt with format: ell C_ell sigma_ell
python cmb_comb.py observed.txt model.txt ../out/
```

### Grid 255 Only
```bash
cd grid_255
# Need: chain.txt with MCMC samples (one parameter per column)
python grid_255.py chain.txt 0 ../out/
# 0 = test first column (parameter index)
```

### Invariance Only
```bash
cd invariance
# Edit main() to add your datasets
python invariance.py ../out/
```

## Troubleshooting

**"No module named pytest"**
```bash
pip install pytest
```

**"No module named scipy"**
```bash
pip install scipy
```

**"Matplotlib not available - skipping plots"**
```bash
pip install matplotlib
```

**Permission denied**
```bash
chmod +x run_examples.py
```

## Documentation

- **Full protocol**: `PROTOCOL.md`
- **Implementation details**: `IMPLEMENTATION_SUMMARY.md`
- **Main README**: `README.md`
- **LaTeX appendix**: `../speculative_extensions/appendices/appendix_F_fingerprint_protocol.tex`

## Testing

```bash
# Run automated test suite
cd ..
pytest tests/test_forensic_fingerprint.py -v

# Expected: 23 tests pass
```

## Support

- Open an issue on GitHub
- See `PROTOCOL.md` for detailed methodology
- Check individual test READMEs for specific usage

---

**Tip**: Start with `run_examples.py` to see all three tests in action, then move to real data analysis.
