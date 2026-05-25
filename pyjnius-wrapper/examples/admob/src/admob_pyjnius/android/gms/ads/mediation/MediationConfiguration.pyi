from typing import Any, ClassVar, overload
from android.gms.ads.AdFormat import AdFormat

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Bundle: ...  # android.os.Bundle

class MediationConfiguration:
    CUSTOM_EVENT_SERVER_PARAMETER_FIELD: ClassVar[str]
    def __init__(self, arg0: AdFormat, arg1: Bundle) -> None: ...
    def getFormat(self) -> AdFormat: ...
    def getServerParameters(self) -> Bundle: ...
