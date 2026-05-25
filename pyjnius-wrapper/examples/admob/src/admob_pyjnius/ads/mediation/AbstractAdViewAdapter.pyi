from typing import Any, ClassVar, overload
from android.gms.ads.AdSize import AdSize
from android.gms.ads.AdView import AdView
from android.gms.ads.internal.client.zzea import zzea
from android.gms.ads.interstitial.InterstitialAd import InterstitialAd
from android.gms.ads.mediation.MediationAdRequest import MediationAdRequest
from android.gms.ads.mediation.MediationBannerListener import MediationBannerListener
from android.gms.ads.mediation.MediationInterstitialListener import MediationInterstitialListener
from android.gms.ads.mediation.MediationNativeListener import MediationNativeListener
from android.gms.ads.mediation.NativeMediationAdRequest import NativeMediationAdRequest

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle:
    """Forward declaration for ``android.os.Bundle``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Bundle')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Bundle
    """
    ...
class Context:
    """Forward declaration for ``android.content.Context``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.Context')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/Context
    """
    ...
class View:
    """Forward declaration for ``android.view.View``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.View')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/View
    """
    ...

class AbstractAdViewAdapter:
    AD_UNIT_ID_PARAMETER: ClassVar[str]
    mAdView: AdView
    mInterstitialAd: InterstitialAd
    def __init__(self) -> None: ...
    def buildExtrasBundle(self, arg0: Bundle, arg1: Bundle) -> Bundle: ...
    def onDestroy(self) -> None: ...
    def onPause(self) -> None: ...
    def onResume(self) -> None: ...
    def getAdUnitId(self, arg0: Bundle) -> str: ...
    def requestBannerAd(self, arg0: Context, arg1: MediationBannerListener, arg2: Bundle, arg3: AdSize, arg4: MediationAdRequest, arg5: Bundle) -> None: ...
    def getBannerView(self) -> View: ...
    def requestInterstitialAd(self, arg0: Context, arg1: MediationInterstitialListener, arg2: Bundle, arg3: MediationAdRequest, arg4: Bundle) -> None: ...
    def onImmersiveModeUpdated(self, arg0: bool) -> None: ...
    def showInterstitial(self) -> None: ...
    def requestNativeAd(self, arg0: Context, arg1: MediationNativeListener, arg2: Bundle, arg3: NativeMediationAdRequest, arg4: Bundle) -> None: ...
    def getVideoController(self) -> zzea: ...
