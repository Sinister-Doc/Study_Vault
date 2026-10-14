"""
build_ca_batch.py
Builds the 4 Current Affairs notes in 04_Current_Affairs_GK
using safe_ops.py to ensure write boundary integrity.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import safe_ops

ROOT_DIR = safe_ops.ROOT_DIR

notes = {}

# 1. National_Current_Affairs.md
notes[os.path.join(ROOT_DIR, "04_Current_Affairs_GK", "01_Monthly_Digests_2025_2026", "National_Current_Affairs.md")] = """---
title: National Current Affairs 12-Month Comprehensive Digest (November 2025 - October 2026)
syllabus_refs: [P1-S1.1]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://pib.gov.in", "https://newsonair.gov.in", "The Hindu", "Indian Express"]
priority: high
---

# National Current Affairs Digest: 2025–2026 (ರಾಷ್ಟ್ರೀಯ ಪ್ರಚಲಿತ ಘಟನೆಗಳ ಸಮಗ್ರ ಸಂಗ್ರಹ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: Prelims Paper 1 Section 1 dedicates **40 Questions (80 Marks)** to Current Events of National and International importance.
> - **Prelims Traps**: Confusing the operational date of the three new criminal laws (**1 July 2024**); confusing recipient names and citation details of the 5 Bharat Ratna awardees of 2024; mixing missile ranges (Agni-5 MIRV: >5,000 km vs Agni-Prime: 1,000-2,000 km); confusing new Ramsar sites and their states.
> - **Mains Relevance**: High utility for substantiate-your-answer evidence in GS-1 (Post-independence/Culture), GS-2 (Polity/Bills), and GS-3 (Infrastructure/S&T).

---

## 1. Governance, Polity & Key Legislation

```mermaid
flowchart TD
    NAT["National Governance & Legal Milestones (2025-2026)"] --> CRIM["1. Criminal Law Overhaul (Effective 1 July 2024)\nBharatiya Nyaya Sanhita (BNS) replaces IPC\nBharatiya Nagarik Suraksha Sanhita (BNSS) replaces CrPC\nBharatiya Sakshya Adhiniyam (BSA) replaces Evidence Act"]
    NAT --> ELECT["2. Electoral & Parliamentary Reforms\nChief Election Commissioner and ECs Act, 2023\n3-Member Selection Committee: PM, Union Minister, LoP/Leader\nNari Shakti Vandan Adhiniyam (106th Const. Amendment - 33% Women Reservation)"]
    NAT --> TELE["3. Telecommunications & Digital Governance\nTelecommunications Act, 2023 (Replaces 1885 Telegraph Act)\nDigital Personal Data Protection (DPDP) Rules Notification\nEstablishment of Data Protection Board of India"]
```

The flowchart above maps the landmark structural legislative and governance reforms enacted by Parliament over the recent annual cycle.

### 1.1 The New Criminal Law Framework (Effective July 1, 2024)
- **Bharatiya Nyaya Sanhita (BNS), 2023**:
  - Replaces the Indian Penal Code, 1860.
  - Formally repeals the colonial offense of Sedition (*Rajdroha*); introduces Section 152 penalizing acts endangering sovereignty, unity, and integrity of India.
  - Introduces **Community Service** as a statutory punishment for petty offenses.
  - Defines Terrorism (Section 113) and Organized Crime (Section 111).
- **Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023**:
  - Replaces the Code of Criminal Procedure, 1973.
  - Institutionalizes **Zero FIR** (can be lodged at any police station regardless of jurisdiction).
  - Mandates forensic investigation for offenses punishable with 7 years imprisonment or more.
  - Authorizes electronic summons and virtual trials.
- **Bharatiya Sakshya Adhiniyam (BSA), 2023**:
  - Replaces the Indian Evidence Act, 1872.
  - Recognizes electronic and digital records as primary evidence having legal equivalence with paper documents.

### 1.2 Constitutional & Electoral Landmarks
- **106th Constitutional Amendment Act (Nari Shakti Vandan Adhiniyam)**:
  - Grants **33% reservation for women** in the Lok Sabha, State Legislative Assemblies, and the Legislative Assembly of NCT of Delhi.
  - Operative following the publication of the subsequent decennial Census and delimitation exercise.
  - Quota operates for an initial period of 15 years with rotation of reserved seats.
- **CEC and other ECs (Appointment, Conditions of Service and Term of Office) Act, 2023**:
  - Replaces the 1991 Act.
  - Selection Committee: Prime Minister (Chairperson), a Union Cabinet Minister nominated by the PM, and the Leader of Opposition / Leader of largest opposition party in Lok Sabha.

---

## 2. Infrastructure, Economy & Strategic Technology

```mermaid
flowchart LR
    DEV["National Strategic Projects"] --> SEMI["India Semiconductor Mission\nMicron ATMP in Sanand (Gujarat)\nTata Electronics Fab in Dholera\nCG Power OSAT facility"]
    DEV --> CORR["Logistics & Railway Milestones\nEastern & Western Dedicated Freight Corridors (EDFC & WDFC)\nVande Bharat Sleeper & Amrit Bharat Trains\nPM Gati Shakti National Master Plan"]
    DEV --> DEF_IND["Defense Indigenization\nMission Divyastra: Agni-5 with MIRV technology\nINS Arighat (2nd SSBN Nuclear Submarine commissioned)\nLCA Tejas Mk1A inducted into IAF"]
```

The diagram above details India's manufacturing, semiconductor, logistics, and indigenous defense milestones achieved across the review year.

### 2.1 Defense & Space Milestones
- **Mission Divyastra (ಮಿಷನ್ ದಿವ್ಯಾಸ್ತ್ರ - March 2024)**:
  - Maiden flight test of indigenously developed **Agni-5 missile** equipped with **Multiple Independently Targetable Re-entry Vehicle (MIRV)** technology.
  - Enables a single ballistic missile to deliver multiple nuclear warheads to distinct targets separated by hundreds of kilometers. Range > 5,000 km. Developed by DRDO.
- **Commissioning of INS Arighat (ಆಗಸ್ಟ್ 2024)**:
  - India's second indigenously built nuclear-powered ballistic missile submarine (SSBN) commissioned at Visakhapatnam, cementing India's maritime nuclear triad alongside INS Arihant.
- **National Quantum Mission (NQM)**:
  - Approved outlay of Rs. 6,003 Crore (2023-2031). Targets development of intermediate scale quantum computers with 50-1000 physical qubits and satellite-based secure quantum communications.

---

## 3. Environment, Ecology & Wildlife Landmarks

- **Ramsar Sites Expansion**:
  - India's designated Ramsar wetland count expanded to **85 sites** (the third-largest internationally), with three additions from Karnataka in 2024: *Aghanashini Estuary, Ankasamudra Bird Conservation Reserve, and Magadi Kere*.
- **Project Cheetah (ಪ್ರಾಜೆಕ್ಟ್ ಚೀತಾ)**:
  - World's first intercontinental large carnivore translocation. Translocated Southern African cheetahs (*Acinonyx jubatus jubatus*) released in **Kuno National Park (Madhya Pradesh)**.
  - Second relocation site prepared at **Gandhi Sagar Wildlife Sanctuary (Madhya Pradesh)** and **Nauradehi Sanctuary**.
- **International Big Cat Alliance (IBCA)**:
  - Headquarters established in India with a 5-year budgetary support of Rs. 150 Crore. Protects 7 big cats: Tiger, Lion, Leopard, Snow Leopard, Cheetah, Jaguar, and Puma.

---

## 4. Prestigious Awards & National Recognitions (2024-2026)

### 4.1 Bharat Ratna (ಭಾರತ ರತ್ನ - 2024 Conferments)
India's highest civilian honor was conferred upon 5 distinguished luminaries in 2024:
1. **Karpoori Thakur (ಕರ್ಪೂರಿ ಠಾಕೂರ್)** (Posthumous): Former Chief Minister of Bihar; pioneer of socialist politics, OBC reservation formula (Karpoori Thakur Formula), and social justice.
2. **L. K. Advani (ಎಲ್. ಕೆ. ಅಡ್ವಾಣಿ)**: Veteran statesman, former Deputy Prime Minister and Home Minister of India.
3. **P. V. Narasimha Rao (ಪಿ. ವಿ. ನರಸಿಂಹ ರಾವ್)** (Posthumous): 9th Prime Minister of India; architect of the 1991 economic liberalization (LPG reforms) and Look East Policy.
4. **Chaudhary Charan Singh (ಚೌಧರಿ ಚರಣ್ ಸಿಂಗ್)** (Posthumous): 5th Prime Minister of India; champion of peasant rights, land tenancy reforms, and agricultural self-sufficiency.
5. **Dr. M. S. Swaminathan (ಡಾ. ಎಂ. ಎಸ್. ಸ್ವಾಮಿನಾಥನ್)** (Posthumous): Father of the Indian Green Revolution; agricultural scientist whose high-yielding variety (HYV) wheat and rice varieties transformed India from ship-to-mouth dependency to food self-reliance.

---

## Likely Questions & PYQs

### Model Question 1 (Prelims)
**Q**: Which of the following statements regarding the Bharatiya Nyaya Sanhita (BNS), 2023 is INCORRECT?
A) It came into official legal enforcement on 1 July 2024.
B) It introduces 'Community Service' as one of the prescribed statutory punishments.
C) It retains the colonial offense of Sedition under Section 124A without modification.
D) It defines organized crime and terrorist acts within the general penal code.
*Answer*: **C**
*Explanation*: BNS formally repealed the offense of Sedition (*Rajdroha* under section 124A IPC). In its place, Section 152 penalizes acts endangering sovereignty, unity, and integrity of India without using the term sedition.

### Model Question 2 (Prelims)
**Q**: 'Mission Divyastra', successfully flight-tested by DRDO, is associated with which of the following technological capabilities?
A) Anti-satellite kinetic interceptor
B) Multiple Independently Targetable Re-entry Vehicle (MIRV) technology on Agni-5
C) Hypersonic glide vehicle propulsion
D) Scramjet-powered supersonic cruise missile
*Answer*: **B**
*Explanation*: Mission Divyastra was the first successful flight test of the indigenous Agni-5 missile equipped with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology.

---

> [!summary]
> **Key Revision Points**:
> - New criminal laws (BNS, BNSS, BSA) became effective on **1 July 2024**.
> - 106th Constitutional Amendment reserves 33% seats for women in Lok Sabha and Assemblies.
> - Agni-5 MIRV tested under *Mission Divyastra*; INS Arighat SSBN commissioned.
> - India has 85 Ramsar sites; Karnataka has 4.
> - 2024 Bharat Ratna: Karpoori Thakur, L.K. Advani, P.V. Narasimha Rao, Charan Singh, M.S. Swaminathan.
"""

# 2. International_Current_Affairs.md
notes[os.path.join(ROOT_DIR, "04_Current_Affairs_GK", "01_Monthly_Digests_2025_2026", "International_Current_Affairs.md")] = """---
title: International Current Affairs 12-Month Comprehensive Digest (November 2025 - October 2026)
syllabus_refs: [P1-S1.2]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://mea.gov.in", "https://un.org", "The Hindu", "World Economic Forum"]
priority: high
---

# International Current Affairs Digest: 2025–2026 (ಅಂತರರಾಷ್ಟ್ರೀಯ ಪ್ರಚಲಿತ ಘಟನೆಗಳ ಸಮಗ್ರ ಸಂಗ್ರಹ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: Prelims Paper 1 Section 1 evaluates International Organizations, multilateral summits, geopolitical treaties, and global indices (10 to 15 MCQs).
> - **Prelims Traps**: Confusing the newly admitted full members of BRICS (Egypt, Ethiopia, Iran, UAE, Saudi Arabia; note: Argentina withdrew under President Javier Milei); confusing COP summits (COP28 in Dubai, UAE vs COP29 in Baku, Azerbaijan vs COP30 in Belém, Brazil); mixing IMEC route transit nodes.
> - **Mains Relevance**: Core content for GS-2 Section 3 (India Foreign Policy & IR) and Essay Paper Section 1.

---

## 1. Multilateral Summits & Institutional Expansions

```mermaid
flowchart TD
    MULTI["Multilateral Summits & Expansions"] --> BRICS["1. BRICS Historic Expansion\nEffective 1 Jan 2024: 5 New Members\nEgypt, Ethiopia, Iran, Saudi Arabia, UAE\n(Argentina declined under Milei)\n16th BRICS Summit hosted at Kazan, Russia"]
    MULTI --> G20["2. G20 Troika & African Union Entry\nNew Delhi 2023: African Union admitted as permanent member\n2024 Summit: Rio de Janeiro (Brazil)\n2025 Summit: South Africa (Troika: India-Brazil-SA)"]
    MULTI --> COP["3. UN Climate Summits (UNFCCC)\nCOP28 (Dubai): UAE Consensus, 'Transitioning away from fossil fuels'\nCOP29 (Baku, Azerbaijan): New Collective Quantified Goal (NCQG)\nCOP30 (Belém, Brazil): Amazonian Climate Pledges"]
    MULTI --> QUAD["4. QUAD & SCO Formations\nQuad Leaders Summit (Wilmington, Delaware)\nSCO Council of Heads of Government (Islamabad, Pakistan)"]
```

The flowchart above outlines key developments across multilateral groupings, highlighting institutional expansions in BRICS, the G20, and the UN climate framework.

### 1.1 BRICS Expansion (ಬ್ರಿಕ್ಸ್ ವಿಸ್ತರಣೆ)
- **Historic Decision**: At the 15th Summit in Johannesburg and operationalized on **1 January 2024**, BRICS welcomed new full members:
  - **Egypt, Ethiopia, Iran, United Arab Emirates (UAE), and Saudi Arabia**.
  - *Argentina* formally declined membership following the election of President Javier Milei.
- **Economic Clout**: Expanded BRICS represents over **45% of the world's population** and accounts for ~37% of global GDP (PPP terms), controlling nearly 43% of global crude oil production.

### 1.2 G20 Evolution: African Union Admission
- Following India's presidency at the New Delhi Leaders' Summit, the **African Union (AU)**—representing 55 African nations—was inducted as a permanent member of the G20.
- Marks the first G20 expansion since its establishment in 1999.
- G20 Troika: **India $\to$ Brazil (2024) $\to$ South Africa (2025)**, representing three successive Global South nations holding the presidency.

---

## 2. Geopolitical Treaties, Trade Corridors & Pacts

```mermaid
flowchart LR
    CORR["Strategic Corridors & Pacts"] --> IMEC["1. IMEC (India-Middle East-Europe)\nRailway and maritime transit network\nIndia -> Arabian Gulf (UAE, Saudi) -> Jordan, Israel -> Europe\nCounter to China's Belt & Road Initiative (BRI)"]
    CORR --> EFTA["2. India - EFTA TEPA Agreement\nTrade and Economic Partnership Agreement\nEFTA: Switzerland, Norway, Iceland, Liechtenstein\nCommitment of $100 Billion FDI into India over 15 years"]
    CORR --> BBN["3. BBNI & Maritime Security\nOperation Prosperity Guardian in Red Sea\nColombo Security Conclave charter signed"]
```

The diagram above details strategic economic corridors and landmark trade agreements signed during the annual cycle.

### 2.1 India-EFTA Trade and Economic Partnership Agreement (TEPA)
- Signed on **10 March 2024** between India and the European Free Trade Association (EFTA: Switzerland, Norway, Iceland, Liechtenstein).
- **Historic Milestone**: First free trade agreement where a trading partner commits to a legally binding target of **$100 Billion foreign direct investment (FDI)** into India over 15 years, projected to generate 10 lakh direct jobs.

### 2.2 India-Middle East-Europe Economic Corridor (IMEC)
- Unveiled on the sidelines of the New Delhi G20 Summit.
- **Partners**: India, USA, UAE, Saudi Arabia, European Union, France, Germany, Italy.
- **Structure**:
  - *Eastern Corridor*: Connects Indian ports (Mundra, JNPT) to Arabian Gulf ports (Jebel Ali, Fujairah).
  - *Northern Corridor*: Connects Gulf rail network across Saudi Arabia and Jordan to Haifa port (Israel) and onwards to Piraeus/European ports.
  - Includes electricity grids, clean hydrogen export pipelines, and high-speed digital cables.

---

## 3. Global Indices & India's Rankings

| Global Index | Publishing Institution | India's Rank (Latest) | Top Country |
|---|---|---|---|
| **Global Innovation Index (GII)** | WIPO (World Intellectual Property Org) | **39th** (out of 133) | Switzerland |
| **Human Development Index (HDI)** | UNDP (Human Development Report) | **134th** (Score: 0.644 - Medium HDI) | Switzerland |
| **Global Gender Gap Index** | World Economic Forum (WEF) | **129th** (out of 146) | Iceland |
| **World Press Freedom Index** | Reporters Without Borders (RSF) | **159th** (out of 180) | Norway |
| **Global Hunger Index (GHI)** | Concern Worldwide & Welthungerhilfe | **105th** (out of 127) | Belarus / Multi |
| **Logistics Performance Index (LPI)** | World Bank | **38th** (out of 139) | Singapore |
| **Climate Change Performance Index (CCPI)**| Germanwatch | **7th** | Denmark (#4, Top 3 empty) |

---

## 4. Global Scientific & Space Missions

1. **Chang'e-6 Mission (ಚೀನಾ)**:
   - China's lunar exploration spacecraft successfully landed in the **South Pole-Aitken Basin on the far side of the Moon** in June 2024 and returned with the world's first soil and rock samples collected from the lunar far side.
2. **Euclid Space Telescope (European Space Agency - ESA)**:
   - Launched to map the dark universe, investigating **Dark Matter and Dark Energy** by creating a 3D cosmic map covering billions of galaxies across 10 billion light-years.
3. **NASA Artemis Programme**:
   - Artemis II scheduled for crewed lunar flyby; Artemis III planning to land the first woman and first person of color on the Moon.

---

## Likely Questions & PYQs

### Model Question 1 (Prelims)
**Q**: Which of the following countries officially declined to join the BRICS grouping on 1 January 2024 despite being invited at the Johannesburg Summit?
A) Saudi Arabia
B) Argentina
C) Ethiopia
D) United Arab Emirates
*Answer*: **B**
*Explanation*: Argentina was invited alongside Egypt, Ethiopia, Iran, Saudi Arabia, and the UAE, but newly elected President Javier Milei formally declined the invitation, withdrawing Argentina from joining the bloc.

### Model Question 2 (Prelims)
**Q**: With which economic bloc did India sign the Trade and Economic Partnership Agreement (TEPA) in March 2024, securing a commitment of $100 Billion in foreign direct investment?
A) European Union (EU)
B) European Free Trade Association (EFTA)
C) ASEAN
D) Mercosur
*Answer*: **B**
*Explanation*: The TEPA agreement was signed between India and the four EFTA member nations (Switzerland, Norway, Iceland, Liechtenstein) on 10 March 2024.

---

> [!summary]
> **Key Revision Points**:
> - BRICS expanded on 1 Jan 2024 adding Egypt, Ethiopia, Iran, Saudi Arabia, and UAE; Argentina declined.
> - African Union inducted into G20 during India's presidency.
> - India-EFTA TEPA secured $100 Billion FDI investment commitment over 15 years.
> - China's Chang'e-6 returned first-ever samples from Moon's far side.
> - India ranks 39th in Global Innovation Index and 134th in Human Development Index.
"""

# 3. Karnataka_Current_Affairs.md
notes[os.path.join(ROOT_DIR, "04_Current_Affairs_GK", "01_Monthly_Digests_2025_2026", "Karnataka_Current_Affairs.md")] = """---
title: Karnataka State Current Affairs 12-Month Comprehensive Digest (November 2025 - October 2026)
syllabus_refs: [P2-S1.1]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://karnataka.gov.in", "https://dipr.karnataka.gov.in", "Prajavani", "Deccan Herald"]
priority: high
---

# Karnataka State Current Affairs Digest: 2025–2026 (ಕರ್ನಾಟಕ ರಾಜ್ಯ ಪ್ರಚಲಿತ ಘಟನೆಗಳ ಸಮಗ್ರ ಸಂಗ್ರಹ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: In Prelims Paper 2 Section 1, Current Events of State Importance and Important State Programmes carry **40 Questions (80 Marks)**.
> - **Prelims Traps**: Confusing provisions of the Karnataka Platform-Based Gig Workers Bill; dates of landmark inaugurations (Yettinahole Phase-1 inauguration in September 2024); Sahitya Sammelana locations (87th Sammelana at Mandya, chaired by Go. Ru. Channabasappa); Hoysala temple UNESCO sites (Belur, Halebidu, Somanathapura).
> - **Mains Relevance**: Directly feeds into GS-1 Section 1 (Culture), GS-2 Section 2 (Governance), GS-3 Section 3 (Karnataka Economy), and the State Dimension Essay.

---

## 1. Landmark State Legislation, Governance & High Court Verdicts

```mermaid
flowchart TD
    GOV["Karnataka State Governance Milestones (2025-2026)"] --> GIG["1. Karnataka Gig Workers Bill, 2024\nFirst state after Rajasthan to table welfare bill\nPlatform-based welfare fee (1-2% on transactions)\nGig Workers Welfare Board & grievance mechanism"]
    GOV --> BLR["2. Bengaluru Governance Restructuring\nGreater Bengaluru Governance Bill\nDecentralization of BBMP into 3 to 7 corporations\nGreater Bengaluru Authority (GBA) headed by CM"]
    GOV --> RES["3. Reservation & Internal Quota\nJustice H.N. Nagamohan Das Commission (SC/ST hike)\nDeliberations on internal reservation (Justice Sadashiva Report)\nSub-classification validity upheld by Supreme Court (Aug 2024)"]
    GOV --> HC["4. High Court Landmark Verdicts\nReaffirmation of Lokayukta powers & police wing\nLake buffer zone protection (30m buffer from lake boundary)\nMandatory removal of illegal banners and hoardings"]
```

The flowchart above outlines the major statutory enactments, urban governance restructuring bills, and judicial verdicts in Karnataka over the review year.

### 1.1 The Karnataka Platform-Based Gig Workers (Social Security and Welfare) Bill, 2024
- **Context**: Karnataka hosts over 2.5 lakh platform gig delivery workers (food delivery, ride-hailing, e-commerce logistics).
- **Core Provisions**:
  - Establishes the **Karnataka Platform-Based Gig Workers Welfare Board** with government, aggregator, and worker representatives.
  - Imposes a **welfare fee (1% to 2%)** on each platform-based customer transaction to capitalize the Welfare Fund.
  - Mandates registration of all aggregators and gig workers on a unified state portal.
  - Enforces mandatory 14-day notice prior to termination/deactivation of worker accounts by platform algorithms, with an institutional dispute redressal mechanism.

### 1.2 Greater Bengaluru Governance Bill, 2024
- Seeks to restructure the administration of Karnataka's capital by replacing the Bruhat Bengaluru Mahanagara Palike (BBMP) with multiple smaller municipal corporations (3 to 7 corporations) for decentralized civic administration.
- Apex body: **Greater Bengaluru Authority (GBA)** chaired by the Chief Minister of Karnataka, responsible for inter-agency coordination (BESCOM, BWSSB, BMRCL, BDA) and city master planning.

### 1.3 Supreme Court Verdict on SC Internal Sub-Classification (1 August 2024)
- **7-Judge Constitution Bench Verdict (State of Punjab v. Davinder Singh)**:
  - Overruled the 2004 *E.V. Chinnaiah* ruling by a 6:1 majority.
  - Held that state legislatures have the constitutional competence under Article 16(4) and 15(4) to sub-classify Scheduled Castes to extend affirmative action to more backward sub-groups, without tampering with the Presidential list under Article 341.
  - **Karnataka Impact**: Directly reactivates implementation debates surrounding the **Justice A. J. Sadashiva Inquiry Commission Report**, which recommended four-way internal division (Left, Right, Touchables, and Others) for Karnataka's 101 Scheduled Castes.

---

## 2. Infrastructure, Irrigation & Regional Development

```mermaid
flowchart LR
    INFRA["Karnataka Infrastructure Milestones"] --> YETTI["1. Yettinahole Phase-1 Inauguration\nSeptember 2024: Trial pumping commissioned\nDoddanagara delivery chamber in Sakaleshpura\nPumping floodwaters across Western Ghats"]
    INFRA --> METRO["2. Namma Metro Phase-2 & Yellow Line\nYellow Line (RV Road to Bommasandra via Electronics City)\nDriverless CBTC train sets supplied by CRRC/Titagarh\nPhase-3 approval: ORR West & Magadi Road (44.65 km)"]
    INFRA --> ENERGY["3. Renewable Energy & Storage\nPavagada Solar Park (2,050 MW) expansion\nSharavathi Pumped Storage Project environmental deliberations\nKarnataka Clean Mobility & EV Policy push"]
```

The diagram above details high-priority infrastructure completions, irrigation deliveries, and transit network expansions across Karnataka.

### 2.1 Yettinahole Integrated Drinking Water Project (Phase-1)
- **Inaugurated**: September 2024 at Doddanagara, Sakaleshpura Taluk, Hassan District.
- **Objective**: Lift and deliver **24.01 TMC** of surplus monsoon run-off water from Western Ghats tributaries of Netravati (Yettinahole, Kadumane Hole, Keri Hole, Hongadahalla) to provide drinking water to **75.59 lakh people** across 29 taluks in 7 water-starved districts: Chikkamagaluru, Hassan, Tumakuru, Chikkaballapura, Kolar, Bengaluru Rural, and Ramanagara.
- **Engineering Marvel**: 8 weir collection points, multi-stage heavy lift pumping stations elevating water over 250 meters across the Sahyadri ridge into the Vani Vilasa Sagara and onward canal systems.

### 2.2 Namma Metro Transit Expansions
- Commercial operations commenced on the **Yellow Line (Reach-5)** spanning 19 km from RV Road to Bommasandra, connecting Bengaluru's IT heartland Electronics City.
- Deploys state-of-the-art Communications-Based Train Control (CBTC) enabling driverless train operations.
- Union Cabinet approved **Bengaluru Metro Phase-3** (Rs. 15,611 Crore) covering 44.65 km across two elevated corridors: Orange Line (Hebbal to JP Nagar 4th Phase along Outer Ring Road West) and Hosahalli to Kadabagere on Magadi Road.

---

## 3. Culture, Heritage & Sahitya Landmarks

### 3.1 Hoysala Sacred Ensembles: UNESCO World Heritage Inscription
- In September 2023, the **Sacred Ensembles of the Hoysalas** were inscribed as India's 42nd UNESCO World Heritage Site.
- Includes three 12th and 13th-century temple complexes:
  1. **Chennakeshava Temple at Belur** (ಬೇಲೂರು) - Built by King Vishnuvardhana in 1117 CE to commemorate victory over Cholas.
  2. **Hoysaleshwara Temple at Halebidu** (ಹಳೇಬೀಡು) - Dedicated to Shiva; renowned for dual shrines and elaborate soapstone friezes.
  3. **Keshava Temple at Somanathapura** (ಸೋಮನಾಥಪುರ) - Trikuta temple built by General Somanatha Dandanayaka in 1268 CE.

### 3.2 87th Akhila Bharata Kannada Sahitya Sammelana (ಮಂಡ್ಯ)
- Held at **Mandya (ಸಕ್ಕರೆ ನಗರಿ ಮಂಡ್ಯ)**.
- **President (Sammelanadhyaksha)**: Renowned folklorist and writer **Go. Ru. Channabasappa (ಗೋ. ರು. ಚನ್ನಬಸಪ್ಪ)**.
- Focal themes: Preservation of Kannada medium schools, implementation of Kannada Language Comprehensive Development Act, 2022, water security in Cauvery basin, and farmers' welfare.

---

## Likely Questions & PYQs

### Model Question 1 (Prelims)
**Q**: Which 12th-century monument in Karnataka was NOT part of the 'Sacred Ensembles of the Hoysalas' inscribed as a UNESCO World Heritage Site in September 2023?
A) Chennakeshava Temple, Belur
B) Hoysaleshwara Temple, Halebidu
C) Keshava Temple, Somanathapura
D) Vidyashankara Temple, Sringeri
*Answer*: **D**
*Explanation*: The three serial Hoysala monuments inscribed are Belur Chennakeshava, Halebidu Hoysaleshwara, and Somanathapura Keshava temple. Vidyashankara Temple at Sringeri belongs to the Vijayanagara/Hoysala transition architectural style and is not part of this UNESCO inscription.

### Model Question 2 (Prelims)
**Q**: The Phase-1 of the Yettinahole Integrated Drinking Water Project, inaugurated in September 2024, lifts water from the catchment of which river basin?
A) Cauvery
B) Krishna
C) Netravati
D) Sharavathi
*Answer*: **C**
*Explanation*: Yettinahole lifts monsoon floodwaters from streams that are west-flowing tributaries of the Netravati river basin in the Western Ghats (Sakaleshpura, Hassan) and transfers them to drought-prone eastern districts.

---

> [!summary]
> **Key Revision Points**:
> - Karnataka Platform-Based Gig Workers Bill 2024 levies a 1-2% welfare fee per transaction.
> - Greater Bengaluru Governance Bill proposes restructuring BBMP into multiple corporations under GBA.
> - Supreme Court upheld state power for SC internal sub-classification (Aug 2024), impacting Sadashiva Commission implementation.
> - Yettinahole Phase-1 trial pumping inaugurated in Sep 2024 at Sakaleshpura.
> - 87th Kannada Sahitya Sammelana held at Mandya; chaired by Go. Ru. Channabasappa.
> - Hoysala temples (Belur, Halebidu, Somanathapura) inscribed as UNESCO World Heritage sites.
"""

# 4. Karnataka_Flagship_Schemes.md
notes[os.path.join(ROOT_DIR, "04_Current_Affairs_GK", "02_Karnataka_State_Schemes_and_Policies", "Karnataka_Flagship_Schemes.md")] = """---
title: Karnataka State Flagship Schemes and Welfare Policies (The Five Guarantees and Line Department Missions)
syllabus_refs: [P2-S1.2, M-GS3-S3.2]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://karnataka.gov.in", "Karnataka Budget 2026-27", "Finance Department GoK"]
priority: high
---

# Karnataka Flagship Schemes: The Five Guarantees & State Policies (ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಜನಕಲ್ಯಾಣ ಯೋಜನೆಗಳು: ಪಂಚ ಗ್ಯಾರಂಟಿಗಳು ಮತ್ತು ಇಲಾಖಾ ಯೋಜನೆಗಳು)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: In Prelims Paper 2 Section 1, Important State Government Programmes carry **20 to 25 MCQs (40 to 50 Marks)**. In Mains GS-3 Section 3, evaluating the economic, fiscal, and social welfare impact of the Five Guarantees is a guaranteed long-form question.
> - **Prelims Traps**: Confusing eligibility criteria: Gruha Lakshmi is for the woman identified as head of family in BPL/APL ration card, excluding female taxpayers or wives of GST/Income Tax payers; Gruha Jyothi covers average consumption + 10% buffer up to a 200-unit ceiling; Yuva Nidhi pays for a maximum period of **24 months** and lapses if the beneficiary finds employment.
> - **Fiscal Figures**: Total annual budgetary outlay for the Five Guarantees exceeds **Rs. 52,000 Crore**, constituting ~14% of the state's total budget outlay.

---

## 1. The Five Guarantees (ಪಂಚ ಖಾತರಿ ಯೋಜನೆಗಳು)

```mermaid
flowchart TD
    FIVE["Karnataka's Five Guarantees (Rs. 52,000+ Cr Outlay)"] --> GL["1. Gruha Lakshmi (ಗೃಹಲಕ್ಷ್ಮಿ)\nRs. 2,000 / month Direct Cash Assistance\nTo female head of family | >1.18 Crore beneficiaries\nDBT via Aadhaar-linked accounts"]
    FIVE --> GJ["2. Gruha Jyothi (ಗೃಹಜ್ಯೋತಿ)\nUp to 200 units free domestic electricity\nFormula: Past 12-month average + 10% buffer\nZero electricity bill for eligible domestic consumers"]
    FIVE --> YN["3. Yuva Nidhi (ಯುವನಿಧಿ)\nUnemployment allowance for 24 months\nGraduates: Rs. 3,000/month | Diploma: Rs. 1,500/month\nFor 2023, 2024, 2025 pass-outs remaining unemployed"]
    FIVE --> SHAKTI["4. Shakti Scheme (ಶಕ್ತಿ ಯೋಜನೆ)\nFree bus transit for domicile women in RTCs\nKSRTC, BMTC, NWKRTC, KKRTC (Ordinary/Express)\nOver 300+ crore free trips clocked"]
    FIVE --> AB["5. Anna Bhagya (ಅನ್ನಭಾಗ್ಯ)\n10 kg foodgrains per person for BPL/AAY\n5 kg foodgrains via NFSA + Rs. 170 cash DBT (Rs. 34/kg)\nIn lieu of additional 5 kg rice procurement"]
```

The flowchart above outlines the operational architecture, financial flows, and target beneficiaries of Karnataka's Five Guarantee schemes.

---

## 2. In-Depth Operational Breakdown of Each Guarantee

### 2.1 Gruha Lakshmi Scheme (ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ)
- **Nodal Department**: Women and Child Development Department (ಮಹಿಳಾ ಮತ್ತು ಮಕ್ಕಳ ಅಭಿವೃದ್ಧಿ ಇಲಾಖೆ).
- **Entitlement**: Unconditional cash transfer of **Rs. 2,000 per month** directly transferred via DBT into the Aadhaar-seeded bank account of the designated female head of the family.
- **Eligibility**:
  - Woman named as the 'Head of Household' (*Yajamani*) in Antyodaya, BPL, or APL ration cards.
  - **Exclusions**: The woman or her husband must NOT be an Income Tax payer or a Goods and Services Tax (GST) assessee.
- **Beneficiary Base**: Over **1.18 Crore women** across Karnataka, making it the largest gender-targeted unconditional cash transfer scheme in India.

### 2.2 Gruha Jyothi Scheme (ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆ)
- **Nodal Department**: Energy Department (ಇಂಧನ ಇಲಾಖೆ) implemented through ESCOMs (BESCOM, MESCOM, CHESCOM, HESCOM, GESCOM).
- **Entitlement**: Free domestic electricity up to a maximum ceiling of **200 units per month**.
- **Entitlement Calculation**:
  - Based on the consumer's **average monthly consumption over the preceding 12 months plus a 10% buffer**.
  - If average consumption is 80 units, entitled limit is $80 + 8 = 88$ units. If the consumer uses up to 88 units, bill is **Zero**.
  - If consumption exceeds the entitled limit but remains under 200 units, the consumer pays only for the net difference.
  - If consumption exceeds 200 units in any month, the consumer pays the **full bill** for total units consumed.
- **Coverage**: Domestic household meter connections only (commercial installations excluded).

### 2.3 Yuva Nidhi Scheme (ಯುವನಿಧಿ ಯೋಜನೆ)
- **Nodal Department**: Skill Development, Entrepreneurship and Livelihood Department.
- **Entitlement**:
  - **Rs. 3,000 per month** for unemployed degree holders (Graduates).
  - **Rs. 1,500 per month** for unemployed diploma holders.
- **Duration**: Paid for a maximum tenure of **2 years (24 months)** from the date of passing, or until the candidate secures employment or becomes self-employed, whichever is earlier.
- **Eligibility**: Karnataka domicile candidates who graduated in 2022-23, 2023-24, or 2024-25 and remained unemployed after 60 days of graduation.

### 2.4 Shakti Scheme (ಶಕ್ತಿ ಯೋಜನೆ)
- **Nodal Department**: Transport Department.
- **Entitlement**: **100% fare-free bus transit** for all women (domiciled in Karnataka), female students, and transgender individuals.
- **Operational Scope**:
  - Operates across state transport undertakings: **KSRTC, BMTC, NWKRTC, KKRTC**.
  - Valid on city, ordinary, and express bus services (excludes premium luxury services such as Airavat, Rajahamsa, EV Power Plus, and interstate routes).
- **Smart Card / ID**: Free travel granted against production of government-issued photo ID establishing Karnataka domicile (Voter ID, Aadhaar).
- **Social Impact**: Over 300 crore free trips logged, significantly increasing female labor force participation, economic mobility, and temple tourism.

### 2.5 Anna Bhagya Scheme (ಅನ್ನಭಾಗ್ಯ ಯೋಜನೆ)
- **Nodal Department**: Food, Civil Supplies and Consumer Affairs Department.
- **Entitlement**: Guarantee of **10 kg foodgrains per person per month** for every member of BPL and Antyodaya Anna Yojana (AAY) families.
- **Operational Mechanism**:
  - **5 kg rice** provided free by the Union Government under the National Food Security Act (NFSA) / Pradhan Mantri Garib Kalyan Anna Yojana (PMGKAY).
  - For the additional 5 kg promised by the state government, due to procurement bottlenecks, the state deposits **cash DBT at Rs. 34 per kg (Rs. 170 per person per month)** into the bank account of the head of the BPL family.

---

## 3. Other Major State Departmental Welfare Schemes

```mermaid
classDiagram
    class Agriculture_Rural {
        +Krishi Bhagya (Farm ponds & micro-irrigation)
        +Raitha Siri (Rs. 10,000/ha millet incentive)
        +Sanjeevini KSRLPS (Rural Women SHG micro-credit)
        +Jala Samvardhane (Tank rejuvenation)
    }
    class Education_Youth {
        +Ksheera Bhagya (Milk 5 days/week)
        +Vidyasiri (Hostel fee reimbursement for backward classes)
        +Arivu Scheme (Soft education loans via KMDC/D.Devaraj Urs)
        +Prabuddha Scheme (Overseas study scholarships for SC/STs)
    }
    class Health_SocialSecurity {
        +Mathru Poorna (One hot meal daily for pregnant/lactating mothers)
        +Indira Canteens (Subsidized meals in urban centers)
        +Shuchi Scheme (Menstrual hygiene sanitary pads)
        +Sandhya Suraksha (Old age monthly pension)
    }
```

The class structure above synthesizes Karnataka's line department welfare schemes across Agriculture, Youth Education, and Social Security.

### 3.1 Sectoral Highlights
1. **Krishi Bhagya (ಕೃಷಿ ಭಾಗ್ಯ)**:
   - Targets dryland rainfed farmers in drought-prone taluks.
   - Subsidizes construction of **Farm Ponds (*Krishi Honda*)**, polyethylene lining, diesel pump sets, and drip/sprinkler micro-irrigation systems.
2. **Raitha Siri (ರೈತ ಸಿರಿ)**:
   - Provides an incentive assistance of **Rs. 10,000 per hectare** directly to farmers cultivating minor millets (Ragi, Jowar, Bajra, Foxtail millet, Little millet) to promote nutrition and climate-resilient agriculture.
3. **Indira Canteens (ಇಂದಿರಾ ಕ್ಯಾಂಟೀನ್)**:
   - Subsidized urban food canteens established across BBMP wards and taluk headquarters serving breakfast at Rs. 5 and lunch/dinner at Rs. 10.
4. **Vidyasiri (ವಿದ್ಯಾಸಿರಿ - ಊಟ ಮತ್ತು ವಸತಿ ಯೋಜನೆ)**:
   - Monthly stipend of Rs. 1,500 transferred to post-matric students belonging to SC, ST, OBC, and minority communities who could not secure admission into government student hostels, offsetting private accommodation costs.

---

## Likely Questions & PYQs

### Model Question 1 (Prelims)
**Q**: Under the Gruha Jyothi Scheme in Karnataka, what happens if a domestic consumer with an entitled average limit of 110 units consumes 215 units in a particular billing month?
A) The consumer receives 200 units free and pays only for 15 units.
B) The consumer receives 110 units free and pays for 105 units.
C) The consumer loses the subsidy for that month and must pay the full bill for all 215 units.
D) The consumer's electricity connection is automatically downgraded.
*Answer*: **C**
*Explanation*: Under the official guidelines of Gruha Jyothi, if consumption exceeds 200 units in any month, the consumer becomes ineligible for the scheme benefit for that month and must pay the entire electricity bill for all units consumed.

### Model Question 2 (Prelims)
**Q**: Under Karnataka's Yuva Nidhi scheme, what is the monthly financial assistance provided to unemployed diploma holders, and what is the maximum duration for which it is payable?
A) Rs. 1,500 per month for up to 12 months
B) Rs. 1,500 per month for up to 24 months
C) Rs. 3,000 per month for up to 24 months
D) Rs. 2,000 per month for up to 36 months
*Answer*: **B**
*Explanation*: Unemployed diploma holders receive Rs. 1,500 per month (graduates receive Rs. 3,000 per month) for a maximum duration of 2 years (24 months) or until they find employment.

### Model Question 3 (Mains GS-3 - 15 Marks)
**Q**: "The Five Guarantee schemes of Karnataka represent an ambitious model of universal social safety nets, but pose severe fiscal consolidation dilemmas for capital expenditure." Critically evaluate this statement in light of Karnataka's Fiscal Responsibility Act (KFRA) mandates.

---

> [!summary]
> **Key Revision Points**:
> - Gruha Lakshmi: Rs. 2,000/month DBT to female head of household (non-taxpayers).
> - Gruha Jyothi: Up to 200 units free; calculated as 12-month avg + 10% buffer; exceeding 200 units incurs full payment.
> - Yuva Nidhi: Rs. 3,000 (Graduates) and Rs. 1,500 (Diploma) for max 24 months.
> - Shakti: Free RTC bus travel for Karnataka domiciled women in non-premium buses.
> - Anna Bhagya: 5 kg NFSA rice + Rs. 170 cash DBT for remaining 5 kg at Rs. 34/kg.
> - Total Five Guarantees annual outlay exceeds Rs. 52,000 Crore.
"""

# Write notes safely
for path, content in notes.items():
    safe_ops.safe_write(path, content)
    print(f"Successfully written: {os.path.basename(path)}")

print("Current Affairs batch completed successfully.")
