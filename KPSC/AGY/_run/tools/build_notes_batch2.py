"""
build_notes_batch2.py
Builds the notes for 07_General_Mental_Ability
using safe_ops.py to ensure write boundary integrity.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import safe_ops

ROOT_DIR = safe_ops.ROOT_DIR

notes = {}

# 1. Reading_Comprehension.md
notes[os.path.join(ROOT_DIR, "03_Notes", "07_General_Mental_Ability", "Reading_Comprehension.md")] = """---
title: Reading Comprehension and Passage Analysis (SSLC Level)
syllabus_refs: [P2-S3.1]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://kpsc.kar.nic.in", "DSERT Class 10 English & Kannada"]
priority: high
---

# Reading Comprehension and Passage Analysis (ಗ್ರಹಣ ಶಕ್ತಿ ಮತ್ತು ಗದ್ಯ ವಿಶ್ಲೇಷಣೆ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: In Prelims Paper 2 Section 3 (General Mental Ability), Comprehension typically carries 5 to 8 MCQs (10 to 16 Marks). Passages are provided in both English and Kannada.
> - **Prelims Traps**: Choosing answers that reflect external general knowledge rather than statements supported strictly by the text; falling for extreme qualifiers (*always*, *never*, *only*, *all*); misinterpreting tone/inference questions.
> - **KAS-Specific Nuance**: KPSC translates passages from English to Kannada (or vice-versa). In case of translational ambiguity in Kannada, the English text is standard, but candidates must verify terms carefully.

---

## 1. Core Comprehension Question Archetypes

```mermaid
flowchart TD
    PASSAGE["Comprehension Passage Types"] --> MAIN["1. Main Idea & Central Theme\n'What is the primary message / crux?'\n'Which title best captures the passage?'"]
    PASSAGE --> FACT["2. Direct & Fact-Retrieval\n'According to the author...'\nExplicit evidence located directly in text"]
    PASSAGE --> INFER["3. Inference & Underlying Assumption\n'What can be logically deduced?'\n'What unstated premise does the author rely on?'"]
    PASSAGE --> TONE["4. Tone & Author's Stance\nCritical, Analytical, Optimistic, Cynical, Objective"]
    PASSAGE --> VOCAB["5. Contextual Vocabulary\nMeaning of idioms or words in specific sentence context"]
```

The diagram above details the 5 foundational question categories appearing in KPSC General Mental Ability comprehension sections.

### 1.1 Systematic 4-Step Passage Solving Strategy
1. **Skim Question Stems First (30 Seconds)**: Read only the question stems (not the options) before diving into the passage. This flags keywords, dates, names, or theme concepts to look for during reading.
2. **Active Analytical Reading (2 Minutes)**:
   - Identify the **Topic Sentence** (usually in paragraph 1).
   - Track transition words signaling logical shifts: *However, Despite, Whereas, On the contrary, Furthermore, Consequently*.
   - Mark concluding statements summarizing the author's viewpoint.
3. **Paraphrase the Crux**: Formulate a one-sentence mental summary of the author's central contention before evaluating options.
4. **Eliminate Aggressively**:
   - Discard options that introduce outside concepts not present in the text.
   - Discard options containing absolute words (*solely, invariably, impossible, everyone*) unless the author explicitly uses them.
   - Beware of "Half-Right, Half-Wrong" distractors.

---

## 2. Bilingual Passage Mastery (ಕನ್ನಡ ಮತ್ತು ಇಂಗ್ಲಿಷ್ ಗದ್ಯ ಗ್ರಹಣ)

In KPSC examinations, passages often address socio-economic development, Karnataka history, environmental conservation, or philosophical themes:
- **Navigating Complex Kannada Prose**:
  - Focus on case markers (ವಿಭಕ್ತಿ ಪ್ರತ್ಯಯಗಳು) and verb conjugations to distinguish the subject (ಕರ್ತೃ), object (ಕರ್ಮ), and action (ಕ್ರಿಯಾಪದ).
  - Watch for formal sandhi/compound formations (ಸಮಾಸಗಳು) frequently used in formal administrative or literary Kannada.
- **Cross-Checking Between Versions**: When an option in Kannada seems confusing or grammatically convoluted, reading the corresponding English sentence clarifies the syntactic intent immediately.

---

## Likely Questions & PYQs

### Practice Passage (KPSC Prelims Model)
*Passage*:
"Sustainable economic progress in agrarian states like Karnataka cannot rely solely on urban-centric service growth. While the capital city Bengaluru generates disproportionate revenues, rural productivity remains constrained by rainfed vulnerability and fragmented landholdings. Without decentralized industrial corridors that link secondary agricultural processing with rural enterprise, regional imbalances will continue to widen, driving unsustainable distress migration to urban centers."

#### Question 1 (Crux / Main Idea)
**Q**: Which of the following best reflects the most logical and critical inference from the passage?
A) Service sector growth in Bengaluru must be curtailed to protect the rural economy.
B) Broad-based economic resilience requires integrating rural agro-processing with regional industrial dispersion.
C) Distress migration can only be prevented by providing guaranteed agricultural subsidies.
D) Urbanization is intrinsically detrimental to sustainable economic development.
*Answer*: **B**
*Explanation*: The passage argues that relying solely on urban-centric growth creates imbalance and that decentralized industrial corridors linking agro-processing with rural enterprise are essential to address regional disparities. Option B captures this comprehensively without extreme distortions.

#### Question 2 (Fact & Inference)
**Q**: According to the author, what is a primary structural constraint affecting rural economic productivity?
A) Lack of telecommunications connectivity
B) Excessive concentration of manufacturing in coastal areas
C) Reliance on rainfed cultivation and fragmented holdings
D) Total absence of state developmental funding
*Answer*: **C**
*Explanation*: The passage explicitly states: "rural productivity remains constrained by rainfed vulnerability and fragmented landholdings."

---

> [!summary]
> **Key Revision Points**:
> - Read question stems before reading the text.
> - Never import outside knowledge; the text is the sole universe of truth.
> - Eliminate extreme options (*all, none, never, only*).
> - Cross-reference English and Kannada versions if translational ambiguity arises.
"""

# 2. Logical_and_Analytical_Reasoning.md
notes[os.path.join(ROOT_DIR, "03_Notes", "07_General_Mental_Ability", "Logical_and_Analytical_Reasoning.md")] = """---
title: Logical and Analytical Reasoning (Deductive, Inductive and Diagrammatic Logic)
syllabus_refs: [P2-S3.2]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://kpsc.kar.nic.in", "Standard Reasoning Textbooks"]
priority: high
---

# Logical and Analytical Reasoning (ತಾರ್ಕಿಕ ಮತ್ತು ವಿಶ್ಲೇಷಣಾತ್ಮಕ ಸಾಮರ್ಥ್ಯ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: Carries 8 to 10 MCQs (16 to 20 Marks) in Prelims Paper 2 Section 3.
> - **Prelims Traps**: Violating Venn diagram rules in Syllogisms (confusing 'Some' with 'Some not', or missing complementary pairs for 'Either-Or'); sign reversal in coded inequalities; mixing left/right orientations in inward vs outward facing circular seating arrangements.
> - **High-Yield Sub-topics**: Syllogisms (ನ್ಯಾಯವಾಕ್ಯಗಳು), Blood Relations (ರಕ್ತ ಸಂಬಂಧಗಳು), Direction Sense Test (ದಿಕ್ಕುಗಳ ಜ್ಞಾನ), Seating Arrangements, Coding-Decoding (ಸಂಕೇತೀಕರಣ), Statement-Assumptions & Statement-Conclusions.

---

## 1. Syllogistic Deduction & Venn Diagrams

```mermaid
flowchart TD
    SYLL["Syllogism Propositions (AEIO)"] --> A["A: Universal Affirmative\n'All A are B' (ಸಕಲ)\nVenn: Circle A fully inside B"]
    SYLL --> E["E: Universal Negative\n'No A is B' (ಯಾವುದೂ ಅಲ್ಲ)\nVenn: Circles A and B disjoint"]
    SYLL --> I["I: Particular Affirmative\n'Some A are B' (ಕೆಲವು)\nVenn: Circles A and B overlap"]
    SYLL --> O["O: Particular Negative\n'Some A are not B'\nVenn: Shaded part of A outside B"]
```

The flowchart above outlines the 4 standard categorical propositions (AEIO square of opposition) used to solve syllogisms via Venn diagrams.

### 1.1 Golden Rules of Syllogisms
1. If both premises are **Particular** (Some + Some), no definite universal conclusion follows.
2. If both premises are **Negative** (No + No), no definite relationship follows.
3. If one premise is **Negative**, the valid conclusion must be **Negative**.
4. If one premise is **Particular**, the valid conclusion must be **Particular**.
5. **Complementary Pairs for "Either-Or"**:
   - Condition 1: Both conclusions have the same Subject and Predicate.
   - Condition 2: Both conclusions are independently indeterminate/false in the basic diagram.
   - Condition 3: One is affirmative and the other is negative (Pair 1: *Some* + *No*; Pair 2: *All* + *Some Not*). Note: *All* + *No* is **never** an Either-Or pair.

---

## 2. Core Reasoning Modules

### 2.1 Coding - Decoding (ಸಂಕೇತೀಕರಣ ಮತ್ತು ವಿಸಂಕೇತೀಕರಣ)
- **Alphabet Position Mapping**: Memorize alphabet ranks 1 to 26 forwards and backwards using mnemonic:
  - **EJOTY**: E=5, J=10, O=15, T=20, Y=25.
  - **Reverse Alphabet Pairs (Sum = 27)**: A-Z (AZad), B-Y (BoY), C-X (CruX), D-W (Dew), E-V (EVen), F-U (FUll), G-T (GT road), H-S (High School), I-R (Indian Railway), J-Q (Jungle Queen), K-P (Kurta Pajama), L-O (LOve), M-N (MaN).

### 2.2 Blood Relations (ರಕ್ತ ಸಂಬಂಧಗಳು)
- **Standard Diagrammatic Conventions**:
  - Male: Square `[M]` or `+`.
  - Female: Circle `(F)` or `-`.
  - Married Couple: Double horizontal line `<=>`.
  - Siblings: Single horizontal line `---`.
  - Generation Gap: Vertical line `|`.

### 2.3 Direction Sense Test (ದಿಕ್ಕುಗಳ ಪರೀಕ್ಷೆ)
- Standard 8-directional compass: North (ಉತ್ತರ), South (ದಕ್ಷಿಣ), East (ಪೂರ್ವ), West (ಪಶ್ಚಿಮ), North-East (ಈಶಾನ್ಯ), South-East (ಆಗ್ನೇಯ), South-West (ನೈಋತ್ಯ), North-West (ವಾಯವ್ಯ).
- **Pythagoras Theorem**: For shortest displacement across right angles:
  $$\text{Displacement} = \sqrt{(\Delta x)^2 + (\Delta y)^2}$$
- **Shadow Direction at Sunrise vs Sunset**:
  - *At Sunrise (Sun in East)*: Shadow of all objects falls towards the **West**.
  - *At Sunset (Sun in West)*: Shadow of all objects falls towards the **East**.

### 2.4 Seating Arrangements (ಆಸನ ವ್ಯವಸ್ಥೆ)
- **Linear Row**: Facing North (Left = your left, Right = your right); Facing South (Left = your right, Right = your left).
- **Circular Table**:
  - *Facing Inward (Center)*: Clockwise movement = Right to Left (Moving to the **Left** of a person); Counter-Clockwise = Moving to the **Right**.
  - *Facing Outward*: Clockwise = Moving to the **Right**; Counter-Clockwise = Moving to the **Left**.

---

## 3. Critical Analytical Reasoning

1. **Statement and Assumptions (ಹೇಳಿಕೆ ಮತ್ತು ಊಹೆಗಳು)**:
   - An assumption is an unstated foundation that the speaker took for granted when framing the statement.
   - An assumption is valid if it logically underpins why the statement was made.
   - Do not accept assumptions that generalize beyond the statement's domain.
2. **Statement and Courses of Action (ಕ್ರಮಗಳು)**:
   - A valid course of action must be a realistic, practical, and proportionate remedy that solves or reduces the problem without introducing a worse crisis.

---

## Likely Questions & PYQs

### Model Question 1 (Syllogisms)
**Statements**:
1. All rivers are water bodies.
2. Some water bodies are lakes.
**Conclusions**:
I. Some rivers are lakes.
II. No river is a lake.
Which conclusion follows?
A) Only I follows
B) Only II follows
C) Either I or II follows
D) Neither I nor II follows
*Answer*: **C**
*Explanation*: The basic diagram shows rivers inside water bodies, and lakes intersecting water bodies without touching rivers. In this diagram, neither I nor II is definitely true. However, a lake could intersect rivers in an alternative diagram. Since both statements have the same subject and predicate (rivers, lakes), both are individually uncertain, and they form a complementary pair ("Some" and "No"), the correct response is **Either I or II follows**.

### Model Question 2 (Direction Sense)
**Q**: An investigator walks 12 km North from the Taluk office, turns right and walks 5 km East, then turns right and walks 12 km South. How far and in which direction is the investigator from the starting point?
A) 5 km East
B) 10 km North
C) 5 km West
D) 13 km North-East
*Answer*: **A**
*Explanation*: The northward displacement of 12 km is neutralized by the southward displacement of 12 km ($12 - 12 = 0$). The only net displacement is 5 km due East from the starting point.

---

> [!summary]
> **Key Revision Points**:
> - Syllogism: Either-Or applies only to *Some + No* or *All + Some Not*.
> - Reverse alphabet mapping always sums to 27.
> - Inward circular seating: Clockwise = Left, Counter-Clockwise = Right.
> - At sunrise, shadows fall strictly West; at sunset, strictly East.
"""

# 3. Decision_Making_Problem_Solving.md
notes[os.path.join(ROOT_DIR, "03_Notes", "07_General_Mental_Ability", "Decision_Making_Problem_Solving.md")] = """---
title: Decision Making and Problem Solving (Administrative Situational Judgement)
syllabus_refs: [P2-S3.3]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://kpsc.kar.nic.in", "2nd ARC 4th Report - Ethics in Governance"]
priority: high
---

# Decision Making and Problem Solving (ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳುವಿಕೆ ಮತ್ತು ಸಮಸ್ಯೆ ಪರಿಹಾರ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: Featured in Prelims Paper 2 Section 3 (4 to 6 Situational Judgement Questions, 8 to 12 Marks).
> - **KPSC Exam Rule**: In KPSC KAS decision making questions, questions present practical administrative scenarios testing legal propriety, public interest, communal neutrality, and procedural discipline. Unlike typical academic questions, there is often no negative marking for genuine decision-making questions, or options are graded (best option 2 marks, second-best 1 mark), though in standard Prelims 1/4th negative marking applies unless specifically notified.
> - **Golden Elimination Rule**: Immediately eliminate choices that involve: (a) abdication of duty / passing responsibility to superiors without taking initial lawful steps; (b) taking the law into one's own hands or using unlawful force; (c) bowing to illegal political or communal pressure; (d) hasty actions that inflame communal or public riots.

---

## 1. The Administrative Decision Matrix

```mermaid
flowchart TD
    CRISIS["Administrative Problem / Dilemma"] --> L1["Step 1: Constitutional & Legal Legality\nDoes the action conform strictly to statutory powers?"]
    L1 --> L2["Step 2: Immediacy & Public Safety\nIs life, bodily safety, or property in immediate hazard?"]
    L2 --> L3["Step 3: Objectivity & Non-Discrimination\nIs the action neutral to caste, creed, and political pressure?"]
    L3 --> L4["Step 4: Proportionality & De-escalation\nIs the use of administrative force minimal and graded?"]
    L4 --> OUTCOME["Optimal Public Decision Executed"]
```

The flowchart above presents the 4-step decision hierarchy an administrator must navigate when responding to situational crises and administrative dilemmas.

### 1.1 Core Principles Governing Situational Decisions
1. **Rule of Law (ಕಾನೂನಿನ ಆಳ್ವಿಕೆ)**: Administrative discretion cannot exceed statutory limits. An officer must act strictly within the powers delegated under the CrPC/BNSS, Karnataka Police Act, Land Revenue Act, or Disaster Management Act.
2. **Proportionality (ಸಮಾನ ಪ್ರಮಾಣತೆ)**: Any coercive or punitive administrative measure must be strictly proportionate to the scale of the threat. Use dialogue and non-lethal dispersal before resorting to severe measures.
3. **Impartiality & Secular Neutrality (ತಟಸ್ಥತೆ)**: Decisions during communal friction, festival processions, or caste tensions must be completely even-handed. Lawful permissions must be respected, and unlawful acts sanctioned regardless of identity.
4. **Accountability & Written Documentation**: Critical instructions must be recorded in writing with official reasons documented, keeping superiors informed via official sit-rep (situation report) communications.

---

## 2. Common Administrative Scenario Archetypes

### 2.1 Communal Unrest & Public Order
- **Scenario**: A festival procession attempts to deviate from its legally permitted route and pass through a sensitive area, creating immediate risk of communal violence.
- **Appropriate Action**:
  - Immediately stop the unauthorized diversion using adequate police bandobast.
  - Engage community leaders and organizers in direct dialogue to insist on the approved route.
  - Impose prohibitory orders under Section 144 CrPC / Sec 163 BNSS if violence threatens to erupt.
  - Avoid unilateral excessive force until non-violent dispersal and tear gas/water cannons have failed.

### 2.2 Natural Disasters & Evacuation
- **Scenario**: A major landslide warning or flood crest alert is issued for a river basin. Villagers refuse to evacuate their ancestral homes and livestock.
- **Appropriate Action**:
  - Deploy local revenue officials, Anganwadi workers, and Panchayat members to explain the immediate risk.
  - Mobilize rescue relief shelters with food, clean water, and livestock holding areas.
  - Enforce mandatory evacuation under the Disaster Management Act, 2005 if lives are in imminent peril.

### 2.3 Political Pressure vs Statutory Duty
- **Scenario**: An influential local politician demands that the Tahsildar stop an anti-encroachment drive on government lake land (Gomal / Tank bed land) that affects his supporters.
- **Appropriate Action**:
  - Politely but firmly decline to halt the lawful eviction drive.
  - Ensure all due process steps (notice under Section 192A of Karnataka Land Revenue Act, survey sketches, hearing opportunities) have been scrupulously documented.
  - Inform the Deputy Commissioner (DC) in writing about the situation and request additional security if interference is anticipated.

---

## Likely Questions & PYQs

### Model Question 1 (Decision Making Scenario)
**Scenario**: You are the Assistant Commissioner (Sub-Divisional Magistrate). A chemical factory in your jurisdiction has suffered a hazardous gas leak. Local villagers are panicking and starting to block highways, while factory management claims the leak is minor and under control.
What is your immediate sequence of actions?
A) Order an immediate lathi charge on the highway protestors to clear transit corridors.
B) Accept factory management's assurance and advise citizens through social media to remain indoors.
C) Immediately rush disaster response teams, verify leak toxicity with technical experts, seal the facility perimeter, establish safe evacuation shelters for downwind residents, and address citizens through official public address channels.
D) Wait for detailed written guidance from the State Disaster Management Authority before intervening.
*Answer*: **C**
*Explanation*: Option C takes proactive charge of public safety, deploys technical assessment, establishes containment and relief, and counters rumors with official communication. Options A, B, and D represent excessive force, naive passivity, and administrative abdication respectively.

### Model Question 2 (Administrative Dilemma)
**Scenario**: As an Executive Officer of a Taluk Panchayat, you discover that a Gram Panchayat Secretary has diverted MGNREGA funds to clear pending water bills of influential village leaders. The Secretary claims he was verbally ordered to do so by the Panchayat President.
What should you do?
A) Overlook the issue since the money was used for public water supply.
B) Verbally reprimand the Secretary and order him to recover the funds privately.
C) Issue a formal show-cause notice to the Secretary, institute a time-bound financial audit, recover the misallocated funds, and report the irregularity to the Chief Executive Officer (CEO) of the Zilla Panchayat for statutory disciplinary action.
D) Immediately file a criminal case against the Panchayat President without conducting any preliminary inquiry.
*Answer*: **C**
*Explanation*: Administrative procedure requires following due process: issuance of show-cause notice, objective auditing of accounts, fund recovery, and reporting through official hierarchy (CEO ZP) for statutory action.

---

> [!summary]
> **Key Revision Points**:
> - Priority order: Legality -> Human Life & Safety -> Neutrality -> Proportionality.
> - Never pass the buck or abdicate lawful authority.
> - Due process and documentation must precede punitive action.
> - In crisis management, combine de-escalation dialogue with firm enforcement of statutory mandates.
"""

# 4. Basic_Numeracy.md
notes[os.path.join(ROOT_DIR, "03_Notes", "07_General_Mental_Ability", "Basic_Numeracy.md")] = """---
title: Basic Numeracy and Quantitative Aptitude (SSLC Standard)
syllabus_refs: [P2-S3.4]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://kpsc.kar.nic.in", "DSERT Class 10 Mathematics Textbook"]
priority: high
---

# Basic Numeracy and Quantitative Aptitude (ಮೂಲಭೂತ ಸಂಖ್ಯಾಶಾಸ್ತ್ರ ಮತ್ತು ಗಣಿತ ಸಾಮರ್ಥ್ಯ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: High-yield quantitative segment in Prelims Paper 2 Section 3 (10 to 12 MCQs, 20 to 24 Marks). Strictly benchmarked at **SSLC (Class 10) Standard**.
> - **Prelims Traps**: Confusing Simple Interest (linear growth on initial principal) with Compound Interest (exponential compounding); failing to convert units in Time-Speed-Distance (km/hr to m/s: multiply by $5/18$); mixing inverse proportions in Time & Work.
> - **Top High-Frequency Topics**: Percentages (ಶೇಕಡಾವಾರು), Profit & Loss (ಲಾಭ ಮತ್ತು ನಷ್ಟ), Simple & Compound Interest (ಸರಳ ಮತ್ತು ಚಕ್ರಬಡ್ಡಿ), Ratios & Proportions (ಅನುಪಾತ ಮತ್ತು ಸಮಾನುಪಾತ), Time & Work (ಸಮಯ ಮತ್ತು ಕೆಲಸ), Time Speed & Distance, Averages, LCM & HCF.

---

## 1. Number Systems & Divisibility Rules

```mermaid
flowchart TD
    NUM["Number Systems & Divisibility"] --> DIV["Divisibility Rules\n2: Last digit even\n3: Sum of digits divisible by 3\n4: Last two digits divisible by 4\n8: Last three digits divisible by 8\n9: Sum of digits divisible by 9\n11: Alternating sum of digits is 0 or multiple of 11"]
    NUM --> HCF["LCM and HCF Relationship\nProduct of two numbers = LCM x HCF\nLCM of fractions = LCM(Num) / HCF(Denom)\nHCF of fractions = HCF(Num) / LCM(Denom)"]
```

The diagram above details essential number properties and fraction arithmetic applied in competitive arithmetic problem solving.

---

## 2. Core Quantitative Formulas & Techniques

### 2.1 Percentages, Profit and Loss
- **Percentage Change**:
  $$\% \text{ Change} = \frac{\text{New Value} - \text{Original Value}}{\text{Original Value}} \times 100$$
- **Successive Percentage Change**: If a value changes by $+a\%$ and then by $+b\%$:
  $$\text{Net Change } \% = a + b + \frac{ab}{100}$$
- **Profit & Loss**:
  $$\text{Gain } \% = \frac{\text{SP} - \text{CP}}{\text{CP}} \times 100 \quad ; \quad \text{Loss } \% = \frac{\text{CP} - \text{SP}}{\text{CP}} \times 100$$
- **Discount on Marked Price (MP)**:
  $$\text{SP} = \text{MP} \times \left(1 - \frac{D\%}{100}\right)$$

### 2.2 Simple and Compound Interest
- **Simple Interest (SI)**:
  $$\text{SI} = \frac{P \times R \times T}{100} \quad ; \quad \text{Amount } A = P + \text{SI}$$
- **Compound Interest (CI)** (Compounded Annually):
  $$A = P \left(1 + \frac{R}{100}\right)^T \quad ; \quad \text{CI} = A - P$$
- **Difference between CI and SI for 2 Years**:
  $$\text{Difference}_{2\text{ yrs}} = P \left(\frac{R}{100}\right)^2$$

### 2.3 Time and Work (ಸಮಯ ಮತ್ತು ಕೆಲಸ)
- If person A finishes work in $x$ days, A's 1-day work rate is $\frac{1}{x}$.
- If person B finishes work in $y$ days, combined work rate is:
  $$\text{Rate}_{(A+B)} = \frac{1}{x} + \frac{1}{y} = \frac{x+y}{xy} \implies \text{Total Days} = \frac{xy}{x+y}$$
- **Efficiency Method (LCM Technique)**:
  - Assume Total Work = $\text{LCM}(x, y)$.
  - Find individual daily efficiencies (Units/day).
  - Divide total units by combined efficiency to get total days.

### 2.4 Time, Speed and Distance (ಸಮಯ, ವೇಗ ಮತ್ತು ದೂರ)
- **Basic Formula**: $\text{Distance} = \text{Speed} \times \text{Time}$.
- **Unit Conversion**:
  $$1 \text{ km/hr} = \frac{5}{18} \text{ m/s} \quad ; \quad 1 \text{ m/s} = \frac{18}{5} \text{ km/hr}$$
- **Average Speed**:
  $$\text{Average Speed} = \frac{\text{Total Distance}}{\text{Total Time}}$$
  - If equal distances are covered at speeds $u$ and $v$:
    $$\text{Average Speed} = \frac{2uv}{u+v}$$
- **Relative Speed**:
  - Moving in **opposite directions**: $\text{Relative Speed} = u + v$.
  - Moving in **same direction**: $\text{Relative Speed} = |u - v|$.

---

## Likely Questions & PYQs

### Model Question 1 (Arithmetic - Percentages)
**Q**: The price of petrol rises by 25%. By what percentage must a motorist reduce petrol consumption so that monthly expenditure on petrol remains unchanged?
A) 25%
B) 20%
C) 16.66%
D) 33.33%
*Answer*: **B**
*Explanation*: Let original price = 100, original consumption = 100. Expenditure = $100 \times 100 = 10,000$.
New price = 125. Required new consumption $= 10,000 / 125 = 80$.
Reduction $= 100 - 80 = 20\%$.
Using shortcut: $\frac{r}{100 + r} \times 100 = \frac{25}{125} \times 100 = 20\%$.

### Model Question 2 (Time & Work)
**Q**: A can complete a project in 12 days, while B can complete the same project in 24 days. If they work together, how many days will they take to complete the project?
A) 6 days
B) 8 days
C) 9 days
D) 10 days
*Answer*: **B**
*Explanation*:
$\text{Days} = \frac{xy}{x+y} = \frac{12 \times 24}{12 + 24} = \frac{288}{36} = 8 \text{ days}$.
Or using LCM: Total work = $\text{LCM}(12, 24) = 24$ units.
A's efficiency = 2 units/day; B's efficiency = 1 unit/day.
Together = $2 + 1 = 3$ units/day.
Days taken = $24 / 3 = 8$ days.

### Model Question 3 (Simple vs Compound Interest)
**Q**: The difference between compound interest and simple interest on a sum of money at 10% per annum for 2 years is Rs. 150. What is the principal sum?
A) Rs. 12,000
B) Rs. 15,000
C) Rs. 18,000
D) Rs. 20,000
*Answer*: **B**
*Explanation*:
$\text{Difference} = P \times \left(\frac{R}{100}\right)^2$.
$150 = P \times \left(\frac{10}{100}\right)^2 = P \times \frac{1}{100}$.
$P = 150 \times 100 = \text{Rs. } 15,000$.

---

> [!summary]
> **Key Revision Points**:
> - Convert km/h to m/s by multiplying by $5/18$.
> - For equal distances, average speed is $\frac{2uv}{u+v}$, never $\frac{u+v}{2}$.
> - Difference between CI and SI for 2 years is $P(R/100)^2$.
> - Price rise of $r\%$ requires consumption cut of $\frac{r}{100+r} \times 100\%$.
"""

# 5. Data_Interpretation.md
notes[os.path.join(ROOT_DIR, "03_Notes", "07_General_Mental_Ability", "Data_Interpretation.md")] = """---
title: Data Interpretation, Data Sufficiency and Statistical Analysis
syllabus_refs: [P2-S3.5, M-GS1-S3.3]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://kpsc.kar.nic.in", "DSERT Class 10 Statistics", "DES Karnataka"]
priority: high
---

# Data Interpretation, Data Sufficiency and Statistical Analysis (ದತ್ತಾಂಶ ವಿಶ್ಲೇಷಣೆ, ದತ್ತಾಂಶ ಸಮರ್ಪಕತೆ ಮತ್ತು ಸಂಖ್ಯಾಶಾಸ್ತ್ರೀಯ ವ್ಯಾಖ್ಯಾನ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: Dual-stage significance across Prelims Paper 2 Section 3 (6 to 8 MCQs, 12 to 16 Marks) and Mains GS-1 Section 3 (Data Collection, Analysis, and Statistical Interpretation - dedicated 20 to 25 marks).
> - **Prelims Traps**: Calculating absolute numbers from percentage shares without verifying total base values; misreading dual y-axis scales in combined bar-line charts; degree to percentage conversion in pie charts ($100\% = 360^\circ \implies 1\% = 3.6^\circ$).
> - **Mains Dimensions**: Explaining differences between Primary vs Secondary data sources; calculating Mean, Median, Mode and Standard Deviation; analyzing sampling methods (Stratified vs Systematic vs Cluster) used in government socio-economic surveys.

---

## 1. Data Representation Formats

```mermaid
flowchart TD
    DATA["Data Interpretation Formats"] --> TABLE["1. Tabular Representation\nStructured rows and columns\nBest for multi-variable raw data"]
    DATA --> BAR["2. Bar Charts & Histograms\nSimple, Grouped, and Subdivided/Stacked\nHistograms for continuous frequency distributions"]
    DATA --> PIE["3. Pie Charts\nCircular proportional division\nDegrees: (Value / Total) x 360°\nPercent: (Value / Total) x 100%"]
    DATA --> LINE["4. Line Graphs / Time Series\nTracking temporal trends over years/months\nDual-axis charts comparing volume vs growth rate"]
```

The flowchart above outlines the primary chart models evaluated in KPSC preliminary and mains examinations.

### 1.1 Essential Calculation Shortcuts for DI
1. **Pie Chart Conversion Rules**:
   - $10\% = 36^\circ$
   - $25\% = 90^\circ$
   - $50\% = 180^\circ$
   - Value $=\frac{\theta^\circ}{360^\circ} \times \text{Total Base Value}$
2. **Growth Rate Calculation**:
   $$\text{CAGR / Growth Rate} = \frac{\text{Value}_{\text{current}} - \text{Value}_{\text{base}}}{\text{Value}_{\text{base}}} \times 100$$
3. **Approximation Technique**: Round denominators to nearest round numbers (e.g. $423 / 891 \approx 420 / 900 = 46.6\%$) to eliminate distractors rapidly in Prelims.

---

## 2. Statistical Analysis: Measures of Central Tendency & Dispersion (Mains GS-1 Syllabus)

### 2.1 Measures of Central Tendency (ಕೇಂದ್ರೀಯ ಪ್ರವೃತ್ತಿಯ ಅಳತೆಗಳು)
1. **Arithmetic Mean ($\bar{x}$ - ಸರಾಸರಿ)**:
   $$\bar{x} = \frac{\sum f_i x_i}{\sum f_i}$$
   - *Advantage*: Based on every observation; algebraically tractable.
   - *Limitation*: Highly sensitive to extreme outliers.
2. **Median ($M$ - ಮಧ್ಯಾಂಕ)**:
   - The value of the middle observation when data is arranged in ascending order.
   - For grouped data:
     $$M = L + \left(\frac{\frac{N}{2} - CF}{f}\right) \times h$$
     *(Where $L$ is lower limit of median class, $CF$ is cumulative frequency of preceding class, $f$ is frequency, $h$ is class width).*
   - *Advantage*: Robust against extreme outliers (preferred metric for income and wealth distributions).
3. **Mode ($Z$ - ಬಹುಲಕ)**:
   - The value that occurs with highest frequency in a dataset.
   - Empirical relationship between Mean, Median, and Mode:
     $$\text{Mode} \approx 3(\text{Median}) - 2(\text{Mean})$$

### 2.2 Measures of Dispersion (ಚದುರುವಿಕೆಯ ಅಳತೆಗಳು)
1. **Range (ವ್ಯಾಪ್ತಿ)**: Difference between Maximum and Minimum observation.
2. **Variance ($\sigma^2$) and Standard Deviation ($\sigma$ - ನಿಯಮಿತ ವಿಚಲನೆ)**:
   $$\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{N}}$$
   - Measures how spread out values are around the mean.
3. **Coefficient of Variation (CV)**:
   $$\text{CV} = \frac{\sigma}{\bar{x}} \times 100$$
   - Dimensionless measure used to compare consistency or stability between two different distributions (lower CV denotes greater consistency).

---

## 3. Data Collection Methods: Primary vs Secondary Data

| Attribute | Primary Data (ಪ್ರಾಥಮಿಕ ದತ್ತಾಂಶ) | Secondary Data (ದ್ವಿತೀಯಕ ದತ್ತಾಂಶ) |
|---|---|---|
| **Definition** | Data collected for the first time by the investigator for a specific purpose. | Data already collected, compiled, and published by other agencies. |
| **Methods** | Direct personal interviews, questionnaires, telephonic surveys, field observation. | Government publications (Census, Economic Survey, DES Karnataka), RBI bulletins, journals. |
| **Reliability** | High originality and accuracy; tailored to study. | Dependent on the credibility of the publishing agency. |
| **Cost & Time** | Expensive, labor-intensive, and time-consuming. | Economical, quick to retrieve, and readily accessible. |

---

## Likely Questions & PYQs

### Model Question 1 (Prelims - Data Interpretation)
*Data Scenario*: In a district with a total population of 10,00,000, a pie chart shows the sector-wise distribution of the workforce:
- Agriculture: $144^\circ$
- Industry: $72^\circ$
- Services: $108^\circ$
- Construction: $36^\circ$

**Q**: What percentage of the workforce is engaged in the Services sector, and what is the absolute workforce count in Agriculture?
A) Services: 30%, Agriculture: 4,00,000
B) Services: 25%, Agriculture: 3,50,000
C) Services: 35%, Agriculture: 4,50,000
D) Services: 30%, Agriculture: 3,60,000
*Answer*: **A**
*Explanation*:
Services percentage $=\frac{108^\circ}{360^\circ} \times 100 = 30\%$.
Agriculture count $=\frac{144^\circ}{360^\circ} \times 10,00,000 = \frac{2}{5} \times 10,00,000 = 4,00,000$.

### Model Question 2 (Prelims - Statistics)
**Q**: In a moderately skewed distribution, if the mean is 45 and the median is 48, what is the empirical mode of the distribution?
A) 51
B) 54
C) 42
D) 46
*Answer*: **B**
*Explanation*:
Using Karl Pearson's empirical relationship:
$\text{Mode} = 3(\text{Median}) - 2(\text{Mean})$
$\text{Mode} = 3(48) - 2(45) = 144 - 90 = 54$.

### Model Question 3 (Mains GS-1 - 10 Marks)
**Q**: Distinguish between Primary and Secondary data. Briefly explain the major sampling techniques employed in state socio-economic surveys in Karnataka.

---

> [!summary]
> **Key Revision Points**:
> - Pie chart degree conversion: $\text{Percentage} = (\text{Degree} / 360) \times 100$.
> - Empirical formula: $\text{Mode} = 3(\text{Median}) - 2(\text{Mean})$.
> - Median is robust to extreme outliers; Mean is sensitive.
> - Coefficient of Variation: $\text{CV} = (\sigma / \bar{x}) \times 100$ (lower CV means higher consistency).
"""

# Write notes safely
for path, content in notes.items():
    safe_ops.safe_write(path, content)
    print(f"Successfully written: {os.path.basename(path)}")

print("Batch 2 completed successfully.")
