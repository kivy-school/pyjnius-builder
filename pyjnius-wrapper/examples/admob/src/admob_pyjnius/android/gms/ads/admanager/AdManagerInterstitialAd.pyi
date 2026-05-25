from typing import Any, ClassVar, overload
from android.gms.ads.admanager.AdManagerAdRequest import AdManagerAdRequest
from android.gms.ads.admanager.AdManagerInterstitialAdLoadCallback import AdManagerInterstitialAdLoadCallback
from android.gms.ads.admanager.AppEventListener import AppEventListener

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context:
    """Forward declaration for ``android.content.Context``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.Context')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/Context
    """
    ...

class AdManagerInterstitialAd:
    def __init__(self) -> None: ...
    @staticmethod
    def load(arg0: Context, arg1: str, arg2: AdManagerAdRequest, arg3: AdManagerInterstitialAdLoadCallback) -> None: ...
    def getAppEventListener(self) -> AppEventListener: ...
    def setAppEventListener(self, arg0: AppEventListener) -> None: ...
