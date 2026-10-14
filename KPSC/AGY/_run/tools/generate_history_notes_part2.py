import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

HIST_DIR = os.path.join(ROOT_DIR, "03_Notes", "01_Karnataka_History_and_Culture")

def create_note_kadambas_gangas():
    path = os.path.join(HIST_DIR, "Early_Dynasties_Kadambas_and_Gangas.md")
    content = """---
title: The Kadambas of Banavasi and Western Gangas of Talakadu
last_verified: 2026-10-13
sources:
  - "Karnataka State Textbooks (KTBS) - 1st PUC History (Chapter 4)"
  - "Dr. Suryanath Kamath, A Concise History of Karnataka, Chapters 4 & 5"
  - "Epigraphia Carnatica, Vol. VII & VIII (Talagunda and Halmidi Inscriptions)"
  - "B.L. Rice, Mysore and Coorg from the Inscriptions"
syllabus_lines: ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1"]
priority: high
tags: ["karnataka-history", "kadambas", "gangas", "halmidi", "shravanabelagola", "veergallu"]
---

# The Kadambas of Banavasi and Western Gangas of Talakadu (ಬನವಾಸಿಯ ಕದಂಬರು ಮತ್ತು ತಲಕಾಡಿನ ಪಶ್ಚಿಮ ಗಂಗರು)

> [!exam-focus]
> **KPSC High-Yield Examination Focus**:
> - **Founding of Kadambas**: Mayurasharma (c. 345-365 CE); Talagunda pillar inscription composed by Kubja giving the origin narrative of Mayurasharma's humiliation at the Pallava Ghatika in Kanchi.
> - **Halmidi Inscription (ಹಾಲ್ಮಿಡಿ ಶಾಸನ)**: Earliest epigraphical record in the Kannada language, dated c. 450 CE under King Kakusthavarma. Found in Halmidi village (Belur taluk, Hassan).
> - **Kadamba Administration & Coins**: *Padmatankas* (ಪದ್ಮಟಂಕ - lotus-punched gold coins); Division of empire into *Mandalas*, *Vishayas*, and *Nadus*.
> - **Western Gangas of Talakadu**: Konganivarma (founder, capital Kolar/Kuvalala, later shifted to Talakadu on Cauvery bank).
> - **King Durvinita**: Scholar-king; translated Gunadhya's *Brihatkatha* from Paisachi into Sanskrit; commentary on Bharavi's *Kiratarjuniya* (15th Sarga); patron of Jainism and Vaishnavism.
> - **Monolithic Gommateshwara at Shravanabelagola**: Consecrated on 13 March 981 CE by Chavundaraya (prime minister of Ganga King Rachamalla IV). Inscription at foot of statue contains earliest Marathi inscription alongside Kannada and Tamil.
> - **Hero Stones (*Veergallu* - ವೀರಗಲ್ಲು) and *Nishidhi* (ನಿಷಿಧಿ)**: Cultural rituals of *Sallekhana* (ಸಲ್ಲೇಖನ - ritual Jain fasting unto death) and battle martyrdom.

---

## 1. The Kadambas of Banavasi (c. 345 – 525 CE)

The Kadambas represent the **first indigenous Kannada kingdom (ಮೊದಲ ಕನ್ನಡ ಸಾಮ್ರಾಜ್ಯ)**, terminating centuries of northern suzerainty and establishing an independent political entity centered at **Banavasi (ಬನವಾಸಿ / ವೈಜಯಂತಿ)** in modern Uttara Kannada district.

```mermaid
flowchart TD
    SUBJUGATION["Humiliation of Mayurasharma at Kanchi Ghatika\n(Pallava Imperial Centre)"] --> RETALIATION["Renounced Brahminical priesthood (Kusha grass)\nTook up Kshatriya Sword\nGuerrilla war in Sriparvata forests"]
    RETALIATION --> TREATY["Pallava King Shivaskandavarman\nrecognizes Kadamba sovereignty\nover Western Sea border to Chandravalli"]
    TREATY --> EXPANSION["Mayurasharma founds Banavasi capital (c. 345 CE)\nTakes title 'Mayuravarma'\nPerforms 18 Ashvamedha sacrifices"]
    EXPANSION --> ZENITH["Kakusthavarma (c. 435-455 CE)\nGolden Age: Matrimonial alliances with Guptas & Vakatakas\nHalmidi Inscription (c. 450 CE)"]
    ZENITH --> SUCCESSION["Division into Banavasi & Triparvata branches\nSubjugated by Badami Chalukya Kirtivarman I (c. 540 CE)"]
```

### 1.1 Origin and the Talagunda Pillar Inscription
- The definitive account of the foundation of the Kadamba dynasty is engraved on a granite pillar in front of the Pranaveshwara temple at **Talagunda (ತಾಳಗುಂದ)** in Shikaripura taluk, Shivamogga district.
- Composed in elegant classical Sanskrit poetry by poet **Kubja** during the reign of Shantivarma (c. 450 CE).
- **The Narrative**: Mayurasharma, a learned Kadamba Brahmin scholar, traveled with his guru Veerasarma to Kanchipuram (capital of the Pallavas) to pursue advanced Vedic studies at the *Ghatika* (university). During an altercation, he was insulted by a Pallava royal guardsman. Enraged that scholarly dignity had been subordinated to arbitrary royal power, Mayurasharma declared that a Brahmin who could master the Vedas could also wield the bow and sword. He retreated to the forests of Sriparvata (Kurnool), raised an army of forest tribes, routed the Pallava frontier garrisons, and forced the Pallava emperor to grant him feudatory territory from the Western Ocean to Prehara.

### 1.2 Chronology of Prominent Kadamba Rulers
| Monarch | Regnal Span | Major Historical Achievements & Epigraphs |
|---|---|---|
| **Mayurasharma (ಮಯೂರಶರ್ಮ)** | c. 345 – 365 CE | Founder of dynasty; established capital at Banavasi (*Vaijayanti*); conducted 18 Ashvamedha yajnas; assumed title *Mayuravarma*. |
| **Kangavarma** | c. 365 – 385 CE | Faced invasions from Vakataka ruler Vindhyashakti II. |
| **Bhagiratha** | c. 385 – 415 CE | Consolidator; contemporary of Chandragupta II Vikramaditya of the Gupta Empire. |
| **Kakusthavarma (ಕಾಕುಸ್ಥವರ್ಮ)** | c. 435 – 455 CE | Greatest ruler; Gupta King Kumaragupta I sent emissaries (Kalidasa is traditionally believed to have visited his court as an envoy); issued the **Halmidi Inscription**; established matrimonial ties with Guptas, Vakatakas, and Gangas. |
| **Shantivarma** | c. 455 – 460 CE | Commissioned the Talagunda pillar inscription; ruled Banavasi while younger brother Krishnavarma I established collateral branch at Triparvata (Halebidu). |
| **Ravivarma** | c. 485 – 519 CE | Re-unified Banavasi and Triparvata branches; defeated the Gangas and Pallavas; noted for the Gudnapur inscription detailing his royal palace complex. |

---

## 2. The Halmidi Inscription (ಹಾಲ್ಮಿಡಿ ಶಾಸನ) — Linguistic Benchmark

- **Discovery**: Discovered in 1936 by Dr. M.H. Krishna (Director of Mysore Archaeology) at Halmidi village, Belur taluk, Hassan district.
- **Date & Language**: Dated to **c. 450 CE**; written in **Purvada Halagannada (ಪೂರ್ವದ ಹಳಗನ್ನಡ - Primitive Old Kannada)** in the southern Brahmi script.
- **Historical Content**: Records a royal land grant (tax-free gift / *Balyachu*) of the villages Palmadi and Mulivalli made by King Kakusthavarma to a warrior named **Vijaarasa (ವಿಜಾರಸ)** of the Sendraka family, in recognition of his valorous fighting against the Pallavas and Kekayas.
- **Linguistic Structure**: Features sixteen lines carved on a sandstone pillar; demonstrates the early transition of spoken Kannada into a formal literary and administrative medium, incorporating Sanskrit compound words with Kannada case endings (*Vibhakti pratyaya*).

---

## 3. Kadamba Administration, Economy and Religion

### 3.1 Administrative Hierarchy
- **Central Government**: King was assisted by a council of ministers:
  - *Pradhana* (Prime Minister), *Maneveri* (Chamberlain), *Tantrapala* (Foreign Affairs Minister), *Karyakartha* (Executive Secretary).
- **Provincial Divisions**:
  - *Mandala* (Province) -> governed by a royal prince (*Mahamandaleshwara*).
  - *Vishaya* (District) -> headed by *Vishayapati*.
  - *Nadu* / *Desha* -> traditional administrative tract.
  - *Grama* (Village) -> basic unit administered by *Gramakuta* / *Gauda*.
- **Coinage**: Minted distinctive gold coins called **Padmatankas (ಪದ್ಮಟಂಕ)**, stamped with an eight-petaled lotus in the center, flanked by punch-marks of conch (*shankha*) and the Kannada legend *Sri*.

### 3.2 Religious and Cultural Contributions
- **Religion**: Royal family adhered to Shaivism (Pranaveshwara of Talagunda, Madhukeshwara of Banavasi), but actively patronized Jainism. Kakusthavarma and Mrigeshavarma donated villages to Jain ascetics of the Yapaniya, Shvetambara, and Digambara sects.
- **Architecture**: Introduced the indigenous **Kadamba Shikara (ಕದಂಬ ಶಿಖರ)**: a stepped-pyramidal tower composed of horizontal receding tiers topped with a *Kalasha* without decorative sculpture, seen at the Kamala Narayana temple at Degaon and Madhukeshwara temple at Banavasi.

---

## 4. The Western Gangas of Talakadu (c. 350 – 1000 CE)

The Western Gangas established a resilient kingdom encompassing southern Karnataka (*Gangavadi 96,000* - ಗಂಗವಾಡಿ ೯೬,೦೦೦), ruling for over six centuries first from **Kolar (Kuvalala)** and subsequently from **Talakadu (ತಲಕಾಡು)** on the banks of the Cauvery river.

```mermaid
flowchart TD
    KONGANI["Konganivarma (c. 350 CE)\nFounding at Kolar (Kuvalala)\nKanvayana Gotra, Jaina blessings of Simhanandi"] --> MADHAVA["Madhava II & Avinita\nShifting capital to Talakadu (Talavanapura)\nConsolidation of Southern Karnataka"]
    MADHAVA --> DURVINITA["Durvinita (c. 529-579 CE)\nScholar-Monarch, Master of Grammar\nCommentary on Kiratarjuniya\nTranslation of Brihatkatha to Sanskrit"]
    DURVINITA --> SHIVAMARA["Shivamara II (c. 788-816 CE)\nAuthor of Gajashtaka (Treatise on Elephants)\nBuilt Keregodu stone temple"]
    SHIVAMARA --> MARASIMHA["Marasimha II (Guthiya Ganga)\nDefender against Rashtrakutas\nSallekhana at Bankapur (975 CE)"]
    MARASIMHA --> RACHAMALLA["Rachamalla IV (c. 974-999 CE)\nPrime Minister Chavundaraya\nErection of Gommateshwara Monolith at Shravanabelagola (981 CE)"]
```

### 4.1 Chronology of Prominent Ganga Monarchs
| Monarch | Regnal Span | Key Achievements & Contributions |
|---|---|---|
| **Konganivarma (Didiga)** | c. 350 – 370 CE | Founded the dynasty at Kuvalala (Kolar) with the guidance of the Jain sage Simhanandi Acharya. |
| **Madhava I** | c. 370 – 390 CE | Skilled scholar; credited with writing a treatise on the Dattaka Sutra (law of adoption). |
| **Avinita** | c. 469 – 529 CE | Ascended throne as an infant; broad religious tolerance; patronized Jain institutions and Shaiva temples. |
| **Durvinita (ದುರ್ವಿನೀತ)** | c. 529 – 579 CE | Greatest intellectual and warrior king of the Gangas; son of Avinita and Punnata princess; defeated Kadambas and Pallavas at Battle of Ponnagara; Sanskrit scholar. |
| **Sripurusha (ಶ್ರೀಪುರುಷ)** | c. 726 – 788 CE | Shifted administrative capital to Manyapura (Manne near Nelamangala); authored **Gajashastra (ಗಜಶಾಸ್ತ್ರ)**, authoritative manual on elephant warfare; realm prospered so greatly that it was titled *Sri Rajya*. |
| **Shivamara II** | c. 788 – 816 CE | Authored **Gajashtaka (ಗಜಾಷ್ಟಕ)**, popular Kannada lyrical work on taming wild elephants (now lost, but celebrated in inscriptions); imprisoned multiple times by Rashtrakutas; constructed Jain Basadi at Kunchi. |
| **Marasimha II** | c. 963 – 975 CE | Titled *Nolambantaka* (Destroyer of Nolambas); loyal ally of Rashtrakutas; performed *Sallekhana* vow at Bankapur under sage Ajitasena. |
| **Rachamalla IV** | c. 974 – 999 CE | His prime minister **Chavundaraya** erected the Shravanabelagola Gommateshwara statue (981 CE); patron of poet Ranna. |

### 4.2 Durvinita's Literary and Epigraphical Stature
King Durvinita is celebrated as one of the most intellectually accomplished monarchs of ancient India:
- Composed a Sanskrit commentary on the difficult 15th Sarga (canto) of poet Bharavi's epic **Kiratarjuniya (ಕಿರಾತಾರ್ಜುನೀಯ)**.
- Translated Gunadhya's famous **Brihatkatha (ಬೃಹತ್ಕಥಾ)** from the vernacular *Paisachi* language into classical Sanskrit.
- Authored a treatise on Sanskrit grammar titled **Shabdavatara (ಶಬ್ದಾವತಾರ)**.
- Mentioned by Sri Vijaya in the *Kavirajamarga* (c. 850 CE) as one of the pre-eminent early masters of Kannada prose (*Gadyada Pravararu*).

---

## 5. Shravanabelagola and the Gommateshwara Monolith (981 CE)

### 5.1 Chavundaraya (ಚಾವುಂಡರಾಯ) — The Statesman-Scholar
- Served as Commander-in-Chief and Prime Minister (*Sarvasainyadhikari*) under Ganga kings Marasimha II and Rachamalla IV.
- Bearing titles *Samara Parashurama* (Parashurama in war) and *Gunaratnabhushana*.
- Authored **Chavundaraya Purana (ಚಾವುಂಡರಾಯ ಪುರಾಣ)** in 978 CE (formally titled *Trishashti Lakshana Mahapurana*), the earliest extant dated continuous prose work in Kannada detailing the lives of 24 Tirthankaras.
- Authored **Charitrasara** in Sanskrit on Jain ethics.

### 5.2 The Monolithic Gommateshwara Colossus (ಗೊಮ್ಮಟೇಶ್ವರ ಏಕಶಿಲಾ ವಿಗ್ರಹ)
- **Location**: Summit of **Vindhyagiri (ದೊಡ್ಡಬೆಟ್ಟ)** in Shravanabelagola, Hassan district.
- **Date of Consecration**: **13 March 981 CE** (Sunday, *Phalguna Shukla Panchami*).
- **Physical Dimensions**: Height of **57 feet (17.5 meters)**; carved from a single continuous block of fine-grained light-grey granite in-situ.
- **Iconography**: Depicts **Bahubali (ಬಾಹುಬಲಿ)**, son of the first Tirthankara Rishabhanatha (Adinatha), standing in the unmoving *Kayotsarga* meditation posture. Anthills (*valmika*) and creepers (*madhavi lata*) entwine his legs and arms, symbolizing complete victory over the senses and ego.
- **Epigraphy at the Foot**: Inscriptions in three languages (Kannada, Marathi, Tamil) record the patronage:
  > *"Sri Chavundarajan Karavisidam"* (ಶ್ರೀ ಚಾವುಂಡರಾಜನ್ ಕರಾವಿಸಿದಂ - Kannada)
  > *"Sri Chavundaraje Karaviyale"* (Marathi - recognized as the earliest dated epigraphic record in the Marathi language).
- **Mahamastakabhisheka (ಮಹಾಮಸ್ತಕಾಭಿಷೇಕ)**: The grand consecration ritual held once every 12 years; last conducted in February 2018; next scheduled for 2030.

---

## 6. The Culture of Hero Stones (ವೀರಗಲ್ಲು) and Sallekhana (ಸಲ್ಲೇಖನ)

### 6.1 Hero Stones (*Veergallu*)
- Karnataka possesses the highest concentration of hero stones in India (over 10,000 recorded stones).
- **Structure**: Typically divided into three or four vertical panels:
  - *Bottom Panel*: The hero fighting fiercely on the battlefield or defending cattle (*Gograhana* - ಗೋಗ್ರಹಣ) or women.
  - *Middle Panel*: Heavenly nymphs (*Apsaras*) carrying the slain hero through the sky to heaven.
  - *Top Panel*: The hero seated in the divine presence of Shiva (as a Linga) or a Jina.
- The famous **Begur Hero Stone (ಬೇಗೂರು ವೀರಗಲ್ಲು)** (c. 908 CE, preserved in the Bengaluru Museum) records the Battle of Bengaluru (*Bengaluru Kalaga*) fought between Ganga King Ereyappa and Nolamba rulers.

### 6.2 The Ritual of Sallekhana and *Nishidhi* (ನಿಷಿಧಿ) Stones
- **Sallekhana (ಸಲ್ಲೇಖನ / ಸನ್ಯಸನ)**: The voluntary termination of life by gradual fasting when facing extreme old age, incurable illness, or calamity, with a peaceful, detached mind.
- **Chandragupta Maurya Tradition**: Jain tradition records that Emperor Chandragupta Maurya, guided by sage Bhadrabahu, migrated to Shravanabelagola during a 12-year famine in Magadha and performed Sallekhana at **Chandragiri hill (ಚಿಕ್ಕಬೆಟ್ಟ)** c. 297 BCE.
- Monuments commemorating individuals who completed the vow are called **Nishidhi Stones (ನಿಷಿಧಿಗಲ್ಲು)**.

---

## 7. Comparative Synoptic Matrix

| Parameter | The Kadambas of Banavasi | The Western Gangas of Talakadu |
|---|---|---|
| **Capital City** | Banavasi (*Vaijayanti*), later Triparvata | Kolar (*Kuvalala*), later Talakadu (*Talavanapura*) |
| **Royal Crest / Emblem** | Lion (*Simha*) and Monkey (*Vanara*) | Caparisoned War Elephant (*Pattavardhana Gaja*) |
| **Dominant Religion** | Vedic Shaivism & Jainism | Jainism (primary royal creed) & Vaishnavism |
| **Linguistic Milestone** | **Halmidi Inscription (c. 450 CE)** | **Chavundaraya Purana (978 CE)** & Gommateshwara |
| **Key Royal Scholar** | Poet Kubja (Talagunda inscription) | King Durvinita & Prime Minister Chavundaraya |
| **Architectural Style** | Stepped-pyramidal *Kadamba Shikara* | Monolithic Bahubali & Dravidian granite temples |
| **Gold Coinage** | *Padmatankas* (Lotus-punched coins) | *Gajapati Tankas* (Elephant-stamped coins) |

---

## 8. Prelims Traps & Mains Answer Blueprint

### 8.1 Prelims Traps
> [!caution]
> - **Trap 1**: Confusing the capitals. Kadambas shifted from Banavasi to Triparvata; Western Gangas moved from Kolar to Talakadu (and briefly Manyapura/Manne).
> - **Trap 2**: Believing the Halmidi inscription mentions the Gangas. *Fact*: It records a grant by Kadamba King Kakusthavarma to Vijaarasa of the Sendraka family for fighting against Pallavas and Kekayas.
> - **Trap 3**: Believing Chavundaraya was a Ganga King. *Fact*: Chavundaraya was the Prime Minister and General under Ganga King Rachamalla IV.

### 8.2 Mains Model Question & Answer Blueprint
**Question**: *Assess the contributions of the Kadambas of Banavasi and Western Gangas of Talakadu to the development of Kannada language, literature, and indigenous political culture.* (Marks: 12.5 / 150 Words)

**Model Answer Outline**:
1. **Introduction (25 words)**:
   - Identify Kadambas and Gangas as the twin foundational indigenous powers that established Karnataka's distinct political boundary, language primacy, and institutional framework from the 4th to 10th century CE.
2. **Body 1: Linguistic and Epigraphical Foundations (50 words)**:
   - **Kadambas**: Halmidi Inscription (c. 450 CE) marks the earliest epigraphic use of Old Kannada in administration. Talagunda inscription exemplifies high classical Sanskrit court literature.
   - **Gangas**: Patronized poet Durvinita (celebrated in *Kavirajamarga*), Shivamara II (*Gajashtaka*), and Chavundaraya (*Chavundaraya Purana* 978 CE - first prose work).
3. **Body 2: Art, Architecture & Religious Institutions (50 words)**:
   - Kadamba stepped-pyramidal *Kadamba Shikara* set the architectural precedent for Chalukyan and Hoysala vimanas.
   - Gangas transformed Shravanabelagola into a pan-Indian Jain cultural center through the monolithic Gommateshwara (981 CE), and fostered the commemorative hero stone (*Veergallu*) tradition.
4. **Conclusion (25 words)**:
   - Summarize that their six centuries of rule firmly rooted Kannada linguistic identity and regional statecraft, laying the bedrock for the imperial achievements of the Chalukyas and Rashtrakutas.

---

## 9. Sources and Verification
- **Verified On**: 2026-10-13 (Tuesday)
- **Primary Source 1**: Epigraphia Carnatica, Vol. II (Inscriptions at Sravana Belgola) & Vol. VII (Shimoga District).
- **Primary Source 2**: Dr. Suryanath Kamath, *A Concise History of Karnataka*, MCC, Bengaluru.
- **Primary Source 3**: Dr. B.L. Rice, *Epigraphical Discoveries in Mysore*, Journal of the Royal Asiatic Society.
"""
    safe_write(path, content)
    print(f"Created: {path} ({len(content.split())} words)")

if __name__ == "__main__":
    create_note_kadambas_gangas()
