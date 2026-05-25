from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbvj import zzbvj

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IObjectWrapper: ...  # com.google.android.gms.dynamic.IObjectWrapper
class IBinder: ...  # android.os.IBinder

class zzci:
    def zze(self, arg0: IObjectWrapper, arg1: zzbvj, arg2: int) -> IBinder: ...
