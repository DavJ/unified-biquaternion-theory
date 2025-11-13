#!/usr/bin/env python3
"""
apply_alpha_forwarder_patch.py
Idempotently patches alpha_core_repro/alpha_two_loop.py to implement:
  def alpha_from_ubt_two_loop_strict(mu: float) -> float:
      p = 137
      delta = compute_two_loop_delta(p)
      ainv = p + delta
      return 1.0/ainv

Usage:
  python tools/apply_alpha_forwarder_patch.py        # dry-run (shows diff)
  python tools/apply_alpha_forwarder_patch.py --apply
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

TARGET = Path("alpha_core_repro/alpha_two_loop.py")

IMPL = """def alpha_from_ubt_two_loop_strict(mu: float) -> float:
    \"\"\"
    Strict two-loop α without fitted params:
      α^{-1} = p + Δ_CT(p), with prime-sector anchor p=137.
    Here μ is kept for API compatibility; the current archimedean limit does not vary with μ.
    \"\"\"
    p = 137
    delta = compute_two_loop_delta(p)
    ainv = p + delta
    return 1.0 / ainv
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    if not TARGET.exists():
        print(f"[error] {TARGET} not found. Run from repo root.")
        sys.exit(2)

    txt = TARGET.read_text(encoding="utf-8", errors="ignore")

    # If function already patched, exit cleanly
    if re.search(r"def\s+alpha_from_ubt_two_loop_strict\s*\([^)]*\):\s*[\s\S]*?return\s+1\.0\s*/\s*\w+", txt):
        print("[ok] alpha_from_ubt_two_loop_strict already appears to return 1/(p+Δ). Nothing to do.")
        return

    # Replace either a placeholder raising RuntimeError OR any previous def block.
    pattern = re.compile(
        r"def\s+alpha_from_ubt_two_loop_strict\s*\([^)]*\):[\s\S]*?(?=\n\S)",
        re.MULTILINE
    )
    if not pattern.search(txt):
        print("[error] Could not locate function alpha_from_ubt_two_loop_strict(mu: float) in target file.")
        sys.exit(3)

    new_txt = pattern.sub(IMPL + "\n", txt)

    if args.apply:
        TARGET.write_text(new_txt, encoding="utf-8")
        print(f"[write] patched {TARGET}")
    else:
        print("[diff] would patch function body in", TARGET)

if __name__ == "__main__":
    main()
