from typing import Any, ClassVar, overload
from OneSignalAPIClient import OneSignalAPIClient
from OneSignalApiResponseHandler import OneSignalApiResponseHandler

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject: ...  # org.json.JSONObject

class OSOutcomeEventsClient:
    def __init__(self, arg0: OneSignalAPIClient) -> None: ...
    def getClient(self) -> OneSignalAPIClient: ...
    def sendOutcomeEvent(self, arg0: JSONObject, arg1: OneSignalApiResponseHandler) -> None: ...
