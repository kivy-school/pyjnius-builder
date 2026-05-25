from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzm import zzm

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzfp:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: int
    zzc: zzm
    zzd: int
    zze: bool
    def __init__(self, arg0: str, arg1: int, arg2: zzm, arg3: int, arg4: bool) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def zza(self, arg0: int) -> "zzfp": ...
