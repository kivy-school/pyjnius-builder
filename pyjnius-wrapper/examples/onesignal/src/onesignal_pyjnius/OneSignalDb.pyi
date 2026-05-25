from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Cursor:
    """Forward declaration for ``android.database.Cursor``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.database.Cursor')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/database/Cursor
    """
    ...
class ContentValues:
    """Forward declaration for ``android.content.ContentValues``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.ContentValues')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/ContentValues
    """
    ...

class OneSignalDb:
    @overload
    def query(self, arg0: str, arg1: list[str], arg2: str, arg3: list[str], arg4: str, arg5: str, arg6: str) -> Cursor: ...
    @overload
    def query(self, arg0: str, arg1: list[str], arg2: str, arg3: list[str], arg4: str, arg5: str, arg6: str, arg7: str) -> Cursor: ...
    def insert(self, arg0: str, arg1: str, arg2: ContentValues) -> None: ...
    def insertOrThrow(self, arg0: str, arg1: str, arg2: ContentValues) -> None: ...
    def update(self, arg0: str, arg1: ContentValues, arg2: str, arg3: list[str]) -> int: ...
    def delete(self, arg0: str, arg1: str, arg2: list[str]) -> None: ...
