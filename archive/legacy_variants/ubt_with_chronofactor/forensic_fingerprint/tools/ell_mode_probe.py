#!/usr/bin/env python3
"""Ell-space probe for potential modes at specific multipoles (e.g., ell=137,139).

This is a complement to `spectral_resonance_v4.py`.
It avoids the `target-mode=inv` assumption and instead works directly with
spherical-harmonic coefficients a_{ell m}.

It computes:
  S(ell): within-ell phase concentration
  C(ell1,ell2): cross-ell phase coherence

Null model: empirical (within the chosen ell-window)
  - p_S(target) computed against the distribution of S(ell) over ell in [lmin,lmax]
  - p_C(pair) computed against random ell-pairs drawn from [lmin,lmax]

Notes:
  * This does not prove cosmological origin. It's a targeted diagnostic designed
    to test "ell=137/139 as modes" without FFT leakage artifacts.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import healpy as hp


def _parse_csv_list(s: str) -> List[str]:
    return [x.strip() for x in (s or "").split(",") if x.strip()]


def _parse_ints(s: str) -> List[int]:
    return [int(x) for x in _parse_csv_list(s)]


def _map2alm_spin_compat(qu_maps, spin: int, lmax: int):
    """Compat wrapper for healpy.map2alm_spin signature differences."""
    attempts = [
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, pol=False, iter=0),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, iter=0),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, pol=False),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax),
    ]
    for fn in attempts:
        try:
            return fn()
        except TypeError:
            continue
    return hp.map2alm_spin(qu_maps, spin, lmax)


def _alm_get(alm: np.ndarray, lmax_alm: int, ell: int, m: int) -> complex:
    return alm[hp.Alm.getidx(lmax_alm, ell, m)]


def phase_concentration_per_ell(alm: np.ndarray, lmax_alm: int, ell: int) -> float:
    """S(ell) = |mean_{m=1..ell} exp(i arg(a_{ell m}))|.

    We skip m=0 (real-only mode) to avoid degeneracy.
    """
    if ell < 1:
        return 0.0
    phases = []
    for m in range(1, ell + 1):
        a = _alm_get(alm, lmax_alm, ell, m)
        phases.append(np.exp(1j * np.angle(a)))
    v = np.mean(np.asarray(phases, dtype=np.complex128))
    return float(np.abs(v))


def cross_ell_coherence(alm: np.ndarray, lmax_alm: int, ell1: int, ell2: int) -> float:
    """C(ell1,ell2) = |mean_{m=1..min(ell1,ell2)} exp(i(arg(a1)-arg(a2)))|."""
    mmax = min(ell1, ell2)
    if mmax < 1:
        return 0.0
    vals = []
    for m in range(1, mmax + 1):
        a1 = _alm_get(alm, lmax_alm, ell1, m)
        a2 = _alm_get(alm, lmax_alm, ell2, m)
        vals.append(np.exp(1j * (np.angle(a1) - np.angle(a2))))
    v = np.mean(np.asarray(vals, dtype=np.complex128))
    return float(np.abs(v))


@dataclass
class ChannelResult:
    channel: str
    s_by_ell: Dict[int, float]
    c_pairs: Dict[Tuple[int, int], float]


def compute_channel_diagnostics(
    alm: np.ndarray,
    lmax_alm: int,
    lmin: int,
    lmax: int,
    targets: Sequence[int],
) -> ChannelResult:
    s_by_ell: Dict[int, float] = {}
    for ell in range(lmin, lmax + 1):
        s_by_ell[ell] = phase_concentration_per_ell(alm, lmax_alm, ell)

    c_pairs: Dict[Tuple[int, int], float] = {}
    tgt = sorted(set([t for t in targets if lmin <= t <= lmax]))
    for e1, e2 in combinations(tgt, 2):
        c_pairs[(e1, e2)] = cross_ell_coherence(alm, lmax_alm, e1, e2)

    return ChannelResult(channel="", s_by_ell=s_by_ell, c_pairs=c_pairs)


def empirical_p_ge(dist: np.ndarray, x: float) -> float:
    """One-sided empirical p-value: P(D >= x). Includes continuity safeguard."""
    n = len(dist)
    if n <= 0:
        return float("nan")
    return float((np.sum(dist >= x) + 1.0) / (n + 1.0))


def sample_pair_null(
    rng: np.random.Generator,
    ells: np.ndarray,
    n_samples: int,
) -> np.ndarray:
    """Sample random distinct ell-pairs from the window."""
    if len(ells) < 2:
        return np.empty((0, 2), dtype=int)
    a = rng.choice(ells, size=n_samples, replace=True)
    b = rng.choice(ells, size=n_samples, replace=True)
    # enforce distinct by resampling collisions (cheap loop)
    mask = a == b
    tries = 0
    while np.any(mask) and tries < 10:
        b[mask] = rng.choice(ells, size=int(np.sum(mask)), replace=True)
        mask = a == b
        tries += 1
    # still collisions? drop them
    ok = a != b
    pairs = np.stack([a[ok], b[ok]], axis=1)
    # normalize ordering so (e1,e2) == (e2,e1)
    pairs.sort(axis=1)
    return pairs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tt-map", help="IQU FITS or TT map FITS (field 0 used)")
    ap.add_argument("--q-map", help="Q map FITS")
    ap.add_argument("--u-map", help="U map FITS")
    ap.add_argument("--channels", default="TT,EE,BB", help="Comma list: TT,EE,BB")
    ap.add_argument("--lmin", type=int, default=2)
    ap.add_argument("--lmax", type=int, default=200)
    ap.add_argument("--lmax-alm", type=int, default=512)
    ap.add_argument("--targets", default="137,139", help="Comma list of target ells")
    ap.add_argument("--pair-null-samples", type=int, default=20000, help="Random pair samples for p_C")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--report-csv", help="Write per-ell S(ell) and target summaries")
    ap.add_argument("--plot-png", help="Optional plot of S(ell)")
    args = ap.parse_args()

    ch_list = [c.upper() for c in _parse_csv_list(args.channels)]
    targets = _parse_ints(args.targets)

    lmin, lmax = int(args.lmin), int(args.lmax)
    lmax_alm = int(args.lmax_alm)

    # Load alms
    alms: Dict[str, np.ndarray] = {}

    if "TT" in ch_list:
        if not args.tt_map:
            raise SystemExit("--tt-map is required for TT")
        # Many Planck IQU FITS have T in field 0.
        mT = hp.read_map(args.tt_map, field=0, verbose=False)
        alms["TT"] = hp.map2alm(mT, lmax=lmax_alm, iter=0)

    if ("EE" in ch_list) or ("BB" in ch_list):
        if not (args.q_map and args.u_map):
            raise SystemExit("--q-map and --u-map are required for EE/BB")
        q = hp.read_map(args.q_map, field=0, verbose=False)
        u = hp.read_map(args.u_map, field=0, verbose=False)
        e_alm, b_alm = _map2alm_spin_compat([q, u], spin=2, lmax=lmax_alm)
        alms["EE"] = e_alm
        alms["BB"] = b_alm

    rng = np.random.default_rng(args.seed)
    ell_window = np.arange(lmin, lmax + 1, dtype=int)

    results: Dict[str, ChannelResult] = {}
    for ch in ch_list:
        if ch not in alms:
            continue
        cr = compute_channel_diagnostics(alms[ch], lmax_alm, lmin, lmax, targets)
        cr.channel = ch
        results[ch] = cr

    # Compute empirical p-values
    # p_S for each target: compare S(target) against S(ell) over full window
    summary_rows: List[Dict[str, object]] = []

    for ch, cr in results.items():
        s_dist = np.asarray([cr.s_by_ell[ell] for ell in ell_window], dtype=float)

        print(f"\n[{ch}] ell=[{lmin},{lmax}] targets={targets}")
        for t in targets:
            if not (lmin <= t <= lmax):
                continue
            s_t = cr.s_by_ell[t]
            p_s = empirical_p_ge(s_dist, s_t)
            print(f"  S(ell={t})={s_t:.6f}  p_emp={p_s:.4f}")
            summary_rows.append({
                "channel": ch,
                "stat": "S",
                "ell1": t,
                "ell2": "",
                "value": s_t,
                "p_emp": p_s,
            })

        # Pair coherence
        if cr.c_pairs:
            # build null by sampling random pairs and computing C for each
            pairs = sample_pair_null(rng, ell_window, args.pair_null_samples)
            # precompute phases per (ell,m) for speed: store arrays of exp(i*angle)
            # But keep memory light: compute on the fly per pair.
            for (e1, e2), c_obs in cr.c_pairs.items():
                c_null = np.empty((len(pairs),), dtype=float)
                for i, (a, b) in enumerate(pairs):
                    c_null[i] = cross_ell_coherence(alms[ch], lmax_alm, int(a), int(b))
                p_c = empirical_p_ge(c_null, c_obs)
                print(f"  C(ell={e1},{e2})={c_obs:.6f}  p_emp={p_c:.4f}  (null_pairs={len(c_null)})")
                summary_rows.append({
                    "channel": ch,
                    "stat": "C",
                    "ell1": e1,
                    "ell2": e2,
                    "value": c_obs,
                    "p_emp": p_c,
                })

    # CSV report
    if args.report_csv:
        out = Path(args.report_csv)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["channel", "ell", "S"])
            w.writeheader()
            for ch, cr in results.items():
                for ell in ell_window:
                    w.writerow({"channel": ch, "ell": int(ell), "S": cr.s_by_ell[int(ell)]})
        # Also write a compact *_summary.csv next to it
        s_out = out.with_name(out.stem + "_summary.csv")
        with s_out.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["channel", "stat", "ell1", "ell2", "value", "p_emp"])
            w.writeheader()
            for r in summary_rows:
                w.writerow(r)
        print(f"[info] wrote CSV: {out}")
        print(f"[info] wrote CSV: {s_out}")

    # Optional plot
    if args.plot_png:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        outp = Path(args.plot_png)
        outp.parent.mkdir(parents=True, exist_ok=True)

        for ch, cr in results.items():
            xs = ell_window
            ys = np.asarray([cr.s_by_ell[int(ell)] for ell in xs], dtype=float)
            plt.figure()
            plt.plot(xs, ys)
            for t in targets:
                if lmin <= t <= lmax:
                    plt.axvline(t, linestyle="--")
            plt.title(f"Phase concentration S(ell) - {ch}")
            plt.xlabel("ell")
            plt.ylabel("S(ell)")
            # write one PNG per channel by suffixing
            ch_out = outp.with_name(outp.stem + f"_{ch}" + outp.suffix)
            plt.savefig(ch_out, dpi=150)
            plt.close()
            print(f"[info] wrote PNG: {ch_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
