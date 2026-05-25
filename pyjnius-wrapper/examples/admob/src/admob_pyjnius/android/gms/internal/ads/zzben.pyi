from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Parcel:
    """Forward declaration for ``android.os.Parcel``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcel')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcel
    """
    ...
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...
class Parcelable:
    """Forward declaration for ``android.os.Parcelable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable
    """
    ...
class IInterface:
    """Forward declaration for ``android.os.IInterface``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.IInterface')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/IInterface
    """
    ...

class zzben:
    @staticmethod
    def zza(arg0: Parcel) -> bool: ...
    @staticmethod
    def zzb(arg0: Parcel, arg1: Creator) -> Parcelable: ...
    @staticmethod
    def zzc(arg0: Parcel, arg1: Parcelable) -> None: ...
    @staticmethod
    def zzd(arg0: Parcel, arg1: Parcelable) -> None: ...
    @staticmethod
    def zze(arg0: Parcel, arg1: IInterface) -> None: ...
    @staticmethod
    def zzf(arg0: Parcel) -> list: ...
    @staticmethod
    def zzg(arg0: Parcel) -> dict: ...
    @staticmethod
    def zzh(arg0: Parcel) -> None: ...
