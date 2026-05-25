from typing import Any, ClassVar, overload
from android.gms.ads.AdFormat import AdFormat
from android.gms.ads.AdRequest import AdRequest
from android.gms.ads.internal.client.zzex import zzex
from android.gms.ads.query.QueryInfoGenerationCallback import QueryInfoGenerationCallback

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle: ...  # android.os.Bundle
class Context: ...  # android.content.Context

class QueryInfo:
    def __init__(self, arg0: zzex) -> None: ...
    def getQuery(self) -> str: ...
    def getQueryBundle(self) -> Bundle: ...
    def getRequestId(self) -> str: ...
    @overload
    @staticmethod
    def generate(arg0: Context, arg1: AdFormat, arg2: AdRequest, arg3: QueryInfoGenerationCallback) -> None: ...
    @overload
    @staticmethod
    def generate(arg0: Context, arg1: AdFormat, arg2: AdRequest, arg3: str, arg4: QueryInfoGenerationCallback) -> None: ...
