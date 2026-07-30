from api.database.rbac_defaults import DEFAULT_ROLE_PERMISSIONS
from api.auth.permission_constants import Permission


def test_super_admin_exists():

    assert "Super Admin" in DEFAULT_ROLE_PERMISSIONS


def test_admin_exists():

    assert "Admin" in DEFAULT_ROLE_PERMISSIONS


def test_recruiter_exists():

    assert "Recruiter" in DEFAULT_ROLE_PERMISSIONS


def test_every_role_has_permissions():

    for role, permissions in DEFAULT_ROLE_PERMISSIONS.items():

        assert isinstance(permissions, list)
        assert len(permissions) > 0


def test_recruiter_permissions():

    permissions = DEFAULT_ROLE_PERMISSIONS["Recruiter"]

    assert Permission.CANDIDATE_CREATE in permissions
    assert Permission.CANDIDATE_VIEW in permissions
    assert Permission.RESUME_UPLOAD in permissions


def test_manager_permissions():

    permissions = DEFAULT_ROLE_PERMISSIONS["Recruitment Manager"]

    assert Permission.MATCHING_RUN in permissions
    assert Permission.RANKING_RUN in permissions
    assert Permission.SEARCH_EXECUTE in permissions


def test_read_only_permissions():

    permissions = DEFAULT_ROLE_PERMISSIONS["Read Only"]

    assert Permission.CANDIDATE_VIEW in permissions
    assert Permission.RESUME_VIEW in permissions

    assert Permission.CANDIDATE_DELETE not in permissions


def test_super_admin_has_wildcard():

    permissions = DEFAULT_ROLE_PERMISSIONS["Super Admin"]

    assert "*" in permissions


def test_duplicate_permissions():

    for role, permissions in DEFAULT_ROLE_PERMISSIONS.items():

        assert len(permissions) == len(set(permissions))
