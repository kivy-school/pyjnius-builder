from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class View: ...  # android.view.View
class IBinder: ...  # android.os.IBinder
class Parcel: ...  # android.os.Parcel

class zzcaa:
    CREATOR: ClassVar[Creator]
    zza: View
    zzb: dict
    def __init__(self, arg0: IBinder, arg1: IBinder) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
