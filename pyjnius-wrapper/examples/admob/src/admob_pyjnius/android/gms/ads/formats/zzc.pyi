from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class WeakHashMap: ...  # java.util.WeakHashMap

class zzc:
    zza: ClassVar[WeakHashMap]
