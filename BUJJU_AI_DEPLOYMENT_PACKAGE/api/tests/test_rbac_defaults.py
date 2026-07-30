from api.database.rbac_defaults import DEFAULT_ROLE_PERMISSIONS


def test_default_role_count():

    assert len(DEFAULT_ROLE_PERMISSIONS) >= 7


def test_all_roles_have_permissions():

    for role_name, permissions in DEFAULT_ROLE_PERMISSIONS.items():

        assert isinstance(role_name, str)
        assert role_name.strip() != ""

        assert isinstance(permissions, list)
        assert len(permissions) > 0


def test_super_admin_contains_wildcard():

    assert "*" in DEFAULT_ROLE_PERMISSIONS["Super Admin"]


def test_admin_permissions():

    permissions = DEFAULT_ROLE_PERMISSIONS["Admin"]

    assert "candidate.create" in permissions
    assert "candidate.view" in permissions
    assert "candidate.update" in permissions
    assert "candidate.delete" in permissions


def test_recruiter_permissions():

    permissions = DEFAULT_ROLE_PERMISSIONS["Recruiter"]

    assert "candidate.view" in permissions
    assert "resume.upload" in permissions


def test_read_only_permissions():

    permissions = DEFAULT_ROLE_PERMISSIONS["Read Only"]

    assert "candidate.view" in permissions
    assert "resume.view" in permissions

    assert "candidate.delete" not in permissions


def test_every_permission_is_unique_per_role():

    for role_name, permissions in DEFAULT_ROLE_PERMISSIONS.items():

        assert len(permissions) == len(set(permissions))
