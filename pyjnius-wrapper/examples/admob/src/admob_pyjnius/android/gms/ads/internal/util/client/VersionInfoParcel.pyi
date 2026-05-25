from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

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
