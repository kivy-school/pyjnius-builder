from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class JSONArray: ...  # org.json.JSONArray
class Parcel: ...  # android.os.Parcel

class zzcci:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: int
    def __init__(self, arg0: str, arg1: int) -> None: ...
    @staticmethod
    def zza(arg0: JSONArray) -> "zzcci": ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
