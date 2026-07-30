from __future__ import annotations

import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from api.schemas.audit import AuditCreate
from api.services.audit_service import AuditService
from api.repositories.audit_repository import AuditRepository
from database.session import SessionLocal


class AuditMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        started = time.perf_counter()

        request_id = str(uuid.uuid4())

        request.state.request_id = request_id

        response = None

        try:

            response = await call_next(request)

            return response

        finally:

            elapsed = (time.perf_counter() - started) * 1000

            db = SessionLocal()

            try:

                repository = AuditRepository(db)

                service = AuditService(repository)

                service.create(
                    AuditCreate(
                        request_id=request_id,
                        action=request.method,
                        event_type="HTTP_REQUEST",
                        status="SUCCESS" if response and response.status_code < 400 else "FAILED",
                        status_code=response.status_code if response else 500,
                        endpoint=request.url.path,
                        http_method=request.method,
                        client_ip=request.client.host if request.client else None,
                        user_agent=request.headers.get("user-agent"),
                        response_time_ms=round(elapsed, 2),
                    )
                )

            finally:
                db.close()
