from typing import Any, ClassVar, overload
from android.gms.ads.MediaContent import MediaContent

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class AttributeSet: ...  # android.util.AttributeSet
class ScaleType: ...  # android.widget.ImageView.ScaleType

class MediaView:
    @overload
    def __init__(self, arg0: Context) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet, arg2: int) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet, arg2: int, arg3: int) -> None: ...
    def setMediaContent(self, arg0: MediaContent) -> None: ...
    def setImageScaleType(self, arg0: ScaleType) -> None: ...
