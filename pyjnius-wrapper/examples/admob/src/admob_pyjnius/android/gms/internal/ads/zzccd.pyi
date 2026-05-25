from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzm import zzm

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzccd:
    CREATOR: ClassVar[Creator]
    zza: zzm
    zzb: str
    def __init__(self, arg0: zzm, arg1: str) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
