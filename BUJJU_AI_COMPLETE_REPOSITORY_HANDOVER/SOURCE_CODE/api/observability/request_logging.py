from __future__ import annotations

import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from .logger import get_logger
from .log_context import request_id

logger=get_logger("requests")


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self,request,call_next):

        rid=str(uuid.uuid4())

        request_id.set(rid)

        start=time.perf_counter()

        response=await call_next(request)

        elapsed=round(
            (time.perf_counter()-start)*1000,
            2,
        )

        logger.info(

            f"{request.method} {request.url.path}",

            extra={

                "duration_ms":elapsed

            }

        )

        response.headers["X-Request-ID"]=rid

        return response
