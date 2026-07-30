from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AuditBase(BaseModel):
    action: str
    event_type: str
    status: str

    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    resource_name: Optional[str] = None

    module: Optional[str] = None
    endpoint: Optional[str] = None
    http_method: Optional[str] = None

    message: Optional[str] = None
    reason: Optional[str] = None

    client_ip: Optional[str] = None
    forwarded_ip: Optional[str] = None
    user_agent: Optional[str] = None

    device: Optional[str] = None
    browser: Optional[str] = None
    platform: Optional[str] = None

    country: Optional[str] = None
    city: Optional[str] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    response_time_ms: Optional[float] = None

    before_data: Optional[Dict[str, Any]] = None
    after_data: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

    request_body: Optional[Dict[str, Any]] = None
    query_params: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, Any]] = None


class AuditCreate(AuditBase):
    tenant_id: Optional[UUID] = None
    organization_id: Optional[UUID] = None
    user_id: Optional[UUID] = None

    username: Optional[str] = None
    email: Optional[str] = None
    role_name: Optional[str] = None

    session_id: Optional[str] = None
    request_id: Optional[str] = None
    correlation_id: Optional[str] = None
    trace_id: Optional[str] = None

    status_code: Optional[int] = None


class AuditUpdate(BaseModel):
    status: Optional[str] = None
    status_code: Optional[int] = None
    message: Optional[str] = None
    reason: Optional[str] = None
    response_time_ms: Optional[float] = None
    after_data: Optional[Dict[str, Any]] = None


class AuditResponse(AuditBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID

    tenant_id: Optional[UUID] = None
    organization_id: Optional[UUID] = None
    user_id: Optional[UUID] = None

    username: Optional[str] = None
    email: Optional[str] = None
    role_name: Optional[str] = None

    session_id: Optional[str] = None
    request_id: Optional[str] = None
    correlation_id: Optional[str] = None
    trace_id: Optional[str] = None

    status_code: Optional[int] = None
    created_at: datetime


class AuditSearchRequest(BaseModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    user_id: Optional[UUID] = None
    action: Optional[str] = None
    event_type: Optional[str] = None
    status: Optional[str] = None

    module: Optional[str] = None
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None

    endpoint: Optional[str] = None
    http_method: Optional[str] = None

    session_id: Optional[str] = None
    request_id: Optional[str] = None
    correlation_id: Optional[str] = None

    keyword: Optional[str] = None

    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=500)


class AuditStatistics(BaseModel):
    total_records: int
    successful_events: int
    failed_events: int
    unique_users: int
    unique_actions: int
    unique_resources: int


class AuditExportRequest(BaseModel):
    format: str = "csv"
    filters: Optional[AuditSearchRequest] = None


class AuditPagedResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: List[AuditResponse]
