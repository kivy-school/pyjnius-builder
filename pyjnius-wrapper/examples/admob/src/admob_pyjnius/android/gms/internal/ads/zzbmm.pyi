from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbml import zzbml

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Drawable:
    """Forward declaration for ``android.graphics.drawable.Drawable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.drawable.Drawable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/drawable/Drawable
    """
    ...
class Uri:
    """Forward declaration for ``android.net.Uri``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.net.Uri')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/net/Uri
    """
    ...

class zzbmm:
    def __init__(self, arg0: zzbml) -> None: ...
    def getDrawable(self) -> Drawable: ...
    def getUri(self) -> Uri: ...
    def getScale(self) -> float: ...
    def zza(self) -> int: ...
    def zzb(self) -> int: ...
