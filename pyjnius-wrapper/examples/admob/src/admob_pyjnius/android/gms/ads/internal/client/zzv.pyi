from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zze import zze

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Bundle: ...  # android.os.Bundle
class Parcel: ...  # android.os.Parcel

class zzv:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: int
    zzc: zze
    zzd: Bundle
    zze: str
    zzf: str
    zzg: str
    zzh: str
    def __init__(self, arg0: str, arg1: int, arg2: zze, arg3: Bundle, arg4: str, arg5: str, arg6: str, arg7: str) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
