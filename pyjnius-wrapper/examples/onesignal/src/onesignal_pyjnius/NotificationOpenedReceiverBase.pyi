from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle: ...  # android.os.Bundle
class Intent: ...  # android.content.Intent

class NotificationOpenedReceiverBase:
    def __init__(self) -> None: ...
    def onCreate(self, arg0: Bundle) -> None: ...
    def onNewIntent(self, arg0: Intent) -> None: ...
