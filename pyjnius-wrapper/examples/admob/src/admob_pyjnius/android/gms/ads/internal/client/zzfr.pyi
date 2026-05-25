from typing import Any, ClassVar, overload
from android.gms.ads.RequestConfiguration import RequestConfiguration

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzfr:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: int
    @overload
    def __init__(self, arg0: int, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: RequestConfiguration) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
