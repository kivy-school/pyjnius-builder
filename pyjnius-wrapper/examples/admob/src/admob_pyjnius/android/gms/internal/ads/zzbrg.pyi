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
class WebResourceRequest:
    """Forward declaration for ``android.webkit.WebResourceRequest``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.WebResourceRequest')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/WebResourceRequest
    """
    ...

class zzbrg:
    def __init__(self, arg0: Context, arg1: WebView) -> None: ...
    def zza(self) -> None: ...
    def zzb(self, arg0: WebViewClient) -> None: ...
    def getDelegate(self) -> WebViewClient: ...
    @overload
    def shouldOverrideUrlLoading(self, arg0: WebView, arg1: WebResourceRequest) -> bool: ...
    @overload
    def shouldOverrideUrlLoading(self, arg0: WebView, arg1: str) -> bool: ...
    def onLoadResource(self, arg0: WebView, arg1: str) -> None: ...
