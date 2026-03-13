#!/usr/bin/env python3
# run_strict_leptons.py
from strict_ubt import alpha_msbar
from strict_ubt.lepton import predict_triplet
import sys

def main():
    try:
        me, mm, mt = predict_triplet()
        print("Strict UBT lepton masses (pole):")
        print(f"  electron ≈ {me:.9f} MeV")
        print(f"  muon     ≈ {mm:.6f} MeV")
        print(f"  tau      ≈ {mt:.3f} MeV")
        return 0
    except Exception as e:
        print("Strict computation failed:", e)
        print("→ Ensure alpha_from_ubt_two_loop_strict(μ) is implemented in this repo.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
