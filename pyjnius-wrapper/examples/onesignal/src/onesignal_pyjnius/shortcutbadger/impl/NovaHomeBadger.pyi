from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class ComponentName: ...  # android.content.ComponentName

class NovaHomeBadger:
    def __init__(self) -> None: ...
    def executeBadge(self, arg0: Context, arg1: ComponentName, arg2: int) -> None: ...
    def getSupportLaunchers(self) -> list: ...
