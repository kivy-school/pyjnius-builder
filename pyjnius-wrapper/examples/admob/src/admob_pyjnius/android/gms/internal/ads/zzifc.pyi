from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ByteBuffer: ...  # java.nio.ByteBuffer

class zzifc:
    zza: ClassVar[list[int]]
    zzb: ClassVar[ByteBuffer]
    @staticmethod
    def zza() -> int: ...
    @staticmethod
    def zzb(arg0: bool) -> int: ...
