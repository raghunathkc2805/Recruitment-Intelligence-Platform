from api.models.rbac import (
    Permission,
    Role,
    role_permissions,
    user_roles,
)


def test_role_model():

    role = Role(
        name="Recruiter",
        description="Recruiter Role",
        is_active=True,
    )

    assert role.name == "Recruiter"
    assert role.description == "Recruiter Role"
    assert role.is_active is True


def test_permission_model():

    permission = Permission(
        name="candidate.view",
        module="candidate",
        description="View Candidate",
        is_active=True,
    )

    assert permission.name == "candidate.view"
    assert permission.module == "candidate"
    assert permission.description == "View Candidate"
    assert permission.is_active is True


def test_user_roles_table():

    assert user_roles.name == "user_roles"

    columns = {column.name for column in user_roles.columns}

    assert columns == {"user_id", "role_id"}


def test_role_permissions_table():

    assert role_permissions.name == "role_permissions"

    columns = {column.name for column in role_permissions.columns}

    assert columns == {"role_id", "permission_id"}


def test_models_have_tablenames():

    assert Role.__tablename__ == "roles"
    assert Permission.__tablename__ == "permissions"
