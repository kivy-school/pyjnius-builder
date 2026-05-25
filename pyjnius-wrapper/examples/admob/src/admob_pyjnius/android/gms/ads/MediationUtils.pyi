from typing import Any, ClassVar, overload
from android.gms.ads.AdSize import AdSize

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class MediationUtils:
    def __init__(self) -> None: ...
    @staticmethod
    def findClosestSize(arg0: Context, arg1: AdSize, arg2: list) -> AdSize: ...
