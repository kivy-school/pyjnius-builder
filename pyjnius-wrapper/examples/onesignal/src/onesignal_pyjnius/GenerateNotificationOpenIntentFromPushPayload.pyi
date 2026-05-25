from typing import Any, ClassVar, overload
from GenerateNotificationOpenIntent import GenerateNotificationOpenIntent

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class JSONObject: ...  # org.json.JSONObject

class GenerateNotificationOpenIntentFromPushPayload:
    INSTANCE: ClassVar["GenerateNotificationOpenIntentFromPushPayload"]
    def create(self, arg0: Context, arg1: JSONObject) -> GenerateNotificationOpenIntent: ...
