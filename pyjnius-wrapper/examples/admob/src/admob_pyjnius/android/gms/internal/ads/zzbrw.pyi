from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzbrw:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: bool
    zzc: int
    zzd: str
    def __init__(self, arg0: str, arg1: bool, arg2: int, arg3: str) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
