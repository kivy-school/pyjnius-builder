from typing import Any, ClassVar, overload
from android.gms.ads.mediation.MediationNativeListener import MediationNativeListener
from android.gms.ads.mediation.NativeMediationAdRequest import NativeMediationAdRequest

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

class MediationNativeAdapter:
    def requestNativeAd(self, arg0: Context, arg1: MediationNativeListener, arg2: Bundle, arg3: NativeMediationAdRequest, arg4: Bundle) -> None: ...
