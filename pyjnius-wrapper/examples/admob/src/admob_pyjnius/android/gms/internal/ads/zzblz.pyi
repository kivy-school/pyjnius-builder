from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ScaleType:
    """Forward declaration for ``android.widget.ImageView.ScaleType``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.widget.ImageView.ScaleType')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/widget/ImageView/ScaleType
    """
    ...

class zzblz:
    def zza(self, arg0: ScaleType) -> None: ...
