from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IObjectWrapper: ...  # com.google.android.gms.dynamic.IObjectWrapper

class zzdr:
    def zze(self, arg0: str, arg1: IObjectWrapper, arg2: IObjectWrapper) -> None: ...
