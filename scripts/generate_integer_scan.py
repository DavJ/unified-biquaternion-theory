#!/usr/bin/env python3
"""
Generate Integer Grid Scan Tool
================================

Generates CSV files with integer n values scanned over a range for testing
mod-4 prime class structure.

This creates synthetic scan data with a specified signal pattern that can be
used to test the channel analysis pipeline.

Usage:
    python scripts/generate_integer_scan.py --scan-integers 100 200 --step 1 --channel BB
    python scripts/generate_integer_scan.py --scan-integers 100 200 --step 1 --channel TT
    python scripts/generate_integer_scan.py --scan-integers 100 200 --step 1 --channel EE

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

import argparse
import csv
import numpy as np
from pathlib import Path


def is_prime(n):
    """Deterministic primality test for integers."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_signal(n, channel='BB', noise_level=0.1, seed=42):
    """
    Generate a synthetic signal value for integer n.
    
    Uses a simple model:
    - Base signal from smooth function
    - Enhancement at primes (especially mod-4 classes)
    - Random noise
    
    Args:
        n: Integer value
        channel: Channel type (BB, TT, EE)
        noise_level: Standard deviation of noise
        seed: Random seed for reproducibility
    
    Returns:
        Signal value (PSD-like)
    """
    np.random.seed(seed + int(n))
    
    # Base signal: decreases slowly with n
    base = 1.0 / (1.0 + 0.001 * n)
    
    # Enhancement at primes
    if is_prime(int(n)):
        prime_boost = 0.5
        
        # Additional boost based on mod-4 class
        n_mod4 = int(n) % 4
        if n_mod4 == 1:
            # Class C1 primes get extra boost in some channels
            if channel in ['BB', 'TT']:
                prime_boost += 0.3
        elif n_mod4 == 3:
            # Class C3 primes get different boost pattern
            if channel in ['EE', 'TT']:
                prime_boost += 0.2
    else:
        prime_boost = 0.0
    
    # Add channel-specific offset
    channel_offset = {'BB': 1.0, 'TT': 1.5, 'EE': 0.8}.get(channel, 1.0)
    
    # Add noise
    noise = np.random.normal(0, noise_level)
    
    signal = channel_offset * base * (1.0 + prime_boost) + noise
    
    return max(0.0, signal)  # Ensure non-negative


def generate_integer_scan(
    start: int,
    end: int,
    step: int = 1,
    channel: str = 'BB',
    output_file: str = None,
    noise_level: float = 0.1,
    seed: int = 42
):
    """
    Generate integer grid scan CSV file.
    
    Args:
        start: Starting integer (inclusive)
        end: Ending integer (inclusive)
        step: Step size
        channel: Channel type (BB, TT, EE)
        output_file: Output CSV path
        noise_level: Noise level for synthetic signal
        seed: Random seed
    """
    # Generate integer range
    n_values = list(range(start, end + 1, step))
    
    # Generate signals
    rows = []
    for n in n_values:
        signal = generate_signal(n, channel=channel, noise_level=noise_level, seed=seed)
        
        # Determine kind
        if n in [137, 139]:
            kind = 'target'
            label = f'p={n}'
        elif is_prime(n):
            kind = 'scan'
            label = f'p={n}'
        else:
            kind = 'scan'
            label = f'n={n}'
        
        rows.append({
            'kind': kind,
            'channel': channel,
            'label': label,
            'raw': n,
            'n': n,  # Also include explicit n column
            'psd_obs': signal,
        })
    
    # Write to CSV
    if output_file is None:
        output_file = f"scans/{channel.lower()}_scan_int_{start}_{end}.csv"
    
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', newline='') as f:
        fieldnames = ['kind', 'channel', 'label', 'raw', 'n', 'psd_obs']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    # Print summary
    n_primes = sum(1 for n in n_values if is_prime(n))
    n_primes_c1 = sum(1 for n in n_values if is_prime(n) and n % 4 == 1)
    n_primes_c3 = sum(1 for n in n_values if is_prime(n) and n % 4 == 3)
    
    print(f"Generated: {output_path}")
    print(f"  Range: [{start}, {end}], step={step}")
    print(f"  Total points: {len(n_values)}")
    print(f"  Primes: {n_primes}")
    print(f"    C1 (p≡1 mod 4): {n_primes_c1}")
    print(f"    C3 (p≡3 mod 4): {n_primes_c3}")
    print(f"  Channel: {channel}")
    
    return output_path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate integer grid scan CSV files for channel analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate BB scan from 100 to 200
  python scripts/generate_integer_scan.py --scan-integers 100 200 --channel BB
  
  # Generate all three channels
  python scripts/generate_integer_scan.py --scan-integers 100 200 --channel BB TT EE
  
  # Custom output location
  python scripts/generate_integer_scan.py --scan-integers 100 200 --channel BB --output my_scan.csv
  
  # Adjust noise level
  python scripts/generate_integer_scan.py --scan-integers 100 200 --channel BB --noise 0.2
"""
    )
    
    parser.add_argument(
        '--scan-integers',
        nargs=2,
        type=int,
        metavar=('START', 'END'),
        required=True,
        help='Integer range to scan (inclusive)'
    )
    
    parser.add_argument(
        '--step',
        type=int,
        default=1,
        help='Step size for integer scan (default: 1)'
    )
    
    parser.add_argument(
        '--channel',
        nargs='+',
        choices=['BB', 'TT', 'EE'],
        default=['BB'],
        help='Channel(s) to generate (default: BB)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Output CSV file path (default: auto-generated in scans/)'
    )
    
    parser.add_argument(
        '--noise',
        type=float,
        default=0.1,
        help='Noise level for synthetic signal (default: 0.1)'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help='Random seed for reproducibility (default: 42)'
    )
    
    args = parser.parse_args()
    
    start, end = args.scan_integers
    
    if start >= end:
        parser.error("START must be less than END")
    
    if args.step < 1:
        parser.error("STEP must be at least 1")
    
    # Generate for each channel
    for channel in args.channel:
        output_file = args.output
        if output_file is None and len(args.channel) > 1:
            # Auto-generate different names for multiple channels
            output_file = f"scans/{channel.lower()}_scan_int_{start}_{end}.csv"
        
        generate_integer_scan(
            start=start,
            end=end,
            step=args.step,
            channel=channel,
            output_file=output_file,
            noise_level=args.noise,
            seed=args.seed
        )
        
        print()


if __name__ == '__main__':
    main()
