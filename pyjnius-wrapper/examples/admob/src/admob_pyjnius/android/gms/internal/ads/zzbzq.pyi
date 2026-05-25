from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbzr import zzbzr

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IBinder: ...  # android.os.IBinder

class zzbzq:
    @staticmethod
    def zzb(arg0: IBinder) -> zzbzr: ...
