from __future__ import annotations
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def load():
    p=ROOT/'tools/verify_split_jet_right_inverse.py'
    spec=importlib.util.spec_from_file_location('split_jet',p)
    assert spec and spec.loader
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def test_exact_symbolic_right_inverse():
    assert all(load().symbolic_checks().values())

def test_exact_samples():
    assert all(load().exact_sample_checks().values())

def test_status_is_kinematic_not_dynamic():
    claims=(ROOT/'CLAIMS.yaml').read_text()
    assert 'GAP-10T-JET-KIN: CLOSED LOCALLY' in claims
    assert (
        'GAP-10T-JET-DYN: CLOSED CONDITIONALLY FOR GR RECOVERY; '
        'OPEN FUNDAMENTALLY'
    ) in claims
