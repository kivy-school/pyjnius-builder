from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbrd import zzbrd

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IBinder: ...  # android.os.IBinder

class zzbrc:
    @staticmethod
    def zzb(arg0: IBinder) -> zzbrd: ...
