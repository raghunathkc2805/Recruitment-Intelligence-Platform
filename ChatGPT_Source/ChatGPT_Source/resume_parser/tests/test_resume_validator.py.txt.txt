from resume_parser.pipeline.resume_pipeline import ResumePipeline
from resume_parser.validators.resume_validator import ResumeValidator


def test_resume_validator(sample_txt):

    result = ResumePipeline.process(sample_txt)

    validation = ResumeValidator.validate(result)

    assert "valid" in validation

    assert "checks" in validation

    assert isinstance(validation["checks"], dict)