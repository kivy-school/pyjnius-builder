from typing import Any, ClassVar, overload

class PackageInfoHelper:
    Companion: ClassVar["Companion"]
    def __init__(self) -> None: ...

    class Companion:
        def getInfo(self, arg0: "Context", arg1: str, arg2: int) -> "GetPackageInfoResult": ...
