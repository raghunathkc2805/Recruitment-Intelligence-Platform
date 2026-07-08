import json
from dataclasses import asdict


def save_job_description(job, output_file):
    """
    Save JobDescription object as JSON.
    """

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            asdict(job),
            f,
            indent=4,
            ensure_ascii=False
        )