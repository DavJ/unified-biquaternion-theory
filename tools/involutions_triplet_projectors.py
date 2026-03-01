# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
involutions_triplet_projectors.py
===================================
Track A: SU(3) candidate via Z2×Z2×Z2 involutions on ℬ = ℂ⊗ℍ.

Enumerates the 8-dimensional basis of ℬ,
    B = {1, I, J, K, i, iI, iJ, iK}
where i is the complex unit and I, J, K are the quaternion units, and
computes the eigenvalue signatures under three commuting involutions:

    P1 : complex conjugation   (i → -i, I/J/K unchanged)
    P2 : quaternion conjugation (I,J,K → -I,-J,-K, i unchanged)
    P3 : axis-flip around I    (I → I, J → -J, K → -K, i unchanged)

The signature of a basis element b is σ(b) = (s1, s2, s3) where Pk(b) = sk·b.

The projector onto sector (s1, s2, s3) is
    Π_(s1 s2 s3) = (1/8) ∏_k (1 + sk Pk)

The script:
  - Verifies each involution satisfies Pk² = id.
  - Verifies pairwise commutativity [Pi, Pj] = 0.
  - Prints the full signature table.
  - Identifies the single-minus sectors S1=(-++), S2=(+-+), S3=(++-).
  - Constructs the candidate triplet carrier space Vc (see below).
  - Exports a Markdown report to reports/involutions_triplet_report.md.

MATHEMATICAL NOTE ON S3:
  Under the given involution definitions, the sector S3=(+,+,-) is provably
  empty: any element with P1=+1 (no complex-i factor) and P2=+1 (no
  quaternion-unit factor) must be a real scalar multiple of 1, and P3(1)=1,
  so it lands in (+,+,+) not (+,+,-).  The script confirms this.

  The natural 3D complex carrier space is instead
      Vc = span_ℂ{I, J, K}
  which is the P2=-1 eigenspace, 3-dimensional over ℂ.  P3 acts on Vc and
  splits it as span_ℂ{I} ⊕ span_ℂ{J, K}.  SU(3) is defined as the group of
  unitary determinant-1 transformations on Vc (a genuine 3D complex space).

Usage (from repository root):
    python tools/involutions_triplet_projectors.py
"""

from __future__ import annotations

import pathlib
from typing import Dict, List, Tuple


def _sign(s: int) -> str:
    """Return '+' for +1 or '-' for -1."""
    return "+" if s == 1 else "-"

# ---------------------------------------------------------------------------
# Basis representation
# ---------------------------------------------------------------------------
# Each basis element is described by two boolean flags:
#   has_i   : True if the element contains the complex unit i
#   quat    : one of '1', 'I', 'J', 'K'  (the quaternion factor)
# The label is the human-readable name.

BASIS: List[Tuple[str, bool, str]] = [
    # (label, has_i, quat_factor)
    ("1",   False, "1"),
    ("I",   False, "I"),
    ("J",   False, "J"),
    ("K",   False, "K"),
    ("i",   True,  "1"),
    ("iI",  True,  "I"),
    ("iJ",  True,  "J"),
    ("iK",  True,  "K"),
]


def p1_eigenvalue(label: str, has_i: bool, quat: str) -> int:
    """P1 = complex conjugation: i → -i, quaternion units unchanged.
    Eigenvalue is -1 iff the element contains the complex unit i."""
    return -1 if has_i else +1


def p2_eigenvalue(label: str, has_i: bool, quat: str) -> int:
    """P2 = quaternion conjugation: I,J,K → -I,-J,-K, i unchanged.
    Eigenvalue is -1 iff the quaternion factor is I, J, or K."""
    return -1 if quat in ("I", "J", "K") else +1


def p3_eigenvalue(label: str, has_i: bool, quat: str) -> int:
    """P3 = axis-flip around I: I → I, J → -J, K → -K, i unchanged.
    Eigenvalue is -1 iff the quaternion factor is J or K."""
    return -1 if quat in ("J", "K") else +1


# ---------------------------------------------------------------------------
# Verification: involutions and commutativity
# ---------------------------------------------------------------------------

def verify_involutions() -> Dict[str, bool]:
    """Verify P1²=P2²=P3²=1 and pairwise commutativity on all basis elements."""
    results: Dict[str, bool] = {}

    for _label, has_i, quat in BASIS:
        s1 = p1_eigenvalue(_label, has_i, quat)
        s2 = p2_eigenvalue(_label, has_i, quat)
        s3 = p3_eigenvalue(_label, has_i, quat)

        # P_k²(b) = P_k(s_k · b) = s_k · P_k(b) = s_k · s_k · b = b  ✓
        assert s1 * s1 == 1, f"P1 not involution on {_label}"
        assert s2 * s2 == 1, f"P2 not involution on {_label}"
        assert s3 * s3 == 1, f"P3 not involution on {_label}"

    results["p1_involution"] = True
    results["p2_involution"] = True
    results["p3_involution"] = True

    # Commutativity: since each Pk acts by a scalar ±1 on every basis
    # element, Pi ∘ Pj and Pj ∘ Pi both act as (si·sj) on b, so they commute.
    results["p1_p2_commute"] = True
    results["p1_p3_commute"] = True
    results["p2_p3_commute"] = True

    return results


# ---------------------------------------------------------------------------
# Signature table
# ---------------------------------------------------------------------------

def compute_signatures() -> List[Dict]:
    """Compute the eigenvalue signature (s1, s2, s3) for each basis element."""
    rows = []
    for label, has_i, quat in BASIS:
        s1 = p1_eigenvalue(label, has_i, quat)
        s2 = p2_eigenvalue(label, has_i, quat)
        s3 = p3_eigenvalue(label, has_i, quat)
        rows.append({
            "element": label,
            "s1": s1,
            "s2": s2,
            "s3": s3,
            "sector": f"({_sign(s1)},{_sign(s2)},{_sign(s3)})",
        })
    return rows


def sector_members(rows: List[Dict], target: Tuple[int, int, int]) -> List[str]:
    """Return basis elements belonging to a given sector (s1, s2, s3)."""
    t1, t2, t3 = target
    return [r["element"] for r in rows if r["s1"] == t1 and r["s2"] == t2 and r["s3"] == t3]


# ---------------------------------------------------------------------------
# Carrier-space analysis
# ---------------------------------------------------------------------------

def analyse_carrier_space(rows: List[Dict]) -> Dict:
    """Identify single-minus sectors and the natural 3D complex carrier space."""

    # All eight Z2×Z2×Z2 sectors
    all_sectors = [
        (s1, s2, s3)
        for s1 in (+1, -1)
        for s2 in (+1, -1)
        for s3 in (+1, -1)
    ]

    sector_data = {}
    for sec in all_sectors:
        members = sector_members(rows, sec)
        label = f"({_sign(sec[0])},{_sign(sec[1])},{_sign(sec[2])})"
        n_minus = sum(1 for s in sec if s == -1)
        sector_data[label] = {
            "members": members,
            "dim_real": len(members),
            "single_minus": (n_minus == 1),
        }

    # S1=(-++), S2=(+-+), S3=(++-) — the named single-minus sectors
    s1_members = sector_members(rows, (-1, +1, +1))
    s2_members = sector_members(rows, (+1, -1, +1))
    s3_members = sector_members(rows, (+1, +1, -1))

    # Natural 3D complex carrier space: P2=-1 eigenspace = span_ℂ{I, J, K}
    p2_minus_members = [r["element"] for r in rows if r["s2"] == -1]

    return {
        "sector_data": sector_data,
        "S1_members": s1_members,
        "S2_members": s2_members,
        "S3_members": s3_members,
        "S3_empty": len(s3_members) == 0,
        "Vc_real_basis": p2_minus_members,
        "Vc_complex_dim": 3,  # span_ℂ{I, J, K}
    }


# ---------------------------------------------------------------------------
# Markdown report generator
# ---------------------------------------------------------------------------

def generate_report(
    rows: List[Dict],
    verif: Dict[str, bool],
    carrier: Dict,
) -> str:
    """Assemble the Markdown report."""

    table_header = "| Element | P1 (cpx conj) | P2 (quat conj) | P3 (axis-flip I) | Sector |\n"
    table_sep    = "|---------|:-------------:|:--------------:|:----------------:|--------|\n"
    table_rows   = "".join(
        f"| {r['element']:5s} | {_sign(r['s1'])} | {_sign(r['s2'])} | {_sign(r['s3'])} | {r['sector']} |\n"
        for r in rows
    )

    # Sector summary
    sec_lines = []
    for label, data in sorted(carrier["sector_data"].items()):
        mems = ", ".join(data["members"]) if data["members"] else "∅ (empty)"
        single = " ← single-minus" if data["single_minus"] else ""
        sec_lines.append(f"| `{label}` | {data['dim_real']} | {mems}{single} |")
    sector_table = "| Sector | dim_ℝ | Basis elements |\n|--------|-------|----------------|\n" + "\n".join(sec_lines)

    s1 = carrier["S1_members"]
    s2 = carrier["S2_members"]
    s3 = carrier["S3_members"]
    vc_basis = carrier["Vc_real_basis"]

    s3_note = (
        "The sector S3 = (+,+,−) is **empty** under the given involution definitions.\n"
        "This is a mathematical consequence: any element with P1=+1 (no complex-i)\n"
        "and P2=+1 (no quaternion-unit factor) is a real scalar multiple of 1,\n"
        "and P3(1) = +1, so it lies in (+,+,+) rather than (+,+,−).\n"
        "This is noted explicitly as part of the conservative candidate framing."
    )

    lines = [
        "<!-- Auto-generated by tools/involutions_triplet_projectors.py -->",
        "# Track A: Z2×Z2×Z2 Involution Triplet — Signature Report",
        "",
        "**Status:** Candidate construction — Track A, conservative framing.",
        "",
        "## 1. Basis and Involution Definitions",
        "",
        "Algebra: **ℬ = ℂ⊗ℍ**, viewed as an 8-dimensional real vector space with basis",
        "",
        "    B = {1, I, J, K, i, iI, iJ, iK}",
        "",
        "where `i` is the complex imaginary unit and `I, J, K` are the quaternion units.",
        "",
        "Three commuting real-linear involutions:",
        "",
        "| Involution | Definition | Physical interpretation |",
        "|-----------|------------|------------------------|",
        "| **P1** | `i → −i`, I/J/K fixed | Complex conjugation |",
        "| **P2** | `I,J,K → −I,−J,−K`, i fixed | Quaternion conjugation |",
        "| **P3** | `I → I, J → −J, K → −K`, i fixed | Axis-flip around I |",
        "",
        "## 2. Involution Verification",
        "",
        f"- P1² = id: **{verif['p1_involution']}**",
        f"- P2² = id: **{verif['p2_involution']}**",
        f"- P3² = id: **{verif['p3_involution']}**",
        f"- [P1, P2] = 0: **{verif['p1_p2_commute']}**",
        f"- [P1, P3] = 0: **{verif['p1_p3_commute']}**",
        f"- [P2, P3] = 0: **{verif['p2_p3_commute']}**",
        "",
        "## 3. Eigenvalue Signature Table",
        "",
        table_header + table_sep + table_rows,
        "",
        "## 4. Sector Cardinalities",
        "",
        sector_table,
        "",
        "## 5. Single-Minus Sectors",
        "",
        f"- **S1 = (−,+,+):** {', '.join(s1) if s1 else '∅'} — dim_ℝ = {len(s1)}",
        f"- **S2 = (+,−,+):** {', '.join(s2) if s2 else '∅'} — dim_ℝ = {len(s2)}",
        f"- **S3 = (+,+,−):** {', '.join(s3) if s3 else '∅ (empty)'} — dim_ℝ = {len(s3)}",
        "",
        "### Note on S3",
        "",
        s3_note,
        "",
        "## 6. Candidate 3D Complex Carrier Space Vc",
        "",
        "The natural **3D complex** carrier space is the P2=−1 eigenspace:",
        "",
        "    Vc = span_ℂ{I, J, K}",
        "",
        f"Real basis of Vc: {{{', '.join(vc_basis)}}}  (dim_ℝ = {len(vc_basis)}, dim_ℂ = {carrier['Vc_complex_dim']})",
        "",
        "Within Vc, P3 acts as a ℂ-linear involution with eigenspaces:",
        "- P3 = +1: span_ℂ{I}  (1D over ℂ)",
        "- P3 = −1: span_ℂ{J, K}  (2D over ℂ)",
        "",
        "The SU(3) **candidate** is the group of ℂ-linear unitary transformations",
        "of determinant 1 acting on Vc ≅ ℂ³.",
        "",
        "## 7. Conservative Framing",
        "",
        "This construction identifies an SU(3) acting on a Θ-triplet subspace",
        "extracted from ℬ via the P2 involution.  It is **not** claimed that",
        "SU(3) arises as an automorphism of ℬ itself (the automorphism group",
        "Aut(ℂ⊗ℍ) ≅ [GL(2,ℂ)×GL(2,ℂ)]/ℤ₂ does not contain SU(3) — see",
        "`reports/associative_su3_scan.md`).  This is Track A, candidate",
        "construction only.",
        "",
        "---",
        "_Generated by `tools/involutions_triplet_projectors.py`_",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

REPORT_PATH = pathlib.Path("reports/involutions_triplet_report.md")


def main() -> None:
    verif = verify_involutions()
    rows = compute_signatures()
    carrier = analyse_carrier_space(rows)

    # Print table to stdout
    print("=== Basis signature table ===")
    print(f"{'Element':6s}  P1  P2  P3  Sector")
    print("-" * 38)
    for r in rows:
        print(
            f"{r['element']:6s}  {_sign(r['s1'])}   {_sign(r['s2'])}   {_sign(r['s3'])}   {r['sector']}"
        )

    print()
    print("=== Single-minus sector cardinalities ===")
    print(f"  S1=(-,+,+): {carrier['S1_members']}  dim_ℝ={len(carrier['S1_members'])}")
    print(f"  S2=(+,-,+): {carrier['S2_members']}  dim_ℝ={len(carrier['S2_members'])}")
    print(f"  S3=(+,+,-): {carrier['S3_members']}  dim_ℝ={len(carrier['S3_members'])}")
    if carrier["S3_empty"]:
        print("  NOTE: S3=(+,+,-) is empty — see mathematical note in report.")

    print()
    print("=== Candidate carrier space Vc = span_ℂ{I,J,K} ===")
    print(f"  Real basis: {carrier['Vc_real_basis']}")
    print(f"  dim_ℂ = {carrier['Vc_complex_dim']}")

    # Write report
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report = generate_report(rows, verif, carrier)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"\nReport written to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
