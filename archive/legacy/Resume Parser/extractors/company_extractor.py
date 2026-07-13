from utils.knowledge_base import COMPANIES


def normalize_company(company_name):
    """
    Normalize company name using the company knowledge base.
    """

    if not company_name:
        return ""

    company_name = company_name.strip().lower()

    for master_company, aliases in COMPANIES.items():

        for alias in aliases:

            if alias.lower() == company_name:
                return master_company

    return company_name.title()


def normalize_company_list(companies):
    """
    Normalize a list of companies and remove duplicates.
    """

    normalized = []
    seen = set()

    for company in companies:

        master = normalize_company(company)

        if master not in seen:
            normalized.append(master)
            seen.add(master)

    return normalized