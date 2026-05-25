from typing import Any, ClassVar, overload
from android.gms.ads.mediation.NativeMediationAdRequest import NativeMediationAdRequest
from android.gms.ads.mediation.customevent.CustomEventNativeListener import CustomEventNativeListener

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Bundle: ...  # android.os.Bundle

class CustomEventNative:
    def requestNativeAd(self, arg0: Context, arg1: CustomEventNativeListener, arg2: str, arg3: NativeMediationAdRequest, arg4: Bundle) -> None: ...
