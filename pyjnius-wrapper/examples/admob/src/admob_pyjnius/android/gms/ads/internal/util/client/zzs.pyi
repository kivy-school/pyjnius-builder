from typing import Any, ClassVar, overload
from android.gms.ads.internal.util.client.zzq import zzq

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class zzs:
    @staticmethod
    def zza(arg0: Context, arg1: str, arg2: zzq) -> Any: ...
    @staticmethod
    def zzb(arg0: Context) -> Context: ...
