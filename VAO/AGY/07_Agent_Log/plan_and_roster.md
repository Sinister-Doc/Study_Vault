# Sub-Agent Roster & Execution Plan — KEA VAO (Village Administrative Officer) 2026

## Overview
This plan coordinates specialized sub-agent tasks to build a complete, high-yield, Obsidian-ready study kit for the KEA Village Administrative Officer (VAO / ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ - formerly Village Accountant) competitive examination. The candidate has ~2–3 days before the exam, requiring maximum syllabus coverage per study hour.

## Sub-Agent Roster & Responsibilities

| Role ID | Role Name | Primary Objective & Deliverables | Dependencies |
| :--- | :--- | :--- | :--- |
| **SAR-01** | **Syllabus & Pattern Analyst** | Extract official KEA notification, exam pattern (Paper 1: General Knowledge, Paper 2: General Kannada, General English, Computer Knowledge), marks, duration, negative marking, section weightage, and official website sources. Output: `02_Syllabus_and_Pattern.md`. | None (Runs first) |
| **SAR-02** | **Resource Scout** | Identify 15–20 verified YouTube videos (coursework, grammar, computer literacy, Karnataka history/geography; no notification/application chatter), authentic PYQ PDFs, and study portals. Output: `05_Resources/` and `07_Agent_Log/YouTube_Links.md`. | SAR-01 |
| **SAR-03** | **Content Distiller** | Ingest transcripts from key grammar, computer knowledge, and Karnataka GK videos via yt-dlp/subtitles; distil core rules, vocabulary lists, shortcut keys, and administrative functions into high-density reference digests. Output: `05_Resources/YouTube_Transcripts/`. | SAR-02 |
| **SAR-04** | **Subject Tutors (GK, Languages, Computer)** | Produce exam-oriented revision notes for: General Knowledge (Karnataka & India History, Geography, Polity, Economy), General Kannada (ವ್ಯಾಕರಣ, ಸಂಧಿ, ಸಮಾಸ, ತತ್ಸಮ-ತದ್ಭವ, ಗಾದೆಗಳು), General English (Grammar, Vocabulary, Idioms, Comprehension), and Computer Knowledge (Hardware, Software, MS Office, Internet, Cybersecurity). Output: `03_Notes/`. | SAR-01, SAR-03 |
| **SAR-05** | **Current Affairs & Karnataka GK Researcher** | Compile high-yield Karnataka state events, government welfare schemes (Guarantee schemes, Gruha Lakshmi, Yuva Nidhi, etc.), revenue administration systems (Bhoomi, RTC/Pahani, e-Swathu), and national current affairs. Output: `04_Current_Affairs_GK/`. | SAR-01 |
| **SAR-06** | **PYQ & Question Analyst** | Analyze previous VAO / Village Accountant question papers (KEA / KPSC), identify recurring grammar patterns, computer terminology, and compile "Most Expected Questions". Output: `05_Resources/PYQ_Analysis.md` & embedded note sections. | SAR-01, SAR-02 |
| **SAR-07** | **Visual Learning Designer** | Review all notes to embed clean Obsidian-compatible Mermaid diagrams (Grammar classification trees, Revenue administration hierarchy, Computer architecture/network topologies, Constitutional organs) with prose explanations, tables, and mnemonics. Output: Enriched `03_Notes/` and `04_Current_Affairs_GK/`. | SAR-04, SAR-05 |
| **SAR-08** | **Mock Test Engineer** | Construct 2–3 fully offline, standalone HTML mock tests matching exact KEA question count, timer, negative marking (1/4th if applicable), question palette, mark for review, subject-wise scoring, and answer keys with explanations. Output: `06_Mock_Tests/`. | SAR-01, SAR-06 |
| **SAR-09** | **Study Planner & Vault Librarian** | Create the master index (`00_START_HERE.md`), hour-by-hour 3-day high-yield study plan and compressed 2-day track (`01_Study_Plan.md`), and ensure bidirectional [[wikilinks]]. | SAR-01 through SAR-08 |
| **SAR-10** | **QA Reviewer** | Rigorously test all external URLs, Obsidian wikilinks, Mermaid syntax, HTML mock test offline execution (timer, scoring, review), and document findings in `07_Agent_Log/qa_report.md`. | All prior deliverables |

## Execution Sequence
```mermaid
flowchart TD
    A[SAR-01: Syllabus & Pattern] --> B[SAR-02: Resource Scout]
    A --> E[SAR-05: Current Affairs & GK]
    A --> F[SAR-06: PYQ & Question Analyst]
    B --> C[SAR-03: Content Distiller]
    C --> D[SAR-04: Subject Tutors]
    F --> D
    D --> H[SAR-08: Mock Test Engineer]
    F --> H
    D --> G[SAR-07: Visual Learning Designer]
    E --> G
    G --> I[SAR-09: Study Planner & Librarian]
    H --> I
    I --> J[SAR-10: QA Reviewer]
```

## Known Constraints & Verification Checkpoints
- Real links only: All YouTube URLs must be verified via yt-dlp or curl/HTTP status.
- Official KEA weightage and negative marking rules must be strictly adhered to.
- Notes must feature clear bilingual terminology where relevant (English & Kannada for administrative terms, revenue terms).
- Offline HTML Mock Tests must be single self-contained files with no external dependencies.
