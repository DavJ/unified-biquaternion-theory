#!/usr/bin/env python3
"""
phase_prime_reset_v2.py

Clean Forensic scan for prime-vs-composite effects in CMB alm phases, with
float-domain shear modes (ell/m/k) and global (look-elsewhere) MC correction.

Design principles:
- Work in float phase domain (radians). No uint8 symbol-domain shear.
- No pseudo Reed-Solomon / XOR "decoders". Measure robust phase/statistics only.
- Prime-gated contrast: Δ = mean(metric|prime ell) - mean(metric|composite ell)
- Theta scan + global MC: compare observed max|Δ(θ)| against null distribution
  of max|Δ(θ)| computed over the full scan interval.

Requires: numpy, healpy
Optional: tqdm (for nicer progress bars)

Example:
MPLBACKEND=Agg python -m forensic_fingerprint.tools.phase_prime_reset_v2 \
  --tt-map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
  --q-map  data/planck_pr3/maps/extracted/SMICA_Q.fits \
  --u-map  data/planck_pr3/maps/extracted/SMICA_U.fits \
  --lmin 128 --lmax 146 --lmax-alm 512 \
  --theta-mode m --theta-scan 0.15:0.30:0.005 \
  --global-mc 500 --weight-mode modes \
  --report-csv scans/ubt_forensic_v2_theta_scan.csv
"""
from __future__ import annotations

import argparse
import csv
import math
import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np

try:
    import healpy as hp
except Exception as e:
    hp = None
    _HEALPY_IMPORT_ERROR = e
else:
    _HEALPY_IMPORT_ERROR = None

try:
    from tqdm import tqdm
except Exception:
    tqdm = None


TAU = 2.0 * math.pi

def wrap_pm_pi(phi: np.ndarray) -> np.ndarray:
    """Wrap angles to (-pi, pi]."""
    x = np.asarray(phi, dtype=np.float64)
    return (x + math.pi) % TAU - math.pi

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

def parse_scan(s: str) -> np.ndarray:
    """Parse 'start:end:step' into inclusive arange (end included if hits grid)."""
    parts = s.split(":")
    if len(parts) != 3:
        raise ValueError("theta-scan must be 'start:end:step'")
    a, b, st = (float(parts[0]), float(parts[1]), float(parts[2]))
    if st <= 0:
        raise ValueError("theta-scan step must be > 0")
    n = int(math.floor((b - a) / st + 1e-12)) + 1
    xs = a + st * np.arange(n, dtype=np.float64)
    xs = xs[xs <= b + 1e-12]
    return xs

def phase_entropy(phi: np.ndarray, bins: int = 64) -> float:
    """Shannon entropy of phase histogram on [-pi, pi)."""
    if phi.size == 0:
        return float("nan")
    h, _ = np.histogram(phi, bins=bins, range=(-math.pi, math.pi), density=False)
    n = float(np.sum(h))
    if n <= 0:
        return float("nan")
    p = h.astype(np.float64) / n
    p = p[p > 0]
    return float(-np.sum(p * np.log(p)))

def rayleigh_R(phi: np.ndarray) -> float:
    """Resultant length R = |mean(exp(i phi))|."""
    if phi.size == 0:
        return float("nan")
    z = np.exp(1j * phi.astype(np.float64))
    return float(np.abs(np.mean(z)))

def quant_pref_cos256(phi: np.ndarray) -> float:
    """Preference for bins of width 2pi/256 via mean(cos(256*phi))."""
    if phi.size == 0:
        return float("nan")
    return float(np.mean(np.cos(256.0 * phi.astype(np.float64))))

def quant_mean_dist_to_grid(phi: np.ndarray, levels: int = 256) -> float:
    """Mean absolute distance to nearest grid point (multiples of 2pi/levels)."""
    if phi.size == 0:
        return float("nan")
    step = TAU / float(levels)
    x = wrap_pm_pi(phi.astype(np.float64))
    nearest = np.round(x / step) * step
    d = np.abs(wrap_pm_pi(x - nearest))
    return float(np.mean(d))


@dataclass
class PhaseSamples:
    """Flattened (phi, ell, m, k) samples, grouped by ell into contiguous segments."""
    phi: np.ndarray
    ell: np.ndarray
    m: np.ndarray
    k: np.ndarray
    unique_ells: np.ndarray
    seg_starts: np.ndarray
    seg_ends: np.ndarray

    def segment_for_ell_index(self, i: int) -> slice:
        return slice(int(self.seg_starts[i]), int(self.seg_ends[i]))


def build_phase_samples_from_alm(
    alm: np.ndarray,
    lmax: int,
    lmin_band: int,
    lmax_band: int,
    use_full_m: bool,
) -> PhaseSamples:
    """Build phase samples for ell in [lmin_band, lmax_band]."""
    if hp is None:
        raise RuntimeError(f"healpy import failed: {_HEALPY_IMPORT_ERROR}")

    ph_list: List[np.ndarray] = []
    ell_list: List[np.ndarray] = []
    m_list: List[np.ndarray] = []

    unique_ells = np.arange(lmin_band, lmax_band + 1, dtype=np.int32)
    seg_starts = np.zeros(unique_ells.size, dtype=np.int64)
    seg_ends = np.zeros(unique_ells.size, dtype=np.int64)

    k_counter = 0
    for i, e in enumerate(unique_ells):
        seg_starts[i] = k_counter

        ms_pos = np.arange(0, e + 1, dtype=np.int32)
        idx_pos = hp.Alm.getidx(lmax, e, ms_pos)
        a_pos = alm[idx_pos]
        ph_pos = np.angle(a_pos).astype(np.float64)

        ph_block = [ph_pos]
        ell_block = [np.full(ms_pos.shape, e, dtype=np.int32)]
        m_block = [ms_pos]

        if use_full_m and e > 0:
            ms_neg = -np.arange(1, e + 1, dtype=np.int32)
            ms_abs = np.arange(1, e + 1, dtype=np.int32)
            ph_neg = wrap_pm_pi(-ph_pos[1:] + math.pi * ms_abs.astype(np.float64))
            ph_block.append(ph_neg)
            ell_block.append(np.full(ms_neg.shape, e, dtype=np.int32))
            m_block.append(ms_neg)

        ph_e = np.concatenate(ph_block)
        ell_e = np.concatenate(ell_block)
        m_e = np.concatenate(m_block)

        ph_list.append(ph_e)
        ell_list.append(ell_e)
        m_list.append(m_e)

        k_counter += ph_e.size
        seg_ends[i] = k_counter

    phi = np.concatenate(ph_list).astype(np.float64)
    ell = np.concatenate(ell_list).astype(np.int32)
    m = np.concatenate(m_list).astype(np.int32)
    k = np.arange(phi.size, dtype=np.int64)

    return PhaseSamples(phi=phi, ell=ell, m=m, k=k,
                        unique_ells=unique_ells, seg_starts=seg_starts, seg_ends=seg_ends)


def build_null_phase_samples(
    lmin_band: int,
    lmax_band: int,
    use_full_m: bool,
    rng: np.random.Generator,
) -> PhaseSamples:
    """Null: phases uniform(-pi,pi) preserving (ell,m) structure and k ordering."""
    ph_list: List[np.ndarray] = []
    ell_list: List[np.ndarray] = []
    m_list: List[np.ndarray] = []

    unique_ells = np.arange(lmin_band, lmax_band + 1, dtype=np.int32)
    seg_starts = np.zeros(unique_ells.size, dtype=np.int64)
    seg_ends = np.zeros(unique_ells.size, dtype=np.int64)

    k_counter = 0
    for i, e in enumerate(unique_ells):
        seg_starts[i] = k_counter

        ms_pos = np.arange(0, e + 1, dtype=np.int32)
        ph_pos = rng.uniform(-math.pi, math.pi, size=ms_pos.size).astype(np.float64)

        ph_block = [ph_pos]
        ell_block = [np.full(ms_pos.shape, e, dtype=np.int32)]
        m_block = [ms_pos]

        if use_full_m and e > 0:
            ms_neg = -np.arange(1, e + 1, dtype=np.int32)
            ph_neg = rng.uniform(-math.pi, math.pi, size=ms_neg.size).astype(np.float64)
            ph_block.append(ph_neg)
            ell_block.append(np.full(ms_neg.shape, e, dtype=np.int32))
            m_block.append(ms_neg)

        ph_e = np.concatenate(ph_block)
        ell_e = np.concatenate(ell_block)
        m_e = np.concatenate(m_block)

        ph_list.append(ph_e)
        ell_list.append(ell_e)
        m_list.append(m_e)

        k_counter += ph_e.size
        seg_ends[i] = k_counter

    phi = np.concatenate(ph_list).astype(np.float64)
    ell = np.concatenate(ell_list).astype(np.int32)
    m = np.concatenate(m_list).astype(np.int32)
    k = np.arange(phi.size, dtype=np.int64)

    return PhaseSamples(phi=phi, ell=ell, m=m, k=k,
                        unique_ells=unique_ells, seg_starts=seg_starts, seg_ends=seg_ends)


def compute_metrics_per_ell(
    samples: PhaseSamples,
    theta_rad: float,
    theta_mode: str,
    entropy_bins: int,
) -> Dict[str, np.ndarray]:
    """Compute per-ell metrics after applying shear in float phase domain."""
    if theta_mode == "ell":
        fac = samples.ell.astype(np.float64)
    elif theta_mode == "m":
        fac = samples.m.astype(np.float64)
    elif theta_mode == "k":
        fac = samples.k.astype(np.float64)
    else:
        raise ValueError(f"unknown theta_mode: {theta_mode}")

    phi_s = wrap_pm_pi(samples.phi + theta_rad * fac)

    R = np.zeros(samples.unique_ells.size, dtype=np.float64)
    H = np.zeros(samples.unique_ells.size, dtype=np.float64)
    Qc = np.zeros(samples.unique_ells.size, dtype=np.float64)
    Qd = np.zeros(samples.unique_ells.size, dtype=np.float64)

    for i in range(samples.unique_ells.size):
        sl = samples.segment_for_ell_index(i)
        ph = phi_s[sl]
        R[i] = rayleigh_R(ph)
        H[i] = phase_entropy(ph, bins=entropy_bins)
        Qc[i] = quant_pref_cos256(ph)
        Qd[i] = quant_mean_dist_to_grid(ph, levels=256)

    return {"R": R, "H": H, "Qc": Qc, "Qd": Qd}


def delta_prime_composite(ells: np.ndarray, values: np.ndarray, weight_mode: str) -> float:
    """Δ = mean_prime(values) - mean_composite(values), with optional weights."""
    ells_i = ells.astype(np.int32)
    v = values.astype(np.float64)

    mask_p = np.array([is_prime(int(e)) for e in ells_i], dtype=bool)
    mask_c = ~mask_p

    if weight_mode == "equal":
        w_all = np.ones_like(ells_i, dtype=np.float64)
    elif weight_mode == "modes":
        w_all = (2.0 * ells_i.astype(np.float64) + 1.0)
    else:
        raise ValueError("weight_mode must be 'equal' or 'modes'")

    vp = v[mask_p]; wp = w_all[mask_p]
    vc = v[mask_c]; wc = w_all[mask_c]

    fp = np.isfinite(vp)
    fc = np.isfinite(vc)
    if not (np.any(fp) and np.any(fc)):
        return float("nan")

    mp = float(np.sum(wp[fp] * vp[fp]) / (np.sum(wp[fp]) + 1e-18))
    mc = float(np.sum(wc[fc] * vc[fc]) / (np.sum(wc[fc]) + 1e-18))
    return mp - mc


def load_alms(args) -> Dict[str, np.ndarray]:
    """Load/compute alms for TT/EE/BB based on provided args."""
    if hp is None:
        raise RuntimeError(f"healpy import failed: {_HEALPY_IMPORT_ERROR}")
    lmax = int(args.lmax_alm)

    out: Dict[str, np.ndarray] = {}

    if args.tt_alm:
        out["TT"] = hp.read_alm(args.tt_alm)
    elif args.tt_map:
        m = hp.read_map(args.tt_map, field=0, verbose=False)
        out["TT"] = hp.map2alm(m, lmax=lmax)
    else:
        raise ValueError("Provide --tt-map or --tt-alm")

    if args.e_alm:
        out["EE"] = hp.read_alm(args.e_alm)
    if args.b_alm:
        out["BB"] = hp.read_alm(args.b_alm)

    if ("EE" not in out or "BB" not in out) and (args.q_map and args.u_map):
        q = hp.read_map(args.q_map, verbose=False)
        u = hp.read_map(args.u_map, verbose=False)
        e, b = hp.map2alm_spin([q, u], spin=2, lmax=lmax)
        out.setdefault("EE", e)
        out.setdefault("BB", b)

    return out


def run_channel_scan(chan: str, alm: np.ndarray, args, theta_degs: np.ndarray, rng: np.random.Generator):
    """Run scan + optional global MC for one channel."""
    lmin_band = int(args.lmin)
    lmax_band = int(args.lmax)
    lmax_alm = int(args.lmax_alm)

    obs_samples = build_phase_samples_from_alm(
        alm=alm, lmax=lmax_alm,
        lmin_band=lmin_band, lmax_band=lmax_band,
        use_full_m=bool(args.use_full_m),
    )

    metrics = ["R", "H", "Qc", "Qd"]
    curves = {m: np.zeros(theta_degs.size, dtype=np.float64) for m in metrics}

    for ti, th_deg in enumerate(theta_degs):
        th_rad = math.radians(float(th_deg))
        per_ell = compute_metrics_per_ell(obs_samples, th_rad, args.theta_mode, int(args.entropy_bins))
        curves["R"][ti]  = delta_prime_composite(obs_samples.unique_ells, per_ell["R"],  args.weight_mode)
        curves["H"][ti]  = delta_prime_composite(obs_samples.unique_ells, -per_ell["H"], args.weight_mode)
        curves["Qc"][ti] = delta_prime_composite(obs_samples.unique_ells, per_ell["Qc"], args.weight_mode)
        curves["Qd"][ti] = delta_prime_composite(obs_samples.unique_ells, -per_ell["Qd"], args.weight_mode)

    obs_max = {m: float(np.nanmax(np.abs(curves[m]))) for m in metrics}

    p_global = {m: float("nan") for m in metrics}
    if int(args.global_mc) > 0:
        mc = int(args.global_mc)
        null_max = {m: np.zeros(mc, dtype=np.float64) for m in metrics}

        iterator = range(mc)
        if tqdm is not None and not args.no_tqdm:
            iterator = tqdm(iterator, desc=f"[{chan}] global MC", leave=False)

        for i in iterator:
            null_samples = build_null_phase_samples(lmin_band, lmax_band, bool(args.use_full_m), rng)

            max_abs = {m: 0.0 for m in metrics}
            for th_deg in theta_degs:
                th_rad = math.radians(float(th_deg))
                per_ell = compute_metrics_per_ell(null_samples, th_rad, args.theta_mode, int(args.entropy_bins))
                dR  = delta_prime_composite(null_samples.unique_ells, per_ell["R"],  args.weight_mode)
                dH  = delta_prime_composite(null_samples.unique_ells, -per_ell["H"], args.weight_mode)
                dQc = delta_prime_composite(null_samples.unique_ells, per_ell["Qc"], args.weight_mode)
                dQd = delta_prime_composite(null_samples.unique_ells, -per_ell["Qd"], args.weight_mode)
                max_abs["R"]  = max(max_abs["R"],  abs(float(dR)))
                max_abs["H"]  = max(max_abs["H"],  abs(float(dH)))
                max_abs["Qc"] = max(max_abs["Qc"], abs(float(dQc)))
                max_abs["Qd"] = max(max_abs["Qd"], abs(float(dQd)))

            for m in metrics:
                null_max[m][i] = max_abs[m]

        for m in metrics:
            obs = obs_max[m]
            ge = float(np.sum(null_max[m] >= obs))
            p_global[m] = (ge + 1.0) / (mc + 1.0)

    return curves, obs_max, p_global


def write_report_csv(path: str, theta_degs: np.ndarray, chan_curves: Dict[str, Dict[str, np.ndarray]]) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    metrics = ["R", "H", "Qc", "Qd"]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["theta_deg", "channel"] + [f"delta_{m}" for m in metrics])
        for chan, curves in chan_curves.items():
            for i, th in enumerate(theta_degs):
                w.writerow([f"{float(th):.12g}", chan] + [f"{float(curves[m][i]):.12g}" for m in metrics])


def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="UBT Forensic v2: float-phase shear scan with global MC look-elsewhere correction")
    ap.add_argument("--tt-map", type=str, default=None)
    ap.add_argument("--tt-alm", type=str, default=None)
    ap.add_argument("--q-map", type=str, default=None)
    ap.add_argument("--u-map", type=str, default=None)
    ap.add_argument("--e-alm", type=str, default=None)
    ap.add_argument("--b-alm", type=str, default=None)

    ap.add_argument("--lmin", type=int, default=128)
    ap.add_argument("--lmax", type=int, default=146)
    ap.add_argument("--lmax-alm", dest="lmax_alm", type=int, default=512)

    ap.add_argument("--use-full-m", action="store_true")
    ap.add_argument("--theta-mode", choices=["ell", "m", "k"], default="m")
    ap.add_argument("--theta-scan", type=str, required=True, help="start:end:step in degrees")

    ap.add_argument("--entropy-bins", type=int, default=64)
    ap.add_argument("--weight-mode", choices=["equal", "modes"], default="modes")

    ap.add_argument("--global-mc", type=int, default=0)
    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--report-csv", type=str, default=None)
    ap.add_argument("--no-tqdm", action="store_true")
    return ap


def main() -> int:
    if hp is None:
        print(f"[error] healpy is required but failed to import: {_HEALPY_IMPORT_ERROR}", file=sys.stderr)
        return 2

    args = build_arg_parser().parse_args()
    theta_degs = parse_scan(args.theta_scan)
    rng = np.random.default_rng(int(args.seed))

    alms = load_alms(args)

    chan_curves = {}
    chan_obs_max = {}
    chan_p_global = {}

    print(f"[phase_prime_reset_v2] ell=[{args.lmin},{args.lmax}] lmax_alm={args.lmax_alm} "
          f"theta_mode={args.theta_mode} scan={args.theta_scan} full_m={bool(args.use_full_m)} "
          f"global_mc={int(args.global_mc)} weight={args.weight_mode}")

    for chan, alm in alms.items():
        curves, obs_max, p_global = run_channel_scan(chan, alm, args, theta_degs, rng)
        chan_curves[chan] = curves
        chan_obs_max[chan] = obs_max
        chan_p_global[chan] = p_global

    print("\n=== Observed scan maxima (max |Δ(θ)| over scan) ===")
    for chan in sorted(chan_obs_max.keys()):
        mx = chan_obs_max[chan]
        print(f"{chan}: max|ΔR|={mx['R']:.6g}  max|Δ(-H)|={mx['H']:.6g}  max|Δ(Qc)|={mx['Qc']:.6g}  max|Δ(-Qd)|={mx['Qd']:.6g}")

    if int(args.global_mc) > 0:
        print("\n=== Global p-values (look-elsewhere, based on max|Δ| over scan) ===")
        for chan in sorted(chan_p_global.keys()):
            pg = chan_p_global[chan]
            print(f"{chan}: p_global(R)={pg['R']:.6g}  p_global(-H)={pg['H']:.6g}  p_global(Qc)={pg['Qc']:.6g}  p_global(-Qd)={pg['Qd']:.6g}")

    if args.report_csv:
        write_report_csv(args.report_csv, theta_degs, chan_curves)
        print(f"\n[info] wrote scan CSV: {args.report_csv}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
