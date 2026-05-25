from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IObjectWrapper: ...  # com.google.android.gms.dynamic.IObjectWrapper
class Throwable: ...  # java.lang.Throwable

class zzbvg:
    @staticmethod
    def zza(arg0: IObjectWrapper, arg1: Throwable, arg2: str) -> None: ...
