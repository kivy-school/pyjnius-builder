from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbjs import zzbjs

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IBinder: ...  # android.os.IBinder

class zzbjr:
    @staticmethod
    def zzb(arg0: IBinder) -> zzbjs: ...
