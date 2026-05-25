from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzr import zzr
from android.gms.internal.ads.zzbvj import zzbvj

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IObjectWrapper: ...  # com.google.android.gms.dynamic.IObjectWrapper
class IBinder: ...  # android.os.IBinder

class zzbv:
    def zze(self, arg0: IObjectWrapper, arg1: zzr, arg2: str, arg3: zzbvj, arg4: int, arg5: int) -> IBinder: ...
