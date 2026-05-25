from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class SharedPreferences: ...  # android.content.SharedPreferences

class zzbiq:
    def __init__(self) -> None: ...
    @staticmethod
    def zza(arg0: Context) -> SharedPreferences: ...
    @staticmethod
    def zzb(arg0: Context) -> SharedPreferences: ...
