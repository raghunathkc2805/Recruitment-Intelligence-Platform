"""
Enterprise Security Headers Middleware
Sprint 7
"""

from __future__ import annotations

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

DEFAULT_CSP = (
    "default-src 'self'; "
    "base-uri 'self'; "
    "frame-ancestors 'none'; "
    "form-action 'self'; "
    "img-src 'self' data: https:; "
    "style-src 'self' 'unsafe-inline'; "
    "script-src 'self'; "
    "object-src 'none'; "
    "connect-src 'self'; "
    "upgrade-insecure-requests"
)

class SecurityHeadersMiddleware(BaseHTTPMiddleware):

    def __init__(
        self,
        app,
        *,
        csp: str = DEFAULT_CSP,
        hsts_max_age: int = 31536000,
    ):
        super().__init__(app)
        self.csp = csp
        self.hsts = (
            f"max-age={hsts_max_age}; "
            "includeSubDomains; preload"
        )

    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:

        response = await call_next(request)

        headers = response.headers

        headers.setdefault(
            "Content-Security-Policy",
            self.csp,
        )

        headers.setdefault(
            "Strict-Transport-Security",
            self.hsts,
        )

        headers.setdefault(
            "X-Frame-Options",
            "DENY",
        )

        headers.setdefault(
            "X-Content-Type-Options",
            "nosniff",
        )

        headers.setdefault(
            "Referrer-Policy",
            "strict-origin-when-cross-origin",
        )

        headers.setdefault(
            "Permissions-Policy",
            "camera=(), microphone=(), geolocation=()",
        )

        headers.setdefault(
            "Cross-Origin-Opener-Policy",
            "same-origin",
        )

        headers.setdefault(
            "Cross-Origin-Resource-Policy",
            "same-origin",
        )

        headers.setdefault(
            "X-Permitted-Cross-Domain-Policies",
            "none",
        )

        headers.setdefault(
            "Cache-Control",
            "no-store",
        )

        return response
