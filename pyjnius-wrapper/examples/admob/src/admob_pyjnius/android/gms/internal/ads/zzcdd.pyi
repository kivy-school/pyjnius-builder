from typing import Any, ClassVar, overload

class zzcdd:
    CREATOR: ClassVar["Creator"]
    zza: str
    zzb: str
    @overload
    def __init__(self, arg0: "ServerSideVerificationOptions") -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str) -> None: ...
    def writeToParcel(self, arg0: "Parcel", arg1: int) -> None: ...
