from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Context: ...  # android.content.Context

class NavigateToAndroidSettingsForNotifications:
    INSTANCE: ClassVar["NavigateToAndroidSettingsForNotifications"]
    def show(self, arg0: Context) -> None: ...
