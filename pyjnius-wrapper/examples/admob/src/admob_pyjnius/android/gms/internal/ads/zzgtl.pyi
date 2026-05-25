from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class StringBuilder: ...  # java.lang.StringBuilder
class Iterable: ...  # java.lang.Iterable
class Iterator: ...  # java.util.Iterator

class zzgtl:
    @staticmethod
    def zzb(arg0: StringBuilder, arg1: Iterable, arg2: str) -> StringBuilder: ...
    @staticmethod
    def zzc(arg0: StringBuilder, arg1: Iterator, arg2: str) -> StringBuilder: ...
    @staticmethod
    def zzd(arg0: Iterable, arg1: str) -> str: ...
