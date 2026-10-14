import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

HIST_DIR = os.path.join(ROOT_DIR, "03_Notes", "01_Karnataka_History_and_Culture")

def create_note_nayakas():
    path = os.path.join(HIST_DIR, "Nayakas_of_Keladi_and_Chitradurga.md")
    content = """---
title: The Nayakas of Keladi, Chitradurga and the Yelahanka Nadaprabhus
last_verified: 2026-10-13
sources:
  - "Karnataka State Textbooks (KTBS) - 1st PUC History (Chapter 11)"
  - "Dr. Suryanath Kamath, A Concise History of Karnataka, Chapter 12: Nayakas of Keladi and Chitradurga"
  - "K.D. Swaminathan, The Nayakas of Ikkeri, P. Varadachary & Co."
  - "B.L. Rice, Mysore Gazetteer, Vol. II"
syllabus_lines: ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.3"]
priority: high
tags: ["karnataka-history", "keladi-nayakas", "shivappa-nayaka-shistu", "rani-chennamma", "chitradurga-nayakas", "onake-obavva", "kempe-gowda"]
---

# The Nayakas of Keladi, Chitradurga and the Yelahanka Nadaprabhus (ಕೆಳದಿಯ ನಾಯಕರು, ಚಿತ್ರದುರ್ಗದ ಪಾಳೆಯಗಾರರು ಮತ್ತು ಯಲಹಂಕದ ನಾಡಪ್ರಭುಗಳು)

> [!exam-focus]
> **KPSC High-Yield Examination Focus**:
> - **Keladi / Ikkeri / Bednore Nayakas**:
>   - Founded by Chaudappa (c. 1499 CE); capitals shifted chronologically: **Keladi -> Ikkeri -> Bednore (Bidanur)**.
>   - **Shivappa Nayaka's Shistu (ಶಿವಪ್ಪ ನಾಯಕನ ಶಿಸ್ತು)**: Exemplary scientific land revenue assessment model based on 5-year average yields and soil categorization (*Uttama, Madhyama, Kanishtha*); defended coastal Karnataka and built Bekal and Mirjan forts; granted refuge to Vijayanagara Emperor Sriranga III.
>   - **Rani Chennamma of Keladi (1671-1696 CE)**: Heroic resistance against Mughal Emperor Aurangzeb; gave political shelter to Maratha King **Chhatrapati Rajaram** (son of Shivaji); defeated allied Mughal and Bijapur armies in the Malnad jungles.
>   - **Shivatattva Ratnakara**: Monumental Sanskrit encyclopedia of 108 *Tarangas* authored by King Basavaraja Nayaka.
> - **Nayakas of Chitradurga (ಪಾಳೆಯಗಾರರು)**:
>   - Architectural defense of the **Seven-Ringed Rock Fort (*Kallina Kote* - ಕಲ್ಲಿನ ಕೋಟೆ)** with natural granite monoliths, *Diddi Bagilu* crevices, and rainwater tanks (*Goni Honda*).
>   - **Onake Obavva (ಒನಕೆ ಓಬವ್ವ, 1779 CE)**: Wife of watchman Kahlaga; single-handedly crushed dozens of infiltrating soldiers of Hyder Ali using a heavy wooden pestle (*Onake*) at the secret crevice (*Kinnari Joga Diddi*).
>   - **Madakari Nayaka V**: Last sovereign; captured and deported by Hyder Ali in 1779 CE.
> - **Yelahanka Nadaprabhus (Founders of Bengaluru)**:
>   - **Kempe Gowda I (ಕೆಂಪೇಗೌಡ I, 1510-1569 CE)**: Founded modern **Bengaluru in 1537 CE** with mud fort and commercial Petes; built **Four Watchtowers (ನಾಲ್ಕು ಗೋಪುರಗಳು)** predicting city borders; excavated Dharmambudhi, Kempambudhi, and Karanji lakes; consecrated Bull Temple (Basavanagudi).

---

## 1. The Nayakas of Keladi / Ikkeri / Bednore (1499–1763 CE)

The Keladi Kingdom emerged as the strongest post-Vijayanagara state in the Western Ghats (Malnad) and coastal Kanara, defending indigenous culture for two and a half centuries.

```mermaid
flowchart TD
    CHAUDAPPA["Chaudappa & Bhadrappa (1499 CE)\nFounding at Keladi village\nLoyal feudatory of Vijayanagara Krishnadevaraya"] --> SADASHIVA["Sadashiva Nayaka (1540-1565 CE)\nTitle: 'Kotegola Suratrana'\nShifts capital to Ikkeri\nConstructs Aghoreshwara Temple"]
    SADASHIVA --> SHIVAPPA["Shivappa Nayaka (1645-1660 CE)\nImperial Zenith: Conquers Kanara coast from Portuguese\nInstitutes scientific 'Shistu' revenue system\nConstructs Bekal, Chandragiri & Mirjan forts"]
    SHIVAPPA --> CHENNAMMA["Rani Chennamma of Keladi (1671-1696 CE)\nDefies Mughal Emperor Aurangzeb\nProtects Chhatrapati Rajaram (Shivaji's son)\nDefeats Mughal forces in Malnad wars"]
    CHENNAMMA --> BASAVARAJA["Basavaraja Nayaka (1696-1714 CE)\nScholar-King; Authors Sanskrit encyclopedia 'Shivatattva Ratnakara'"]
    BASAVARAJA --> HYDER_ALI["Queen Virammaji conquered by Hyder Ali of Mysore (1763 CE)\nBednore annexed; renamed Haidernagar"]
```

### 1.1 Shivappa Nayaka and the "Shistu" Revenue Reform (ಶಿಸ್ತು)
Shivappa Nayaka was celebrated across the Deccan for his agrarian reforms, creating the **Shistu (ಶಿಸ್ತು - Systematic Land Settlement)**, which became the benchmark for subsequent revenue models in Mysore and British Kanara:
- **Scientific Land Classification**:
  - Divided agricultural lands into four precise fertility grades: *Uttama* (Superior), *Madhyama* (Average), *Kanishtha* (Inferior), and *Adhama* (Barren/Marginal).
  - Differentiated between *Tari* (wet paddy land), *Kushki* (dry rainfed land), and *Bagayat* (arecanut, pepper, and coconut garden land).
- **Yield Assessment (*Praja Gurutu*)**:
  - Maintained five-year rolling average records of grain yield for every plot.
  - One-third of the gross yield on wet lands and one-sixth on dry lands was collected as royal tax, payable in either cash or grain (*Danya*).
- **Commercial Sovereignty**: Expelled the Portuguese from their fortified trading posts at Mangaluru, Honnavar, and Kundapura, ending their exploitative monopoly over rice and pepper exports.

### 1.2 Rani Chennamma of Keladi: Defiance of the Mughal Empire (1689 CE)
- **The Crisis**: In 1689 CE, following the brutal execution of Chhatrapati Sambhaji by Mughal Emperor Aurangzeb, Sambhaji's younger brother **Chhatrapati Rajaram** fled Maharashtra disguised as an ascetic, desperately seeking refuge in the South while fleeing relentless Mughal pursuit.
- **The Decision**: Every ruler in the Deccan refused shelter for fear of Aurangzeb's wrath. When Rajaram reached Bednore, Queen **Chennamma** granted him full royal asylum, protection, and military escort to reach the fortress of Jinji in Tamil Nadu.
- **The Mughal War**: Enraged, Aurangzeb dispatched his Mughal imperial army under General Jan Nisar Khan to invade Keladi. Chennamma retreated into the dense tropical rainforests of the Western Ghats, employed devastating guerrilla warfare, cut off Mughal supply lines, and routed the imperial troops.
- **Peace Treaty**: Aurangzeb recognized Chennamma's valor and concluded a peace treaty, sending her rich gifts, while the Maratha state survived through her courage.

---

## 2. The Nayakas of Chitradurga (1568–1779 CE)

The Beda (Valmiki) Nayakas of Chitradurga established one of the most formidable hill fortresses in peninsular India, maintaining independence from the Bijapur Sultans, Marathas, and Mysore kings.

```mermaid
flowchart TD
    TIMMANNA["Timmanna Nayaka (1568 CE)\nAppointed Palegar by Vijayanagara Vijayanagara Emperor\nFortifies Chitradurga granite hills"] --> KASTURI["Kasturi Rangappa & Baramanna Nayaka\nExpands territory to Davanagere & Ballari\nConstructs Seven Walls & Water Tanks"]
    KASTURI --> MADAKARI_V["Madakari Nayaka V (1758-1779 CE)\nHeroic defense against repeated sieges of Hyder Ali\nSupported Marathas at Battle of Oorukere"]
    MADAKARI_V --> OBAVVA["The Siege of 1779 CE\nOnake Obavva slays infiltrators at Kinnari Joga Diddi\nObavva martyred; Fort falls through exhaustion"]
    OBAVVA --> FALL["Hyder Ali captures Chitradurga (1779 CE)\nMadakari Nayaka imprisoned; Beda army absorbed into Mysore"]
```

### 2.1 The Seven-Ringed Rock Fortress (*Kallina Kote* - ಕಲ್ಲಿನ ಕೋಟೆ)
- Engineered around a cluster of gigantic granite boulders rising 3,000 feet above sea level.
- Designed with **Seven Concentric Enceintes (ಏಳು ಸುತ್ತಿನ ಕೋಟೆ)**:
  - Outer walls feature labyrinthine zigzag entrances designed to prevent enemy elephants from gaining battering momentum.
  - Secret trap crevices (*Diddi Bagilu*) and underground escape tunnels (*Suranga Margagalu*).
  - Revolutionary Rainwater Harvesting: Constructed interconnected cascading storage tanks (**Goni Honda, Akka-Thangiyara Honda, Santhe Honda**) ensuring the garrison never surrendered due to water scarcity during multi-year sieges.

### 2.2 The Epic Heroism of Onake Obavva (1779 CE)
- During Hyder Ali's prolonged siege of Chitradurga in 1779 CE, his reconnaissance scouts discovered a secret narrow fissure in the granite ramparts known as the **Kinnari Joga Diddi (ಕಿನ್ನರಿ ಜೋಗಿ ದಿಡ್ಡಿ)**, where only a single soldier could crawl through at a time.
- The regular guard at this post, **Kahlaga**, stepped away to take his midday meal.
- His wife, **Obavva (ಓಬವ್ವ)**, went to fetch drinking water from a nearby pond and noticed the gleaming bayonets of Hyder Ali's soldiers squeezing through the rock crevice.
- Without causing panic, she grabbed a heavy household wooden pestle (**Onake - ಒನಕೆ**, used for pounding paddy) and stood concealed by the side of the narrow aperture.
- As each enemy soldier emerged head-first from the fissure, Obavva struck him with lethal force on the skull, dragged the corpse aside, and waited for the next. She single-handedly slaughtered dozens of enemy soldiers before her husband returned with reinforcements.
- Though martyred shortly thereafter in the chaos, her heroic defense immortalized her as a supreme legend of female valor in Karnataka history.

---

## 3. The Yelahanka Nadaprabhus: Kempe Gowda I (1510–1569 CE)

The Yelahanka Prabhu family (Morasu Vokkaliga chieftains) served the Vijayanagara Empire with great loyalty, founding the modern capital city of **Bengaluru**.

```
Foundational Achievements of Nadaprabhu Kempe Gowda I (1537 CE)
├── 1. Founding of Bengaluru Metropolis (1537 CE):
│   ├── Secured imperial permission from Achyuta Deva Raya of Vijayanagara.
│   ├── Built oval-shaped Mud Fort (ಮಣ್ಣಿನ ಕೋಟೆ) and excavated perimeter moat.
│   └── Laid out planned commercial streets (Petes) divided by trade:
│       • Chikkapete & Doddapete (textiles and general merchandise)
│       • Balepete (bangles and glass ornaments)
│       • Aralepete (cotton merchant street - modern Cottonpet)
│       • Tharagupete (wholesale grain and agricultural commodities)
│       • Akkipete (rice and cereals market)
│       • Tigalarapete (vegetable and flower gardeners)
├── 2. The Four Boundary Watchtowers (ನಾಲ್ಕು ಗಡಿ ಗೋಪುರಗಳು):
│   └── Constructed 4 sentinel towers predicting the outer boundary of the future city:
│       1. North Tower: Near Mekhri Circle / Palace Guttahalli.
│       2. South Tower: At Lalbagh rock summit.
│       3. East Tower: Near Halasuru (Ulsoor) Lake.
│       4. West Tower: On the ridge overlooking Kempambudhi Lake.
└── 3. Water Reservoirs and Monumental Shrines:
    ├── Interconnected lake grid: Dharmambudhi Lake (Majestic Bus Stand site),
    │   Kempambudhi Lake, Karanji Lake, and Sampangi Lake (Kanteerava Stadium site).
    └── Consecrated the Bull Temple (Dodda Basavana Gudi) and Gavi Gangadhareshwara Cave Temple.
```

---

## 4. Comparative Synoptic Matrix

| Dynasty / Chieftaincy | Capital Seat | Peak Sovereign | Defining Contribution |
|---|---|---|---|
| **Keladi Nayakas** | Keladi, Ikkeri, Bednore | Shivappa Nayaka & Rani Chennamma | **Shistu revenue model**; Sheltered Chhatrapati Rajaram; *Shivatattva Ratnakara*. |
| **Chitradurga Nayakas** | Chitradurga (*Kallina Kote*) | Madakari Nayaka V | Seven-ringed stone fort; **Onake Obavva's heroism** against Hyder Ali. |
| **Yelahanka Prabhus** | Yelahanka, Bengaluru, Magadi | Kempe Gowda I | **Founding of Bengaluru (1537 CE)**; Four Watchtowers; Grid of Petes & lakes. |

---

## 5. Prelims Traps & Mains Answer Blueprint

### 5.1 Prelims Traps
> [!caution]
> - **Trap 1**: Confusing Rani Chennamma of Keladi with Rani Chennamma of Kittur. *Fact*: **Rani Chennamma of Keladi** defied Mughal Emperor Aurangzeb in 1689 CE. **Rani Chennamma of Kittur** fought against the British East India Company in 1824 CE!
> - **Trap 2**: Believing the Shistu revenue system was created by the Mysore Dewans. *Fact*: It was formulated by **Shivappa Nayaka of Keladi** in the 17th century.
> - **Trap 3**: Believing Kempe Gowda built the stone fort of Bengaluru. *Fact*: Kempe Gowda I built a **mud fort** in 1537 CE. The fort was rebuilt in stone by **Hyder Ali** in 1761 CE and Tipu Sultan.

### 5.2 Mains Model Question & Answer Blueprint
**Question**: *Examine the administrative and agricultural reforms of Shivappa Nayaka of Keladi. How did the 'Shistu' system balance state revenue with farmer security?* (Marks: 12.5 / 150 Words)

**Model Answer Outline**:
1. **Introduction (25 words)**:
   - Introduce Shivappa Nayaka (1645-1660 CE) as the greatest ruler of Keladi whose land settlement (*Shivappa Nayakana Shistu*) established an enduring scientific revenue benchmark in Karnataka.
2. **Body 1: Core Mechanisms of the Shistu System (50 words)**:
   - Categorized all land into four empirical grades (*Uttama, Madhyama, Kanishtha, Adhama*) based on soil quality, water source, and distance to markets.
   - Introduced *Praja Gurutu*: Maintained five-year rolling average records of actual crop yield rather than speculative arbitrary assessments.
   - Fixed tax at 1/3rd for wet paddy and 1/6th for dry lands, with flexible options to pay in grain or cash.
3. **Body 2: Balance of State Revenue & Farmer Welfare (50 words)**:
   - Guaranteed security of land tenure; prohibited arbitrary eviction of cultivating peasants.
   - Granted state tax exemptions during drought, flood, or insect blights, preventing rural indebtedness.
   - Provided surplus state revenues that financed coastal defense fortresses (Bekal, Mirjan) against European colonialism.
4. **Conclusion (25 words)**:
   - Conclude that the Shistu system represented an enlightened indigenous fiscal model that influenced subsequent land settlements under Tipu Sultan and British land administrators in Kanara.

---

## 6. Sources and Verification
- **Verified On**: 2026-10-13 (Tuesday)
- **Primary Source 1**: Dr. Suryanath Kamath, *A Concise History of Karnataka*, MCC, Bengaluru.
- **Primary Source 2**: K.D. Swaminathan, *The Nayakas of Ikkeri*, P. Varadachary & Co., Madras.
- **Primary Source 3**: B.L. Rice, *Epigraphia Carnatica*, Vol. VIII (Shimoga District Inscriptions).
"""
    safe_write(path, content)
    print(f"Created: {path} ({len(content.split())} words)")

if __name__ == "__main__":
    create_note_nayakas()
