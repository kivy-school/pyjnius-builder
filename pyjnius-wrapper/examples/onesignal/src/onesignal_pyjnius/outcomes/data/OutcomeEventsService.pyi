from typing import Any, ClassVar, overload
from OneSignalApiResponseHandler import OneSignalApiResponseHandler

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject: ...  # org.json.JSONObject

class OutcomeEventsService:
    def sendOutcomeEvent(self, arg0: JSONObject, arg1: OneSignalApiResponseHandler) -> None: ...
