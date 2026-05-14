#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
prime_sequence.py

Task 1: Generate primes up to N, compute k = (p^2 - 1) // 24 for each prime p > 3,
and store the result as a Parquet file.

Note: For every prime p > 3, p is coprime to 6, so p ≡ 1 or 5 (mod 6).
This implies p^2 ≡ 1 (mod 24), so k = (p^2 - 1) / 24 is guaranteed to be a
positive integer — no filtering needed.

Output: data/primes_mod24.parquet
Columns: p, p_sq, k, log_p, gap_to_next
"""

from __future__ import annotations

import argparse
import math
import os
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Sieve of Eratosthenes
# ---------------------------------------------------------------------------

def sieve(n: int) -> np.ndarray:
    """Return array of all primes <= n using a simple bit-sieve."""
    if n < 2:
        return np.array([], dtype=np.int64)
    composite = np.zeros(n + 1, dtype=bool)
    composite[0] = composite[1] = True
    for i in range(2, int(math.isqrt(n)) + 1):
        if not composite[i]:
            composite[i * i :: i] = True
    return np.where(~composite)[0].astype(np.int64)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def build_dataframe(n: int) -> pd.DataFrame:
    """Build the prime/k DataFrame for all primes p in (3, n]."""
    all_primes = sieve(n)
    # Filter p > 3
    primes = all_primes[all_primes > 3]

    p_sq = primes.astype(np.int64) ** 2
    k = (p_sq - 1) // 24
    log_p = np.log(primes.astype(np.float64))

    # Gap to next prime (for the last prime use NaN)
    gaps = np.empty(len(primes), dtype=np.float64)
    gaps[:-1] = (primes[1:] - primes[:-1]).astype(np.float64)
    gaps[-1] = np.nan

    df = pd.DataFrame({
        "p": primes,
        "p_sq": p_sq,
        "k": k,
        "log_p": log_p,
        "gap_to_next": gaps,
    })
    return df


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate prime mod-24 sequence dataset")
    ap.add_argument("--n", type=float, default=1e5,
                    help="Upper bound for prime sieve (default: 1e5)")
    ap.add_argument("--out", default="DATA/prime_mod24/primes_mod24.parquet",
                    help="Output Parquet path (default: DATA/prime_mod24/primes_mod24.parquet)")
    args = ap.parse_args()

    n = int(args.n)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Sieving primes up to N = {n:,} …")
    df = build_dataframe(n)

    print(f"  Primes > 3 found: {len(df):,}")
    print(f"  k range: [{df['k'].min()}, {df['k'].max()}]")
    print(f"  Writing → {out_path}")

    df.to_parquet(out_path, index=False, engine="pyarrow", compression="snappy")
    print("Done.")


if __name__ == "__main__":
    main()
