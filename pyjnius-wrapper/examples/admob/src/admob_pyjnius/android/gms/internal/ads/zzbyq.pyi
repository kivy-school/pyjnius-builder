from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbnc import zzbnc

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class View:
    """Forward declaration for ``android.view.View``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.View')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/View
    """
    ...

class zzbyq:
    def __init__(self, arg0: zzbnc) -> None: ...
    def start(self) -> bool: ...
    def setView(self, arg0: View) -> None: ...
