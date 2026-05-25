from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class zzbii:
    @staticmethod
    def zza(arg0: Context) -> None: ...
    @staticmethod
    def zzb(arg0: Context) -> None: ...
    @staticmethod
    def zzc(arg0: Context) -> int: ...
    @staticmethod
    def zzd(arg0: Context) -> int: ...
    @staticmethod
    def zze(arg0: Context) -> None: ...
