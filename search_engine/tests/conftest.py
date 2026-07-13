import pytest


@pytest.fixture
def sample_candidates():

    return [
        {
            "id": 1,
            "name": "John Doe",
            "skills": "Python Docker AWS Kubernetes",
            "location": "Bangalore",
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "skills": "Java Spring Boot",
            "location": "Hyderabad",
        },
        {
            "id": 3,
            "name": "David",
            "skills": "Python FastAPI PostgreSQL",
            "location": "Chennai",
        },
    ]