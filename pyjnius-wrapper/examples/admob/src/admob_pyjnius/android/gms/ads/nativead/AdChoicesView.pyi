from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class AttributeSet: ...  # android.util.AttributeSet

class AdChoicesView:
    @overload
    def __init__(self, arg0: Context) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet, arg2: int) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet, arg2: int, arg3: int) -> None: ...
