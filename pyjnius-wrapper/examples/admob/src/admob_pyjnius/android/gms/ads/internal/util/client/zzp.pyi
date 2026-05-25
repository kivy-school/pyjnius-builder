from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle: ...  # android.os.Bundle

class zzp:
    @staticmethod
    def zza(arg0: Bundle, arg1: Bundle) -> bool: ...
