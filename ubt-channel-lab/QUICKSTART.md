# Quick Start Guide - UBT Channel Stability Lab

## Prerequisites

```bash
# Install required Python packages
pip install numpy scipy pandas pyyaml matplotlib seaborn
```

## Running All Experiments (Recommended)

The easiest way to run the complete analysis pipeline:

```bash
cd ubt-channel-lab
./run_all_experiments.sh
```

This will:
1. Run all four stability criteria scans (S1-S4)
2. Perform bootstrap null testing
3. Generate visualizations
4. Aggregate results into a final ranking

**Results will be saved to `results/` directory.**

## Running Individual Experiments

### S1: Spectral Robustness
```bash
python experiments/spectral_scan.py --config configs/scan_config.yaml
```

### S2: Twin Prime Coherence
```bash
# Note: Requires S1 results to be generated first
python experiments/twin_prime_scan.py --config configs/scan_config.yaml
```

### S3: Energy Criterion
```bash
python experiments/energy_scan.py --config configs/scan_config.yaml
```

### S4: Information Criterion
```bash
python experiments/information_scan.py --config configs/scan_config.yaml
```

### Bootstrap Null Testing
```bash
# Requires S1, S3, S4 results to be generated first
python experiments/bootstrap_null.py --config configs/scan_config.yaml --n-bootstrap 10000
```

### Visualizations
```bash
# Requires all scans to be completed
python experiments/heatmap_visualization.py --config configs/scan_config.yaml
```

### Results Summary
```bash
# Requires all scans to be completed
python analysis/results_summary.py --config configs/scan_config.yaml
```

## Customizing Parameters

Edit `configs/scan_config.yaml` to modify:

- **Scan range**: Change `scan_range.min` and `scan_range.max`
- **Bootstrap iterations**: Change `bootstrap.n_iterations`
- **Significance level**: Change `statistics.significance_level`
- **Visualization settings**: Change `visualization` parameters

**Important**: Lock the configuration before running experiments to maintain blind protocol!

## Interpreting Results

### Key Output Files

1. **`results/final_summary_report.txt`** - Human-readable summary
2. **`results/combined_ranking.csv`** - Final ranking of all channels
3. **`results/s1_ranking.csv`** - S1 criterion results
4. **`results/s2_twin_prime_ranking.csv`** - Twin prime pair results
5. **`results/null_test_*_pvalues.csv`** - Statistical significance

### Visualizations

- **`s1_heatmap.png`** - Spectral robustness across channels
- **`s1_distribution.png`** - Prime vs non-prime comparison
- **`prime_vs_nonprime_comparison.png`** - Box plots for all criteria
- **`null_distributions.png`** - Bootstrap null distributions

## Example: Checking Channel 137

After running experiments, check the summary report:

```bash
cat results/final_summary_report.txt | grep -A 10 "CHANNEL 137"
```

Or examine the combined ranking:

```bash
grep "^.*,137," results/combined_ranking.csv
```

## Workflow for Paper Writing

1. Run all experiments: `./run_all_experiments.sh`
2. Review `results/final_summary_report.txt`
3. Copy key tables/figures to `paper/draft_channel_selection.tex`
4. Compile LaTeX: `cd paper && pdflatex draft_channel_selection.tex`

## Troubleshooting

**Q: Script says "S1 results not found"**  
A: Run `spectral_scan.py` first, as other scripts depend on it.

**Q: Matplotlib warnings about 'labels' parameter**  
A: These are deprecation warnings and can be safely ignored.

**Q: Results directory not found**  
A: The `results/` directory is created automatically. Check write permissions.

**Q: ImportError for numpy/scipy**  
A: Install dependencies: `pip install numpy scipy pandas pyyaml matplotlib seaborn`

## Notes on Blind Protocol

- **Pre-register** scan parameters in `scan_config.yaml` before running
- **Lock** the config file (set `blind_protocol.lock_config: true`)
- **Do not** modify parameters after seeing results
- **Report** all findings, including null results

## Contact

For questions about the theoretical framework, see main UBT repository documentation.
