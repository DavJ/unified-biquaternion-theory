#!/usr/bin/env python3
"""Compile every active standalone LaTeX root without fail-fast behaviour.

The tool discovers TeX files containing ``\\documentclass`` and builds each root
in an isolated output directory.  A failed document never prevents later roots
from being attempted.  The report directory is deleted and recreated at the
start of every run so it always describes exactly one audit run.

Document failures are reported but do not make the process fail unless
``--strict`` is requested.  Infrastructure failures (for example a missing
``latexmk`` executable) still return a non-zero exit status.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import datetime as dt
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
from typing import Iterable, Sequence

DEFAULT_EXCLUDED_PREFIXES = (
    ".git/",
    ".latex-build/",
    "build/",
    "dist/",
    "node_modules/",
    "ARCHIVE/archive_legacy/",
    "research_tracks/legacy_theory_variants/",
)

ENGINE_MAGIC_RE = re.compile(
    r"^[ \t]*%\s*!?TEX\s+(?:program|engine)\s*=\s*(pdflatex|xelatex|lualatex)",
    re.IGNORECASE | re.MULTILINE,
)
DOCUMENTCLASS_RE = re.compile(r"^[ \t]*(?!%)[^\n]*\\documentclass(?:\[[^\]]*\])?\{", re.MULTILINE)


@dataclasses.dataclass(frozen=True)
class BuildResult:
    root: str
    engine: str
    status: str
    seconds: float
    returncode: int | None
    pdf: str | None
    log: str | None
    message: str

    @property
    def succeeded(self) -> bool:
        return self.status == "success"




def _display_path(path: Path, repo: Path) -> str:
    try:
        return path.relative_to(repo).as_posix()
    except ValueError:
        return path.as_posix()

def _safe_name(path: str) -> str:
    digest = hashlib.sha1(path.encode("utf-8")).hexdigest()[:10]
    stem = re.sub(r"[^A-Za-z0-9._-]+", "__", path).strip("._")
    return f"{stem[:150]}__{digest}"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def detect_engine(path: Path, override: str | None = None) -> str:
    if override:
        if override not in {"pdflatex", "xelatex", "lualatex"}:
            raise ValueError(f"Unsupported LaTeX engine override: {override}")
        return override
    text = _read_text(path)
    magic = ENGINE_MAGIC_RE.search(text)
    if magic:
        return magic.group(1).lower()
    if re.search(r"\\usepackage(?:\[[^\]]*\])?\{[^}]*luacode", text):
        return "lualatex"
    if re.search(r"\\usepackage(?:\[[^\]]*\])?\{[^}]*(?:fontspec|polyglossia|unicode-math)", text):
        return "xelatex"
    return "pdflatex"




def load_engine_overrides(repo: Path, path: Path | None) -> dict[str, str]:
    if path is None:
        return {}
    resolved = path if path.is_absolute() else repo / path
    if not resolved.is_file():
        return {}
    overrides: dict[str, str] = {}
    for number, raw in enumerate(resolved.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = raw.split("\t")
        if len(fields) != 2:
            raise ValueError(f"{resolved}:{number}: expected ROOT<TAB>ENGINE")
        root, engine = (field.strip() for field in fields)
        engine = engine.lower()
        if engine not in {"pdflatex", "xelatex", "lualatex"}:
            raise ValueError(f"{resolved}:{number}: unsupported engine {engine}")
        overrides[root] = engine
    return overrides

def _is_excluded(relative: str, prefixes: Sequence[str], include_archive: bool) -> bool:
    rel = relative.replace(os.sep, "/")
    for prefix in prefixes:
        if include_archive and prefix in {
            "ARCHIVE/archive_legacy/",
            "research_tracks/legacy_theory_variants/",
        }:
            continue
        if rel.startswith(prefix):
            return True
    return False


def discover_roots(
    repo: Path,
    *,
    include_archive: bool = False,
    include_patterns: Sequence[str] = (),
    exclude_patterns: Sequence[str] = (),
    excluded_prefixes: Sequence[str] = DEFAULT_EXCLUDED_PREFIXES,
) -> list[Path]:
    roots: list[Path] = []
    for path in repo.rglob("*.tex"):
        if not path.is_file():
            continue
        rel = path.relative_to(repo).as_posix()
        if _is_excluded(rel, excluded_prefixes, include_archive):
            continue
        if include_patterns and not any(fnmatch.fnmatch(rel, pattern) for pattern in include_patterns):
            continue
        if any(fnmatch.fnmatch(rel, pattern) for pattern in exclude_patterns):
            continue
        try:
            text = _read_text(path)
        except OSError:
            continue
        if DOCUMENTCLASS_RE.search(text):
            roots.append(path)
    return sorted(roots, key=lambda p: p.relative_to(repo).as_posix().lower())


def _latexmk_command(engine: str, output_dir: Path, root_name: str) -> list[str]:
    engine_flag = {
        "pdflatex": "-pdf",
        "xelatex": "-xelatex",
        "lualatex": "-lualatex",
    }[engine]
    return [
        "latexmk",
        engine_flag,
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "-recorder",
        f"-outdir={output_dir}",
        root_name,
    ]


def compile_root(
    repo: Path,
    root: Path,
    work_dir: Path,
    pdf_dir: Path,
    log_dir: Path,
    timeout: int,
    engine_override: str | None = None,
) -> BuildResult:
    rel = root.relative_to(repo).as_posix()
    engine = detect_engine(root, engine_override)
    safe = _safe_name(rel)
    root_work = work_dir / safe
    root_work.mkdir(parents=True, exist_ok=True)
    command = _latexmk_command(engine, root_work, root.name)
    env = os.environ.copy()
    repo_texinputs = f"{repo}//"
    current_texinputs = env.get("TEXINPUTS", "")
    env["TEXINPUTS"] = f".:{repo_texinputs}:{current_texinputs}"

    started = time.monotonic()
    try:
        proc = subprocess.run(
            command,
            cwd=root.parent,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            errors="replace",
            timeout=timeout,
            check=False,
        )
        output = proc.stdout or ""
        returncode: int | None = proc.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        partial = exc.stdout or ""
        if isinstance(partial, bytes):
            partial = partial.decode("utf-8", errors="replace")
        output = partial + f"\n\n[TIMEOUT] Build exceeded {timeout} seconds.\n"
        returncode = None
        timed_out = True
    elapsed = time.monotonic() - started

    built_pdf = root_work / f"{root.stem}.pdf"
    if not timed_out and returncode == 0 and built_pdf.is_file():
        target_pdf = pdf_dir / root.relative_to(repo).with_suffix(".pdf")
        target_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(built_pdf, target_pdf)
        return BuildResult(
            root=rel,
            engine=engine,
            status="success",
            seconds=elapsed,
            returncode=returncode,
            pdf=_display_path(target_pdf, repo),
            log=None,
            message="PDF produced",
        )

    status = "timeout" if timed_out else "failed"
    log_path = log_dir / f"{safe}.txt"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        f"ROOT: {rel}\n"
        f"ENGINE: {engine}\n"
        f"STATUS: {status}\n"
        f"RETURN_CODE: {returncode}\n"
        f"SECONDS: {elapsed:.2f}\n"
        f"COMMAND: {' '.join(command)}\n"
        "\n--- LATEXMK OUTPUT ---\n"
    )
    log_path.write_text(header + output, encoding="utf-8")
    message = "timed out" if timed_out else f"latexmk exit code {returncode}"
    if not built_pdf.is_file() and not timed_out and returncode == 0:
        message = "latexmk returned success but no PDF was produced"
    return BuildResult(
        root=rel,
        engine=engine,
        status=status,
        seconds=elapsed,
        returncode=returncode,
        pdf=None,
        log=_display_path(log_path, repo),
        message=message,
    )


def _git_value(repo: Path, *args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args], cwd=repo, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def write_reports(
    repo: Path,
    report_dir: Path,
    results: Sequence[BuildResult],
    started_at: str,
    include_archive: bool,
) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)
    successes = [r for r in results if r.succeeded]
    failures = [r for r in results if not r.succeeded]
    total_seconds = sum(r.seconds for r in results)
    commit = os.environ.get("GITHUB_SHA") or _git_value(repo, "rev-parse", "HEAD")
    ref = os.environ.get("GITHUB_REF_NAME") or _git_value(repo, "branch", "--show-current")

    payload = {
        "schema_version": 1,
        "started_at_utc": started_at,
        "commit": commit,
        "ref": ref,
        "scope": "all roots including archive" if include_archive else "active standalone roots",
        "totals": {
            "discovered": len(results),
            "success": len(successes),
            "failed": sum(r.status == "failed" for r in failures),
            "timeout": sum(r.status == "timeout" for r in failures),
            "aggregate_build_seconds": round(total_seconds, 3),
        },
        "results": [dataclasses.asdict(r) for r in results],
    }
    (report_dir / "results.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (report_dir / "roots.txt").write_text(
        "\n".join(r.root for r in results) + ("\n" if results else ""), encoding="utf-8"
    )
    (report_dir / "failures.txt").write_text(
        "\n".join(f"{r.status.upper()}\t{r.root}\t{r.message}\t{r.log or '-'}" for r in failures)
        + ("\n" if failures else "No failed LaTeX roots.\n"),
        encoding="utf-8",
    )

    lines = [
        "# LaTeX build audit",
        "",
        "> This directory is generated from scratch by `tools/latex_audit.py`. "
        "Do not append manual results; the next run deletes the directory first.",
        "",
        f"- Started (UTC): `{started_at}`",
        f"- Commit: `{commit}`",
        f"- Ref: `{ref or 'unknown'}`",
        f"- Scope: `{'all roots including archive' if include_archive else 'active standalone roots'}`",
        f"- Roots attempted: **{len(results)}**",
        f"- PDFs produced: **{len(successes)}**",
        f"- Failed: **{sum(r.status == 'failed' for r in failures)}**",
        f"- Timed out: **{sum(r.status == 'timeout' for r in failures)}**",
        "",
        "A failed document does not stop later builds. Successful PDFs are uploaded as a workflow artifact; "
        "only curated publication PDFs are committed to `docs/pdfs/`.",
        "",
    ]
    if failures:
        lines.extend([
            "## Failed roots",
            "",
            "| Status | Root | Engine | Seconds | Failure log |",
            "|---|---|---:|---:|---|",
        ])
        for result in failures:
            lines.append(
                f"| {result.status} | `{result.root}` | `{result.engine}` | "
                f"{result.seconds:.1f} | `{result.log}` |"
            )
    else:
        lines.extend(["## Result", "", "All discovered roots compiled successfully."])
    lines.append("")
    (report_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with Path(step_summary).open("a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--report-dir", type=Path, default=Path("reports/latex_build"))
    parser.add_argument("--build-dir", type=Path, default=Path("build/latex-audit"))
    parser.add_argument("--jobs", type=int, default=max(1, min(4, os.cpu_count() or 1)))
    parser.add_argument("--timeout", type=int, default=180, help="seconds per root")
    parser.add_argument("--include-archive", action="store_true")
    parser.add_argument("--engine-overrides", type=Path, default=Path(".github/latex_engine_overrides.tsv"))
    parser.add_argument("--include", action="append", default=[], help="glob for roots to include")
    parser.add_argument("--exclude", action="append", default=[], help="glob for roots to exclude")
    parser.add_argument("--list-only", action="store_true")
    parser.add_argument("--strict", action="store_true", help="return 1 if any root fails")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    repo = args.repo.resolve()
    report_dir = (repo / args.report_dir).resolve() if not args.report_dir.is_absolute() else args.report_dir
    build_dir = (repo / args.build_dir).resolve() if not args.build_dir.is_absolute() else args.build_dir

    if shutil.which("latexmk") is None and not args.list_only:
        print("ERROR: latexmk is not installed", file=sys.stderr)
        return 2

    try:
        engine_overrides = load_engine_overrides(repo, args.engine_overrides)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    roots = discover_roots(
        repo,
        include_archive=args.include_archive,
        include_patterns=args.include,
        exclude_patterns=args.exclude,
    )
    if args.list_only:
        for root in roots:
            print(root.relative_to(repo).as_posix())
        print(f"Discovered {len(roots)} roots", file=sys.stderr)
        return 0

    # The report directory is intentionally atomic-per-run: remove every old
    # summary and failure log before compiling anything.
    shutil.rmtree(report_dir, ignore_errors=True)
    shutil.rmtree(build_dir, ignore_errors=True)
    work_dir = build_dir / "work"
    pdf_dir = build_dir / "pdfs"
    log_dir = report_dir / "logs"
    work_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    started_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    print(f"Discovered {len(roots)} standalone TeX roots; compiling with {args.jobs} workers")
    results: list[BuildResult] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        future_map = {
            pool.submit(
                compile_root,
                repo,
                root,
                work_dir,
                pdf_dir,
                log_dir,
                args.timeout,
                engine_overrides.get(root.relative_to(repo).as_posix()),
            ): root
            for root in roots
        }
        for index, future in enumerate(concurrent.futures.as_completed(future_map), start=1):
            root = future_map[future]
            try:
                result = future.result()
            except Exception as exc:  # Defensive: one Python error must not abort the batch.
                rel = root.relative_to(repo).as_posix()
                safe = _safe_name(rel)
                log_path = log_dir / f"{safe}.txt"
                log_path.write_text(f"Internal compiler exception for {rel}:\n{exc!r}\n", encoding="utf-8")
                result = BuildResult(
                    root=rel,
                    engine="unknown",
                    status="failed",
                    seconds=0.0,
                    returncode=None,
                    pdf=None,
                    log=_display_path(log_path, repo),
                    message=f"internal exception: {exc!r}",
                )
            results.append(result)
            marker = "OK" if result.succeeded else result.status.upper()
            print(f"[{index:03d}/{len(roots):03d}] {marker:7s} {result.root}")

    results.sort(key=lambda r: r.root.lower())
    write_reports(repo, report_dir, results, started_at, args.include_archive)
    failures = [result for result in results if not result.succeeded]
    print(f"Completed: {len(results) - len(failures)} success, {len(failures)} failed/timeout")
    if args.strict and failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
