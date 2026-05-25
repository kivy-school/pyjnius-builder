from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class WorkerParameters: ...  # androidx.work.WorkerParameters
class Result: ...  # androidx.work.ListenableWorker.Result

class OfflinePingSender:
    def __init__(self, arg0: Context, arg1: WorkerParameters) -> None: ...
    def doWork(self) -> Result: ...
