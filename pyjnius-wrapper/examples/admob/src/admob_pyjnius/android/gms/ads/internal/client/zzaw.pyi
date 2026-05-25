from typing import Any, ClassVar, overload
from android.gms.ads.h5.OnH5AdsEventListener import OnH5AdsEventListener
from android.gms.ads.internal.client.zzbq import zzbq
from android.gms.ads.internal.client.zzbu import zzbu
from android.gms.ads.internal.client.zzch import zzch
from android.gms.ads.internal.client.zzdt import zzdt
from android.gms.ads.internal.client.zzfc import zzfc
from android.gms.ads.internal.client.zzi import zzi
from android.gms.ads.internal.client.zzk import zzk
from android.gms.ads.internal.client.zzl import zzl
from android.gms.ads.internal.client.zzr import zzr
from android.gms.internal.ads.zzbmp import zzbmp
from android.gms.internal.ads.zzboe import zzboe
from android.gms.internal.ads.zzbof import zzbof
from android.gms.internal.ads.zzbra import zzbra
from android.gms.internal.ads.zzbvj import zzbvj
from android.gms.internal.ads.zzbzb import zzbzb
from android.gms.internal.ads.zzbzf import zzbzf
from android.gms.internal.ads.zzbzi import zzbzi
from android.gms.internal.ads.zzccp import zzccp
from android.gms.internal.ads.zzcdb import zzcdb
from android.gms.internal.ads.zzcet import zzcet

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
class FrameLayout:
    """Forward declaration for ``android.widget.FrameLayout``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.widget.FrameLayout')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/widget/FrameLayout
    """
    ...
class Activity:
    """Forward declaration for ``android.app.Activity``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.app.Activity')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/app/Activity
    """
    ...

class zzaw:
    def __init__(self, arg0: zzk, arg1: zzi, arg2: zzfc, arg3: zzboe, arg4: zzcdb, arg5: zzbzf, arg6: zzbof, arg7: zzl) -> None: ...
    def zza(self, arg0: Context, arg1: zzr, arg2: str, arg3: zzbvj) -> zzbu: ...
    def zzb(self, arg0: Context, arg1: zzr, arg2: str, arg3: zzbvj) -> zzbu: ...
    def zzc(self, arg0: Context, arg1: str, arg2: zzbvj) -> zzbq: ...
    def zzd(self, arg0: Context, arg1: zzbvj) -> zzch: ...
    def zze(self, arg0: Context, arg1: FrameLayout, arg2: FrameLayout) -> zzbmp: ...
    def zzf(self, arg0: Context, arg1: str, arg2: zzbvj) -> zzccp: ...
    def zzg(self, arg0: Activity) -> zzbzi: ...
    def zzh(self, arg0: Context, arg1: zzbvj) -> zzdt: ...
    def zzi(self, arg0: Context, arg1: zzbvj) -> zzcet: ...
    def zzj(self, arg0: Context, arg1: zzbvj) -> zzbzb: ...
    def zzk(self, arg0: Context, arg1: zzbvj, arg2: OnH5AdsEventListener) -> zzbra: ...
