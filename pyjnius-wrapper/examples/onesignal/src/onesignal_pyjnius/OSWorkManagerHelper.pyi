from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class WorkManager: ...  # androidx.work.WorkManager

class OSWorkManagerHelper:
    INSTANCE: ClassVar["OSWorkManagerHelper"]
    @staticmethod
    def getInstance(arg0: Context) -> WorkManager: ...
