from resume_parser.resume_service import ResumeService


def test_resume_service_parse(sample_txt):

    result = ResumeService.parse(sample_txt)

    assert result["success"] is True

    assert "candidate" in result


def test_resume_service_parse_resume(sample_txt):

    result = ResumeService.parse_resume(sample_txt)

    assert result["success"] is True


def test_resume_service_process(sample_txt):

    result = ResumeService.process(sample_txt)

    assert result["success"] is True


def test_resume_service_candidate_exists(sample_txt):

    result = ResumeService.parse(sample_txt)

    assert isinstance(result["candidate"], dict)