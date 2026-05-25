from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class View:
    """Forward declaration for ``android.view.View``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.View')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/View
    """
    ...
class LayoutParams:
    """Forward declaration for ``android.view.ViewGroup.LayoutParams``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.ViewGroup.LayoutParams')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/ViewGroup/LayoutParams
    """
    ...
class MotionEvent:
    """Forward declaration for ``android.view.MotionEvent``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.MotionEvent')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/MotionEvent
    """
    ...

class zzh:
    def addView(self, arg0: View, arg1: int, arg2: LayoutParams) -> None: ...
    def removeView(self, arg0: View) -> None: ...
    def removeAllViews(self) -> None: ...
    def bringChildToFront(self, arg0: View) -> None: ...
    def onVisibilityChanged(self, arg0: View, arg1: int) -> None: ...
    def dispatchTouchEvent(self, arg0: MotionEvent) -> bool: ...
