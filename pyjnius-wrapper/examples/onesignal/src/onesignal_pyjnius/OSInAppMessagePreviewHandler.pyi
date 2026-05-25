from typing import Any, ClassVar, overload

class OSInAppMessagePreviewHandler:
    INSTANCE: ClassVar["OSInAppMessagePreviewHandler"]
    @staticmethod
    def notificationReceived(arg0: "Context", arg1: "Bundle") -> bool: ...
    @staticmethod
    def notificationOpened(arg0: "Activity", arg1: "JSONObject") -> bool: ...
    @staticmethod
    def inAppPreviewPushUUID(arg0: "JSONObject") -> str: ...
