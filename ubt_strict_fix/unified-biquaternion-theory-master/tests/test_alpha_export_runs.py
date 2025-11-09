# tests/test_alpha_export_runs.py
import os, pathlib, importlib, runpy

def test_export_alpha_csv_runs():
    root = pathlib.Path(__file__).resolve().parents[1]
    os.environ['PYTHONPATH'] = str(root) + os.pathsep + os.environ.get('PYTHONPATH', '')
    # ensure forwarder module is importable
    import alpha_core_repro.two_loop_core  # noqa: F401
    # run exporter; it should write the CSV
    runpy.run_module('alpha_core_repro.export_alpha_csv', run_name='__main__')
    assert (root / 'data' / 'alpha_two_loop_grid.csv').exists(), 'alpha grid CSV not created'
