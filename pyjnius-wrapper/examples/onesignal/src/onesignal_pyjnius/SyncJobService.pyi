from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JobParameters:
    """Forward declaration for ``android.app.job.JobParameters``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.app.job.JobParameters')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/app/job/JobParameters
    """
    ...

class SyncJobService:
    def __init__(self) -> None: ...
    def onStartJob(self, arg0: JobParameters) -> bool: ...
    def onStopJob(self, arg0: JobParameters) -> bool: ...
