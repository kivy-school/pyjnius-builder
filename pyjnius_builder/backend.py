from __future__ import annotations

from json import JSONDecodeError
from pathlib import Path
import json
import tarfile
import tempfile
import zipfile

from setuptools import build_meta as _setuptools_build_meta

try:
    import tomllib as _tomllib
except ImportError:  # pragma: no cover
    _tomllib = None

_SDIST_SPOOL_MAX_SIZE = 1024 * 1024


def _flatten_paths(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        raw_values = [value]
    elif isinstance(value, (list, tuple)):
        raw_values = [str(item) for item in value]
    else:
        raw_values = [str(value)]

    paths: list[str] = []
    for raw in raw_values:
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, list):
                paths.extend(str(item).strip() for item in parsed if str(item).strip())
                continue
        except (JSONDecodeError, TypeError, ValueError):
            pass

        paths.extend(part.strip() for part in raw.split(",") if part.strip())
    return paths


def _read_pyproject_java_paths(project_root: Path) -> list[str]:
    pyproject = project_root / "pyproject.toml"
    if not pyproject.exists():
        return []

    if _tomllib is None:
        return []
    data = _tomllib.loads(pyproject.read_text(encoding="utf-8"))
    tool_data = data.get("tool", {}).get("pyjnius-builder", {})
    return _flatten_paths(tool_data.get("java_paths"))


def get_java_source_dirs(config_settings=None, project_root: Path | None = None) -> list[Path]:
    root = Path.cwd() if project_root is None else Path(project_root)
    config_settings = config_settings or {}

    configured_paths = _read_pyproject_java_paths(root)
    configured_paths.extend(
        _flatten_paths(config_settings.get("java_paths"))
        + _flatten_paths(config_settings.get("java-paths"))
        + _flatten_paths(config_settings.get("java-path"))
        + _flatten_paths(config_settings.get("pyjnius-builder.java_paths"))
    )

    unique_paths: list[Path] = []
    seen: set[Path] = set()
    for configured_path in configured_paths:
        path = (root / configured_path).resolve()
        if path in seen:
            continue
        if not path.exists():
            raise FileNotFoundError(
                f"Configured java path does not exist: {configured_path} (resolved to {path})"
            )
        if not path.is_dir():
            raise NotADirectoryError(
                f"Configured java path is not a directory: {configured_path} (resolved to {path})"
            )
        seen.add(path)
        unique_paths.append(path)
    return unique_paths


def _collect_java_files(java_dirs: list[Path]) -> list[tuple[Path, str]]:
    java_files: list[tuple[Path, str]] = []
    for source_dir in java_dirs:
        for source_file in source_dir.rglob("*"):
            if not source_file.is_file():
                continue
            rel = source_file.relative_to(source_dir).as_posix()
            java_files.append((source_file, f".java/{rel}"))
    return java_files


def add_java_sources_to_wheel(wheel_path: Path, java_dirs: list[Path]) -> None:
    if not java_dirs:
        return
    java_files = _collect_java_files(java_dirs)
    if not java_files:
        return
    with zipfile.ZipFile(wheel_path, "a", compression=zipfile.ZIP_DEFLATED) as wheel:
        for source_file, archive_name in java_files:
            wheel.writestr(archive_name, source_file.read_bytes())


def add_java_sources_to_sdist(sdist_path: Path, java_dirs: list[Path]) -> None:
    if not java_dirs:
        return
    java_files = _collect_java_files(java_dirs)
    if not java_files:
        return

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_sdist_path = Path(tmpdir) / "rewritten.tar.gz"
        with tarfile.open(sdist_path, "r:gz") as source_tar:
            members = source_tar.getmembers()
            root_prefix = members[0].name.split("/", 1)[0] if members else ""

            with tarfile.open(temp_sdist_path, "w:gz") as new_tar:
                for member in members:
                    file_obj = source_tar.extractfile(member) if member.isfile() else None
                    new_tar.addfile(member, file_obj)
                for source_file, archive_name in java_files:
                    tar_info = tarfile.TarInfo(
                        name=f"{root_prefix}/{archive_name}" if root_prefix else archive_name
                    )
                    file_bytes = source_file.read_bytes()
                    tar_info.size = len(file_bytes)
                    with tempfile.SpooledTemporaryFile(max_size=_SDIST_SPOOL_MAX_SIZE) as spooled:
                        spooled.write(file_bytes)
                        spooled.seek(0)
                        new_tar.addfile(tar_info, spooled)

        temp_sdist_path.replace(sdist_path)


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    java_dirs = get_java_source_dirs(config_settings=config_settings)
    wheel_name = _setuptools_build_meta.build_wheel(
        wheel_directory=wheel_directory,
        config_settings=config_settings,
        metadata_directory=metadata_directory,
    )
    add_java_sources_to_wheel(Path(wheel_directory) / wheel_name, java_dirs)
    return wheel_name


def build_sdist(sdist_directory, config_settings=None):
    java_dirs = get_java_source_dirs(config_settings=config_settings)
    sdist_name = _setuptools_build_meta.build_sdist(
        sdist_directory=sdist_directory,
        config_settings=config_settings,
    )
    add_java_sources_to_sdist(Path(sdist_directory) / sdist_name, java_dirs)
    return sdist_name


def get_requires_for_build_wheel(config_settings=None):
    return _setuptools_build_meta.get_requires_for_build_wheel(config_settings=config_settings)


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    return _setuptools_build_meta.prepare_metadata_for_build_wheel(
        metadata_directory=metadata_directory,
        config_settings=config_settings,
    )


def get_requires_for_build_sdist(config_settings=None):
    return _setuptools_build_meta.get_requires_for_build_sdist(config_settings=config_settings)
