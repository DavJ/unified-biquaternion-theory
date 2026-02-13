"""
Layer 2 Configuration Space Definition

This module defines Layer 2 parameters and configuration space sampling.

Layer 2 Parameters (UBT Digital Architecture):
-----------------------------------------------
- rs_n, rs_k: Reed-Solomon error correction code parameters
  Status: Design choice (RS(255,200) in current UBT)
  
- ofdm_channels: Orthogonal frequency-division multiplexing channels
  Status: Design choice (16 in current UBT)
  
- winding_number: Topological winding number (related to α)
  Status: Hypothesis - potentially constrained by stability (n=137 in current UBT)
  
- prime_gate_pattern: Prime gating pattern index
  Status: Design choice / Unknown constraint
  
- quantization_grid: Quantization grid size (e.g., 255, 256)
  Status: Design choice

Note: Layer 2 parameters are "channel selection" choices, not fundamental
physics constants. See docs/architecture/LAYERS.md for Layer 1 vs Layer 2.

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

from __future__ import annotations

import math
from dataclasses import dataclass, asdict
from typing import Tuple, List
import numpy as np


@dataclass
class Layer2Config:
    """
    A single Layer 2 configuration.
    
    Attributes
    ----------
    rs_n : int
        Reed-Solomon code length (design choice)
    rs_k : int  
        Reed-Solomon code dimension (design choice)
    ofdm_channels : int
        Number of OFDM channels (design choice)
    winding_number : int
        Topological winding number (hypothesis - may be constrained)
    prime_gate_pattern : int
        Prime gating pattern index (design choice/unknown)
    quantization_grid : int
        Quantization grid size (design choice)
    """
    rs_n: int
    rs_k: int
    ofdm_channels: int
    winding_number: int
    prime_gate_pattern: int
    quantization_grid: int
    
    def __post_init__(self):
        """Validate configuration constraints."""
        if self.rs_k > self.rs_n:
            raise ValueError(
                f"rs_k ({self.rs_k}) cannot exceed rs_n ({self.rs_n})"
            )
        if self.rs_n <= 0 or self.rs_k <= 0:
            raise ValueError("rs_n and rs_k must be positive")
        if self.ofdm_channels <= 0:
            raise ValueError("ofdm_channels must be positive")
        if self.winding_number <= 0:
            raise ValueError("winding_number must be positive")
        if self.prime_gate_pattern < 0:
            raise ValueError("prime_gate_pattern must be non-negative")
        if self.quantization_grid <= 0:
            raise ValueError("quantization_grid must be positive")
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return asdict(self)


class ConfigurationSpace:
    """
    Defines a configuration space for Layer 2 parameter sampling.
    
    Three predefined spaces:
    - 'debug': Small ranges for quick testing
    - 'baseline': Standard ranges around current UBT values  
    - 'wide': Broader ranges for wider exploration
    """
    
    def __init__(self, space_type: str):
        """
        Initialize configuration space.
        
        Parameters
        ----------
        space_type : str
            One of: 'baseline', 'wide', 'debug'
        """
        self.space_type = space_type
        self._define_ranges()
    
    def _define_ranges(self):
        """Define parameter ranges for each space type."""
        if self.space_type == 'baseline':
            # Standard ranges around current UBT values
            self.rs_n_range = (200, 300)
            self.rs_k_ratio_range = (0.6, 0.9)  # k/n ratio
            self.ofdm_range = (8, 32)
            self.winding_range = (101, 199)  # Prime numbers preferred
            self.prime_gate_patterns = 10
            self.quantization_grids = [128, 255, 256, 512]
            
        elif self.space_type == 'wide':
            # Broader ranges for wider exploration
            self.rs_n_range = (100, 500)
            self.rs_k_ratio_range = (0.5, 0.95)
            self.ofdm_range = (4, 64)
            self.winding_range = (50, 250)
            self.prime_gate_patterns = 20
            self.quantization_grids = [64, 128, 255, 256, 512, 1024]
            
        elif self.space_type == 'debug':
            # Small range for quick testing
            self.rs_n_range = (250, 260)
            self.rs_k_ratio_range = (0.75, 0.85)
            self.ofdm_range = (12, 20)
            self.winding_range = (130, 145)
            self.prime_gate_patterns = 3
            self.quantization_grids = [255, 256]
            
        else:
            raise ValueError(f"Unknown space type: {self.space_type}")
    
    def sample(self, rng: np.random.Generator) -> Layer2Config:
        """
        Sample a random configuration from this space.
        
        Parameters
        ----------
        rng : np.random.Generator
            Random number generator for reproducibility
            
        Returns
        -------
        Layer2Config
            Randomly sampled configuration
        """
        # Sample RS parameters
        rs_n = rng.integers(self.rs_n_range[0], self.rs_n_range[1] + 1)
        k_ratio = rng.uniform(self.rs_k_ratio_range[0], self.rs_k_ratio_range[1])
        rs_k = max(1, int(rs_n * k_ratio))
        
        # Sample OFDM channels
        ofdm_channels = rng.integers(self.ofdm_range[0], self.ofdm_range[1] + 1)
        
        # Sample winding number (prefer primes in baseline/wide)
        if self.space_type in ['baseline', 'wide']:
            winding_number = self._sample_prime(rng, self.winding_range)
        else:
            winding_number = rng.integers(
                self.winding_range[0], 
                self.winding_range[1] + 1
            )
        
        # Sample prime gate pattern
        prime_gate_pattern = rng.integers(0, self.prime_gate_patterns)
        
        # Sample quantization grid
        quantization_grid = rng.choice(self.quantization_grids)
        
        return Layer2Config(
            rs_n=rs_n,
            rs_k=rs_k,
            ofdm_channels=ofdm_channels,
            winding_number=winding_number,
            prime_gate_pattern=prime_gate_pattern,
            quantization_grid=quantization_grid
        )
    
    def _sample_prime(
        self, 
        rng: np.random.Generator, 
        range_tuple: Tuple[int, int]
    ) -> int:
        """Sample a prime number from a range."""
        primes = [
            p for p in range(range_tuple[0], range_tuple[1] + 1) 
            if self._is_prime(p)
        ]
        if not primes:
            # Fallback to any integer if no primes in range
            return rng.integers(range_tuple[0], range_tuple[1] + 1)
        return rng.choice(primes)
    
    @staticmethod
    def _is_prime(n: int) -> bool:
        """Check if n is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def describe(self) -> dict:
        """Return description of this configuration space."""
        return {
            'space_type': self.space_type,
            'rs_n_range': self.rs_n_range,
            'rs_k_ratio_range': self.rs_k_ratio_range,
            'ofdm_range': self.ofdm_range,
            'winding_range': self.winding_range,
            'prime_gate_patterns': self.prime_gate_patterns,
            'quantization_grids': self.quantization_grids,
        }
