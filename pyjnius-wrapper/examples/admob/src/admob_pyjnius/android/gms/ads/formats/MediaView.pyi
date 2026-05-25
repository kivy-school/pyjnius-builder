from typing import Any, ClassVar, overload
from android.gms.ads.MediaContent import MediaContent

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context:
    """Forward declaration for ``android.content.Context``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.Context')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/Context
    """
    ...
class AttributeSet:
    """Forward declaration for ``android.util.AttributeSet``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.util.AttributeSet')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/util/AttributeSet
    """
    ...
class ScaleType:
    """Forward declaration for ``android.widget.ImageView.ScaleType``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.widget.ImageView.ScaleType')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/widget/ImageView/ScaleType
    """
    ...

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
