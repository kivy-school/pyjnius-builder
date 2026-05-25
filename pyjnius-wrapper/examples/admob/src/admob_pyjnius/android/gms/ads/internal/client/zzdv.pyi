from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzv import zzv

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle:
    """Forward declaration for ``android.os.Bundle``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Bundle')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Bundle
    """
    ...

class zzdv:
    def zze(self) -> str: ...
    def zzf(self) -> str: ...
    def zzg(self) -> list: ...
    def zzh(self) -> zzv: ...
    def zzi(self) -> Bundle: ...
    def zzj(self) -> str: ...
