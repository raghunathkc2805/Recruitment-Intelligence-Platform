# FILE INDEX

---

## Document Information

| Item | Value |
|------|-------|
| Project | Recruitment Intelligence Platform |
| Document | FILE_INDEX |
| Status | Approved |
| Architecture | Frozen |
| Update Method | Generated from project_state |

---

# 1. PURPOSE

The File Index provides a deterministic inventory of repository files and
their organizational structure.

This document serves as the authoritative generated catalog of repository
artifacts.

Governance documents remain manually maintained and are listed for reference
only.

---

# 2. FILE CLASSIFICATION

Repository files are organized into the following categories:

- Application Source
- Configuration
- Documentation
- Governance
- Machine-readable Project State
- Automation
- Tests
- Scripts
- Database
- User Interface
- Assets

---

# 3. ROOT-LEVEL FILES

Representative repository files include:

- README.md
- LICENSE
- pyproject.toml
- requirements.txt
- project.json
- roadmap.json
- sprint.json
- tests.json

The complete repository inventory shall be generated from repository scanning
to ensure deterministic and reproducible output.

---

# 4. GOVERNANCE DOCUMENTS

The following governance documents are maintained manually:

- PROJECT_SPECIFICATION.md
- ARCHITECTURE.md
- CODING_STANDARDS.md
- DEVELOPMENT_WORKFLOW.md
- DECISION_LOG.md

These documents are excluded from automatic regeneration.


---

# 5. DIRECTORY INVENTORY

Primary Repository Directories

api/

Purpose

Application programming interfaces.

---

core/

Purpose

Core business logic.

---

database/

Purpose

Database models, migrations and persistence.

---

docs/

Purpose

Repository documentation.

---

project_state/

Purpose

Machine-readable project state.

---

scripts/

Purpose

Engineering automation scripts.

---

tests/

Purpose

Repository test suites.

---

tools/

Purpose

Engineering tooling and automation.

---

ui/

Purpose

User interface implementation.

---

# 6. GENERATED DOCUMENTATION

Generated documentation includes:

- PROJECT_CONTEXT.md
- PROJECT_MANIFEST.json
- ROADMAP.md
- PROJECT_STATUS.md
- CHANGELOG.md
- NEXT_TASK.md
- FILE_INDEX.md
- MODULE_INDEX.md
- DEPENDENCY_MAP.md
- TEST_HISTORY.md
- SPRINT_HISTORY.md
- CODE_GENERATION_MANIFEST.md

Generated documentation is recreated from project_state and repository
analysis.


---

# 7. FILE CATEGORIES

Application Source

Purpose

Implements business functionality of the Recruitment Intelligence Platform.

Examples

- api/
- core/
- ui/

---

Configuration

Purpose

Defines repository configuration and application settings.

Examples

- pyproject.toml
- requirements.txt
- configuration files

---

Automation

Purpose

Implements engineering automation.

Examples

- tools/
- scripts/

---

Machine-readable Project State

Purpose

Acts as the authoritative source of generated documentation.

Files

- project.json
- roadmap.json
- sprint.json
- tests.json

---

Documentation

Purpose

Provides generated engineering documentation.

Location

docs/PROJECT_OPERATING_SYSTEM/

---

Governance

Purpose

Provides authoritative engineering policies.

Location

docs/GOVERNANCE/

Generation

Manual Only

---

# 8. INVENTORY PRINCIPLES

Repository inventory generation shall:

- Be deterministic.
- Preserve stable ordering.
- Reflect repository state.
- Exclude temporary files.
- Exclude build artifacts.
- Exclude cache directories.
- Preserve engineering traceability.
- Remain reproducible across executions.


---

# 9. INVENTORY VALIDATION

Repository inventory generation shall verify:

Repository Root

Exists

Documentation Directory

Exists

Governance Directory

Exists

Project State Directory

Exists

Automation Directory

Exists

Application Source

Present

Generated Documentation

Consistent

Repository Structure

Valid

Deterministic Ordering

Verified

---

# 10. INVENTORY EXCLUSIONS

The following content shall be excluded from generated inventories unless
explicitly configured otherwise:

- __pycache__/
- .pytest_cache/
- .mypy_cache/
- .ruff_cache/
- .coverage
- htmlcov/
- .git/
- .venv/
- venv/
- node_modules/
- *.pyc
- *.pyo
- *.tmp
- *.log
- Temporary export directories
- Build artifacts

These exclusions ensure repository inventories remain deterministic and
focused on engineering artifacts.

---

# 11. ENGINEERING REQUIREMENTS

The File Index shall:

- Reflect current repository state.
- Preserve deterministic ordering.
- Support automated regeneration.
- Maintain engineering traceability.
- Preserve frozen architecture.
- Avoid modifying governance documents.
- Remain reproducible across executions.
- Support future repository growth.


---

# 12. RELATED DOCUMENTS

Governance

- PROJECT_SPECIFICATION.md
- ARCHITECTURE.md
- CODING_STANDARDS.md
- DEVELOPMENT_WORKFLOW.md
- DECISION_LOG.md

Generated Documentation

- PROJECT_CONTEXT.md
- PROJECT_MANIFEST.json
- ROADMAP.md
- PROJECT_STATUS.md
- CHANGELOG.md
- NEXT_TASK.md
- MODULE_INDEX.md
- DEPENDENCY_MAP.md
- TEST_HISTORY.md
- SPRINT_HISTORY.md
- CODE_GENERATION_MANIFEST.md

Machine-readable Project State

- project.json
- roadmap.json
- sprint.json
- tests.json

---

# 13. DOCUMENT STATUS

Document Name

FILE_INDEX.md

Classification

Generated Documentation

Owner

Project Operating System

Generation Method

Generated from project_state and repository scan

Update Method

Automatic

Architecture Compatibility

Frozen Architecture

Deterministic Generation

Required

Status

Approved

End of Document

