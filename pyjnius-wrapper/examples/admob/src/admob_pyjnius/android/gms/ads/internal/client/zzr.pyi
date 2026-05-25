from typing import Any, ClassVar, overload
from android.gms.ads.AdSize import AdSize

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
class Context:
    """Forward declaration for ``android.content.Context``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.Context')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/Context
    """
    ...
class DisplayMetrics:
    """Forward declaration for ``android.util.DisplayMetrics``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.util.DisplayMetrics')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/util/DisplayMetrics
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

class zzr:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: int
    zzc: int
    zzd: bool
    zze: int
    zzf: int
    zzg: list["zzr"]
    zzh: bool
    zzi: bool
    zzj: bool
    zzk: bool
    zzl: bool
    zzm: bool
    zzn: bool
    zzo: bool
    zzp: bool
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AdSize) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: list[AdSize]) -> None: ...
    @staticmethod
    def zza(arg0: DisplayMetrics) -> int: ...
    @staticmethod
    def zzb() -> "zzr": ...
    @staticmethod
    def zzc() -> "zzr": ...
    @staticmethod
    def zzd() -> "zzr": ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
