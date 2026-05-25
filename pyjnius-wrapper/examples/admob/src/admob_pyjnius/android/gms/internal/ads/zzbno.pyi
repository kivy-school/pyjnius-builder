from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbnp import zzbnp

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IBinder: ...  # android.os.IBinder
class Parcel: ...  # android.os.Parcel

class zzbno:
    def __init__(self) -> None: ...
    @staticmethod
    def zzb(arg0: IBinder) -> zzbnp: ...
    def zzdd(self, arg0: int, arg1: Parcel, arg2: Parcel, arg3: int) -> bool: ...
