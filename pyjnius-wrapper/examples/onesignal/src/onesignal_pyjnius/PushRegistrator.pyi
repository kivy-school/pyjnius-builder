from typing import Any, ClassVar, overload

class PushRegistrator:
    def registerForPush(self, arg0: "Context", arg1: str, arg2: "RegisteredHandler") -> None: ...

    class RegisteredHandler:
        def complete(self, arg0: str, arg1: int) -> None: ...
