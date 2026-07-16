from __future__ import annotations

import json
import os
from pathlib import Path
import stat

from tools import latex_audit


def _write_root(path: Path, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\\documentclass{article}\n\\begin{document}\n" + body + "\n\\end{document}\n",
        encoding="utf-8",
    )


def test_discovery_excludes_legacy_and_fragments(tmp_path: Path) -> None:
    _write_root(tmp_path / "papers" / "good.tex")
    _write_root(tmp_path / "ARCHIVE" / "archive_legacy" / "old.tex")
    (tmp_path / "papers" / "fragment.tex").write_text("\\section{Fragment}\n", encoding="utf-8")

    active = latex_audit.discover_roots(tmp_path)
    assert [p.relative_to(tmp_path).as_posix() for p in active] == ["papers/good.tex"]

    all_roots = latex_audit.discover_roots(tmp_path, include_archive=True)
    assert [p.relative_to(tmp_path).as_posix() for p in all_roots] == [
        "ARCHIVE/archive_legacy/old.tex",
        "papers/good.tex",
    ]


def test_batch_continues_after_failed_root_and_resets_report(tmp_path: Path, monkeypatch) -> None:
    repo = tmp_path / "repo"
    _write_root(repo / "papers" / "fail.tex", "FAIL")
    _write_root(repo / "papers" / "success.tex", "SUCCESS")
    report = repo / "reports" / "latex_build"
    report.mkdir(parents=True)
    (report / "stale.txt").write_text("old run", encoding="utf-8")

    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_latexmk = fake_bin / "latexmk"
    fake_latexmk.write_text(
        "#!/usr/bin/env python3\n"
        "import pathlib, sys\n"
        "out = next(a.split('=', 1)[1] for a in sys.argv if a.startswith('-outdir='))\n"
        "root = pathlib.Path(sys.argv[-1])\n"
        "pathlib.Path(out).mkdir(parents=True, exist_ok=True)\n"
        "if root.name == 'fail.tex':\n"
        "    print('intentional failure')\n"
        "    raise SystemExit(7)\n"
        "(pathlib.Path(out) / (root.stem + '.pdf')).write_bytes(b'%PDF-1.4\\n%%EOF\\n')\n"
        "print('success')\n",
        encoding="utf-8",
    )
    fake_latexmk.chmod(fake_latexmk.stat().st_mode | stat.S_IXUSR)
    monkeypatch.setenv("PATH", f"{fake_bin}{os.pathsep}{os.environ['PATH']}")

    rc = latex_audit.main(
        [
            "--repo",
            str(repo),
            "--jobs",
            "2",
            "--timeout",
            "10",
        ]
    )
    assert rc == 0
    assert not (report / "stale.txt").exists()
    payload = json.loads((report / "results.json").read_text(encoding="utf-8"))
    assert payload["totals"]["discovered"] == 2
    assert payload["totals"]["success"] == 1
    assert payload["totals"]["failed"] == 1
    assert (repo / "build" / "latex-audit" / "pdfs" / "papers" / "success.pdf").is_file()
    assert list((report / "logs").glob("*.txt"))


def test_strict_mode_reports_failure_after_attempting_everything(tmp_path: Path, monkeypatch) -> None:
    repo = tmp_path / "repo"
    _write_root(repo / "a.tex")
    _write_root(repo / "b.tex")

    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_latexmk = fake_bin / "latexmk"
    fake_latexmk.write_text("#!/bin/sh\necho fail\nexit 2\n", encoding="utf-8")
    fake_latexmk.chmod(fake_latexmk.stat().st_mode | stat.S_IXUSR)
    monkeypatch.setenv("PATH", f"{fake_bin}{os.pathsep}{os.environ['PATH']}")

    rc = latex_audit.main(["--repo", str(repo), "--jobs", "2", "--strict"])
    assert rc == 1
    payload = json.loads((repo / "reports" / "latex_build" / "results.json").read_text())
    assert payload["totals"]["discovered"] == 2
    assert payload["totals"]["failed"] == 2
