#!/bin/bash
# Run all UBT channel selection experiments
# This script executes all analysis modules in sequence

set -e  # Exit on error

# Configuration
RANGE_MIN=100
RANGE_MAX=200
N_TRIALS=1000
LAMBDA=0.5
OUTPUT_DIR="results"

echo "======================================================================"
echo "UBT EXPERIMENTAL CHANNEL SELECTION - FULL ANALYSIS SUITE"
echo "======================================================================"
echo "Range: n ∈ [$RANGE_MIN, $RANGE_MAX]"
echo "Trials: $N_TRIALS"
echo "Lambda: $LAMBDA"
echo "Output directory: $OUTPUT_DIR"
echo ""

# Clean previous results (optional)
# rm -rf "$OUTPUT_DIR"

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "1/5: Running interference functional analysis..."
python3 interference_functional.py \
    --range $RANGE_MIN $RANGE_MAX \
    --output "$OUTPUT_DIR/interference_data.csv"

echo ""
echo "2/5: Running prime vs composite scan..."
python3 prime_vs_composite_scan.py \
    --range $RANGE_MIN $RANGE_MAX \
    --output "$OUTPUT_DIR"

echo ""
echo "3/5: Running Jacobi packet width analysis..."
python3 jacobi_packet_width_analysis.py \
    --centers 127 131 137 139 149 151 157 \
    --width 20 \
    --output "$OUTPUT_DIR/jacobi"

echo ""
echo "4/5: Running channel error model..."
python3 channel_error_model.py \
    --lambda $LAMBDA \
    --range $RANGE_MIN $RANGE_MAX \
    --output "$OUTPUT_DIR/channel"

echo ""
echo "5/5: Running devil's advocate falsification test..."
python3 devil_advocate_test.py \
    --target 137 \
    --range $RANGE_MIN $RANGE_MAX \
    --trials $N_TRIALS \
    --output "$OUTPUT_DIR/devil"

echo ""
echo "======================================================================"
echo "ANALYSIS COMPLETE"
echo "======================================================================"
echo "All results saved to: $OUTPUT_DIR/"
echo ""
echo "Summary of outputs:"
echo "  - Interference functional data: $OUTPUT_DIR/interference_data.csv"
echo "  - Prime vs composite plots: $OUTPUT_DIR/*.png"
echo "  - Ranking table: $OUTPUT_DIR/ranking.csv"
echo "  - Jacobi packet analysis: $OUTPUT_DIR/jacobi/"
echo "  - Channel error model: $OUTPUT_DIR/channel/"
echo "  - Falsification tests: $OUTPUT_DIR/devil/"
echo ""
echo "Review the plots and CSV files for detailed analysis."
