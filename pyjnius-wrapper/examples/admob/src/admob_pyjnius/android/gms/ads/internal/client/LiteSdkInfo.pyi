from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzez import zzez
from android.gms.internal.ads.zzbvj import zzbvj

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class LiteSdkInfo:
    def __init__(self, arg0: Context) -> None: ...
    def getLiteSdkVersion(self) -> zzez: ...
    def getAdapterCreator(self) -> zzbvj: ...
