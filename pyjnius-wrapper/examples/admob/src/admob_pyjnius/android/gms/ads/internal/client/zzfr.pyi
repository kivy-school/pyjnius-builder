from typing import Any, ClassVar, overload

class zzfr:
    CREATOR: ClassVar["Creator"]
    zza: int
    zzb: int
    @overload
    def __init__(self, arg0: int, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: "RequestConfiguration") -> None: ...
    def writeToParcel(self, arg0: "Parcel", arg1: int) -> None: ...
