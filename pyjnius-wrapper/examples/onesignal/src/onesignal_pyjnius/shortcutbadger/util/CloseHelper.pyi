from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Cursor: ...  # android.database.Cursor
class Closeable: ...  # java.io.Closeable

class CloseHelper:
    def __init__(self) -> None: ...
    @staticmethod
    def close(arg0: Cursor) -> None: ...
    @staticmethod
    def closeQuietly(arg0: Closeable) -> None: ...
