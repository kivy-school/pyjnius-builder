from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class zzee:
    CREATOR: ClassVar[Creator]
    zza: int
    def __init__(self, arg0: int) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
