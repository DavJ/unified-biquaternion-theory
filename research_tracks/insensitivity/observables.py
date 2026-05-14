# insensitivity/observables.py
from __future__ import annotations
import math
from dataclasses import dataclass

@dataclass
class AlphaBundle:
    alpha: float     # fine-structure constant
    m_e: float = 1.0 # normalized (can be rescaled if UBT requires)

def rydberg_scale(ab: AlphaBundle) -> float:
    # ∝ α^2 m_e in natural units (constant factors irrelevant for relative sweeps)
    return (ab.alpha ** 2) * ab.m_e

def thomson_sigma_proxy(ab: AlphaBundle) -> float:
    # σ_T ∝ α^2 / m_e^2 => proxy captures α-dependence; m_e rescaling can enforce insensitivity
    return (ab.alpha ** 2) / (ab.m_e ** 2)

def gamow_barrier_proxy(ab: AlphaBundle) -> float:
    # very crude proxy ∝ α^2 (true Gamow factor is exponential in √(E_G/E));
    # we use it only to measure relative sensitivity in small-Δα sweeps.
    return (ab.alpha ** 2)
