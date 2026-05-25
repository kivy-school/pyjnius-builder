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

class zzex:
    def __init__(self, arg0: str, arg1: Bundle, arg2: str) -> None: ...
    def zza(self) -> str: ...
    def zzb(self) -> str: ...
    def zzc(self) -> Bundle: ...
