import resume_parser


def test_package_version():

    assert hasattr(resume_parser, "__version__")


def test_package_service():

    assert hasattr(resume_parser, "ResumeService")