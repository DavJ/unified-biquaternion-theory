#!/usr/bin/env python3
import csv, sys
from pathlib import Path

def main():
    path = Path("validation/electron_mass_vs_sector.csv")
    if not path.exists():
        print("File missing:", path)
        sys.exit(1)
    rows = list(csv.DictReader(path.open()))
    assert rows, "empty CSV"
    required = ['p','alpha0','mu_star_MeV','m0_MeV','me_MeV','alpha_at_me']
    for i, row in enumerate(rows, 1):
        for k in required:
            assert k in row and row[k] != '', f"row {i}: missing {k}"
            float(row[k])  # also validates numeric
    print("OK: electron_mass_vs_sector.csv looks sane")

if __name__ == "__main__":
    main()

