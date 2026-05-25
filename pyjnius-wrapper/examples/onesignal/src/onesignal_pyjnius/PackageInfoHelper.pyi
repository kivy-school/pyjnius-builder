from typing import Any, ClassVar, overload
from GetPackageInfoResult import GetPackageInfoResult

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class PackageInfoHelper:
    Companion: ClassVar["Companion"]
    def __init__(self) -> None: ...

    class Companion:
        def getInfo(self, arg0: Context, arg1: str, arg2: int) -> GetPackageInfoResult: ...
