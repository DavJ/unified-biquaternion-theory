#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
tools/generate_theory_map.py

Parse DERIVATION_INDEX.md and generate:
  - docs/THEORY_STATUS.md       : Mermaid diagram of theory proof status
  - docs/THEORY_STATUS_SUMMARY.md : Plain-text summary table for README

Usage:
    python tools/generate_theory_map.py
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DERIVATION_INDEX = os.path.join(REPO_ROOT, "DERIVATION_INDEX.md")
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
THEORY_STATUS_MD = os.path.join(DOCS_DIR, "THEORY_STATUS.md")
THEORY_STATUS_SUMMARY_MD = os.path.join(DOCS_DIR, "THEORY_STATUS_SUMMARY.md")

# ---------------------------------------------------------------------------
# Status normalisation
# ---------------------------------------------------------------------------

# Maps lowercase keyword fragments → (canonical label, symbol, Mermaid class)
_STATUS_MAP = [
    ("proven",                ("Proved",        "✅", "proved")),
    ("derived",               ("Proved",        "✅", "proved")),
    ("verified",              ("Proved",        "✅", "proved")),
    ("documented",            ("Proved",        "✅", "proved")),
    ("supported by numerical",("Supported",     "⚡", "supported")),
    ("supported",             ("Supported",     "⚡", "supported")),
    ("semi-empirical",        ("Semi-empirical","⚠️", "semiempirical")),
    ("partially verified",    ("Semi-empirical","⚠️", "semiempirical")),
    ("open hard problem",     ("Open",          "❌", "openhard")),
    ("dead end",              ("Dead End",      "❌", "openhard")),
    ("extended dead end",     ("Dead End",      "❌", "openhard")),
    ("conjecture",            ("Conjecture",    "💭", "conjecture")),
    ("open",                  ("Open",          "❌", "openhard")),
    ("to verify",             ("Open",          "❌", "openhard")),
]

_SYMBOL_TO_STYLE = {
    "✅": "proved",
    "⚡": "supported",
    "⚠️": "semiempirical",
    "❌": "openhard",
    "💭": "conjecture",
}


def _normalise_status(raw: str):
    """Return (canonical, symbol, style) from a raw status cell."""
    s = raw.lower()
    s = re.sub(r"\*+", "", s)
    s = re.sub(r"\[.*?\]", "", s).strip()
    for key, val in _STATUS_MAP:
        if key in s:
            return val
    return ("Unknown", "❓", "unknown")


# ---------------------------------------------------------------------------
# Parsing DERIVATION_INDEX.md
# ---------------------------------------------------------------------------

def parse_derivation_index(filepath: str) -> dict:
    """
    Parse DERIVATION_INDEX.md.

    Returns dict mapping section_title → list of entry dicts:
        { 'result': str, 'status_raw': str,
          'canonical': str, 'symbol': str, 'style': str }
    """
    sections: dict = {}
    current_section: str | None = None
    header_seen = False

    with open(filepath, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")

            # ## Section headings
            m = re.match(r"^## (.+)$", line)
            if m:
                current_section = m.group(1).strip()
                sections.setdefault(current_section, [])
                header_seen = False
                continue

            if current_section is None:
                continue

            # Skip table header row and separator
            if re.match(r"^\|[-\s|:]+\|", line):
                continue
            if re.match(r"^\|\s*(Result|Check|Claim|Column)\b", line, re.IGNORECASE):
                header_seen = True
                continue

            # Table data rows only
            if not line.startswith("|"):
                continue

            parts = [p.strip() for p in line.split("|")]
            # Expect at least |result|status| (parts[0] is empty before first |)
            if len(parts) < 4:
                continue
            result = parts[1]
            status_raw = parts[2]
            if not result or not status_raw:
                continue
            if result.startswith("---") or result.lower() in ("result", "check", "claim"):
                continue

            canonical, symbol, style = _normalise_status(status_raw)
            sections[current_section].append(
                {
                    "result": result,
                    "status_raw": status_raw,
                    "canonical": canonical,
                    "symbol": symbol,
                    "style": style,
                }
            )

    return sections


# ---------------------------------------------------------------------------
# Node status lookup helpers
# ---------------------------------------------------------------------------

def _lookup(sections: dict, section: str, keywords: list[str]):
    """Return first matching entry using keyword priority order (earlier keywords win)."""
    for kw in keywords:
        for entry in sections.get(section, []):
            if kw.lower() in entry["result"].lower():
                return entry
    return None


def _node(sections: dict, section: str, keywords: list[str], default_sym: str):
    """Return (symbol, style) for a diagram node."""
    entry = _lookup(sections, section, keywords)
    if entry:
        return entry["symbol"], entry["style"]
    return default_sym, _SYMBOL_TO_STYLE.get(default_sym, "unknown")


# ---------------------------------------------------------------------------
# Diagram generation
# ---------------------------------------------------------------------------

_SM = "Standard Model Gauge Group"
_ALPHA = "Fine Structure Constant (α)"
_GEN = "Three Fermion Generations"
_PHI = "φ-Universe Parameter and h_μν Vacuum"


def _build_node_data(sections: dict) -> dict:
    """Return dict of node_id → (label_text, symbol, style) for all leaf nodes."""
    n = {}

    def add(node_id, label, section, keywords, default_sym):
        sym, sty = _node(sections, section, keywords, default_sym)
        n[node_id] = (label, sym, sty)

    # Algebra
    add("B", "SU(2)_L",       _SM,    ["SU(2)_L from left", "SU(2)_L"],          "✅")
    add("C", "U(1)_Y",        _SM,    ["U(1)_Y from right", "U(1)_Y"],            "✅")
    add("D", "U(1)_EM",       _SM,    ["U(1)_EM", "U(1)_em"],                     "✅")
    add("E", "SU(3)_c",       _SM,    ["SU(3)"],                                  "⚠️")
    add("F", "Associativity", _SM,    ["B = ℂ⊗", "Mat(2,ℂ)", "Aut(B)"],          "✅")

    # Gravity — fall back to φ-Universe section; hard-code GR conservation law
    add("H", "G_μν vakuum",    _PHI, ["φ-projection", "satisfies GR"],           "✅")
    add("I", "G_μν + hmota",   _PHI, ["h_μν ≠ 0", "two-mode winding"],           "✅")
    n["J"] = ("∇^μ T_μν = 0", "✅", "proved")   # hard-coded: GR conservation law

    # Three Generations
    add("L", "ψ-módy nezávislé", _GEN, ["ψ-modes as independent", "independent B-fields"], "✅")
    add("M", "T-invariance",     _GEN, ["ψ-parity forbids", "T-invariance"],                "✅")
    add("N", "Hecke konjektura", _GEN, ["Hecke eigenvalue conjecture", "Hecke"],             "⚡")
    # "hmotnostní poměry" → mass ratios supported via Hecke numerical evidence
    add("O", "hmotnostní poměry", _GEN, ["Hecke eigenvalue", "ψ-instanton", "mass ratio"], "⚡")

    # Constants
    add("Q", "α⁻¹ = 137 bare", _ALPHA, ["α⁻¹ = 137 (bare", "bare value"],         "⚠️")
    add("R", "N_eff = 12",      _ALPHA, ["N_eff = 12"],                              "✅")
    add("S", "B₀ = 8π",        _ALPHA, ["B₀ = 25.1", "one-loop baseline"],          "✅")
    add("T", "B_phenom",        _ALPHA, ["B_base", "N_eff^{3/2}", "B_phenom"],       "❌")

    # Cosmology — not yet in DERIVATION_INDEX; hard-coded as conjectures
    n["V"] = ("CMB predikce", "💭", "conjecture")
    n["W"] = ("ΔN_eff",       "💭", "conjecture")

    return n


def generate_mermaid(sections: dict) -> str:
    """Return a Mermaid graph string."""
    nd = _build_node_data(sections)

    def leaf(node_id):
        label, sym, _sty = nd[node_id]
        return f'["{sym} {label}"]'

    lines = [
        "```mermaid",
        "graph TD",
        "",
        "    %% Algebra",
        '    A["ℂ⊗ℍ Algebra"]',
        f"    A --> B{leaf('B')}",
        f"    A --> C{leaf('C')}",
        f"    A --> D{leaf('D')}",
        f"    A --> E{leaf('E')}",
        f"    A --> F{leaf('F')}",
        "",
        "    %% Gravity",
        '    G["Gravitace"]',
        f"    G --> H{leaf('H')}",
        f"    G --> I{leaf('I')}",
        f"    G --> J{leaf('J')}",
        "",
        "    %% Three Generations",
        '    K["Tři generace"]',
        f"    K --> L{leaf('L')}",
        f"    K --> M{leaf('M')}",
        f"    K --> N{leaf('N')}",
        f"    K --> O{leaf('O')}",
        "",
        "    %% Constants",
        '    P["Konstanty"]',
        f"    P --> Q{leaf('Q')}",
        f"    P --> R{leaf('R')}",
        f"    P --> S{leaf('S')}",
        f"    P --> T{leaf('T')}",
        "",
        "    %% Cosmology",
        '    U["Kosmologie"]',
        f"    U --> V{leaf('V')}",
        f"    U --> W{leaf('W')}",
        "",
        "    %% Style classes",
        "    classDef proved       fill:#90EE90,stroke:#228B22,color:#000",
        "    classDef supported    fill:#FFD700,stroke:#DAA520,color:#000",
        "    classDef semiempirical fill:#FFA500,stroke:#FF8C00,color:#000",
        "    classDef openhard     fill:#FF6B6B,stroke:#DC143C,color:#000",
        "    classDef conjecture   fill:#C0C0C0,stroke:#808080,color:#000",
        "    classDef unknown      fill:#EEEEEE,stroke:#AAAAAA,color:#000",
        "",
    ]

    # Apply classes to leaf nodes
    for node_id, (_label, _sym, sty) in nd.items():
        lines.append(f"    class {node_id} {sty}")

    lines.append("```")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------

# Mapping from DERIVATION_INDEX section title → diagram area name
_SECTION_TO_AREA = {
    "Standard Model Gauge Group":         "Algebra",
    "Prime Attractor Theorem":            "Algebra",
    "φ-Universe Parameter and h_μν Vacuum": "Gravity",
    "Three Fermion Generations":          "Generations",
    "Fine Structure Constant (α)":        "Constants",
    "Cross-Gap Consistency Checks":       None,   # skip
}

_AREA_ORDER = ["Algebra", "Gravity", "Generations", "Constants", "Cosmology"]


def generate_summary_table(sections: dict) -> str:
    """Return a Markdown summary table string."""
    counts = {area: {"Proved": 0, "Supported": 0, "Semi-empirical": 0, "Open": 0}
              for area in _AREA_ORDER}

    for section_title, entries in sections.items():
        area = _SECTION_TO_AREA.get(section_title)
        if area is None:
            continue
        for entry in entries:
            canonical = entry["canonical"]
            if canonical == "Proved":
                counts[area]["Proved"] += 1
            elif canonical == "Supported":
                counts[area]["Supported"] += 1
            elif canonical == "Semi-empirical":
                counts[area]["Semi-empirical"] += 1
            elif canonical in ("Open", "Conjecture"):
                counts[area]["Open"] += 1
            # Dead End intentionally excluded from public totals

    # Cosmology is not tracked in DERIVATION_INDEX yet — hard-code 2 conjectures
    counts["Cosmology"]["Open"] = 2

    header = "| Area | Proved | Supported | Semi-empirical | Open |"
    sep    = "|------|--------|-----------|----------------|------|"
    rows   = [header, sep]
    total  = {"Proved": 0, "Supported": 0, "Semi-empirical": 0, "Open": 0}

    for area in _AREA_ORDER:
        c = counts[area]
        for k in total:
            total[k] += c[k]
        rows.append(
            f"| {area} | {c['Proved']} | {c['Supported']} | {c['Semi-empirical']} | {c['Open']} |"
        )

    rows.append(
        f"| **Total** | **{total['Proved']}** | **{total['Supported']}**"
        f" | **{total['Semi-empirical']}** | **{total['Open']}** |"
    )
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# File writers
# ---------------------------------------------------------------------------

def write_theory_status(sections: dict):
    mermaid = generate_mermaid(sections)
    summary = generate_summary_table(sections)

    content = (
        "<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->\n"
        "<!-- Auto-generated by tools/generate_theory_map.py — do not edit manually -->\n\n"
        "# UBT Theory Status Map\n\n"
        "*Auto-generated from [`DERIVATION_INDEX.md`](../DERIVATION_INDEX.md). "
        "Do not edit manually — run `python tools/generate_theory_map.py` to regenerate.*\n\n"
        "## Status Legend\n\n"
        "| Symbol | Meaning |\n"
        "|--------|---------------------------|\n"
        "| ✅ | **Proved** — rigorous derivation, no free parameters |\n"
        "| ⚡ | **Supported** — numerical / structural evidence |\n"
        "| ⚠️ | **Semi-empirical** — structural derivation with ≥1 free parameter |\n"
        "| ❌ | **Open Hard Problem** — no known derivation |\n"
        "| 💭 | **Conjecture** — proposed, derivation pending |\n\n"
        "## Theory Map\n\n"
        + mermaid
        + "\n\n"
        "## Summary\n\n"
        + summary
        + "\n\n"
        "---\n\n"
        "*See also: [`THEORY_STATUS_SUMMARY.md`](THEORY_STATUS_SUMMARY.md) "
        "for the plain-text table.*\n"
    )

    with open(THEORY_STATUS_MD, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"✓ Written: {THEORY_STATUS_MD}")


def write_summary(sections: dict):
    summary = generate_summary_table(sections)

    content = (
        "<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->\n"
        "<!-- Auto-generated by tools/generate_theory_map.py — do not edit manually -->\n\n"
        "# UBT Theory Status Summary\n\n"
        "*Auto-generated from [`DERIVATION_INDEX.md`](../DERIVATION_INDEX.md). "
        "Run `python tools/generate_theory_map.py` to regenerate.*\n\n"
        + summary
        + "\n\n"
        "---\n\n"
        "**Legend**:\n"
        "- **Proved** — rigorous derivation; zero free parameters\n"
        "- **Supported** — numerical or structural evidence\n"
        "- **Semi-empirical** — derivation with ≥1 unexplained parameter\n"
        "- **Open** — no known approach reproduces the result; or conjecture\n"
        "- Dead Ends (documented failed approaches) are excluded from totals.\n\n"
        "Full map: [`THEORY_STATUS.md`](THEORY_STATUS.md)\n"
    )

    with open(THEORY_STATUS_SUMMARY_MD, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"✓ Written: {THEORY_STATUS_SUMMARY_MD}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not os.path.exists(DERIVATION_INDEX):
        print(f"ERROR: {DERIVATION_INDEX} not found", file=sys.stderr)
        sys.exit(1)

    os.makedirs(DOCS_DIR, exist_ok=True)

    sections = parse_derivation_index(DERIVATION_INDEX)

    write_theory_status(sections)
    write_summary(sections)

    print("Theory map generated.")


if __name__ == "__main__":
    main()
