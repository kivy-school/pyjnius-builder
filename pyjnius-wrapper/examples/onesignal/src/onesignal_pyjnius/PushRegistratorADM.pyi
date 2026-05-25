from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class RegisteredHandler: ...  # com.onesignal.PushRegistrator.RegisteredHandler

class PushRegistratorADM:
    def __init__(self) -> None: ...
    def registerForPush(self, arg0: Context, arg1: str, arg2: RegisteredHandler) -> None: ...
    @staticmethod
    def fireCallback(arg0: str) -> None: ...
