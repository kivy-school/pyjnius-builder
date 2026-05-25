from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzeh import zzeh
from android.gms.ads.internal.client.zzm import zzm

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class zzq:
    zza: ClassVar["zzq"]
    def __init__(self) -> None: ...
    def zza(self, arg0: Context, arg1: zzeh) -> zzm: ...
