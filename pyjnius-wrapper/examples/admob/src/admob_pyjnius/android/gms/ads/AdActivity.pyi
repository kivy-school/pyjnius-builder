from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle:
    """Forward declaration for ``android.os.Bundle``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Bundle')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Bundle
    """
    ...
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
class Intent:
    """Forward declaration for ``android.content.Intent``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.Intent')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/Intent
    """
    ...
class Configuration:
    """Forward declaration for ``android.content.res.Configuration``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.res.Configuration')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/res/Configuration
    """
    ...

class AdActivity:
    CLASS_NAME: ClassVar[str]
    def __init__(self) -> None: ...
    def onCreate(self, arg0: Bundle) -> None: ...
    def onRestart(self) -> None: ...
    def onStart(self) -> None: ...
    def onUserLeaveHint(self) -> None: ...
    def onResume(self) -> None: ...
    def onPause(self) -> None: ...
    def onSaveInstanceState(self, arg0: Bundle) -> None: ...
    def onStop(self) -> None: ...
    def onDestroy(self) -> None: ...
    @overload
    def setContentView(self, arg0: int) -> None: ...
    @overload
    def setContentView(self, arg0: View) -> None: ...
    @overload
    def setContentView(self, arg0: View, arg1: LayoutParams) -> None: ...
    def onBackPressed(self) -> None: ...
    def onActivityResult(self, arg0: int, arg1: int, arg2: Intent) -> None: ...
    def onConfigurationChanged(self, arg0: Configuration) -> None: ...
    def onRequestPermissionsResult(self, arg0: int, arg1: list[str], arg2: list[int]) -> None: ...
