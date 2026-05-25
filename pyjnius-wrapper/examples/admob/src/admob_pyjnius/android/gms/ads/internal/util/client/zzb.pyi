from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ThreadPoolExecutor: ...  # java.util.concurrent.ThreadPoolExecutor
class ExecutorService: ...  # java.util.concurrent.ExecutorService

class zzb:
    zza: ClassVar[ThreadPoolExecutor]
    zzb: ClassVar[ExecutorService]
