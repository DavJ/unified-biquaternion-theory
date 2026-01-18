#!/usr/bin/env python3
"""
Spectral parity / RS-consistency test on Planck CMB alms.

Unified & repaired version - 2026-01-18
Key fixes:
- Proper m<0 reconstruction for phase streams (healpy stores only m>=0 packed alm).
- Safe phase -> uint8 symbolization (wrap to (-pi,pi], shift by +pi, quantize to 0..255).
- Phase shear supports scan + CSV reporting.
- Robust CLI: includes --phase-shear-scan, --phase-shear-report-prefix, and legacy alias --prime-plot-prefix.
- Symbols supports slicing/subscript (__getitem__).

No scipy/matplotlib required for core operation.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

try:
    import healpy as hp
except Exception as e:
    hp = None
    _HEALPY_IMPORT_ERROR = e
else:
    _HEALPY_IMPORT_ERROR = None


def _ensure_healpy() -> None:
    if hp is None:
        raise RuntimeError(f"healpy import failed: {_HEALPY_IMPORT_ERROR!r}")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if (n % 2) == 0:
        return False
    r = int(math.isqrt(n))
    f = 3
    while f <= r:
        if (n % f) == 0:
            return False
        f += 2
    return True


def ell_shell_slice(ell: int) -> slice:
    start = ell * ell
    end = (ell + 1) * (ell + 1)
    return slice(start, end)


def phase_wrap(phi: np.ndarray) -> np.ndarray:
    phi = np.asarray(phi, dtype=np.float64)
    return (phi + math.pi) % (2.0 * math.pi) - math.pi


def phase_to_symbol(phi: np.ndarray) -> np.ndarray:
    phi = phase_wrap(phi)
    u = (phi + math.pi) / (2.0 * math.pi)
    u = np.mod(u, 1.0)
    sym = np.floor(u * 256.0).astype(np.int32)
    return np.clip(sym, 0, 255).astype(np.uint8)


@dataclass
class Symbols:
    arr: np.ndarray
    ells: np.ndarray

    def __post_init__(self) -> None:
        self.arr = np.asarray(self.arr, dtype=np.uint8).ravel()
        self.ells = np.asarray(self.ells, dtype=np.int32).ravel()
        if self.ells.size != self.arr.size:
            raise ValueError(f"Symbols: ells size {self.ells.size} != arr size {self.arr.size}")

    def __len__(self) -> int:
        return int(self.arr.size)

    def __getitem__(self, key):
        return self.arr[key]


def read_map_field(path: str, field: int):
    _ensure_healpy()
    return hp.read_map(path, field=field)


def read_qu_maps(q_path: str, u_path: str):
    _ensure_healpy()
    q = hp.read_map(q_path, field=0)
    u = hp.read_map(u_path, field=0)
    return q, u


def load_channel_alm(args: argparse.Namespace, chan: str, lmax: int) -> np.ndarray:
    _ensure_healpy()
    chan = chan.upper()
    if chan == "TT":
        if args.tt_alm:
            return hp.read_alm(args.tt_alm)
        if not args.tt_map:
            raise ValueError("TT requires --tt-map or --tt-alm")
        m = read_map_field(args.tt_map, field=0)
        return hp.map2alm(m, lmax=lmax)
    if chan in ("EE", "BB"):
        if chan == "EE" and args.e_alm:
            return hp.read_alm(args.e_alm)
        if chan == "BB" and args.b_alm:
            return hp.read_alm(args.b_alm)
        if not (args.q_map and args.u_map):
            raise ValueError(f"{chan} requires --e-alm/--b-alm or both --q-map and --u-map")
        q, u = read_qu_maps(args.q_map, args.u_map)
        e_alm, b_alm = hp.map2alm_spin([q, u], spin=2, lmax=lmax)
        return e_alm if chan == "EE" else b_alm
    raise ValueError(f"Unknown channel: {chan}")


def get_channels(args: argparse.Namespace) -> Iterable[str]:
    if args.channels:
        for c in str(args.channels).split(","):
            c = c.strip().upper()
            if c:
                yield c
        return
    has_tt = bool(args.tt_map or args.tt_alm)
    has_qu = bool(args.q_map and args.u_map)
    has_e = bool(args.e_alm)
    has_b = bool(args.b_alm)
    if has_tt:
        yield "TT"
    if has_e or has_qu:
        yield "EE"
    if has_b or has_qu:
        yield "BB"


def symbols_from_alm_phase(
    alm: np.ndarray,
    lmax: int,
    *,
    differential: bool = False,
    dither_amp: float = 0.0,
    rng: Optional[np.random.Generator] = None,
) -> Symbols:
    _ensure_healpy()
    ell, m = hp.Alm.getlm(lmax, np.arange(hp.Alm.getsize(lmax)))
    n_stream = (lmax + 1) * (lmax + 1)
    phi_stream = np.zeros(n_stream, dtype=np.float64)
    ells_stream = np.zeros(n_stream, dtype=np.int32)
    phi_plus = np.arctan2(np.imag(alm), np.real(alm)).astype(np.float64, copy=False)

    for i in range(phi_plus.size):
        e = int(ell[i])
        mm = int(m[i])
        ells_stream[ell_shell_slice(e)] = e
        phi_stream[e * e + e + mm] = float(phi_plus[i])
        if mm > 0:
            phm = -float(phi_plus[i]) + math.pi * float(mm)
            phi_stream[e * e + e - mm] = (phm + math.pi) % (2.0 * math.pi) - math.pi

    if dither_amp and float(dither_amp) > 0.0:
        if rng is None:
            rng = np.random.default_rng(0)
        phi_stream = phi_stream + (rng.random(size=phi_stream.shape) - 0.5) * float(dither_amp)

    if differential:
        phi_stream = phase_wrap(np.diff(phi_stream, prepend=phi_stream[0]))

    return Symbols(arr=phase_to_symbol(phi_stream), ells=ells_stream)


def apply_phase_shear(sym: Symbols, theta_deg: float, mode: str = "k") -> Symbols:
    theta_deg = float(theta_deg)
    if abs(theta_deg) < 1e-15:
        return sym
    theta_rad = theta_deg * math.pi / 180.0
    scale = 256.0 / (2.0 * math.pi) * theta_rad
    arr16 = sym.arr.astype(np.int16, copy=False)
    mode = str(mode).lower()
    if mode == "k":
        f = np.arange(arr16.size, dtype=np.float64)
    elif mode == "ell":
        f = sym.ells.astype(np.float64)
    else:
        raise ValueError("phase-shear-mode must be 'k' or 'ell'")
    offset = np.rint(scale * f).astype(np.int16)
    out = ((arr16 + offset) & 0xFF).astype(np.uint8)
    return Symbols(arr=out, ells=sym.ells.copy())


def truncate_symbols(sym: Symbols, *, step: int, max_frames: int) -> Symbols:
    step = int(step)
    max_frames = int(max_frames)
    n_cap = min(max_frames * step, sym.arr.size)
    n_cap = (n_cap // step) * step
    return Symbols(arr=sym.arr[:n_cap], ells=sym.ells[:n_cap])


def _compute_channel_symbols(chan: str, args: argparse.Namespace, *, lmax: int, rng: np.random.Generator) -> Symbols:
    alm = load_channel_alm(args=args, chan=chan, lmax=lmax)
    sym = symbols_from_alm_phase(
        alm,
        lmax,
        differential=bool(args.differential_phase),
        dither_amp=float(args.phase_dither_amp),
        rng=rng,
    )
    if abs(float(args.phase_shear_deg)) > 1e-15:
        sym = apply_phase_shear(sym, float(args.phase_shear_deg), mode=str(args.phase_shear_mode))
    return truncate_symbols(sym, step=int(args.step), max_frames=int(args.max_frames))


def _hamming_valid_rate_uint8(block: np.ndarray) -> float:
    block = np.asarray(block, dtype=np.uint8)
    if block.size != 255:
        return 0.0
    data = block[:201]
    parity = block[201:]
    acc = np.uint8(0)
    chk = np.empty(54, dtype=np.uint8)
    for i in range(201):
        acc = np.uint8(((int(acc) << 1) & 0xFF) | ((int(acc) >> 7) & 0x01))
        acc ^= data[i]
        if i < 54:
            chk[i] = acc
        else:
            chk[i % 54] ^= acc
    return float(np.mean(chk == parity))


def hamming_valid_rate_fast(symbols: np.ndarray) -> float:
    symbols = np.asarray(symbols, dtype=np.uint8)
    if symbols.size < 255:
        return float("nan")
    n_frames = symbols.size // 255
    if n_frames <= 0:
        return float("nan")
    s = 0.0
    for i in range(n_frames):
        s += _hamming_valid_rate_uint8(symbols[i * 255 : (i + 1) * 255])
    return float(s / n_frames)


def rs_mean_zero_proxy(symbols: np.ndarray) -> float:
    symbols = np.asarray(symbols, dtype=np.uint8)
    n = symbols.size // 255
    if n <= 0:
        return float("nan")
    z = np.array([np.sum(symbols[i * 255 : (i + 1) * 255] == 0) for i in range(n)], dtype=float)
    return float(np.mean(z))


def rs_tail_rate_proxy(symbols: np.ndarray, tail_k: int = 8) -> float:
    symbols = np.asarray(symbols, dtype=np.uint8)
    n = symbols.size // 255
    if n <= 0:
        return float("nan")
    z = np.array([np.sum(symbols[i * 255 : (i + 1) * 255] == 0) for i in range(n)], dtype=int)
    return float(np.mean(z >= int(tail_k)))


def prime_gated_integrity_curve(symbol_stream: Symbols, lmin: int, lmax: int) -> Tuple[np.ndarray, np.ndarray]:
    ells = np.arange(int(lmin), int(lmax) + 1, dtype=np.int32)
    integrity = np.array([hamming_valid_rate_fast(symbol_stream[ell_shell_slice(int(e))]) for e in ells], dtype=float)
    return ells, integrity


def prime_gated_delta_mean(ells: np.ndarray, integrity: np.ndarray) -> float:
    mask_p = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    p = integrity[mask_p]
    c = integrity[~mask_p]
    p = p[np.isfinite(p)]
    c = c[np.isfinite(c)]
    if p.size == 0 or c.size == 0:
        return 0.0
    return float(np.mean(p) - np.mean(c))


def gaussian_weights_for_ell(ells: np.ndarray, center: float, sigma: float) -> np.ndarray:
    sigma = float(sigma)
    if sigma <= 0:
        raise ValueError("sigma must be > 0")
    w = np.exp(-0.5 * ((ells.astype(float) - float(center)) / sigma) ** 2)
    return w / (np.mean(w) + 1e-18)


def prime_gated_delta_mean_weighted(ells: np.ndarray, integrity: np.ndarray, weights: np.ndarray) -> float:
    mask_p = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    w = np.asarray(weights, dtype=float)
    ip = integrity[mask_p]
    ic = integrity[~mask_p]
    wp = w[mask_p]
    wc = w[~mask_p]
    fp = np.isfinite(ip)
    fc = np.isfinite(ic)
    if not (np.any(fp) and np.any(fc)):
        return 0.0
    mp = float(np.sum(wp[fp] * ip[fp]) / (np.sum(wp[fp]) + 1e-18))
    mc = float(np.sum(wc[fc] * ic[fc]) / (np.sum(wc[fc]) + 1e-18))
    return float(mp - mc)


def prime_gated_permutation_pvalue(ells: np.ndarray, integrity: np.ndarray, weights: Optional[np.ndarray], n_perm: int, rng: np.random.Generator) -> float:
    n_perm = int(n_perm)
    if n_perm <= 0:
        return 1.0
    mask_p = np.array([is_prime(int(e)) for e in ells], dtype=bool)
    obs = prime_gated_delta_mean_weighted(ells, integrity, weights) if weights is not None else prime_gated_delta_mean(ells, integrity)
    if not np.isfinite(obs):
        return 1.0
    cnt = 0
    for _ in range(n_perm):
        perm = rng.permutation(mask_p)
        if weights is not None:
            ip = integrity[perm]
            ic = integrity[~perm]
            wp = weights[perm]
            wc = weights[~perm]
            fp = np.isfinite(ip)
            fc = np.isfinite(ic)
            if not (np.any(fp) and np.any(fc)):
                continue
            d = float(np.sum(wp[fp] * ip[fp]) / (np.sum(wp[fp]) + 1e-18) - np.sum(wc[fc] * ic[fc]) / (np.sum(wc[fc]) + 1e-18))
        else:
            ip = integrity[perm]
            ic = integrity[~perm]
            ip = ip[np.isfinite(ip)]
            ic = ic[np.isfinite(ic)]
            if ip.size == 0 or ic.size == 0:
                continue
            d = float(np.mean(ip) - np.mean(ic))
        if abs(d) >= abs(obs):
            cnt += 1
    return float((cnt + 1) / (n_perm + 1))


def randomize_phases_per_ell(alm: np.ndarray, lmax: int, rng: np.random.Generator) -> np.ndarray:
    _ensure_healpy()
    out = np.array(alm, copy=True)
    ell, _m = hp.Alm.getlm(lmax, np.arange(hp.Alm.getsize(lmax)))
    for e in range(lmax + 1):
        idx = np.where(ell == e)[0]
        if idx.size == 0:
            continue
        ph = rng.uniform(-math.pi, math.pi, size=idx.size)
        amp = np.abs(out[idx])
        out[idx] = amp * (np.cos(ph) + 1j * np.sin(ph))
    return out


def mc_null_for_channel(args: argparse.Namespace, chan: str, lmax: int, rng: np.random.Generator, sym_real: Symbols) -> Dict[str, float]:
    mc = int(args.mc)
    if mc <= 0:
        return {"p_rs_mean_zero": float("nan"), "p_rs_tail_rate": float("nan"), "delta_mc_mean": float("nan"), "delta_mc_std": float("nan"), "delta_mc_p_two_sided": float("nan")}
    alm0 = load_channel_alm(args=args, chan=chan, lmax=lmax)
    rz_real = rs_mean_zero_proxy(sym_real.arr)
    rt_real = rs_tail_rate_proxy(sym_real.arr, tail_k=int(args.rs_tail_k))
    delta_real = 0.0
    if args.prime_gated:
        ells_r, integ_r = prime_gated_integrity_curve(sym_real, int(args.lmin), int(args.lmax))
        if args.prime_weight_center is not None:
            w = gaussian_weights_for_ell(ells_r, float(args.prime_weight_center), float(args.prime_weight_sigma))
            delta_real = prime_gated_delta_mean_weighted(ells_r, integ_r, w)
        else:
            delta_real = prime_gated_delta_mean(ells_r, integ_r)
    rz_mc = np.zeros(mc, dtype=float)
    rt_mc = np.zeros(mc, dtype=float)
    d_mc = np.zeros(mc, dtype=float)
    for i in range(mc):
        alm_r = randomize_phases_per_ell(alm0, lmax, rng)
        s = symbols_from_alm_phase(alm_r, lmax, differential=bool(args.differential_phase), dither_amp=float(args.phase_dither_amp), rng=rng)
        if abs(float(args.phase_shear_deg)) > 1e-15:
            s = apply_phase_shear(s, float(args.phase_shear_deg), mode=str(args.phase_shear_mode))
        s = truncate_symbols(s, step=int(args.step), max_frames=int(args.max_frames))
        rz_mc[i] = rs_mean_zero_proxy(s.arr)
        rt_mc[i] = rs_tail_rate_proxy(s.arr, tail_k=int(args.rs_tail_k))
        if args.prime_gated:
            ells, integ = prime_gated_integrity_curve(s, int(args.lmin), int(args.lmax))
            if args.prime_weight_center is not None:
                w = gaussian_weights_for_ell(ells, float(args.prime_weight_center), float(args.prime_weight_sigma))
                d_mc[i] = prime_gated_delta_mean_weighted(ells, integ, w)
            else:
                d_mc[i] = prime_gated_delta_mean(ells, integ)
        else:
            d_mc[i] = 0.0
    p_rz = float(np.mean(rz_mc >= rz_real)) if np.isfinite(rz_real) else float("nan")
    p_rt = float(np.mean(rt_mc >= rt_real)) if np.isfinite(rt_real) else float("nan")
    if args.prime_gated:
        mu = float(np.mean(d_mc))
        sd = float(np.std(d_mc, ddof=0))
        p_delta = float(np.mean(np.abs(d_mc - mu) >= abs(delta_real - mu)))
    else:
        mu = 0.0
        sd = 0.0
        p_delta = float("nan")
    return {"p_rs_mean_zero": p_rz, "p_rs_tail_rate": p_rt, "delta_mc_mean": mu, "delta_mc_std": sd, "delta_mc_p_two_sided": p_delta}


def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="spectral_parity_test")
    ap.add_argument("--lmin", type=int, default=2)
    ap.add_argument("--lmax", type=int, default=256)
    ap.add_argument("--tt-map", dest="tt_map", type=str, default=None)
    ap.add_argument("--tt-alm", dest="tt_alm", type=str, default=None)
    ap.add_argument("--q-map", dest="q_map", type=str, default=None)
    ap.add_argument("--u-map", dest="u_map", type=str, default=None)
    ap.add_argument("--e-alm", dest="e_alm", type=str, default=None)
    ap.add_argument("--b-alm", dest="b_alm", type=str, default=None)
    ap.add_argument("--step", type=int, default=255)
    ap.add_argument("--max-frames", type=int, default=2048)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--prime-gated", action="store_true")
    ap.add_argument("--prime-perm", type=int, default=20000)
    ap.add_argument("--prime-weight-center", type=float, default=None)
    ap.add_argument("--prime-weight-sigma", type=float, default=0.0)
    ap.add_argument("--phase-shear-deg", type=float, default=0.0)
    ap.add_argument("--phase-shear-mode", choices=["k", "ell"], default="k")
    ap.add_argument("--phase-shear-scan", type=str, default=None, help="start:stop:step in degrees")
    ap.add_argument("--phase-shear-report-prefix", type=str, default=None, help="write scan CSV to <prefix>.csv")
    ap.add_argument("--prime-plot-prefix", type=str, default=None, help="DEPRECATED alias for --phase-shear-report-prefix")
    ap.add_argument("--phase-dither-amp", type=float, default=0.0, help="tiny phase dither in radians (debug)")
    ap.add_argument("--differential-phase", action="store_true", help="use phase differences (DPSK-like)")
    ap.add_argument("--mc", type=int, default=0)
    ap.add_argument("--rs-tail-k", dest="rs_tail_k", type=int, default=8)
    ap.add_argument("--channels", type=str, default=None, help="Comma-separated list: TT,EE,BB (optional)")
    return ap


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_arg_parser().parse_args(list(argv) if argv is not None else None)
    if args.prime_plot_prefix and not args.phase_shear_report_prefix:
        args.phase_shear_report_prefix = args.prime_plot_prefix
    _ensure_healpy()
    rng = np.random.default_rng(int(args.seed))
    lmax = int(args.lmax)
    print(f"[spectral_parity_test] file={__file__} lmin={args.lmin} lmax={args.lmax} mc={args.mc} prime_gated={bool(args.prime_gated)}", flush=True)
    syms: Dict[str, Symbols] = {}
    channels = list(get_channels(args))
    if not channels:
        print("[error] No channels enabled. Provide --tt-map/--tt-alm and/or Q/U or E/B ALMs.", flush=True)
        return 2
    for chan in channels:
        try:
            print(f"[info] computing channel {chan} symbols...", flush=True)
            syms[chan] = _compute_channel_symbols(chan, args, lmax=lmax, rng=rng)
            print(f"[info] channel {chan}: symbols={syms[chan].arr.size}", flush=True)
        except Exception as e:
            print(f"[warn] channel {chan}: failed to compute symbols: {e}", flush=True)
    if not syms:
        print("[error] No symbol streams were produced. Check input paths and lmax.", flush=True)
        return 2
    print("\n=== Observed scores ===", flush=True)
    for chan, s in syms.items():
        hr = hamming_valid_rate_fast(s.arr)
        rz = rs_mean_zero_proxy(s.arr)
        rt = rs_tail_rate_proxy(s.arr, tail_k=int(args.rs_tail_k))
        print(f"{chan}: hamming_rate={hr:.6f}  rs_mean_zero={rz:.3f}  rs_tail_rate(>={args.rs_tail_k})={rt:.6f}", flush=True)
        if args.prime_gated:
            ells, integ = prime_gated_integrity_curve(s, int(args.lmin), int(args.lmax))
            if args.prime_weight_center is not None:
                w = gaussian_weights_for_ell(ells, float(args.prime_weight_center), float(args.prime_weight_sigma))
                delta = prime_gated_delta_mean_weighted(ells, integ, w)
            else:
                w = None
                delta = prime_gated_delta_mean(ells, integ)
            p_perm = prime_gated_permutation_pvalue(ells, integ, w, int(args.prime_perm), rng)
            print(f"  [Prime-Gated] Δmean(P−C)={delta:+.7g}  perm_p(two-sided)={p_perm:.6g}  (perm={args.prime_perm})", flush=True)
    if int(args.mc) > 0:
        print("\n=== Monte Carlo (phase randomization per ell) ===", flush=True)
        for chan, s in syms.items():
            d = mc_null_for_channel(args=args, chan=chan, lmax=lmax, rng=rng, sym_real=s)
            print(f"{chan}: p(rs_mean_zero)={d['p_rs_mean_zero']:.6g}  p(rs_tail_rate)={d['p_rs_tail_rate']:.6g}  (mc={args.mc})", flush=True)
            if args.prime_gated:
                print(f"  [Prime-Gated null] Δmean(P−C): mc_mean={d['delta_mc_mean']:+.3g}  mc_std={d['delta_mc_std']:.3g}  mc_p(two-sided)={d['delta_mc_p_two_sided']:.6g}", flush=True)
    if args.phase_shear_scan and args.prime_gated:
        print("\n=== Phase-shear scan (Prime-Gated) ===", flush=True)
        start_s, stop_s, step_s = args.phase_shear_scan.split(":")
        start, stop, step = float(start_s), float(stop_s), float(step_s)
        rows: List[Tuple[float, str, float]] = []
        theta = start
        while theta <= stop + 1e-12:
            for chan, sym_base in syms.items():
                sym_t = apply_phase_shear(sym_base, theta, mode=str(args.phase_shear_mode))
                ells, integ = prime_gated_integrity_curve(sym_t, int(args.lmin), int(args.lmax))
                delta = prime_gated_delta_mean(ells, integ)
                print(f"Theta={theta:+.3f} {chan}: Δ={delta:+.7g}", flush=True)
                rows.append((float(theta), str(chan), float(delta)))
            theta += step
        if args.phase_shear_report_prefix:
            out_csv = f"{args.phase_shear_report_prefix}.csv"
            os.makedirs(os.path.dirname(out_csv) or ".", exist_ok=True)
            with open(out_csv, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["theta_deg", "channel", "delta_mean_prime_minus_composite"])
                w.writerows(rows)
            print(f"[info] scan report written: {out_csv}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
