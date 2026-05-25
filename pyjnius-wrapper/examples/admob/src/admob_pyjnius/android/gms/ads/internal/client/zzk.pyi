from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzbu import zzbu
from android.gms.ads.internal.client.zzr import zzr
from android.gms.internal.ads.zzbvj import zzbvj

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class zzk:
    def __init__(self) -> None: ...
    def zza(self, arg0: Context, arg1: zzr, arg2: str, arg3: zzbvj, arg4: int) -> zzbu: ...
