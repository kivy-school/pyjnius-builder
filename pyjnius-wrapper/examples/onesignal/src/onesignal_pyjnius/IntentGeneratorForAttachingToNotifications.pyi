from typing import Any, ClassVar, overload

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
class Intent:
    """Forward declaration for ``android.content.Intent``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.Intent')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/Intent
    """
    ...
class PendingIntent:
    """Forward declaration for ``android.app.PendingIntent``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.app.PendingIntent')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/app/PendingIntent
    """
    ...

class IntentGeneratorForAttachingToNotifications:
    def __init__(self, arg0: Context) -> None: ...
    def getContext(self) -> Context: ...
    def getNewBaseIntent(self, arg0: int) -> Intent: ...
    def getNewActionPendingIntent(self, arg0: int, arg1: Intent) -> PendingIntent: ...
