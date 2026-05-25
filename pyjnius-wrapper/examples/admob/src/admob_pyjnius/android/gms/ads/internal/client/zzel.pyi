from typing import Any, ClassVar, overload
from android.gms.ads.appopen.AppOpenAd import AppOpenAd

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class zzel:
    def __init__(self, arg0: Context) -> None: ...
    def zza(self, arg0: str) -> AppOpenAd: ...
