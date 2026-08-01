#!/usr/bin/env python3
"""Verify visible and machine-readable provenance in curated UBT PDFs."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REVIEW_REGISTRY = ROOT / "PROVENANCE_REVIEW.yaml"


def load_tool():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "ubt_provenance_tool", ROOT / "tools" / "apply_provenance_headers.py"
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot import provenance header tool")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run_text(command: list[str]) -> str:
    proc = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode:
        raise RuntimeError(f"Command failed ({proc.returncode}): {' '.join(command)}\n{proc.stdout}")
    return proc.stdout


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", type=Path, default=ROOT / ".github" / "latex_publish_map.tsv")
    parser.add_argument("--require-all", action="store_true", help="fail if a curated PDF is absent")
    args = parser.parse_args(argv)

    for executable in ("pdfinfo", "pdftotext"):
        if shutil.which(executable) is None:
            print(f"ERROR: required executable not found: {executable}", file=sys.stderr)
            return 2

    tool = load_tool()
    config = yaml.safe_load((ROOT / "PROVENANCE_TIERS.yaml").read_text(encoding="utf-8"))
    review_data = (
        yaml.safe_load(REVIEW_REGISTRY.read_text(encoding="utf-8"))
        if REVIEW_REGISTRY.exists()
        else {"profiles": {}}
    )
    review_profiles = review_data.get("profiles", {}) if isinstance(review_data, dict) else {}
    failures: list[str] = []
    checked = 0
    for raw in args.map.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        source_pdf, destination = raw.split("\t", 1)
        source_tex = source_pdf[:-4] + ".tex"
        pdf = ROOT / destination
        if not pdf.exists():
            if args.require_all:
                failures.append(f"missing curated PDF: {destination}")
            continue
        tier_key = tool.classify_path(source_tex, config)
        if tier_key not in tool.TIERS:
            failures.append(f"unmarkable source in publish map: {source_tex}")
            continue
        tier = tool.TIERS[tier_key].short
        info = run_text(["pdfinfo", str(pdf)])
        subject = next((line for line in info.splitlines() if line.startswith("Subject:")), "")
        keywords = next((line for line in info.splitlines() if line.startswith("Keywords:")), "")
        if "AI-assisted content" not in subject or f"tier {tier}" not in subject:
            failures.append(f"{destination}: missing tier-{tier} Subject metadata")
        if "AI provenance" not in keywords or f"tier {tier}" not in keywords:
            failures.append(f"{destination}: missing tier-{tier} Keywords metadata")
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "text.txt"
            run_text(["pdftotext", str(pdf), str(out)])
            text = out.read_text(encoding="utf-8", errors="replace")
        normalized_text = " ".join(text.split())
        if f"AI provenance — Tier {tier}" not in normalized_text and f"AI provenance - Tier {tier}" not in normalized_text:
            failures.append(f"{destination}: visible tier-{tier} notice not found")

        review_profile = review_profiles.get(source_tex)
        if isinstance(review_profile, dict):
            labels = review_profile.get("publication_labels", {})
            machine = str(labels.get("machine") or "")
            human = str(labels.get("human") or "")
            editorial = str(labels.get("editorial") or "")
            for label, value in (("machine verification", machine), ("human review", human), ("editorial approval", editorial)):
                if not value:
                    failures.append(f"{source_tex}: missing publication label for {label}")
                    continue
                if f"{label}: {value}" not in subject.lower():
                    failures.append(f"{destination}: missing {label} review metadata")
            if "Review profile." not in normalized_text:
                failures.append(f"{destination}: visible orthogonal review profile not found")
            for phrase in (
                f"Machine verification: {machine}",
                f"human review: {human}",
                f"editorial approval: {editorial}",
            ):
                if phrase not in normalized_text:
                    failures.append(f"{destination}: visible review phrase not found: {phrase}")
        checked += 1

    print(f"Checked {checked} curated PDF(s).")
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
