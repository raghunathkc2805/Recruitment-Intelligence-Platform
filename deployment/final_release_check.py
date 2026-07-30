from pathlib import Path
import sys
import subprocess
import importlib


ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)


checks = []


def check(name, result):

    checks.append(
        {
            "component": name,
            "status": result,
        }
    )


print(
    "=== VERSION 1.0 RELEASE SMOKE TEST ==="
)


modules = [

    "api.app",

    "database.engine",

    "jd_parser",

    "matching_engine",

    "api.services.recruiter_copilot_service",

    "api.services.ai_search_assistant_service",

    "api.services.boolean_search_service",

    "api.services.explainable_ai_service",

    "api.services.resume_intelligence_service",

    "api.services.jd_intelligence_service",

]


for module in modules:

    try:

        importlib.import_module(
            module
        )

        check(
            module,
            "PASS"
        )

        print(
            f"PASS : {module}"
        )


    except Exception as error:

        check(
            module,
            f"FAIL : {error}"
        )

        print(
            f"FAIL : {module}"
        )



print(
    ""
)

print(
    "=== DOCUMENTATION VALIDATION ==="
)


documents = [

    "docs/ADMINISTRATOR_GUIDE.md",

    "docs/RECRUITER_USER_GUIDE.md",

    "docs/EXECUTIVE_RELEASE_SUMMARY.md",

    "docs/VERSION_1_RELEASE_NOTES.md",

]


for document in documents:

    file = ROOT / document


    if file.exists():

        check(
            document,
            "PASS"
        )

        print(
            f"PASS : {document}"
        )

    else:

        check(
            document,
            "MISSING"
        )

        print(
            f"FAIL : {document}"
        )



print(
    ""
)

print(
    "=== RELEASE ARTIFACT VALIDATION ==="
)


artifacts = [

    "Dockerfile",

    "docker-compose.yml",

    ".env.production.template",

    "deployment/production_deploy.ps1",

    "deployment/release_validation.py",

]


for artifact in artifacts:

    file = ROOT / artifact


    if file.exists():

        check(
            artifact,
            "PASS"
        )

        print(
            f"PASS : {artifact}"
        )

    else:

        check(
            artifact,
            "MISSING"
        )

        print(
            f"FAIL : {artifact}"
        )



failed = [

    item

    for item in checks

    if item["status"] != "PASS"

]


print(
    ""
)


if failed:

    print(
        "RELEASE PACKAGE FAILED"
    )

    print(
        failed
    )

    sys.exit(1)



print(
    "===================================="
)

print(
    "RECRUITMENT INTELLIGENCE PLATFORM"
)

print(
    "VERSION 1.0 RELEASE READY"
)

print(
    "===================================="

)
