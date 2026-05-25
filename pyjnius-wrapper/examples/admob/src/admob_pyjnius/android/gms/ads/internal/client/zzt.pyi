from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel
class JSONObject: ...  # org.json.JSONObject

class zzt:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: int
    zzc: str
    zzd: int
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: int) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    @staticmethod
    def zza(arg0: JSONObject) -> "zzt": ...
