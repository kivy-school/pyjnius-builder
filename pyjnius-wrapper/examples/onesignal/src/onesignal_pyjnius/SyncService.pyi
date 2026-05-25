from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Intent: ...  # android.content.Intent
class IBinder: ...  # android.os.IBinder

class SyncService:
    def __init__(self) -> None: ...
    def onStartCommand(self, arg0: Intent, arg1: int, arg2: int) -> int: ...
    def onBind(self, arg0: Intent) -> IBinder: ...
