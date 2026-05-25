from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Activity: ...  # android.app.Activity

class AlertDialogPrepromptForAndroidSettings:
    INSTANCE: ClassVar["AlertDialogPrepromptForAndroidSettings"]
    def show(self, arg0: Activity, arg1: str, arg2: str, arg3: "Callback") -> None: ...

    class Callback:
        def onAccept(self) -> None: ...
        def onDecline(self) -> None: ...
