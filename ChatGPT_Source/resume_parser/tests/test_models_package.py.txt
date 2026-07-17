from resume_parser.models import (
    Candidate,
    Certification,
    Education,
    Employment,
    Project,
    Resume,
    Skill,
)


def test_models_package_exports():

    assert Candidate is not None

    assert Certification is not None

    assert Education is not None

    assert Employment is not None

    assert Project is not None

    assert Resume is not None

    assert Skill is not None