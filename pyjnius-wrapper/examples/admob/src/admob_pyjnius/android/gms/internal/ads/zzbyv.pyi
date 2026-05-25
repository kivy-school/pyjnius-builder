from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbnm import zzbnm
from android.gms.internal.ads.zzbnp import zzbnp

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OnCustomFormatAdLoadedListener: ...  # com.google.android.gms.ads.nativead.NativeCustomFormatAd.OnCustomFormatAdLoadedListener
class OnCustomClickListener: ...  # com.google.android.gms.ads.nativead.NativeCustomFormatAd.OnCustomClickListener

class zzbyv:
    def __init__(self, arg0: OnCustomFormatAdLoadedListener, arg1: OnCustomClickListener) -> None: ...
    def zza(self) -> zzbnp: ...
    def zzb(self) -> zzbnm: ...
