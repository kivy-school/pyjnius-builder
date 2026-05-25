from typing import Any, ClassVar, overload
from android.gms.ads.mediation.MediationNativeListener import MediationNativeListener
from android.gms.ads.mediation.NativeMediationAdRequest import NativeMediationAdRequest

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Bundle: ...  # android.os.Bundle

class MediationNativeAdapter:
    def requestNativeAd(self, arg0: Context, arg1: MediationNativeListener, arg2: Bundle, arg3: NativeMediationAdRequest, arg4: Bundle) -> None: ...
