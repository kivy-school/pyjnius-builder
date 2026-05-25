from typing import Any, ClassVar, overload

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
class WebView:
    """Forward declaration for ``android.webkit.WebView``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.WebView')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/WebView
    """
    ...
class WebViewClient:
    """Forward declaration for ``android.webkit.WebViewClient``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.WebViewClient')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/WebViewClient
    """
    ...

class H5AdsWebViewClient:
    def __init__(self, arg0: Context, arg1: WebView) -> None: ...
    def clearAdObjects(self) -> None: ...
    def setDelegateWebViewClient(self, arg0: WebViewClient) -> None: ...
    def getDelegateWebViewClient(self) -> WebViewClient: ...
    def getDelegate(self) -> WebViewClient: ...
