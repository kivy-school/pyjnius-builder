from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class ApplicationInfo: ...  # android.content.pm.ApplicationInfo

class ApplicationInfoHelper:
    Companion: ClassVar["Companion"]
    def __init__(self) -> None: ...

    class Companion:
        def getInfo(self, arg0: Context) -> ApplicationInfo: ...
