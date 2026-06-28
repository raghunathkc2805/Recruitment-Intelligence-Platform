from utils.knowledge_base import CERTIFICATIONS


def extract_certifications(text):
    """
    Extract certifications from resume.
    """

    text = text.lower()

    found = []

    for category, certifications in CERTIFICATIONS.items():

        for certification in certifications:

            if certification.lower() in text:

                found.append(
                    {
                        "category": category,
                        "name": certification
                    }
                )

    return found