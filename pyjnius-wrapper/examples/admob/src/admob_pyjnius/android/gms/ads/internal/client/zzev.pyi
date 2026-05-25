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
class ProviderInfo:
    """Forward declaration for ``android.content.pm.ProviderInfo``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.pm.ProviderInfo')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/pm/ProviderInfo
    """
    ...
class Uri:
    """Forward declaration for ``android.net.Uri``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.net.Uri')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/net/Uri
    """
    ...
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

class zzev:
    def __init__(self) -> None: ...
    def attachInfo(self, arg0: Context, arg1: ProviderInfo) -> None: ...
    def onCreate(self) -> bool: ...
    def query(self, arg0: Uri, arg1: list[str], arg2: str, arg3: list[str], arg4: str) -> Cursor: ...
    def getType(self, arg0: Uri) -> str: ...
    def insert(self, arg0: Uri, arg1: ContentValues) -> Uri: ...
    def delete(self, arg0: Uri, arg1: str, arg2: list[str]) -> int: ...
    def update(self, arg0: Uri, arg1: ContentValues, arg2: str, arg3: list[str]) -> int: ...
