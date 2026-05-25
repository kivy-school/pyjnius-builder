from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzccp import zzccp

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IBinder: ...  # android.os.IBinder
class Parcel: ...  # android.os.Parcel

class zzcco:
    def __init__(self) -> None: ...
    @staticmethod
    def zzt(arg0: IBinder) -> zzccp: ...
    def zzdd(self, arg0: int, arg1: Parcel, arg2: Parcel, arg3: int) -> bool: ...
