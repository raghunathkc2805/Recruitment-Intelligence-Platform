from pathlib import Path

import pytest


@pytest.fixture
def sample_resume_dir():

    return (
        Path(__file__).resolve().parents[1]
        / "sample_resumes"
    )


@pytest.fixture
def sample_pdf(sample_resume_dir):

    return str(
        sample_resume_dir / "sample_resume_01.pdf"
    )


@pytest.fixture
def sample_docx(sample_resume_dir):

    return str(
        sample_resume_dir / "sample_resume_02.docx"
    )


@pytest.fixture
def sample_txt(sample_resume_dir):

    return str(
        sample_resume_dir / "sample_resume_03.txt"
    )