from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Looper:
    """Forward declaration for ``android.os.Looper``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Looper')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Looper
    """
    ...
class Message:
    """Forward declaration for ``android.os.Message``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Message')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Message
    """
    ...

class zzgax:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Looper) -> None: ...
    def dispatchMessage(self, arg0: Message) -> None: ...
    def zza(self, arg0: Message) -> None: ...
