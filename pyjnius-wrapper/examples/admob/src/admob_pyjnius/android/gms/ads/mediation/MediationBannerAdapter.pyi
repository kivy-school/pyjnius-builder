from typing import Any, ClassVar, overload
from android.gms.ads.AdSize import AdSize
from android.gms.ads.mediation.MediationAdRequest import MediationAdRequest
from android.gms.ads.mediation.MediationBannerListener import MediationBannerListener

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context
class Bundle: ...  # android.os.Bundle
class View: ...  # android.view.View

class MediationBannerAdapter:
    def requestBannerAd(self, arg0: Context, arg1: MediationBannerListener, arg2: Bundle, arg3: AdSize, arg4: MediationAdRequest, arg5: Bundle) -> None: ...
    def getBannerView(self) -> View: ...
