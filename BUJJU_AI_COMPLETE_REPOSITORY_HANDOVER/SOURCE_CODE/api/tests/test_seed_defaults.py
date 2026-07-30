from api.database.seed_rbac import DEFAULT_ROLES, DEFAULT_PERMISSIONS


def test_default_roles_unique():

    role_names = [role[0] for role in DEFAULT_ROLES]

    assert len(role_names) == len(set(role_names))


def test_default_permissions_unique():

    permission_names = [
        permission[0]
        for permission in DEFAULT_PERMISSIONS
    ]

    assert len(permission_names) == len(set(permission_names))


def test_role_structure():

    for role in DEFAULT_ROLES:

        assert len(role) == 2

        assert isinstance(role[0], str)
        assert isinstance(role[1], str)


def test_permission_structure():

    for permission in DEFAULT_PERMISSIONS:

        assert len(permission) == 3

        assert isinstance(permission[0], str)
        assert isinstance(permission[1], str)
        assert isinstance(permission[2], str)


def test_candidate_permissions_exist():

    permissions = {
        permission[0]
        for permission in DEFAULT_PERMISSIONS
    }

    assert "candidate.create" in permissions
    assert "candidate.view" in permissions
    assert "candidate.update" in permissions
    assert "candidate.delete" in permissions


def test_resume_permissions_exist():

    permissions = {
        permission[0]
        for permission in DEFAULT_PERMISSIONS
    }

    assert "resume.upload" in permissions
    assert "resume.view" in permissions


def test_admin_permissions_exist():

    permissions = {
        permission[0]
        for permission in DEFAULT_PERMISSIONS
    }

    assert "user.manage" in permissions
    assert "role.manage" in permissions
    assert "permission.manage" in permissions
