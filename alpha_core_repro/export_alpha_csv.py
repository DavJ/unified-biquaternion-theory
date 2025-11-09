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

# Physically meaningful mu scales with proper precision
# Using precise values from PDG and other standards
MU_GRID = [
    0.510998946,     # Electron pole mass (PDG 2024) in MeV
    1.776_86,        # Tau mass in GeV (if interpreting as GeV scale)
    10.0,            # Typical hadronic scale (GeV)
    91.1876,         # Z boson mass in GeV
]

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
