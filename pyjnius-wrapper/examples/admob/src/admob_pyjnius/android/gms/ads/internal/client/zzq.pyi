from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzeh import zzeh
from android.gms.ads.internal.client.zzm import zzm

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context:
    """Forward declaration for ``android.content.Context``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.Context')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/Context
    """
    ...

class zzq:
    zza: ClassVar["zzq"]
    def __init__(self) -> None: ...
    def zza(self, arg0: Context, arg1: zzeh) -> zzm: ...
