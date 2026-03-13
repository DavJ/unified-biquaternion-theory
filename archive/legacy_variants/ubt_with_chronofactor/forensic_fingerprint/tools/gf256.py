"""GF(256) arithmetic.

Field: GF(2^8)
Primitive polynomial: 0x11d
Primitive element: 0x02

Elements are ints 0..255.
Add/sub: XOR.
Mul/div/pow: log/exp tables.

Sufficient for RS syndrome checks (not a full decoder).
"""

from __future__ import annotations

from typing import List

PRIMITIVE_POLY = 0x11D
PRIMITIVE_ELEM = 0x02
FIELD_SIZE = 256



# exp table duplicated to length 512 so exp[idx] works without modulo 255.
_EXP: List[int] = [0] * 512
_LOG: List[int] = [0] * 256


def _init_tables() -> None:
    x = 1
    for i in range(0, 255):
        _EXP[i] = x
        _LOG[x] = i
        x <<= 1
        if x & 0x100:
            x ^= PRIMITIVE_POLY
    # duplicate
    for i in range(255, 512):
        _EXP[i] = _EXP[i - 255]


_init_tables()


def add(a: int, b: int) -> int:
    return a ^ b


sub = add


def mul(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return _EXP[_LOG[a] + _LOG[b]]


def div(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError('division by zero in GF(256)')
    if a == 0:
        return 0
    return _EXP[(_LOG[a] - _LOG[b]) % 255]


def pow_alpha(k: int) -> int:
    """Return alpha^k in GF(256), where alpha is the primitive element."""
    return _EXP[k % 255]


def pow(a: int, k: int) -> int:
    if k == 0:
        return 1
    if a == 0:
        return 0
    return _EXP[(_LOG[a] * k) % 255]


def exp_table() -> List[int]:
    return list(_EXP)


def log_table() -> List[int]:
    return list(_LOG)
