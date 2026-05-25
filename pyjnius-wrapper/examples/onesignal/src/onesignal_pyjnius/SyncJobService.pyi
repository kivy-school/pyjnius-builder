from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JobParameters: ...  # android.app.job.JobParameters

class SyncJobService:
    def __init__(self) -> None: ...
    def onStartJob(self, arg0: JobParameters) -> bool: ...
    def onStopJob(self, arg0: JobParameters) -> bool: ...
