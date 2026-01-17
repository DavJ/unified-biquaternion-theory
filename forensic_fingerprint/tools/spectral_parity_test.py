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
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

try:
    import healpy as hp
except Exception as e:  # pragma: no cover
    hp = None

from .rs_syndrome import RSParams, syndrome_zero_count


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


def iter_lm(lmax: int) -> Iterable[Tuple[int, int]]:
    for ell in range(0, lmax + 1):
        for m in range(-ell, ell + 1):
            yield ell, m


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


def hamming_valid_rate(symbols: np.ndarray) -> float:
    if symbols.size == 0:
        return float('nan')
    ok = 0
    for x in symbols.tolist():
        if hamming_8_4_is_valid(int(x)):
            ok += 1
    return ok / float(symbols.size)


def load_alm_from_map(map_path: str, lmax: int) -> np.ndarray:
    _require_healpy()
    m = hp.read_map(map_path, field=0, verbose=False)
    alm = hp.map2alm(m, lmax=lmax, pol=False, iter=3)
    return alm


def load_almE_B_from_qu_maps(q_path: str, u_path: str, lmax: int) -> Tuple[np.ndarray, np.ndarray]:
    _require_healpy()
    q = hp.read_map(q_path, field=0, verbose=False)
    u = hp.read_map(u_path, field=0, verbose=False)
    # spin-2 transform
    almE, almB = hp.map2alm_spin([q, u], spin=2, lmax=lmax, iter=3)
    return almE, almB


def load_alm_fits(path: str) -> np.ndarray:
    _require_healpy()
    return hp.read_alm(path)


def build_symbol_stream_from_alm(alm: np.ndarray, lmax: int, name: str) -> Symbols:
    """Build uint8 symbol stream using phase quantization, for all m in [-ell,ell].

    healpy stores only m>=0. For real fields, negative m are obtained by:
      a_{l,-m} = (-1)^m * conj(a_{l,m})
    """
    _require_healpy()
    sym = np.zeros(((lmax + 1) * (lmax + 1)), dtype=np.uint8)  # total modes up to lmax

    for ell in range(0, lmax + 1):
        # m=0
        a0 = hp.alm_getidx(lmax, ell, 0)
        sym[k_index(ell, 0)] = quantize_phase_to_u8(complex(alm[a0]))
        for m in range(1, ell + 1):
            idx = hp.alm_getidx(lmax, ell, m)
            a = complex(alm[idx])
            sym[k_index(ell, m)] = quantize_phase_to_u8(a)
            aneg = ((-1) ** m) * np.conj(a)
            sym[k_index(ell, -m)] = quantize_phase_to_u8(complex(aneg))

    return Symbols(name=name, symbols=sym)


def phase_randomize_per_ell(alm: np.ndarray, lmax: int, rng: np.random.Generator) -> np.ndarray:
    """Null model N1: randomize phases within each ell while preserving amplitudes."""
    _require_healpy()
    out = np.array(alm, copy=True)
    for ell in range(0, lmax + 1):
        # m=0 real mode: keep as is (or random sign); keep as is for safety.
        for m in range(1, ell + 1):
            idx = hp.alm_getidx(lmax, ell, m)
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


def compute_scores(symbols: np.ndarray, rs_params: RSParams, frame: int = 255, step: int = 1, tail_k: int = 8) -> Tuple[float, float]:
    """Return (mean_zero_count, tail_rate) for RS syndrome zeros."""
    counts: List[int] = []
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--lmax', type=int, default=1024)
    ap.add_argument('--tt-map', type=str, default=None, help='HEALPix FITS map for temperature')
    ap.add_argument('--tt-alm', type=str, default=None, help='FITS alm for temperature')
    ap.add_argument('--q-map', type=str, default=None, help='HEALPix FITS Q map')
    ap.add_argument('--u-map', type=str, default=None, help='HEALPix FITS U map')
    ap.add_argument('--e-alm', type=str, default=None, help='FITS alm for E')
    ap.add_argument('--b-alm', type=str, default=None, help='FITS alm for B')
    ap.add_argument('--mc', type=int, default=50, help='Monte Carlo iterations for null N1')
    ap.add_argument('--frame', type=int, default=255)
    ap.add_argument('--step', type=int, default=1)
    ap.add_argument('--tail-k', type=int, default=8, help='tail threshold on zero-syndrome count')
    ap.add_argument('--seed', type=int, default=12345)

    args = ap.parse_args()

    _require_healpy()

    rs_params = RSParams(n=255, k=201)

    rng = np.random.default_rng(args.seed)

    # Load TT
    tt_alm = None
    if args.tt_alm:
        tt_alm = load_alm_fits(args.tt_alm)
    elif args.tt_map:
        tt_alm = load_alm_from_map(args.tt_map, lmax=args.lmax)

    if tt_alm is None:
        raise SystemExit('Provide --tt-map or --tt-alm')

    symbols_all: List[Tuple[str, np.ndarray, np.ndarray]] = []  # (label, alm, symbols)
    tt_sym = build_symbol_stream_from_alm(tt_alm, args.lmax, 'TT')
    symbols_all.append(('TT', tt_alm, tt_sym.symbols))

    # Load polarization
    if args.e_alm and args.b_alm:
        e_alm = load_alm_fits(args.e_alm)
        b_alm = load_alm_fits(args.b_alm)
        e_sym = build_symbol_stream_from_alm(e_alm, args.lmax, 'EE')
        b_sym = build_symbol_stream_from_alm(b_alm, args.lmax, 'BB')
        symbols_all.append(('EE', e_alm, e_sym.symbols))
        symbols_all.append(('BB', b_alm, b_sym.symbols))
    elif args.q_map and args.u_map:
        e_alm, b_alm = load_almE_B_from_qu_maps(args.q_map, args.u_map, lmax=args.lmax)
        e_sym = build_symbol_stream_from_alm(e_alm, args.lmax, 'EE')
        b_sym = build_symbol_stream_from_alm(b_alm, args.lmax, 'BB')
        symbols_all.append(('EE', e_alm, e_sym.symbols))
        symbols_all.append(('BB', b_alm, b_sym.symbols))

    print('=== Observed scores ===')
    observed: Dict[str, TestResult] = {}
    for label, alm, sym in symbols_all:
        tr = run_test(Symbols(label, sym), rs_params, frame=args.frame, step=args.step, tail_k=args.tail_k)
        observed[label] = tr
        print(f'{label}: hamming_rate={tr.hamming_rate:.6f}  rs_mean_zero={tr.rs_mean_zero_syndromes:.3f}  rs_tail_rate(>={args.tail_k})={tr.rs_tail_rate:.6f}')

    # Monte Carlo null
    print('\n=== Monte Carlo (phase randomization per ell) ===')
    for label, alm, sym in symbols_all:
        null_means: List[float] = []
        null_tails: List[float] = []
        for _ in range(args.mc):
            a_null = phase_randomize_per_ell(alm, args.lmax, rng)
            s_null = build_symbol_stream_from_alm(a_null, args.lmax, name=label).symbols
            mean, tail = compute_scores(s_null, rs_params, frame=args.frame, step=args.step, tail_k=args.tail_k)
            null_means.append(mean)
            null_tails.append(tail)

        p_mean = monte_carlo_pvalue(observed[label].rs_mean_zero_syndromes, null_means)
        p_tail = monte_carlo_pvalue(observed[label].rs_tail_rate, null_tails)

        print(f'{label}: p(rs_mean_zero)={p_mean:.4g}  p(rs_tail_rate)={p_tail:.4g}  (mc={args.mc})')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
