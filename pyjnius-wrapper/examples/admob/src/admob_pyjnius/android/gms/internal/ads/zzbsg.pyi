from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Bundle: ...  # android.os.Bundle
class Parcel: ...  # android.os.Parcel

class zzbsg:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: Bundle
    def __init__(self, arg0: str, arg1: Bundle) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
