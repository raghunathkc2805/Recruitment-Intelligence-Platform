from resume_parser.pipeline.resume_pipeline import ResumePipeline


def test_resume_pipeline(sample_txt):

    result = ResumePipeline.process(sample_txt)

    assert result["success"] is True

    assert "candidate" in result

    candidate = result["candidate"]

    assert "name" in candidate

    assert "email" in candidate

    assert "phone" in candidate

    assert "skills" in candidate

    assert "education" in candidate

    assert "experience" in candidate