from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzidl import zzidl
from android.gms.internal.ads.zzidp import zzidp
from android.gms.internal.ads.zzidz import zzidz

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class InputStream: ...  # java.io.InputStream

class zzigh:
    def zzc(self, arg0: zzidp, arg1: zzidz) -> Any: ...
    def zzb(self, arg0: zzidl, arg1: zzidz) -> Any: ...
    def zza(self, arg0: InputStream, arg1: zzidz) -> Any: ...
