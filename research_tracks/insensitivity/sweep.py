# insensitivity/sweep.py
from __future__ import annotations
import csv, math
from pathlib import Path
from .observables import AlphaBundle, rydberg_scale, thomson_sigma_proxy, gamow_barrier_proxy

def run_sweep(alpha0_inv=137.035999, deltas=(-0.02, -0.0144, 0.0, 0.02), out_csv="insensitivity/out/alpha_insensitivity.csv"):
    a0 = 1.0/alpha0_inv
    Path("insensitivity/out").mkdir(parents=True, exist_ok=True)
    rows = []
    for d in deltas:
        a = a0 * (1.0 + d)
        # UBT co-scaling: example — keep α^2*m_e constant => m_e ∝ 1/α^2
        m_e = 1.0 / (a*a)
        bundle = AlphaBundle(alpha=a, m_e=m_e)
        rows.append({
            "delta_alpha_frac": f"{d:.6f}",
            "alpha": f"{a:.12f}",
            "m_e_scaled": f"{m_e:.12f}",
            "rydberg_rel": f"{rydberg_scale(bundle):.9f}",
            "sigmaT_rel": f"{thomson_sigma_proxy(bundle):.9f}",
            "gamow_rel": f"{gamow_barrier_proxy(bundle):.9f}",
        })
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return out_csv

if __name__ == "__main__":
    path = run_sweep()
    print(f"Wrote {path}")
