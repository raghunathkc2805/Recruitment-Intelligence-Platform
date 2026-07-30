from resume_parser.models.candidate import Candidate
from resume_parser.models.certification import Certification
from resume_parser.models.education import Education
from resume_parser.models.employment import Employment
from resume_parser.models.project import Project
from resume_parser.models.resume import Resume
from resume_parser.models.skill import Skill


def test_skill_model():

    skill = Skill(
        name="Python",
        category="technical",
    )

    assert skill.name == "Python"

    assert skill.category == "technical"


def test_certification_model():

    certification = Certification(
        name="AWS Certified Solutions Architect",
    )

    assert certification.name.startswith("AWS")


def test_education_model():

    education = Education(
        degree="B.E",
        year="2022",
    )

    assert education.degree == "B.E"


def test_employment_model():

    employment = Employment(
        company="Infosys",
        designation="Software Engineer",
    )

    assert employment.company == "Infosys"


def test_project_model():

    project = Project(
        project_name="Recruitment Intelligence Platform",
    )

    assert project.project_name == "Recruitment Intelligence Platform"


def test_candidate_model():

    candidate = Candidate(
        name="John Doe",
    )

    assert candidate.name == "John Doe"


def test_resume_model():

    resume = Resume(
        file_name="resume.pdf",
        file_type=".pdf",
        file_size=1024,
        page_count=2,
    )

    assert resume.file_name == "resume.pdf"

    assert resume.success is True