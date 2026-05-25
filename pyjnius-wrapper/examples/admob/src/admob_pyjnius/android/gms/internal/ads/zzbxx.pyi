from typing import Any, ClassVar, overload
from android.gms.ads.VersionInfo import VersionInfo

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzbxx:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: int
    zzc: int
    @staticmethod
    def zza(arg0: VersionInfo) -> "zzbxx": ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def toString(self) -> str: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
