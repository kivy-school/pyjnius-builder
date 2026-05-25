from typing import Any, ClassVar, overload

class OneSignalHmsEventBridge:
    HMS_TTL_KEY: ClassVar[str]
    HMS_SENT_TIME_KEY: ClassVar[str]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def onNewToken(arg0: "Context", arg1: str, arg2: "Bundle") -> None: ...
    @overload
    @staticmethod
    def onNewToken(arg0: "Context", arg1: str) -> None: ...
    @staticmethod
    def onMessageReceived(arg0: "Context", arg1: "RemoteMessage") -> None: ...
