from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbmp import zzbmp

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class FrameLayout: ...  # android.widget.FrameLayout

class zzboe:
    def __init__(self) -> None: ...
    def zza(self, arg0: Context, arg1: FrameLayout, arg2: FrameLayout) -> zzbmp: ...
