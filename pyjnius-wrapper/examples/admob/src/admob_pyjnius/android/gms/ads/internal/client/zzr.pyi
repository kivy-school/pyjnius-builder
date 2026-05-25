from typing import Any, ClassVar, overload

class zzr:
    CREATOR: ClassVar["Creator"]
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
    def __init__(self, arg0: "Context", arg1: "AdSize") -> None: ...
    @overload
    def __init__(self, arg0: "Context", arg1: list["AdSize"]) -> None: ...
    @staticmethod
    def zza(arg0: "DisplayMetrics") -> int: ...
    @staticmethod
    def zzb() -> "zzr": ...
    @staticmethod
    def zzc() -> "zzr": ...
    @staticmethod
    def zzd() -> "zzr": ...
    def writeToParcel(self, arg0: "Parcel", arg1: int) -> None: ...
