# UBT Experimental Channel Selection - Usage Guide

## Quick Start

### 1. Installation

```bash
# Navigate to the channel_selection directory
cd EXPERIMENTS/channel_selection/

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Individual Modules

#### Interference Functional Analysis
```bash
python3 interference_functional.py --range 100 200
python3 interference_functional.py --range 100 200 --output results/interference.csv
```

#### Prime vs Composite Scan
```bash
python3 prime_vs_composite_scan.py --range 100 200 --output results/
```

#### Jacobi Packet Width Analysis
```bash
# Single center
python3 jacobi_packet_width_analysis.py --center 137 --width 20

# Multiple centers
python3 jacobi_packet_width_analysis.py --centers 131 137 139 149 --width 20 --output results/jacobi/
```

#### Channel Error Model
```bash
python3 channel_error_model.py --lambda 0.5 --range 100 200 --output results/channel/
```

#### Devil's Advocate Test
```bash
python3 devil_advocate_test.py --target 137 --range 100 200 --trials 1000 --output results/devil/
```

### 3. Run Complete Analysis Suite

```bash
# Run all experiments
./run_all_experiments.sh

# Or with custom parameters
bash run_all_experiments.sh
```

## Detailed Usage

### Interference Functional

**Purpose**: Compute I(n) = aliasing(n) + overlap(n) to measure mode stability.

**Options**:
- `--range MIN MAX`: Range of modes to evaluate (default: 100 200)
- `--output FILE`: Output CSV file path

**Example**:
```bash
# Analyze modes 50-300
python3 interference_functional.py --range 50 300 --output wide_scan.csv
```

### Prime vs Composite Scan

**Purpose**: Systematically compare spectral stability of primes vs composites.

**Options**:
- `--range MIN MAX`: Range of modes (default: 100 200)
- `--output DIR`: Output directory (default: results)

**Outputs**:
- `interference_data.csv`: Raw I(n) values
- `ranking.csv`: Modes ranked by I(n)
- `interference_landscape.png`: Plot of I(n) vs n
- `prime_composite_distributions.png`: Statistical comparison

**Example**:
```bash
python3 prime_vs_composite_scan.py --range 130 160 --output focused_scan/
```

### Jacobi Packet Width Analysis

**Purpose**: Analyze theta function dispersion around specific modes.

**Options**:
- `--center N`: Single center mode (default: 137)
- `--centers N1 N2 ...`: Multiple centers
- `--width W`: Scan width around center (default: 20)
- `--output DIR`: Output directory

**Outputs**:
- `packet_width_nXXX.png`: Plot for each center
- `packet_widths.csv`: Summary statistics

**Example**:
```bash
# Analyze twin primes
python3 jacobi_packet_width_analysis.py --centers 137 139 --width 15
```

### Channel Error Model

**Purpose**: Model Layer 2 as information channel with error-dependent cost.

**Options**:
- `--lambda LAMBDA`: Weight for error rate in F(n) = I(n) + λ·error (default: 0.5)
- `--range MIN MAX`: Mode range (default: 100 200)
- `--output DIR`: Output directory

**Outputs**:
- `channel_model_lambdaX.XX.csv`: F(n) values
- `cost_functional_lambdaX.XX.png`: Cost landscape plot

**Example**:
```bash
# Test different lambda values
python3 channel_error_model.py --lambda 0.2 --range 100 200 --output channel_lambda02/
python3 channel_error_model.py --lambda 0.8 --range 100 200 --output channel_lambda08/
```

### Devil's Advocate Test

**Purpose**: Attempt to falsify the hypothesis that n=137 is special.

**Options**:
- `--target N`: Mode to test (default: 137)
- `--range MIN MAX`: Mode range (default: 100 200)
- `--trials N`: Number of randomization trials (default: 1000)
- `--output DIR`: Output directory

**Outputs**:
- `falsification_test_nXXX.csv`: Test statistics
- `falsification_distributions_nXXX.png`: Permutation and MC distributions

**Example**:
```bash
# Test n=139 with 5000 trials
python3 devil_advocate_test.py --target 139 --range 100 200 --trials 5000
```

## Interpreting Results

### Interference Functional I(n)

- **Lower values** = more stable modes
- **I(n) = 0** for primes (no divisors → no harmonic overlap)
- **Higher values** for composites with many divisors

### Prime vs Composite Statistics

- **Effect size (Cohen's d)**:
  - d < 0.2: negligible
  - 0.2 ≤ d < 0.5: small
  - 0.5 ≤ d < 0.8: medium
  - d ≥ 0.8: large

### Jacobi Packet Width

- **σ (sigma)**: Gaussian width parameter
- **FWHM**: Full width at half maximum
- **Narrower packets** may indicate more localized energy

### Channel Error Model

- **F(n)**: Total cost functional
- **Stability region**: Top 25th percentile (lowest F(n))
- **Lower error rate** = more reliable channel

### Falsification Score

- **0.0-0.2**: Hypothesis NOT falsified (mode is special)
- **0.2-0.4**: Weak evidence
- **0.4-0.6**: Ambiguous
- **0.6-1.0**: Hypothesis FALSIFIED (mode is random)

### P-values

- **p < 0.01**: Strong evidence against randomness
- **p < 0.05**: Moderate evidence
- **p < 0.10**: Weak evidence
- **p ≥ 0.10**: No significant evidence

## Analysis Requirements

Following the project constraints, all analyses:

✅ **Do NOT**:
- Modify core UBT theory
- Reinterpret existing results
- Privilege mode 137 a priori

✅ **Always**:
- Compare against neighboring values
- Report global AND local minima
- Use statistical tests
- State if 137 is NOT special (if data shows this)

## Example Workflow

```bash
# 1. Quick test on small range
python3 interference_functional.py --range 130 145
python3 prime_vs_composite_scan.py --range 130 145 --output quick_test/

# 2. Focused analysis around 137
python3 jacobi_packet_width_analysis.py --centers 137 --width 25
python3 channel_error_model.py --lambda 0.5 --range 125 150

# 3. Statistical validation
python3 devil_advocate_test.py --target 137 --range 100 200 --trials 1000

# 4. Full analysis
./run_all_experiments.sh

# 5. Extended scan
python3 prime_vs_composite_scan.py --range 50 300 --output extended_scan/
```

## Troubleshooting

### Import Errors

```bash
# Install missing dependencies
pip install -r requirements.txt

# Or install individually
pip install numpy scipy matplotlib
```

### Memory Issues (Large Ranges)

```bash
# Split into smaller chunks
python3 interference_functional.py --range 100 200 --output chunk1.csv
python3 interference_functional.py --range 200 300 --output chunk2.csv
```

### Plot Generation Issues

If matplotlib is not available:
- Plots will be skipped automatically
- All CSV data will still be generated
- Install matplotlib: `pip install matplotlib`

## Contributing

This is an experimental/analytical layer. Contributions should:

1. Maintain isolation from core UBT theory
2. Use measurable, testable mathematics only
3. Avoid confirmation bias
4. Report all results honestly (even if 137 is not special)

## License

See repository LICENSE.md
