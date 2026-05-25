from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Runnable: ...  # java.lang.Runnable

class OSBackgroundManager:
    def __init__(self) -> None: ...
    def runRunnableOnThread(self, arg0: Runnable, arg1: str) -> None: ...
