from typing import Any, ClassVar, overload

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
class Bundle:
    """Forward declaration for ``android.os.Bundle``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Bundle')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Bundle
    """
    ...
class Location:
    """Forward declaration for ``android.location.Location``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.location.Location')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/location/Location
    """
    ...

class MediationAdConfiguration:
    TAG_FOR_CHILD_DIRECTED_TREATMENT_TRUE: ClassVar[int]
    TAG_FOR_CHILD_DIRECTED_TREATMENT_FALSE: ClassVar[int]
    TAG_FOR_CHILD_DIRECTED_TREATMENT_UNSPECIFIED: ClassVar[int]
    def __init__(self, arg0: Context, arg1: str, arg2: Bundle, arg3: Bundle, arg4: bool, arg5: Location, arg6: int, arg7: int, arg8: str, arg9: str) -> None: ...
    def getBidResponse(self) -> str: ...
    def getServerParameters(self) -> Bundle: ...
    def getMediationExtras(self) -> Bundle: ...
    def getContext(self) -> Context: ...
    def taggedForChildDirectedTreatment(self) -> int: ...
    def isTestRequest(self) -> bool: ...
    def taggedForUnderAgeTreatment(self) -> int: ...
    def getMaxAdContentRating(self) -> str: ...
    def getWatermark(self) -> str: ...

    class TagForChildDirectedTreatment:
        ...
