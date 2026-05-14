#!/usr/bin/env python3
"""
install_two_loop_core.py
Copies alpha_core_repro/two_loop_core.py into your repo (idempotent).
Usage:
  python tools/install_two_loop_core.py --apply
"""
from __future__ import annotations
import argparse, shutil
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    src = Path(__file__).resolve().parents[1] / "alpha_core_repro" / "two_loop_core.py"
    dst = Path("alpha_core_repro") / "two_loop_core.py"
    if not args.apply:
        print(f"[plan] would install {dst} (from {src})")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"[write] {dst}")

if __name__ == "__main__":
    main()
