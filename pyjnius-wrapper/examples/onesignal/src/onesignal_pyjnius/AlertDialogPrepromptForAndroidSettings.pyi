from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Activity:
    """Forward declaration for ``android.app.Activity``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.app.Activity')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/app/Activity
    """
    ...

class AlertDialogPrepromptForAndroidSettings:
    INSTANCE: ClassVar["AlertDialogPrepromptForAndroidSettings"]
    def show(self, arg0: Activity, arg1: str, arg2: str, arg3: "Callback") -> None: ...

    class Callback:
        def onAccept(self) -> None: ...
        def onDecline(self) -> None: ...
