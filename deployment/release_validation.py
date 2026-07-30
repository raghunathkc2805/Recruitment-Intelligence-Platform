from __future__ import annotations

import sys
import subprocess
import importlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)


MODULES = [

    "api.app",

    "database.engine",

    "matching_engine",

    "jd_parser",

    "api.services.recruiter_copilot_service",

    "api.services.ai_search_assistant_service",

    "api.services.boolean_search_service",

    "api.services.analytics_service",

    "api.services.continuous_learning_service",

    "api.services.knowledge_governance_service",

]


failed = []


print("=== MODULE VALIDATION ===")


for module in MODULES:

    try:

        importlib.import_module(
            module
        )

        print(
            f"PASS : {module}"
        )


    except Exception as error:

        failed.append(
            {
                "module": module,
                "error": str(error),
            }
        )

        print(
            f"FAIL : {module}"
        )


print("")
print("=== PYTEST VALIDATION ===")


result = subprocess.run(
    [
        sys.executable,
        "-m",
        "pytest",
        "-q",
    ],
    cwd=ROOT,
)


if result.returncode != 0:

    failed.append(
        {
            "module": "pytest",
            "error": "Test suite failed",
        }
    )


if failed:

    print(
        "RELEASE VALIDATION FAILED"
    )

    print(
        failed
    )

    sys.exit(1)


print("")
print("==============================")
print("RECRUITMENT INTELLIGENCE PLATFORM")
print("VERSION 1.0 VALIDATION PASSED")
print("==============================")