from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Callable: ...  # java.util.concurrent.Callable

class zzcb:
    @staticmethod
    def zza(arg0: Context, arg1: Callable) -> Any: ...
