from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Intent: ...  # android.content.Intent

class GenerateNotificationOpenIntent:
    def __init__(self, arg0: Context, arg1: Intent, arg2: bool) -> None: ...
    def getIntentVisible(self) -> Intent: ...
