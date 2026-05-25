from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle: ...  # android.os.Bundle
class RemoteMessage: ...  # com.huawei.hms.push.RemoteMessage

class HmsMessageServiceOneSignal:
    def __init__(self) -> None: ...
    @overload
    def onNewToken(self, arg0: str, arg1: Bundle) -> None: ...
    @overload
    def onNewToken(self, arg0: str) -> None: ...
    def onMessageReceived(self, arg0: RemoteMessage) -> None: ...
