import json
from dataclasses import asdict


def save_candidate(candidate, output_file):
    """
    Save Candidate object as JSON.
    """

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            asdict(candidate),
            f,
            indent=4,
            ensure_ascii=False
        )