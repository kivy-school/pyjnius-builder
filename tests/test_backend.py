from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from pyjnius_builder.backend import (
    _read_pyproject_java_paths,
    add_java_sources_to_wheel,
    get_java_source_dirs,
)


class TestBackendJavaSourceDirs(unittest.TestCase):
    def test_reads_java_paths_from_pyproject_and_config_settings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pyproject = root / "pyproject.toml"
            pyproject.write_text(
                """
[tool.pyjnius-builder]
java_paths = ["java_from_pyproject"]
""".strip(),
                encoding="utf-8",
            )
            (root / "java_from_pyproject").mkdir()
            (root / "java_from_config").mkdir()

            result = get_java_source_dirs(
                config_settings={"java_paths": "java_from_config"},
                project_root=root,
            )

            self.assertEqual(
                result,
                [
                    (root / "java_from_pyproject").resolve(),
                    (root / "java_from_config").resolve(),
                ],
            )

    def test_deduplicates_repeated_java_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pyproject = root / "pyproject.toml"
            pyproject.write_text(
                """
[tool.pyjnius-builder]
java_paths = ["java_src"]
""".strip(),
                encoding="utf-8",
            )
            (root / "java_src").mkdir()

            result = get_java_source_dirs(
                config_settings={"java_paths": ["java_src", "java_src"]},
                project_root=root,
            )

            self.assertEqual(result, [(root / "java_src").resolve()])

    def test_adds_java_sources_to_dot_java_folder_in_wheel(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            java_dir = root / "java_src"
            (java_dir / "org/example").mkdir(parents=True)
            (java_dir / "org/example/Test.java").write_text("class Test {}", encoding="utf-8")
            wheel_path = root / "pkg-0.1-py3-none-any.whl"

            with zipfile.ZipFile(wheel_path, "w") as wheel:
                wheel.writestr("existing.txt", "ok")

            add_java_sources_to_wheel(wheel_path, [java_dir])

            with zipfile.ZipFile(wheel_path) as wheel:
                names = set(wheel.namelist())
                self.assertIn(".java/org/example/Test.java", names)
                self.assertEqual(wheel.read(".java/org/example/Test.java"), b"class Test {}")

    def test_returns_empty_when_tomllib_is_unavailable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "pyproject.toml").write_text(
                """
[tool.pyjnius-builder]
java_paths = ["java_src"]
""".strip(),
                encoding="utf-8",
            )

            original_import = __import__

            def import_side_effect(name, *args, **kwargs):
                if name == "tomllib":
                    raise ImportError("tomllib unavailable")
                return original_import(name, *args, **kwargs)

            with patch("builtins.__import__", side_effect=import_side_effect):
                self.assertEqual(_read_pyproject_java_paths(root), [])


if __name__ == "__main__":
    unittest.main()
