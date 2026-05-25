from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class OSNotificationOpenAppSettings:
    INSTANCE: ClassVar["OSNotificationOpenAppSettings"]
    def getShouldOpenActivity(self, arg0: Context) -> bool: ...
    def getSuppressLaunchURL(self, arg0: Context) -> bool: ...
