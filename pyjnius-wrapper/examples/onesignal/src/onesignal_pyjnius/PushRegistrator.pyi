from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class PushRegistrator:
    def registerForPush(self, arg0: Context, arg1: str, arg2: "RegisteredHandler") -> None: ...

    class RegisteredHandler:
        def complete(self, arg0: str, arg1: int) -> None: ...
