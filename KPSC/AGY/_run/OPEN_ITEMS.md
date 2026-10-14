# Open Items and Examination Deliberations Log
**Run As-of Date**: 2026-10-13 (Tuesday, 13 October 2026)
**Target Exam**: KPSC Gazetted Probationers (KAS) 2026-27 (Group A & Group B Services)

---

## 1. Resolved Items & Clarified Examination Facts

1. **Personality Test (Interview) Marks**:
   - *Issue*: Historical coaching material references 200 marks for the interview.
   - *Resolution*: Confirmed as **25 Marks** under the Karnataka Recruitment of Gazetted Probationers (Appointment by Competitive Examinations) (Amendment) Rules, 2022 (DPAR 20 SSR 2022 Dt: 12-04-2022). Total aggregate merit is $1250 + 25 = 1275$ Marks.
2. **Negative Marking Scheme**:
   - *Issue*: Some portal mock tests use 1/3rd negative marking (UPSC pattern).
   - *Resolution*: Confirmed strictly **one-fourth (0.25) deduction** per wrong answer (0.50 marks deducted for 2-mark questions) per KPSC 10th Amendment Rules 2013 and official notification section 4(1)(b).
3. **Optional Subjects Elimination**:
   - *Issue*: Clarifying whether optional subjects exist in Mains.
   - *Resolution*: Reconfirmed that optional subjects were completely abolished under the 2014 revised pattern; Mains consists strictly of 2 Qualifying Language papers + Essay + 4 General Studies papers (GS-1 to GS-4).
4. **Candidate Category & Context**:
   - *Issue*: Candidate application context redaction.
   - *Resolution*: Candidate is competing under General Merit (GM) with B.E. qualification. No reservations claimed for Kannada Medium, Rural, PH, Ex-serviceman, or Kalyana Karnataka 371J. All personal candidate identifiers (PII) were redacted and unredacted raw files permanently purged.
5. **Current Affairs Monthly Source Verification (Round 2)**:
   - *Issue*: Official DIPR Karnataka portal (`karnatakavarthe.org`) blocks bot user-agents with HTTP 403 Forbidden.
   - *Resolution*: Sourced high-quality, free public monthly current affairs magazines from IASbaba's public archive. Cross-verified all facts against official PIB releases, Karnataka State Gazette notifications, and Supreme Court judgments. Registered all 9 monthly PDFs with SHA-256 in `_sources/magazines/MANIFEST.md`.
6. **Computer-Based Test (CBT) Offline Portability (Round 2)**:
   - *Issue*: Browser local storage policies when running HTML via `file://` URIs can throw exceptions if security settings restrict storage access.
   - *Resolution*: Wrapped `localStorage` state access in safe `try/catch` fallbacks, allowing full in-memory interactive test-taking, question navigation, timer, scoring, and review mode even in locked sandbox browsers.
7. **CBT Engine Wall-Clock Timer Synchronization (Round 3)**:
   - *Issue*: Standard `setInterval` countdown drifted over long 120-minute sessions and reset elapsed dwell time upon page reloads.
   - *Resolution*: Replaced decrementing counter with an absolute end timestamp derived from the system wall clock (`Date.now() + durationMs`), persisted in `localStorage`. The timer computes remaining seconds dynamically on every tick, eliminating drift and reload cheating. Implemented automatic auto-submit at zero, alongside a 2-minute "Quick Check" mode for candidate verification.
8. **Answer Keying & Raw Competitive Scoring (Round 3)**:
   - *Issue*: Storing candidate selections by array index corrupted state during section filtering; clamping scores with `Math.max(0, ...)` masked negative penalty marks.
   - *Resolution*: Keyed all responses strictly by stable question IDs (`q.id`) and option IDs (`opt.id`). Rewrote evaluation as a pure function calculating exact raw competitive scores (allowing true negative marks) and providing detailed per-section and per-topic performance breakdowns.
9. **History & Geography Notes Tiered Separation (Round 3)**:
   - *Issue*: Brief overview notes and new textbook-depth notes resided in the same flat folder, causing navigation redundancy.
   - *Resolution*: Reorganised into clean `01_Textbook_Notes/` (main study material) and `Quick_Revision/` (renamed `<Topic> - Quick Revision.md` with aliases) folders, connected via comprehensive subject hub notes (`Karnataka_History_Hub.md` and `Karnataka_Geography_Hub.md`).

---

## 2. Monitored Items for Candidate Awareness

1. **Tentative Preliminary Exam Date (15 November 2026)**:
   - *Status*: The Commission notified 15-11-2026 as the tentative examination date. Candidate must monitor `https://kpsc.kar.nic.in` for the release of formal admission tickets (Hall Tickets) typically issued 10 to 14 days prior to the examination date.
2. **Implementation of SC Internal Sub-Classification (Justice Sadashiva Report)**:
   - *Status*: Following the landmark 7-judge Supreme Court ruling in August 2024 upholding state legislative power for internal sub-classification, the state cabinet is evaluating data metrics. Candidates should monitor any formal Government Orders (GO) issued prior to the final merit ranking.
3. **KPSC Corrigenda on Examination Centers**:
   - *Status*: Any district-level exam venue reallocations will be updated directly on the KPSC web portal.

---

> [!summary]
> All open items are non-blocking. The study vault is completely self-contained, validated, and ready for immediate examination preparation.
