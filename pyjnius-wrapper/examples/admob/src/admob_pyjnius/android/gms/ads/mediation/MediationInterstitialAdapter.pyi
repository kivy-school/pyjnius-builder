from typing import Any, ClassVar, overload
from android.gms.ads.mediation.MediationAdRequest import MediationAdRequest
from android.gms.ads.mediation.MediationInterstitialListener import MediationInterstitialListener

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Bundle: ...  # android.os.Bundle

class MediationInterstitialAdapter:
    def requestInterstitialAd(self, arg0: Context, arg1: MediationInterstitialListener, arg2: Bundle, arg3: MediationAdRequest, arg4: Bundle) -> None: ...
    def showInterstitial(self) -> None: ...
