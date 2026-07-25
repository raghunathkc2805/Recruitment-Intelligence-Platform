# PROJECT STATE SCHEMA

---

## Document Information

| Item | Value |
|------|-------|
| Project | Recruitment Intelligence Platform |
| Document | PROJECT_STATE_SCHEMA |
| Status | Approved |
| Architecture | Frozen |
| Update Method | Automatically Generated |

---

# 1. PURPOSE

This document defines the machine-readable schema used by the Project
Operating System to maintain deterministic project state.

The schema standardizes project metadata, sprint information, roadmap,
testing history, generated artifacts, repository status, and engineering
metrics.

---

# 2. OBJECTIVES

The schema shall:

- Standardize project state.
- Support deterministic automation.
- Preserve engineering traceability.
- Enable reproducible document generation.
- Maintain backward compatibility.
- Preserve frozen architecture.
- Support repository validation.

---

# 3. PRIMARY STATE FILES

The Project Operating System maintains the following state files:

- project.json
- roadmap.json
- sprint.json
- tests.json

These files are the authoritative machine-readable source for all generated
documentation.

---

# 4. SCHEMA DESIGN PRINCIPLES

The schema shall:

- Use deterministic field names.
- Preserve stable object structures.
- Support incremental updates.
- Avoid duplicate records.
- Maintain immutable history where required.
- Preserve compatibility across releases.


---

# 5. PROJECT.JSON SCHEMA

The project.json schema shall include:

Project Identifier

Project Name

Repository Name

Repository Version

Architecture Status

Current Sprint

Overall Completion Percentage

Repository Health

Current Status

Last Updated Timestamp

Engineering Metrics

Repository Statistics

Documentation Statistics

Validation Results

---

# 6. ROADMAP.JSON SCHEMA

The roadmap.json schema shall include:

Roadmap Version

Planning Horizon

Milestones

Sprint Mapping

Dependencies

Priority

Status

Estimated Completion

Engineering Notes

---

# 7. SPRINT.JSON SCHEMA

The sprint.json schema shall include:

Sprint Identifier

Sprint Name

Sprint Status

Objectives

Deliverables

Completed Work

Deferred Work

Repository Version

Validation Status

Engineering Notes


---

# 8. TESTS.JSON SCHEMA

The tests.json schema shall include:

Execution Identifier

Execution Timestamp

Repository Version

Test Framework

Execution Environment

Total Tests

Passed Tests

Failed Tests

Skipped Tests

Execution Duration

Overall Result

Validation Summary

Engineering Notes

---

# 9. COMMON SCHEMA REQUIREMENTS

All Project Operating System state files shall:

- Use UTF-8 encoding.
- Maintain deterministic property names.
- Preserve stable object structures.
- Support incremental updates.
- Prevent duplicate records.
- Preserve immutable historical data where applicable.
- Support automated validation.
- Maintain backward compatibility.

---

# 10. VALIDATION REQUIREMENTS

Every machine-readable state file shall be validated for:

Schema Compliance

Required Fields

Data Type Consistency

Relationship Integrity

Repository Consistency

Architecture Compatibility

Deterministic Structure

Overall Validation Status

Validation shall occur before generated documentation is produced.


---

# 11. RELATED DOCUMENTS

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
- FILE_INDEX.md
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

# 12. DOCUMENT STATUS

Document Name

PROJECT_STATE_SCHEMA.md

Classification

Generated Documentation

Owner

Project Operating System

Generation Method

Automatically Generated

Update Method

Automatic

Architecture Compatibility

Frozen Architecture

Historical Retention

Version Controlled

Deterministic Generation

Required

Status

Approved

End of Document

