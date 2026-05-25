from typing import Any, ClassVar, overload
from android.gms.ads.AdError import AdError
from android.gms.ads.LoadAdError import LoadAdError

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class IBinder: ...  # android.os.IBinder
class Parcel: ...  # android.os.Parcel

class zze:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: str
    zzc: str
    zzd: "zze"
    zze: IBinder
    def __init__(self, arg0: int, arg1: str, arg2: str, arg3: "zze", arg4: IBinder) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def zza(self) -> AdError: ...
    def zzb(self) -> LoadAdError: ...
