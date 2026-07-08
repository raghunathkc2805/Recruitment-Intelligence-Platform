# Recruitment Automation Suite (RAS)

## Version

**2.2.0 Baseline**

---

# Overview

Recruitment Automation Suite (RAS) is an enterprise recruitment automation platform built using Microsoft Outlook VBA, Microsoft Excel and Python.

The platform automates the complete recruitment lifecycle by processing Outlook emails, maintaining a centralized recruitment database, managing candidate records, tracking offers, interviews, background verification, apprenticeship programs (NATS/NAPS), and generating recruitment dashboards.

The system is designed specifically for high-volume recruitment operations and is configurable through Excel without requiring VBA code changes for routine administration.

---

# Key Features

* Outlook Email Processing
* Automatic Email Classification
* Candidate Management
* Resume Management
* Attachment Management
* Offer Tracking
* Interview Tracking
* Background Verification Tracking
* Deviation Tracking
* NATS Management
* NAPS Management
* Candidate Timeline
* Recruiter Dashboard
* KPI Reporting
* Power BI Integration
* Resume Intelligence (Version 2.2)
* AI Recruitment Assistant (Version 3.0)

---

# Technology Stack

| Component         | Technology            |
| ----------------- | --------------------- |
| Email Integration | Microsoft Outlook VBA |
| Database          | Microsoft Excel       |
| Resume Parsing    | Python                |
| Dashboard         | Power BI              |
| Documentation     | Markdown              |

---

# Folder Structure

```text
Recruitment Automation Version 2
│
├── Database
├── Backup
├── Logs
├── Reports
├── Candidates
├── Resumes
├── Offer Letters
├── BGV
├── Interview
├── Power BI
├── Resume Parser
├── Source
│   ├── VBA
│   ├── Releases
│   ├── Documentation
│   └── Tests
└── Test Data
```

---

# Project Modules

## Core Engine

* Configuration
* Settings
* Logger
* Utilities
* Excel Engine

## Outlook Engine

* Mail Scanner
* Mail Classifier
* Dispatcher
* Duplicate Detection

## Recruitment Engine

* Candidate Engine
* Resource Engine
* Resume Engine
* Attachment Engine
* Offer Engine
* Interview Engine
* BGV Engine
* Deviation Engine
* NATS Engine
* NAPS Engine

---

# Database

Current Database Version

**39+ Worksheets**

Major tables include:

* Candidates_Master
* Resources
* Offers
* Interviews
* BGV
* NATS
* NAPS
* Attachments
* Candidate Timeline
* Resume Parser

---

# Current Status

Current Version:

**2.2.0 Baseline**

Project Status:

Stable

Compile Status:

No Compile Errors

Architecture:

Frozen

---

# Roadmap

## Version 2.2

Resume Intelligence Platform

## Version 2.3

Recruitment Dashboard

## Version 2.4

Power BI Integration

## Version 3.0

AI Recruitment Assistant

---

# Development Standards

* All modules must compile successfully before release.
* Every public procedure must include error handling.
* Every business transaction must use CandidateID.
* Every major change requires a new version.
* Database structure remains stable unless a major version requires migration.

---

# Author

Project Owner:
Raghunath K C

Platform:
Recruitment Automation Suite (RAS)

Current Release:
Version 2.2.0 Baseline
