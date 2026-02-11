#!/usr/bin/env python3
"""
spectral_resonance_v4.py (v4.2 patch: adds --target-correlation)

Run example (your failing command becomes valid):

  MPLBACKEND=Agg python -m forensic_fingerprint.tools.spectral_resonance_v4 \
    --tt-map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
    --q-map  data/planck_pr3/maps/extracted/SMICA_Q.fits \
    --u-map  data/planck_pr3/maps/extracted/SMICA_U.fits \
    --lmin 2 --lmax 512 --lmax-alm 512 \
    --channels BB \
    --targets 137,139 --target-mode bin \
    --scan 136:140:1 \
    --mc 500 --seed 0 \
    --report-csv scans/resonance_v4_scan_bins_136_140.csv \
    --plot-png scans/resonance_v4_scan_bins_136_140.png

Meaning of target-mode:
  inv  : treat targets as periods p -> frequency f=1/p
  freq : treat targets as frequencies f (cycles/sample)
  bin  : treat targets as FFT bin indices k -> f=k/N

Monte Carlo null: per-ell phase randomization (preserves |a_lm| and intra-ell structure).
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import healpy as hp

def _map2alm_spin_compat(qu_maps, spin: int, lmax: int):
    """Compatibility wrapper for healpy.map2alm_spin across healpy versions.

    Some versions accept args like pol=..., iter=..., others don't.
    We try the common signatures in a safe order.
    """
    # Try most explicit forms first, then fall back.
    attempts = [
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, pol=False, iter=0),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, iter=0),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax, pol=False),
        lambda: hp.map2alm_spin(qu_maps, spin=spin, lmax=lmax),
        lambda: hp.map2alm_spin(qu_maps, spin, lmax),
    ]
    last_err = None
    for fn in attempts:
        try:
            return fn()
        except TypeError as e:
            last_err = e
            continue
    raise last_err

def _parse_list_csv(s: str) -> List[str]:
    return [x.strip() for x in (s or "").split(",") if x.strip()]


def _parse_floats_csv(s: str) -> List[float]:
    out: List[float] = []
    for tok in _parse_list_csv(s):
        out.append(float(tok))
    return out


def _parse_range(s: str) -> Tuple[float, float, float]:
    parts = (s or "").split(":")
    if len(parts) != 3:
        raise ValueError(f"Invalid --scan '{s}', expected a:b:step")
    a, b, step = (float(parts[0]), float(parts[1]), float(parts[2]))
    if step <= 0:
        raise ValueError("scan step must be > 0")
    if b < a:
        raise ValueError("scan requires b >= a")
    return a, b, step


def _frange(a: float, b: float, step: float) -> List[float]:
    n = int(math.floor((b - a) / step + 1e-12)) + 1
    xs = [a + i * step for i in range(n)]
    if xs and xs[-1] + 1e-10 < b:
        xs.append(b)
    return xs


def _hann(n: int) -> np.ndarray:
    if n <= 1:
        return np.ones((n,), dtype=float)
    return np.hanning(n)


def _fft_psd(x: np.ndarray, window: str = "hann") -> Tuple[np.ndarray, np.ndarray]:
    n = int(x.shape[0])
    if n == 0:
        raise ValueError("Empty stream")

    if window == "hann":
        w = _hann(n).astype(float)
        xw = x * w
        wnorm = float(np.mean(w**2))
        if wnorm > 0:
            xw = xw / math.sqrt(wnorm)
    elif window == "none":
        xw = x
    else:
        raise ValueError(f"Unknown window: {window}")

    X = np.fft.fft(xw)
    freqs = np.fft.fftfreq(n)  # [-0.5..0.5)
    pos = freqs >= 0
    freqs_pos = freqs[pos]
    X_pos = X[pos]
    psd = (np.abs(X_pos) ** 2) / n
    return freqs_pos, psd


def _idx_from_freq(n: int, f: float) -> int:
    if f < 0:
        f = -f
    k = int(round(f * n))
    kmax = n // 2
    if k > kmax:
        k = kmax
    return k


def _iter_stream_coeffs(alm: np.ndarray, lmax_alm: int, lmin: int, lmax: int, use_full_m: bool) -> Iterable[complex]:
    for ell in range(lmin, lmax + 1):
        for m in range(0, ell + 1):
            idx = hp.Alm.getidx(lmax_alm, ell, m)
            yield alm[idx]
        if use_full_m:
            for m in range(1, ell + 1):
                idx = hp.Alm.getidx(lmax_alm, ell, m)
                yield ((-1) ** m) * np.conjugate(alm[idx])


def _phase_stream_from_alm(alm: np.ndarray, lmax_alm: int, lmin: int, lmax: int, use_full_m: bool) -> np.ndarray:
    coeffs = list(_iter_stream_coeffs(alm, lmax_alm, lmin, lmax, use_full_m))
    coeffs_arr = np.asarray(coeffs, dtype=np.complex128)
    phi = np.angle(coeffs_arr)
    return np.exp(1j * phi)


def _phase_randomize_per_ell(alm: np.ndarray, lmax_alm: int, rng: np.random.Generator) -> np.ndarray:
    out = alm.copy()
    for ell in range(0, lmax_alm + 1):
        theta = rng.uniform(0.0, 2.0 * math.pi)
        rot = complex(math.cos(theta), math.sin(theta))
        for m in range(0, ell + 1):
            idx = hp.Alm.getidx(lmax_alm, ell, m)
            out[idx] *= rot
    return out


@dataclass
class Target:
    raw: float
    f: float
    k: int
    label: str


def _targets_to_freqs(targets: Sequence[float], mode: str, n: int) -> List[Target]:
    out: List[Target] = []
    for t in targets:
        if mode == "inv":
            if t == 0:
                raise ValueError("Target period cannot be 0 in inv mode")
            f = 1.0 / float(t)
            k = _idx_from_freq(n, f)
            out.append(Target(raw=float(t), f=f, k=k, label=f"p={t:g}"))
        elif mode == "freq":
            f = float(t)
            k = _idx_from_freq(n, f)
            out.append(Target(raw=float(t), f=f, k=k, label=f"f={t:g}"))
        elif mode == "bin":
            k = int(round(float(t)))
            if k < 0:
                k = -k
            kmax = n // 2
            if k > kmax:
                k = kmax
            f = k / float(n)
            out.append(Target(raw=float(t), f=f, k=k, label=f"k={int(round(float(t)))}"))
        else:
            raise ValueError(f"Unknown target mode: {mode}")
    return out


def _scan_to_targets(scan: Optional[str], mode: str, n: int) -> List[Target]:
    if not scan:
        return []
    a, b, step = _parse_range(scan)
    xs = _frange(a, b, step)
    return _targets_to_freqs(xs, mode=mode, n=n)


def _analyze_stream(stream: np.ndarray, targets: List[Target], scan_targets: List[Target], window: str):
    freqs, psd = _fft_psd(stream, window=window)
    obs = {t.label: float(psd[t.k]) if t.k < len(psd) else float(psd[-1]) for t in targets}

    scan_peak = None
    if scan_targets:
        best_t = None
        best_v = -1.0
        for t in scan_targets:
            v = float(psd[t.k]) if t.k < len(psd) else float(psd[-1])
            if v > best_v:
                best_v = v
                best_t = t
        scan_peak = (best_t, best_v)
    return freqs, psd, obs, scan_peak


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="spectral_resonance_v4")
    ap.add_argument("--tt-map", dest="tt_map", default=None)
    ap.add_argument("--q-map", dest="q_map", default=None)
    ap.add_argument("--u-map", dest="u_map", default=None)
    ap.add_argument("--lmin", type=int, default=2)
    ap.add_argument("--lmax", type=int, default=512)
    ap.add_argument("--lmax-alm", type=int, default=512)
    ap.add_argument("--channels", type=str, default="TT,EE,BB")
    ap.add_argument("--use-full-m", action="store_true")
    ap.add_argument("--window", choices=["hann", "none"], default="hann")
    ap.add_argument("--targets", type=str, default="137,139")
    ap.add_argument("--target-mode", choices=["inv", "freq", "bin"], default="inv")
    ap.add_argument("--scan", type=str, default=None)
    ap.add_argument("--mc", type=int, default=0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--target-correlation", action="store_true", help="Compute MC correlation/joint-tail diagnostics between targets (Pearson r and p_joint based on product).")
    ap.add_argument("--cross", action="store_true", help="reserved (not implemented)")
    ap.add_argument("--report-csv", type=str, default=None)
    ap.add_argument("--plot-png", type=str, default=None)
    args = ap.parse_args(argv)

    ch_list = [c.strip().upper() for c in _parse_list_csv(args.channels)]
    if not ch_list:
        raise SystemExit("No channels requested. Use --channels TT,EE,BB")

    if "TT" in ch_list and not args.tt_map:
        raise SystemExit("--tt-map is required for TT")
    if any(c in ch_list for c in ("EE", "BB")) and (not args.q_map or not args.u_map):
        raise SystemExit("--q-map and --u-map are required for EE/BB")

    lmin, lmax, lmax_alm = int(args.lmin), int(args.lmax), int(args.lmax_alm)
    if lmax_alm < lmax:
        raise SystemExit("--lmax-alm must be >= --lmax")

    print(
        f"[spectral_resonance_v4] ell=[{lmin},{lmax}] lmax_alm={lmax_alm} "
        f"channels={','.join(ch_list)} mc={args.mc} use_full_m={args.use_full_m} "
        f"target_mode={args.target_mode} window={args.window}"
    )

    almT = almE = almB = None
    if args.tt_map:
        mT = hp.read_map(args.tt_map, field=0, verbose=False)
        almT = hp.map2alm(mT, lmax=lmax_alm, pol=False, iter=0)

    if args.q_map and args.u_map:
        q = hp.read_map(args.q_map, verbose=False)
        u = hp.read_map(args.u_map, verbose=False)
        # healpy map2alm_spin signature differs across versions.

        # healpy map2alm_spin signature differs across versions.
        # Use a small compatibility shim.
        almE, almB = _map2alm_spin_compat([q, u], spin=2, lmax=lmax_alm)
    
    streams: Dict[str, np.ndarray] = {}
    if "TT" in ch_list:
        streams["TT"] = _phase_stream_from_alm(almT, lmax_alm, lmin, lmax, args.use_full_m)
    if "EE" in ch_list:
        streams["EE"] = _phase_stream_from_alm(almE, lmax_alm, lmin, lmax, args.use_full_m)
    if "BB" in ch_list:
        streams["BB"] = _phase_stream_from_alm(almB, lmax_alm, lmin, lmax, args.use_full_m)

    n = int(next(iter(streams.values())).shape[0])

    targets = _targets_to_freqs(_parse_floats_csv(args.targets), mode=args.target_mode, n=n)
    scan_targets = _scan_to_targets(args.scan, mode=args.target_mode, n=n) if args.scan else []

    obs_psd: Dict[str, Dict[str, float]] = {}
    scan_peak_obs: Dict[str, float] = {}
    scan_peak_meta: Dict[str, Tuple[str, float, int]] = {}  # label,f,k
    plots: Dict[str, Tuple[np.ndarray, np.ndarray]] = {}

    for ch, stream in streams.items():
        freqs, psd, obs, scan_peak = _analyze_stream(stream, targets, scan_targets, window=args.window)
        obs_psd[ch] = obs
        plots[ch] = (freqs, psd)

        print(f"\n[{ch}] stream_n={n}")
        for t in targets:
            print(f"  target {t.label:>8s}  f={t.f:.8f}  bin={t.k:d}  PSD={obs[t.label]:.6g}")

        if scan_peak and scan_peak[0] is not None:
            tbest, vbest = scan_peak
            scan_peak_obs[ch] = float(vbest)
            scan_peak_meta[ch] = (tbest.label, float(tbest.f), int(tbest.k))
            # show also period for inv mode, or bin for bin mode
            extra = ""
            if args.target_mode == "inv":
                extra = f" (period≈{1.0/tbest.f:.2f})"
            elif args.target_mode == "bin":
                extra = f" (bin={tbest.k})"
            print(f"  scan peak at {tbest.label}{extra}  f≈{tbest.f:.8f}  PSD={vbest:.6g}")

    mc = int(args.mc or 0)
    p_counts: Dict[Tuple[str, str], int] = {(ch, t.label): 0 for ch in streams for t in targets}
    scan_counts: Dict[str, int] = {ch: 0 for ch in streams} if scan_targets else {}

    # Optional: store MC PSD samples at each target bin for correlation/joint tests.
    corr_samples: Dict[Tuple[str, str], List[float]] = {}
    if args.target_correlation and mc > 0 and len(targets) >= 2:
        corr_samples = {(ch, t.label): [] for ch in streams for t in targets}

    if mc > 0:
        rng = np.random.default_rng(int(args.seed))
        base_alms: Dict[str, np.ndarray] = {}
        if almT is not None:
            base_alms["TT"] = almT
        if almE is not None:
            base_alms["EE"] = almE
        if almB is not None:
            base_alms["BB"] = almB

        for i in range(1, mc + 1):
            if i % 50 == 0:
                print(f"[mc] {i}/{mc}")
            for ch in streams.keys():
                alm_rand = _phase_randomize_per_ell(base_alms[ch], lmax_alm, rng)
                stream_rand = _phase_stream_from_alm(alm_rand, lmax_alm, lmin, lmax, args.use_full_m)
                _, psd_rand = _fft_psd(stream_rand, window=args.window)

                for t in targets:
                    v = float(psd_rand[t.k]) if t.k < len(psd_rand) else float(psd_rand[-1])
                    if v >= obs_psd[ch][t.label]:
                        p_counts[(ch, t.label)] += 1
                    if corr_samples:
                        corr_samples[(ch, t.label)].append(v)

                if scan_targets:
                    vmax = -1.0
                    for t in scan_targets:
                        v = float(psd_rand[t.k]) if t.k < len(psd_rand) else float(psd_rand[-1])
                        if v > vmax:
                            vmax = v
                    if vmax >= scan_peak_obs.get(ch, float("inf")):
                        scan_counts[ch] += 1

        print("\n=== MC p-values at targets (one-sided: PSD >= observed) ===")
        for ch in streams.keys():
            for t in targets:
                print(f"{ch} {t.label:>8s}  p_mc={p_counts[(ch, t.label)]/mc:.6g}")

        if corr_samples:
            import itertools
            print("\n=== Target correlation diagnostics (MC) ===")
            for ch in streams.keys():
                for t1, t2 in itertools.combinations(targets, 2):
                    v1 = np.asarray(corr_samples[(ch, t1.label)], dtype=np.float64)
                    v2 = np.asarray(corr_samples[(ch, t2.label)], dtype=np.float64)
                    s1 = float(v1.std())
                    s2 = float(v2.std())
                    if s1 == 0.0 or s2 == 0.0:
                        r = float("nan")
                    else:
                        r = float(np.corrcoef(v1, v2)[0, 1])
                    obs_prod = float(obs_psd[ch][t1.label] * obs_psd[ch][t2.label])
                    p_joint = float(np.mean((v1 * v2) >= obs_prod))
                    print(f"{ch} pair {t1.label}-{t2.label}: Pearson r={r:.4f}, p_joint={p_joint:.6g}")

        if scan_targets:
            print("\n=== Global p-values over scan (look-elsewhere on max PSD) ===")
            for ch in streams.keys():
                print(f"{ch} p_global(max_PSD_over_scan)={scan_counts[ch]/mc:.6g}")

    if args.report_csv:
        os.makedirs(os.path.dirname(args.report_csv) or ".", exist_ok=True)
        with open(args.report_csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["kind", "channel", "label", "raw", "freq", "bin", "psd_obs", "p_mc", "p_global"])
            for ch in streams.keys():
                for t in targets:
                    p_mc = (p_counts[(ch, t.label)] / mc) if mc > 0 else ""
                    w.writerow(["target", ch, t.label, f"{t.raw:g}", f"{t.f:.12g}", t.k, f"{obs_psd[ch][t.label]:.12g}", p_mc, ""])
                if scan_targets and ch in scan_peak_meta:
                    lbl, fbest, kbest = scan_peak_meta[ch]
                    p_glob = (scan_counts[ch] / mc) if mc > 0 else ""
                    w.writerow(["scan_peak", ch, lbl, "", f"{fbest:.12g}", kbest, f"{scan_peak_obs[ch]:.12g}", "", p_glob])
                if scan_targets:
                    freqs, psd = plots[ch]
                    for t in scan_targets:
                        v = float(psd[t.k]) if t.k < len(psd) else float(psd[-1])
                        w.writerow(["scan", ch, t.label, f"{t.raw:g}", f"{t.f:.12g}", t.k, f"{v:.12g}", "", ""])
        print(f"[info] wrote CSV: {args.report_csv}")

    if args.plot_png:
        import matplotlib.pyplot as plt
        os.makedirs(os.path.dirname(args.plot_png) or ".", exist_ok=True)
        plt.figure(figsize=(12, 6))
        for ch, (freqs, psd) in plots.items():
            plt.semilogy(freqs, psd, label=ch)
        for t in targets:
            plt.axvline(t.f, linestyle="--", alpha=0.6)
        plt.xlim(0, 0.5)
        plt.xlabel("frequency [cycles/sample]")
        plt.ylabel("PSD (one-sided)")
        plt.title(f"Spectral resonance v4.1  ell=[{lmin},{lmax}]  mode={args.target_mode}")
        plt.grid(True, which="both", alpha=0.25)
        plt.legend()
        plt.tight_layout()
        plt.savefig(args.plot_png, dpi=150)
        plt.close()
        print(f"[info] wrote PNG: {args.plot_png}")



if __name__ == "__main__":
    raise SystemExit(main())
