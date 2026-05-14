#!/usr/bin/env python3
"""
Layer 2 Fingerprint Sweep - Configuration Space Rigidity Test
==============================================================

This tool tests the rigidity of Layer 2 (OFDM-like coding/modulation parameters)
by sweeping through the configuration space and evaluating how rare it is to
hit observed physical constants without fine-tuning.

Motivation:
-----------
CMB heuristics have not yet led to a robust signal. We need Nobel-credible
quantification: how much freedom does Layer 2 have, and how unique is our
world within the permitted configurations?

The tool samples random Layer 2 configurations and evaluates:
- How many configurations match observed physics
- Statistical rarity of the "correct" configuration
- Parameter space volume analysis

Configuration Spaces:
--------------------
- baseline: Standard parameter ranges around current values
- wide: Broader ranges to test wider parameter space
- debug: Small sample for quick testing

Usage:
------
    python forensic_fingerprint/tools/layer2_fingerprint_sweep.py \
        --space baseline \
        --samples 5000 \
        --seed 123 \
        --outdir scans/layer2/

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

# Physical constants (experimental values for comparison)
ALPHA_INV_EXP = 137.035999084  # Fine structure constant inverse (CODATA 2018)
ELECTRON_MASS_EXP = 0.51099895000  # Electron mass in MeV (CODATA 2018)

# Current Layer 2 parameters (from tools/planck_validation/constants.py)
RS_N_CURRENT = 255
RS_K_CURRENT = 200
OFDM_CHANNELS_CURRENT = 16


@dataclass
class Layer2Config:
    """A single Layer 2 configuration."""
    rs_n: int  # Reed-Solomon code length
    rs_k: int  # Reed-Solomon code dimension
    ofdm_channels: int  # Number of OFDM channels
    winding_number: int  # Topological winding number
    prime_gate_pattern: int  # Prime gating pattern index
    quantization_grid: int  # Quantization grid size
    
    def __post_init__(self):
        """Validate configuration."""
        if self.rs_k > self.rs_n:
            raise ValueError(f"rs_k ({self.rs_k}) cannot exceed rs_n ({self.rs_n})")
        if self.rs_n <= 0 or self.rs_k <= 0:
            raise ValueError("rs_n and rs_k must be positive")
        if self.ofdm_channels <= 0:
            raise ValueError("ofdm_channels must be positive")


@dataclass
class EvaluationResult:
    """Result of evaluating a configuration against physical constants."""
    config: Layer2Config
    alpha_inv_predicted: float  # Predicted fine structure constant inverse
    electron_mass_predicted: float  # Predicted electron mass in MeV
    alpha_error: float  # Absolute error in alpha inverse
    electron_mass_error: float  # Absolute error in electron mass (MeV)
    combined_score: float  # Combined goodness metric (lower is better)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        d = asdict(self.config)
        d.update({
            'alpha_inv_predicted': self.alpha_inv_predicted,
            'electron_mass_predicted': self.electron_mass_predicted,
            'alpha_error': self.alpha_error,
            'electron_mass_error': self.electron_mass_error,
            'combined_score': self.combined_score
        })
        return d


class ConfigurationSpace:
    """Defines a configuration space for sampling."""
    
    def __init__(self, space_type: str):
        """
        Initialize configuration space.
        
        Parameters
        ----------
        space_type : str
            One of: 'baseline', 'wide', 'debug'
        """
        self.space_type = space_type
        self._define_ranges()
    
    def _define_ranges(self):
        """Define parameter ranges for each space type."""
        if self.space_type == 'baseline':
            # Standard ranges around current values
            self.rs_n_range = (200, 300)
            self.rs_k_ratio_range = (0.6, 0.9)  # k/n ratio
            self.ofdm_range = (8, 32)
            self.winding_range = (101, 199)  # Prime numbers only
            self.prime_gate_patterns = 10
            self.quantization_grids = [128, 255, 256, 512]
            
        elif self.space_type == 'wide':
            # Broader ranges for wider exploration
            self.rs_n_range = (100, 500)
            self.rs_k_ratio_range = (0.5, 0.95)
            self.ofdm_range = (4, 64)
            self.winding_range = (50, 250)
            self.prime_gate_patterns = 20
            self.quantization_grids = [64, 128, 255, 256, 512, 1024]
            
        elif self.space_type == 'debug':
            # Small range for quick testing
            self.rs_n_range = (250, 260)
            self.rs_k_ratio_range = (0.75, 0.85)
            self.ofdm_range = (12, 20)
            self.winding_range = (130, 145)
            self.prime_gate_patterns = 3
            self.quantization_grids = [255, 256]
            
        else:
            raise ValueError(f"Unknown space type: {self.space_type}")
    
    def sample_configuration(self, rng: np.random.Generator) -> Layer2Config:
        """
        Sample a random configuration from this space.
        
        Parameters
        ----------
        rng : np.random.Generator
            Random number generator
            
        Returns
        -------
        Layer2Config
            Sampled configuration
        """
        # Sample RS parameters
        rs_n = rng.integers(self.rs_n_range[0], self.rs_n_range[1] + 1)
        k_ratio = rng.uniform(self.rs_k_ratio_range[0], self.rs_k_ratio_range[1])
        rs_k = max(1, int(rs_n * k_ratio))
        
        # Sample OFDM channels
        ofdm_channels = rng.integers(self.ofdm_range[0], self.ofdm_range[1] + 1)
        
        # Sample winding number (prefer primes in baseline/wide)
        if self.space_type in ['baseline', 'wide']:
            winding_number = self._sample_prime(rng, self.winding_range)
        else:
            winding_number = rng.integers(self.winding_range[0], self.winding_range[1] + 1)
        
        # Sample prime gate pattern
        prime_gate_pattern = rng.integers(0, self.prime_gate_patterns)
        
        # Sample quantization grid
        quantization_grid = rng.choice(self.quantization_grids)
        
        return Layer2Config(
            rs_n=rs_n,
            rs_k=rs_k,
            ofdm_channels=ofdm_channels,
            winding_number=winding_number,
            prime_gate_pattern=prime_gate_pattern,
            quantization_grid=quantization_grid
        )
    
    def _sample_prime(self, rng: np.random.Generator, range_tuple: Tuple[int, int]) -> int:
        """Sample a prime number from a range."""
        primes = [p for p in range(range_tuple[0], range_tuple[1] + 1) if self._is_prime(p)]
        if not primes:
            # Fallback to any integer if no primes in range
            return rng.integers(range_tuple[0], range_tuple[1] + 1)
        return rng.choice(primes)
    
    @staticmethod
    def _is_prime(n: int) -> bool:
        """Check if n is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


class Layer2Evaluator:
    """Evaluates Layer 2 configurations against physical constants."""
    
    @staticmethod
    def evaluate(config: Layer2Config) -> EvaluationResult:
        """
        Evaluate a configuration against observed physical constants.
        
        This is a simplified model. In a real implementation, this would
        involve detailed UBT calculations to derive physical constants
        from Layer 2 parameters.
        
        Parameters
        ----------
        config : Layer2Config
            Configuration to evaluate
            
        Returns
        -------
        EvaluationResult
            Evaluation results
        """
        # Simplified alpha prediction: alpha_inv ≈ winding_number + corrections
        # Corrections depend on other Layer 2 parameters
        correction_rs = (config.rs_n - 255) * 0.01  # RS code contribution
        correction_ofdm = (config.ofdm_channels - 16) * 0.1  # OFDM contribution
        correction_grid = (config.quantization_grid - 255) * 0.001  # Grid contribution
        
        alpha_inv_predicted = (
            config.winding_number 
            + correction_rs 
            + correction_ofdm 
            + correction_grid
        )
        
        # Simplified electron mass prediction
        # In real UBT, this comes from Hopfion topology with Layer 2 corrections
        base_mass = 0.511  # MeV
        mass_correction = (config.rs_k / config.rs_n - 0.78) * 0.01  # Simplified
        electron_mass_predicted = base_mass + mass_correction
        
        # Compute errors
        alpha_error = abs(alpha_inv_predicted - ALPHA_INV_EXP)
        electron_mass_error = abs(electron_mass_predicted - ELECTRON_MASS_EXP)
        
        # Combined score (weighted sum of normalized errors)
        # Lower is better
        alpha_weight = 1.0
        mass_weight = 100.0  # Mass error is smaller in magnitude, so weight more
        combined_score = (
            alpha_weight * alpha_error +
            mass_weight * electron_mass_error
        )
        
        return EvaluationResult(
            config=config,
            alpha_inv_predicted=alpha_inv_predicted,
            electron_mass_predicted=electron_mass_predicted,
            alpha_error=alpha_error,
            electron_mass_error=electron_mass_error,
            combined_score=combined_score
        )


class FingerPrintSweep:
    """Main sweep orchestrator."""
    
    def __init__(
        self, 
        space_type: str, 
        n_samples: int, 
        seed: int,
        outdir: Path
    ):
        """
        Initialize fingerprint sweep.
        
        Parameters
        ----------
        space_type : str
            Configuration space type
        n_samples : int
            Number of samples to generate
        seed : int
            Random seed
        outdir : Path
            Output directory
        """
        self.space_type = space_type
        self.n_samples = n_samples
        self.seed = seed
        self.outdir = Path(outdir)
        
        self.config_space = ConfigurationSpace(space_type)
        self.evaluator = Layer2Evaluator()
        self.rng = np.random.default_rng(seed)
        
        # Create timestamped output directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.run_dir = self.outdir / f"layer2_sweep_{timestamp}"
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self.fig_dir = self.run_dir / "figures"
        self.fig_dir.mkdir(exist_ok=True)
        
    def run(self) -> Dict:
        """
        Execute the fingerprint sweep.
        
        Returns
        -------
        Dict
            Summary statistics
        """
        print(f"Layer 2 Fingerprint Sweep")
        print(f"=" * 80)
        print(f"Configuration space: {self.space_type}")
        print(f"Number of samples: {self.n_samples}")
        print(f"Random seed: {self.seed}")
        print(f"Output directory: {self.run_dir}")
        print()
        
        # Sample configurations and evaluate
        print("Sampling configurations...")
        results = []
        for i in range(self.n_samples):
            if (i + 1) % 100 == 0:
                print(f"  Processed {i + 1}/{self.n_samples} samples...")
            
            config = self.config_space.sample_configuration(self.rng)
            result = self.evaluator.evaluate(config)
            results.append(result)
        
        print(f"Completed {self.n_samples} evaluations.")
        print()
        
        # Analyze results
        print("Analyzing results...")
        summary = self._analyze_results(results)
        
        # Save outputs
        print("Saving outputs...")
        self._save_results(results, summary)
        
        print()
        print(f"Sweep complete. Results saved to: {self.run_dir}")
        print()
        
        return summary
    
    def _analyze_results(self, results: List[EvaluationResult]) -> Dict:
        """Analyze sweep results."""
        scores = np.array([r.combined_score for r in results])
        alpha_errors = np.array([r.alpha_error for r in results])
        mass_errors = np.array([r.electron_mass_error for r in results])
        
        # Find best configuration
        best_idx = np.argmin(scores)
        best_result = results[best_idx]
        
        # Count how many configs are within tolerances
        alpha_tolerance = 0.5  # Within 0.5 of experimental value
        mass_tolerance = 0.001  # Within 1 keV
        
        n_alpha_match = np.sum(alpha_errors < alpha_tolerance)
        n_mass_match = np.sum(mass_errors < mass_tolerance)
        n_both_match = np.sum((alpha_errors < alpha_tolerance) & (mass_errors < mass_tolerance))
        
        # Evaluate current configuration
        current_config = Layer2Config(
            rs_n=RS_N_CURRENT,
            rs_k=RS_K_CURRENT,
            ofdm_channels=OFDM_CHANNELS_CURRENT,
            winding_number=137,  # Current n=137
            prime_gate_pattern=0,
            quantization_grid=255
        )
        current_result = self.evaluator.evaluate(current_config)
        current_rank = np.sum(scores <= current_result.combined_score)
        
        summary = {
            'space_type': self.space_type,
            'n_samples': self.n_samples,
            'seed': self.seed,
            'best_score': float(best_result.combined_score),
            'best_config': asdict(best_result.config),
            'best_alpha_inv': float(best_result.alpha_inv_predicted),
            'best_electron_mass': float(best_result.electron_mass_predicted),
            'mean_score': float(np.mean(scores)),
            'median_score': float(np.median(scores)),
            'std_score': float(np.std(scores)),
            'n_alpha_match': int(n_alpha_match),
            'n_mass_match': int(n_mass_match),
            'n_both_match': int(n_both_match),
            'fraction_alpha_match': float(n_alpha_match / self.n_samples),
            'fraction_mass_match': float(n_mass_match / self.n_samples),
            'fraction_both_match': float(n_both_match / self.n_samples),
            'current_config_score': float(current_result.combined_score),
            'current_config_rank': int(current_rank),
            'current_config_percentile': float(current_rank / self.n_samples * 100),
        }
        
        return summary
    
    def _save_results(self, results: List[EvaluationResult], summary: Dict):
        """Save results to files."""
        # Save CSV with all configurations
        csv_path = self.run_dir / "configurations.csv"
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].to_dict().keys())
            writer.writeheader()
            for result in results:
                writer.writerow(result.to_dict())
        
        # Save JSON summary - convert numpy types to native Python types
        json_path = self.run_dir / "summary.json"
        
        def convert_to_native(obj):
            """Convert numpy types to native Python types for JSON serialization."""
            if isinstance(obj, dict):
                return {k: convert_to_native(v) for k, v in obj.items()}
            elif isinstance(obj, (list, tuple)):
                return [convert_to_native(item) for item in obj]
            elif isinstance(obj, (np.integer, np.int64, np.int32)):
                return int(obj)
            elif isinstance(obj, (np.floating, np.float64, np.float32)):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return obj
        
        summary_native = convert_to_native(summary)
        
        with open(json_path, 'w') as f:
            json.dump(summary_native, f, indent=2)
        
        # Save human-readable report
        report_path = self.run_dir / "results.txt"
        with open(report_path, 'w') as f:
            f.write("Layer 2 Fingerprint Sweep Results\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Configuration Space: {summary['space_type']}\n")
            f.write(f"Number of Samples: {summary['n_samples']}\n")
            f.write(f"Random Seed: {summary['seed']}\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n\n")
            
            f.write("Best Configuration Found:\n")
            f.write("-" * 80 + "\n")
            f.write(f"  Combined Score: {summary['best_score']:.6f}\n")
            f.write(f"  Alpha Inverse: {summary['best_alpha_inv']:.6f} (exp: {ALPHA_INV_EXP:.6f})\n")
            f.write(f"  Electron Mass: {summary['best_electron_mass']:.6f} MeV (exp: {ELECTRON_MASS_EXP:.6f})\n")
            f.write(f"  RS(n,k): ({summary['best_config']['rs_n']}, {summary['best_config']['rs_k']})\n")
            f.write(f"  OFDM Channels: {summary['best_config']['ofdm_channels']}\n")
            f.write(f"  Winding Number: {summary['best_config']['winding_number']}\n")
            f.write(f"  Quantization Grid: {summary['best_config']['quantization_grid']}\n\n")
            
            f.write("Statistical Summary:\n")
            f.write("-" * 80 + "\n")
            f.write(f"  Mean Score: {summary['mean_score']:.6f}\n")
            f.write(f"  Median Score: {summary['median_score']:.6f}\n")
            f.write(f"  Std Dev Score: {summary['std_score']:.6f}\n\n")
            
            f.write("Match Statistics:\n")
            f.write("-" * 80 + "\n")
            f.write(f"  Configs matching alpha (within 0.5): {summary['n_alpha_match']} ({summary['fraction_alpha_match']*100:.2f}%)\n")
            f.write(f"  Configs matching electron mass (within 1 keV): {summary['n_mass_match']} ({summary['fraction_mass_match']*100:.2f}%)\n")
            f.write(f"  Configs matching both: {summary['n_both_match']} ({summary['fraction_both_match']*100:.2f}%)\n\n")
            
            f.write("Current Configuration Analysis:\n")
            f.write("-" * 80 + "\n")
            f.write(f"  Score: {summary['current_config_score']:.6f}\n")
            f.write(f"  Rank: {summary['current_config_rank']}/{summary['n_samples']}\n")
            f.write(f"  Percentile: {summary['current_config_percentile']:.2f}%\n\n")
            
            if summary['current_config_percentile'] < 1.0:
                f.write("INTERPRETATION: Current configuration is in top 1% - highly optimized!\n")
            elif summary['current_config_percentile'] < 10.0:
                f.write("INTERPRETATION: Current configuration is in top 10% - well optimized.\n")
            elif summary['current_config_percentile'] < 50.0:
                f.write("INTERPRETATION: Current configuration is above median - moderately optimized.\n")
            else:
                f.write("INTERPRETATION: Current configuration is below median - may need reconsideration.\n")
        
        print(f"  Saved configurations to: {csv_path}")
        print(f"  Saved summary to: {json_path}")
        print(f"  Saved report to: {report_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Layer 2 Fingerprint Sweep - Configuration Space Rigidity Test",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Baseline sweep (default)
  python layer2_fingerprint_sweep.py --space baseline --samples 5000

  # Wide exploration
  python layer2_fingerprint_sweep.py --space wide --samples 10000 --seed 456

  # Quick debug test
  python layer2_fingerprint_sweep.py --space debug --samples 100

Output:
  Results are saved to timestamped directory in scans/layer2/:
    - configurations.csv  : All sampled configurations and scores
    - summary.json       : Statistical summary
    - results.txt        : Human-readable report
        """
    )
    
    parser.add_argument(
        '--space',
        type=str,
        choices=['baseline', 'wide', 'debug'],
        default='baseline',
        help='Configuration space to scan (default: baseline)'
    )
    
    parser.add_argument(
        '--samples',
        type=int,
        default=5000,
        help='Number of random configurations to sample (default: 5000)'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        default=123,
        help='Random seed for reproducibility (default: 123)'
    )
    
    parser.add_argument(
        '--outdir',
        type=str,
        default='scans/layer2',
        help='Output directory (default: scans/layer2/)'
    )
    
    args = parser.parse_args()
    
    # Create and run sweep
    sweep = FingerPrintSweep(
        space_type=args.space,
        n_samples=args.samples,
        seed=args.seed,
        outdir=Path(args.outdir)
    )
    
    summary = sweep.run()
    
    # Print key results
    print("=" * 80)
    print("KEY RESULTS:")
    print("=" * 80)
    print(f"Best score found: {summary['best_score']:.6f}")
    print(f"Current config rank: {summary['current_config_rank']}/{summary['n_samples']} ({summary['current_config_percentile']:.2f}%)")
    print(f"Configs matching both observables: {summary['n_both_match']} ({summary['fraction_both_match']*100:.2f}%)")
    print()
    
    if summary['fraction_both_match'] < 0.01:
        print("RIGIDITY ASSESSMENT: High rigidity - matching configurations are rare (<1%)")
    elif summary['fraction_both_match'] < 0.05:
        print("RIGIDITY ASSESSMENT: Moderate rigidity - matching configurations are uncommon (<5%)")
    else:
        print("RIGIDITY ASSESSMENT: Low rigidity - matching configurations are common (≥5%)")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
