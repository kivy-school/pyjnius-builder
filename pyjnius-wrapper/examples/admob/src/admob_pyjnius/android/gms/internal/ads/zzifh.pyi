from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IOException: ...  # java.io.IOException

class zzifh:
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: IOException) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: IOException) -> None: ...
