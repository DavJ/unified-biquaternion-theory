#!/usr/bin/env python3
"""
forensic_fingerprint.tools.spectral_resonance_2d

2D spectral/cepstral resonance probe on (ell, m) grids built from Healpix a_lm.

Why:
- Avoids 1D "stream ordering" artifacts by working on a natural 2D lattice.
- Supports 2D PSD (via FFT2) and 2D real cepstrum ("2-kepstrum") for periodicity detection.

Typical use (BB phase, ell window, PSD targets as periods along ell/m):
MPLBACKEND=Agg python -m forensic_fingerprint.tools.spectral_resonance_2d \
  --q-map data/...Q...fits --u-map data/...U...fits \
  --channels BB --lmin 100 --lmax 200 \
  --field phase --m-mode nonneg --pad-to-lmax \
  --analysis psd --window2d hann \
  --targets-ell 137,139 --targets-m 137,139 --target-mode period \
  --mc 2000 --null ell-rot --seed 0 \
  --report-csv scans/sr2d_bb_100_200.csv --plot-png scans/sr2d_bb_100_200.png

Notes:
- target-mode=period means the numbers you pass are *periods* in samples along each axis.
  Internally we map period -> FFT bin k ≈ N/period.
- For cepstrum analysis, we compute real cepstrum of log(PSD) and target periods map to quefrency bins q ≈ period.
"""

from __future__ import annotations
import argparse
import csv
import math
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import healpy as hp

# ---------------------------- parsing helpers ----------------------------

def _parse_list_csv(s: str) -> List[str]:
    return [x.strip() for x in (s or "").split(",") if x.strip()]

def _parse_floats_csv(s: str) -> List[float]:
    return [float(x) for x in _parse_list_csv(s)]

def _ensure_dir_for(path: Optional[str]) -> None:
    if not path:
        return
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

# ---------------------------- alm helpers ----------------------------

def _map2alm_spin_compat(qu_maps, spin: int, lmax: int):
    """Healpy signature compatibility across versions."""
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

def _alm_get(alm: np.ndarray, lmax: int, ell: int, m: int) -> complex:
    return alm[hp.Alm.getidx(lmax, ell, m)]

# ---------------------------- 2D grid construction ----------------------------

def _build_grid_from_alm(
    alm: np.ndarray,
    lmax_alm: int,
    lmin: int,
    lmax: int,
    field: str,
    m_mode: str,
    pad_to_lmax: bool,
    whiten_eps: float = 1e-30,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns:
      X: complex/real matrix [N_ell, N_m] (after padding),
      ells: array of ell values length N_ell,
      ms: array of m indices length N_m (semantic depends on m_mode)
    """
    ells = np.arange(lmin, lmax + 1, dtype=int)
    n_ell = len(ells)

    # Choose m axis layout
    if m_mode == "nonneg":
        n_m = (lmax + 1) if pad_to_lmax else (lmax + 1)  # still needs a consistent width
        ms = np.arange(0, n_m, dtype=int)
        X = np.zeros((n_ell, n_m), dtype=np.complex128)
        for i, ell in enumerate(ells):
            m_max = ell
            for m in range(0, m_max + 1):
                a = _alm_get(alm, lmax_alm, ell, m)
                X[i, m] = a
            # remaining m are zeros (padding)
    elif m_mode == "full":
        # m in [-lmax..+lmax] with symmetry for negative m
        n_m = (2 * lmax + 1)
        ms = np.arange(-lmax, lmax + 1, dtype=int)
        X = np.zeros((n_ell, n_m), dtype=np.complex128)
        for i, ell in enumerate(ells):
            for m in range(0, ell + 1):
                a = _alm_get(alm, lmax_alm, ell, m)
                # place +m
                X[i, m + lmax] = a
                # place -m using reality condition for real sky maps:
                # a_{ell,-m} = (-1)^m * conj(a_{ell,m})
                if m != 0:
                    X[i, -m + lmax] = ((-1) ** m) * np.conjugate(a)
            # outside |m|>ell remains zero
    else:
        raise ValueError(f"Invalid --m-mode '{m_mode}'. Use 'nonneg' or 'full'.")

    # Transform to chosen field
    if field == "phase":
        # Avoid phase of 0: keep zeros as 0
        ang = np.angle(X, deg=False)
        X = np.where(np.abs(X) > 0, np.exp(1j * ang), 0.0).astype(np.complex128)
    elif field == "alm":
        X = X.astype(np.complex128)
    elif field == "abs":
        X = np.abs(X).astype(np.float64)
    elif field == "whitened":
        # Estimate Cl per ell from available m>=0 coefficients in the window
        # Use unbiased-ish mean of |a|^2 over m in [0..ell]
        Xw = np.zeros_like(X, dtype=np.complex128)
        for i, ell in enumerate(ells):
            vals = []
            for m in range(0, ell + 1):
                a = _alm_get(alm, lmax_alm, ell, m)
                vals.append(np.abs(a) ** 2)
            cl_hat = float(np.mean(vals)) if vals else 0.0
            denom = math.sqrt(cl_hat + whiten_eps)
            # divide only where X nonzero
            Xw[i, :] = np.where(np.abs(X[i, :]) > 0, X[i, :] / denom, 0.0)
        X = Xw
    else:
        raise ValueError(f"Invalid --field '{field}'.")

    return X, ells.astype(int), ms.astype(int)

# ---------------------------- windows / transforms ----------------------------

def _window_1d(n: int, kind: str) -> np.ndarray:
    if kind == "none":
        return np.ones(n, dtype=np.float64)
    if kind == "hann":
        return np.hanning(n).astype(np.float64)
    if kind == "hamming":
        return np.hamming(n).astype(np.float64)
    if kind == "blackman":
        return np.blackman(n).astype(np.float64)
    raise ValueError(f"Invalid window kind '{kind}' (use none|hann|hamming|blackman).")

def _apply_window2d(X: np.ndarray, kind: str, normalize_rms: bool = True) -> np.ndarray:
    if kind == "none":
        return X
    # separable taper
    w0 = _window_1d(X.shape[0], kind)
    w1 = _window_1d(X.shape[1], kind)
    W = np.outer(w0, w1)
    if normalize_rms:
        # normalize so RMS(W)=1 (helps compare PSD scales across windows)
        W = W / math.sqrt(float(np.mean(W ** 2)) + 1e-30)
    return X * W

def _psd2(X: np.ndarray) -> np.ndarray:
    F = np.fft.fft2(X)
    P = (np.abs(F) ** 2) / (X.shape[0] * X.shape[1])
    return P

def _real_cepstrum2(P: np.ndarray, eps: float = 1e-30) -> np.ndarray:
    # 2D real cepstrum of power spectrum: ifft2(log(P))
    L = np.log(P + eps)
    C = np.fft.ifft2(L)
    return np.real(C)

# ---------------------------- null models ----------------------------

def _null_ell_rot(alm: np.ndarray, lmax_alm: int, rng: np.random.Generator) -> np.ndarray:
    """Rotate all m at each ell by a random phase; preserves |alm|, breaks phase coherence across ell."""
    out = alm.copy()
    for ell in range(lmax_alm + 1):
        rot = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi))
        for m in range(0, ell + 1):
            out[hp.Alm.getidx(lmax_alm, ell, m)] *= rot
    return out

def _null_lm_rand(alm: np.ndarray, lmax_alm: int, rng: np.random.Generator) -> np.ndarray:
    """Randomize phase per (ell,m); preserves |alm|."""
    out = alm.copy()
    for ell in range(lmax_alm + 1):
        for m in range(0, ell + 1):
            idx = hp.Alm.getidx(lmax_alm, ell, m)
            a = out[idx]
            if a == 0:
                continue
            out[idx] = np.abs(a) * np.exp(1j * rng.uniform(0.0, 2.0 * np.pi))
    return out

# ---------------------------- target mapping ----------------------------

@dataclass(frozen=True)
class Target2D:
    label: str
    k_ell: int
    k_m: int
    raw_ell: float
    raw_m: float

def _map_target_to_k(raw: float, n: int, mode: str) -> int:
    """
    mode:
      - period: raw is period in samples -> k ≈ round(n / period)
      - freq: raw is normalized frequency in [0,1) cycles/sample -> k ≈ round(raw*n)
      - bin: raw is bin index -> k = int(raw)
    """
    if mode == "period":
        if raw == 0:
            return 0
        k = int(round(n / raw))
    elif mode == "freq":
        k = int(round(raw * n))
    elif mode == "bin":
        k = int(round(raw))
    else:
        raise ValueError(f"Invalid --target-mode '{mode}' (period|freq|bin).")
    # fold into valid range [0..n-1]
    k = max(0, min(k, n - 1))
    return k

def _targets2d(targets_ell: Sequence[float], targets_m: Sequence[float], n_ell: int, n_m: int, mode: str) -> List[Target2D]:
    out: List[Target2D] = []
    for te in targets_ell:
        for tm in targets_m:
            ke = _map_target_to_k(te, n_ell, mode)
            km = _map_target_to_k(tm, n_m, mode)
            out.append(Target2D(label=f"ell={te:g},m={tm:g}", k_ell=ke, k_m=km, raw_ell=te, raw_m=tm))
    return out

# ---------------------------- reporting ----------------------------


def _write_csv(path: str, rows: List[Dict[str, object]]) -> None:
    """Write rows to CSV, allowing heterogeneous dict keys.

    The standard csv.DictWriter requires a fixed set of fieldnames; this helper
    builds the union of keys across all rows (stable ordering: common/important
    keys first, then the rest alphabetically).
    """
    if not path:
        return
    if not rows:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("")
        return

    # Prefer a human-friendly order for common metadata fields.
    preferred = [
        "channel", "analysis", "target_mode",
        "ell_in", "m_in", "k_ell", "k_m",
        "obs", "p_mc",
        "N_ell", "N_m",
        "field", "m_mode", "window2d",
        "null", "mc", "seed",
    ]
    key_union = []
    seen = set()
    for k in preferred:
        for r in rows:
            if k in r and k not in seen:
                key_union.append(k); seen.add(k)
                break
    # Add remaining keys in sorted order for determinism.
    for k in sorted({k for r in rows for k in r.keys()}):
        if k not in seen:
            key_union.append(k); seen.add(k)

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=key_union, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

def _maybe_plot(path: Optional[str], psd: Optional[np.ndarray], cep: Optional[np.ndarray], title: str) -> None:
    if not path:
        return
    _ensure_dir_for(path)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Prefer PSD plot; if both, stack as separate images is messy -> plot PSD and save, and if cep present save *_cep.png
    if psd is not None:
        plt.figure(figsize=(8, 6))
        plt.imshow(np.fft.fftshift(psd), aspect="auto")
        plt.title(title + " (PSD2, fftshifted)")
        plt.colorbar()
        plt.tight_layout()
        plt.savefig(path, dpi=150)
        plt.close()

    if cep is not None:
        base, ext = os.path.splitext(path)
        cep_path = base + "_cep" + ext
        plt.figure(figsize=(8, 6))
        plt.imshow(np.fft.fftshift(cep), aspect="auto")
        plt.title(title + " (Real Cepstrum2, fftshifted)")
        plt.colorbar()
        plt.tight_layout()
        plt.savefig(cep_path, dpi=150)
        plt.close()

# ---------------------------- main ----------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tt-map", help="IQU FITS for TT (field 0) or temperature-only map")
    ap.add_argument("--q-map", help="Q map FITS (single field)")
    ap.add_argument("--u-map", help="U map FITS (single field)")

    ap.add_argument("--lmin", type=int, default=2)
    ap.add_argument("--lmax", type=int, default=512)
    ap.add_argument("--lmax-alm", type=int, default=512)

    ap.add_argument("--channels", default="TT,EE,BB")
    ap.add_argument("--field", default="phase", choices=["phase", "alm", "abs", "whitened"])
    ap.add_argument("--m-mode", default="nonneg", choices=["nonneg", "full"])
    ap.add_argument("--pad-to-lmax", action="store_true", help="Pad m axis to Lmax width (recommended)")

    ap.add_argument("--analysis", default="psd", choices=["psd", "cepstrum", "both"])
    ap.add_argument("--window2d", default="hann", choices=["none", "hann", "hamming", "blackman"])

    ap.add_argument("--targets-ell", default="", help="Comma-separated numbers for ell-axis targets")
    ap.add_argument("--targets-m", default="", help="Comma-separated numbers for m-axis targets")
    ap.add_argument("--target-mode", default="period", choices=["period", "freq", "bin"])

    ap.add_argument("--mc", type=int, default=0)
    ap.add_argument("--null", default="ell-rot", choices=["ell-rot", "lm-rand"])
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--report-csv", default=None)
    ap.add_argument("--plot-png", default=None)

    args = ap.parse_args()

    ch_list = [c.strip().upper() for c in _parse_list_csv(args.channels)]
    lmin, lmax, lmax_alm = args.lmin, args.lmax, args.lmax_alm

    # Load maps -> alms
    alms: Dict[str, np.ndarray] = {}

    if "TT" in ch_list:
        if not args.tt_map:
            raise SystemExit("--tt-map is required for TT")
        # Keep verbose arg to match your current environment (suppresses logs, but Healpy deprecates it)
        mT = hp.read_map(args.tt_map, field=0, verbose=False)
        alms["TT"] = hp.map2alm(mT, lmax=lmax_alm, iter=0)

    if any(ch in ch_list for ch in ("EE", "BB")):
        if not (args.q_map and args.u_map):
            raise SystemExit("--q-map and --u-map are required for EE/BB")
        q = hp.read_map(args.q_map, field=0, verbose=False)
        u = hp.read_map(args.u_map, field=0, verbose=False)
        ee, bb = _map2alm_spin_compat([q, u], spin=2, lmax=lmax_alm)
        alms["EE"] = ee
        alms["BB"] = bb

    # Build observed products + targets
    targets_ell = _parse_floats_csv(args.targets_ell)
    targets_m = _parse_floats_csv(args.targets_m)
    want_targets = bool(targets_ell and targets_m)

    obs_rows: List[Dict[str, object]] = []
    mc_rows: List[Dict[str, object]] = []

    rng = np.random.default_rng(args.seed)

    print(f"[spectral_resonance_2d] ell=[{lmin},{lmax}] lmax_alm={lmax_alm} channels={','.join(ch_list)} field={args.field} m_mode={args.m_mode} window2d={args.window2d} analysis={args.analysis} mc={args.mc} null={args.null}")

    for ch in ch_list:
        if ch not in alms:
            continue

        X0, ells, ms = _build_grid_from_alm(
            alms[ch], lmax_alm=lmax_alm, lmin=lmin, lmax=lmax,
            field=args.field, m_mode=args.m_mode, pad_to_lmax=args.pad_to_lmax
        )
        X0w = _apply_window2d(X0, args.window2d, normalize_rms=True)

        psd0 = _psd2(X0w) if args.analysis in ("psd", "both") else None
        cep0 = _real_cepstrum2(psd0) if (args.analysis in ("cepstrum", "both") and psd0 is not None) else None

        title = f"{ch} 2D {args.analysis}  ell=[{lmin},{lmax}] field={args.field} m={args.m_mode} win={args.window2d}"
        _maybe_plot(args.plot_png, psd0, cep0, title)

        print(f"\n[{ch}] grid shape={X0w.shape} (N_ell={X0w.shape[0]}, N_m={X0w.shape[1]})")

        if want_targets:
            t2 = _targets2d(targets_ell, targets_m, n_ell=X0w.shape[0], n_m=X0w.shape[1], mode=args.target_mode)

            # If multiple raw targets map onto the same (k_ell,k_m) bin, report it.
            uniq = {(t.k_ell, t.k_m) for t in t2}
            if len(uniq) < len(t2):
                print(f"[warn] {len(t2)} requested 2D targets map to only {len(uniq)} unique FFT bins. "
                      f"Consider --target-mode bin or --analysis with finer resolution (e.g., zero-padding / larger grids).")
            for t in t2:
                if psd0 is not None:
                    obs = float(psd0[t.k_ell, t.k_m])
                    print(f"  PSD target ({t.label}) -> k=({t.k_ell},{t.k_m}) PSD={obs:.6g}")
                    obs_rows.append({
                        "channel": ch, "analysis": "psd",
                        "target_ell": t.raw_ell, "target_m": t.raw_m,
                        "k_ell": t.k_ell, "k_m": t.k_m,
                        "value": obs
                    })
                if cep0 is not None:
                    # cepstrum "targets" are naturally quefrency bins: q ≈ period
                    # here we reuse k-mapping; user can pass mode=bin for explicit quefrency bins
                    obs = float(cep0[t.k_ell, t.k_m])
                    print(f"  CEP target ({t.label}) -> q=({t.k_ell},{t.k_m}) C={obs:.6g}")
                    obs_rows.append({
                        "channel": ch, "analysis": "cepstrum",
                        "target_ell": t.raw_ell, "target_m": t.raw_m,
                        "k_ell": t.k_ell, "k_m": t.k_m,
                        "value": obs
                    })

            # Monte Carlo p-values at targets
            if args.mc > 0:
                # collect MC values per target per analysis
                mc_vals_psd = {t: [] for t in t2} if psd0 is not None else {}
                mc_vals_cep = {t: [] for t in t2} if cep0 is not None else {}

                for i in range(1, args.mc + 1):
                    if i % 50 == 0:
                        print(f"[mc] {i}/{args.mc}")

                    if args.null == "ell-rot":
                        alm_r = _null_ell_rot(alms[ch], lmax_alm, rng)
                    else:
                        alm_r = _null_lm_rand(alms[ch], lmax_alm, rng)

                    Xr, _, _ = _build_grid_from_alm(
                        alm_r, lmax_alm=lmax_alm, lmin=lmin, lmax=lmax,
                        field=args.field, m_mode=args.m_mode, pad_to_lmax=args.pad_to_lmax
                    )
                    Xrw = _apply_window2d(Xr, args.window2d, normalize_rms=True)
                    Pr = _psd2(Xrw) if psd0 is not None else None
                    Cr = _real_cepstrum2(Pr) if (cep0 is not None and Pr is not None) else None

                    for t in t2:
                        if Pr is not None:
                            mc_vals_psd[t].append(float(Pr[t.k_ell, t.k_m]))
                        if Cr is not None:
                            mc_vals_cep[t].append(float(Cr[t.k_ell, t.k_m]))

                # compute p-values (one-sided: >= observed for PSD; for cepstrum use abs >= abs(obs) to be safer)
                print("\n=== MC p-values at 2D targets ===")
                for t in t2:
                    if psd0 is not None:
                        obs = float(psd0[t.k_ell, t.k_m])
                        arr = np.asarray(mc_vals_psd[t], dtype=float)
                        p = float(np.mean(arr >= obs))
                        print(f"{ch} PSD ({t.label}) p_mc={p:.6g}")
                        mc_rows.append({
                            "channel": ch, "analysis": "psd",
                            "target_ell": t.raw_ell, "target_m": t.raw_m,
                            "k_ell": t.k_ell, "k_m": t.k_m,
                            "obs": obs, "p_mc": p, "mc": args.mc, "null": args.null,
                            "window2d": args.window2d, "field": args.field, "m_mode": args.m_mode,
                            "target_mode": args.target_mode
                        })
                    if cep0 is not None:
                        obs = float(cep0[t.k_ell, t.k_m])
                        arr = np.asarray(mc_vals_cep[t], dtype=float)
                        p = float(np.mean(np.abs(arr) >= abs(obs)))
                        print(f"{ch} CEP ({t.label}) p_mc_abs={p:.6g}")
                        mc_rows.append({
                            "channel": ch, "analysis": "cepstrum",
                            "target_ell": t.raw_ell, "target_m": t.raw_m,
                            "k_ell": t.k_ell, "k_m": t.k_m,
                            "obs": obs, "p_mc_abs": p, "mc": args.mc, "null": args.null,
                            "window2d": args.window2d, "field": args.field, "m_mode": args.m_mode,
                            "target_mode": args.target_mode
                        })

    # Write report
    if args.report_csv:
        rows = []
        # interleave obs + mc summaries
        rows.extend(obs_rows)
        rows.extend(mc_rows)
        _write_csv(args.report_csv, rows)
        print(f"[info] wrote CSV: {args.report_csv}")

if __name__ == "__main__":
    main()
