from typing import Any, ClassVar, overload
from android.gms.ads.admanager.AdManagerAdRequest import AdManagerAdRequest
from android.gms.ads.admanager.AdManagerInterstitialAdLoadCallback import AdManagerInterstitialAdLoadCallback
from android.gms.ads.admanager.AppEventListener import AppEventListener

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class AdManagerInterstitialAd:
    def __init__(self) -> None: ...
    @staticmethod
    def load(arg0: Context, arg1: str, arg2: AdManagerAdRequest, arg3: AdManagerInterstitialAdLoadCallback) -> None: ...
    def getAppEventListener(self) -> AppEventListener: ...
    def setAppEventListener(self, arg0: AppEventListener) -> None: ...
