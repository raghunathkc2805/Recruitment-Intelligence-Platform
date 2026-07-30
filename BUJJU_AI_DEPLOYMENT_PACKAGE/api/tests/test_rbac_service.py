import pytest

from api.services.rbac_service import RBACService


class MockRole:
    def __init__(self, role_id):
        self.id = role_id


class MockPermission:
    def __init__(self, permission_id):
        self.id = permission_id


class MockRepository:

    def get_role_by_name(self, role_name):
        if role_name == "Recruiter":
            return MockRole(1)
        return None

    def get_permission_by_name(self, permission_name):
        if permission_name == "candidate.view":
            return MockPermission(10)
        return None

    def assign_role_to_user(self, **kwargs):
        return True

    def assign_permission_to_role(self, **kwargs):
        return True


@pytest.fixture
def service():

    service = RBACService(db=None)
    service.repository = MockRepository()

    return service


def test_assign_role_to_user(service):

    service.assign_role_to_user(
        user_id=100,
        role_name="Recruiter",
    )


def test_assign_permission_to_role(service):

    service.assign_permission_to_role(
        role_name="Recruiter",
        permission_name="candidate.view",
    )


def test_invalid_role(service):

    with pytest.raises(ValueError):

        service.assign_role_to_user(
            user_id=1,
            role_name="Unknown",
        )


def test_invalid_permission(service):

    with pytest.raises(ValueError):

        service.assign_permission_to_role(
            role_name="Recruiter",
            permission_name="unknown.permission",
        )
