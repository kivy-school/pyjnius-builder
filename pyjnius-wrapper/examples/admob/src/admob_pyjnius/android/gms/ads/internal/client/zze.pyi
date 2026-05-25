from typing import Any, ClassVar, overload
from android.gms.ads.AdError import AdError
from android.gms.ads.LoadAdError import LoadAdError

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...
class IBinder:
    """Forward declaration for ``android.os.IBinder``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.IBinder')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/IBinder
    """
    ...
class Parcel:
    """Forward declaration for ``android.os.Parcel``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcel')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcel
    """
    ...

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
