from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class NavigateToAndroidSettingsForLocation:
    INSTANCE: ClassVar["NavigateToAndroidSettingsForLocation"]
    def show(self, arg0: Context) -> None: ...
