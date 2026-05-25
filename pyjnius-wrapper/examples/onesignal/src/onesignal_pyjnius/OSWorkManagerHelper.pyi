from typing import Any, ClassVar, overload

class OSWorkManagerHelper:
    INSTANCE: ClassVar["OSWorkManagerHelper"]
    @staticmethod
    def getInstance(arg0: "Context") -> "WorkManager": ...
