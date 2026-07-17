from resume_parser.extractors.project_extractor import (
    ProjectExtractor,
)


def test_extract_project():

    text = """
    PROJECTS

    Recruitment Intelligence Platform

    Developed using Python, FastAPI, PostgreSQL,
    Docker and Kubernetes.
    """

    result = ProjectExtractor.extract(text)

    assert len(result) == 1

    assert "Python" in result[0]["technologies"]

    assert "Docker" in result[0]["technologies"]


def test_extract_project_empty():

    assert ProjectExtractor.extract("") == []


def test_extract_project_without_section():

    text = """
    Experienced Python Developer with 5 years experience.
    """

    assert ProjectExtractor.extract(text) == []


def test_extract_project_multiple_technologies():

    text = """
    Projects

    Cloud Migration

    AWS Docker Kubernetes Terraform Python
    """

    result = ProjectExtractor.extract(text)

    technologies = result[0]["technologies"]

    assert "AWS" in technologies

    assert "Docker" in technologies

    assert "Kubernetes" in technologies

    assert "Python" in technologies