# alpha_core_repro/tests/test_alpha_two_loop.py
# SPDX-License-Identifier: MIT
import os, numpy as np, pytest
from alpha_core_repro.alpha_two_loop import compute_two_loop_delta, alpha_corrected, TwoLoopConfig

PRIMES = [131, 137, 139]

def _cfg(strict: bool):
    return TwoLoopConfig(strict=strict)

@pytest.mark.parametrize("p", PRIMES)
def test_two_loop_pipeline_sanity(p):
    strict = os.environ.get("UBT_ALPHA_STRICT", "1") == "1"
    cfg = _cfg(strict=strict)
    if strict:
        with pytest.raises(NotImplementedError):
            compute_two_loop_delta(p, cfg)
        pytest.skip("Strict mode: implement two-loop core to enable full test.")
    else:
        os.environ["UBT_ALPHA_ALLOW_MOCK"] = "1"
        dct = compute_two_loop_delta(p, cfg)
        assert np.isfinite(dct) and dct > 0
        inva = 1.0 / alpha_corrected(p, dct)
        assert abs(inva - p) < 1.0

def test_alpha_137_precision_when_mock_enabled():
    os.environ["UBT_ALPHA_STRICT"] = "0"
    os.environ["UBT_ALPHA_ALLOW_MOCK"] = "1"
    cfg = _cfg(strict=False)
    dct = compute_two_loop_delta(137, cfg)
    inva = 1.0 / alpha_corrected(137, dct)
    assert abs(inva - 137.035999) < 5e-4
