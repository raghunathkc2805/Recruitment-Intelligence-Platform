from resume_parser.schemas import (
    ResponseSchema,
    ResumeSchema,
)


def test_resume_schema_exists():

    assert ResumeSchema is not None


def test_response_schema_exists():

    assert ResponseSchema is not None


def test_schema_exports():

    assert "ResumeSchema" in ResumeSchema.__name__

    assert "ResponseSchema" in ResponseSchema.__name__