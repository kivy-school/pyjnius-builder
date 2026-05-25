from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbio import zzbio

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
class SharedPreferences:
    """Forward declaration for ``android.content.SharedPreferences``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.SharedPreferences')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/SharedPreferences
    """
    ...

class zzbiv:
    def __init__(self) -> None: ...
    def zza(self, arg0: Context) -> None: ...
    def zzc(self) -> bool: ...
    def zzd(self, arg0: zzbio) -> Any: ...
    def zze(self, arg0: zzbio) -> Any: ...
    def onSharedPreferenceChanged(self, arg0: SharedPreferences, arg1: str) -> None: ...
