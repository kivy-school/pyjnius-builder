from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Extender: ...  # androidx.core.app.NotificationCompat.Extender

class OSMutableNotification:
    def setExtender(self, arg0: Extender) -> None: ...
    def setAndroidNotificationId(self, arg0: int) -> None: ...
