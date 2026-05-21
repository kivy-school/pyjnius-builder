# pyjnius-builder
A PEP 517 build backend implementation developed for Pyjnius based packages.

Use `tool.pyjnius.java_paths` in `pyproject.toml` to include Java source folders in built distributions under
`.java/` (for wheels this becomes `site-packages/.java`).

```toml
[tool.pyjnius]
java-paths = [
    "root/path/to/java"
]
```
