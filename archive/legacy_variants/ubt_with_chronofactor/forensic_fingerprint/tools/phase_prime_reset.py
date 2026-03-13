#!/usr/bin/env python3
from __future__ import annotations
import argparse, math
import numpy as np

try:
    import healpy as hp
except Exception as e:
    hp = None
    _E = e
else:
    _E = None

def wrap(phi):
    return (phi + np.pi) % (2*np.pi) - np.pi

def is_prime(n:int)->bool:
    if n < 2: return False
    if n in (2,3): return True
    if n%2==0: return False
    r=int(math.isqrt(n)); f=3
    while f<=r:
        if n%f==0: return False
        f+=2
    return True

def load_tt_alm(tt_map, tt_alm, lmax):
    if hp is None:_toggle()
    if tt_alm:
        return hp.read_alm(tt_alm)
    m = hp.read_map(tt_map, field=0)
    return hp.map2alm(m, lmax=lmax)

def _toggle():
    raise RuntimeError(f"healpy import failed: {_E!r}")

def phases_by_ell(alm, lmax, use_full_m: bool):
    ell, m = hp.Alm.getlm(lmax, np.arange(hp.Alm.getsize(lmax)))
    ph = np.angle(alm).astype(np.float64)
    out = {e: [] for e in range(lmax+1)}
    for i in range(ph.size):
        e = int(ell[i]); mm = int(m[i])
        out[e].append(ph[i])
        if use_full_m and mm > 0:
            # a_{l,-m} = (-1)^m a*_{l,m} => phase(-m)= -phase(m) + m*pi
            out[e].append(wrap(-ph[i] + mm*np.pi))
    for e in out:
        out[e] = np.array(out[e], dtype=np.float64) if len(out[e]) else np.empty(0, dtype=np.float64)
    return out

def rayleigh_R(phases: np.ndarray) -> float:
    if phases.size == 0: return float("nan")
    z = np.exp(1j*phases)
    return float(np.abs(np.mean(z)))

def phase_entropy(phases: np.ndarray, bins: int = 32) -> float:
    if phases.size == 0: return float("nan")
    h, _ = np.histogram(phases, bins=bins, range=(-np.pi, np.pi), density=False)
    p = h.astype(np.float64)
    p = p / (p.sum() + 1e-18)
    p = p[p>0]
    return float(-np.sum(p*np.log(p)))

def weighted_delta(metric_by_ell: dict, lmin:int, lmax:int):
    primes=[]; comps=[]; wp=[]; wc=[]
    for e in range(lmin, lmax+1):
        v = metric_by_ell.get(e, float("nan"))
        if not np.isfinite(v): 
            continue
        w = 2*e + 1
        if is_prime(e):
            primes.append(v); wp.append(w)
        else:
            comps.append(v); wc.append(w)
    if not primes or not comps:
        return float("nan")
    mp = np.sum(np.array(primes)*np.array(wp)) / (np.sum(wp)+1e-18)
    mc = np.sum(np.array(comps)*np.array(wc)) / (np.sum(wc)+1e-18)
    return float(mp - mc)

def randomize_phases_per_ell(alm, lmax, rng):
    out = np.array(alm, copy=True)
    ell, _ = hp.Alm.getlm(lmax, np.arange(hp.Alm.getsize(lmax)))
    for e in range(lmax+1):
        idx = np.where(ell==e)[0]
        if idx.size==0: continue
        ph = rng.uniform(-np.pi, np.pi, size=idx.size)
        amp = np.abs(out[idx])
        out[idx] = amp * (np.cos(ph) + 1j*np.sin(ph))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--tt-map", type=str, required=False)
    ap.add_argument("--tt-alm", type=str, required=False)
    ap.add_argument("--lmin", type=int, default=128)
    ap.add_argument("--lmax", type=int, default=146)
    ap.add_argument("--lmax-alm", type=int, default=512)
    ap.add_argument("--use-full-m", action="store_true")
    ap.add_argument("--theta-deg", type=float, default=0.0)
    ap.add_argument("--theta-mode", choices=["ell","k"], default="ell")
    ap.add_argument("--mc", type=int, default=500)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--entropy-bins", type=int, default=32)
    args=ap.parse_args()

    if hp is None: _toggle()
    rng=np.random.default_rng(args.seed)
    alm = load_tt_alm(args.tt_map, args.tt_alm, args.lmax_alm)

    # optional shear in PHASE domain: phi_{ellm} += theta * ell  (ell-mode)
    # note: this is a placeholder shear model; you can also shear by index if desired
    def apply_shear(ph_by_ell):
        if abs(args.theta_deg) < 1e-15:
            return ph_by_ell
        th = args.theta_deg * np.pi/180.0
        out={}
        for e, ph in ph_by_ell.items():
            if ph.size==0: 
                out[e]=ph
                continue
            if args.theta_mode == "ell":
                out[e]=wrap(ph + th*e)
            else:
                # "k" mode not well-defined here; keep as ell for hard reset
                out[e]=wrap(ph + th*e)
        return out

    ph0 = phases_by_ell(alm, args.lmax_alm, args.use_full_m)
    ph0 = apply_shear(ph0)

    R_by = {e: rayleigh_R(ph) for e, ph in ph0.items()}
    H_by = {e: phase_entropy(ph, bins=args.entropy_bins) for e, ph in ph0.items()}

    dR = weighted_delta(R_by, args.lmin, args.lmax)
    dH = weighted_delta({e: -H_by[e] for e in H_by}, args.lmin, args.lmax)  # higher = more structured

    print("=== Observed (float-phase) ===")
    print(f"ΔR(prime-composite) = {dR:+.6g}")
    print(f"Δ(-Entropy)(prime-composite) = {dH:+.6g}")

    if args.mc > 0:
        dR_mc=np.zeros(args.mc); dH_mc=np.zeros(args.mc)
        for i in range(args.mc):
            ar = randomize_phases_per_ell(alm, args.lmax_alm, rng)
            ph = phases_by_ell(ar, args.lmax_alm, args.use_full_m)
            ph = apply_shear(ph)
            Rb = {e: rayleigh_R(p) for e,p in ph.items()}
            Hb = {e: phase_entropy(p, bins=args.entropy_bins) for e,p in ph.items()}
            dR_mc[i]=weighted_delta(Rb, args.lmin, args.lmax)
            dH_mc[i]=weighted_delta({e: -Hb[e] for e in Hb}, args.lmin, args.lmax)
        pR = float(np.mean(np.abs(dR_mc - dR_mc.mean()) >= abs(dR - dR_mc.mean())))
        pH = float(np.mean(np.abs(dH_mc - dH_mc.mean()) >= abs(dH - dH_mc.mean())))
        print("\n=== MC null (phase randomization per ell) ===")
        print(f"ΔR: mc_mean={dR_mc.mean():+.3g} mc_std={dR_mc.std():.3g} p(two-sided)={pR:.6g}")
        print(f"Δ(-Entropy): mc_mean={dH_mc.mean():+.3g} mc_std={dH_mc.std():.3g} p(two-sided)={pH:.6g}")

if __name__=="__main__":
    main()

