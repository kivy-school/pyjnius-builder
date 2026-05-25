from typing import Any, ClassVar, overload

class zzbma:
    CREATOR: ClassVar["Creator"]
    zza: int
    zzb: bool
    zzc: int
    zzd: bool
    zze: int
    zzf: "zzfw"
    zzg: bool
    zzh: int
    zzi: int
    zzj: bool
    zzk: int
    @overload
    def __init__(self, arg0: "NativeAdOptions") -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: bool, arg2: int, arg3: bool, arg4: int, arg5: "zzfw", arg6: bool, arg7: int, arg8: int, arg9: bool, arg10: int) -> None: ...
    def writeToParcel(self, arg0: "Parcel", arg1: int) -> None: ...
    @staticmethod
    def zza(arg0: "zzbma") -> "NativeAdOptions": ...
