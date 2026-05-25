from typing import Any, ClassVar, overload
from android.gms.ads.VideoOptions import VideoOptions

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzfw:
    CREATOR: ClassVar[Creator]
    zza: bool
    zzb: bool
    zzc: bool
    @overload
    def __init__(self, arg0: VideoOptions) -> None: ...
    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: bool) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
