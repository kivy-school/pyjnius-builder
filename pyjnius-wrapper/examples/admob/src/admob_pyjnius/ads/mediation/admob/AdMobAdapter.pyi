from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle: ...  # android.os.Bundle

class AdMobAdapter:
    NEW_BUNDLE: ClassVar[str]
    def __init__(self) -> None: ...
    def buildExtrasBundle(self, arg0: Bundle, arg1: Bundle) -> Bundle: ...
