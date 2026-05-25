from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Runnable: ...  # java.lang.Runnable

class CallbackThreadManager:
    Companion: ClassVar["Companion"]
    def __init__(self) -> None: ...

    class Companion:
        def getPreference(self) -> "UseThread": ...
        def setPreference(self, arg0: "UseThread") -> None: ...
        def runOnPreferred(self, arg0: Runnable) -> None: ...

        class WhenMappings:
            ...

    class UseThread:
        MainUI: ClassVar["UseThread"]
        Background: ClassVar["UseThread"]
        @staticmethod
        def values() -> list["UseThread"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "UseThread": ...
