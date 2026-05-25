from typing import Any, ClassVar, overload
from android.gms.ads.nativead.NativeAdOptions import NativeAdOptions
from android.gms.internal.ads.zzbma import zzbma

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
class Bundle:
    """Forward declaration for ``android.os.Bundle``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Bundle')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Bundle
    """
    ...
class Location:
    """Forward declaration for ``android.location.Location``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.location.Location')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/location/Location
    """
    ...

class MediationNativeAdConfiguration:
    def __init__(self, arg0: Context, arg1: str, arg2: Bundle, arg3: Bundle, arg4: bool, arg5: Location, arg6: int, arg7: int, arg8: str, arg9: str, arg10: zzbma) -> None: ...
    def getNativeAdOptions(self) -> NativeAdOptions: ...
