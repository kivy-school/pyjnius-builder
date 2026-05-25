from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class zzbib:
    @overload
    def __init__(self, arg0: Context) -> None: ...
    @overload
    def __init__(self) -> None: ...
