from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Depends, Query

from database.session import get_db
from api.repositories.audit_repository import AuditRepository
from api.schemas.audit import (
    AuditCreate,
    AuditExportRequest,
    AuditSearchRequest,
)
from api.services.audit_export_service import AuditExportService
from api.services.audit_retention_service import AuditRetentionService
from api.services.audit_service import AuditService

router = APIRouter(
    prefix="/audit",
    tags=["Audit"]
)


def get_service(db=Depends(get_db)):
    return AuditService(
        AuditRepository(db)
    )


@router.post("/")
def create_audit(
    request: AuditCreate,
    service: AuditService = Depends(get_service),
):
    return service.create(request)


@router.get("/")
def list_audit(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=500),
    service: AuditService = Depends(get_service),
):
    return service.list(page, page_size)


@router.get("/{audit_id}")
def get_audit(
    audit_id: UUID,
    service: AuditService = Depends(get_service),
):
    return service.get(audit_id)


@router.delete("/{audit_id}")
def delete_audit(
    audit_id: UUID,
    service: AuditService = Depends(get_service),
):
    return service.delete(audit_id)


@router.post("/search")
def search(
    request: AuditSearchRequest,
    service: AuditService = Depends(get_service),
):
    return service.search(
        start_date=request.start_date,
        end_date=request.end_date,
        action=request.action,
        status=request.status,
        user_id=request.user_id,
    )


@router.get("/users/{user_id}")
def by_user(
    user_id: UUID,
    page: int = 1,
    page_size: int = 50,
    service: AuditService = Depends(get_service),
):
    return service.by_user(
        user_id=user_id,
        page=page,
        page_size=page_size,
    )


@router.get("/actions/{action}")
def by_action(
    action: str,
    service: AuditService = Depends(get_service),
):
    return service.by_action(action)


@router.get("/resources/{resource_type}")
def by_resource(
    resource_type: str,
    resource_id: str | None = None,
    service: AuditService = Depends(get_service),
):
    return service.by_resource(
        resource_type,
        resource_id,
    )


@router.post("/export")
def export(
    request: AuditExportRequest,
    service: AuditService = Depends(get_service),
):

    exporter = AuditExportService()

    records = service.search()

    return exporter.export(
        records,
        request.format,
    )


@router.delete("/retention/{days}")
def purge(
    days: int,
    db=Depends(get_db),
):

    service = AuditRetentionService(db)

    return {
        "deleted": service.purge(days)
    }
