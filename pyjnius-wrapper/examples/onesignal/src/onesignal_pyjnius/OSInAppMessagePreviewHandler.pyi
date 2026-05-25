from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Bundle: ...  # android.os.Bundle
class Activity: ...  # android.app.Activity
class JSONObject: ...  # org.json.JSONObject

class OSInAppMessagePreviewHandler:
    INSTANCE: ClassVar["OSInAppMessagePreviewHandler"]
    @staticmethod
    def notificationReceived(arg0: Context, arg1: Bundle) -> bool: ...
    @staticmethod
    def notificationOpened(arg0: Activity, arg1: JSONObject) -> bool: ...
    @staticmethod
    def inAppPreviewPushUUID(arg0: JSONObject) -> str: ...
