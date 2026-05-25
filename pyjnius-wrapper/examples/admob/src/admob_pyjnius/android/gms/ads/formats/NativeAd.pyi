from typing import Any, ClassVar, overload

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

class NativeAd:
    ASSET_ADCHOICES_CONTAINER_VIEW: ClassVar[str]
    def __init__(self) -> None: ...
    def performClick(self, arg0: Bundle) -> None: ...
    def recordImpression(self, arg0: Bundle) -> bool: ...
    def reportTouchEvent(self, arg0: Bundle) -> None: ...

    class AdChoicesInfo:
        def __init__(self) -> None: ...
        def getText(self) -> str: ...
        def getImages(self) -> list: ...

    class Image:
        def __init__(self) -> None: ...
        def getDrawable(self) -> Drawable: ...
        def getUri(self) -> Uri: ...
        def getScale(self) -> float: ...
        def zza(self) -> int: ...
        def zzb(self) -> int: ...
