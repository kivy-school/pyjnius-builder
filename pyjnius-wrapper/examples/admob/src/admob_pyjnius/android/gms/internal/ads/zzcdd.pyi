from typing import Any, ClassVar, overload
from android.gms.ads.rewarded.ServerSideVerificationOptions import ServerSideVerificationOptions

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzcdd:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: str
    @overload
    def __init__(self, arg0: ServerSideVerificationOptions) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
