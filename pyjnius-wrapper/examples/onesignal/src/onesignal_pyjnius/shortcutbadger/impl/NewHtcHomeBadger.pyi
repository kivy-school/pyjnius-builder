from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class ComponentName: ...  # android.content.ComponentName

class NewHtcHomeBadger:
    INTENT_UPDATE_SHORTCUT: ClassVar[str]
    INTENT_SET_NOTIFICATION: ClassVar[str]
    PACKAGENAME: ClassVar[str]
    COUNT: ClassVar[str]
    EXTRA_COMPONENT: ClassVar[str]
    EXTRA_COUNT: ClassVar[str]
    def __init__(self) -> None: ...
    def executeBadge(self, arg0: Context, arg1: ComponentName, arg2: int) -> None: ...
    def getSupportLaunchers(self) -> list: ...
