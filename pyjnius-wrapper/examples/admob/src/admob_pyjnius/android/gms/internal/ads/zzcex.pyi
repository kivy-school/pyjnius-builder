from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzm import zzm
from android.gms.ads.internal.client.zzr import zzr

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzcex:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: str
    zzc: zzr
    zzd: zzm
    def __init__(self, arg0: str, arg1: str, arg2: zzr, arg3: zzm) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
