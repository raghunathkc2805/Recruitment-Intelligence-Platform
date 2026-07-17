import pytest


@pytest.fixture
def candidate():

    return {
        "skills": [
            "Python",
            "Docker",
            "AWS",
        ],
        "experience": {
            "years": 5,
        },
        "education": [
            {
                "degree": "B.E",
            }
        ],
        "designations": [
            "Software Engineer",
        ],
        "locations": [
            {
                "location": "Bangalore",
            }
        ],
        "certifications": [
            {
                "certification": "AWS Certified Solutions Architect",
            }
        ],
    }


@pytest.fixture
def job():

    return {
        "skills": [
            "Python",
            "Docker",
        ],
        "experience": 3,
        "education": [
            "B.E",
        ],
        "designations": [
            "Software Engineer",
        ],
        "locations": [
            "Bangalore",
        ],
        "certifications": [
            "AWS Certified Solutions Architect",
        ],
    }