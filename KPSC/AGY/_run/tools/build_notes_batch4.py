"""
build_notes_batch4.py
Builds the notes for 09_Qualifying_Kannada_and_English
using safe_ops.py to ensure write boundary integrity.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import safe_ops

ROOT_DIR = safe_ops.ROOT_DIR

notes = {}

# 1. Qualifying_Kannada_Preparation.md
notes[os.path.join(ROOT_DIR, "03_Notes", "09_Qualifying_Kannada_and_English", "Qualifying_Kannada_Preparation.md")] = """---
title: Compulsory Qualifying Kannada Paper Preparation (SSLC First Language Standard)
syllabus_refs: [M-KAN.1]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://kpsc.kar.nic.in", "DSERT Class 10 First Language Kannada Textbook", "Karnataka Gazetted Probationers Rules"]
priority: high
---

# Compulsory Qualifying Kannada Paper (ಕಡ್ಡಾಯ ಕನ್ನಡ ಪರೀಕ್ಷೆ - ಎಸ್.ಎಸ್.ಎಲ್.ಸಿ ಪ್ರಥಮ ಭಾಷಾ ಮಟ್ಟ)

> [!exam-focus]
> **Exam Weightage & Testing Rules**: Mandatory qualifying paper in Mains Written Examination.
> - **Total Marks**: 150 Marks | **Duration**: 2 Hours.
> - **Qualifying Cut-off**: Strictly **35% (52.5 Marks out of 150)**. Marks do not count for merit ranking, but if a candidate fails to score 35% here, their compulsory GS papers are **not evaluated**.
> - **Standard of Paper**: SSLC First Language Kannada (ಎಸ್.ಎಸ್.ಎಲ್.ಸಿ ಪ್ರಥಮ ಭಾಷಾ ಕನ್ನಡ ಮಟ್ಟ).
> - **Key Trap**: Overconfidence leading to inadequate practice; poor handwriting or orthographic spelling errors (ಕಾಗುಣಿತ ದೋಷಗಳು, ಮಹಾಪ್ರಾಣ-ಅಲ್ಪಪ್ರಾಣ ದೋಷಗಳು, ಒತ್ತು-ಅಕ್ಷರ ತಪ್ಪುಗಳು) causing loss of easy marks.

---

## 1. Paper Pattern & Mark Distribution

```mermaid
flowchart TD
    KANNADA["Compulsory Kannada (150 Marks / 2 Hours)"] --> SEC1["1. Comprehension (ಗದ್ಯ ಗ್ರಹಣ) - 25 Marks\nPassage reading & answering 5 structured questions"]
    KANNADA --> SEC2["2. Précis Writing (ಸಂಕ್ಷಿಪ್ತ ಲೇಖನ) - 25 Marks\nCondensing passage to 1/3rd with suitable title"]
    KANNADA --> SEC3["3. Vocabulary & Usage (ಪದ ಬಳಕೆ & ಶಬ್ದಕೋಶ) - 25 Marks\nನುಡಿಗಟ್ಟುಗಳು, ಗಾದೆ ವಿಸ್ತರಣೆ, ತತ್ಸಮ-ತದ್ಭವ, ಸಮಾನಾರ್ಥಕಗಳು"]
    KANNADA --> SEC4["4. Essay Writing (ಕಿರು ಪ್ರಬಂಧ) - 25 Marks\nContemporary socio-economic or cultural topic (approx 300 words)"]
    KANNADA --> SEC5["5. Translation (ಇಂಗ್ಲಿಷ್‌ನಿಂದ ಕನ್ನಡಕ್ಕೆ ಭಾಷಾಂತರ) - 25 Marks\nTranslating administrative / conceptual English text into idiomatic Kannada"]
    KANNADA --> SEC6["6. Grammar & Syntax (ಕನ್ನಡ ವ್ಯಾಕರಣ) - 25 Marks\nಸಂಧಿಗಳು, ಸಮಾಸಗಳು, ವಿಭಕ್ತಿ ಪ್ರತ್ಯಯಗಳು, ವಾಕ್ಯ ದೋಷ ತಿದ್ದುಪಡಿ"]
```

The flowchart above outlines the 6 constituent components of the KPSC Compulsory Qualifying Kannada examination, each carrying 25 marks.

---

## 2. Core Kannada Grammar Essentials (ವ್ಯಾಕರಣಾಂಶಗಳು)

### 2.1 Sandhi (ಸಂಧಿಗಳು)
- **ಕನ್ನಡ ಸಂಧಿಗಳು (ಸ್ವರ ಸಂಧಿ & ವ್ಯಂಜನ ಸಂಧಿ)**:
  1. *ಲೋಪ ಸಂಧಿ (Lopa Sandhi)*: ಸ್ವರದ ಮುಂದೆ ಸ್ವರವು ಬಂದು ಸಂಧಿಯಾದಾಗ ಪೂರ್ವಪದದ ಕೊನೆಯಲ್ಲಿರುವ ಸ್ವರವು ಅರ್ಥವು ಕೆಡದಿದ್ದರೆ ಮಾತ್ರ ಬಿಟ್ಟುಹೋಗುವುದು (ಉದಾ: ಮಾತು + ಇಲ್ಲ = ಮಾತಿಲ್ಲ; ಊರು + ಊರು = ಊರೂರು).
  2. *ಆಗಮ ಸಂಧಿ (Aagama Sandhi)*: ಸ್ವರದ ಮುಂದೆ ಸ್ವರವು ಬಂದಾಗ 'ಯ' ಅಥವಾ 'ವ' ಕಾರವು ಹೊಸದಾಗಿ ಬಂದು ಸೇರುವುದು (ಉದಾ: ಮನೆ + ಅನ್ನು = ಮನೆಯನ್ನು ['ಯ' ಕಾರಾಗಮ]; ಗುರು + ಅನ್ನು = ಗುರುವನ್ನು ['ವ' ಕಾರಾಗಮ]).
  3. *ಆದೇಶ ಸಂಧಿ (Aadesha Sandhi)*: ಉತ್ತರಪದದ ಆದಿಯಲ್ಲಿರುವ ಕ, ತ, ಪ ಗಳಿಗೆ ಕ್ರಮವಾಗಿ ಗ, ದ, ಬ ಗಳು ಬರುವುದು (ಉದಾ: ಕಣ್ + ಪನಿ = ಕಣ್ಣನಿ; ಮಳೆ + ಕಾಲ = ಮಳೆಗಾಲ; ಬೆಟ್ಟ + ತಾವರೆ = ಬೆಟ್ಟದಾವರೆ).
- **ಸಂಸ್ಕೃತ ಸಂಧಿಗಳು**:
  - *ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ*: ದೇವ + ಆಲಯ = ದೇವಾಲಯ; ಕವಿ + ಈಶ್ವರ = ಕವೀಶ್ವರ.
  - *ಗುಣ ಸಂಧಿ*: ಮಹಾ + ಈಶ = ಮಹೇಶ; ಸೂರ್ಯ + ಉದಯ = ಸೂರ್ಯೋದಯ.
  - *ವೃದ್ಧಿ ಸಂಧಿ*: ಏಕ + ಏಕ = ಏಕೈಕ; ಜಲ + ಓಘ = ಜಲೌಘ.

### 2.2 Samasa (ಸಮಾಸಗಳು)
- **ತತ್ಪುರುಷ ಸಮಾಸ**: ಉತ್ತರಪದದ ಅರ್ಥ ಪ್ರಧಾನವಾಗಿರುವ ಸಮಾಸ (ಉದಾ: ಮರದ ಕಾಲು = ಮರಗಾಲು; ಹಣೆಗಣ್ಣ).
- **ಕರ್ಮಧಾರಯ ಸಮಾಸ**: ವಿಶೇಷಣ-ವಿಶೇಷ್ಯ ಸಂಬಂಧವುಳ್ಳದ್ದು (ಉದಾ: ಹಿರಿದಾದ ಜೇನು = ಹೆಜ್ಜೇನು; ಕೆಂಪಾದ ಕಮಲ = ಕೆಂದಾವರೆ).
- **ದ್ವಂದ್ವ ಸಮಾಸ**: ಎರಡೂ ಪದಗಳ ಅರ್ಥ ಪ್ರಧಾನವಾಗಿರುವ ಸಮಾಸ (ಉದಾ: ಗಿಡವೂ ಮರವೂ ಬಳ್ಳಿಯೂ = ಗಿಡಮರಬಳ್ಳಿಗಳು).
- **ದ್ವಿಗು ಸಮಾಸ**: ಪೂರ್ವಪದವು ಸಂಖ್ಯಾ ವಾಚಕವಾಗಿರುವ ಸಮಾಸ (ಉದಾ: ಮೂರು ಕಣ್ಣು = ಮುಕ್ಕಣ್ಣ; ನಾಲ್ಕು ದಿಕ್ಕು = ನಾಲ್ದೆಸೆ).
- **ಬಹು Metaphor / ಬಹುವ್ರೀಹಿ ಸಮಾಸ**: ಅನ್ಯಪದದ ಅರ್ಥ ಪ್ರಧಾನವಾಗಿರುವ ಸಮಾಸ (ಉದಾ: ಚಕ್ರವು ಪಾಣಿಯಲ್ಲಿ ಯಾವುದಕ್ಕೋ ಅವನು = ಚಕ್ರಪಾಣಿ [ವಿಷ್ಣು]).

### 2.3 Tatsama - Tadbhava (ತತ್ಸಮ - ತದ್ಭವ ಪಟ್ಟಿ)
| ಸಂಸ್ಕೃತ ಮೂಲ (ತತ್ಸಮ) | ಕನ್ನಡ ರೂಪ (ತದ್ಭವ) | ಸಂಸ್ಕೃತ ಮೂಲ (ತತ್ಸಮ) | ಕನ್ನಡ ರೂಪ (ತದ್ಭವ) |
|---|---|---|---|
| ಆಶ್ಚರ್ಯ | ಅಚ್ಚರಿ | ಯುದ್ಧ | ಜುದ್ಧ |
| ಕಾರ್ಯ | ಕಜ್ಜ | ಲಕ್ಷ್ಮೀ | ಲಕ್ಕಿ |
| ಕಾವ್ಯ | ಕಬ್ಬ | ಪಕ್ಷಿ | ಹಕ್ಕಿ |
| ಶೃಂಗಾರ | ಸಿಂಗಾರ | ವರ್ಷ | ವರುಷ |
| ಮುಖ | ಮೊಗ | ರತ್ನ | ರನ್ನ |
| ಭಕ್ತಿ | ಬಕುತಿ | ಸ್ಥಾನ | ತಾಣ |
| ಸ್ತನ | ಮೊಲೆ | ರಾಜ | ರಾಯ |
| ಯಜ್ಞ | ಜನ್ನ | ಪಾದ | ಹಾದಿ |

---

## 3. High-Yield Vocabulary: Proverbs & Idioms

### 3.1 Nudigattugalu (ನುಡಿಗಟ್ಟುಗಳು - Idioms & Usages)
- **ಕೈಕೊಡು (Kaikodu)**: ಮೋಸ ಮಾಡು ಅಥವಾ ಕೈಚೆಲ್ಲು (ಉದಾ: ಸಂಕಷ್ಟದ ಸಮಯದಲ್ಲಿ ಆಪ್ತ ಮಿತ್ರನೇ ಕೈಕೊಟ್ಟನು).
- **ಕಣ್ಣಿಡು (Kannidu)**: ಗಮನಿಸು ಅಥವಾ ಆಸೆಪಡು (ಉದಾ: ಅಧಿಕಾರಿಗಳು ಅಕ್ರಮ ಗಣಿಗಾರಿಕೆಯ ಮೇಲೆ ತೀವ್ರ ಕಣ್ಣಿಟ್ಟಿದ್ದಾರೆ).
- **ತಲೆಯೆತ್ತು (Taleyettu)**: ಸ್ವಾಭಿಮಾನದಿಂದ ಜೀವಿಸು / ಅಭಿವೃದ್ಧಿಯಾಗು (ಉದಾ: ಸ್ವಾತಂತ್ರ್ಯಾನಂತರ ಭಾರತವು ವಿಜ್ಞಾನ ಕ್ಷೇತ್ರದಲ್ಲಿ ತಲೆಯೆತ್ತಿ ನಿಂತಿದೆ).
- **ಕಿವಿಗೊಡು (Kivigodu)**: ಗಮನವಿಟ್ಟು ಆಲಿಸು (ಉದಾ: ಶಿಕ್ಷಕರ ಹಿತವಚನಕ್ಕೆ ವಿದ್ಯಾರ್ಥಿಗಳು ಕಿವಿಗೊಡಬೇಕು).

### 3.2 Gaadegalu (ಗಾದೆ ಮಾತುಗಳು - Proverbs with Expansion Framework)
- **"ಹಾಸಿಗೆ ಇದ್ದಷ್ಟು ಕಾಲು ಚಾಚು" (Stretch legs according to bed length)**:
  - *ವಿವರಣೆ*: ಒಬ್ಬ ವ್ಯಕ್ತಿಯು ತನ್ನ ಆರ್ಥಿಕ ಆದಾಯ ಮತ್ತು ಸಾಮರ್ಥ್ಯದ ಮಿತಿಯಲ್ಲಿ ಮಾತ್ರ ಖರ್ಚು ಮಾಡಬೇಕು. ಆಡಳಿತದಲ್ಲಿಯೂ ಬಜೆಟ್ ಮಿತಿಯಲ್ಲಿ ಕಾರ್ಯಯೋಜನೆ ರೂಪಿಸುವುದನ್ನು ಇದು ಬೋಧಿಸುತ್ತದೆ.
- **"ಕುಂಬಳಕಾಯಿ ಕಳ್ಳ ಎಂದರೆ ಹೆಗಲು ಮುಟ್ಟಿ ನೋಡಿಕೊಂಡ" (Guilty conscience needs no accuser)**:
  - *ವಿವರಣೆ*: ತಪ್ಪು ಮಾಡಿದ ವ್ಯಕ್ತಿಯು ಯಾರೂ ಹೆಸರಿಸದಿದ್ದರೂ ತನ್ನ ಆಂತರಿಕ ಅಪರಾಧಿ ಭಾವನೆಯಿಂದ ತಾನೇ ಬಹಿರಂಗಗೊಳ್ಳುತ್ತಾನೆ.
- **"ಉಪ್ಪಿಟ್ಟವರನ್ನು ಮುಪ್ಪಿನ ತನಕ ನೆನೆ" (Remember your benefactors till old age)**:
  - *ವಿವರಣೆ*: ಕೃತಜ್ಞತಾ ಭಾವದ ಶ್ರೇಷ್ಠತೆ; ನಮಗೆ ಉಪಕಾರ ಮಾಡಿದವರನ್ನು ಎಂದಿಗೂ ಮರೆಯಬಾರದು.

---

## 4. Translation Strategy: English to Kannada (ಇಂಗ್ಲಿಷ್‌ನಿಂದ ಕನ್ನಡಕ್ಕೆ ಭಾಷಾಂತರ)

### 4.1 Golden Rules for Translation:
1. **Never Translate Word-for-Word (ಅಕ್ಷರಶಃ ಭಾಷಾಂತರಿಸಬೇಡಿ)**: Understand the complete sentence thought, then express it in natural Kannada sentence structure: **ಕರ್ತೃ (Subject) -> ಕರ್ಮ (Object) -> ಕ್ರಿಯಾಪದ (Verb)**.
   - *English*: The Deputy Commissioner inspected the drought-affected village yesterday.
   - *Kannada*: ಜಿಲ್ಲಾಧಿಕಾರಿಗಳು ನಿನ್ನೆ ಬರಪೀಡಿತ ಗ್ರಾಮವನ್ನು ಪರಿಶೀಲಿಸಿದರು.
2. **Administrative Glossary Mapping**:
   - Gazette = ಗೆಜೆಟ್ / ರಾಜ್ಯಪತ್ರ
   - Discretionary powers = ವಿವೇಚನಾಧಿಕಾರ
   - Public Interest = ಸಾರ್ವಜನಿಕ ಹಿತಾಸಕ್ತಿ
   - Autonomous body = ಸ್ವಾಯತ್ತ ಸಂಸ್ಥೆ
   - Accountability = ಹೊಣೆಗಾರಿಕೆ
   - Redressal of grievances = ಕುಂದುಕೊರತೆಗಳ ನಿವಾರಣೆ

---

## 5. Précis Writing Strategy (ಸಂಕ್ಷಿಪ್ತ ಲೇಖನ / ಸಾರಾಂಶ ಬರಹ)

1. Read the passage twice to grasp the central thesis.
2. Count the total words (e.g. 300 words). The précis must be approximately **one-third (1/3rd) length** (approx 100 words).
3. Do not include personal examples, quotes, rhetorical flourishes, or outside commentary.
4. Provide an apt, concise title in Kannada (ಉದಾ: *"ಸ್ವಚ್ಛತೆಯ ಮಹತ್ವ"*, *"ವಿದ್ಯಾರ್ಥಿ ಮತ್ತು ಶಿಸ್ತು"*).
5. Prepare a rough draft first, refine word count, and write the fair draft cleanly.

---

> [!summary]
> **Key Revision Points**:
> - Qualifying mark: strictly 35% (52.5/150).
> - Kannada sentence structure: Subject -> Object -> Verb (SOV).
> - Précis must be 1/3rd word count with an apt title.
> - Master Tatsama-Tadbhava conversions and 10 common Kannada proverbs.
> - Avoid spelling mistakes in Mahaprana (ಖ, ಘ, ಛ, ಝ, ಠ, ಢ, ಥ, ಧ, ಫ, ಭ).
"""

# 2. Qualifying_English_Preparation.md
notes[os.path.join(ROOT_DIR, "03_Notes", "09_Qualifying_Kannada_and_English", "Qualifying_English_Preparation.md")] = """---
title: Compulsory Qualifying English Paper Preparation (SSLC Standard)
syllabus_refs: [M-ENG.1]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://kpsc.kar.nic.in", "DSERT Class 10 English Textbook", "Wren & Martin High School English Grammar"]
priority: high
---

# Compulsory Qualifying English Paper (ಕಡ್ಡಾಯ ಇಂಗ್ಲಿಷ್ ಪರೀಕ್ಷೆ - ಎಸ್.ಎಸ್.ಎಲ್.ಸಿ ಮಟ್ಟ)

> [!exam-focus]
> **Exam Weightage & Testing Rules**: Mandatory qualifying paper in Mains Written Examination.
> - **Total Marks**: 150 Marks | **Duration**: 2 Hours.
> - **Qualifying Cut-off**: Strictly **35% (52.5 Marks out of 150)**. Marks do not count for merit ranking, but clearing it is an absolute prerequisite for GS paper evaluation.
> - **Standard of Paper**: SSLC Standard English (Class 10).
> - **Key Traps**: Common grammatical errors in Subject-Verb Agreement, misuse of tenses, spelling and punctuation errors, exceeding word limits in Précis writing.

---

## 1. Paper Structure & Blueprint

```mermaid
flowchart TD
    ENG["Compulsory English (150 Marks / 2 Hours)"] --> SEC1["1. Reading Comprehension (25 Marks)\n5 factual & inferential questions from a prose passage"]
    ENG --> SEC2["2. Précis Writing (25 Marks)\nSummarizing given text to 1/3rd with title"]
    ENG --> SEC3["3. Vocabulary & Usage (25 Marks)\nSynonyms, Antonyms, Idioms, One-word substitutes, Phrasal verbs"]
    ENG --> SEC4["4. Short Essay (25 Marks)\nWell-structured essay of ~300 words on a general theme"]
    ENG --> SEC5["5. Translation: Kannada to English (25 Marks)\nTranslating Kannada narrative / passage into fluent English"]
    ENG --> SEC6["6. Grammar & Syntax (25 Marks)\nTenses, Active-Passive Voice, Direct-Indirect Speech, Prepositions"]
```

The diagram above details the standard 6-section composition of the KPSC Compulsory English Examination.

---

## 2. Core Grammar Rules & Error Spotting

### 2.1 Subject - Verb Agreement (The Golden Rules)
1. **Rule of Singular Subjects with Conjunctions**: When two singular nouns are joined by *as well as, along with, together with, in addition to*, the verb agrees with the **first subject**.
   - *Incorrect*: The Deputy Commissioner, along with his officers, were present.
   - *Correct*: The Deputy Commissioner, along with his officers, **was** present.
2. **Either...Or / Neither...Nor**: The verb agrees with the **nearer subject**.
   - *Correct*: Neither the minister nor the directors **were** available.
   - *Correct*: Neither the directors nor the minister **was** available.
3. **Collective Nouns**: Take a singular verb when considered as a single collective unit, but plural when individual members act separately.
   - *The committee has submitted its report.*
   - *The committee are divided in their opinions.*

### 2.2 Active and Passive Voice Transformations
- Present Continuous:
  - *Active*: The government is constructing a new reservoir.
  - *Passive*: A new reservoir **is being constructed** by the government.
- Past Perfect:
  - *Active*: The vigilance team had seized the illicit documents.
  - *Passive*: The illicit documents **had been seized** by the vigilance team.
- Modal Verbs:
  - *Active*: The administration must protect public wetlands.
  - *Passive*: Public wetlands **must be protected** by the administration.

### 2.3 Direct and Indirect Speech
- Reporting verb in Past Tense changes the reported speech tense:
  - Simple Present $\to$ Simple Past (*"I work hard" $\to$ he worked hard*).
  - Present Continuous $\to$ Past Continuous (*"I am reviewing" $\to$ he was reviewing*).
  - Simple Past $\to$ Past Perfect (*"I saw the incident" $\to$ he had seen the incident*).
  - Universal truths remain in Present Tense: *The teacher said, "The earth revolves around the sun." $\to$ The teacher said that the earth revolves around the sun.*

---

## 3. High-Yield Vocabulary, Idioms and One-Word Substitutes

### 3.1 Idioms & Phrases
- **At the eleventh hour**: At the last possible moment.
- **Burn the midnight oil**: Work or study late into the night.
- **A blessing in disguise**: Something that seems bad initially but results in something good.
- **Through thick and thin**: Under all conditions, no matter how difficult.
- **Leave no stone unturned**: Make every possible effort to accomplish a goal.

### 3.2 High-Frequency One-Word Substitutes
- *One who looks at the bright side of things*: **Optimist**.
- *One who looks at the dark side of things*: **Pessimist**.
- *A person who loves mankind and makes charitable gifts*: **Philanthropist**.
- *A person who renounces a religious or political belief*: **Apostate**.
- *An official appointed to settle a dispute*: **Arbitrator**.
- *Government by the wealthy class*: **Plutocracy**.
- *Government by the officials/bureaucracy*: **Bureaucracy**.

---

## 4. Précis Writing Masterclass

### Step-by-Step Rules:
1. **Title**: Always write a clear, catchy title reflecting the central theme (carries 5 marks).
2. **Length**: Exactly **one-third (1/3rd) of original word count** ($\pm 10\%$).
   - E.g., if passage has 300 words, write between 90 and 110 words.
3. **Voice & Person**: Always write in the **Third Person** and **Past/Present Tense**, indirect speech. Never use "I", "we", or "you".
4. **No Outside Facts**: Do not insert personal opinions, commentary, or external knowledge.
5. **No Direct Quotations**: Convert all quotes and dialogues into objective summary statements.
6. **Rough Draft**: Write a draft, count words, eliminate repetitions, then write the neat final version.

---

## 5. Translation: Kannada to English (ಕನ್ನಡದಿಂದ ಇಂಗ್ಲಿಷ್‌ಗೆ ಭಾಷಾಂತರ)

### Model Translation Exercise:
*Kannada Text*:
"ಕರ್ನಾಟಕವು ಶ್ರೀಮಂತ ನೈಸರ್ಗಿಕ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಹಾಗೂ ವೈವಿಧ್ಯಮಯ ಸಂಸ್ಕೃತಿಯನ್ನು ಹೊಂದಿದೆ. ನಮ್ಮ ರಾಜ್ಯದ ಪಶ್ಚಿಮ ಘಟ್ಟಗಳು ಜಾಗತಿಕ ಜೀವವೈವಿಧ್ಯ ತಾಣಗಳಾಗಿವೆ. ಪರಿಸರ ಸಂರಕ್ಷಣೆ ಮತ್ತು ಕೈಗಾರಿಕಾ ಅಭಿವೃದ್ಧಿಯ ನಡುವೆ ಸಮತೋಲನ ಸಾಧಿಸುವುದು ಇಂದಿನ ಆಡಳಿತದ ಪ್ರಮುಖ ಸವಾಲಾಗಿದೆ."

*Standard English Translation*:
"Karnataka possesses abundant natural resources and a rich, diverse culture. The Western Ghats of our state are globally recognized biodiversity hotspots. Achieving a balance between environmental conservation and industrial development represents a paramount challenge for contemporary governance."

---

> [!summary]
> **Key Revision Points**:
> - Qualifying mark: 35% (52.5/150).
> - Précis: Must have a title, exactly 1/3rd word count, written in third person.
> - Subject-verb agreement: 'as well as' agrees with 1st subject; 'neither...nor' agrees with nearer subject.
> - In translation, maintain English Subject-Verb-Object (SVO) order.
"""

# Write notes safely
for path, content in notes.items():
    safe_ops.safe_write(path, content)
    print(f"Successfully written: {os.path.basename(path)}")

print("Batch 4 completed successfully.")
