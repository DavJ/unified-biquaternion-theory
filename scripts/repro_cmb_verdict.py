#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
CMB verdict reproduction script.

Reproduces the CMB (Cosmic Microwave Background) analysis pipeline
used to derive the UBT verdict against observational data.

Usage:
    python scripts/repro_cmb_verdict.py [--mode MODE] [--dry-run] [OPTIONS]

Modes:
    theory       (default) Run pipeline using UBT theoretical predictions as model
    obs-as-model Use one CMB dataset as model and compare to the other

This script orchestrates the full pipeline:
  STEP 1: Download CMB datasets (Planck 2018, WMAP 9-yr)
  STEP 2: Sanity check downloaded data
  STEP 3: Generate SHA-256 manifests
  STEP 4: Validate manifests
  STEP 5: Run CMB comb pipeline
  STEP 6: Locate latest run and print verdict
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def find_repo_root() -> Path:
    """Find repository root by looking for pytest.ini or .git."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / "pytest.ini").exists() or (current / ".git").exists():
            return current
        current = current.parent
    return Path(__file__).resolve().parent.parent


REPO_ROOT = find_repo_root()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="repro_cmb_verdict.py",
        description="CMB verdict reproduction script for UBT analysis pipeline.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--mode",
        choices=["theory", "obs-as-model"],
        default="theory",
        help="Pipeline mode: 'theory' uses UBT predictions as model; "
             "'obs-as-model' uses one CMB dataset as model.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without executing any steps.",
    )
    parser.add_argument(
        "--no-download",
        action="store_true",
        help="Skip the dataset download step (use already-downloaded data).",
    )
    parser.add_argument(
        "--planck-obs",
        default=None,
        metavar="PATH",
        help="Path to Planck observational data file (overrides default).",
    )
    parser.add_argument(
        "--wmap-obs",
        default=None,
        metavar="PATH",
        help="Path to WMAP observational data file (overrides default).",
    )
    parser.add_argument(
        "--ell-min-planck",
        type=int,
        default=2,
        metavar="N",
        help="Minimum multipole ell for Planck spectrum (default: 2).",
    )
    parser.add_argument(
        "--ell-max-planck",
        type=int,
        default=2500,
        metavar="N",
        help="Maximum multipole ell for Planck spectrum (default: 2500).",
    )
    parser.add_argument(
        "--variant",
        default="default",
        metavar="VARIANT",
        help="Pipeline variant label (e.g. 'A', 'B', 'default').",
    )
    parser.add_argument(
        "--mc-samples",
        type=int,
        default=1000,
        metavar="N",
        help="Number of Monte Carlo samples for uncertainty estimation (default: 1000).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        metavar="N",
        help="Random seed for reproducibility (default: 42).",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        metavar="DIR",
        help="Output directory for results (default: <repo_root>/test_output/).",
    )
    return parser


def print_dry_run_header(args: argparse.Namespace) -> None:
    """Print DRY RUN header and configuration summary."""
    print("=" * 70)
    print("CMB VERDICT REPRODUCTION PIPELINE — DRY RUN")
    print("=" * 70)
    print()
    print(f"Repository root: {REPO_ROOT}")
    print(f"Mode: {args.mode}")
    print()
    print("Configuration:")
    print(f"  --mode            {args.mode}")
    print(f"  --dry-run         True")

    if args.planck_obs:
        print(f"  --planck-obs      {args.planck_obs}")
    if args.wmap_obs:
        print(f"  --wmap-obs        {args.wmap_obs}")
    if args.ell_min_planck != 2:
        print(f"  --ell_min_planck {args.ell_min_planck}")
    if args.ell_max_planck != 2500:
        print(f"  --ell_max_planck {args.ell_max_planck}")
    if args.variant != "default":
        print(f"  --variant {args.variant}")
    if args.mc_samples != 1000:
        print(f"  --mc_samples {args.mc_samples}")
    if args.seed != 42:
        print(f"  --seed {args.seed}")
    print()


def print_step(n: int, title: str, detail: str = "") -> None:
    print(f"[DRY RUN] STEP {n}: {title}")
    if detail:
        print(f"          {detail}")


def run_dry_run(args: argparse.Namespace) -> int:
    """Print all pipeline steps without executing them."""
    print_dry_run_header(args)

    if args.no_download:
        print("Skipping download step (--no-download specified).")
        print()

    planck_path = args.planck_obs or str(REPO_ROOT / "data" / "planck_pr3" / "COM_PowerSpect_CMB-TT-full_R3.01.txt")
    wmap_path = args.wmap_obs or str(REPO_ROOT / "data" / "wmap_9yr" / "wmap_tt_spectrum_9yr_v5.txt")

    if not args.no_download:
        print_step(1, "Download CMB datasets",
                   f"Planck 2018 PR3 + WMAP 9-yr from official sources.")
    else:
        print_step(1, "Download CMB datasets", "SKIPPED (--no-download)")

    print_step(2, "Sanity check",
               f"Validate file formats and header metadata.")

    print_step(3, "Generate SHA-256 manifests",
               f"Hash Planck: {planck_path}\n"
               f"          Hash WMAP:   {wmap_path}")

    print_step(4, "Validate manifests",
               "Compare computed hashes against stored provenance manifest.")

    pipeline_cmd = (
        f"python scripts/cmb_comb.py "
        f"--planck {planck_path} "
        f"--wmap {wmap_path} "
        f"--mode {args.mode} "
        f"--ell_min_planck {args.ell_min_planck} "
        f"--ell_max_planck {args.ell_max_planck} "
        f"--variant {args.variant} "
        f"--mc_samples {args.mc_samples} "
        f"--seed {args.seed}"
    )
    print_step(5, "Run CMB comb pipeline", pipeline_cmd)

    output_dir = args.output_dir or str(REPO_ROOT / "test_output")
    print_step(6, "Locate latest run",
               f"Check {output_dir} for verdict JSON and report.")

    if args.mode == "obs-as-model":
        print()
        print(f"obs-as-model mode: Using Planck spectrum as reference model,")
        print(f"  comparing WMAP against it to establish observational baseline.")

    print()
    print("DRY RUN complete — no files written, no downloads attempted.")
    return 0


def run_pipeline(args: argparse.Namespace) -> int:
    """Execute the full CMB verdict reproduction pipeline."""
    print(f"Repository root: {REPO_ROOT}")
    print(f"Mode: {args.mode}")
    print()

    # Check dependencies
    try:
        import numpy  # noqa: F401
    except ImportError:
        print("ERROR: numpy is required. Install with: pip install numpy", file=sys.stderr)
        return 1

    print("Full pipeline execution not yet implemented in this scaffold.")
    print("Use --dry-run to see what steps would be executed.")
    return 1


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.dry_run:
        rc = run_dry_run(args)
    else:
        rc = run_pipeline(args)

    sys.exit(rc)


if __name__ == "__main__":
    main()
