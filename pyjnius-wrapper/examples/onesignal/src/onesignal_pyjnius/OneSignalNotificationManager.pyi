from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class OneSignalNotificationManager:
    def __init__(self) -> None: ...
    @staticmethod
    def areNotificationsEnabled(arg0: Context, arg1: str) -> bool: ...
