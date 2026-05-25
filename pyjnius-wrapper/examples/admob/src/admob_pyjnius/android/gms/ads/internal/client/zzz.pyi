from typing import Any, ClassVar, overload
from android.gms.ads.AdSize import AdSize

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class AttributeSet: ...  # android.util.AttributeSet

class zzz:
    def __init__(self, arg0: Context, arg1: AttributeSet) -> None: ...
    def zza(self, arg0: bool) -> list[AdSize]: ...
    def zzb(self) -> str: ...
