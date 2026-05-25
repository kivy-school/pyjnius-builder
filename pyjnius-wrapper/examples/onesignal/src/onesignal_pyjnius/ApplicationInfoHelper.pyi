from typing import Any, ClassVar, overload

class ApplicationInfoHelper:
    Companion: ClassVar["Companion"]
    def __init__(self) -> None: ...

    class Companion:
        def getInfo(self, arg0: "Context") -> "ApplicationInfo": ...
