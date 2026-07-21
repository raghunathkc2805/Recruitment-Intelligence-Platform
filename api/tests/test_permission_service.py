import pytest

from api.services.permission_service import PermissionService


class MockRole:
    def __init__(self):
        self.id = 1
        self.name = "Recruiter"


class MockPermission:
    def __init__(self):
        self.id = 1
        self.name = "candidate.view"


class MockRepository:

    def __init__(self):
        self.roles = [MockRole()]
        self.permissions = [MockPermission()]

    def list_roles(self):
        return self.roles

    def list_permissions(self):
        return self.permissions

    def get_role(self, name):
        for role in self.roles:
            if role.name == name:
                return role
        return None

    def get_permission(self, name):
        for permission in self.permissions:
            if permission.name == name:
                return permission
        return None

    def create_role(self, **kwargs):
        role = MockRole()
        role.name = kwargs["name"]
        self.roles.append(role)
        return role

    def create_permission(self, **kwargs):
        permission = MockPermission()
        permission.name = kwargs["name"]
        self.permissions.append(permission)
        return permission


@pytest.fixture
def service():

    service = PermissionService(db=None)
    service.repository = MockRepository()

    return service


def test_list_roles(service):

    assert len(service.get_roles()) > 0


def test_list_permissions(service):

    assert len(service.get_permissions()) > 0


def test_existing_role(service):

    assert service.role_exists("Recruiter") is True


def test_existing_permission(service):

    assert service.permission_exists("candidate.view") is True


def test_create_role(service):

    role = service.create_role(
        name="Hiring Manager"
    )

    assert role.name == "Hiring Manager"


def test_create_permission(service):

    permission = service.create_permission(
        name="candidate.create",
        module="candidate"
    )

    assert permission.name == "candidate.create"
