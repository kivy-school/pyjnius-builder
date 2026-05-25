from typing import Any, ClassVar, overload
from android.gms.ads.VideoController import VideoController

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class AttributeSet: ...  # android.util.AttributeSet

class AdView:
    @overload
    def __init__(self, arg0: Context) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet, arg2: int) -> None: ...
    def zza(self) -> VideoController: ...
