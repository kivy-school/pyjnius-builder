from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbio import zzbio

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Editor:
    """Forward declaration for ``android.content.SharedPreferences.Editor``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.SharedPreferences.Editor')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/SharedPreferences/Editor
    """
    ...
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class zzbip:
    def __init__(self) -> None: ...
    def zza(self, arg0: zzbio) -> None: ...
    def zzb(self, arg0: zzbio) -> None: ...
    def zzc(self, arg0: zzbio) -> None: ...
    def zzd(self, arg0: Editor, arg1: int, arg2: JSONObject) -> None: ...
    def zze(self) -> list: ...
    def zzf(self) -> list: ...
