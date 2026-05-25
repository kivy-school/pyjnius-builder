from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzeh import zzeh

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class AppOpenAdLoadCallback: ...  # com.google.android.gms.ads.appopen.AppOpenAd.AppOpenAdLoadCallback

class zzbgy:
    def __init__(self, arg0: Context, arg1: str, arg2: zzeh, arg3: AppOpenAdLoadCallback) -> None: ...
    def zza(self) -> None: ...
