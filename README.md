# pyjnius-builder
A PEP 517 build backend implementation developed for Pyjnius based packages.

Use `tool.pyjnius-builder.java_paths` in `pyproject.toml` (or `config_settings` key
`java_paths`) to include Java source folders in built distributions under
`.java/` (for wheels this becomes `site-packages/.java`).
