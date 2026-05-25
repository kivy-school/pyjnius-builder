from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Looper: ...  # android.os.Looper
class Message: ...  # android.os.Message

class zzgax:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Looper) -> None: ...
    def dispatchMessage(self, arg0: Message) -> None: ...
    def zza(self, arg0: Message) -> None: ...
