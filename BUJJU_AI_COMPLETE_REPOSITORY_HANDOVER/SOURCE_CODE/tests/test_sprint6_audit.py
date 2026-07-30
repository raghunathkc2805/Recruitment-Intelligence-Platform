import importlib

import pytest


MODULES = [
    "database.models.audit_log",
    "api.schemas.audit",
    "api.repositories.audit_repository",
    "api.services.audit_service",
    "api.services.audit_export_service",
    "api.services.audit_retention_service",
    "api.middleware.audit_middleware",
    "api.dependencies.audit_permission",
    "api.routes.audit",
]


@pytest.mark.parametrize("module_name", MODULES)
def test_module_import(module_name):

    module = importlib.import_module(module_name)

    assert module is not None


def test_route_router_exists():

    from api.routes.audit import router

    assert router is not None


def test_service_exists():

    from api.services.audit_service import AuditService

    assert AuditService is not None


def test_repository_exists():

    from api.repositories.audit_repository import AuditRepository

    assert AuditRepository is not None


def test_schema_exists():

    from api.schemas.audit import AuditCreate

    assert AuditCreate is not None


def test_model_exists():

    from database.models.audit_log import AuditLog

    assert AuditLog is not None


def test_export_service_exists():

    from api.services.audit_export_service import AuditExportService

    assert AuditExportService is not None


def test_retention_service_exists():

    from api.services.audit_retention_service import AuditRetentionService

    assert AuditRetentionService is not None


def test_permission_dependency_exists():

    from api.dependencies.audit_permission import require_audit_view

    assert callable(require_audit_view)


def test_middleware_exists():

    from api.middleware.audit_middleware import AuditMiddleware

    assert AuditMiddleware is not None
