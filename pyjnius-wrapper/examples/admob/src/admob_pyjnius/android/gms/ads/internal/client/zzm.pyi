from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzc import zzc
from android.gms.ads.internal.client.zzft import zzft

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
class Bundle:
    """Forward declaration for ``android.os.Bundle``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Bundle')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Bundle
    """
    ...
class Location:
    """Forward declaration for ``android.location.Location``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.location.Location')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/location/Location
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

class zzm:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: int
    zzc: Bundle
    zzd: int
    zze: list
    zzf: bool
    zzg: int
    zzh: bool
    zzi: str
    zzj: zzft
    zzk: Location
    zzl: str
    zzm: Bundle
    zzn: Bundle
    zzo: list
    zzp: str
    zzq: str
    zzr: bool
    zzs: zzc
    zzt: int
    zzu: str
    zzv: list
    zzw: int
    zzx: str
    zzy: int
    zzz: int
    zzA: int
    zzB: int
    zzC: Bundle
    def __init__(self, arg0: int, arg1: int, arg2: Bundle, arg3: int, arg4: list, arg5: bool, arg6: int, arg7: bool, arg8: str, arg9: zzft, arg10: Location, arg11: str, arg12: Bundle, arg13: Bundle, arg14: list, arg15: str, arg16: str, arg17: bool, arg18: zzc, arg19: int, arg20: str, arg21: list, arg22: int, arg23: str, arg24: int, arg25: int, arg26: int, arg27: int) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def equals(self, arg0: Any) -> bool: ...
    def zza(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def zzb(self) -> bool: ...
    def zzc(self) -> bool: ...
    def zzd(self) -> bool: ...
