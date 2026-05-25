from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Intent: ...  # android.content.Intent

class FCMIntentService:
    def __init__(self) -> None: ...
    def onHandleIntent(self, arg0: Intent) -> None: ...
