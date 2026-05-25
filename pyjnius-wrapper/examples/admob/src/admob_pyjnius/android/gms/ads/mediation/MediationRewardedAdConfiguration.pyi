from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Bundle: ...  # android.os.Bundle
class Location: ...  # android.location.Location

class MediationRewardedAdConfiguration:
    def __init__(self, arg0: Context, arg1: str, arg2: Bundle, arg3: Bundle, arg4: bool, arg5: Location, arg6: int, arg7: int, arg8: str, arg9: str) -> None: ...
