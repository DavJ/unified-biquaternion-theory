#!/bin/bash
# UBT Channel Lab - Complete Workflow Runner
# This script runs all experiments in the correct order

set -e  # Exit on error

echo "=================================="
echo "UBT Channel Stability Lab"
echo "Complete Workflow Runner"
echo "=================================="
echo ""

CONFIG="configs/scan_config.yaml"

# Check if config exists
if [ ! -f "$CONFIG" ]; then
    echo "Error: Config file not found at $CONFIG"
    exit 1
fi

# Create results directory if it doesn't exist
mkdir -p results

echo "Step 1/7: Running S1 (Spectral Robustness) scan..."
python experiments/spectral_scan.py --config "$CONFIG"
echo ""

echo "Step 2/7: Running S3 (Energy Criterion) scan..."
python experiments/energy_scan.py --config "$CONFIG"
echo ""

echo "Step 3/7: Running S4 (Information Criterion) scan..."
python experiments/information_scan.py --config "$CONFIG"
echo ""

echo "Step 4/7: Running S2 (Twin Prime Coherence) scan..."
python experiments/twin_prime_scan.py --config "$CONFIG"
echo ""

echo "Step 5/7: Running Bootstrap Null Testing..."
echo "(Using reduced sample size for quick testing, modify --n-bootstrap for full analysis)"
python experiments/bootstrap_null.py --config "$CONFIG" --n-bootstrap 1000
echo ""

echo "Step 6/7: Generating Visualizations..."
python experiments/heatmap_visualization.py --config "$CONFIG"
echo ""

echo "Step 7/7: Aggregating Results..."
python analysis/results_summary.py --config "$CONFIG"
echo ""

echo "=================================="
echo "Workflow Complete!"
echo "=================================="
echo ""
echo "Generated outputs in results/:"
echo "  - s1_ranking.csv (Spectral robustness)"
echo "  - s2_twin_prime_ranking.csv (Twin prime coherence)"
echo "  - s3_energy_ranking.csv (Energy criterion)"
echo "  - s4_information_ranking.csv (Information criterion)"
echo "  - null_test_*_pvalues.csv (Statistical significance)"
echo "  - combined_ranking.csv (Final unified ranking)"
echo "  - final_summary_report.txt (Summary report)"
echo "  - *.png (Visualizations)"
echo ""
echo "Next steps:"
echo "  1. Review results/final_summary_report.txt"
echo "  2. Examine visualizations in results/"
echo "  3. Check statistical significance in null_test_*_pvalues.csv"
echo "  4. Update paper/draft_channel_selection.tex with findings"
echo ""
