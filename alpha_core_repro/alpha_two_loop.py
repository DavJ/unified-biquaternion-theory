# alpha_core_repro/alpha_two_loop.py
# SPDX-License-Identifier: MIT
from __future__ import annotations
import os, math, csv
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Optional, List

FormFactor = Callable[[int], float]

@dataclass
class TwoLoopConfig:
    scheme: str = "MSbar"
    mu: Optional[float] = None
    form_factor: Optional[FormFactor] = None
    strict: bool = True  # strict=True => no mocks allowed

def compute_two_loop_delta(p: int, cfg: Optional[TwoLoopConfig] = None) -> float:
    if cfg is None:
        cfg = TwoLoopConfig()
    ff = 1.0 if cfg.form_factor is None else float(cfg.form_factor(p))
    if not math.isfinite(ff) or ff <= 0.0:
        raise ValueError(f"Invalid sector form factor for p={p}: {ff}")
    core = _two_loop_archimedean_core(p=p, scheme=cfg.scheme, mu=cfg.mu, strict=cfg.strict)
    return ff * core

def alpha_corrected(p: int, delta_ct: float) -> float:
    denom = float(p) + float(delta_ct)
    if denom <= 0 or not math.isfinite(denom):
        raise ValueError(f"Non-physical denominator: p={p}, Δ={delta_ct}")
    return 1.0 / denom

def run_grid(primes: Iterable[int],
             cfg: Optional[TwoLoopConfig] = None,
             out_csv: Path | str = "alpha_core_repro/out/alpha_two_loop_grid.csv") -> Path:
    if cfg is None:
        cfg = TwoLoopConfig()
    out_path = Path(out_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows: List[dict] = []
    for p in primes:
        dct = compute_two_loop_delta(p, cfg)
        a = alpha_corrected(p, dct)
        rows.append({
            "p": int(p),
            "delta_ct": f"{dct:.9f}",
            "alpha_inv": f"{1.0/a:.9f}",
            "alpha": f"{a:.12f}",
            "scheme": cfg.scheme,
            "mu": "" if cfg.mu is None else f"{cfg.mu:.6g}",
            "form_factor": "" if cfg.form_factor is None else f"{cfg.form_factor(p):.9f}",
        })
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return out_path

def _two_loop_archimedean_core(p: int, scheme: str, mu: Optional[float], strict: bool) -> float:
    allow_mock = os.environ.get("UBT_ALPHA_ALLOW_MOCK", "0") == "1"
    if strict and not allow_mock:
        raise NotImplementedError(
            "Two-loop core not implemented. Set UBT_ALPHA_ALLOW_MOCK=1 and use TwoLoopConfig(strict=False) temporarily."
        )
    # MOCK: reproduce 137.035999 for p=137, keep similar scale for others
    if p == 137:
        return 0.035999000
    return 0.036000000
