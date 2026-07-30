from starlette.middleware.base import BaseHTTPMiddleware

from api.observability.tracing import start_trace
from api.observability.trace_context import trace_id

class TraceMiddleware(BaseHTTPMiddleware):

    async def dispatch(self,request,call_next):

        tid=start_trace()

        response=await call_next(request)

        response.headers["X-Trace-ID"]=tid

        return response
