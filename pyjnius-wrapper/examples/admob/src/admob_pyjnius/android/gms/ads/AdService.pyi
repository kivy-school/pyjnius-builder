from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Intent:
    """Forward declaration for ``android.content.Intent``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.Intent')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/Intent
    """
    ...

class AdService:
    CLASS_NAME: ClassVar[str]
    def __init__(self) -> None: ...
    def onHandleIntent(self, arg0: Intent) -> None: ...
