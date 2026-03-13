#!/usr/bin/env python3
"""
spectral_resonance_v3.py
Clean forensic spectral test: look for PSD peaks near 1/137 and 1/139
in a 1D stream built from alm phases.

- Builds unit phasor stream z = alm/|alm| in selected ell band.
- Computes PSD (optionally Welch-averaged).
- Estimates p-values by phase randomization per ell (MC).
- Optionally writes CSV + PNG.

No SciPy required.
"""

from __future__ import annotations
import argparse
import csv
import math
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np

try:
    import healpy as hp
except Exception as e:
    hp = None
    _HP_ERR = e
else:
    _HP_ERR = None

def _require_healpy():
    if hp is None:
        raise RuntimeError(f"healpy import failed: {_HP_ERR}")

def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tt-map", type=str, required=True)
    ap.add_argument("--q-map", type=str, default=None)
    ap.add_argument("--u-map", type=str, default=None)

    ap.add_argument("--lmin", type=int, default=128)
    ap.add_argument("--lmax", type=int, default=146)
    ap.add_argument("--lmax-alm", type=int, default=512)

    ap.add_argument("--channels", type=str, default="TT",
                    help="Comma-separated: TT,EE,BB (EE/BB require q-map/u-map)")

    ap.add_argument("--use-full-m", action="store_true",
                    help="Include full m (requires reconstructing negative-m consistently). "
                         "Default uses only m>=0 entries as produced by healpy indexing.")

    ap.add_argument("--welch", action="store_true", help="Use simple Welch PSD average.")
    ap.add_argument("--welch-seg", type=int, default=4096, help="Welch segment length.")
    ap.add_argument("--welch-overlap", type=float, default=0.5, help="Welch overlap fraction [0,1).")

    ap.add_argument("--mc", type=int, default=0, help="MC count for p-values (phase randomization per ell).")
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--f0", type=float, default=1.0/137.036, help="Target frequency 1/k (default 1/137.036).")
    ap.add_argument("--f1", type=float, default=1.0/139.0, help="Second target frequency 1/k (default 1/139).")
    ap.add_argument("--report-csv", type=str, default=None)
    ap.add_argument("--plot-png", type=str, default=None)
    return ap

def _read_alms(args) -> Dict[str, np.ndarray]:
    _require_healpy()
    lmax = int(args.lmax_alm)

    # TT
    mT = hp.read_map(args.tt_map, field=0, verbose=False)
    almT = hp.map2alm(mT, lmax=lmax)

    out = {"TT": almT}

    if "EE" in args.channels or "BB" in args.channels:
        if not args.q_map or not args.u_map:
            raise ValueError("EE/BB requested but --q-map/--u-map missing.")
        q = hp.read_map(args.q_map, verbose=False)
        u = hp.read_map(args.u_map, verbose=False)
        e, b = hp.map2alm_spin([q, u], spin=2, lmax=lmax)
        out["EE"] = e
        out["BB"] = b

    return out

def _unit_phasor(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.complex128)
    a = np.abs(x)
    # guard: zeros -> 0 phasor
    out = np.zeros_like(x, dtype=np.complex128)
    m = a > 0
    out[m] = x[m] / a[m]
    return out

def _stream_from_alm(alm: np.ndarray, lmin: int, lmax: int, lmax_alm: int,
                     use_full_m: bool) -> np.ndarray:
    """
    Default: use healpy's packed alm entries (m>=0 only) restricted to ell band.
    If use_full_m: reconstruct a full (-m..+m) stream per ell using conjugation symmetry.
    """
    _require_healpy()
    size = hp.Alm.getsize(lmax_alm)
    idx = np.arange(size)
    ell, m = hp.Alm.getlm(lmax_alm, idx)

    band = (ell >= lmin) & (ell <= lmax)
    alm_band = alm[band]
    ell_band = ell[band]
    m_band = m[band]

    if not use_full_m:
        # stream in healpy natural order within band
        z = _unit_phasor(alm_band)
        # remove mean to reduce DC dominance
        z = z - np.mean(z)
        return z

    # Build explicit per-ell stream: m=-ell..+ell
    streams: List[np.ndarray] = []
    for e in range(lmin, lmax + 1):
        mask_e = (ell_band == e)
        if not np.any(mask_e):
            continue
        # for this ell, we have m=0..e from healpy
        alm_e = alm_band[mask_e]
        m_e = m_band[mask_e]

        # map m->alm
        arr = np.zeros(2*e + 1, dtype=np.complex128)
        # indices: m=-e..+e mapped to 0..2e
        for a, mm in zip(alm_e, m_e):
            mm = int(mm)
            arr[e + mm] = a
            if mm > 0:
                # a_{l,-m} = (-1)^m * conj(a_{l,m})
                arr[e - mm] = ((-1)**mm) * np.conjugate(a)

        streams.append(_unit_phasor(arr))

    z = np.concatenate(streams) if streams else np.zeros(0, dtype=np.complex128)
    if z.size:
        z = z - np.mean(z)
    return z

def _psd_rfft(z: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    PSD of complex sequence using rfft on real/imag separately -> sum.
    This avoids losing information by taking only np.real(z).
    """
    z = np.asarray(z, dtype=np.complex128)
    n = z.size
    if n < 8:
        return np.zeros(0), np.zeros(0)
    xr = np.real(z)
    xi = np.imag(z)
    Fr = np.fft.rfft(xr)
    Fi = np.fft.rfft(xi)
    psd = (np.abs(Fr)**2 + np.abs(Fi)**2) / float(n)
    freqs = np.fft.rfftfreq(n, d=1.0)
    return freqs, psd

def _psd_welch(z: np.ndarray, seg: int, overlap_frac: float) -> Tuple[np.ndarray, np.ndarray]:
    z = np.asarray(z, dtype=np.complex128)
    n = z.size
    if n < max(16, seg):
        return _psd_rfft(z)

    seg = int(seg)
    overlap = int(seg * float(overlap_frac))
    step = max(1, seg - overlap)

    # Hann window
    w = 0.5 - 0.5 * np.cos(2.0 * np.pi * np.arange(seg) / (seg - 1))
    w_norm = np.sum(w**2)

    acc_psd = None
    count = 0
    for start in range(0, n - seg + 1, step):
        chunk = z[start:start+seg]
        # apply window to real and imag
        cw = (np.real(chunk) * w) + 1j * (np.imag(chunk) * w)
        freqs, psd = _psd_rfft(cw)
        # correct for window power
        psd = psd / (w_norm / seg)
        if acc_psd is None:
            acc_psd = psd.copy()
        else:
            acc_psd += psd
        count += 1

    if acc_psd is None or count == 0:
        return _psd_rfft(z)
    return freqs, acc_psd / float(count)

def _nearest_bin(freqs: np.ndarray, f: float) -> int:
    if freqs.size == 0:
        return -1
    return int(np.argmin(np.abs(freqs - float(f))))

def _phase_randomize_per_ell(alm: np.ndarray, lmax_alm: int, rng: np.random.Generator) -> np.ndarray:
    _require_healpy()
    out = alm.copy()
    size = hp.Alm.getsize(lmax_alm)
    idx = np.arange(size)
    ell, _m = hp.Alm.getlm(lmax_alm, idx)
    for e in range(lmax_alm + 1):
        mask = (ell == e)
        if not np.any(mask):
            continue
        ph = rng.uniform(-np.pi, np.pi, size=int(np.sum(mask)))
        out[mask] = np.abs(out[mask]) * (np.cos(ph) + 1j*np.sin(ph))
    return out

@dataclass
class PeakResult:
    f0: float
    f1: float
    idx0: int
    idx1: int
    p0: float
    p1: float

def _peak_pvalues(freqs: np.ndarray, psd: np.ndarray, f0: float, f1: float,
                  mc_psd0: Optional[np.ndarray], mc_psd1: Optional[np.ndarray]) -> PeakResult:
    idx0 = _nearest_bin(freqs, f0)
    idx1 = _nearest_bin(freqs, f1)
    obs0 = float(psd[idx0]) if idx0 >= 0 else float("nan")
    obs1 = float(psd[idx1]) if idx1 >= 0 else float("nan")

    def pv(obs: float, mc: Optional[np.ndarray]) -> float:
        if mc is None or mc.size == 0 or not np.isfinite(obs):
            return float("nan")
        return float((np.sum(mc >= obs) + 1.0) / (mc.size + 1.0))

    return PeakResult(f0=f0, f1=f1, idx0=idx0, idx1=idx1,
                      p0=pv(obs0, mc_psd0), p1=pv(obs1, mc_psd1))

def main() -> int:
    args = build_arg_parser().parse_args()
    ch_list = [c.strip().upper() for c in args.channels.split(",") if c.strip()]
    args.channels = ch_list

    _require_healpy()
    rng = np.random.default_rng(int(args.seed))

    alms = _read_alms(args)

    results = []
    rows_csv = []

    for ch in ch_list:
        if ch not in alms:
            print(f"[warn] channel {ch} not available, skipping.")
            continue

        alm = alms[ch]
        z = _stream_from_alm(alm, args.lmin, args.lmax, args.lmax_alm, args.use_full_m)

        if z.size < 64:
            print(f"[warn] channel {ch}: stream too short (n={z.size}), skipping.")
            continue

        if args.welch:
            freqs, psd = _psd_welch(z, args.welch_seg, args.welch_overlap)
        else:
            freqs, psd = _psd_rfft(z)

        mc0 = mc1 = None
        if int(args.mc) > 0:
            mc = int(args.mc)
            mc0 = np.zeros(mc, dtype=float)
            mc1 = np.zeros(mc, dtype=float)
            idx0 = _nearest_bin(freqs, args.f0)
            idx1 = _nearest_bin(freqs, args.f1)
            for i in range(mc):
                alm_r = _phase_randomize_per_ell(alm, args.lmax_alm, rng)
                z_r = _stream_from_alm(alm_r, args.lmin, args.lmax, args.lmax_alm, args.use_full_m)
                if args.welch:
                    _f, _psd = _psd_welch(z_r, args.welch_seg, args.welch_overlap)
                else:
                    _f, _psd = _psd_rfft(z_r)
                mc0[i] = float(_psd[idx0]) if idx0 >= 0 else float("nan")
                mc1[i] = float(_psd[idx1]) if idx1 >= 0 else float("nan")

        pk = _peak_pvalues(freqs, psd, args.f0, args.f1, mc0, mc1)

        print(f"\n[{ch}] stream_n={z.size}  f0={pk.f0:.6g}  f1={pk.f1:.6g}")
        print(f"  PSD(f0)={psd[pk.idx0]:.6g}  p_mc={pk.p0}")
        print(f"  PSD(f1)={psd[pk.idx1]:.6g}  p_mc={pk.p1}")

        results.append((ch, freqs, psd, pk))
        if args.report_csv:
            rows_csv.append({
                "channel": ch,
                "lmin": args.lmin, "lmax": args.lmax, "lmax_alm": args.lmax_alm,
                "use_full_m": bool(args.use_full_m),
                "welch": bool(args.welch),
                "f0": pk.f0, "f1": pk.f1,
                "idx0": pk.idx0, "idx1": pk.idx1,
                "psd_f0": float(psd[pk.idx0]),
                "psd_f1": float(psd[pk.idx1]),
                "p_mc_f0": pk.p0, "p_mc_f1": pk.p1,
                "mc": int(args.mc)
            })

    if args.report_csv and rows_csv:
        os.makedirs(os.path.dirname(args.report_csv) or ".", exist_ok=True)
        with open(args.report_csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows_csv[0].keys()))
            w.writeheader()
            w.writerows(rows_csv)
        print(f"\n[info] wrote CSV: {args.report_csv}")

    if args.plot_png and results:
        import matplotlib.pyplot as plt
        os.makedirs(os.path.dirname(args.plot_png) or ".", exist_ok=True)
        plt.figure()
        for (ch, freqs, psd, pk) in results:
            plt.semilogy(freqs, psd, label=ch)
        plt.axvline(args.f0, linestyle="--", alpha=0.7)
        plt.axvline(args.f1, linestyle="--", alpha=0.7)
        plt.xlabel("frequency [1/index]")
        plt.ylabel("PSD (arb.)")
        plt.title(f"Phase-stream PSD  ell=[{args.lmin},{args.lmax}]  full_m={args.use_full_m}  welch={args.welch}")
        plt.legend()
        plt.grid(True, which="both", alpha=0.25)
        plt.tight_layout()
        plt.savefig(args.plot_png, dpi=160)
        print(f"[info] wrote PNG: {args.plot_png}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())

