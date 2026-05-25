from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Throwable: ...  # java.lang.Throwable

class OneSignalApiResponseHandler:
    def onSuccess(self, arg0: str) -> None: ...
    def onFailure(self, arg0: int, arg1: str, arg2: Throwable) -> None: ...
