from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Notification: ...  # android.app.Notification

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
