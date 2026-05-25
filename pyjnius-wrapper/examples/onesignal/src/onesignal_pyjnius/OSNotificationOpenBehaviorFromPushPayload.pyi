from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class JSONObject: ...  # org.json.JSONObject
class Uri: ...  # android.net.Uri

class OSNotificationOpenBehaviorFromPushPayload:
    def __init__(self, arg0: Context, arg1: JSONObject) -> None: ...
    def getShouldOpenApp(self) -> bool: ...
    def getUri(self) -> Uri: ...
