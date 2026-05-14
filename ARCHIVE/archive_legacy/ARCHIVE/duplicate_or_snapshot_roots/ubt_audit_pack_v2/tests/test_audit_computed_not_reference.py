# tests/test_audit_computed_not_reference.py (v2)
import subprocess, sys, pathlib

def test_audit_script_v2_passes():
    root = pathlib.Path(__file__).resolve().parents[1]
    cmd = [sys.executable, str(root / "tools" / "audit_computed_not_reference.py"), "--root", str(root)]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(proc.stdout)
    assert proc.returncode == 0, "Audit failed; see output above"
