"""
Enterprise Audit Logging Middleware
Sprint 7
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path

from starlette.middleware.base import BaseHTTPMiddleware

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("audit")

if not logger.handlers:
    handler = logging.FileHandler(LOG_DIR / "audit.log", encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.setLevel(logging.INFO)


class AuditLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start = time.perf_counter()

        response = await call_next(request)

        elapsed = round((time.perf_counter() - start) * 1000, 2)

        event = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "method": request.method,
            "path": request.url.path,
            "query": str(request.url.query),
            "client_ip": request.client.host if request.client else "unknown",
            "user": request.headers.get("X-User-ID", "anonymous"),
            "status": response.status_code,
            "duration_ms": elapsed,
            "user_agent": request.headers.get("User-Agent", ""),
        }

        if (
            request.url.path.startswith("/auth")
            or response.status_code in (401, 403)
            or request.method in ("POST", "PUT", "PATCH", "DELETE")
        ):
            logger.info(json.dumps(event))

        return response
