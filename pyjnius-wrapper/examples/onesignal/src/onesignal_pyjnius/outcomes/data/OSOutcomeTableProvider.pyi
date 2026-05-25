from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class SQLiteDatabase:
    """Forward declaration for ``android.database.sqlite.SQLiteDatabase``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.database.sqlite.SQLiteDatabase')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase
    """
    ...

class OSOutcomeTableProvider:
    def __init__(self) -> None: ...
    def upgradeOutcomeTableRevision1To2(self, arg0: SQLiteDatabase) -> None: ...
    def upgradeOutcomeTableRevision2To3(self, arg0: SQLiteDatabase) -> None: ...
    def upgradeCacheOutcomeTableRevision1To2(self, arg0: SQLiteDatabase) -> None: ...
