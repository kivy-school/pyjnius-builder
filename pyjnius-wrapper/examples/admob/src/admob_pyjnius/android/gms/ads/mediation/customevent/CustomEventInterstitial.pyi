from typing import Any, ClassVar, overload
from android.gms.ads.mediation.MediationAdRequest import MediationAdRequest
from android.gms.ads.mediation.customevent.CustomEventInterstitialListener import CustomEventInterstitialListener

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Bundle: ...  # android.os.Bundle

class CustomEventInterstitial:
    def requestInterstitialAd(self, arg0: Context, arg1: CustomEventInterstitialListener, arg2: str, arg3: MediationAdRequest, arg4: Bundle) -> None: ...
    def showInterstitial(self) -> None: ...
