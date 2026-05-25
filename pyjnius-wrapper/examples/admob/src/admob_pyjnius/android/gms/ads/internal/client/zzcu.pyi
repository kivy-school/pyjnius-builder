from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzcv import zzcv

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IBinder: ...  # android.os.IBinder
class Parcel: ...  # android.os.Parcel

class zzcu:
    def __init__(self) -> None: ...
    @staticmethod
    def asInterface(arg0: IBinder) -> zzcv: ...
    def zzdd(self, arg0: int, arg1: Parcel, arg2: Parcel, arg3: int) -> bool: ...
