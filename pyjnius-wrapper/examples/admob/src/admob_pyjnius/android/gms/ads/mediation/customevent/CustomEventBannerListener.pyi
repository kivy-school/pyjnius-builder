from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class View: ...  # android.view.View

class CustomEventBannerListener:
    def onAdLoaded(self, arg0: View) -> None: ...
