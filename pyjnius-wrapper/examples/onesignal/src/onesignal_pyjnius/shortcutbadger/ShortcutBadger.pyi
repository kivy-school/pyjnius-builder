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
class Notification:
    """Forward declaration for ``android.app.Notification``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.app.Notification')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/app/Notification
    """
    ...

class ShortcutBadger:
    @staticmethod
    def applyCount(arg0: Context, arg1: int) -> bool: ...
    @staticmethod
    def applyCountOrThrow(arg0: Context, arg1: int) -> None: ...
    @staticmethod
    def removeCount(arg0: Context) -> bool: ...
    @staticmethod
    def removeCountOrThrow(arg0: Context) -> None: ...
    @staticmethod
    def isBadgeCounterSupported(arg0: Context) -> bool: ...
    @staticmethod
    def applyNotification(arg0: Context, arg1: Notification, arg2: int) -> None: ...
