from __future__ import annotations

import importlib
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


REQUIRED_MODULES = [

    "api.app",

    "database.engine",

    "matching_engine",

    "jd_parser",

]


FAILED = []


for module in REQUIRED_MODULES:

    try:

        importlib.import_module(
            module
        )

        print(
            f"PASS : {module}"
        )


    except Exception as error:

        FAILED.append(
            {
                "module": module,
                "error": str(error),
            }
        )

        print(
            f"FAIL : {module}"
        )


if FAILED:

    print(
        FAILED
    )

    sys.exit(1)


print(
    "Production Validation Passed"
)