#!/usr/bin/env python3
"""Generate the speculative UBT prime-resonance harmonic table.
Important boundary:
- 137 is used here as the alpha-adjacent anchor already studied elsewhere.
- 139 is treated only as a speculative neighboring prime / harmonic partner.
- N0 = 137 * 139 and all cycle interpretations are non-canonical and belong only under speculative_extensions.


Status: speculative extension / research sketch.
This is intentionally not part of canonical UBT.
"""
from __future__ import annotations
from pathlib import Path
import csv, math

N0 = 137 * 139
LAMBDA = 0.015
OUT = Path(__file__).resolve().parents[2] / 'speculative_extensions' / 'prime_resonance_channels' / 'data'
OUT.mkdir(parents=True, exist_ok=True)


def divisor_count(k: int) -> int:
    c = 0
    r = int(math.sqrt(k))
    for d in range(1, r + 1):
        if k % d == 0:
            c += 1 if d * d == k else 2
    return c


def factor_pairs(k: int) -> list[tuple[int, int]]:
    return [(d, k // d) for d in range(1, int(math.sqrt(k)) + 1) if k % d == 0]


def prime_factors(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def eta_like_weight(k: int, lam: float = LAMBDA) -> float:
    # not a theorem; a soft factor-pair weight inspired by eta-product suppression
    return sum(math.exp(-lam * (m + n)) for m, n in factor_pairs(k))


def scale_label(T: float) -> str:
    if T >= 15000:
        return "paleoclimate / glacial-precessional boundary scale"
    if T >= 8000:
        return "early Holocene / Neolithic transition scale"
    if T >= 5000:
        return "early agricultural-civilizational scale"
    if T >= 3000:
        return "long civilizational epoch scale"
    if T >= 1200:
        return "religious / imperial macro-cycle scale"
    if T >= 600:
        return "empire / cultural-memory scale"
    if T >= 250:
        return "dynastic / historical wave scale"
    if T >= 80:
        return "human lifetime / generational scale"
    if T >= 20:
        return "social-generation scale"
    if T >= 7:
        return "short cultural cycle scale"
    if T >= 1:
        return "annual/subannual harmonic scale"
    return "subannual high harmonic scale"


def resonance_score(k: int) -> float:
    tau = divisor_count(k)
    w = eta_like_weight(k)
    # simple monotone score: favors many factor channels and eta-like soft support
    return tau * math.log1p(k) * (1.0 + w)


def main() -> None:
    full_rows = []
    for k in range(1, N0 + 1):
        T = N0 / k
        pairs = factor_pairs(k)
        factors = prime_factors(k)
        tau = divisor_count(k)
        w = eta_like_weight(k)
        score = resonance_score(k)
        full_rows.append({
            "k": k,
            "period_N0_over_k": f"{T:.12f}",
            "divisor_count_tau": tau,
            "prime_factorization": "*".join(map(str, factors)) if factors else "1",
            "factor_pairs": "; ".join(f"{a}x{b}" for a,b in pairs),
            "eta_like_weight_lambda_0_015": f"{w:.12e}",
            "resonance_score": f"{score:.12f}",
            "scale_label": scale_label(T),
        })

    full_csv = OUT / "prime_resonance_harmonic_table_full.csv"
    with full_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(full_rows[0].keys()))
        writer.writeheader()
        writer.writerows(full_rows)

    # Smaller ranked table for paper/README readability
    top_by_score = sorted(full_rows, key=lambda r: float(r["resonance_score"]), reverse=True)[:250]
    top_csv = OUT / "prime_resonance_top250_by_score.csv"
    with top_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(full_rows[0].keys()))
        writer.writeheader()
        writer.writerows(top_by_score)

    # Landmark channels: divisors of N0 plus near-alpha/near-139 channels and selected periods
    landmark_k = sorted(set([1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 137*139]))
    landmark_rows = [full_rows[k-1] for k in landmark_k]
    landmark_csv = OUT / "prime_resonance_landmark_channels.csv"
    with landmark_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(full_rows[0].keys()))
        writer.writeheader()
        writer.writerows(landmark_rows)

    md = OUT / "prime_resonance_table_summary.md"
    with md.open("w", encoding="utf-8") as f:
        f.write("# Prime resonance harmonic table summary\n\n")
        f.write("Status: speculative extension, not canonical UBT.\n\n")
        f.write(f"Base integer: `N0 = 137 * 139 = {N0}`.\n\n")
        f.write("Files generated:\n\n")
        f.write("- `prime_resonance_harmonic_table_full.csv` — all k = 1..19043.\n")
        f.write("- `prime_resonance_top250_by_score.csv` — top 250 by the simple speculative resonance score.\n")
        f.write("- `prime_resonance_landmark_channels.csv` — selected landmark channels including 137, 139, and N0.\n\n")
        f.write("## Landmark channels\n\n")
        f.write("| k | period N0/k | tau(k) | prime factors | eta-like weight | label |\n")
        f.write("|---:|---:|---:|---|---:|---|\n")
        for r in landmark_rows:
            f.write(f"| {r['k']} | {r['period_N0_over_k']} | {r['divisor_count_tau']} | {r['prime_factorization']} | {r['eta_like_weight_lambda_0_015']} | {r['scale_label']} |\n")
        f.write("\n## Top 50 channels by speculative score\n\n")
        f.write("| rank | k | period N0/k | tau(k) | factors | score | label |\n")
        f.write("|---:|---:|---:|---:|---|---:|---|\n")
        for i, r in enumerate(top_by_score[:50], start=1):
            f.write(f"| {i} | {r['k']} | {r['period_N0_over_k']} | {r['divisor_count_tau']} | {r['prime_factorization']} | {r['resonance_score']} | {r['scale_label']} |\n")

    print(f"Generated {full_csv}")
    print(f"Generated {top_csv}")
    print(f"Generated {landmark_csv}")
    print(f"Generated {md}")


if __name__ == "__main__":
    main()
