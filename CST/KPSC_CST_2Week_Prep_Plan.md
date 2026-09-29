---
tags:
  - kpsc
  - cst
  - exam-prep
  - plan-b
created: 2026-08-25
exam: KPSC Computer Teachers (CST) Recruitment
duration: 14 days, 4-5 hrs/day
---

# KPSC Computer Teachers (CST) — 2-Week Prep Plan

> Backup-plan prep, built on an ECE (VTU, 2018 scheme) background + 1.5 yrs Boeing India (Systems Engineering) + 4-5 months Golang backend internship.
> Self-assessed: **strong** in Data Structures & Algorithms and AI basics. **Everything else treated as fresh**, including the rest of Paper 2's CS core.

---

## 0. Exam Shape (from official syllabus)

| Paper | Sections |
|---|---|
| **Paper 1 (General)** | GK, Current Affairs, ಸಾಮಾನ್ಯ ಕನ್ನಡ (Kannada), General English, Educational Psychology (ಶೈಕ್ಷಣಿಕ ಮನೋವಿಜ್ಞಾನ), Computer Literacy, Health Education (ಆರೋಗ್ಯ ಶಿಕ್ಷಣ), Value Education (ಮೌಲ್ಯ ಶಿಕ್ಷಣ) |
| **Paper 2 (CST — Computer Science)** | 10 units: Fundamentals of Computers → AI |

**Strategy for the 14 days:** front-load the Paper 2 CS units (your natural strength as an engineer, even where topics are technically "fresh" — you'll absorb them faster than a non-CS candidate), then dedicate focused blocks to the Paper 1 sections that have zero overlap with your engineering background (Educational Psychology, Kannada grammar, Value/Health Education), and close with GK/Current Affairs + full revision + mocks.

> [!TIP] 🎥 Curated Video Lectures & Study Guides (from Papa's Recommendations)
> - **CST Master Video Hub**: [[CST_Computer_Teacher_Study_Resources]] (27 mapped lectures, logic gate sessions, previous solved papers)
> - **Unit 1 Study Guide**: [[Unit01_Fundamentals_of_Computer_Study_Guide]] (Von Neumann architecture, generations, memory hierarchy, motherboard assembly)
> - **Full Master Study Catalog**: [[Master_YouTube_Study_Catalog]] (all 100 competitive exam resources across UPSC, KPSC, CST, and Banking)

---

## 1. Full Detailed Syllabus

### PAPER 2 — Computer Science (10 Units)

**Unit 1 — Fundamentals of Computers**
Functional components, evolution & generations of computers, classification, applications, I/O & memory devices, software concepts, problem-solving methodology, word processing/spreadsheets/PPT, motherboard types & components, memory, power supply, assembling a system.
- 🎥 **Core Lecture**: [Unit 01 Fundamentals of Computer — Statecraft IAS Academy (41m)](https://youtu.be/OvboDQ1Fi44) `(Kannada)` | Detailed Notes: [[Unit01_Fundamentals_of_Computer_Study_Guide]]
- 🎥 **Chapter 1 Full Course**: [Complete Computer Course Part 1 — Spardha Tejas (11h 55m)](https://www.youtube.com/live/0l7uwv7LC0A) `(Kannada)`
- 🎥 **Classification & Hardware**: [Classification and Applications of Computers — Learn with Maktum (41m)](https://youtu.be/vWE2Kjb1R-Y) `(Kannada)`
- 🎥 **Inventions & Pioneers**: [Computer Inventions & Inventors — Sadhana School (24m)](https://youtu.be/rmNaX7g3agQ) `(Kannada)`
- 🎥 **Chapter 1 MCQs**: [Computer Chapter 1 MCQ Series — Samara Academy (1h 14m)](https://www.youtube.com/live/WaKFTxqx1I0) `(Kannada)`

**Unit 2 — Discrete Structures and Optimization**
- Mathematical Logic: propositional & predicate logic, equivalences, normal forms, quantifiers, rules of inference
- Sets & Relations: operations, representation, equivalence relations, partial ordering
- Counting, Induction, Probability: pigeonhole principle, permutations/combinations, inclusion-exclusion, mathematical induction, probability, Bayes' theorem
- Graph Theory: simple/multi/weighted graphs, paths & circuits, shortest paths, Euler & Hamiltonian paths, planar graphs, graph coloring, bipartite graphs, trees, spanning trees, cut-sets
- Boolean Algebra: functions, representation, simplification

**Unit 3 — Computer System Architecture**
- Digital Logic: gates, K-maps, combinational/sequential circuits, flip-flops, decoders, multiplexers, registers, counters, memory unit
- 🎥 **Digital Logic & Logic Gates**: [Computer Science Teacher: Logic Gates — Dr. Gururaj Bulbule, Sadhana Academy (25m)](https://youtu.be/kodEefWzx5s) `(Kannada)`
- Data Representation: number systems, complements, fixed/floating point, error detection codes, computer arithmetic
- Basic Computer Organization: stored program, registers, instructions, timing/control, instruction cycle, memory-reference instructions, I/O, interrupts
- Programming the Basic Computer: machine/assembly language, assembler, loops, subroutines
- CPU: register organization, stack organization, instruction formats, addressing modes, RISC vs CISC
- I/O Organization: peripherals, interfaces, async data transfer, modes of transfer, priority interrupt, DMA, serial comm
- Memory Hierarchy: main/auxiliary/associative/cache/virtual memory

**Unit 4 — Programming Languages & Computer Graphics**
- Language design/translation, paradigms, syntax, translation stages
- Elementary Data Types: scalar & composite
- Programming in C: tokens, data types, control flow, arrays, structures, unions, strings, pointers, functions, file handling, command-line args, preprocessors
- OOP: class, object, instantiation, inheritance, encapsulation, abstract class, polymorphism
- Programming in C++: tokens, operators, control statements, parameter passing, virtual functions, constructors/destructors, overloading, inheritance, templates, exceptions, streams/files
- Web Programming: HTML, DHTML, CSS, XML, JavaScript

**Unit 5 — Database Management Systems**
- DB architecture: data models, schemas, 3-schema architecture, data independence, centralized/client-server
- Data Modelling: ER diagrams, relational model, constraints, relational algebra & calculus
- SQL: DDL/DML, data types, aggregate functions, constraints, queries, views, stored procedures, triggers, SQL injection
- Normalization: anomalies, functional dependencies, normal forms, query processing/optimization, transactions, concurrency control, recovery
- Data Warehousing & Mining: OLAP/OLTP, association rules, classification, clustering, regression

**Unit 6 — System Software and Operating Systems**
- System Software: assemblers, compilers/interpreters, loading/linking/relocation, macros, debuggers
- OS Basics: structure, services, system calls, design, boot process
- Process Management: scheduling, IPC, synchronization, critical section, Peterson's solution, semaphores
- Threads: multicore programming, multithreading models, thread libraries
- CPU Scheduling: criteria, algorithms, multi-processor & real-time scheduling
- Deadlocks: characterization, prevention, avoidance, detection, recovery
- Memory Management: contiguous allocation, paging, segmentation, demand paging, page replacement, thrashing
- Storage Management: mass storage, disk scheduling, RAID
- File & I/O Systems: access methods, directory structure, allocation methods, free space management
- Security: protection, access control, cryptography, authentication
- Linux & Windows OS: design principles, components, file systems

**Unit 7 — Software Engineering**
- Process Models: generic model, prescriptive models, Agile (XP, Scrum, DSDM, FDD)
- Requirements: functional/non-functional, use cases, SRS
- Design: abstraction, architecture, patterns, cohesion/coupling, OOD
- Testing: verification/validation, unit/integration testing, white-box/black-box, regression, performance, stress testing

**Unit 8 — Data Structures and Algorithms** *(you're already strong here — light revision pass)*
- Arrays, sparse matrix, stacks, queues, priority queues, linked lists, trees (binary, threaded, BST, AVL), graphs, sorting/searching, hashing
- Complexity: time/space, asymptotic notation, recurrence relations
- Design techniques: divide & conquer, DP, greedy, backtracking, branch & bound
- Graph algorithms: BFS, DFS, shortest paths, max flow, MST
- Complexity theory: P vs NP, NP-completeness

**Unit 9 — Data Communication and Computer Networks**
- Data Comm: components, transmission modes, analog/digital signals, bandwidth/throughput/latency, encoding, multiplexing, transmission media, errors
- Networks: topologies, LAN/MAN/WAN, wireless, internet
- Network Models: OSI, TCP/IP, addressing, switching
- Protocols: framing, error/flow control, sliding window, HDLC, CSMA/CD/CA, FDMA/CDMA/TDMA
- IP: IPv4/IPv6, addressing, fragmentation, ARP, routing, TCP/UDP/SCTP
- WWW: URL, DNS, email (SMTP/POP/IMAP), TELNET, FTP
- Security: malware, cryptography, digital signatures, VPN, firewalls
- Mobile Tech: GSM/CDMA, mobile IP, wireless LANs
- Cloud & IoT: SaaS/PaaS/IaaS, virtualization, cloud storage, IoT basics

**Unit 10 — Artificial Intelligence** *(you're already fairly strong here — light revision pass)*
- Approaches: Turing test, rational agents, state space, heuristic search, game playing
- Knowledge Representation: logic, semantic networks, frames, rules, ontologies, expert systems
- Problem Solving: BFS/DFS, A*, bidirectional/greedy best-first search
- NLP: grammar, parsing, semantic analysis
- ANN: supervised/unsupervised/reinforcement learning

---

### PAPER 1 — General

**1. General Knowledge** — famous books/authors, inventions & discoveries, basic science, health & hygiene, Karnataka history/culture/art, Indian history (ancient/medieval/modern), world history chronology, geography (land, people, festivals, population, literacy, natural resources, food crops), Indian economy (industries, public undertakings), awards & honours, Indian Constitution (rights, legislature, executive, judiciary), current affairs (international/national/state), basics of computers.

**2. Current Affairs** — international & national affairs, movies, currency & capitals, important days/slogans, festivals/folk dance/tribes, UN & HQs, education initiatives in India, monuments & forests, tourist places & peaks, industries & ores, three wings of army, Constitution, highways/railways/airports, abbreviations.

**3. ಸಾಮಾನ್ಯ ಕನ್ನಡ (General Kannada)** — ವರ್ಣಮಾಲೆ, ನಾಮಪದ, ಸರ್ವನಾಮ, ಕ್ರಿಯಾಪದ, ಲಿಂಗ-ವಚನ, ವಿಭಕ್ತಿ ಪ್ರತ್ಯಯ, ಸಂಧಿ, ಸಮಾಸ, ಕೃದಂತ-ತದ್ಧಿತಾಂತ, ಗಾದೆಗಳು, ಅವ್ಯಯ, ವಾಕ್ಯ ರಚನೆ, ಲೇಖನ ಚಿಹ್ನೆಗಳು, ಪದಗಳ ಅರ್ಥ/ಸಮಾನಾರ್ಥಕ/ವಿರುದ್ಧಾರ್ಥಕ, ಛಂದಸ್ಸು-ಅಲಂಕಾರ, ಹಳಗನ್ನಡ & ಹೊಸಗನ್ನಡ ಸಾಹಿತ್ಯ ಚರಿತ್ರೆ.
- 🎥 **Comprehensive Grammar**: [Complete Kannada Grammar — Chethana Academy (4h 12m)](https://youtu.be/lHAV0r6sHVY) `(Kannada)`
- 🎥 **Exam Grammar Practice**: [Kannada for VAO & Competitive Exams (36m)](https://youtu.be/ea4PUB-DGeU) `(Kannada)`

**4. General English** — parts of speech, tense/aspect, auxiliaries & modals, phonology, punctuation, phrasal verbs/idioms, transformations (voice, degrees of comparison, sentence types, reported speech, clauses), comprehension passages, letter writing.
- 🎥 **Paper 1 English Class**: [GPSTR English Paper-1 — Suresh B N, Jnana Gangothri (1h 14m)](https://youtu.be/CzKWRJgdu3Y) `(Kannada/English)`

**5. Educational Psychology** — meaning/scope, methods, growth & development, childhood & adolescence, individual differences, intelligence & IQ, gifted/backward/creative children, emotional intelligence (Goleman), learning & factors affecting it (maturation, motivation-Maslow, attention, memory), transfer of learning, learning styles & domains (cognitive/affective/psychomotor), 21st-century skills, theories of learning (trial & error, classical/operant conditioning, insight, social learning), personality (Freud), cognitive development (Piaget, Vygotsky, Bruner), mental health, adjustment/frustration/stress/conflict, defense mechanisms.
- 🎥 **Pedagogy Marathon**: [Educational Psychology (ಮನೋವಿಜ್ಞಾನ) Complete Class — Shrishail Sir, Payana Academy (2h 45m)](https://www.youtube.com/live/VxWM_ZAkkHc) `(Kannada)`

**6. Computer Literacy** — intro to computers, categories & languages, hardware/software; OS types (Linux, Mac, Windows); application software (MS Office, PowerPoint, Excel formulas/charts, Paint); Google Workspace (Classroom, Forms, Drive); internet basics (URL/ISP/LAN/WAN/WWW, browsers, servers), email; Nudi & Baraha (Kannada typing software); AI basics; cyber security & cyber law.
- 🎥 **Guaranteed Scoring Guide**: [Computer Literacy 5-10 Marks Guaranteed — Teacher's Academy (42m)](https://youtu.be/RAAi5WtSJDo) `(Kannada)`
- 🎥 **Speed MCQ Sprint**: [Computer Literacy 100 MCQs in 40 Minutes — Know Now Muniraju (37m)](https://youtu.be/0XvQOtmDT9M) `(Kannada)`
- 🎥 **Past Years Solved**: [Solved GPSTR Computer Papers 2015-2022 — Ananthagnanadhare (50m)](https://youtu.be/ascjrEwGESo) `(Kannada)`
- 🎥 **Rapid MCQs**: [Top 50 Computer MCQs — GK Power (9m)](https://youtu.be/jigRsaw6Jrs) & [Computer Basic Top 50 — Computer Tech Academy (9m)](https://youtu.be/w3X-hrm4DoE)

**7. Health Education** — meaning/importance, communicable & non-communicable diseases, mental health, nutrition & balanced diet, adolescent/reproductive health, RTIs/STIs, self-confidence & growth, drug abuse, sexual harassment awareness, social health, first aid & safety, physical exercise/yoga/pranayama/meditation.

**8. Value Education** — meaning/definition/classification of values (universal, human, moral, national, social), teaching methods (direct/indirect/incidental), theories of goodness, human behavior rules/theories, utilitarianism, character & personality development, values in sustainable development.

---

## 2. Self-Assessment Snapshot

| Status | Topics |
|---|---|
| ✅ **Strong (light revision only)** | Data Structures & Algorithms (Unit 8), AI Basics (Unit 10) |
| 🟡 **Fresh but engineering-adjacent (should move fast)** | Fundamentals of Computers, Discrete Structures, Computer Architecture, Programming (C/C++/OOP/Web), DBMS, OS, Software Engineering, Computer Networks |
| 🔴 **Fully fresh, no prior exposure (needs dedicated slow blocks)** | Educational Psychology, Kannada grammar, Value Education, Health Education, GK/Current Affairs, General English |

---

## 3. Daily Plan — 14 Days, 4-5 hrs/day

> Format per day: `[Time block] — Topic — Resource — Obsidian note to create`
> Build one Obsidian note per unit; link them under a `#kpsc-cst` MOC (Map of Content).

### Week 1 — Paper 2 (Computer Science Core)

**Day 1 — Fundamentals of Computers + Discrete Math Part 1**
- 09:00–11:00 — Fundamentals of Computers (all topics) → *P.K. Sinha & P. Sinha, "Computer Fundamentals"* (syllabus's own reference)
  - 🎥 **Video Companion**: [Unit 01 Fundamentals of Computer — Statecraft IAS Academy (41m)](https://youtu.be/OvboDQ1Fi44) | Study Guide: [[Unit01_Fundamentals_of_Computer_Study_Guide]]
- 11:15–13:15 — Mathematical Logic + Sets & Relations → *Kenneth Rosen, "Discrete Mathematics and Its Applications"* (Ch. 1–2, 9)
- 14:00–15:00 — Notes consolidation + flashcards in Obsidian

**Day 2 — Discrete Math Part 2 + Boolean Algebra**
- 09:00–11:00 — Counting, Induction, Probability, Bayes' Theorem → Rosen Ch. 5–7
- 11:15–13:00 — Graph Theory (paths, trees, coloring, spanning trees) → Rosen Ch. 10–11
- 13:45–14:45 — Boolean Algebra & simplification → any digital logic text (Morris Mano, Ch. 2–3)
  - 🎥 **Video Companion**: [Logic Gates & Digital Logic — Dr. Gururaj Bulbule, Sadhana Academy (25m)](https://youtu.be/kodEefWzx5s)
- 15:00–16:00 — Practice MCQs (search "discrete mathematics MCQ" sets / GATE-level questions — fast diagnostic)

**Day 3 — Computer System Architecture**
- 09:00–11:00 — Digital Logic Circuits, Data Representation, Computer Arithmetic → *Morris Mano, "Digital Logic and Computer Design"*
- 11:15–13:15 — Basic Computer Organization, CPU (registers, addressing modes, RISC/CISC) → Morris Mano, "Computer System Architecture"
- 14:00–15:30 — Memory Hierarchy, I/O Organization
- 15:30–16:00 — Notes + diagram sketches (instruction cycle, memory hierarchy) in Obsidian using Excalidraw plugin

**Day 4 — Programming (C/C++/OOP) + Web**
- 09:00–11:00 — C fundamentals refresh (pointers, structures, file handling) — you likely have solid recall from ECE/Golang background; skim fast
- 11:15–13:00 — OOP concepts (class, inheritance, polymorphism) + C++ specifics (virtual functions, templates, exceptions) → *E. Balagurusamy, "Object-Oriented Programming with C++"*
- 13:45–15:00 — Web Programming basics: HTML/CSS/JS/XML fundamentals (MDN Web Docs / W3Schools — fast reference reads)
- 15:00–16:00 — MCQ practice + notes

**Day 5 — DBMS & SQL**
- 09:00–11:00 — DB architecture, ER modeling, relational model, normalization → *Elmasri & Navathe, "Fundamentals of Database Systems"* (syllabus reference)
- 11:15–13:15 — SQL (DDL/DML, joins, aggregate functions, views, triggers, SQL injection) → hands-on practice on SQLZoo or a local SQLite sandbox
- 14:00–15:30 — Transactions, concurrency control, recovery, OLAP/OLTP, data mining basics
- 15:30–16:00 — Notes + write 10 sample SQL queries from memory

**Day 6 — Operating Systems**
- 09:00–11:00 — OS structure, process management, scheduling algorithms → *Silberschatz, Galvin, "Operating System Concepts"* (aligns with syllabus)
- 11:15–13:00 — Synchronization (semaphores, Peterson's solution), deadlocks
- 13:45–15:15 — Memory management (paging, segmentation, virtual memory), file systems
- 15:15–16:00 — Linux vs Windows design comparison + security/cryptography basics

**Day 7 — Software Engineering + DSA Light Revision**
- 09:00–10:30 — SE process models (Agile/Scrum/XP), requirements, SRS → *Ian Sommerville / Roger Pressman* (syllabus references)
- 10:45–12:00 — Software design principles, testing types (white-box/black-box, regression)
- 13:00–15:00 — DSA revision (light, since you're strong): sorting/searching complexity, tree traversals, graph algorithms (BFS/DFS/Dijkstra/MST), DP patterns — timed problem-solving on LeetCode/GfG to stay sharp
- 15:00–16:00 — Week 1 consolidation: review all Obsidian notes, self-quiz on flashcards

### Week 2 — Networks, AI (light), Paper 1, and Revision

**Day 8 — Computer Networks & Data Communication**
- 09:00–11:00 — Data comm fundamentals, transmission, encoding, multiplexing → *Behrouz Forouzan, "Data Communications and Networking"* (syllabus reference)
- 11:15–13:15 — OSI/TCP-IP models, IPv4/IPv6, routing, TCP/UDP → *Tanenbaum, "Computer Networks"* (syllabus reference)
- 14:00–15:15 — Network security, mobile tech (GSM/CDMA), cloud computing & IoT basics
- 15:15–16:00 — Notes + protocol comparison table (OSI vs TCP/IP layers)

**Day 9 — AI (light) + Computer Literacy (Paper 1)**
- 09:00–10:30 — AI revision (light, since you're strong): search algorithms, knowledge representation, ANN basics — quick recap, no need for deep dive
- 10:45–12:15 — Computer Literacy: MS Office suite specifics, Google Workspace tools, Nudi/Baraha (Kannada typing tools — note these are exam-specific, look up briefly), cyber law basics
  - 🎥 **Video Companions**: [Computer Literacy 5-10 Marks Guaranteed — Teacher's Academy (42m)](https://youtu.be/RAAi5WtSJDo) | [Computer Literacy 100 MCQs — Know Now Muniraju (37m)](https://youtu.be/0XvQOtmDT9M)
- 13:00–15:00 — Full Paper 2 rapid-fire MCQ round (mix all 10 units) — use this to flag weak spots for Day 14 revision
- 15:00–16:00 — Update weak-spot list in Obsidian

**Day 10 — Educational Psychology (heaviest fresh topic — full day)**
- 09:00–11:00 — Growth & development, childhood/adolescence, individual differences, intelligence & IQ
- 11:15–13:00 — Learning theories (classical/operant conditioning, insight, social learning), motivation (Maslow), memory, attention
- 14:00–15:30 — Cognitive development (Piaget, Vygotsky, Bruner), personality (Freud), emotional intelligence (Goleman)
- 15:30–16:00 — Mental health, adjustment/stress/defense mechanisms
  - 🎥 **Video Companion**: [Educational Psychology (ಮನೋವಿಜ್ಞಾನ) Complete Class — Shrishail Sir, Payana Academy (2h 45m)](https://www.youtube.com/live/VxWM_ZAkkHc)
- *Resource:* Anita Woolfolk or S.K. Mangal's "Educational Psychology" (both listed in official syllabus references) — these are the highest-yield single resource for this section

**Day 11 — Kannada + General English**
- 09:00–11:00 — ಕನ್ನಡ ವ್ಯಾಕರಣ: ಸಂಧಿ, ಸಮಾಸ, ವಿಭಕ್ತಿ, ಕೃದಂತ-ತದ್ಧಿತಾಂತ, ಗಾದೆಗಳು → ತೀ.ನಂ.ಶ್ರೀಕಂಠಯ್ಯ's grammar text (syllabus reference) or KTBS 8th–10th std Kannada textbooks (fastest refresher)
  - 🎥 **Video Companion (Kannada)**: [Complete Kannada Grammar — Chethana Academy (4h 12m)](https://youtu.be/lHAV0r6sHVY)
- 11:15–12:30 — ಹಳಗನ್ನಡ/ಹೊಸಗನ್ನಡ ಸಾಹಿತ್ಯ ಚರಿತ್ರೆ (literature history) — skim key poets/periods only, don't over-invest
- 13:15–14:45 — English: tenses, active/passive voice, reported speech, clauses → Wren & Martin or Raymond Murphy's "Essential English Grammar" (both syllabus references)
  - 🎥 **Video Companion (English)**: [GPSTR English Paper-1 — Suresh B N, Jnana Gangothri (1h 14m)](https://youtu.be/CzKWRJgdu3Y)
- 14:45–16:00 — Comprehension practice + letter writing format

**Day 12 — GK: History, Geography, Economy, Constitution**
- 09:00–10:30 — Indian & Karnataka history (ancient/medieval/modern), Karnataka culture & art
  - 🎥 **History Companion**: [Complete Karnataka History Mega Episode — Shankaranand Banashankari (10h 38m)](https://youtu.be/hMqU4gE_yxM)
- 10:45–12:00 — Geography basics, Indian economy (industries, public undertakings)
  - 🎥 **Geography & Rivers**: [Cauvery River Basin — Classic Education (33m)](https://youtu.be/0oPY66rWSGo) | [Krishna River System (15m)](https://youtu.be/RM3cgHwQ3jI) | [Complete 9th Std Geography Marathon (2h 19m)](https://youtu.be/P12Ygye5zyE)
- 12:45–14:00 — Indian Constitution (fundamental rights, legislature, executive, judiciary)
  - 🎥 **Constitution Revision**: [Complete Indian Constitution in Kannada — Classic Education (3h 50m)](https://youtu.be/CyQmNKsjisw) | [12-Hour Mega Analysis — Satish Joga DCTE (11h 53m)](https://youtu.be/wA2C4Zu-BT8)
- 14:00–15:30 — Books/authors, inventions/discoveries, awards & honours, basic science
- *Resource:* Lucent's GK or M. Laxmikanth's "Indian Polity" (for Constitution section) — standard for this kind of exam
- 15:30–16:00 — Flashcard creation for rapid-recall facts (dates, names, awards)

**Day 13 — Current Affairs + Health Education + Value Education**
- 09:00–10:30 — Current affairs (last 6-12 months): national/international, awards, days/slogans, sports → any monthly current affairs digest (PIB summaries, monthly GK capsules)
- 10:45–12:00 — Currency/capitals, UN & HQs, festivals/folk dance/tribes, monuments/forests, tourist spots
- 13:00–14:00 — Health Education: communicable/non-communicable diseases, nutrition, first aid, yoga
- 14:15–15:15 — Value Education: values classification, teaching methods, theories of goodness/behavior
- 15:15–16:00 — Notes consolidation

**Day 14 — Full Revision + Mock Tests**
- 09:00–10:30 — Weak-spot sweep (from Day 9's flagged list) — Paper 2
- 10:45–12:00 — Weak-spot sweep — Paper 1 (Psychology, Kannada, GK)
- 13:00–14:30 — Full-length mock test (Paper 1 + Paper 2, timed) if a mock series is available; else, self-test using flashcards across all 18 topic notes
- 14:30–15:30 — Review mistakes, re-read only the specific sub-topics that tripped you up
- 15:30–16:00 — Final checklist review + exam-day logistics prep (admit card, ID, stationery)

---

## 4. Resource Quick-Reference

| Area | Primary Resource (from official syllabus references where available) |
|---|---|
| Fundamentals of Computers | P.K. Sinha & P. Sinha — *Computer Fundamentals* |
| Discrete Structures | Kenneth Rosen — *Discrete Mathematics and Its Applications* |
| Computer Architecture | Morris Mano — *Digital Logic and Computer System Design* |
| Programming/OOP | Balagurusamy — *OOP with C++*; any C reference (K&R) |
| DBMS | Elmasri & Navathe — *Fundamentals of Database Systems* |
| OS | Silberschatz, Galvin, Gagne — *Operating System Concepts* |
| Software Engineering | Sommerville / Pressman — *Software Engineering* |
| DSA | Horowitz & Sahni — *Fundamentals of Data Structures*; GfG/LeetCode for practice |
| Networks | Forouzan — *Data Communications & Networking*; Tanenbaum — *Computer Networks* |
| AI | Russell & Norvig — *AI: A Modern Approach* (skim, since already strong) |
| Educational Psychology | Anita Woolfolk / S.K. Mangal — *Educational Psychology* |
| Kannada Grammar | ತೀ.ನಂ.ಶ್ರೀಕಂಠಯ್ಯ grammar; KTBS 8th-10th textbooks |
| English | Wren & Martin; Raymond Murphy — *Essential English Grammar* |
| GK/Current Affairs | Lucent's GK; monthly current affairs capsules |
| Constitution | M. Laxmikanth — *Indian Polity* |
| Health/Value Education | D.S.E.R.T. syllabus material (official reference) |

---

## 5. Obsidian Setup Tips

- Create a `KPSC-CST` folder with subfolders `Paper1/` and `Paper2/`
- One note per unit, tagged `#kpsc-cst/paper2/unitN` or `#kpsc-cst/paper1/<topic>`
- Maintain a single **MOC (Map of Content)** note linking every unit note, checked off as completed
- Keep a running **`Weak Spots.md`** note — append anything you get wrong during MCQ practice; this becomes your Day 14 revision list
- Use the Excalidraw plugin for diagrams (OSI layers, memory hierarchy, ER diagrams) — visual recall helps under exam time pressure
