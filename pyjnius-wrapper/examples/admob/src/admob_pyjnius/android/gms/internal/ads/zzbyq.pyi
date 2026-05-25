from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbnc import zzbnc

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class View: ...  # android.view.View

class zzbyq:
    def __init__(self, arg0: zzbnc) -> None: ...
    def start(self) -> bool: ...
    def setView(self, arg0: View) -> None: ...
