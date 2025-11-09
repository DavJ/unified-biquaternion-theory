# alpha_core_repro/export_alpha_csv.py
"""
Exports two-loop strict alpha values to CSV for TeX inclusion.
Assumes alpha_core_repro.two_loop.alpha_from_ubt_two_loop_strict(mu: float) -> float exists.
"""
import csv, pathlib

try:
    from alpha_core_repro.two_loop import alpha_from_ubt_two_loop_strict
except Exception as e:
    raise SystemExit(f"Missing strict two-loop alpha provider: {e}")

OUT = pathlib.Path("data/alpha_two_loop_grid.csv")
OUT.parent.mkdir(parents=True, exist_ok=True)

# You can tailor the mu grid; keep at least a few canonical points
MU_GRID = [0.511, 1.0, 10.0, 91.1876]  # MeV/GeV per your convention

rows = []
for mu in MU_GRID:
    a = alpha_from_ubt_two_loop_strict(mu=mu)
    rows.append({"mu": mu, "alpha": a, "alpha_inv": 1.0 / a})

with OUT.open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["mu", "alpha", "alpha_inv"])
    w.writeheader()
    w.writerows(rows)

print(f"[export_alpha_csv] Wrote {OUT.resolve()} with {len(rows)} rows.")
