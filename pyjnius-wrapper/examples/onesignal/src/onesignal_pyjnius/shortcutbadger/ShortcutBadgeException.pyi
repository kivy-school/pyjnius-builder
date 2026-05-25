from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Exception: ...  # java.lang.Exception

class ShortcutBadgeException:
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: Exception) -> None: ...
