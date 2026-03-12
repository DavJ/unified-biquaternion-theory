# UBT Experimental Channel Selection

**Project**: UBT_Experimental_Channel_Selection  
**Version**: 0.1.0  
**Status**: Experimental/Analytical Layer

## Overview

This directory contains experimental tools to explore possible selection mechanisms for prime number modes (especially 137, 139) **without any modification to the core UBT theory**.

This is a **purely experimental/analytical layer** that tests emergent stability properties of discrete modes in the biquaternionic field.

## Constraints

- ✅ **Do NOT modify Layer 0** (scalar source)
- ✅ **Do NOT modify Layer 1** (8D torus, complex time τ, Jacobi kernel)
- ✅ **Do NOT alter any core theoretical files**
- ✅ All work isolated in `EXPERIMENTS/channel_selection/`
- ✅ No reinterpretation of existing results
- ✅ No philosophical additions
- ✅ Only measurable, testable mathematics

## Modules

### 1. interference_functional.py
Defines interference functional I(n) for discrete mode n to measure aliasing, harmonic overlaps, and spectral redundancy.

**Features**:
- `compute_aliasing_metric(n, spectrum)` - Measure aliasing effects
- `compute_harmonic_overlap(n)` - Detect harmonic overlaps
- `I(n)` - Combined interference functional
- Evaluation for n ∈ [100, 200]
- Prime vs composite comparison

### 2. prime_vs_composite_scan.py
Systematically compares spectral stability of primes vs composite numbers.

**Features**:
- Prime number generation in tested interval
- I(n) computation for each n
- Ranking table generation
- Plots of I(n) vs n
- Highlights 137 and 139 **without privileging them**

### 3. jacobi_packet_width_analysis.py
Verifies whether the Jacobi kernel (Layer 1) generates natural energy packets around certain modes.

**Features**:
- Numerical simulation of theta function dispersion
- Gaussian envelope width measurement
- Correlation with prime modes
- Cluster width statistics output

### 4. channel_error_model.py
Models Layer 2 as an information channel with mode-dependent error rate.

**Features**:
- `error_rate(n)` definition based on aliasing
- Reed-Solomon style redundancy simulation
- Stability region evaluation
- Cost functional minimization: F(n) = interference(n) + λ·error_rate(n)

### 5. devil_advocate_test.py
Attempts to **falsify** the hypothesis about privileged status of 137.

**Features**:
- Spectral data randomization
- Mode label shuffling
- Re-run interference scan
- Probability estimation for 137 emerging by chance
- Falsification score output

## Analysis Requirements

- ✅ No confirmation bias
- ✅ Always compare against neighboring values
- ✅ Always report global and local minima
- ✅ Never assume 137 must win
- ✅ **If 137 is not special, explicitly state it**

## Validation Steps

1. Run full scan for n = 50–300
2. Separate primes and composites statistically
3. Compute mean I(n) for primes vs composites
4. Perform permutation test
5. Produce p-value for prime advantage hypothesis

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run interference functional analysis
python interference_functional.py --range 100 200

# Run prime vs composite scan
python prime_vs_composite_scan.py --range 100 200 --output results/

# Run Jacobi packet analysis
python jacobi_packet_width_analysis.py --config config.yaml

# Run channel error model
python channel_error_model.py --lambda 0.5

# Run devil's advocate test
python devil_advocate_test.py --trials 1000
```

## Output

- CSV tables of I(n) values
- Plots of functional landscape
- Ranked list of most stable modes
- Statistical summary report
- Falsification test results

## Future Extensions

- Extend scan to 500–1000
- Test twin-prime pairs specifically
- Connect to cosmological observables (optional, separate module)

## Critical Rule

> This is an **exploratory validation project**.  
> It must **NOT** rewrite, reinterpret, or modify Unified Biquaternion Theory.  
> It only tests emergent stability properties of discrete modes.

## License

See repository LICENSE.md
