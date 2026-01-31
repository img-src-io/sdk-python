import httpx
import pytest

from img_src.httpclient import HttpClient
from img_src.sdk import Imgsrc


class MockHttpClient:
    """Mock HTTP client that implements the HttpClient protocol."""

    def __init__(self):
        self._inner = httpx.Client()
        self.response: httpx.Response | None = None
        self.last_request: httpx.Request | None = None

    def send(self, request: httpx.Request, **kwargs) -> httpx.Response:
        self.last_request = request
        assert self.response is not None, "Set mock_client.response before calling SDK"
        return self.response

    def build_request(self, method, url, **kwargs) -> httpx.Request:
        return self._inner.build_request(method, url, **kwargs)

    def close(self) -> None:
        self._inner.close()


class MockAsyncHttpClient:
    """Mock async HTTP client that implements the AsyncHttpClient protocol."""

    def __init__(self):
        self._inner = httpx.AsyncClient()
        self.response: httpx.Response | None = None
        self.last_request: httpx.Request | None = None

    async def send(self, request: httpx.Request, **kwargs) -> httpx.Response:
        self.last_request = request
        assert self.response is not None, "Set mock_client.response before calling SDK"
        return self.response

    def build_request(self, method, url, **kwargs) -> httpx.Request:
        return self._inner.build_request(method, url, **kwargs)

    async def aclose(self) -> None:
        await self._inner.aclose()


def make_mock_response(status_code: int, json_body: dict | None = None) -> httpx.Response:
    """Create an httpx.Response with the given status and JSON body."""
    request = httpx.Request("GET", "http://test.local")
    if json_body is not None:
        return httpx.Response(
            status_code=status_code,
            json=json_body,
            request=request,
            headers={"content-type": "application/json"},
        )
    return httpx.Response(status_code=status_code, request=request)


@pytest.fixture
def mock_client():
    client = MockHttpClient()
    yield client
    client.close()


@pytest.fixture
def mock_async_client():
    client = MockAsyncHttpClient()
    return client


@pytest.fixture
def make_sdk(mock_client, mock_async_client):
    """Create an Imgsrc SDK instance with mock HTTP clients."""
    sdk = Imgsrc(
        bearer_auth="test-token",
        server_url="http://test.local",
        client=mock_client,
        async_client=mock_async_client,
    )
    return sdk
