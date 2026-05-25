from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle: ...  # android.os.Bundle

class zzceq:
    def zzb(self, arg0: str) -> None: ...
    def zzc(self, arg0: str, arg1: str, arg2: Bundle) -> None: ...
