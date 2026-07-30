from api.auth.permission_dependency import _normalize_permissions


def test_empty_permissions():

    assert _normalize_permissions([]) == set()


def test_none_permissions():

    assert _normalize_permissions([None, "", "   "]) == set()


def test_trim_permissions():

    permissions = _normalize_permissions(
        [
            " candidate.view ",
            "candidate.create  ",
            "  candidate.update",
        ]
    )

    assert "candidate.view" in permissions
    assert "candidate.create" in permissions
    assert "candidate.update" in permissions


def test_lowercase_conversion():

    permissions = _normalize_permissions(
        [
            "Candidate.View",
            "Candidate.Create",
        ]
    )

    assert "candidate.view" in permissions
    assert "candidate.create" in permissions


def test_duplicate_permissions_removed():

    permissions = _normalize_permissions(
        [
            "candidate.view",
            "Candidate.View",
            " candidate.view ",
        ]
    )

    assert len(permissions) == 1
    assert "candidate.view" in permissions


def test_multiple_permissions():

    permissions = _normalize_permissions(
        [
            "resume.view",
            "resume.upload",
            "candidate.view",
            "candidate.create",
        ]
    )

    assert len(permissions) == 4
