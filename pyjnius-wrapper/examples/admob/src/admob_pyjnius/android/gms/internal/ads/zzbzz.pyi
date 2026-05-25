from typing import Any, ClassVar, overload
from android.gms.ads.AdFormat import AdFormat
from android.gms.ads.internal.client.zzeh import zzeh
from android.gms.ads.query.QueryInfoGenerationCallback import QueryInfoGenerationCallback
from android.gms.internal.ads.zzcet import zzcet

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

class zzbzz:
    def __init__(self, arg0: Context, arg1: AdFormat, arg2: zzeh, arg3: str) -> None: ...
    @staticmethod
    def zza(arg0: Context) -> zzcet: ...
    def zzb(self, arg0: QueryInfoGenerationCallback) -> None: ...
