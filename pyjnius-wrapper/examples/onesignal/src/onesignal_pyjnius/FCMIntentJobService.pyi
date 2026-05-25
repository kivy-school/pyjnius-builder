from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Intent: ...  # android.content.Intent
class Context: ...  # android.content.Context

class FCMIntentJobService:
    BUNDLE_EXTRA: ClassVar[str]
    def __init__(self) -> None: ...
    def onHandleWork(self, arg0: Intent) -> None: ...
    @staticmethod
    def enqueueWork(arg0: Context, arg1: Intent) -> None: ...
