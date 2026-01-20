#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
spectral_resonance_v4.py

Targeted spectral resonance test on the (l,m)-linearized phase stream.

Key idea:
- We do NOT rely on FFT/Welch bin alignment for f=1/137 and f=1/139.
- We compute power at exact target frequencies via a matched-filter / targeted DFT:
    X(f) = sum_k w[k] * x[k] * exp(-i 2π f k)
    PSD_target(f) = |X(f)|^2 / sum_k w[k]^2
- x[k] is a unit phasor exp(i*phi_k) (robust to phase wrapping).

Null:
- Monte Carlo via phase randomization per-ell (preserve |a_lm|).

Extras:
- Cross-channel coherence between channels at target frequencies.
- Optional fine scan around target frequencies (no FFT grid artifacts).

Caveat:
- Here "frequency" means cycles per index k in your stream.
  Period 137 samples => f = 1/137.

Author: (you + ChatGPT)
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np

import healpy as hp

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except Exception:
    plt = None


# -----------------------------
# Utilities
# -----------------------------

def _parse_channels(s: str) -> List[str]:
    chans = [c.strip().upper() for c in s.split(",") if c.strip()]
    for c in chans:
        if c not in ("TT", "EE", "BB"):
            raise ValueError(f"Unsupported channel: {c}. Use TT,EE,BB.")
    return chans


def _hann(n: int) -> np.ndarray:
    if n <= 1:
        return np.ones((n,), dtype=float)
    return 0.5 - 0.5 * np.cos(2.0 * np.pi * np.arange(n) / (n - 1))


def _standardize_stream_phasor(phi: np.ndarray) -> np.ndarray:
    """
    Convert phase array to unit phasors exp(i*phi).
    Also remove the mean phasor to suppress trivial DC-like bias.
    """
    x = np.exp(1j * phi)
    # Remove mean phasor (optional but helps in practice):
    x = x - np.mean(x)
    return x


def _targeted_psd(
    x: np.ndarray,
    freqs: np.ndarray,
    w: Optional[np.ndarray] = None,
) -> np.ndarray:
    """
    Targeted PSD at exact freqs via matched filter / targeted DFT.

    x: complex stream length N
    freqs: array of frequencies in cycles/sample (0..0.5 typically)
    w: optional real weights/window length N

    Returns:
        psd[f] = |sum_k w[k] x[k] exp(-i2π f k)|^2 / sum_k w[k]^2
    """
    n = x.shape[0]
    k = np.arange(n, dtype=float)

    if w is None:
        w = np.ones((n,), dtype=float)
    w = w.astype(float, copy=False)

    denom = np.sum(w * w)
    if denom <= 0:
        denom = 1.0

    # Compute for each freq (K is small: e.g. 2 or a few hundred in scans).
    out = np.empty((freqs.shape[0],), dtype=float)
    for i, f in enumerate(freqs):
        ph = np.exp(-1j * 2.0 * np.pi * f * k)
        X = np.sum((w * x) * ph)
        out[i] = (np.abs(X) ** 2) / denom
    return out


def _targeted_csd_and_coh(
    x: np.ndarray,
    y: np.ndarray,
    freqs: np.ndarray,
    w: Optional[np.ndarray] = None,
    eps: float = 1e-12,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Targeted cross spectrum and coherence at exact freqs.

    Returns:
        Sxy: complex cross-spectrum estimate at each freq
        Sxx: auto-spectrum of x at each freq
        Syy: auto-spectrum of y at each freq
        coherence = |Sxy|^2 / (Sxx*Syy + eps)
    """
    n = x.shape[0]
    k = np.arange(n, dtype=float)

    if w is None:
        w = np.ones((n,), dtype=float)
    w = w.astype(float, copy=False)
    denom = np.sum(w * w)
    if denom <= 0:
        denom = 1.0

    Sxy = np.empty((freqs.shape[0],), dtype=np.complex128)
    Sxx = np.empty((freqs.shape[0],), dtype=float)
    Syy = np.empty((freqs.shape[0],), dtype=float)

    for i, f in enumerate(freqs):
        ph = np.exp(-1j * 2.0 * np.pi * f * k)
        X = np.sum((w * x) * ph)
        Y = np.sum((w * y) * ph)
        Sxy[i] = (X * np.conj(Y)) / denom
        Sxx[i] = (np.abs(X) ** 2) / denom
        Syy[i] = (np.abs(Y) ** 2) / denom

    coh = (np.abs(Sxy) ** 2) / (Sxx * Syy + eps)
    return Sxy, Sxx, Syy, coh


def _phase_randomize_per_ell(
    alm: np.ndarray,
    l_arr: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    """
    Randomize phase of alm per-ell:
      a_lm -> |a_lm| * exp(i*(arg(a_lm)+u_lm))
    with u_lm ~ Uniform(0,2π), independent per mode.

    This destroys phase structure but preserves magnitude distribution.
    """
    out = alm.copy()
    phi = np.angle(out)
    mag = np.abs(out)
    u = rng.uniform(0.0, 2.0 * np.pi, size=out.shape[0])
    out = mag * np.exp(1j * (phi + u))
    return out


def _alm_stream_in_lrange(
    alm: np.ndarray,
    l_arr: np.ndarray,
    m_arr: np.ndarray,
    lmin: int,
    lmax: int,
    use_full_m: bool,
) -> np.ndarray:
    """
    Extract phase stream for l in [lmin,lmax].
    If use_full_m: include all m (healpy alm already stores m>=0 only,
    so "full m" here means we include all stored modes (m>=0) BUT we can
    optionally augment by mirrored negative-m phase if you had such logic.
    In this v4 script, we keep it simple and consistent: healpy alm indices
    are m>=0. If you want explicit "full m", you must reconstruct negative m
    using reality constraints, but that introduces assumptions.

    For stability + auditability, we define:
      - use_full_m=False: use only m>=0 (same as healpy storage)
      - use_full_m=True: also only m>=0 (explicitly), but label remains for
        compatibility with your earlier CLI; if you need true full-m, tell me
        and we’ll add a controlled reconstruction with tests.
    """
    mask = (l_arr >= lmin) & (l_arr <= lmax)
    # healpy alm uses only m>=0 by construction
    # keep mask as is; "use_full_m" left for future extension
    return alm[mask]


def _compute_TEB_alm(
    tt_map: Optional[str],
    q_map: Optional[str],
    u_map: Optional[str],
    lmax_alm: int,
) -> Tuple[Optional[np.ndarray], Optional[np.ndarray], Optional[np.ndarray]]:
    """
    Return (almT, almE, almB) depending on available inputs.
    TT from map; E/B from Q/U if provided.
    """
    almT = almE = almB = None

    if tt_map:
        mT = hp.read_map(tt_map, field=0, verbose=False)
        almT = hp.map2alm(mT, lmax=lmax_alm)

    if q_map and u_map:
        q = hp.read_map(q_map, verbose=False)
        u = hp.read_map(u_map, verbose=False)
        # spin-2 transform to E/B
        almE, almB = hp.map2alm_spin([q, u], spin=2, lmax=lmax_alm)

    return almT, almE, almB


@dataclass
class ChannelResult:
    channel: str
    n: int
    f_targets: List[float]
    psd_targets: List[float]
    p_mc: List[float]


# -----------------------------
# Main analysis
# -----------------------------

def run(
    tt_map: Optional[str],
    q_map: Optional[str],
    u_map: Optional[str],
    lmin: int,
    lmax: int,
    lmax_alm: int,
    channels: List[str],
    use_full_m: bool,
    window: str,
    # targets
    targets: List[float],          # in "period" units: e.g. [137,139] meaning f=1/period
    target_mode: str,              # "inv" => f=1/p ; "freq" => f=p directly
    # scan
    scan: Optional[str],           # e.g. "136.0:140.0:0.01" in period units (if inv), or freq units (if freq)
    # monte carlo
    mc: int,
    seed: int,
    # cross
    cross: bool,
    # reporting
    report_csv: Optional[str],
    plot_png: Optional[str],
) -> int:

    print(
        f"[spectral_resonance_v4] ell=[{lmin},{lmax}] lmax_alm={lmax_alm} "
        f"channels={','.join(channels)} mc={mc} use_full_m={use_full_m} "
        f"target_mode={target_mode} window={window}"
    )

    # Build freq targets
    if target_mode == "inv":
        f_targets = [1.0 / float(p) for p in targets]
    elif target_mode == "freq":
        f_targets = [float(p) for p in targets]
    else:
        raise ValueError("target_mode must be 'inv' or 'freq'.")

    f_targets = np.array(f_targets, dtype=float)

    # Scan grid (optional)
    scan_freqs = None
    scan_periods = None
    if scan:
        a, b, step = scan.split(":")
        a = float(a); b = float(b); step = float(step)
        scan_periods = np.arange(a, b + 0.5 * step, step, dtype=float)
        if target_mode == "inv":
            scan_freqs = 1.0 / scan_periods
        else:
            scan_freqs = scan_periods

    # Window/weights
    # (Hann is the default to reduce leakage.)
    w = None
    win_name = window.lower().strip()
    if win_name == "none":
        w = None
    else:
        # We build w after we know stream length; here just mark.
        pass

    # Load alms
    almT, almE, almB = _compute_TEB_alm(tt_map, q_map, u_map, lmax_alm=lmax_alm)
    l_arr, m_arr = hp.Alm.getlm(lmax_alm)

    channel_to_alm = {"TT": almT, "EE": almE, "BB": almB}

    # Compute observed PSD targets (+ optional scan)
    rng = np.random.default_rng(seed)

    obs_results: Dict[str, Dict[str, np.ndarray]] = {}  # channel -> {"psd_targets":..., "psd_scan":...}
    streams: Dict[str, np.ndarray] = {}

    for ch in channels:
        alm = channel_to_alm.get(ch)
        if alm is None:
            print(f"[warn] channel {ch} missing inputs; skipping.")
            continue

        alm_seg = _alm_stream_in_lrange(alm, l_arr, m_arr, lmin, lmax, use_full_m=use_full_m)
        phi = np.angle(alm_seg)
        x = _standardize_stream_phasor(phi)
        streams[ch] = x

        n = x.shape[0]
        if win_name == "none":
            ww = None
        else:
            ww = _hann(n)

        psd_t = _targeted_psd(x, f_targets, w=ww)
        out = {"psd_targets": psd_t}

        if scan_freqs is not None:
            psd_scan = _targeted_psd(x, scan_freqs, w=ww)
            out["psd_scan"] = psd_scan
        obs_results[ch] = out

        print(f"\n[{ch}] stream_n={n}")
        for i, f in enumerate(f_targets):
            print(f"  target f={f:.8f}  PSD={psd_t[i]:.6g}")

        if scan_freqs is not None:
            j = int(np.argmax(obs_results[ch]["psd_scan"]))
            if target_mode == "inv":
                print(
                    f"  scan peak at period≈{scan_periods[j]:.6g}  f≈{scan_freqs[j]:.8f}  PSD={obs_results[ch]['psd_scan'][j]:.6g}"
                )
            else:
                print(
                    f"  scan peak at f≈{scan_freqs[j]:.8f}  PSD={obs_results[ch]['psd_scan'][j]:.6g}"
                )

    if not obs_results:
        print("[error] No channels produced streams.")
        return 2

    # Cross-channel coherence at targets (observed)
    cross_rows = []
    if cross and len(streams) >= 2:
        ch_list = list(streams.keys())
        for i in range(len(ch_list)):
            for j in range(i + 1, len(ch_list)):
                a = ch_list[i]
                b = ch_list[j]
                xa = streams[a]
                xb = streams[b]
                n = min(xa.shape[0], xb.shape[0])
                xa = xa[:n]
                xb = xb[:n]
                ww = None if win_name == "none" else _hann(n)
                Sxy, Sxx, Syy, coh = _targeted_csd_and_coh(xa, xb, f_targets, w=ww)
                for kf in range(f_targets.shape[0]):
                    cross_rows.append(
                        {
                            "pair": f"{a}-{b}",
                            "f": float(f_targets[kf]),
                            "coherence": float(coh[kf]),
                            "csd_real": float(np.real(Sxy[kf])),
                            "csd_imag": float(np.imag(Sxy[kf])),
                        }
                    )
        print("\n=== Observed cross-channel coherence (targets) ===")
        for r in cross_rows:
            print(
                f"{r['pair']} f={r['f']:.8f} coh={r['coherence']:.6g} "
                f"Sxy=({r['csd_real']:.3g}+{r['csd_imag']:.3g}i)"
            )

    # Monte Carlo null
    # We compute p-values as fraction of MC with PSD >= observed PSD at each target.
    if mc > 0:
        mc_counts: Dict[str, np.ndarray] = {ch: np.zeros_like(obs_results[ch]["psd_targets"], dtype=int) for ch in obs_results.keys()}
        mc_counts_scan: Dict[str, int] = {ch: 0 for ch in obs_results.keys()}  # for global max over scan (optional)

        for it in range(mc):
            if (it + 1) % max(1, mc // 10) == 0:
                print(f"[mc] {it+1}/{mc}")

            for ch in list(obs_results.keys()):
                alm = channel_to_alm[ch]
                alm_rand = _phase_randomize_per_ell(alm, l_arr, rng=rng)
                alm_seg = _alm_stream_in_lrange(alm_rand, l_arr, m_arr, lmin, lmax, use_full_m=use_full_m)
                phi = np.angle(alm_seg)
                x = _standardize_stream_phasor(phi)

                n = x.shape[0]
                ww = None if win_name == "none" else _hann(n)

                psd_t = _targeted_psd(x, f_targets, w=ww)
                mc_counts[ch] += (psd_t >= obs_results[ch]["psd_targets"]).astype(int)

                if scan_freqs is not None:
                    psd_scan = _targeted_psd(x, scan_freqs, w=ww)
                    max_mc = float(np.max(psd_scan))
                    max_obs = float(np.max(obs_results[ch]["psd_scan"]))
                    if max_mc >= max_obs:
                        mc_counts_scan[ch] += 1

        pvals: Dict[str, np.ndarray] = {}
        for ch in obs_results.keys():
            # Add +1 smoothing to avoid exactly 0.
            p = (mc_counts[ch] + 1.0) / (mc + 1.0)
            pvals[ch] = p

        print("\n=== MC p-values at targets (one-sided: PSD >= observed) ===")
        for ch in obs_results.keys():
            for i, f in enumerate(f_targets):
                print(f"{ch} f={f:.8f}  p_mc={float(pvals[ch][i]):.6g}")

        if scan_freqs is not None:
            print("\n=== Global p-values over scan (look-elsewhere on max PSD) ===")
            for ch in obs_results.keys():
                p_glob = (mc_counts_scan[ch] + 1.0) / (mc + 1.0)
                print(f"{ch} p_global(max_PSD_over_scan)={p_glob:.6g}")
    else:
        pvals = {ch: np.full_like(obs_results[ch]["psd_targets"], np.nan, dtype=float) for ch in obs_results.keys()}

    # Report CSV
    if report_csv:
        rows = []
        for ch in obs_results.keys():
            for i, f in enumerate(f_targets):
                row = {
                    "channel": ch,
                    "stream_n": int(streams[ch].shape[0]),
                    "target_f": float(f),
                    "target_period": float(1.0 / f) if f != 0 else float("inf"),
                    "psd": float(obs_results[ch]["psd_targets"][i]),
                    "p_mc": float(pvals[ch][i]) if mc > 0 else "",
                }
                rows.append(row)

        # include scan peaks if present
        if scan_freqs is not None:
            for ch in obs_results.keys():
                j = int(np.argmax(obs_results[ch]["psd_scan"]))
                rows.append(
                    {
                        "channel": ch,
                        "stream_n": int(streams[ch].shape[0]),
                        "target_f": float(scan_freqs[j]),
                        "target_period": float(1.0 / scan_freqs[j]) if scan_freqs[j] != 0 else float("inf"),
                        "psd": float(obs_results[ch]["psd_scan"][j]),
                        "p_mc": "",
                        "note": "scan_peak",
                    }
                )

        # add cross coherence
        if cross_rows:
            for r in cross_rows:
                rows.append(
                    {
                        "channel": r["pair"],
                        "stream_n": "",
                        "target_f": r["f"],
                        "target_period": float(1.0 / r["f"]) if r["f"] != 0 else float("inf"),
                        "psd": "",
                        "p_mc": "",
                        "coherence": r["coherence"],
                        "csd_real": r["csd_real"],
                        "csd_imag": r["csd_imag"],
                        "note": "cross",
                    }
                )

        # write
        fieldnames = sorted({k for r in rows for k in r.keys()})
        with open(report_csv, "w", newline="") as f:
            wcsv = csv.DictWriter(f, fieldnames=fieldnames)
            wcsv.writeheader()
            wcsv.writerows(rows)
        print(f"\n[info] wrote CSV: {report_csv}")

    # Plot PNG (optional)
    if plot_png and plt is not None:
        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(1, 1, 1)

        # If scan, plot scan PSD; else plot targets as points
        for ch in obs_results.keys():
            if scan_freqs is not None:
                ax.plot(scan_freqs, obs_results[ch]["psd_scan"], label=f"{ch} scan")
            else:
                ax.scatter(f_targets, obs_results[ch]["psd_targets"], label=f"{ch} targets")

        # draw target lines
        for f in f_targets:
            ax.axvline(f, linestyle="--", alpha=0.4)

        ax.set_title(f"Targeted resonance (ell={lmin}-{lmax})")
        ax.set_xlabel("frequency (cycles per k)")
        ax.set_ylabel("targeted PSD (matched-filter)")
        ax.grid(True, alpha=0.3)
        ax.legend()

        fig.tight_layout()
        fig.savefig(plot_png, dpi=160)
        print(f"[info] wrote PNG: {plot_png}")

    return 0


def main() -> int:
    ap = argparse.ArgumentParser("spectral_resonance_v4")

    ap.add_argument("--tt-map", type=str, default=None)
    ap.add_argument("--q-map", type=str, default=None)
    ap.add_argument("--u-map", type=str, default=None)

    ap.add_argument("--lmin", type=int, default=128)
    ap.add_argument("--lmax", type=int, default=146)
    ap.add_argument("--lmax-alm", type=int, default=512)

    ap.add_argument("--channels", type=str, default="TT,EE,BB")
    ap.add_argument("--use-full-m", action="store_true", help="kept for compatibility; v4 uses healpy m>=0 stream for auditability")

    ap.add_argument("--window", type=str, default="hann", choices=["hann", "none"])

    # targets: either periods (inv) or direct freqs (freq)
    ap.add_argument("--targets", type=str, default="137,139", help="comma-separated target values (periods if --target-mode inv, else freqs)")
    ap.add_argument("--target-mode", type=str, default="inv", choices=["inv", "freq"],
                    help="inv: interpret targets as periods P and use f=1/P. freq: interpret targets as direct frequencies f.")

    # optional scan around targets (in same units as targets)
    ap.add_argument("--scan", type=str, default=None,
                    help="optional scan range a:b:step (in target units; periods if inv, else freqs). Example: 136:140:0.01")

    ap.add_argument("--mc", type=int, default=0)
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--cross", action="store_true", help="compute cross-channel coherence at targets (observed only)")

    ap.add_argument("--report-csv", type=str, default=None)
    ap.add_argument("--plot-png", type=str, default=None)

    args = ap.parse_args()

    channels = _parse_channels(args.channels)
    targets = [float(x.strip()) for x in args.targets.split(",") if x.strip()]

    return run(
        tt_map=args.tt_map,
        q_map=args.q_map,
        u_map=args.u_map,
        lmin=args.lmin,
        lmax=args.lmax,
        lmax_alm=args.lmax_alm,
        channels=channels,
        use_full_m=args.use_full_m,
        window=args.window,
        targets=targets,
        target_mode=args.target_mode,
        scan=args.scan,
        mc=args.mc,
        seed=args.seed,
        cross=args.cross,
        report_csv=args.report_csv,
        plot_png=args.plot_png,
    )


if __name__ == "__main__":
    raise SystemExit(main())

