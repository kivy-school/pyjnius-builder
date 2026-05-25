from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject: ...  # org.json.JSONObject

class OSInAppMessage:
    IAM_ID: ClassVar[str]
    messageId: str
    def getMessageId(self) -> str: ...
    def toJSONObject(self) -> JSONObject: ...
