#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
tools/generate_wiki.py

Parse DERIVATION_INDEX.md and update generated sections in wiki/ pages.

Reads:
  DERIVATION_INDEX.md

Updates (between BEGIN/END GENERATED markers):
  wiki/Home.md            — status_summary
  wiki/Derivations.md     — derivation_summary
  wiki/Gauge_Structure.md — gauge_status
  wiki/GR_Recovery.md     — gr_recovery_status
  wiki/Alpha_Constant.md  — alpha_status
  wiki/SU3_Structure.md   — su3_status
  wiki/Hecke_Modular_Structure.md — hecke_status
  wiki/Mirror_Sector.md   — mirror_status

Also updates _Sidebar.md navigation if section titles change.

Usage:
    python tools/generate_wiki.py [--wiki-dir PATH]
"""

from __future__ import annotations

import argparse
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DERIVATION_INDEX = os.path.join(REPO_ROOT, "DERIVATION_INDEX.md")
WIKI_DIR = os.path.join(REPO_ROOT, "wiki")

REPO_URL = "https://github.com/DavJ/unified-biquaternion-theory"
BLOB_BASE = f"{REPO_URL}/blob/master"

# ---------------------------------------------------------------------------
# Status normalisation (shared with generate_theory_map.py)
# ---------------------------------------------------------------------------

_STATUS_MAP = [
    ("proven",                  ("Proved",          "✅")),
    ("derived",                 ("Proved",          "✅")),
    ("verified",                ("Proved",          "✅")),
    ("documented",              ("Proved",          "✅")),
    ("supported by numerical",  ("Supported",       "⚡")),
    ("strong numerical",        ("Supported",       "⚡")),
    ("numerical observation",   ("Supported",       "⚡")),
    ("supported",               ("Supported",       "⚡")),
    ("semi-empirical",          ("Semi-empirical",  "⚠️")),
    ("partially verified",      ("Semi-empirical",  "⚠️")),
    ("open hard problem",       ("Open",            "❌")),
    ("dead end",                ("Dead End",        "❌")),
    ("extended dead end",       ("Dead End",        "❌")),
    ("motivated conjecture",    ("Conj.",           "💭")),
    ("conjecture",              ("Conjecture",      "💭")),
    ("open",                    ("Open",            "❌")),
    ("to verify",               ("Open",            "❌")),
]


def _normalise_status(raw: str) -> tuple[str, str]:
    """Return (canonical_label, symbol) from raw status cell text."""
    s = raw.lower()
    s = re.sub(r"\*+", "", s)
    s = re.sub(r"\[.*?\]", "", s).strip()
    for key, val in _STATUS_MAP:
        if key in s:
            return val
    return ("Unknown", "❓")


# ---------------------------------------------------------------------------
# Parse DERIVATION_INDEX.md
# ---------------------------------------------------------------------------

def parse_derivation_index(filepath: str) -> dict[str, list[dict]]:
    """
    Parse DERIVATION_INDEX.md.

    Returns dict: section_title → list of entry dicts:
        { 'result', 'status_raw', 'file', 'notes',
          'label', 'symbol' }
    """
    sections: dict[str, list[dict]] = {}
    current_section: str | None = None

    with open(filepath, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")

            m = re.match(r"^## (.+)$", line)
            if m:
                current_section = m.group(1).strip()
                sections.setdefault(current_section, [])
                continue

            if current_section is None:
                continue

            # Skip table separator rows
            if re.match(r"^\|[-\s|:]+\|", line):
                continue
            # Skip header rows
            if re.match(r"^\|\s*(Result|Check|Claim)\b", line, re.IGNORECASE):
                continue

            if not line.startswith("|"):
                continue

            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 4:
                continue
            result = parts[1]
            status_raw = parts[2]
            file_col = parts[3] if len(parts) > 3 else ""
            notes = parts[4] if len(parts) > 4 else ""

            if not result or not status_raw:
                continue
            if result.lower() in ("result", "check", "claim") or result.startswith("---"):
                continue

            label, symbol = _normalise_status(status_raw)
            sections[current_section].append({
                "result":     result,
                "status_raw": status_raw,
                "file":       file_col,
                "notes":      notes,
                "label":      label,
                "symbol":     symbol,
            })

    return sections


# ---------------------------------------------------------------------------
# Generate content fragments for each wiki section
# ---------------------------------------------------------------------------

def _extract_primary_file(file_col: str) -> str:
    """
    Extract the first file path from a DERIVATION_INDEX file column cell.

    The cell may contain one or more backtick-quoted paths, possibly followed
    by section references (e.g. §1) and/or comma-separated additional files.
    Returns the first clean path, or empty string if none found.

    Examples:
      '`canonical/geometry/metric.tex`'          → 'canonical/geometry/metric.tex'
      '`ARCHIVE/foo.tex §2`, `bar.tex`'           → 'ARCHIVE/foo.tex'
      '`experiments/three_gen/file.tex §3` notes' → 'experiments/three_gen/file.tex'
    """
    if not file_col:
        return ""
    # Find the first backtick-quoted token
    m = re.search(r"`([^`]+)`", file_col)
    if not m:
        return ""
    raw = m.group(1).strip()
    # Strip section references: space + § or space + (
    raw = re.split(r"\s+[§(]", raw)[0].strip()
    # Strip trailing slash (directories)
    raw = raw.rstrip("/")
    return raw


def _file_link(file_col: str) -> str:
    """
    Return a Markdown hyperlink for the primary file in a DERIVATION_INDEX
    file column cell, or an empty string if no valid file is found.

    Only creates a link if the file actually exists in the repository.
    """
    if not file_col:
        return ""
    path = _extract_primary_file(file_col)
    if not path:
        return ""
    full = os.path.join(REPO_ROOT, path)
    if not os.path.exists(full):
        return ""
    # Use /blob/ for files and /tree/ for directories
    link_type = "tree" if os.path.isdir(full) else "blob"
    basename = os.path.basename(path) or os.path.basename(os.path.dirname(path))
    return f"[`{basename}`]({REPO_URL}/{link_type}/master/{path})"


def _status_table(entries: list[dict], max_rows: int = 20) -> str:
    """Render a compact Markdown status table from DERIVATION_INDEX entries."""
    if not entries:
        return "_No entries found in DERIVATION_INDEX.md for this section._"

    # Determine whether any entry has a valid file link before building the table,
    # so we add the File column only when it provides useful information.
    # Use a two-pass approach: first scan for any valid link, then render rows.
    visible = entries[:max_rows]
    has_links = any(_file_link(e["file"]) for e in visible)

    if has_links:
        rows = ["| Result | Status | File |", "|--------|--------|------|"]
    else:
        rows = ["| Result | Status |", "|--------|--------|"]

    for e in visible:
        result = re.sub(r"\[.*?\]", "", e["result"]).strip()
        result = result[:80] + "…" if len(result) > 80 else result
        label = e["label"]
        symbol = e["symbol"]
        if has_links:
            link = _file_link(e["file"])
            rows.append(f"| {result} | {symbol} **{label}** | {link} |")
        else:
            rows.append(f"| {result} | {symbol} **{label}** |")

    if len(entries) > max_rows:
        rows.append(
            f"| *… and {len(entries) - max_rows} more results* "
            f"| *See [DERIVATION_INDEX.md]({REPO_URL}/blob/master/DERIVATION_INDEX.md)* |"
            + (" |" if has_links else "")
        )

    return "\n".join(rows)


def _count_statuses(entries: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {
        "Proved": 0, "Supported": 0, "Semi-empirical": 0,
        "Conj.": 0, "Conjecture": 0, "Open": 0, "Dead End": 0, "Unknown": 0,
    }
    for e in entries:
        key = e["label"]
        counts[key] = counts.get(key, 0) + 1
    # Merge Conj. and Conjecture
    counts["Conjecture"] = counts.get("Conjecture", 0) + counts.pop("Conj.", 0)
    return counts


# ---------------------------------------------------------------------------
# Section-specific generators
# ---------------------------------------------------------------------------

_SECTION_SM     = "Standard Model Gauge Group"
_SECTION_ALPHA  = "Fine Structure Constant (α)"
_SECTION_GEN    = "Three Fermion Generations"
_SECTION_HECKE  = "Hecke Bridge (ℂ⊗ℍ ↔ Modular Forms)"
_SECTION_GR     = "GR Recovery Status (v48+, updated 2026-03-11)"
_SECTION_MIRROR = "Mirror Sector (Twin Prime Vacuum)"

# Sections that are explicitly about GR recovery in DERIVATION_INDEX
_GR_KEYWORDS = ["metric", "signature", "non-degeneracy", "einstein", "hilbert",
                "gr closure", "gr recovery", "levi-civita", "riemann", "closure"]


def _gr_entries(all_sections: dict) -> list[dict]:
    """Extract GR-relevant entries from the whole index."""
    out = []
    for section_entries in all_sections.values():
        for e in section_entries:
            r = e["result"].lower()
            if any(kw in r for kw in _GR_KEYWORDS):
                out.append(e)
    return out


def gen_status_summary(sections: dict) -> str:
    """Home page: overall counts table."""
    area_map = {
        "Standard Model Gauge Group":                  "Gauge Structure",
        "Fine Structure Constant (α)":                 "Fine Structure Constant",
        "Three Fermion Generations":                   "Three Generations",
        "φ-Universe Parameter and h_μν Vacuum":        "Gravity / φ-Universe",
        "GR Recovery Status (v48+, updated 2026-03-11)": "Gravity / φ-Universe",
        "Mirror Sector (Twin Prime Vacuum)":           "Mirror Sector",
        "Hecke Bridge (ℂ⊗ℍ ↔ Modular Forms)":         "Three Generations",
        "Cross-Gap Consistency Checks":                None,
        "Prime Attractor Theorem":                     "Algebra",
        "QM Emergence from Complex Time (Track: CORE)": None,
        "QED Reproducibility at φ = const (Track: CORE)": None,
        "Chirality Derivation — SU(2)_L Selection (Track: CORE)": "Gauge Structure",
        "8π Common Origin (Track: CORE)":              None,
        "FPE Equivalence — QM/GR/Stat-Mech Unification (Track: CORE)": None,
    }
    area_order = [
        "Gauge Structure", "Fine Structure Constant",
        "Three Generations", "Gravity / φ-Universe",
        "Mirror Sector", "Algebra",
    ]
    totals: dict[str, dict[str, int]] = {a: {} for a in area_order}

    for sec_title, entries in sections.items():
        area = area_map.get(sec_title)
        if area is None:
            continue
        c = _count_statuses(entries)
        for k, v in c.items():
            totals[area][k] = totals[area].get(k, 0) + v

    header = "| Area | ✅ Proved | ⚡ Supported | ⚠️ Semi-emp. | 💭 Conjecture | ❌ Open/Dead-end |"
    sep    = "|------|----------|------------|------------|-------------|----------------|"
    rows = [header, sep]
    grand = {}
    for area in area_order:
        c = totals[area]
        proved = c.get("Proved", 0)
        supp   = c.get("Supported", 0)
        semi   = c.get("Semi-empirical", 0)
        conj   = c.get("Conjecture", 0)
        open_  = c.get("Open", 0) + c.get("Dead End", 0)
        rows.append(
            f"| {area} | {proved} | {supp} | {semi} | {conj} | {open_} |"
        )
        for k, v in [("Proved", proved), ("Supported", supp),
                     ("Semi-empirical", semi), ("Conjecture", conj),
                     ("Open", open_)]:
            grand[k] = grand.get(k, 0) + v

    rows.append(
        f"| **Total** | **{grand.get('Proved',0)}** | **{grand.get('Supported',0)}**"
        f" | **{grand.get('Semi-empirical',0)}** | **{grand.get('Conjecture',0)}**"
        f" | **{grand.get('Open',0)}** |"
    )

    note = (
        "\n*Auto-generated from "
        f"[`DERIVATION_INDEX.md`]({REPO_URL}/blob/master/DERIVATION_INDEX.md). "
        "Dead Ends are counted in Open/Dead-end.*"
    )
    return "\n".join(rows) + note


def gen_derivation_summary(sections: dict) -> str:
    return gen_status_summary(sections)


def gen_gauge_status(sections: dict) -> str:
    entries = sections.get(_SECTION_SM, [])
    return _status_table(entries)


def gen_gr_recovery_status(sections: dict) -> str:
    entries = sections.get(_SECTION_GR, [])
    if not entries:
        entries = _gr_entries(sections)
    return _status_table(entries, max_rows=15)


def gen_alpha_status(sections: dict) -> str:
    entries = sections.get(_SECTION_ALPHA, [])
    return _status_table(entries)


def gen_su3_status(sections: dict) -> str:
    entries = [e for e in sections.get(_SECTION_SM, [])
               if "su(3)" in e["result"].lower() or "su3" in e["result"].lower()
               or "involution" in e["result"].lower()
               or "color" in e["result"].lower()
               or "confinement" in e["result"].lower()
               or "gell-mann" in e["result"].lower()
               or "qubit" in e["result"].lower()]
    if not entries:
        entries = sections.get(_SECTION_SM, [])
    return _status_table(entries)


def gen_hecke_status(sections: dict) -> str:
    entries = sections.get(_SECTION_HECKE, [])
    if not entries:
        entries = [e for e in sections.get(_SECTION_GEN, [])
                   if "hecke" in e["result"].lower()
                   or "cm" in e["result"].lower()
                   or "non-cm" in e["result"].lower()
                   or "twin" in e["result"].lower()
                   or "prime" in e["result"].lower()]
    return _status_table(entries)


def gen_mirror_status(sections: dict) -> str:
    entries = sections.get(_SECTION_MIRROR, [])
    if not entries:
        entries = [e for e in sections.get(_SECTION_GEN, [])
                   if "139" in e["result"] or "mirror" in e["result"].lower()]
    return _status_table(entries)


# ---------------------------------------------------------------------------
# Section registry
# ---------------------------------------------------------------------------

SECTION_GENERATORS = {
    "status_summary":    gen_status_summary,
    "derivation_summary": gen_derivation_summary,
    "gauge_status":      gen_gauge_status,
    "gr_recovery_status": gen_gr_recovery_status,
    "alpha_status":      gen_alpha_status,
    "su3_status":        gen_su3_status,
    "hecke_status":      gen_hecke_status,
    "mirror_status":     gen_mirror_status,
}

# ---------------------------------------------------------------------------
# Inject generated content into wiki files
# ---------------------------------------------------------------------------

_MARKER_RE = re.compile(
    r"<!-- BEGIN GENERATED: (\w+) -->.*?<!-- END GENERATED: \1 -->",
    re.DOTALL
)


def inject_section(content: str, section_id: str, new_body: str) -> str:
    """Replace the generated block for section_id with new_body."""
    replacement = (
        f"<!-- BEGIN GENERATED: {section_id} -->\n"
        f"{new_body}\n"
        f"<!-- END GENERATED: {section_id} -->"
    )

    def _replace(m: re.Match) -> str:
        if m.group(1) == section_id:
            return replacement
        return m.group(0)

    new_content, n = _MARKER_RE.subn(_replace, content)
    if n == 0:
        # Marker not found — append a warning (shouldn't happen if templates are correct)
        print(f"  ⚠️  No marker found for section '{section_id}'", file=sys.stderr)
    return new_content


def update_wiki_file(filepath: str, sections_data: dict, dry_run: bool = False) -> bool:
    """
    Update all generated sections in a wiki file.

    Returns True if file was modified.
    """
    if not os.path.exists(filepath):
        print(f"  ⚠️  File not found: {filepath}", file=sys.stderr)
        return False

    with open(filepath, encoding="utf-8") as fh:
        original = fh.read()

    content = original

    # Find all section IDs referenced in this file
    for section_id, generator in SECTION_GENERATORS.items():
        marker = f"<!-- BEGIN GENERATED: {section_id} -->"
        if marker not in content:
            continue

        new_body = generator(sections_data)
        content = inject_section(content, section_id, new_body)

    if content == original:
        return False

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(content)

    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate wiki content from DERIVATION_INDEX.md"
    )
    parser.add_argument(
        "--wiki-dir",
        default=WIKI_DIR,
        help=f"Path to wiki directory (default: {WIKI_DIR})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing files",
    )
    args = parser.parse_args(argv)

    wiki_dir: str = args.wiki_dir
    dry_run: bool = args.dry_run

    if not os.path.exists(DERIVATION_INDEX):
        print(f"ERROR: {DERIVATION_INDEX} not found", file=sys.stderr)
        return 1

    if not os.path.isdir(wiki_dir):
        print(f"ERROR: wiki directory not found: {wiki_dir}", file=sys.stderr)
        return 1

    print(f"Parsing {DERIVATION_INDEX} …")
    sections = parse_derivation_index(DERIVATION_INDEX)
    print(f"  Found {len(sections)} sections, "
          f"{sum(len(v) for v in sections.values())} entries total.")

    changed = 0
    for filename in sorted(os.listdir(wiki_dir)):
        if not filename.endswith(".md"):
            continue
        filepath = os.path.join(wiki_dir, filename)
        modified = update_wiki_file(filepath, sections, dry_run=dry_run)
        if modified:
            verb = "Would update" if dry_run else "Updated"
            print(f"  {verb}: {filename}")
            changed += 1
        else:
            print(f"  No changes: {filename}")

    print(f"\n{'Dry-run: ' if dry_run else ''}{'Updated' if not dry_run else 'Would update'} "
          f"{changed} wiki file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
