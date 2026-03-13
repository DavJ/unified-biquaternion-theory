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

# Physically meaningful mu scales
# NOTE: These scales are chosen based on physical significance, not fitted values
# The electron pole mass below is from PDG (experimental reference), but the
# alpha calculation at these scales is purely from UBT theory
MU_GRID = [
    1.0,             # Reference scale (1 MeV) - UBT baseline defined here
    100.0,           # Typical hadronic scale
    1000.0,          # GeV scale
    91187.6,         # Z boson mass in MeV (if interpreting as scale)
]

# Note: If you want to include the electron mass scale for comparison:
# from alpha_core_repro.two_loop_core import MU0
# The UBT baseline is defined at MU0 = 1.0 MeV by convention

rows = []
for mu in MU_GRID:
    a = alpha_from_ubt_two_loop_strict(mu=mu)
    # Use high precision formatting to preserve all significant digits
    rows.append({
        "mu": f"{mu:.15g}",           # 15 significant figures
        "alpha": f"{a:.18e}",          # 18 decimals in scientific notation
        "alpha_inv": f"{1.0 / a:.15f}" # 15 decimal places
    })

with OUT.open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["mu", "alpha", "alpha_inv"])
    w.writeheader()
    w.writerows(rows)

print(f"[export_alpha_csv] Wrote {OUT.resolve()} with {len(rows)} rows.")
print(f"  Precision: mu (15 sig figs), alpha (18 decimals), alpha_inv (15 decimals)")
