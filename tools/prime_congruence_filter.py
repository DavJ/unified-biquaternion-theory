# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Prime congruence filter for genus(X_0(p))=11 and p ≡ 1 (mod 4)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PrimeRecord:
    p: int
    genus: int
    nu2: int
    nu3: int
    p_mod_4: int


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def genus_gamma0_prime(p: int) -> int:
    """Genus of X_0(p) for odd prime p (Diamond–Shurman formula)."""
    if p < 2 or not is_prime(p):
        raise ValueError("p must be prime")
    if p in (2, 3):
        return 0
    nu2 = 2 if p % 4 == 1 else 0
    nu3 = 2 if p % 3 == 1 else 0
    g = 1 + (p + 1) / 12 - nu2 / 4 - nu3 / 3 - 1
    return int(round(g))


def scan(lo: int = 50, hi: int = 500) -> list[PrimeRecord]:
    out: list[PrimeRecord] = []
    for p in range(lo, hi + 1):
        if not is_prime(p):
            continue
        if p in (2, 3):
            continue
        nu2 = 2 if p % 4 == 1 else 0
        nu3 = 2 if p % 3 == 1 else 0
        g = genus_gamma0_prime(p)
        out.append(PrimeRecord(p=p, genus=g, nu2=nu2, nu3=nu3, p_mod_4=p % 4))
    return out


def main() -> None:
    lo, hi = 50, 500
    rows = scan(lo, hi)

    genus11 = [r for r in rows if r.genus == 11]
    selected = [r for r in genus11 if r.p_mod_4 == 1]

    print(f"Prime scan range: [{lo}, {hi}]")
    print(f"Total primes scanned: {len(rows)}")
    print()

    print("Primes with genus(X_0(p)) = 11:")
    for r in genus11:
        print(f"  p={r.p:3d}  p mod 4={r.p_mod_4}  nu2={r.nu2}  nu3={r.nu3}")
    print()

    print("Filtered by p ≡ 1 (mod 4):")
    for r in selected:
        print(f"  p={r.p:3d}  genus={r.genus}  nu2={r.nu2}")
    print()

    print(f"Count(genus=11 AND p≡1 mod 4): {len(selected)}")
    print(f"Selected primes: {[r.p for r in selected]}")


if __name__ == "__main__":
    main()
