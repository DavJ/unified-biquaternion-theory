#!/usr/bin/env python3
"""Spectral parity / RS-consistency test for CMB alm coefficients.

Rotation-invariant "multiplex" test:
  1) Obtain a_{\ell m} coefficients (TT, and optionally EE/BB via Q/U).
  2) Define an ordering k(\ell,m) = \ell^2 + \ell + m (shell-by-shell).
  3) Quantize each coefficient to an 8-bit symbol (phase quantization).
  4) Scan frames of length 255 symbols and compute:
     - Hamming(8,4) validity rate (quick screening)
     - RS(255,201) syndrome score E = count_{j=1..54}[S_j==0]
  5) Compute p-values via Monte Carlo nulls that preserve C_\ell.

Inputs
------
You can pass either maps (HEALPix FITS) or alm (FITS) files.
For polarization, pass Q/U maps or precomputed almE/almB.

Null models
-----------
N1: Phase randomization per \ell (preserves |a_{\ell m}| hence C_\ell).

Notes
-----
- This is a forensic "consistency" test, not a proof of any model.
- A null result does not invalidate UBT Layer-1; it only constrains this
  specific Layer-2 encoding hypothesis.
"""

from __future__ import annotations

import argparse
import math
import os
import random
import sys
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

# Optional plotting (only used for the Prime-Gated view).
# Keeping this optional avoids forcing matplotlib for headless/CI runs.
try:  # pragma: no cover
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover
    plt = None

try:
    from tqdm import tqdm
except Exception:  # pragma: no cover
    tqdm = None

try:
    import healpy as hp
except Exception as e:  # pragma: no cover
    hp = None

from .rs_syndrome import RSParams, syndrome_zero_count


# -----------------------------------------------------------------------------
# Prime-gated helper utilities
# -----------------------------------------------------------------------------

def is_prime(n: int) -> bool:
    """Return True if n is a prime number.

    Notes
    -----
    - We only care about small-ish multipoles (ell), so a deterministic
      sqrt(n) test is more than enough.
    - ell=0,1 are treated as non-prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2) == 0 or (n % 3) == 0:
        return False
    r = int(math.isqrt(n))
    f = 5
    while f <= r:
        if (n % f) == 0 or (n % (f + 2)) == 0:
            return False
        f += 6
    return True


def ell_shell_indices(ell: int) -> np.ndarray:
    """Return the k-indices for the full (ell,m) shell: m in [-ell, ..., +ell]."""
    # NOTE: With k(ell,m)=ell^2+ell+m, the shell is actually contiguous:
    #   m=-ell -> k=ell^2
    #   m=+ell -> k=ell^2+2ell
    # Keeping the explicit list is handy for clarity, but the prime-gated
    # computation uses the contiguous slice directly for performance.
    return np.array([k_index(ell, m) for m in range(-ell, ell + 1)], dtype=np.int64)


def ell_shell_slice(ell: int) -> slice:
    """Return a contiguous slice covering the (ell,m) shell in the k-stream."""
    start = int(ell * ell)
    stop = int(ell * ell + 2 * ell + 1)  # python stop is exclusive
    return slice(start, stop)


def shell_hamming_integrity(symbol_stream: np.ndarray, ell: int) -> float:
    """Digit-level "purity" for one multipole shell.

    We use the Hamming(8,4) validity rate as a fast, purely digital checksum.
    For a random byte stream, expected validity is 1/16 = 0.0625.

    This matches the user's intended "Hammingova čistota" view per multipole.
    """
    # Fast path: the shell is contiguous in k.
    sl = ell_shell_slice(int(ell))
    return hamming_valid_rate_fast(symbol_stream[sl])


def prime_gated_integrity_curve(
    symbol_stream: np.ndarray,
    lmin: int,
    lmax: int,
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute per-ell integrity curve for plotting / inspection."""
    ells = np.arange(int(lmin), int(lmax) + 1, dtype=int)
    integrity = np.empty_like(ells, dtype=float)
    for i, ell in enumerate(ells.tolist()):
        integrity[i] = shell_hamming_integrity(symbol_stream, ell)
    return ells, integrity


def prime_gated_delta_from_symbol_stream(
    symbol_stream: np.ndarray,
    lmin: int,
    lmax: int,
) -> float:
    """Compute Δmean(P−C) for one symbol stream without storing the whole curve."""
    p_sum = 0.0
    c_sum = 0.0
    p_n = 0
    c_n = 0
    for ell in range(int(lmin), int(lmax) + 1):
        r = shell_hamming_integrity(symbol_stream, ell)
        if not np.isfinite(r):
            continue
        if is_prime(ell):
            p_sum += r
            p_n += 1
        elif ell >= 2:
            c_sum += r
            c_n += 1
    if p_n == 0 or c_n == 0:
        return float('nan')
    return float((p_sum / p_n) - (c_sum / c_n))


def prime_gated_delta_mean(ells: np.ndarray, integrity: np.ndarray) -> float:
    """Compute mean(integrity | ell is prime) - mean(integrity | ell is composite)."""
    prime_mask = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    comp_mask = (ells >= 2) & (~prime_mask)
    p = integrity[prime_mask]
    c = integrity[comp_mask]
    if p.size == 0 or c.size == 0:
        return float('nan')
    return float(np.mean(p) - np.mean(c))


def permutation_null_deltas(
    ells: np.ndarray,
    integrity: np.ndarray,
    n_perm: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Permutation null for Prime-Gated effect.

    Keeps the integrity values fixed, but randomly reassigns "prime" labels
    to the same number of multipoles. This tests whether P vs C difference
    can arise purely from the marginal integrity distribution.
    """
    ells = np.asarray(ells, dtype=int)
    integrity = np.asarray(integrity, dtype=float)

    prime_mask = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    comp_mask = (ells >= 2) & (~prime_mask)
    valid_idx = np.where(ells >= 2)[0]

    p_count = int(np.sum(prime_mask))
    c_count = int(np.sum(comp_mask))
    if p_count == 0 or c_count == 0:
        return np.array([], dtype=float)

    out = np.empty(int(n_perm), dtype=float)
    for i in range(int(n_perm)):
        perm = rng.permutation(valid_idx)
        p_idx = perm[:p_count]
        c_idx = perm[p_count : p_count + c_count]
        out[i] = float(np.mean(integrity[p_idx]) - np.mean(integrity[c_idx]))
    return out


# RSParams API compatibility: some versions accept nsym, others derive it.
# Our local rs_syndrome.RSParams accepts (n,k,nsym), but keep this robust.
def _make_rs_params(RSParams, n=255, k=201, nsym=54):
    try:
        import inspect
        sig = inspect.signature(RSParams)
        params = sig.parameters
        if 'nsym' in params:
            return RSParams(n=n, k=k, nsym=nsym)
        if 'parity' in params:
            return RSParams(n=n, k=k, parity=nsym)
        if 'npar' in params:
            return RSParams(n=n, k=k, npar=nsym)
        return RSParams(n=n, k=k)
    except Exception:
        try:
            return RSParams(n, k, nsym)
        except Exception:
            return RSParams(n, k)


class _Progress:
    """Single-line progress reporting with optional tqdm support.

    Uses tqdm if available; otherwise writes a single updating line to stderr.
    Designed to avoid spamming many lines in long Monte Carlo runs.
    """

    def __init__(self, enabled: bool, total: int, desc: str, unit: str = 'it'):
        self.enabled = bool(enabled)
        self.total = int(total)
        self.desc = desc
        self.unit = unit
        self._t0 = time.time()
        self._i = 0
        self._pbar = None
        if self.enabled and tqdm is not None:
            self._pbar = tqdm(total=self.total, desc=self.desc, unit=self.unit, dynamic_ncols=True)

    def update(self, n: int = 1, **postfix):
        if not self.enabled:
            return
        self._i += n
        if self._pbar is not None:
            self._pbar.update(n)
            if postfix:
                # Keep postfix compact; tqdm renders it on the same line.
                self._pbar.set_postfix(**{k: v for k, v in postfix.items() if v is not None})
            return

        # Fallback: single-line status (carriage-return overwrite).
        elapsed = time.time() - self._t0
        rate = (self._i / elapsed) if elapsed > 0 else 0.0
        eta = ((self.total - self._i) / rate) if rate > 0 else float('inf')
        tail = '  '.join([f"{k}={v}" for k, v in postfix.items() if v is not None])
        msg = f"{self.desc}: {self._i}/{self.total} {self.unit}  {rate:.2f}/{self.unit}/s  ETA {eta:.0f}s"
        if tail:
            msg += '  |  ' + tail
        sys.stderr.write('\r' + msg[:220].ljust(220))
        sys.stderr.flush()

    def close(self):
        if not self.enabled:
            return
        if self._pbar is not None:
            self._pbar.close()
            return
        sys.stderr.write('\n')
        sys.stderr.flush()


@dataclass
class Symbols:
    name: str
    symbols: np.ndarray  # uint8


def _require_healpy() -> None:
    if hp is None:
        raise RuntimeError(
            "healpy is required to load maps/alm. Install via: pip install healpy"
        )


def k_index(ell: int, m: int) -> int:
    """k(ell,m) = ell^2 + ell + m."""
    return ell * ell + ell + m


DEFAULT_LMIN = 2


# -----------------------------
# Prime-Gated (UBT fingerprint)
# -----------------------------
#
# Motivation (as used in the repo discussions):
# - Compute a *per-multipole* digital purity / integrity score.
# - Compare the distribution for prime ℓ (set P) vs composite ℓ (set C).
# - Contrast real data vs nulls (Monte Carlo) that preserve C_ℓ.
#
# This script already implements an RS-consistency test on a long symbol stream.
# For the Prime-Gated view we use a *local* per-ℓ score based on the same
# 8-bit phase-quantized symbols. The most stable per-ℓ score is the
# Hamming(8,4) validity rate computed on the shell (m=-ℓ..ℓ), i.e. on
# exactly (2ℓ+1) symbols. This is what the user refers to as
# “Hammingova čistota / parity integrity”.


def is_prime(n: int) -> bool:
    """Return True if n is prime.

    Deterministic for n up to typical lmax (<= a few thousand).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(math.isqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def split_ells_prime_composite(ells: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Return (prime_mask, composite_mask) for an array of multipoles."""
    prime_mask = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    composite_mask = (ells >= 2) & (~prime_mask)
    return prime_mask, composite_mask


def shell_symbols(symbol_stream: np.ndarray, ell: int) -> np.ndarray:
    """Extract the (2ℓ+1) symbols for a single multipole shell.

    The stream uses the rotation-invariant ordering k(ℓ,m)=ℓ^2+ℓ+m.
    This function returns symbols for m=-ℓ..ℓ (inclusive).
    """
    # k runs from ℓ^2 to ℓ^2+2ℓ
    start = ell * ell
    end = ell * ell + 2 * ell
    return symbol_stream[start : end + 1]


def hamming_shell_integrity(symbol_stream: np.ndarray, ell: int) -> float:
    """Per-ℓ integrity score: Hamming(8,4) validity rate on the shell."""
    s = shell_symbols(symbol_stream, ell)
    return hamming_valid_rate(s)


def quantize_phase_to_u8(z: complex) -> int:
    """Map complex phase arg(z) to 0..255."""
    if z == 0:
        return 0
    phi = math.atan2(z.imag, z.real)
    if phi < 0:
        phi += 2 * math.pi
    return int((256.0 * phi) / (2 * math.pi)) & 0xFF


def hamming_8_4_is_valid(byte: int) -> bool:
    """Check if an 8-bit value is a valid extended Hamming(8,4) codeword.

    Bit positions (1-indexed): 1,2,4 are parity; 8 is overall parity.
    Data bits at 3,5,6,7.

    This yields 16 valid codewords out of 256 (expected rate 1/16 for random bytes).
    """
    b = [(byte >> i) & 1 for i in range(8)]  # b[0] is LSB
    # Map to positions 1..8 where position 1 is LSB
    p1 = b[0]
    p2 = b[1]
    d1 = b[2]
    p4 = b[3]
    d2 = b[4]
    d3 = b[5]
    d4 = b[6]
    p8 = b[7]

    c1 = (d1 ^ d2 ^ d4) == p1
    c2 = (d1 ^ d3 ^ d4) == p2
    c4 = (d2 ^ d3 ^ d4) == p4
    overall = (p1 ^ p2 ^ d1 ^ p4 ^ d2 ^ d3 ^ d4) == p8
    return bool(c1 and c2 and c4 and overall)


# Precompute validity table for fast vectorized rates.
# This avoids a Python loop over large symbol streams when doing per-ell scans.
HAMMING_VALID_TABLE = np.array([hamming_8_4_is_valid(i) for i in range(256)], dtype=bool)


def hamming_valid_rate(symbols: np.ndarray) -> float:
    if symbols.size == 0:
        return float('nan')
    ok = 0
    for x in symbols.tolist():
        if hamming_8_4_is_valid(int(x)):
            ok += 1
    return ok / float(symbols.size)


def hamming_valid_rate_fast(symbols: np.ndarray) -> float:
    """Vectorized validity rate using the precomputed lookup table."""
    if symbols.size == 0:
        return float('nan')
    # symbols are uint8; lookup yields boolean array.
    return float(np.mean(HAMMING_VALID_TABLE[symbols]))


def load_alm_from_map(map_path: str, lmax: int) -> np.ndarray:
    _require_healpy()

    # healpy>=1.15 deprecates "verbose"; keep compatibility.
    m = hp.read_map(map_path, field=0)
    alm = hp.map2alm(m, lmax=lmax, pol=False, iter=3)
    return alm


def load_almE_B_from_qu_maps(q_path: str, u_path: str, lmax: int) -> Tuple[np.ndarray, np.ndarray]:
    _require_healpy()
    q = hp.read_map(q_path, field=0)
    u = hp.read_map(u_path, field=0)
    # spin-2 transform
    # healpy API compatibility:
    # some versions support iter=..., some do not
    try:
        almE, almB = hp.map2alm_spin([q, u], spin=2, lmax=lmax, iter=3)
    except TypeError:
        almE, almB = hp.map2alm_spin([q, u], spin=2, lmax=lmax)
    return almE, almB


def load_alm_fits(path: str) -> np.ndarray:
    _require_healpy()
    return hp.read_alm(path)


def build_symbol_stream_from_alm(alm: np.ndarray, lmax: int, name: str, lmin: int = DEFAULT_LMIN) -> Symbols:
    """Build uint8 symbol stream using phase quantization, for all m in [-ell,ell].

    healpy stores only m>=0. For real fields, negative m are obtained by:
      a_{l,-m} = (-1)^m * conj(a_{l,m})
    """
    _require_healpy()
    sym = np.zeros(((lmax + 1) * (lmax + 1)), dtype=np.uint8)  # total modes up to lmax

    for ell in range(lmin, lmax + 1):
        # m=0
        a0 = hp.Alm.getidx(lmax, ell, 0)
        sym[k_index(ell, 0)] = quantize_phase_to_u8(complex(alm[a0]))
        for m in range(1, ell + 1):
            idx = hp.Alm.getidx(lmax, ell, m)
            a = complex(alm[idx])
            sym[k_index(ell, m)] = quantize_phase_to_u8(a)
            aneg = ((-1) ** m) * np.conj(a)
            sym[k_index(ell, -m)] = quantize_phase_to_u8(complex(aneg))

    return Symbols(name=name, symbols=sym)


def phase_randomize_per_ell(
    alm: np.ndarray,
    lmax: int,
    rng: np.random.Generator,
    lmin: int = DEFAULT_LMIN,
) -> np.ndarray:
    """Null model N1: randomize phases within each ell while preserving amplitudes."""
    _require_healpy()
    out = np.array(alm, copy=True)
    for ell in range(lmin, lmax + 1):
        # m=0 real mode: keep as is (or random sign); keep as is for safety.
        for m in range(1, ell + 1):
            idx = hp.Alm.getidx(lmax, ell, m)
            r = abs(out[idx])
            phi = rng.uniform(0.0, 2 * math.pi)
            out[idx] = r * (math.cos(phi) + 1j * math.sin(phi))
    return out


def windowed(seq: np.ndarray, n: int, step: int) -> Iterable[np.ndarray]:
    for start in range(0, max(0, seq.size - n + 1), step):
        yield seq[start : start + n]


@dataclass
class TestResult:
    name: str
    hamming_rate: float
    rs_mean_zero_syndromes: float
    rs_tail_rate: float


def compute_scores(
    symbols: np.ndarray,
    rs_params: RSParams,
    frame: int = 255,
    step: int = 255,
    tail_k: int = 8,
    max_frames: Optional[int] = None,
    rng: Optional[np.random.Generator] = None,
) -> Tuple[float, float]:
    """Return (mean_zero_count, tail_rate) for RS syndrome zeros.

    Performance note
    ----------------
    Scanning a ~1M symbol stream with step=1 yields ~1M frames; doing that for
    hundreds of Monte Carlo iterations is prohibitively slow.

    Use either:
      - a larger --step (default 255 = non-overlapping frames), and/or
      - --max-frames with --seed to sample a fixed subset of windows.
    """
    counts: List[int] = []

    if max_frames is not None and max_frames > 0:
        if rng is None:
            max_start = max(0, symbols.size - frame)
        max_start = max(0, symbols.size - frame)
        if max_start <= 0:
            return float('nan'), float('nan')
        # Sample window starts; align to "step" grid for determinism.
        grid = np.arange(0, max_start + 1, step, dtype=np.int64)
        if grid.size == 0:
            return float('nan'), float('nan')
        choose = min(int(max_frames), int(grid.size))
        starts = rng.choice(grid, size=choose, replace=False)
        for s in starts.tolist():
            w = symbols[s : s + frame]
            counts.append(syndrome_zero_count(w.tolist(), rs_params))
    else:
        for w in windowed(symbols, frame, step):
            counts.append(syndrome_zero_count(w.tolist(), rs_params))
    if not counts:
        return float('nan'), float('nan')
    arr = np.array(counts, dtype=np.float64)
    mean = float(arr.mean())
    tail = float((arr >= tail_k).mean())
    return mean, tail


def run_test(symbols: Symbols, rs_params: RSParams, frame: int, step: int, tail_k: int) -> TestResult:
    ham = hamming_valid_rate(symbols.symbols)
    rs_mean, rs_tail = compute_scores(symbols.symbols, rs_params, frame=frame, step=step, tail_k=tail_k)
    return TestResult(symbols.name, ham, rs_mean, rs_tail)


def monte_carlo_pvalue(obs: float, null_values: List[float]) -> float:
    if not null_values:
        return float('nan')
    ge = sum(1 for v in null_values if v >= obs)
    return (1.0 + ge) / (1.0 + len(null_values))


def _plot_prime_gated_integrity(
    *,
    ells: np.ndarray,
    integrity: np.ndarray,
    title: str,
    highlight_ells: Sequence[int] = (137, 139),
    outpath: Optional[str] = None,
) -> None:
    """Scatter: integrity vs ell, colored by prime/composite."""
    if plt is None:  # pragma: no cover
        return

    prime_mask = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    comp_mask = (ells >= 2) & (~prime_mask)

    plt.figure()
    plt.scatter(ells[prime_mask], integrity[prime_mask], s=12, label='Prime ℓ (P)')
    plt.scatter(ells[comp_mask], integrity[comp_mask], s=12, label='Composite ℓ (C)')

    # Highlight special nodes (e.g., 137, 139) if they are in range.
    for h in highlight_ells:
        w = np.where(ells == int(h))[0]
        if w.size:
            plt.scatter([int(h)], [float(integrity[w[0]])], s=90, marker='*', label=f'ℓ={h}')

    plt.xlabel('Multipole ℓ')
    plt.ylabel('Hamming(8,4) validity rate (per-ℓ shell)')
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    if outpath:
        plt.savefig(outpath, dpi=150)
    else:
        plt.show()


def _plot_prime_gated_null_hist(
    *,
    null_deltas: np.ndarray,
    real_delta: float,
    title: str,
    outpath: Optional[str] = None,
) -> None:
    """Histogram: Δmean(P−C) under a null, with real delta shown as a line."""
    if plt is None:  # pragma: no cover
        return
    if null_deltas.size == 0 or not np.isfinite(real_delta):
        return
    plt.figure()
    plt.hist(null_deltas, bins=40)
    plt.axvline(real_delta, linewidth=2, label=f'Real Δmean(P−C) = {real_delta:.6g}')
    plt.xlabel('Δmean(P) − mean(C)')
    plt.ylabel('Count')
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    if outpath:
        plt.savefig(outpath, dpi=150)
    else:
        plt.show()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--lmin', type=int, default=DEFAULT_LMIN, help='minimum ell to include (default: 2)')
    ap.add_argument('--lmax', type=int, default=1024)
    ap.add_argument('--tt-map', type=str, default=None, help='HEALPix FITS map for temperature')
    ap.add_argument('--tt-alm', type=str, default=None, help='FITS alm for temperature')
    ap.add_argument('--q-map', type=str, default=None, help='HEALPix FITS Q map')
    ap.add_argument('--u-map', type=str, default=None, help='HEALPix FITS U map')
    ap.add_argument('--e-alm', type=str, default=None, help='FITS alm for E')
    ap.add_argument('--b-alm', type=str, default=None, help='FITS alm for B')
    ap.add_argument('--mc', type=int, default=50, help='Monte Carlo iterations for null N1')
    ap.add_argument('--frame', type=int, default=255)
    ap.add_argument('--step', type=int, default=255, help='window step (default 255 = non-overlapping)')
    ap.add_argument('--max-frames', type=int, default=4096, help='limit number of windows per run (sampled). 0 disables')
    ap.add_argument('--tail-k', type=int, default=8, help='tail threshold on zero-syndrome count')
    ap.add_argument('--seed', type=int, default=12345)
    ap.add_argument('--progress', dest='progress', action='store_true', help='enable progress display (default: on if TTY)')
    ap.add_argument('--no-progress', dest='progress', action='store_false', help='disable progress display')

    # Prime-gated fingerprint view: compares per-ell Hamming purity for primes vs composites.
    ap.add_argument('--prime-gated', action='store_true', help='enable Prime-Gated per-ell analysis (plots + Δmean(P−C))')
    ap.add_argument('--prime-perm', type=int, default=5000, help='permutation null samples for Prime-Gated test (default: 5000)')
    ap.add_argument('--prime-plot-prefix', type=str, default=None, help='if set, save plots to <prefix>_<label>_*.png')
    ap.add_argument('--prime-highlight', type=str, default='137,139', help='comma-separated ell values to highlight (default: 137,139)')

    ap.set_defaults(progress=sys.stderr.isatty())

    args = ap.parse_args(argv)


    # RS parameters and RNG
    rs_params = _make_rs_params(RSParams, n=255, k=201, nsym=54)
    rng = np.random.default_rng(args.seed)
    _require_healpy()

    # Load TT
    tt_alm = None
    if args.tt_alm:
        tt_alm = load_alm_fits(args.tt_alm)
    elif args.tt_map:
        tt_alm = load_alm_from_map(args.tt_map, lmax=args.lmax)

    if tt_alm is None:
        raise SystemExit('Provide --tt-map or --tt-alm')

    symbols_all: List[Tuple[str, np.ndarray, np.ndarray]] = []  # (label, alm, symbols)
    tt_sym = build_symbol_stream_from_alm(tt_alm, args.lmax, 'TT', lmin=args.lmin)
    symbols_all.append(('TT', tt_alm, tt_sym.symbols))

    # Load polarization
    if args.e_alm and args.b_alm:
        e_alm = load_alm_fits(args.e_alm)
        b_alm = load_alm_fits(args.b_alm)
        e_sym = build_symbol_stream_from_alm(e_alm, args.lmax, 'EE', lmin=args.lmin)
        b_sym = build_symbol_stream_from_alm(b_alm, args.lmax, 'BB', lmin=args.lmin)
        symbols_all.append(('EE', e_alm, e_sym.symbols))
        symbols_all.append(('BB', b_alm, b_sym.symbols))
    elif args.q_map and args.u_map:
        e_alm, b_alm = load_almE_B_from_qu_maps(args.q_map, args.u_map, lmax=args.lmax)
        e_sym = build_symbol_stream_from_alm(e_alm, args.lmax, 'EE', lmin=args.lmin)
        b_sym = build_symbol_stream_from_alm(b_alm, args.lmax, 'BB', lmin=args.lmin)
        symbols_all.append(('EE', e_alm, e_sym.symbols))
        symbols_all.append(('BB', b_alm, b_sym.symbols))

    print('=== Observed scores ===', flush=True)
    observed: Dict[str, TestResult] = {}
    for label, alm, sym in symbols_all:
        tr = run_test(Symbols(label, sym), rs_params, frame=args.frame, step=args.step, tail_k=args.tail_k)
        observed[label] = tr
        print(f'{label}: hamming_rate={tr.hamming_rate:.6f}  rs_mean_zero={tr.rs_mean_zero_syndromes:.3f}  rs_tail_rate(>={args.tail_k})={tr.rs_tail_rate:.6f}')

    # --- Prime-Gated fingerprint (Real) ---
    # This is the per-multipole "digital purity" view: compute integrity(ell) for each ell
    # and compare primes (set P) vs composites (set C).
    prime_real: Dict[str, Dict[str, object]] = {}
    if args.prime_gated:
        # Parse highlight ells (default: 137,139)
        try:
            highlight_ells = [int(x.strip()) for x in str(args.prime_highlight).split(',') if x.strip()]
        except Exception:
            highlight_ells = [137, 139]

        print('\n=== Prime-Gated (Real): per-ell Hamming purity ===', flush=True)
        for label, alm, sym in symbols_all:
            ells_pg, integ_pg = prime_gated_integrity_curve(sym, args.lmin, args.lmax)
            delta_real = prime_gated_delta_mean(ells_pg, integ_pg)

            # Permutation null: keeps the integrity curve fixed, shuffles prime labels.
            perm_deltas = permutation_null_deltas(ells_pg, integ_pg, n_perm=int(args.prime_perm), rng=rng)
            finite_perm = perm_deltas[np.isfinite(perm_deltas)]
            if finite_perm.size and np.isfinite(delta_real):
                p_perm_two_sided = float((np.sum(np.abs(finite_perm) >= abs(delta_real)) + 1) / (finite_perm.size + 1))
            else:
                p_perm_two_sided = float('nan')

            print(
                f'{label}: Δmean(P−C)={delta_real:.6g}  '
                f'perm_p(two-sided)={p_perm_two_sided:.4g}  (perm={int(args.prime_perm)})'
            )

            # Save for MC comparison later.
            prime_real[label] = {
                'ells': ells_pg,
                'integrity': integ_pg,
                'delta': delta_real,
                'perm_deltas': perm_deltas,
                'highlight_ells': highlight_ells,
                'perm_p_two_sided': p_perm_two_sided,
            }

            # Optional plot saving.
            if args.prime_plot_prefix:
                prefix = str(args.prime_plot_prefix)
                _plot_prime_gated_integrity(
                    ells=ells_pg,
                    integrity=integ_pg,
                    title=(
                        f'Prime-Gated integrity vs ℓ ({label}, Real)  '
                        f'Δmean={delta_real:.3g}, perm_p≈{p_perm_two_sided:.3g}'
                    ),
                    highlight_ells=highlight_ells,
                    outpath=f'{prefix}_{label}_prime_gated_integrity.png',
                )
                if finite_perm.size:
                    _plot_prime_gated_null_hist(
                        null_deltas=finite_perm,
                        real_delta=float(delta_real),
                        title=f'Prime-Gated Δmean(P−C) permutation null ({label})',
                        outpath=f'{prefix}_{label}_prime_gated_perm_null.png',
                    )

    # Monte Carlo null
    print('\n=== Monte Carlo (phase randomization per ell) ===', flush=True)
    for label, alm, sym in symbols_all:
        null_means: List[float] = []
        null_tails: List[float] = []
        # Optional: Prime-Gated deltas (Δmean(P−C)) under the MC null.
        null_prime_deltas: List[float] = []
        obs_mean = observed[label].rs_mean_zero_syndromes
        obs_tail = observed[label].rs_tail_rate

        ge_mean = 0
        ge_tail = 0
        mc_prog = _Progress(args.progress, total=args.mc, desc=f'{label} MC', unit='mc')
        for i_mc in range(args.mc):
            a_null = phase_randomize_per_ell(alm, args.lmax, rng, lmin=args.lmin)
            s_null = build_symbol_stream_from_alm(a_null, args.lmax, name=label, lmin=args.lmin).symbols
            mf = None if args.max_frames == 0 else args.max_frames
            mean, tail = compute_scores(
                s_null,
                rs_params,
                frame=args.frame,
                step=args.step,
                tail_k=args.tail_k,
                max_frames=mf,
                rng=rng,
            )
            null_means.append(mean)
            null_tails.append(tail)

            # Prime-Gated null: compute Δmean(P−C) for this MC realization.
            # This is the key "MC sees no difference" check when compared to real Δ.
            if args.prime_gated and label in prime_real:
                d_mc = prime_gated_delta_from_symbol_stream(s_null, args.lmin, args.lmax)
                null_prime_deltas.append(float(d_mc))

            # Running p-value estimate (one-sided, >= observed)
            if mean >= obs_mean:
                ge_mean += 1
            if tail >= obs_tail:
                ge_tail += 1

            # Update progress occasionally to reduce overhead.
            postfix = None
            if (i_mc + 1) % 5 == 0 or (i_mc + 1) == args.mc:
                p_est_mean = (1.0 + ge_mean) / (1.0 + (i_mc + 1))
                p_est_tail = (1.0 + ge_tail) / (1.0 + (i_mc + 1))
                postfix = {
                    'p_mean': f'{p_est_mean:.4g}',
                    'p_tail': f'{p_est_tail:.4g}',
                }

            if postfix:
                mc_prog.update(1, **postfix)
            else:
                mc_prog.update(1)

        mc_prog.close()

        p_mean = monte_carlo_pvalue(observed[label].rs_mean_zero_syndromes, null_means)
        p_tail = monte_carlo_pvalue(observed[label].rs_tail_rate, null_tails)

        print(f'{label}: p(rs_mean_zero)={p_mean:.4g}  p(rs_tail_rate)={p_tail:.4g}  (mc={args.mc})')

        # Report Prime-Gated behavior under phase-randomization MC.
        if args.prime_gated and label in prime_real:
            real_delta = float(prime_real[label]['delta'])
            mc_arr = np.array(null_prime_deltas, dtype=float)
            mc_arr = mc_arr[np.isfinite(mc_arr)]

            if mc_arr.size and np.isfinite(real_delta):
                p_mc_two_sided = float((np.sum(np.abs(mc_arr) >= abs(real_delta)) + 1) / (mc_arr.size + 1))
                mc_mu = float(np.mean(mc_arr))
                mc_sd = float(np.std(mc_arr))
            else:
                p_mc_two_sided = float('nan')
                mc_mu = float('nan')
                mc_sd = float('nan')

            print(
                f'  [Prime-Gated null] Δmean(P−C): real={real_delta:.6g}  '
                f'mc_mean={mc_mu:.6g}  mc_std={mc_sd:.6g}  mc_p(two-sided)={p_mc_two_sided:.4g}'
            )

            # Optional plot saving.
            if args.prime_plot_prefix and mc_arr.size:
                prefix = str(args.prime_plot_prefix)
                _plot_prime_gated_null_hist(
                    null_deltas=mc_arr,
                    real_delta=real_delta,
                    title=f'Prime-Gated Δmean(P−C) phase-randomization MC null ({label})',
                    outpath=f'{prefix}_{label}_prime_gated_mc_null.png',
                )

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
