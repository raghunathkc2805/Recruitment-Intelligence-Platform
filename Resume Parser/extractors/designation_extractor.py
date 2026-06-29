from utils.knowledge_base import DESIGNATION_ALIASES


def normalize_designation(designation):
    """
    Normalize a designation using the designation alias knowledge base.
    """

    if not designation:
        return ""

    designation = designation.strip().lower()

    for master_designation, aliases in DESIGNATION_ALIASES.items():

        for alias in aliases:

            if alias.lower() == designation:
                return master_designation

    return designation.title()


def normalize_designation_list(designations):
    """
    Normalize a list of designations and remove duplicates.
    """

    normalized = []
    seen = set()

    for designation in designations:

        master = normalize_designation(designation)

        if master not in seen:
            normalized.append(master)
            seen.add(master)

    return normalized