from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbsa import zzbsa

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IBinder: ...  # android.os.IBinder
class Parcel: ...  # android.os.Parcel

class zzbrz:
    def __init__(self) -> None: ...
    @staticmethod
    def zzb(arg0: IBinder) -> zzbsa: ...
    def zzdd(self, arg0: int, arg1: Parcel, arg2: Parcel, arg3: int) -> bool: ...
