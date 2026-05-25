from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Throwable: ...  # java.lang.Throwable

class zzguo:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Throwable) -> None: ...
