"""
build_notes_batch1.py
Builds the remaining notes for 06_Science_Technology_Environment
using safe_ops.py to ensure write boundary integrity.
"""

import os
import sys

# Add tools to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import safe_ops

ROOT_DIR = safe_ops.ROOT_DIR

notes = {}

# 1. Environment_Biodiversity_Climate.md
notes[os.path.join(ROOT_DIR, "03_Notes", "06_Science_Technology_Environment", "Environment_Biodiversity_Climate.md")] = """---
title: Environment, Ecology, Biodiversity and Climate Change
syllabus_refs: [P2-S2.1, P2-S2.2]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://moef.gov.in", "https://kspcb.karnataka.gov.in", "https://unfccc.int"]
priority: high
---

# Environment, Ecology, Biodiversity and Climate Change (ಪರಿಸರ, ಪರಿಸರ ವಿಜ್ಞಾನ, ಜೀವವೈವಿಧ್ಯ ಮತ್ತು ಹವಾಮಾನ ಬದಲಾವಣೆ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: High-priority core topic in Prelims Paper 2 Section 2 (10-12 MCQs) and Mains GS-3 Section 2.
> - **Prelims Traps**: Confusing greenhouse gases by GWP (SF6 > HFCs > N2O > CH4 > CO2); mixing Ramsar criteria with UNESCO Natural Heritage criteria; confusing National Ambient Air Quality Standards (NAAQS: 12 pollutants) with Air Quality Index (AQI: 8 pollutants).
> - **Mains Dimensions**: Assessing India's Panchamrit commitments versus development imperatives; evaluating Karnataka State Action Plan on Climate Change (KSAPCC 2.0); analyzing carbon credit trading schemes under the Energy Conservation (Amendment) Act.

---

## 1. Fundamentals of Ecology & Ecosystems

```mermaid
flowchart TD
    ECO["Ecosystem Structure & Dynamics"] --> COMP["1. Ecosystem Components\nBiotic (Producers, Consumers, Decomposers)\nAbiotic (Temperature, Light, Water, Edaphic)"]
    ECO --> FLOW["2. Energy Flow & Trophic Dynamics\n10 Percent Law (Lindeman)\nFood Chains (Grazing vs Detritus)\nEcological Pyramids (Energy always upright)"]
    ECO --> CYCLES["3. Biogeochemical Cycles\nGaseous: Carbon, Nitrogen Cycles\nSedimentary: Phosphorus, Sulphur Cycles"]
    ECO --> SUCC["4. Ecological Succession\nPrimary (Hydrarch / Xerarch) -> Pioneer Species\nSecondary (Faster rate) -> Seral Stages -> Climax"]
```

The diagram above details the operational architecture of ecosystems, illustrating the directional flow of thermodynamic energy, biogeochemical element cycling, and community succession toward ecological equilibrium.

### 1.1 Trophic Dynamics & Ecological Pyramids
- **Lindeman's 10% Energy Efficiency Rule**: Only ~10% of energy stored as biomass in a given trophic level is transferred to the next trophic level; 90% is lost via metabolic respiration and entropy.
- **Pyramids Comparison**:
  - *Pyramid of Numbers*: Upright in grasslands; inverted in single-tree ecosystems supporting hyper-parasites.
  - *Pyramid of Biomass*: Upright in terrestrial forests; **inverted in aquatic / marine ecosystems** (phytoplankton turnover is rapid with minimal instantaneous biomass supporting larger zooplankton).
  - *Pyramid of Energy*: **Always upright without exception**, abiding by the Second Law of Thermodynamics.

### 1.2 Ecological Concepts for KAS
- **Ecotone (ಪರಿಸರ ಪರಿವರ್ತನಾ ವಲಯ)**: Transition zone between two distinct biomes (e.g., mangroves between terrestrial and marine; marshland). Exhibiting the **"Edge Effect" (ಅಂಚಿನ ಪರಿಣಾಮ)** where species density and richness exceed either bordering community.
- **Ecological Niche (ಪರಿಸರ ಗೂಡು)**: The unique functional status, trophic role, and spatial habitat of an organism within its ecological community (defined by Joseph Grinnell and G.E. Hutchinson). Two species cannot indefinitely occupy identical ecological niches (Gause's Competitive Exclusion Principle).
- **Keystone Species (ಪ್ರಮುಖ ಪ್ರಭೇದ)**: Species whose presence and role exert disproportionately large control over community structure relative to their numerical abundance (e.g., Tiger in Bandipur, Ficus trees producing year-round fig fruit in Western Ghats).

---

## 2. Biodiversity & Conservation Paradigms

### 2.1 Biodiversity Levels & Measurement
1. **Genetic Diversity**: Variation of genes within a species (e.g., over 50,000 distinct rice strains in India).
2. **Species Diversity**: Variety of species within a habitat, measured through:
   - *Alpha Diversity*: Species richness within a single homogeneous community.
   - *Beta Diversity*: Degree of species turnover/change between adjacent habitats along an environmental gradient.
   - *Gamma Diversity*: Total landscape or regional species diversity.
3. **Ecosystem Diversity**: Diversity of ecological habitats, biomes, and biological communities across geographical regions.

### 2.2 Conservation Strategies: In-situ vs Ex-situ
| Type | Characteristics | Key Protected Areas in India & Karnataka |
|---|---|---|
| **In-situ Conservation (ಸ್ಥಳೀಯ ಸಂರಕ್ಷಣೆ)** | Protection of genetic resources within natural ecosystems and natural habitats. | **National Parks (5 in Karnataka)**: Bandipur, Nagarhole, Kudremukh, Anshi, Bannerghatta.<br/>**Wildlife Sanctuaries (33 in KA)**: Cauvery, Bhadra, Dandeli, Sharavathi.<br/>**Biosphere Reserves**: Nilgiri Biosphere Reserve (includes Bandipur & Nagarhole).<br/>**Conservation Reserves**: Bankapura Peacock Sanctuary, Hornbill Conservation Reserve. |
| **Ex-situ Conservation (ಪರ-ಸ್ಥಳೀಯ ಸಂರಕ್ಷಣೆ)** | Preservation of components of biological diversity outside their natural habitats. | **Botanical Gardens**: Lalbagh Botanical Garden (Bengaluru).<br/>**Zoological Gardens**: Sri Chamarajendra Zoological Gardens (Mysuru Zoo), Bannerghatta Biological Park.<br/>**Gene & Seed Banks**: National Bureau of Plant Genetic Resources (NBPGR, New Delhi). |

---

## 3. Global Environmental Conventions & Protocols

```mermaid
flowchart LR
    RIO1992["1992 Rio Earth Summit\n(UNCED)"] --> UNFCCC["UNFCCC\n(Climate Change)"]
    RIO1992 --> CBD["CBD\n(Convention on Biological Diversity)"]
    RIO1992 --> UNCCD["UNCCD\n(Desertification & Land Degradation)"]
    UNFCCC --> KYOTO["1997 Kyoto Protocol\n(Clean Dev Mechanism, Carbon Credits)"]
    UNFCCC --> PARIS["2015 Paris Agreement\n(1.5°C Goal, NDCs, Global Stocktake)"]
    CBD --> CARTAGENA["2000 Cartagena Protocol\n(Biosafety & Living Modified Organisms)"]
    CBD --> NAGOYA["2010 Nagoya Protocol\n(Access & Benefit Sharing - ABS)"]
```

The diagram above displays the multilateral treaties originating from the landmark 1992 Rio Earth Summit (Rio Conventions), along with their subsequent protocols governing global climate, biosafety, and equitable genetic resource distribution.

### 3.1 Landmark Treaties
- **Ramsar Convention on Wetlands (1971)**: Intergovernmental treaty for conservation and wise use of wetlands. Karnataka hosts 4 designated Ramsar sites:
  1. *Ranganathittu Bird Sanctuary (ರಂಗನತಿಟ್ಟು)* (Mandya) - Designated 2022.
  2. *Aghanashini Estuary (ಅಘನಾಶಿನಿ)* (Uttara Kannada) - Designated 2024.
  3. *Ankasamudra Bird Conservation Reserve (ಅಂಕಸಮುದ್ರ)* (Vijayanagara) - Designated 2024.
  4. *Magadi Kere Conservation Reserve (ಮಾಗಡಿ ಕೆರೆ)* (Gadag) - Designated 2024.
- **CITES (1973)**: Convention on International Trade in Endangered Species of Wild Fauna and Flora. Classifies species into Appendix I (commercial trade banned), Appendix II, and Appendix III.
- **Basel, Rotterdam & Stockholm Conventions (BRS Triad)**:
  - *Basel*: Transboundary movements of hazardous wastes.
  - *Rotterdam*: Prior Informed Consent (PIC) procedure for certain hazardous chemicals and pesticides in international trade.
  - *Stockholm*: Elimination of Persistent Organic Pollutants (POPs - the "dirty dozen").
- **Montreal Protocol (1987)** & **Kigali Amendment (2016)**: Phasing out ozone-depleting substances (CFCs, HCFCs) and hydrofluorocarbons (HFCs, potent GHGs). World Ozone Day celebrated on **16 September**.

---

## 4. India's Climate Action & Karnataka Initiatives

### 4.1 India's Enhanced Nationally Determined Contributions (NDCs) & Panchamrit (ಪಂಚಾಮೃತ)
At COP26 (Glasgow) and formally submitted to the UNFCCC:
1. Reach non-fossil energy capacity of **500 GW by 2030**.
2. Meet **50% of energy requirements from renewable energy by 2030**.
3. Reduce total projected carbon emissions by **1 billion tonnes by 2030**.
4. Reduce emissions intensity of GDP by **45% by 2030** compared to 2005 levels.
5. Achieve target of **Net-Zero Emissions by 2070**.

### 4.2 Mission LiFE (Lifestyle for Environment - ಪರಿಸರಕ್ಕಾಗಿ ಜೀವನಶೈಲಿ)
- Launched by Prime Minister Narendra Modi at COP26 and operationalized worldwide with UN Secretary-General António Guterres. Focuses on individual and community demand-side interventions across 7 themes: Save Energy, Save Water, Say No to Single-Use Plastic, Adopt Sustainable Food Systems, Reduce Waste, Adopt Healthy Lifestyles, Reduce E-Waste.

### 4.3 Karnataka State Action Plan on Climate Change (KSAPCC 2.0)
- Prepared under the nodal coordination of the **Environmental Management and Policy Research Institute (EMPRI - ಬೆಂಗಳೂರು)**.
- Identifies vulnerability zones:
  - *North Interior Karnataka (ಬೆಳಗಾವಿ, ಕಲಬುರಗಿ, ವಿಜಯಪುರ)*: High vulnerability to drought, extreme heat waves, and rain deficits.
  - *Coastal Karnataka (ಉಡುಪಿ, ದಕ್ಷಿಣ ಕನ್ನಡ, ಉತ್ತರ ಕನ್ನಡ)*: Vulnerable to sea-level rise, coastal erosion, saltwater intrusion into aquifers, and cyclonic storm surges.
  - *Western Ghats (ಮಲೆನಾಡು)*: Vulnerable to slope instability, severe landslides (e.g., Wayanad-Kodagu disaster vulnerabilities), and fragmentation of endemic flora.

---

## 5. Environmental Pollution & Legal Safeguards

### 5.1 Air Quality Standards & Pollutants
- **National Ambient Air Quality Standards (NAAQS)**: Formulated under the Air (Prevention and Control of Pollution) Act, 1981 by CPCB. Monitors **12 pollutants**: PM10, PM2.5, SO2, NO2, CO, NH3, O3, Lead (Pb), Benzene, Benzo(a)pyrene, Arsenic, Nickel.
- **National Air Quality Index (AQI)**: Public health communication metric monitoring **8 pollutants**: PM10, PM2.5, NO2, SO2, CO, O3, NH3, and Pb. Evaluated across 6 categories (Good, Satisfactory, Moderate, Poor, Very Poor, Severe).

### 5.2 Key Environmental Legislation in India
1. **Wildlife (Protection) Act, 1972 (WPA)**: Amended in 2022 to reduce Schedules from 6 to 4 and align with CITES Appendices.
2. **Water (Prevention and Control of Pollution) Act, 1974**: Established Central and State Pollution Control Boards (KSPCB in Karnataka).
3. **Air (Prevention and Control of Pollution) Act, 1981**: Expanded PCB mandates to atmospheric contamination and noise pollution.
4. **Environment (Protection) Act, 1986 (EPA)**: Umbrella legislation enacted under Article 253 of the Constitution in the aftermath of the Bhopal Gas Tragedy (1984). Notified Coastal Regulation Zone (CRZ) rules and Environmental Impact Assessment (EIA).
5. **Biological Diversity Act, 2002**: Three-tier structure:
   - *National Biodiversity Authority (NBA, Chennai)*.
   - *State Biodiversity Boards (Karnataka Biodiversity Board - KBB, Bengaluru)*.
   - *Biodiversity Management Committees (BMCs)* at Panchayat/Urban local body level, preparing **People's Biodiversity Registers (PBRs)**.
6. **National Green Tribunal Act, 2010 (NGT)**: Established judicial body for expeditious disposal of environmental disputes within 6 months. Guided by principles of natural justice and sustainable development.

---

## Likely Questions & PYQs

### Model Question 1 (Prelims)
**Q**: Which one of the following ecological pyramids is NEVER inverted under any circumstances?
A) Pyramid of biomass in a deep lake
B) Pyramid of numbers in a parasitic forest ecosystem
C) Pyramid of energy in an ecosystem
D) Pyramid of biomass in a temperate grassland
*Answer*: **C**
*Explanation*: Energy transfer across trophic levels is governed by the Second Law of Thermodynamics and Lindeman's 10% law. Energy is dissipated as heat at each step; therefore, the pyramid of energy is always strictly upright.

### Model Question 2 (Prelims)
**Q**: Consider the following wetlands in Karnataka:
1. Ranganathittu Bird Sanctuary
2. Aghanashini Estuary
3. Ankasamudra Bird Conservation Reserve
4. Magadi Kere Conservation Reserve
How many of the above are designated Ramsar Sites of International Importance as of 2026?
A) Only one
B) Only two
C) Only three
D) All four
*Answer*: **D**
*Explanation*: All four wetlands are officially designated Ramsar sites. Ranganathittu was declared in 2022; Aghanashini, Ankasamudra, and Magadi Kere were added in 2024, raising Karnataka's total Ramsar sites to four.

### Model Question 3 (Mains GS-3 - 15 Marks)
**Q**: Examine the vulnerability profile of Karnataka across agro-ecological zones to climate change. Critically evaluate the adaptation strategies outlined in the Karnataka State Action Plan on Climate Change (KSAPCC 2.0).

---

> [!summary]
> **Key Revision Points**:
> - Pyramid of energy is always upright; aquatic biomass pyramid is inverted.
> - Ecotone exhibits the Edge Effect; Keystone species maintain disproportionate ecosystem balance.
> - Karnataka has 4 Ramsar sites: Ranganathittu, Aghanashini, Ankasamudra, Magadi Kere.
> - India's COP26 Panchamrit targets: 500 GW non-fossil by 2030, 50% RE by 2030, 45% carbon intensity reduction, Net-Zero by 2070.
> - EMPRI coordinates KSAPCC 2.0; Western Ghats and North Interior Karnataka represent extreme vulnerability hotspots.
"""

# 2. Karnataka_IT_BT_and_Innovation.md
notes[os.path.join(ROOT_DIR, "03_Notes", "06_Science_Technology_Environment", "Karnataka_IT_BT_and_Innovation.md")] = """---
title: Karnataka IT, BT and Innovation Ecosystem (Information Technology, Biotechnology, Startups and Innovation)
syllabus_refs: [P2-S2.1, M-GS3-S1.2]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://karnataka.gov.in", "https://itskarnataka.gov.in", "https://kits.karnataka.gov.in"]
priority: high
---

# Karnataka IT, BT and Innovation Ecosystem (ಕರ್ನಾಟಕದ ಮಾಹಿತಿ ತಂತ್ರಜ್ಞಾನ, ಜೈವಿಕ ತಂತ್ರಜ್ಞಾನ ಮತ್ತು ನಾವೀನ್ಯತಾ ಪರಿಸರ ವ್ಯವಸ್ಥೆ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: High-yield syllabus area in Prelims Paper 2 Section 2 and Mains GS-3 Section 1 (Section 1 Question on Karnataka's Knowledge Economy, Innovation, and Startup Policies).
> - **Prelims Traps**: Confusing state nodal agencies (KITS - Karnataka Innovation and Technology Society vs K-Tech vs KEONICS); misidentifying "Beyond Bengaluru" cluster cities (Hubballi-Dharwad, Mysuru, Mangaluru, Belagavi, Shivamogga, Kalaburagi); confusing venture funding schemes (KITVEN fund vs ELEVATE 100).
> - **Mains Dimensions**: Analyzing Karnataka's competitive advantage in IT/ITeS services and biotechnology; assessing spatial inequality resulting from Bengaluru's primacy and evaluating policy efficacy of "Beyond Bengaluru"; examining intellectual property (IP) creation and deep-tech innovation in the state.

---

## 1. Karnataka: India's Innovation & Tech Capital

```mermaid
flowchart TD
    TECH["Karnataka's Innovation Architecture"] --> IT["1. Information Technology & ITES\nSilicon Valley of Asia | 40% of India's Software Exports\nGlobal Capability Centers (GCCs): 40%+ of India's GCCs\nKEONICS | Electronics City | Whitefield ITPL"]
    TECH --> BT["2. Biotechnology & Life Sciences\nBiotech Capital: ~60% of India's Biotech Revenues\nBioinnovation Centre (IBAB & C-CAMP)\nGenome Valley & Agricultural Biotech"]
    TECH --> STARTUP["3. Startup & Venture Ecosystem\nELEVATE 100 Seed Funding\nUnicorn Capital: ~40 of India's 115+ Unicorns\nK-Tech Innovation Hubs & Incubators"]
    TECH --> REGIONAL["4. Spatial Decentralization\n'Beyond Bengaluru' Policy\nMysuru, Hubballi-Dharwad, Mangaluru Clusters\nESDM Incentives & Hardware Parks"]
```

The diagram above illustrates the multi-dimensional structure of Karnataka's knowledge economy, showcasing its dominant national share across IT exports, biotechnology revenues, startup incubation, and regional dispersion initiatives.

### 1.1 Structural Economic Significance
- **National Leadership**: Karnataka contributes approximately **38% to 40% of India's total software and IT service exports** and is home to over 2 million IT professionals.
- **Biotechnology Primacy**: The state houses over **60% of India's biotechnology companies** and generates more than 50% of the national biotechnology workforce and revenue.
- **Global Capability Centers (GCCs)**: Karnataka hosts over **400 premier Global Capability Centers**, representing leading Fortune 500 corporations in aerospace, fintech, healthcare, and retail analytics.
- **India Innovation Index (NITI Aayog)**: Karnataka has consistently secured the **Rank 1 position among Major States** on the NITI Aayog India Innovation Index, driven by high human capital, research density, VC funding, and patent filings.

---

## 2. Institutional Framework & Nodal Agencies

1. **Department of Electronics, IT, Bt and S&T (ಇ-ಆಡಳಿತ ಮತ್ತು ಐಟಿ-ಬಿಟಿ ಇಲಾಖೆ)**: Administrative department formulating state technology policies.
2. **KITS (Karnataka Innovation and Technology Society)**: Implementing agency executing startup initiatives, biotech infrastructure, and skill development programs.
3. **KEONICS (Karnataka State Electronics Development Corporation Ltd)**: Established in 1976; established **Electronics City (ಇಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಸಿಟಿ)** on Hosur Road in Bengaluru, creating the physical foundation for India's IT revolution.
4. **IBAB (Institute of Bioinformatics and Applied Biotechnology)**: Located at Biotech Park, Electronic City, providing specialized bioinformatics research and industry-ready talent.
5. **C-CAMP (Centre for Cellular and Molecular Platforms)**: An initiative supported by the Department of Biotechnology (Govt of India) and Karnataka Govt, acting as a deep-tech bio-incubator fostering life sciences startups.

---

## 3. Flagship Policy Frameworks

### 3.1 Karnataka IT Policy 2020-2025 & Beyond
- **Strategic Vision**: Transform Karnataka into a global leader in emerging technologies (AI, Robotics, Blockchain, Quantum Computing, IoT) while geographically expanding IT operations outside Bengaluru.
- **Core Targets**:
  - Achieve 30% contribution to India's digital economy target.
  - Create over 60 lakh direct and indirect technology jobs.
  - Decentralize growth by building robust IT ecosystems in Tier-2 and Tier-3 cities.

### 3.2 "Beyond Bengaluru" (ಬಿಯಾಂಡ್ ಬೆಂಗಳೂರು) Initiative
Recognizing the infrastructural stress and traffic congestion of Bengaluru Urban, the Government of Karnataka rolled out the **"Beyond Bengaluru" Policy**:
- **Target Growth Clusters**:
  1. *Mysuru Cluster*: IT, ESDM (Electronics System Design & Manufacturing), cyber security, and clean mobility.
  2. *Hubballi-Dharwad-Belagavi Cluster*: Manufacturing IT, automotive software, agri-tech, and AI-driven precision engineering.
  3. *Mangaluru-Udupi Cluster*: Fintech, health-tech, marine biotechnology, and BPO operations.
  4. *Shivamogga & Kalaburagi Clusters*: Regional IT-BPO centres and local incubation hubs.
- **Fiscal Incentives**:
  - Subsidized lease rentals and land allotment through KIADB.
  - Reimbursement of Employee Provident Fund (EPF) and training costs.
  - Power tariff concessions and stamp duty exemptions.

### 3.3 Karnataka Biotechnology Policy
- Known as the **Bio-Economy Policy**, aiming to elevate Karnataka's bio-economy to $50 Billion.
- Thrust Areas:
  - *Biopharma*: Biosimilars, vaccines, monoclonal antibodies.
  - *Agri-Biotechnology*: Climate-resilient seeds, bio-fertilizers, tissue culture.
  - *Industrial Biotechnology*: Bio-fuels, enzyme engineering, synthetic biology.
  - *Bioinformatics & Genomics*: Next-generation sequencing and personalized medicine.

### 3.4 Karnataka Startup Policy & ELEVATE Program
- **ELEVATE 100 Scheme**: Flagship grant-in-aid startup support mechanism providing up to **Rs. 50 Lakhs** equity-free seed funding for innovative, early-stage startups selected through a competitive pitch process.
- **Special Windows**:
  - *ELEVATE Kalyana Karnataka*: Targeted seed funding reserved for entrepreneurs from the 371J backward region.
  - *ELEVATE Women*: Dedicated funding allocation for women-founded technology enterprises.
  - *KITVEN (Karnataka Information Technology Venture Capital Fund)*: State-sponsored SEBI-registered venture capital fund providing equity investments to startups.

---

## 4. Deep-Tech, AI and Future Frontiers

### 4.1 Centers of Excellence (CoEs)
The Government of Karnataka has established specialized CoEs in partnership with premier industry bodies (NASSCOM, IESA) and academic institutions (IISc):
- **CoE in Artificial Intelligence & Data Science** (Bengaluru).
- **CoE in Internet of Things (IoT)** (Bengaluru).
- **CoE in Cyber Security (CySecK)** (Housed at IISc Bengaluru to secure state digital infrastructure and nurture cybersecurity startups).
- **CoE in Aerospace and Defense** (Focusing on digital twinning, simulation, and defense avionics).
- **CoE in Agri-Innovation** (Focusing on drone sensors, satellite imagery for crop insurance, and precision irrigation).

### 4.2 Semiconductor & ESDM Push
- Karnataka approved the setup of advanced semiconductor assembly, testing, marking, and packaging (ATMP) facilities and design houses.
- Accounts for over **85% of India's chip design talent**, with global semiconductor design giants (Intel, Qualcomm, Texas Instruments, AMD, NVIDIA) operating major R&D campuses in Bengaluru.

---

## Likely Questions & PYQs

### Model Question 1 (Prelims)
**Q**: Which state-sponsored program in Karnataka provides grant-in-aid seed funding of up to Rs. 50 Lakhs to promising early-stage technology startups?
A) Amrutha Surabhi
B) ELEVATE 100
C) Yuva Snehi
D) Udyog Mitra
*Answer*: **B**
*Explanation*: The ELEVATE scheme administered by KITS under the Department of Electronics, IT/BT provides equity-free seed grants of up to Rs. 50 Lakhs for innovative tech startups in Karnataka.

### Model Question 2 (Prelims)
**Q**: Which organization founded Electronics City in Bengaluru in 1976?
A) KIADB
B) KEONICS
C) KINFRA
D) KITS
*Answer*: **B**
*Explanation*: KEONICS (Karnataka State Electronics Development Corporation Ltd), under the leadership of R. K. Baliga, conceived and established Electronics City in 1976, laying the foundation for Bengaluru's IT boom.

### Model Question 3 (Mains GS-3 - 12.5 Marks)
**Q**: "While Bengaluru has cemented its position as the Silicon Valley of India, regional imbalance in technology investments poses serious infrastructural challenges." In this context, analyze the objectives and key strategies of Karnataka's 'Beyond Bengaluru' policy.

---

> [!summary]
> **Key Revision Points**:
> - Karnataka accounts for ~40% of India's IT exports and ~60% of biotech revenues.
> - Consistently ranks #1 in NITI Aayog India Innovation Index (Major States).
> - KEONICS developed Electronics City in 1976 under R.K. Baliga.
> - "Beyond Bengaluru" targets Mysuru, Hubballi-Dharwad, and Mangaluru as growth clusters.
> - ELEVATE provides up to Rs. 50 Lakh seed funding; CySecK CoE is at IISc.
"""

# 3. Karnataka_Biodiversity_and_Western_Ghats.md
notes[os.path.join(ROOT_DIR, "03_Notes", "06_Science_Technology_Environment", "Karnataka_Biodiversity_and_Western_Ghats.md")] = """---
title: Biodiversity of Karnataka and Western Ghats Ecology (Sahyadri, Protected Areas, Forest Cover and Conservation)
syllabus_refs: [P2-S2.2, M-GS3-S2.1]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://aranya.gov.in", "https://wii.gov.in", "https://kspcb.karnataka.gov.in"]
priority: high
---

# Biodiversity of Karnataka and Western Ghats Ecology (ಕರ್ನಾಟಕದ ಜೀವವೈವಿಧ್ಯ ಮತ್ತು ಪಶ್ಚಿಮ ಘಟ್ಟಗಳ ಪರಿಸರ ವಿಜ್ಞಾನ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: One of the most frequently tested areas in both Prelims Paper 2 (8-10 questions on National Parks, Tiger Reserves, Endemism, Ramsar sites) and Mains GS-3 Section 2 (Western Ghats conservation vs development dilemmas).
> - **Prelims Traps**: Confusing Karnataka's 5 National Parks (Bannerghatta is the only one with a biological park/butterfly park; Kudremukh has origin of Tunga, Bhadra, and Netravati); confusing Gadgil Commission (WGEEP - strict 3-tier ESZ) with Kasturirangan Committee (HLWG - 37% natural landscape as ESA); mixing tiger census ranks (Karnataka is 2nd with 563 tigers, just behind MP with 785).
> - **Mains Dimensions**: Analyzing the ecological-economic friction in Western Ghats development; the controversy over Yettinahole river diversion and Sharavathi pumped storage project; community-based forest rights under the Forest Rights Act (FRA 2006) in Malnad.

---

## 1. Western Ghats (ಸಹ್ಯಾದ್ರಿ): Global Biodiversity Hotspot

```mermaid
flowchart TD
    GHATS["Western Ghats (Sahyadri) in Karnataka"] --> BIO["1. Biodiversity Primacy\nUNESCO World Heritage Site (39 sites, 10 in KA)\nGlobal Hotspot (Norman Myers - 1 of 36 globally)\nEndemism: Lion-tailed Macaque, Malabar Pit Viper"]
    GHATS --> RIVERS["2. Water Tower of Peninsular India\nOrigins: Krishna, Cauvery, Tungabhadra, Sharavathi\nHydroelectric Generation: Linganamakki, Supa Dam\nShola Grassland-Forest Complex"]
    GHATS --> PA["3. Protected Area Network\n5 National Parks | 5 Tiger Reserves\nNilgiri Biosphere Reserve (First BR in India 1986)\n4 Ramsar Wetlands"]
    GHATS --> POLICY["4. Ecological Governance Debates\nGadgil Commission (WGEEP, 2011)\nKasturirangan Committee (HLWG, 2013)\nEco-Sensitive Areas (ESA) Notification Disputes"]
```

The diagram above illustrates the ecological importance of Karnataka's Western Ghats, functioning as peninsular India's hydrological lifeline, biodiversity reservoir, and center of conservation policy debates.

### 1.1 Ecological Profile & Endemism
- **Global Hotspot Status**: One of Norman Myers' original biodiversity hotspots, fulfilling two criteria:
  1. Contains at least **1,500 species of vascular plants as endemics** (>0.5% of world's total).
  2. Has lost at least **70% of its primary native vegetation**.
- **UNESCO World Heritage Site**: Inscribed in 2012; Karnataka contains **10 of the 39 serial heritage clusters**, including Pushpagiri, Brahmagiri, Talacauvery, Kudremukh, and Agumbe.
- **Endemic Fauna & Flora**:
  - *Lion-tailed Macaque (ಸಿಂಹಬಾಲದ ಸಿಂಹ)*: Endemic to evergreen rainforests of Western Ghats (Sharavathi Valley, Someshwara).
  - *Nilgiri Tahr (ನೀಲಗಿರಿ ತಹ್ರ್)*: Found in southern fringes bordering Nilgiris.
  - *Malabar Gliding Frog* & *Kottigehar Dancing Frog (Micrixalus kottigeharensis)*: Endemic to Malnad streams.
  - *Shola Ecosystem (ಶೋಲಾ ಅರಣ್ಯಗಳು)*: Stunted tropical montane evergreen forest patches nestled in valleys surrounded by rolling montane grasslands at altitudes above 1,500 meters (Kudremukh, Bababudangiri).

---

## 2. Protected Area Network in Karnataka

Karnataka has **5 National Parks**, **33 Wildlife Sanctuaries**, and **5 Tiger Reserves**.

```mermaid
classDiagram
    class NationalParks {
        +Bandipur (Chamarajanagar)
        +Nagarhole / Rajiv Gandhi (Kodagu-Mysuru)
        +Kudremukh (Chikkamagaluru-Udupi-DK)
        +Anshi / Kali (Uttara Kannada)
        +Bannerghatta (Bengaluru Urban/Rural-Ramanagara)
    }
    class TigerReserves {
        +Bandipur Tiger Reserve (1973 - Project Tiger)
        +Nagarhole Tiger Reserve
        +Bhadra Tiger Reserve (Chikkamagaluru)
        +Kali Tiger Reserve (Anshi-Dandeli)
        +Biligiriranganatha Swamy Temple / BRT (Chamarajanagar)
    }
    class RamsarSites {
        +Ranganathittu Bird Sanctuary (Mandya)
        +Aghanashini Estuary (Uttara Kannada)
        +Ankasamudra Bird Conservation Reserve (Vijayanagara)
        +Magadi Kere Conservation Reserve (Gadag)
    }
```

The class structure above organizes Karnataka's premier conservation estates across National Parks, Project Tiger Reserves, and internationally recognized Ramsar wetland sites.

### 2.1 Detailed Profile of the 5 National Parks
1. **Bandipur National Park (ಬಂಡೀಪುರ)** (Chamarajanagar District):
   - Formed in 1974; part of the Nilgiri Biosphere Reserve.
   - One of India's first Project Tiger reserves (1973).
   - High density of Bengal tigers, Asiatic elephants, and Indian leopards.
2. **Nagarhole National Park / Rajiv Gandhi NP (ನಾಗರಹೊಳೆ)** (Kodagu & Mysuru Districts):
   - Named after the meandering stream *Nagarahole* ('Snake River').
   - Contiguous with Bandipur and Wayanad (Kerala). Renowned for Kabini river reservoir safari and predator density.
3. **Kudremukh National Park (ಕುದುರೆಮುಖ)** (Chikkamagaluru, Udupi, Dakshina Kannada):
   - Named after the distinctive horse-face peak (1,892 m).
   - Major Shola-grassland ecosystem. Origin of three sacred rivers: **Tunga, Bhadra, and Netravati**. Historic landmark Supreme Court verdict ended iron-ore mining by KIOCL inside the park.
4. **Anshi National Park / Kali Tiger Reserve (ಅಣಶಿ / ಕಾಳಿ)** (Uttara Kannada):
   - Evergreen rainforest habitat in the Kali river basin. Home to the rare melanistic leopard (Black Panther) and great Indian hornbill.
5. **Bannerghatta National Park (ಬನ್ನೇರುಘಟ್ಟ)** (Bengaluru Urban/Rural):
   - Located on the periphery of Bengaluru. Contains a biological park, safari, rescue center, and **India's first Butterfly Park** (opened 2006). Crucial elephant corridor connecting BMTP to Hosur forests.

### 2.2 Status of Tigers & Elephants in Karnataka
- **Tiger Population (Status of Tigers in India 2022 Report)**:
  - Karnataka ranks **2nd in India with 563 tigers** (Madhya Pradesh ranks 1st with 785).
  - Bandipur and Nagarhole are among the highest tiger density landscapes globally.
- **Elephant Population**:
  - Karnataka ranks **1st in India** with over **6,000 Asiatic wild elephants**, accounting for ~25% of India's total elephant population.

---

## 3. Western Ghats Conservation Committees: Gadgil vs Kasturirangan

```mermaid
flowchart TD
    DEBATE["Western Ghats Policy Dilemma"] --> GADGIL["Madhav Gadgil Commission (WGEEP, 2011)\n- 100% Western Ghats designated as ESA\n- 3-Tier Zoning: ESZ-1, ESZ-2, ESZ-3\n- Complete ban on mining, dams, polluting industries\n- Grassroots Panchayat democracy (Gram Sabhas)\n- Rejected by all 6 state governments as too radical"]
    DEBATE --> KASTURI["K. Kasturirangan Committee (HLWG, 2013)\n- Pragmatic split: Cultural (63%) vs Natural (37%) Landscape\n- Only Natural Landscape (37% ~59,940 sq km) marked ESA\n- Complete ban on: Mining, Thermal plants, Red-category industries\n- Permits agriculture, plantations, non-polluting activities\n- Still faces local resistance across Malnad districts"]
```

The flowchart above outlines the divergent conservation paradigms between the ecocentric Madhav Gadgil Report and the pragmatic landscape-split Kasturirangan Report.

### Comparative Breakdown:
| Parameter | Madhav Gadgil Report (WGEEP 2011) | K. Kasturirangan Report (HLWG 2013) |
|---|---|---|
| **Coverage** | Entire Western Ghats (~1,29,037 sq km) declared Eco-Sensitive. | Only **37% (Natural Landscape)** (~59,940 sq km) declared ESA. |
| **Zoning** | 3-tier graded zoning: Eco-Sensitive Zone 1, 2, and 3. | Single-tier ESA covering natural forest patches. |
| **Human Inhabitation** | Imposed strict curbs across inhabited villages in ESZ-1. | Excluded **Cultural Landscape (63%)** with human settlements and plantations. |
| **Mining & Quarries** | Indefinite ban in ESZ-1 & ESZ-2; phase-out in 5 years in ESZ-3. | Complete ban on mining, quarrying, and sand mining within ESA. |
| **Hydroelectric Projects** | Banned large storage dams (specifically Athirappilly and Gundia). | Strict case-by-case EIA with 30% ecological flow mandate. |
| **Governance Structure** | Proposed statutory Western Ghats Ecology Authority (WGEA). | Recommended existing monitoring mechanisms under EPA 1986. |

---

## 4. Major Environmental Conflicts & Challenges in Karnataka

1. **Human-Wildlife Conflict (ಮಾನವ-ವನ್ಯಜೀವಿ ಸಂಘರ್ಷ)**: Severe crop raiding and human casualties by elephants in Hassan, Kodagu, and Chikkamagaluru. Response includes elephant proof trenches (EPT), solar fencing, railway barricades, and Rapid Response Teams (Elephant Task Force).
2. **Yettinahole Drinking Water Project (ಎತ್ತಿನಹೊಳೆ ಯೋಜನೆ)**: Diversion of 24 TMC of floodwaters from Netravati tributaries in Sakaleshpura to drought-prone Kolar, Chikkaballapura, and Bengaluru Rural. Criticized by environmentalists for endangering Western Ghats forests and estuarine fisheries in Mangaluru.
3. **Sharavathi Pumped Storage Hydroelectric Project (ಶರಾವತಿ ಪಂಪ್ಡ್ ಸ್ಟೋರೇಜ್)**: Proposed 2,000 MW underground pumped storage within Sharavathi Valley Wildlife Sanctuary; faces environmental opposition due to forest submergence and threat to Lion-tailed Macaque habitat.
4. **Forest Fires & Lantana camara Weed Infestation**: Proliferation of invasive *Lantana camara* and *Senna spectabilis* choking native fodder in Bandipur and Nagarhole.

---

## Likely Questions & PYQs

### Model Question 1 (Prelims)
**Q**: Which of the following rivers originating in the Kudremukh National Park flow into the Arabian Sea?
A) Tunga
B) Bhadra
C) Netravati
D) Hemavathi
*Answer*: **C**
*Explanation*: Three rivers originate at Gangamoola in Kudremukh: Tunga and Bhadra flow east towards the Bay of Bengal, while the Netravati flows west through Dakshina Kannada into the Arabian Sea.

### Model Question 2 (Prelims)
**Q**: What percentage of the Western Ghats was recommended to be declared as Eco-Sensitive Area (ESA) by the High-Level Working Group chaired by Dr. K. Kasturirangan?
A) 100%
B) 63%
C) 37%
D) 25%
*Answer*: **C**
*Explanation*: The Kasturirangan Committee differentiated between Cultural (63%) and Natural Landscapes (37%), recommending that only the 37% Natural Landscape be notified as Eco-Sensitive Area.

### Model Question 3 (Mains GS-3 - 15 Marks)
**Q**: Compare and contrast the recommendations of the Madhav Gadgil and K. Kasturirangan committees regarding Western Ghats conservation. Why have state governments and local communities in Karnataka resisted the notification of Eco-Sensitive Areas?

---

> [!summary]
> **Key Revision Points**:
> - Karnataka has 5 National Parks (Bandipur, Nagarhole, Kudremukh, Anshi, Bannerghatta).
> - Bannerghatta houses India's first butterfly park (2006).
> - Karnataka is #2 in Tigers (563) and #1 in Elephants (>6,000).
> - Gadgil recommended 100% Western Ghats as ESZ; Kasturirangan recommended 37% (natural landscape only).
> - Kudremukh is origin of Tunga, Bhadra (east-flowing) and Netravati (west-flowing).
"""

# 4. Public_Health_and_Sanitation_Karnataka.md
notes[os.path.join(ROOT_DIR, "03_Notes", "06_Science_Technology_Environment", "Public_Health_and_Sanitation_Karnataka.md")] = """---
title: Public Health, Sanitation and Nutrition in Karnataka (Epidemiology, Health Infrastructure, NFHS-5 and Welfare Missions)
syllabus_refs: [P2-S2.2, M-GS3-S2.2]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources: ["https://hfw.karnataka.gov.in", "https://nhm.gov.in", "https://rchiips.org/nfhs"]
priority: high
---

# Public Health, Sanitation and Nutrition in Karnataka (ಕರ್ನಾಟಕದ ಸಾರ್ವಜನಿಕ ಆರೋಗ್ಯ, ನೈರ್ಮಲ್ಯ ಮತ್ತು ಪೌಷ್ಟಿಕಾಂಶ)

> [!exam-focus]
> **Exam Weightage & Testing Patterns**: High-yield syllabus area across Prelims Paper 2 Section 2 and Mains GS-3 Section 2 (Health, Disease Burden & Sanitation).
> - **Prelims Traps**: Confusing vector-borne disease vectors (KFD is tick-borne: *Haemaphysalis spinigera*, not mosquito-borne; Dengue/Chikungunya by *Aedes aegypti*; Malaria by *Anopheles*; Filariasis by *Culex*); confusing health metrics (Karnataka's MMR is 69 per 1 lakh live births, achieving the SDG target <70; IMR is ~19 per 1,000 live births); mixing Mathru Poorna (hot cooked meal for pregnant/lactating women at anganwadis) with Mathru Vandana (cash incentive PMMVY).
> - **Mains Dimensions**: Assessing the regional disparity in health infrastructure between South Karnataka and Kalyana Karnataka; evaluating anemia and malnutrition indicators in NFHS-5; analyzing Universal Health Coverage under Ayushman Bharat - Arogya Karnataka.

---

## 1. Demographic & Public Health Indicators: Karnataka vs National Benchmarks

```mermaid
flowchart LR
    HEALTH["Key Health Milestones (Karnataka)"] --> MMR["1. Maternal Mortality Ratio (MMR)\nKarnataka: 69 per 1,00,000 live births\nSDG Target (<70) achieved ahead of 2030"]
    HEALTH --> IMR["2. Infant Mortality Rate (IMR)\nKarnataka: 19 per 1,000 live births\nNational Average: ~28 per 1,000"]
    HEALTH --> TFR["3. Total Fertility Rate (TFR)\nKarnataka: 1.7 (NFHS-5)\nBelow replacement level (2.1)"]
    HEALTH --> INST["4. Institutional Deliveries\nKarnataka: 99.4% (NFHS-5)\nAlmost universal institutional birth coverage"]
```

The diagram above details Karnataka's demographic performance metrics, showing that the state has surpassed SDG targets in Maternal Mortality Ratio and replacement-level fertility.

### Comparative Indicator Table (NFHS-5 & SRS Data):
| Health / Demographic Indicator | Karnataka Level | All-India Benchmark | SDG Target (2030) |
|---|---|---|---|
| **Maternal Mortality Ratio (MMR)** (per 1,00,000 live births) | **69** | 97 | < 70 |
| **Infant Mortality Rate (IMR)** (per 1,000 live births) | **19** | 28 | <= 12 |
| **Under-Five Mortality Rate (U5MR)** | **21** | 32 | <= 25 |
| **Total Fertility Rate (TFR)** | **1.7** | 2.0 | 2.1 (Replacement) |
| **Sex Ratio at Birth (SRB)** (females per 1000 males) | **916** (SRS) / **978** (NFHS-5) | 907 / 929 | 950+ |
| **Institutional Deliveries** | **99.4%** | 88.6% | 100% |
| **Full Immunization Coverage (12-23 months)** | **84.1%** | 76.4% | 90%+ |

---

## 2. Epidemiology & Disease Burden in Karnataka

### 2.1 Kyasanur Forest Disease (KFD / ಮಂಗನ ಕಾಯಿಲೆ)
- **Nature**: Zoonotic viral hemorrhagic disease caused by Kyasanur Forest Disease virus (Flaviviridae family).
- **History & Geography**: First identified in 1957 in **Kyasanur forest, Shivamogga district**. Endemic across Western Ghats districts (Shivamogga, Uttara Kannada, Chikkamagaluru, Udupi, Kodagu).
- **Transmission Vector**: Hard tick ***Haemaphysalis spinigera***.
- **Hosts & Reservoirs**: Black-faced langurs (*Semnopithecus entellus*) and red-faced bonnet macaques (*Macaca radiata*) are highly susceptible hosts. Death of monkeys serves as an early sentinel indicator of outbreak.
- **Control**: Formalin-inactivated vaccine, vector control using tick repellents (DEP/DEET), and the dedicated **Virus Diagnostic Laboratory (VDL)** at Shivamogga.

### 2.2 Vector-Borne & Communicable Diseases
- **Dengue & Chikungunya**: Transmitted by the day-biting ***Aedes aegypti*** mosquito. Karnataka conducts intense IEC campaigns during monsoon and dry-day observances.
- **Tuberculosis (TB)**: State actively executing National TB Elimination Programme (NTEP) targeting TB elimination. Deployment of CBNAAT/Truenat molecular diagnostic machines in all Taluk hospitals, Nikshay Poshan Yojana direct benefit transfers (Rs. 500/month nutritional support), and community Ni-kshay Mitras.
- **Non-Communicable Diseases (NCDs)**: Shift towards chronic lifestyle disorders (Hypertension, Diabetes Mellitus, Cardiovascular diseases, Cervical and Breast Cancer). Screened at Primary Health Centers (PHCs) via the **Comprehensive Primary Health Care (CPHC) - NCD portal**.

---

## 3. Nutrition & Malnutrition Profile (NFHS-5 Analysis)

Despite impressive economic growth, child and maternal nutritional indicators reveal significant challenges, particularly in Northern Karnataka:
- **Child Nutritional Deficits (Under 5 years)**:
  - *Stunting (ಕುಬ್ಜತೆ - Low height-for-age)*: **35.4%** in Karnataka (indicates chronic undernutrition).
  - *Wasting (ತೆಳ್ಳಗಾಗುವುದು - Low weight-for-height)*: **19.5%** (indicates acute malnutrition).
  - *Severely Wasted*: **7.2%**.
  - *Underweight (ಕಡಿಮೆ ತೂಕ - Low weight-for-age)*: **32.9%**.
- **Anemia Burden (ರಕ್ತಹೀನತೆ)**:
  - Children (6-59 months): **65.5%** are anemic.
  - Women (15-49 years): **47.8%** are anemic.
  - Pregnant Women: **45.7%** are anemic.
- **Regional Disparity**: Kalyana Karnataka districts (Yadgir, Raichur, Kalaburagi) exhibit stunting rates above 40%, contrasting with coastal and southern districts (Udupi, Mandya) where rates are below 25%.

---

## 4. State Health & Nutrition Interventions

```mermaid
flowchart TD
    SCHEMES["Karnataka Health & Nutrition Architecture"] --> MATERNAL["1. Maternal & Child Nutrition\nMathru Poorna Scheme (One hot meal at Anganwadi)\nMathru Vandana Yojana (PMMVY - Cash transfer)\nKsheera Bhagya (Milk 5 days/wk for students)\nPoshan Abhiyaan (National Nutrition Mission)"]
    SCHEMES --> CARE["2. Healthcare Delivery & Insurance\nAyushman Bharat - Arogya Karnataka (AB-ArK)\nNamma Clinics (Urban PHCs in BBMP & cities)\nJanani Suraksha Yojana (JSY)\n108 Arogya Kavacha (Emergency Response)"]
    SCHEMES --> SANIT["3. Sanitation & Clean Water\nSwachh Bharat Mission (Grameen & Urban - ODF+)\nJal Jeevan Mission (Functional Tap Connections)\nShuchi Scheme (Menstrual hygiene sanitary pads)"]
```

The flowchart above outlines Karnataka's tiered interventions spanning maternal-child nutrition, universal health insurance, urban health clinics, and sanitation infrastructure.

### 4.1 Flagship Health & Nutrition Schemes
1. **Ayushman Bharat - Arogya Karnataka (AB-ArK)**:
   - Co-branded Universal Health Coverage scheme.
   - Provides cashless secondary and tertiary medical care of up to **Rs. 5 Lakhs per family per year** for eligible BPL families. APL families receive 30% co-payment support up to Rs. 1.5 Lakhs.
2. **Mathru Poorna Scheme (ಮಾತೃಪೂರ್ಣ ಯೋಜನೆ)**:
   - Launched to curb maternal malnutrition and low birth-weight.
   - Provides **one nutritious, hot cooked meal daily** (rice, dal/sambar, egg/sprouted gram, milk, vegetable) to pregnant and lactating mothers for 15 months at Anganwadi centres, along with Iron Folic Acid (IFA) tablets.
3. **Ksheera Bhagya Scheme (ಕ್ಷೀರಭಾಗ್ಯ ಯೋಜನೆ)**:
   - Provides 150 ml of nutritious milk 5 days a week to school children (Class 1 to 10) and Anganwadi children, utilizing surplus milk procurement by KMF (Nandini).
4. **Namma Clinics (ನಮ್ಮ ಕ್ಲಿನಿಕ್)**:
   - Established across municipal corporations, especially in BBMP (Bengaluru) wards and district headquarters, to deliver free outpatient consultation, basic diagnostic tests, and essential drugs in urban slums.
5. **Shuchi Scheme (ಶುಚಿ ಯೋಜನೆ)**:
   - Distribution of free sanitary napkins to adolescent school girls aged 10-19 years in government and aided schools to promote menstrual hygiene.

---

## 5. Water, Sanitation & Environmental Health

- **Swachh Bharat Mission (Grameen) Phase-II**:
  - Transition from Open Defecation Free (ODF) to **ODF Plus (ODF+)**.
  - Key focus areas: Solid Waste Management (SWM), Greywater Management (soak pits and stabilization ponds), Faecal Sludge Management, and plastic waste recycling units at Gram Panchayat level.
- **Jal Jeevan Mission (Mane Manege Gange - ಮನೆ ಮನೆಗೆ ಗಂಗೆ)**:
  - Providing Functional Household Tap Connections (FHTC) providing 55 liters per capita per day (lpcd) of potable water to all rural households.
  - Critical in addressing waterborne pathogens (diarrhea, cholera, enteric fever) and fluorosis in endemic districts (Kolar, Pavagada, Koppal).

---

## Likely Questions & PYQs

### Model Question 1 (Prelims)
**Q**: Kyasanur Forest Disease (KFD), commonly known as 'Monkey Fever', is transmitted to humans through the bite of which of the following vectors?
A) Aedes aegypti mosquito
B) Haemaphysalis spinigera tick
C) Phlebotomus sandfly
D) Anopheles stephensi mosquito
*Answer*: **B**
*Explanation*: KFD is caused by a flavivirus and transmitted primarily by the forest tick *Haemaphysalis spinigera*. Monkeys act as common hosts, and their death frequently flags an impending human outbreak.

### Model Question 2 (Prelims)
**Q**: Which of the following statements regarding Karnataka's demographic indicators as per official health data is/are correct?
1. Karnataka has achieved the Sustainable Development Goal (SDG) target of Maternal Mortality Ratio (MMR) below 70 per 1,00,000 live births.
2. The Total Fertility Rate (TFR) in Karnataka is below the replacement level of 2.1.
Select the correct answer:
A) 1 only
B) 2 only
C) Both 1 and 2
D) Neither 1 nor 2
*Answer*: **C**
*Explanation*: Both statements are correct. Karnataka's MMR stands at 69 (SDG target is <70), and its TFR is 1.7 (well below the 2.1 replacement level).

### Model Question 3 (Mains GS-3 - 12.5 Marks)
**Q**: Analyze the paradox between Karnataka's high economic performance and the persistent rates of child stunting and female anemia reported in NFHS-5. Suggest actionable policy measures to address regional malnutrition disparities in the state.

---

> [!summary]
> **Key Revision Points**:
> - MMR in Karnataka is 69 (SDG target <70 achieved); IMR is 19; TFR is 1.7.
> - KFD is caused by Flavivirus and transmitted by *Haemaphysalis spinigera* ticks (first found in Shivamogga 1957).
> - Child stunting is 35.4% and wasting is 19.5% in Karnataka (NFHS-5), with severe disparity in Kalyana Karnataka.
> - Mathru Poorna provides one hot cooked meal daily to pregnant/lactating mothers at Anganwadis.
> - AB-ArK provides up to Rs. 5 Lakhs cashless health coverage for BPL families.
"""

# Write all notes safely
for path, content in notes.items():
    safe_ops.safe_write(path, content)
    print(f"Successfully written: {os.path.basename(path)}")

print("Batch 1 completed successfully.")
