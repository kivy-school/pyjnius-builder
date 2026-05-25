from typing import Any, ClassVar, overload

class OSInAppMessage:
    IAM_ID: ClassVar[str]
    messageId: str
    def getMessageId(self) -> str: ...
    def toJSONObject(self) -> "JSONObject": ...
