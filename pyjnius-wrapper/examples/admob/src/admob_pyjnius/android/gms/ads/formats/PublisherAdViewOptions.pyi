from typing import Any, ClassVar, overload
from android.gms.ads.formats.ShouldDelayBannerRenderingListener import ShouldDelayBannerRenderingListener
from android.gms.ads.internal.client.zzcl import zzcl

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator: ...  # android.os.Parcelable.Creator
class Parcel: ...  # android.os.Parcel

class PublisherAdViewOptions:
    CREATOR: ClassVar[Creator]
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def zza(self) -> bool: ...
    def zzb(self) -> zzcl: ...

    class Builder:
        def __init__(self) -> None: ...
        def setShouldDelayBannerRenderingListener(self, arg0: ShouldDelayBannerRenderingListener) -> "Builder": ...
