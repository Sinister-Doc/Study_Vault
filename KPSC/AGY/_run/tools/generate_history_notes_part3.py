import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

HIST_DIR = os.path.join(ROOT_DIR, "03_Notes", "01_Karnataka_History_and_Culture")

def create_note_badami_chalukyas():
    path = os.path.join(HIST_DIR, "Badami_Chalukyas_Architecture_and_Empire.md")
    content = """---
title: The Chalukyas of Badami, Empire and Architectural Renaissance
last_verified: 2026-10-13
sources:
  - "Karnataka State Textbooks (KTBS) - 1st PUC History (Chapter 5)"
  - "Dr. Suryanath Kamath, A Concise History of Karnataka, Chapter 6: The Chalukyas of Badami"
  - "K.A. Nilakanta Sastri, A History of South India"
  - "Epigraphia Indica, Vol. VI (The Aihole Inscription of Pulakeshin II)"
syllabus_lines: ["P1-S2.1", "P1-S2.2", "M-GS1-S1.1", "M-GS1-S1.2"]
priority: high
tags: ["karnataka-history", "badami-chalukyas", "pulakeshin-ii", "aihole", "pattadakal", "vesara-architecture"]
---

# The Chalukyas of Badami, Empire and Architectural Renaissance (ಬಾದಾಮಿ ಚಾಲುಕ್ಯರು, ಸಾಮ್ರಾಜ್ಯ ಮತ್ತು ವಾಸ್ತುಶಿಲ್ಪ ನವೋದಯ)

> [!exam-focus]
> **KPSC High-Yield Examination Focus**:
> - **Founder**: Pulakeshin I (c. 543-566 CE); fortified the natural sandstone cliff of Vatapi (Badami) in Bagalkote district and conducted the *Ashvamedha* horse sacrifice.
> - **Pulakeshin II (ಪುಲಕೇಶಿ II, c. 609-642 CE)**: Greatest sovereign; halted the southward imperial expansion of Emperor Harshavardhana of Kannauj on the banks of the Narmada River (c. 618-619 CE), assuming the imperial title **Parameshwara (ಪರಮೇಶ್ವರ)** and *Dakshinapatheshwara*.
> - **Aihole Inscription (ಐಹೊಳೆ ಶಾಸನ, 634 CE)**: Composed in chaste classical Sanskrit *Kavya* by Jain court poet **Ravikirti (ರವಿಕೀರ್ತಿ)** on the eastern wall of Meguti Jain temple. Establishes the exact chronology of Pulakeshin II's conquests; asserts Ravikirti's poetic brilliance as equal to Kalidasa and Bharavi.
> - **Diplomacy & Foreign Accounts**: Exchange of embassies with Sassanid Persian King Khosrow II (Pervez) as depicted in Cave 1 paintings at Ajanta; Chinese pilgrim Hiuen Tsang (Xuanzang) visiting Maharashtra/Karnataka in 640-641 CE.
> - **Genesis of Vesara Temple Architecture**: The experimental laboratory at **Aihole** ("Cradle of Indian Temple Architecture" with 120+ temples), rock-cut sanctuaries at **Badami**, and climax at **Pattadakal (ಪಟ್ಟದಕಲ್ಲು - UNESCO World Heritage Site)** featuring the monumental Virupaksha and Mallikarjuna temples.

---

## 1. Political Emergence and Imperial Expansion

The Chalukyas of Badami (c. 543 – 753 CE) welded the Deccan into a unified political imperium for over two centuries, bridging northern and southern cultural forms.

```mermaid
flowchart TD
    PULAKESHIN_I["Pulakeshin I (c. 543-566 CE)\nFortifies Vatapi (Badami) cliff\nPerforms Ashvamedha, Agnistoma"] --> KIRTIVARMAN_I["Kirtivarman I (c. 566-597 CE)\nDefeats Nalas, Mauryas of Konkan, Kadambas\nBegins Badami rock-cut cave temples"]
    KIRTIVARMAN_I --> MANGALESHA["Mangalesha (c. 597-609 CE)\nRegent; Conquers Revatidvipa (Goa)\nConsecrates Cave 3 (Maha Vishnu)\nCivil War over succession"]
    MANGALESHA --> PULAKESHIN_II["Pulakeshin II (c. 609-642 CE)\nGreatest Deccan Emperor\nBattle of Narmada: Defeats Harsha (618 CE)\nSubjugates Kadambas, Gangas, Pallavas\nIssues Aihole Inscription (634 CE)"]
    PULAKESHIN_II --> PALLAVA_INVASION["Pallava Narasimhavarman I attacks Vatapi (642 CE)\nPulakeshin II dies in battle\n13-Year Interregnum"]
    PALLAVA_INVASION --> VIKRAMADITYA_I["Vikramaditya I (c. 655-681 CE)\nLiberates Badami, drives out Pallavas\nCaptures Kanchi in retaliation"]
    VIKRAMADITYA_I --> VIKRAMADITYA_II["Vikramaditya II (c. 733-744 CE)\nThrice captures Pallava capital Kanchi\nSpares Kailasanatha temple, engraves Kannada victory inscription\nQueens build Virupaksha & Mallikarjuna at Pattadakal"]
    VIKRAMADITYA_II --> KIRTIVARMAN_II["Kirtivarman II (c. 744-753 CE)\nOverthrown by Rashtrakuta feudatory Dantidurga"]
```

### 1.1 Pulakeshin II: The Pinnacle of Deccan Suzerainty
- **Ascension to the Throne**: Mangalesha sought to bypass Pulakeshin II (son of Kirtivarman I) in favor of his own son. Pulakeshin fled to the Bana territory, raised an army, defeated and killed Mangalesha at Elapattu-Simbige, and secured the throne in 609 CE.
- **The Northern War & Defeat of Harsha**:
  - Emperor Harshavardhana of Kannauj had conquered the entire Indo-Gangetic plain (*Sakalottarapathanatha*). As Harsha marched south to annex the Deccan, Pulakeshin II met him on the rugged banks of the **Narmada River** (c. 618-619 CE).
  - Pulakeshin II's elephant corps and seasoned infantry decisively shattered Harsha's army. Harsha was forced to accept the Narmada as the perpetual border between the northern and southern empires.
  - Pulakeshin II assumed the supreme sovereign title **Parameshwara (ಪರಮೇಶ್ವರ)**.
- **Subjugation of Eastern Deccan**: Pulakeshin II appointed his younger brother **Kubja Vishnuvardhana** as viceroy of Vengi, who subsequently founded the long-lived dynasty of the **Eastern Chalukyas of Vengi (ವೆಂಗಿಯ ಪೂರ್ವ ಚಾಲುಕ್ಯರು)** in Andhra.

---

## 2. The Aihole Inscription (634 CE) — Epigraphical Masterpiece

Carved on the eastern wall of the Meguti Jain temple at Aihole (Bagalkote district), this 19-line Sanskrit inscription is among the most famous in Indian history.

```
Key Historical Disclosures of the Aihole Inscription (ರವಿಕೀರ್ತಿಯ ಐಹೊಳೆ ಶಾಸನ)
├── Author & Date: Composed by court poet Ravikirti in Shaka 556 (634 CE) / Kaliyuga 3735.
├── Literary Claim: Ravikirti boasts his poetic fame equals Kalidasa and Bharavi:
│   "ಯೆನಾಕಾರಿ ಕವಿತಾಸು ಕವಿತಾ ಕಾಳಿದಾಸ ಭಾರವಿ ಕೀರ್ತಿಃ" (Equal in fame to Kalidasa and Bharavi).
├── Military Chronicle:
│   ├── Defeat of Appayika and Govinda who rebelled against Pulakeshin.
│   ├── Storming of Banavasi (Kadambas) and subjugation of Gangas of Talakadu and Alupas.
│   ├── Naval assault and capture of Puri (Elephanta island) from Mauryas of Konkan with 100 ships.
│   ├── Subjugation of Latas, Malavas, and Gurjaras as tributary allies.
│   └── Defeat of Harsha: "Harsha whose joy (harsha) melted away through fear" (ಭಯವಿಗಳಿತಹರ್ಷೊ ಯಸ್ಯ ಚಾಕಾರ ಹರ್ಷಃ).
└── Chronological Value: Provides an anchor date for computing the Kaliyuga and Shaka eras.
```

---

## 3. Society, Religion and Hiuen Tsang's Account (640 CE)

The Chinese Buddhist pilgrim **Hiuen Tsang (Xuanzang)** visited Pulakeshin II's realm (which he designated *Mo-ho-la-ch'a* / Maharashtra-Karnata) in 640-641 CE. His travelogue *Si-Yu-Ki* records:
- **Character of the People**: "The inhabitants are proud, warlike, and spirited; grateful for favors, vengeful for wrongs. If insulted, they risk their lives to avenge it. If anyone in distress seeks their help, they forget their own safety to succor him. If an enemy surrenders, they do not slay him."
- **Military Prowess**: "The king possesses hundreds of war elephants intoxicated with liquor before battle. When the general loses a battle, he is not punished, but presented with women's clothes, driving him to commit suicide out of shame."
- **State Prosperity**: Flourishing agriculture, vibrant overseas trade through ports like Kalyan, Chaul, and Goa, and extensive Buddhist and Brahmanical establishments living in mutual coexistence.

---

## 4. The Architectural Renaissance: Genesis of the Vesara Style

The Chalukyas of Badami synthesized the square cruciform tower of the Northern Nagara style with the horizontal stepped tiers of the Southern Dravidian style to create the **Vesara Style (ವೇಸರ / ಕರ್ನಾಟಕ ದ್ರಾವಿಡ ಶೈಲಿ)**.

```mermaid
flowchart LR
    AIHOLE["Aihole (ಐಹೊಳೆ)\n'Cradle of Indian Architecture'\n120+ Structural Temples\nExperimentation Stage (5th-7th C)"] --> BADAMI["Badami (ಬಾದಾಮಿ)\nRock-Cut Cave Temples\nSandstone Escarpments\nCave 1 (Shiva), Cave 2 & 3 (Vishnu), Cave 4 (Jaina)"]
    BADAMI --> PATTADAKAL["Pattadakal (ಪಟ್ಟದಕಲ್ಲು)\nUNESCO World Heritage Site (1987)\nCulmination of Vesara & Dravida\nRoyal Coronation Site (ಕಿಸುವೊಳಲ್)"]
```

### 4.1 Aihole: The Experimental Laboratory
- Over 120 stone temples dating from the 5th to 8th centuries CE.
- **Lad Khan Temple**: Originally a community hall / *mandapa*, converted into a Shiva temple; features a flat roof with stone logs imitating wooden post-and-beam construction.
- **Durga Temple**: Celebrated for its unique **apsidal (horseshoe-shaped) ground plan**, modeled after Buddhist *chaitya* halls; encircled by an open pillared ambulatory (*pradakshinapatha*).
- **Huchimalli Gudi**: Introduced the *shukanasa* (vestibule / antechamber connecting sanctum to hall).
- **Meguti Jain Temple**: Built entirely of stone blocks on an elevated hillock by poet Ravikirti in 634 CE; houses the Aihole inscription.

### 4.2 Badami: The Rock-Cut Cave Sanctuaries
Four magnificent pillared cave temples carved into the red sandstone cliffs overlooking the Agastya Tirtha lake:
- **Cave 1 (Shaiva)**: Features a life-size 18-armed dancing Shiva Nataraja performing the *Tandava*, capable of forming 81 distinct Bharatanatyam postures.
- **Cave 2 (Vaishnava)**: Dedicated to Vishnu as Trivikrama / Vamana, with one foot planted on earth and the other raised to the heavens.
- **Cave 3 (Vaishnava - Maha Vishnu)**: Largest and most ornate cave; excavated by King Mangalesha in Shaka 500 (578 CE); contains relief of Vishnu seated on the coiled serpent Adishesha, Varaha rescuing Bhudevi, and Narasimha.
- **Cave 4 (Jaina)**: Carved in the late 6th century; contains sanctum of Tirthankara Parshvanatha with five-hooded serpent and Bahubali Gommateshwara in meditation.

### 4.3 Pattadakal (ಪಟ್ಟದಕಲ್ಲು) — UNESCO World Heritage Monument (1987)
Situated on the banks of the north-flowing Malaprabha River (*Uttara Vahini*), Pattadakal (*Kisuvolal* - ಕಿಸುವೊಳಲ್) was the sacred ceremonial site where Chalukya kings were consecrated (*Pattabhisheka*).
- **Virupaksha Temple (Lokeshwara Temple)**:
  - Built c. 740 CE by Senior Queen **Lokamahadevi (ಲೋಕಮಹಾದೇವಿ)** to celebrate King Vikramaditya II's third victorious capture of the Pallava capital Kanchipuram.
  - Architect: **Gunda Anivaritachari** (honored with the royal title *Tribhuvanachari* - Architect of the Three Worlds).
  - Modeled closely on the Kailasanatha temple of Kanchi, but surpassed it in sculptural elegance; later served as the direct architectural prototype for the monolithic Kailasa temple at Ellora built by Rashtrakuta Krishna I.
- **Mallikarjuna Temple (Trailokyeshwara Temple)**: Built adjacent to Virupaksha by Junior Queen **Trailokyamahadevi**.
- **Papanatha Temple**: Remarkable for its hybrid design—incorporating a Northern Nagara curvilinear tower (*Rekha-Nagara Shikara*) on a Southern Dravidian floor plan.
- **Galaganatha & Sangameshwara Temples**: Sangameshwara (built by Vijayaditya) represents pure early Dravidian architecture.

---

## 5. Synoptic Matrix of Badami Chalukya Monarchs & Monuments

| Monarch | Capital & Emblem | Major Architectural Commission | Epigraphs & Literary Works |
|---|---|---|---|
| **Pulakeshin I** (543-566) | Vatapi; Varaha (Boar crest) | Badami Fortification cliff | Badami cliff inscription (543 CE) |
| **Kirtivarman I** (566-597) | Vatapi; Varaha | Initiated Badami Cave temples | Godachi copper plate |
| **Mangalesha** (597-609) | Vatapi; Varaha | Consecrated Cave 3 (Maha Vishnu) | Mahakuta Pillar Inscription (602 CE) |
| **Pulakeshin II** (609-642) | Vatapi; Varaha | Meguti Jain Temple at Aihole | **Aihole Inscription (634 CE)** |
| **Vikramaditya I** (655-681) | Vatapi; Varaha | Reconstructed damaged shrines | Gadval & Kurnool plates |
| **Vijayaditya** (696-733) | Vatapi; Varaha | Sangameshwara temple (Pattadakal) | Longest peaceful reign (37 years) |
| **Vikramaditya II** (733-744) | Vatapi; Varaha | Virupaksha & Mallikarjuna (Pattadakal) | Kanchi Kailasanatha Kannada Pillar Inscription |

---

## 6. Prelims Traps & Mains Answer Blueprint

### 6.1 Prelims Traps
> [!caution]
> - **Trap 1**: Believing the Meguti temple at Aihole is a Hindu temple. *Fact*: It is a **Jain temple** dedicated to Vardhamana Mahavira, commissioned by poet Ravikirti.
> - **Trap 2**: Confusing who constructed the Virupaksha temple at Pattadakal. *Fact*: It was commissioned by Queen **Lokamahadevi**, not King Vikramaditya II himself, although it commemorated his victory over Kanchi.
> - **Trap 3**: Confusing Aihole with Pattadakal as the UNESCO site. *Fact*: Only **Pattadakal** is a UNESCO World Heritage Site (inscribed 1987). Aihole is on the tentative list.

### 6.2 Mains Model Question & Answer Blueprint
**Question**: *Analyze the architectural evolution from rock-cut shrines to structural temples under the Chalukyas of Badami. Why is Aihole designated as the 'Cradle of Indian Temple Architecture'?* (Marks: 15 / 250 Words)

**Model Answer Outline**:
1. **Introduction (35 words)**:
   - Identify the Badami Chalukyas (6th-8th century CE) as the creators of the Vesara (Karnataka Dravida) style, bridging North Indian Nagara and South Indian Dravidian architectural idioms in the Malaprabha river basin.
2. **Body 1: The Aihole Experimental Crucible (75 words)**:
   - Over 120 stone temples at Aihole document the trial-and-error experimentation of ancient Indian guilds.
   - *Lad Khan Temple*: Progression from flat-roofed post-and-lintel wooden hall assemblies to stone pillared mandapas.
   - *Durga Temple*: Adaptation of the apsidal Buddhist chaitya layout into a Hindu sanctum with a curvilinear shikhara and pillared parikrama.
   - Introduction of foundational components: *Shukanasa* (vestibule), *Garbhagriha* (sanctum), *Gudhamandapa*, and lattice stone jali windows.
3. **Body 2: Rock-Cut Caves to Pattadakal Masterpieces (90 words)**:
   - *Badami Sandstone Escarpment*: Cave 1-4 demonstrate mastery of monumental narrative relief carving (Nataraja 81 poses, Trivikrama, Anantasayana Vishnu).
   - *Pattadakal Zenith*: Synthesis of northern and southern idioms side-by-side. Papanatha (Nagara curvilinear tower) standing beside Virupaksha (Dravida tiered pyramidal vimana).
   - Virupaksha's sophisticated plan (mandapa with 16 sculpted pillars, separate Nandi pavilion, subsidiary shrines) influenced the monolithic Kailasa temple at Ellora.
4. **Conclusion (30 words)**:
   - Conclude that the stylistic vocabulary formulated by Chalukyan master craftsmen (*Gunda Anivaritachari*) at Aihole and Pattadakal directly seeded the subsequent architectural triumphs of the Rashtrakutas, Kalyana Chalukyas, and Hoysalas.

---

## 7. Sources and Verification
- **Verified On**: 2026-10-13 (Tuesday)
- **Primary Source 1**: Archaeological Survey of India (ASI), *World Heritage Series: Pattadakal*, New Delhi.
- **Primary Source 2**: Dr. Suryanath Kamath, *A Concise History of Karnataka*, MCC, Bengaluru.
- **Primary Source 3**: K.A. Nilakanta Sastri, *A History of South India*, Oxford University Press.
"""
    safe_write(path, content)
    print(f"Created: {path} ({len(content.split())} words)")

if __name__ == "__main__":
    create_note_badami_chalukyas()
