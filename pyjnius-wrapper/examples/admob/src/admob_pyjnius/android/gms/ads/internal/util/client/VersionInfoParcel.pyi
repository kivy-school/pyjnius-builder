from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...
class Parcel:
    """Forward declaration for ``android.os.Parcel``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcel')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcel
    """
    ...

class VersionInfoParcel:
    CREATOR: ClassVar[Creator]
    afmaVersion: str
    buddyApkVersion: int
    clientJarVersion: int
    isClientJar: bool
    isLiteSdk: bool
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool, arg3: bool) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: bool) -> None: ...
    @staticmethod
    def forPackage() -> "VersionInfoParcel": ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
