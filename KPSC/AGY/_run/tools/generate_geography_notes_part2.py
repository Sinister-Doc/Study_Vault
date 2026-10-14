import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

GEO_DIR = os.path.join(ROOT_DIR, "03_Notes", "03_Geography_Karnataka_and_World")

def create_note_drainage():
    path = os.path.join(GEO_DIR, "Karnataka_Drainage_and_River_Basins.md")
    content = """---
title: Karnataka Drainage Systems, River Basins, Major Dams and Water Disputes
last_verified: 2026-10-13
sources:
  - "Karnataka State Textbooks (KTBS) - 10th Standard Social Science & 2nd PUC Geography (Chapter 3)"
  - "Dr. M.B. Patil, Geography of Karnataka, Chapter 4: Drainage System"
  - "Water Resources Department (WRD), Government of Karnataka: Major & Medium Irrigation Projects"
  - "Krishna & Cauvery Water Disputes Tribunal Awards and Official Gazettes"
syllabus_lines: ["P1-S2.3", "M-GS1-S2.1", "M-GS1-S2.2"]
priority: high
tags: ["karnataka-geography", "drainage", "krishna-river", "cauvery-river", "dams-irrigation", "water-disputes"]
---

# Karnataka Drainage Systems, River Basins, Major Dams and Water Disputes (ಕರ್ನಾಟಕದ ನದೀ ವ್ಯವಸ್ಥೆ, ಜಲಾನಯನ ಪ್ರದೇಶಗಳು, ಪ್ರಮುಖ ಅಣೆಕಟ್ಟುಗಳು ಮತ್ತು ನದಿ ನೀರು ವಿವಾದಗಳು)

> [!exam-focus]
> **KPSC High-Yield Examination Focus**:
> - **Twin Drainage Asymmetry**: The Western Ghats act as the continental water divide (*Jala Vibhajaka*).
>   - **East-Flowing Rivers (ಪೂರ್ವಕ್ಕೆ ಹರಿಯುವ ನದಿಗಳು)**: Drain 80% of state's area into Bay of Bengal (Krishna, Cauvery, Pennar, Palar); long courses, broad alluvial valleys, extensive canal networks.
>   - **West-Flowing Rivers (ಪಶ್ಚಿಮಕ್ಕೆ ಹರಿಯುವ ನದಿಗಳು)**: Drain 20% into Arabian Sea (Sharavathi, Kali, Netravati, Aghanashini, Varahi); short, torrential, non-navigable courses, plunging in magnificent waterfalls with enormous **Hydroelectric Potential (ಜಲವಿದ್ಯುತ್ ಸಾಮರ್ಥ್ಯ)**.
> - **Krishna Basin (ಕೃಷ್ಣಾ ಜಲಾನಯನ)**: Largest river basin in Karnataka (59% of geographical area); enters at Kurundwad (Belagavi); major tributaries: Tungabhadra, Ghataprabha, Malaprabha, Bhima.
> - **Cauvery Basin (ಕಾವೇರಿ ಜಲಾನಯನ)**: Sacred lifeline of southern Karnataka (18% of area); originates at Talakaveri (Brahmagiri hills, Kodagu); tributaries: Hemavathi, Harangi, Lakshmanatirtha, Kabini, Shimsha, Arkavathi.
> - **Jog Falls (ಜೋಗ ಜಲಪಾತ)**: Formed by the Sharavathi River plunging **253 meters** in four distinct cascades: **Raja, Roarer, Rocket, and Rani**; feeds the Linganamakki reservoir.
> - **Major Dams & Multipurpose Projects**: Krishna Raja Sagara (KRS), Almatti Dam (Lal Bahadur Shastri Reservoir - UKP), Tungabhadra Dam (Hosapete), Supa Dam (Kali), Gorur Dam (Hemavathi).
> - **Interstate River Disputes**:
>   - **Cauvery Water Management Authority (CWMA)**: 2018 Supreme Court judgment allocating 284.75 TMC to Karnataka and mandating release of 177.25 TMC to Tamil Nadu at Biligundlu; **Mekedatu balancing reservoir** dispute.
>   - **Krishna Water Disputes Tribunal (KWDT-II)**: Brijesh Kumar award; raising Almatti dam height to 524.256 meters.
>   - **Mahadayi / Kalasa-Banduri Nala Project**: 2018 Tribunal award allocating 13.42 TMC to Karnataka (including 3.9 TMC for drinking water to Hubballi-Dharwad via Malaprabha).

---

## 1. The Continental Water Divide and Drainage Morphology

The Western Ghats ridgeline forms the principal continental drainage divide of peninsular India. Karnataka's rivers fall into two contrasting hydrological regimes:

```mermaid
flowchart TD
    DIVIDE["Western Ghats Crestline (Continental Water Divide)"]
    DIVIDE --> EAST_FLOWING["East-Flowing Drainage (80% Area)\n• Drains into the Bay of Bengal\n• Long, mature river courses with gentle gradients\n• Expansive irrigation command areas\n• 1. Krishna Basin (59% of Karnataka area)\n• 2. Cauvery Basin (18% of Karnataka area)\n• 3. North & South Pennar and Palar Basins"]
    DIVIDE --> WEST_FLOWING["West-Flowing Drainage (20% Area)\n• Drains into the Arabian Sea\n• Short, swift, torrential mountain streams\n• Steep gorges & high waterfalls\n• High Hydroelectric Power potential\n• Sharavathi (Jog 253 m), Kali, Netravati, Aghanashini, Varahi"]
```

---

## 2. The Krishna River Basin (ಕೃಷ್ಣಾ ನದೀ ವ್ಯವಸ್ಥೆ)

The Krishna is the second-largest east-flowing peninsular river in India, and the **largest river system in Karnataka**, draining 1,13,271 sq km (59.4% of the state's total area).

```
The Krishna River System in Karnataka
├── Origin: Mahabaleshwar (Maharashtra) at 1,337 m elevation.
├── Enters Karnataka: Near Kurundwad (Chikkodi taluk, Belagavi district).
├── Length in Karnataka: ~483 km (out of total 1,400 km length).
└── Major Tributaries in Karnataka:
    ├── Right-Bank Tributaries:
    │   ├── Ghataprabha (ಗಟಪ್ರಭಾ): Originates in Western Ghats; Hidkal Dam; Gokak Falls (53 m).
    │   ├── Malaprabha (ಮಲಪ್ರಭಾ): Originates at Kanakumbi (Khanapur); Navilatirtha (Renukasagar Dam).
    │   └── Tungabhadra (ತುಂಗಭದ್ರಾ): Formed by Tunga & Bhadra confluence at Kudli; Tungabhadra Dam (Hosapete).
    └── Left-Bank Tributaries:
        └── Bhima (ಭೀಮಾ): Enters at Vijayapura/Kalaburagi border; joined by Kagina River; Sonna Barrage.
```

### 2.1 Tributaries of the Krishna:
1. **Tungabhadra River (ತುಂಗಭದ್ರಾ)**:
   - Formed by the union of two sacred rivers: **Tunga** (originates at Gangamoola in Varaha Parvatha, Chikkamagaluru) and **Bhadra** (originates at Gangamoola); they flow independently and unite at **Kudli (ಕೂಡ್ಲಿ)** near Shivamogga.
   - Flows through Chikkamagaluru, Shivamogga, Davanagere, Haveri, Vijayanagara, and Ballari.
   - Tributaries: Varada and Hagari (Vedavathi). Joins the Krishna at Sangameshwara in Kurnool (AP).
   - **Tungabhadra Project (Hosapete)**: Multi-purpose dam constructed jointly by Karnataka and Andhra Pradesh; capacity ~100 TMC; irrigates extensive semi-arid tracts in Ballari, Raichur, and Koppal.
2. **Ghataprabha River (ಘಟಪ್ರಭಾ)**:
   - Flows 283 km eastward through Belagavi and Bagalkote.
   - **Gokak Falls (ಗೋಕಾಕ್ ಜಲಪಾತ)**: Plunges 53 meters over sandstone cliffs, creating the "Niagara of Karnataka"; historic hanging rope-bridge and early hydel power station (1887).
   - **Hidkal Dam (Raja Lakhamagouda Reservoir)** in Hukkeri taluk.
3. **Malaprabha River (ಮಲಪ್ರಭಾ)**:
   - Originates at Kanakumbi in Khanapur taluk, Belagavi. Flows 304 km through historic temple sites of Aihole, Pattadakal, and Badami.
   - Confluence with Krishna at the sacred pilgrim site of **Kudala Sangama (ಕೂಡಲಸಂಗಮ)**.
   - **Navilatirtha Dam (Renukasagar Reservoir)** in Saundatti taluk.
4. **Upper Krishna Project (UKP - ಕೃಷ್ಣಾ ಮೇಲ್ದಂಡೆ ಯೋಜನೆ)**:
   - Largest irrigation undertaking in Karnataka; harnesses Krishna waters for the drought-stricken districts of Vijayapura, Bagalkote, Kalaburagi, and Yadgir.
   - **Almatti Dam (ಲಾಲ ಬಹದ್ದೂರ್ ಶಾಸ್ತ್ರಿ ಜಲಾಶಯ)**: Main storage reservoir in Bagalkote; current FRL 519.60 meters; 290 MW hydel powerhouse.
   - **Narayanapura Dam (ಬಸವ ಸಾಗರ ಜಲಾಶಯ)**: Downstream diversion dam in Yadgir feeding left and right bank canals.

---

## 3. The Cauvery River Basin (ಕಾವೇರಿ ನದೀ ವ್ಯವಸ್ಥೆ)

Known as the *Dakshina Ganga* (Ganges of the South), the Cauvery is the sacred cultural lifeline of southern Karnataka, draining 34,273 sq km (17.9% of the state's area).

```
The Cauvery River System in Karnataka
├── Origin: Talakaveri (ತಲಕಾವೇರಿ) in Brahmagiri hills (Kodagu district) at 1,341 m elevation.
├── Course: 380 km within Karnataka (out of total 800 km length).
├── Leaves Karnataka: Near Biligundlu gorge, entering Tamil Nadu.
└── Major Tributaries in Karnataka:
    ├── Left-Bank Tributaries:
    │   ├── Harangi (ಹಾರಂಗಿ): Originates in Pushpagiri hills (Harangi Dam near Kushalnagar).
    │   ├── Hemavathi (ಹೇಮಾವತಿ): Originates at Ballalarayanadurga; Gorur Dam in Hassan.
    │   ├── Shimsha (ಶಿಂಶಾ): Originates in Devarayanadurga hills, Tumakuru; Markonahalli Dam.
    │   └── Arkavathi (ಅರ್ಕಾವತಿ): Originates in Nandi Hills; Hesaraghatta & Thippagondanahalli reservoirs.
    └── Right-Bank Tributaries:
        ├── Lakshmanatirtha (ಲಕ್ಷ್ಮಣತೀರ್ಥ): Originates in Brahmagiri; Iruppu Falls.
        ├── Kabini / Kapila (ಕಬಿನಿ): Originates in Wayanad (Kerala); Beechanahalli Dam (HD Kote).
        └── Suvarnavathi (ಸುವರ್ಣಾವತಿ): Joins near T. Narasipura.
```

### 3.1 Sacred Confluences and Islands:
- **Triveni Sangama at T. Narasipura**: Holy confluence of Cauvery, Kapila (Kabini), and mythical underground Spatika Sarovara.
- **Three Sacred River Islands (ದ್ವೀಪಗಳು)**:
  1. *Adi Ranga*: **Srirangapatna** (Mandya district).
  2. *Madhya Ranga*: **Shivanasamudra** (Mandya/Chamarajanagar district).
  3. *Antya Ranga*: **Srirangam** (Tamil Nadu).
- **Shivanasamudra Falls (ಶಿವನಸಮುದ್ರ ಜಲಪಾತ)**: The Cauvery branches around the island of Shivanasamudra and plunges 98 meters in twin spectacular cascades:
  - **Gaganachukki (ಗಗನಚುಕ್ಕಿ)** and **Bharachukki (ಭರಚುಕ್ಕಿ)**.
  - Site of the historic **Shivanasamudra Hydroelectric Station (1902 CE)** built by Dewan Sir K. Seshadri Iyer.

### 3.2 Krishna Raja Sagara Dam (KRS - ಕೃಷ್ಣರಾಜ ಸಾಗರ ಅಣೆಕಟ್ಟು)
- Located at Kannambadi near Srirangapatna, just below the confluence of Cauvery, Hemavathi, and Lakshmanatirtha.
- Conceptualized and designed by **Sir M. Visvesvaraya**; constructed between 1911 and 1932 during the reign of Maharaja Krishnaraja Wodeyar IV.
- Masonry gravity dam built with *Surki* mortar; height of 130 feet; storage capacity of 49.45 TMC; feeds the **Visvesvaraya Canal (VC Canal)** transforming Mandya into the "Sugar Bowl of Karnataka".

---

## 4. West-Flowing Rivers and Hydroelectric Power (ಪಶ್ಚಿಮಕ್ಕೆ ಹರಿಯುವ ನದಿಗಳು)

Though draining only 20% of Karnataka's land area, these rivers receive the heaviest rainfall in peninsular India (>3,500-5,000 mm) along the Western Ghats crestline, generating over **60% of Karnataka's total hydroelectric power**.

```mermaid
flowchart TD
    WEST_RIVERS["West-Flowing Rivers of Karnataka"]
    WEST_RIVERS --> SHARAVATHI["Sharavathi River (ಶರಾವತಿ)\n• Origin: Ambuthirtha (Thirthahalli, Shivamogga)\n• Jog Falls (253 m / Raja, Roarer, Rocket, Rani)\n• Linganamakki Dam (152 TMC - Main Hydel source)\n• Gerusoppa Dam & Sharavathi Generating Station (1,035 MW)"]
    WEST_RIVERS --> KALI["Kali River (ಕಾಳಿ)\n• Origin: Diggi (Joida taluk, Uttara Kannada)\n• Flows 184 km through Karwar\n• Supa Dam (Massive reservoir)\n• Nagjhari, Kodasalli & Kadra Powerhouses (1,200 MW)"]
    WEST_RIVERS --> NETRAVATI["Netravati & Kumaradhara (ನೇತ್ರಾವತಿ)\n• Origin: Kudremukh & Subrahmanya\n• Confluence at Uppinangadi (Panchalingeshwara)\n• Lifeline of Dakshina Kannada; enters sea at Mangaluru"]
    WEST_RIVERS --> OTHERS["Aghanashini, Gangavali, Varahi\n• Aghanashini: Unchalli Falls (116 m); pristine Ramsar estuary\n• Gangavali / Bedti: Magod Falls (180 m)\n• Varahi: Kunchikal Falls; Varahi underground hydel project"]
```

### Table 4.1: Major West-Flowing Rivers of Karnataka
| River Name | Origin Point | Length (km) | Major Waterfalls & Hydroelectric Projects |
|---|---|---|---|
| **Sharavathi (ಶರಾವತಿ)** | Ambuthirtha (Shivamogga) | 128 km | **Jog Falls (253 m)**; Linganamakki Dam, Gerusoppa Dam, Mahatma Gandhi HEP, Sharavathi Valley Project. |
| **Kali (ಕಾಳಿ)** | Diggi village (Uttara Kannada)| 184 km | **Supa Dam**, Nagjhari powerhouse, Kodasalli, Kadra Dams. |
| **Varahi (ವಾರಾಹಿ)** | Hebbagilu (Shivamogga) | 66 km | **Kunchikal Falls (455 m)**; Varahi Underground Hydroelectric Project (460 MW). |
| **Aghanashini (ಅಘನಾಶಿನಿ)** | Shankara Honda (Sirsi) | 121 km | **Unchalli / Lushington Falls (116 m)**; Aghanashini Estuary Ramsar Site. |
| **Gangavali / Bedti** | Dharwad district (Shalmala) | 152 km | **Magod Falls (180 m)**; Sahasralinga riverbed carvings. |
| **Netravati (ನೇತ್ರಾವತಿ)** | Bangrabalige (Chikkamagaluru)| 103 km | Meets Kumaradhara at Uppinangadi; Lifeline of Mangaluru; Yettinahole diversion project. |

---

## 5. Major Waterfalls of Karnataka

| Waterfall | River | District | Height & Distinction |
|---|---|---|---|
| **Kunchikal Falls (ಕುಂಚಿಕಲ್)** | Varahi | Shivamogga | **455 meters (1,493 ft)**; highest tiered waterfall in India (partially submerged by dam). |
| **Jog Falls (ಜೋಗ ಜಲಪಾತ)** | Sharavathi | Shivamogga | **253 meters (830 ft)**; highest untiered vertical plunge waterfall in India; 4 streams: Raja, Roarer, Rocket, Rani. |
| **Magod Falls (ಮಾಗೋಡು)** | Bedti / Gangavali | Uttara Kannada | 180 meters; two-tiered plunge in dense forest. |
| **Shivanasamudra (ಶಿವನಸಮುದ್ರ)**| Cauvery | Mandya/Chamarajanagar| 98 meters; twin cascades Gaganachukki & Bharachukki; first hydel plant in Asia (1902). |
| **Unchalli Falls (ಉಂಚಳ್ಳಿ)** | Aghanashini | Uttara Kannada | 116 meters; discovered in 1845 by British collector J.D. Lushington (Lushington Falls). |
| **Gokak Falls (ಗೋಕಾಕ್)** | Ghataprabha | Belagavi | 53 meters; horseshoe plunge over sandstone gorge; "Niagara of Karnataka". |
| **Iruppu Falls (ಇರುಪ್ಪು)** | Lakshmanatirtha | Kodagu | 52 meters; sacred Shiva pilgrimage in Brahmagiri hills. |
| **Abbey Falls (ಅಬ್ಬಿ ಜಲಪಾತ)** | Cauvery tributary | Kodagu | 21 meters; scenic cascade within coffee and spice plantations near Madikeri. |
| **Hebbe Falls (ಹೆಬ್ಬೆ)** | Bhadra tributary | Chikkamagaluru | 168 meters; twin falls Dodda Hebbe and Chikka Hebbe in Kemmangundi. |

---

## 6. Major Multipurpose Dams and Reservoirs Matrix

| Dam / Project | River | District | Type / Storage | Primary Benefits |
|---|---|---|---|---|
| **Krishna Raja Sagara (KRS)** | Cauvery | Mandya | Masonry / 49.5 TMC | Irrigation (VC Canal: Mandya, Mysuru); drinking water to Bengaluru; hydel. |
| **Almatti Dam (LBS Reservoir)** | Krishna | Bagalkote | Masonry & Earthen / 123 TMC | Upper Krishna Project (UKP); irrigates 6 lakh ha in Bagalkote, Vijayapura; 290 MW power. |
| **Tungabhadra Dam (Pampa Sagara)**| Tungabhadra | Vijayanagara / Ballari| Masonry gravity / 100 TMC | Joint KA-AP project; irrigates 3.6 lakh ha in Ballari, Raichur, Koppal. |
| **Linganamakki Dam** | Sharavathi | Shivamogga | Masonry & Composite / 152 TMC | Largest reservoir by capacity; generates 1,035 MW hydel power. |
| **Supa Dam** | Kali | Uttara Kannada | Concrete gravity / 145 TMC | Primary reservoir for Kalinadi Hydroelectric Project (1,200 MW). |
| **Bhadra Dam (Lakkavalli)** | Bhadra | Chikkamagaluru | Composite / 71 TMC | Irrigates Shivamogga, Davanagere, Channagiri; 39 MW power. |
| **Hemavathi Dam (Gorur)** | Hemavathi | Hassan | Masonry & Earthen / 37 TMC | Irrigates Hassan, Mandya, Tumakuru; drinking water to Tumakuru. |
| **Kabini Dam (Beechanahalli)** | Kabini | Mysuru | Composite / 19.5 TMC | Irrigates Mysuru, Chamarajanagar; critical buffer for Tamil Nadu releases. |
| **Malaprabha Dam (Renukasagar)** | Malaprabha | Belagavi | Masonry gravity / 34 TMC | Irrigates Belagavi, Bagalkote, Dharwad, Gadag. |
| **Hidkal Dam (Raja Lakhamagouda)**| Ghataprabha | Belagavi | Earthen & Masonry / 51 TMC | Irrigates Belagavi, Bagalkote; 32 MW power. |

---

## 7. Interstate Water Disputes and Legal Frameworks

Due to its upper-riparian status in peninsular India, Karnataka is entangled in three major interstate river water sharing disputes:

```mermaid
flowchart TD
    DISPUTES["Interstate Water Disputes of Karnataka"]
    DISPUTES --> CAUVERY["1. Cauvery Dispute (Karnataka vs Tamil Nadu)\n• CWDT 2007 Final Award modified by Supreme Court (Feb 2018)\n• Karnataka Share: 284.75 TMC | TN Share: 404.25 TMC\n• Mandatory annual release to TN: 177.25 TMC at Biligundlu\n• Cauvery Water Management Authority (CWMA) & CWRC oversight\n• Mekedatu Balancing Reservoir Dispute (67 TMC drinking water)"]
    DISPUTES --> KRISHNA["2. Krishna Dispute (Karnataka vs AP / Telangana / Maharashtra)\n• KWDT-I (Bachawat Award 1976): KA allocated 700 TMC\n• KWDT-II (Brijesh Kumar Award 2010): KA allocated 911 TMC\n• Contention: Raising Almatti Dam height from 519.6 m to 524.256 m\n• UKP Stage III implementation pending central gazette notification"]
    DISPUTES --> MAHADAYI["3. Mahadayi Dispute (Karnataka vs Goa vs Maharashtra)\n• MWDT Award (August 2018): Karnataka allocated 13.42 TMC\n• Kalasa-Banduri Nala Project: 3.9 TMC drinking water diversion\n• Diverts surplus to Malaprabha basin for Hubballi-Dharwad & Belagavi"]
```

### 7.1 The Cauvery Water Dispute (ಕಾವೇರಿ ವಿವಾದ)
- **Historical Origin**: Rooted in the 1892 and **1924 Agreements** between the Princely State of Mysore and Madras Presidency, which heavily restricted Mysore's dam-building rights.
- **The 2018 Supreme Court Verdict**:
  - On 16 February 2018, a 3-judge bench headed by CJI Dipak Misra delivered the final verdict:
  - Affirmed that **interstate rivers are national assets** and no single riparian state can claim exclusive ownership.
  - Reduced Tamil Nadu's allocation from the 2007 Tribunal award by 14.75 TMC, reallocating it to Karnataka to fulfill the drinking water needs of Bengaluru.
  - Final State Allocations:
    - **Tamil Nadu**: 404.25 TMC
    - **Karnataka**: 284.75 TMC
    - **Kerala**: 30 TMC
    - **Puducherry**: 7 TMC
    - Environmental Protection & Outflow to Sea: 14 TMC
  - Mandatory annual release: Karnataka must release **177.25 TMC** (instead of 192 TMC) to Tamil Nadu at the interstate gauging station at **Biligundlu**.
  - Established statutory oversight bodies: **Cauvery Water Management Authority (CWMA)** and **Cauvery Water Regulation Committee (CWRC)**.
- **The Mekedatu Balancing Reservoir Project**: Karnataka has proposed a Rs. 9,000-crore multi-purpose balancing reservoir (67 TMC capacity) at Mekedatu in Kanakapura taluk to generate 400 MW of power and supply 4.75 TMC drinking water to Bengaluru; opposed by Tamil Nadu before the Supreme Court and CWMA.

### 7.2 The Mahadayi / Kalasa-Banduri Nala Project (ಮಹದಾಯಿ / ಕಳಸಾ-ಬಂಡೂರಿ)
- Mahadayi (known as Mandovi in Goa) originates in the Western Ghats at Khanapur taluk, Belagavi district.
- **Kalasa-Banduri Drinking Water Project**: Designed to divert **3.9 TMC** of surplus water from the Kalasa and Banduri tributaries into the Malaprabha River to resolve the acute perennial drinking water crisis of **Hubballi-Dharwad, Belagavi, and Gadag**.
- Opposed by Goa on grounds of estuarine salinity and Western Ghats forest disruption.
- In August 2018, the **Mahadayi Water Disputes Tribunal (MWDT)** awarded **13.42 TMC** to Karnataka (3.9 TMC drinking water diversion, 1.5 TMC in-basin consumption, and 8.02 TMC for hydel power). In 2023, the Central Water Commission (CWC) granted technical clearance to Karnataka's revised Detailed Project Report (DPR).

---

## 8. Prelims Traps & Mains Answer Blueprint

### 8.1 Prelims Traps
> [!caution]
> - **Trap 1**: Believing Jog Falls is the highest waterfall in India. *Fact*: **Kunchikal Falls (455 m)** on the Varahi river in Shivamogga is recognized as the highest tiered waterfall. Jog Falls (253 m) is the highest untiered vertical plunge waterfall.
> - **Trap 2**: Confusing the location of Almatti Dam. *Fact*: Almatti Dam is located in **Bagalkote district** on the Krishna River, whereas Narayanapura Dam is in **Yadgir district**.
> - **Trap 3**: Believing the Kalasa-Banduri project diverts Cauvery water. *Fact*: Kalasa-Banduri diverts water from the **Mahadayi River basin into the Malaprabha River (Krishna basin)**.

### 8.2 Mains Model Question & Answer Blueprint
**Question**: *Examine the geographical causes and socio-economic ramifications of the Cauvery water dispute between Karnataka and Tamil Nadu. Evaluate the viability of the Mekedatu balancing reservoir project.* (Marks: 15 / 250 Words)

**Model Answer Outline**:
1. **Introduction (35 words)**:
   - Introduce the Cauvery dispute as peninsular India's most complex riparian conflict, arising from monsoon rainfall variability, asymmetrical catchment geography, and intense agricultural demands in Karnataka and Tamil Nadu.
2. **Body 1: Geographical and Hydrological Drivers (75 words)**:
   - *Monsoon Asymmetry*: Karnataka's upper catchment receives rainfall during the South-West Monsoon (June-Sept), while Tamil Nadu's delta receives rain during the North-East Monsoon (Oct-Dec). During drought years, storage deficits trigger fierce release disputes.
   - *Crop Intensification*: Rapid expansion of summer paddy (*Kuruvai* and *Thaladi*) in the Thanjavur delta alongside sugarcane and urban drinking water demands in Bengaluru.
   - *The 2018 Supreme Court Benchmark*: Reallocated 14.75 TMC to Karnataka for Bengaluru's drinking water, pegging mandatory annual releases at 177.25 TMC at Biligundlu.
3. **Body 2: The Mekedatu Reservoir Evaluation (100 words)**:
   - *Karnataka's Justification*: Designed as a 67 TMC balancing reservoir in Kanakapura to store surplus flood waters during bumper monsoon years (which currently drain unutilized into the sea), ensuring drinking water security for Greater Bengaluru and generating 400 MW green hydel power.
   - *Tamil Nadu's Objections*: Argues that an upstream reservoir will obstruct natural flows, alter lower riparian delta ecology, and reduce inflows during distress years.
   - *Viability & Resolution*: Project is legally situated within Karnataka's sovereign allocation; however, environmental clearance requires mitigating submerged Western Ghats forest land, alongside transparent oversight by CWMA to guarantee distress-sharing formulas.
4. **Conclusion (40 words)**:
   - Conclude that resolving the Cauvery crisis demands moving beyond zero-sum inter-state litigation toward automated real-time reservoir monitoring, micro-irrigation crop diversification in delta zones, and institutionalizing an equitable scientific distress-sharing formula under CWMA.

---

## 9. Sources and Verification
- **Verified On**: 2026-10-13 (Tuesday)
- **Primary Source 1**: Supreme Court of India, *State of Karnataka vs. State of Tamil Nadu & Ors*, Civil Appeal No. 2453 of 2007 (Judgment Dt: 16-02-2018).
- **Primary Source 2**: Water Resources Department (WRD), *Annual Administration Report 2024-2026*, Government of Karnataka.
- **Primary Source 3**: Dr. M.B. Patil, *Geography of Karnataka*, Vidyanidhi Prakashana.
"""
    safe_write(path, content)
    print(f"Created: {path} ({len(content.split())} words)")

if __name__ == "__main__":
    create_note_drainage()
