from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Throwable: ...  # java.lang.Throwable

class zzgun:
    @staticmethod
    def zza(arg0: Throwable, arg1: type) -> None: ...
    @staticmethod
    def zzb(arg0: Throwable) -> None: ...
