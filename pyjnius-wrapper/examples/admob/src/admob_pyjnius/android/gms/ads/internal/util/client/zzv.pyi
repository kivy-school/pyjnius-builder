from typing import Any, ClassVar, overload
from android.gms.ads.internal.util.client.zzx import zzx

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject: ...  # org.json.JSONObject

class zzv:
    def __init__(self) -> None: ...
    def zza(self) -> zzx: ...
    @staticmethod
    def zzb(arg0: JSONObject) -> "zzv": ...
