from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Intent: ...  # android.content.Intent

class BroadcastHelper:
    def __init__(self) -> None: ...
    @staticmethod
    def canResolveBroadcast(arg0: Context, arg1: Intent) -> bool: ...
    @staticmethod
    def resolveBroadcast(arg0: Context, arg1: Intent) -> list: ...
    @staticmethod
    def sendIntentExplicitly(arg0: Context, arg1: Intent) -> None: ...
