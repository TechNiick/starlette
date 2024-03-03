from __future__ import annotations

from typing import Protocol

from httpx import Cookies, Headers

from starlette.testclient import TestClient
from starlette.types import ASGIApp


class TestClientFactory(Protocol):  # pragma: no cover
    __test__ = False  # type: ignore

    def __call__(
        self,
        app: ASGIApp,
        base_url: str = "http://testserver",
        raise_server_exceptions: bool = True,
        root_path: str = "",
        cookies: Cookies | dict[str, str] | None = None,
        headers: Headers | None = None,
        follow_redirects: bool = True,
    ) -> TestClient:
        ...
