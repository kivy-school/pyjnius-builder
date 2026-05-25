from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class WebViewClient:
    """Forward declaration for ``android.webkit.WebViewClient``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.WebViewClient')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/WebViewClient
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
class WebResourceRequest:
    """Forward declaration for ``android.webkit.WebResourceRequest``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.WebResourceRequest')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/WebResourceRequest
    """
    ...
class Bitmap:
    """Forward declaration for ``android.graphics.Bitmap``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.Bitmap')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/Bitmap
    """
    ...
class WebResourceResponse:
    """Forward declaration for ``android.webkit.WebResourceResponse``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.WebResourceResponse')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/WebResourceResponse
    """
    ...
class Message:
    """Forward declaration for ``android.os.Message``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Message')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Message
    """
    ...
class WebResourceError:
    """Forward declaration for ``android.webkit.WebResourceError``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.WebResourceError')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/WebResourceError
    """
    ...
class SslErrorHandler:
    """Forward declaration for ``android.webkit.SslErrorHandler``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.SslErrorHandler')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/SslErrorHandler
    """
    ...
class SslError:
    """Forward declaration for ``android.net.http.SslError``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.net.http.SslError')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/net/http/SslError
    """
    ...
class ClientCertRequest:
    """Forward declaration for ``android.webkit.ClientCertRequest``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.ClientCertRequest')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/ClientCertRequest
    """
    ...
class HttpAuthHandler:
    """Forward declaration for ``android.webkit.HttpAuthHandler``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.HttpAuthHandler')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/HttpAuthHandler
    """
    ...
class KeyEvent:
    """Forward declaration for ``android.view.KeyEvent``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.KeyEvent')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/KeyEvent
    """
    ...
class RenderProcessGoneDetail:
    """Forward declaration for ``android.webkit.RenderProcessGoneDetail``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.RenderProcessGoneDetail')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/RenderProcessGoneDetail
    """
    ...
class SafeBrowsingResponse:
    """Forward declaration for ``android.webkit.SafeBrowsingResponse``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.webkit.SafeBrowsingResponse')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/webkit/SafeBrowsingResponse
    """
    ...

class zzbqt:
    def __init__(self) -> None: ...
    def getDelegate(self) -> WebViewClient: ...
    @overload
    def shouldOverrideUrlLoading(self, arg0: WebView, arg1: str) -> bool: ...
    @overload
    def shouldOverrideUrlLoading(self, arg0: WebView, arg1: WebResourceRequest) -> bool: ...
    def onPageStarted(self, arg0: WebView, arg1: str, arg2: Bitmap) -> None: ...
    def onPageFinished(self, arg0: WebView, arg1: str) -> None: ...
    def onLoadResource(self, arg0: WebView, arg1: str) -> None: ...
    def onPageCommitVisible(self, arg0: WebView, arg1: str) -> None: ...
    @overload
    def shouldInterceptRequest(self, arg0: WebView, arg1: str) -> WebResourceResponse: ...
    @overload
    def shouldInterceptRequest(self, arg0: WebView, arg1: WebResourceRequest) -> WebResourceResponse: ...
    def onTooManyRedirects(self, arg0: WebView, arg1: Message, arg2: Message) -> None: ...
    @overload
    def onReceivedError(self, arg0: WebView, arg1: int, arg2: str, arg3: str) -> None: ...
    @overload
    def onReceivedError(self, arg0: WebView, arg1: WebResourceRequest, arg2: WebResourceError) -> None: ...
    def onReceivedHttpError(self, arg0: WebView, arg1: WebResourceRequest, arg2: WebResourceResponse) -> None: ...
    def onFormResubmission(self, arg0: WebView, arg1: Message, arg2: Message) -> None: ...
    def doUpdateVisitedHistory(self, arg0: WebView, arg1: str, arg2: bool) -> None: ...
    def onReceivedSslError(self, arg0: WebView, arg1: SslErrorHandler, arg2: SslError) -> None: ...
    def onReceivedClientCertRequest(self, arg0: WebView, arg1: ClientCertRequest) -> None: ...
    def onReceivedHttpAuthRequest(self, arg0: WebView, arg1: HttpAuthHandler, arg2: str, arg3: str) -> None: ...
    def shouldOverrideKeyEvent(self, arg0: WebView, arg1: KeyEvent) -> bool: ...
    def onUnhandledKeyEvent(self, arg0: WebView, arg1: KeyEvent) -> None: ...
    def onScaleChanged(self, arg0: WebView, arg1: float, arg2: float) -> None: ...
    def onReceivedLoginRequest(self, arg0: WebView, arg1: str, arg2: str, arg3: str) -> None: ...
    def onRenderProcessGone(self, arg0: WebView, arg1: RenderProcessGoneDetail) -> bool: ...
    def onSafeBrowsingHit(self, arg0: WebView, arg1: WebResourceRequest, arg2: int, arg3: SafeBrowsingResponse) -> None: ...
