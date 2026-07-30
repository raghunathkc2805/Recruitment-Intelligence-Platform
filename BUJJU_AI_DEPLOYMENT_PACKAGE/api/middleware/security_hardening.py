"""
Sprint 7
Enterprise Security Hardening Middleware
"""

from __future__ import annotations

import re
from urllib.parse import unquote

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


SQL_PATTERNS = [
    r"union\s+select",
    r"drop\s+table",
    r"insert\s+into",
    r"delete\s+from",
    r"update\s+\w+\s+set",
    r"--",
    r"/\*",
    r"\*/",
    r";\s*$",
]

XSS_PATTERNS = [
    r"<script",
    r"javascript:",
    r"onerror=",
    r"onload=",
    r"<iframe",
    r"<object",
    r"<embed",
]

PATH_PATTERNS = [
    r"\.\./",
    r"\.\.\\",
    r"%2e%2e",
]

MAX_QUERY_LENGTH = 4096

MAX_PATH_LENGTH = 2048


class SecurityHardeningMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        path = unquote(str(request.url.path)).lower()

        query = unquote(str(request.url.query)).lower()

        if len(path) > MAX_PATH_LENGTH:

            return JSONResponse(
                status_code=414,
                content={"detail": "Request URI too long."},
            )

        if len(query) > MAX_QUERY_LENGTH:

            return JSONResponse(
                status_code=400,
                content={"detail": "Query too large."},
            )

        payload = path + " " + query

        for pattern in SQL_PATTERNS:

            if re.search(pattern, payload):

                return JSONResponse(
                    status_code=400,
                    content={"detail": "Potential SQL Injection detected."},
                )

        for pattern in XSS_PATTERNS:

            if re.search(pattern, payload):

                return JSONResponse(
                    status_code=400,
                    content={"detail": "Potential XSS detected."},
                )

        for pattern in PATH_PATTERNS:

            if re.search(pattern, payload):

                return JSONResponse(
                    status_code=400,
                    content={"detail": "Path traversal detected."},
                )

        return await call_next(request)

