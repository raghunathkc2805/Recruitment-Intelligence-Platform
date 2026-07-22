import time

from starlette.middleware.base import BaseHTTPMiddleware

from api.observability.metrics_registry import *

class MetricsMiddleware(BaseHTTPMiddleware):

    async def dispatch(self,request,call_next):

        ACTIVE_REQUESTS.inc()

        start=time.perf_counter()

        response=await call_next(request)

        duration=time.perf_counter()-start

        REQUEST_DURATION.labels(
            request.method,
            request.url.path
        ).observe(duration)

        REQUEST_COUNT.labels(
            request.method,
            request.url.path,
            response.status_code
        ).inc()

        ACTIVE_REQUESTS.dec()

        return response
