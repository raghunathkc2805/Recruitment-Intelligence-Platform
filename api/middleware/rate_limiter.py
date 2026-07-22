"""
Enterprise Rate Limiting Middleware
Sprint 7
"""

from __future__ import annotations

import time
from collections import defaultdict, deque

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class SlidingWindow:

    def __init__(self, limit: int, seconds: int):
        self.limit = limit
        self.seconds = seconds
        self.requests = defaultdict(deque)

    def allow(self, key: str):

        now = time.time()

        q = self.requests[key]

        while q and now - q[0] > self.seconds:
            q.popleft()

        if len(q) >= self.limit:
            return False

        q.append(now)

        return True


class RateLimiterMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):

        super().__init__(app)

        self.ip_limit = SlidingWindow(
            limit=300,
            seconds=60,
        )

        self.login_limit = SlidingWindow(
            limit=10,
            seconds=300,
        )

        self.user_limit = SlidingWindow(
            limit=600,
            seconds=60,
        )

    async def dispatch(self, request, call_next):

        ip = request.client.host if request.client else "unknown"

        if not self.ip_limit.allow(ip):

            return JSONResponse(
                status_code=429,
                content={
                    "detail": "IP rate limit exceeded."
                },
            )

        if request.url.path.startswith("/auth/login"):

            if not self.login_limit.allow(ip):

                return JSONResponse(
                    status_code=429,
                    content={
                        "detail": "Too many login attempts."
                    },
                )

        user = request.headers.get("X-User-ID")

        if user:

            if not self.user_limit.allow(user):

                return JSONResponse(
                    status_code=429,
                    content={
                        "detail": "User request limit exceeded."
                    },
                )

        return await call_next(request)

