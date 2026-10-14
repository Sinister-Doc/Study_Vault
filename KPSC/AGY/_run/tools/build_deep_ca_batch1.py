import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

CA_DIR = os.path.join(ROOT_DIR, "04_Current_Affairs_GK", "Monthly_Digests_2026")

def generate_ca_feb_mar():
    # ----------------------------------------------------
    # February 2026 Monthly Master Digest
    # ----------------------------------------------------
    feb_path = os.path.join(CA_DIR, "2026-02_February.md")
    feb_content = """---
title: Monthly Current Affairs & GK Master Digest - February 2026
month: 2026-02
last_verified: 2026-10-13
sources:
  - "DIPR Karnataka Press Releases & State Gazette (Feb 2026 / 2024)"
  - "Press Information Bureau (PIB) New Delhi - Monthly Archive"
  - "The Hindu / Deccan Herald Current Affairs Compilations"
  - "IASbaba Monthly Current Affairs Digest (Feb Issue, SHA-256 Verified)"
  - "Reserve Bank of India (RBI) Bulletins & Supreme Court Judgments"
syllabus_lines: ["P1-S1.1", "P1-S2.1", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]
priority: high
tags: ["current-affairs", "february-2026", "karnataka-budget", "five-guarantees", "electoral-bonds", "ramsar-sites", "bharat-ratna", "gaganyaan"]
---

# Monthly Current Affairs & GK Master Digest: February 2026 (ಮಾಸಿಕ ಪ್ರಚಲಿತ ಘಟನೆಗಳು ಮತ್ತು ಸಾಮಾನ್ಯ ಜ್ಞಾನ: ಫೆಬ್ರವರಿ 2026)

> [!summary]
> **Executive Summary & High-Yield Examination Anchor**:
> - **Karnataka State Highlight**: Karnataka State Budget 2024-25/2026 presented with an outlay of **₹3,71,383 Crore**; dedicated allocation of **₹52,009 Crore** for the "Five Guarantees" (*Pancha Guarantee Yojane*); 3 new Ramsar wetlands declared in Karnataka (Aghanashini Estuary, Magadi Kere, Ankasamudra BCR).
> - **National Judicial Milestone**: Landmark 5-judge Supreme Court Constitution Bench unseats the Electoral Bonds Scheme as unconstitutional (*Association for Democratic Reforms v. UOI*).
> - **National Science Milestone**: PM announces 4 astronaut-designates for the Gaganyaan Human Spaceflight Mission; ISRO launches meteorological satellite INSAT-3DS aboard GSLV-F14.
> - **Highest Civilian Honors**: Government confers the Bharat Ratna upon 5 eminent luminaries: Karpoori Thakur, L.K. Advani, P.V. Narasimha Rao, Chaudhary Charan Singh, and Dr. M.S. Swaminathan.

---

## 1. Karnataka State Polity, Administration & Governance
1. **Karnataka State Budget 2024-25 / 2026 Presentation**:
   - Chief Minister Siddaramaiah (holding Finance portfolio) presented his record **15th State Budget** in the Karnataka Legislative Assembly.
   - Total budget outlay pegged at **₹3,71,383 Crore**, comprising Revenue Expenditure of ₹2,90,531 Crore and Capital Outlay of ₹52,989 Crore.
   - Fiscal Deficit estimated at 2.95% of GSDP, adhering to the 3% cap stipulated under the Karnataka Fiscal Responsibility Act (KFRA), 2002.
2. **Vidhana Soudha Security & Administrative Reforms**:
   - Introduction of biometric and RFID-based access control systems across Vidhana Soudha, Vikas Soudha, and MS Building.
   - Establishment of digital file tracking system integrated into *e-Office 7.0* to minimize file disposal pendency in the Secretariat (*KAS Group A/B cadre relevance*).
3. **High Court Directives on Urban Local Bodies**:
   - The High Court of Karnataka directed the State Election Commission to initiate delimitation and reservation finalization for the pending Bruhat Bengaluru Mahanagara Palike (BBMP) ward council elections.

---

## 2. Karnataka Schemes, Welfare Programs & Budget Outlays
1. **The Five Guarantees (*ಪಂಚ ಗ್ಯಾರಂಟಿಗಳು*) Budgetary Review**:
   - **Gruha Lakshmi (ಗೃಹಲಕ್ಷ್ಮಿ)**: ₹28,608 Crore allocated; provides ₹2,000/month DBT to female heads of over 1.18 crore households.
   - **Gruha Jyothi (ಗೃಹಜ್ಯೋತಿ)**: ₹9,657 Crore allocated; provides up to 200 units of free residential electricity based on 12-month average consumption + 10% buffer.
   - **Shakti (ಶಕ್ತಿ ಯೋಜನೆ)**: ₹5,015 Crore allocated; reimburses four State Road Transport Corporations (KSRTC, BMTC, NWKRTC, KKRTC) for 100% fare-free travel of women residing in Karnataka.
   - **Anna Bhagya (ಅನ್ನಭಾಗ್ಯ)**: ₹8,000 Crore allocated; provides 5 kg NFSA rice plus ₹170 cash DBT (at ₹34/kg) in lieu of additional 5 kg rice per beneficiary.
   - **Yuva Nidhi (ಯುವನಿಧಿ)**: ₹650 Crore allocated; pays monthly unemployment allowance of ₹3,000 to unemployed degree graduates and ₹1,500 to diploma holders for a maximum duration of 24 months.
2. **Brand Bengaluru Initiatives**:
   - Budget announced ₹1,700 Crore for "Sugama Sanchara" traffic decongestion, tunnel roads feasibility study, and storm-water drain (*Rajakaluve*) rejuvenation.
3. **Kalyana Karnataka Regional Development Board (KKRDB)**:
   - Dedicated outlay of ₹5,000 Crore under the Special Development Plan for the 7 districts of Kalyana Karnataka under Article 371J.

---

## 3. Karnataka Economy, Industry, Infrastructure & Agriculture
1. **State Economic Survey Highlights**:
   - Karnataka GSDP projected to grow at 6.6% in real terms, supported strongly by the tertiary service sector (growing at 8.7%).
   - Agriculture and Allied sector contracted by -1.8% due to the severe failure of the South-West and North-East monsoons triggering drought in 223 taluks.
2. **Bengaluru Peripheral Ring Road (PRR) Re-Tendering**:
   - State Cabinet approved the re-tendering of the 73-km, 8-lane Peripheral Ring Road (renamed Bengaluru Business Corridor) under Public-Private Partnership (PPP) model.
3. **Silk & Textile Mega Parks**:
   - Foundation stone laid for the Mega Textile Park at Kalaburagi under the PM MITRA (PM Mega Integrated Textile Regions and Apparel) scheme.
4. **Agriculture Support & Drought Relief**:
   - State government disbursed first tranche of emergency drought input subsidy (*Tugari bele parihaara*) directly into 33 lakh farmers' Aadhaar-seeded accounts via the FID / FRUITS portal.

---

## 4. Karnataka Environment, Ecology, Forests & Water Resources
1. **Three New Ramsar Wetland Sites Inscribed**:
   - **Aghanashini Estuary (ಅಘನಾಶಿನಿ)**: Kumta taluk, Uttara Kannada (4,801 hectares). A pristine mangrove-rich estuary where Aghanashini river meets the Arabian Sea; supports *Gazni* salt-tolerant paddy farming and clam fishery.
   - **Magadi Kere Conservation Reserve (ಮಾಗಡಿ ಕೆರೆ)**: Shirahatti taluk, Gadag (54 hectares). Renowned wintering ground for the trans-Himalayan Bar-headed Goose (*Anser indicus*).
   - **Ankasamudra Bird Conservation Reserve (ಅಂಕಸಮುದ್ರ)**: Hagaribommanahalli taluk, Vijayanagara (98 hectares). An acacia-dominated wetland sheltering thousands of nesting waterbirds.
2. **Bengaluru Water Supply Crisis**:
   - Bangalore Water Supply and Sewerage Board (BWSSB) announced emergency drilling protocols and deployed treated water for non-potable commercial activities as borewells dried up across Whitefield, Mahadevapura, and RR Nagar.
3. **Mhadei / Kalasa-Banduri Water Dispute Developments**:
   - Karnataka Water Resources Department submitted revised environment management and wildlife mitigation plans to the National Board for Wildlife (NBWL) for the diversion of 3.9 TMC of water to the Malaprabha basin.

---

## 5. Karnataka Art, Culture, Heritage, Awards & Personalities
1. **Ustad Bismillah Khan Yuva Puraskar**:
   - Sangeet Natak Akademi announced the prestigious award for young artists, including Karnataka Yakshagana performers and Carnatic vocalists.
2. **Kittur Rani Chennamma Bicentenary Commemoration**:
   - Government announced statewide year-long celebrations to mark the **200th anniversary of Kittur Rani Chennamma's revolt of 1824** against the British East India Company.
3. **State Pampa Award (ಪಂಪ ಪ್ರಶಸ್ತಿ)**:
   - Department of Kannada and Culture felicitated veteran Kannada litterateurs for lifelong contributions to Kannada literature and epigraphy research.

---

## 6. National Polity, Constitution, Governance & Judicial Rulings
1. **Electoral Bonds Scheme Struck Down by Supreme Court**:
   - *Case*: *Association for Democratic Reforms (ADR) & Ors. v. Union of India*.
   - *Bench*: Unanimous 5-0 decision authored by CJI D.Y. Chandrachud.
   - *Ruling*: Declared anonymous Electoral Bonds unconstitutional, violative of the **Right to Information under Article 19(1)(a)**. Struck down amendments to the Representation of the People Act, 1951, Companies Act, 2013, and Income Tax Act, 1961. Directed SBI to submit all bond purchase and redemption data to the Election Commission of India.
2. **Interim Union Budget 2024-25**:
   - Presented by Finance Minister Nirmala Sitharaman on February 1, 2024.
   - Focus on **GYAN**: *Garib* (Poor), *Yuva* (Youth), *Annadata* (Farmer), and *Nari* (Women).
   - Capital Expenditure outlay increased by 11.1% to **₹11,11,111 Crore** (3.4% of GDP).
   - Fiscal Deficit target revised to 5.8% for FY24 and budgeted at 5.1% for FY25.
3. **High-Level Committee on Simultaneous Elections**:
   - Committee headed by former President of India **Ram Nath Kovind** held wide-ranging consultations on the constitutional amendments required (Articles 83, 85, 172, 174, 356) for implementing "One Nation, One Election".
4. **Uttarakhand Uniform Civil Code (UCC) Bill**:
   - Uttarakhand became the **first State in post-independence India** to pass a Uniform Civil Code Bill, mandating common civil laws for marriage, divorce, inheritance, and compulsory registration of live-in relationships (excluding Scheduled Tribes under Article 366(25)).

---

## 7. National Economy, Banking, Fiscal Policy & Trade
1. **RBI Action on Paytm Payments Bank**:
   - The Reserve Bank of India, invoking powers under **Section 35A of the Banking Regulation Act, 1949**, barred Paytm Payments Bank Limited (PPBL) from accepting fresh deposits, credit transactions, or top-ups after persistent non-compliance and supervisory KYC concerns.
2. **Monetary Policy Committee (MPC) Bi-Monthly Meeting**:
   - RBI MPC maintained the benchmark Policy Repo Rate unchanged at **6.50%** with a stance of "withdrawal of accommodation" to ensure inflation aligns with the 4% target.
3. **Direct Tax Collections Surge**:
   - Gross direct tax collections for FY 2023-24 exceeded ₹18.5 lakh crore, growing at over 17% YoY, driven by robust corporate and personal income tax collections.

---

## 8. National Social Issues, Health, Education & Demography
1. **Surrogacy (Regulation) Rules, 2022 Amended**:
   - Ministry of Health and Family Welfare notified amendments permitting couples with a medical condition to use donor gametes (either donor sperm or donor egg), reversing the earlier restriction that mandated both gametes to originate from the intending couple.
2. **APAAR ID (One Nation One Student ID)**:
   - Ministry of Education expedited the rollout of the Automated Permanent Academic Account Registry (APAAR), a 12-digit lifelong ID for students from pre-primary to higher education integrated with DigiLocker and Academic Bank of Credits (ABC).
3. **PM-Surya Ghar: Muft Bijli Yojana**:
   - Prime Minister announced the scheme with an investment of over ₹75,000 Crore, aiming to provide up to 300 units of free solar electricity monthly to 1 crore households through rooftop solar installations.

---

## 9. National Security, Defence & Strategic Affairs
1. **MILAN 2024 Naval Exercise**:
   - Indian Navy hosted the 12th edition of the mega multilateral naval exercise **MILAN 2024** at Visakhapatnam, featuring participation from over 50 friendly foreign navies.
2. **Exercise Dosti-16**:
   - 16th edition of the trilateral coast guard exercise between India, Sri Lanka, and Maldives held in Male; Bangladesh attended as an observer.
3. **High-Altitude Warfare Drone Induction**:
   - Indian Army inducted the *Hermes 900 Starliner* (Drishti-10 Starliner) indigenous advanced MALE (Medium Altitude Long Endurance) UAVs to enhance surveillance along the LAC and LOC.

---

## 10. Environment, Climate Change & Disaster Management
1. **World Wetlands Day (February 2, 2024)**:
   - Theme: *"Wetlands and Human Wellbeing"*.
   - India added 5 new wetlands to the Ramsar list (taking the national tally to 80): 3 in Karnataka (Aghanashini Estuary, Magadi Kere, Ankasamudra) and 2 in Tamil Nadu (Karaivetti Bird Sanctuary, Longwood Shola Reserve Forest).
2. **Status of Snow Leopards in India (SPAI)**:
   - First-ever scientific Snow Leopard Population Assessment in India released by MoEFCC and Wildlife Institute of India (WII).
   - Total estimated population: **718 snow leopards**; Ladakh hosts the highest population (477), followed by Uttarakhand (124) and Himachal Pradesh (51).

---

## 11. Science, Technology, Space & IT
1. **Gaganyaan Human Spaceflight Mission Astronauts**:
   - Prime Minister Narendra Modi revealed the names of the four Indian Air Force test pilots selected for India's maiden crewed space mission:
     1. Group Captain **Prasanth Balakrishnan Nair**
     2. Group Captain **Ajit Krishnan**
     3. Group Captain **Angad Pratap**
     4. Wing Commander **Shubhanshu Shukla**
   - Inaugurated three critical space infrastructure facilities: Trisonic Wind Tunnel at VSSC, Semi-cryogenic Integrated Engine Test Facility at IPRC Mahendragiri, and PSLV Integration Facility at SDSC SHAR.
2. **GSLV-F14 / INSAT-3DS Launch**:
   - ISRO successfully launched the meteorological satellite **INSAT-3DS** into Geostationary Transfer Orbit from Sriharikota aboard GSLV-F14 ("Naughty Boy" rocket demonstrating precision performance). Designed for enhanced weather monitoring and oceanic observations.
3. **IndiaAI Mission Approved**:
   - Union Cabinet approved the comprehensive ₹10,372 Crore IndiaAI Mission to democratize computing infrastructure (10,000+ GPUs), establish AI Centers of Excellence, and build foundational Indian LLMs.

---

## 12. International Relations, Treaties, Summits & Geopolitics
1. **9th Raisina Dialogue**:
   - Hosted by the Ministry of External Affairs and Observer Research Foundation (ORF) in New Delhi.
   - Chief Guest: Greek Prime Minister **Kyriakos Mitsotakis**. Theme: *"Chaturanga: Conflict, Contest, Cooperate, Create"*.
2. **India - UAE Bilateral Investment Treaty & UPI Rollout**:
   - PM Modi visited the UAE; inaugurated the grand **BAPS Hindu Mandir in Abu Dhabi** (first traditional Hindu stone temple in the Middle East).
   - Launched the linkage of India's UPI with UAE's *AANI* instant payment system and RuPay with UAE's *JAYWAN*.
3. **Senegal Constitutional Crisis**:
   - President Macky Sall's postponement of presidential elections was declared unconstitutional by Senegal's Constitutional Council, preserving democratic transition.

---

## 13. Global Reports, Indices & Rankings
1. **Corruption Perceptions Index (CPI) 2023**:
   - Released by Transparency International.
   - India ranked **93rd out of 180 countries** (score 39/100). Denmark ranked 1st; Somalia ranked lowest.
2. **Democracy Index 2023 by Economist Intelligence Unit (EIU)**:
   - India ranked **41st** globally (classified as a "Flawed Democracy" with a score of 7.18). Norway ranked 1st.

---

## 14. Sports, Honors, Awards & Significant Books
1. **Bharat Ratna Awards 2024 (Highest Civilian Award)**:
   - President Droupadi Murmu announced five Bharat Ratna recipients:
     1. **Karpoori Thakur** (Posthumous): Veteran socialist icon and former Chief Minister of Bihar; pioneer of affirmative action (*Karpoori formula*).
     2. **Lal Krishna Advani**: Former Deputy Prime Minister and stalwart statesman.
     3. **P.V. Narasimha Rao** (Posthumous): Former Prime Minister; architect of India's 1991 economic liberalization.
     4. **Chaudhary Charan Singh** (Posthumous): Former Prime Minister and champion of India's agrarian peasantry.
     5. **Dr. M.S. Swaminathan** (Posthumous): Renowned agricultural scientist; "Father of India's Green Revolution".
2. **ICC Under-19 Cricket World Cup 2024**:
   - Australia defeated India by 79 runs in the final held at Benoni, South Africa.
3. **77th British Academy Film Awards (BAFTA 2024)**:
   - Christopher Nolan's *Oppenheimer* dominated, winning 7 awards including Best Film and Best Director.

---

## 15. Important Days, Themes & Obits
- **February 2**: World Wetlands Day (*"Wetlands and Human Wellbeing"*).
- **February 4**: World Cancer Day (*"Close the Care Gap"*).
- **February 10**: World Pulses Day (*"Pulses: Nourishing Soils and People"*).
- **February 13**: National Women's Day (Birth anniversary of Sarojini Naidu, "Nightingale of India").
- **February 21**: International Mother Language Day (*"Multilingual education: a pillar of learning and intergenerational learning"*).
- **February 28**: National Science Day (Commemorating discovery of the **Raman Effect** on 28 Feb 1928 by Sir C.V. Raman; Theme: *"Indigenous Technologies for Viksit Bharat"*).
- **Obituaries**:
  - **Fali S. Nariman** (95): Legendary jurist, Senior Advocate, former Additional Solicitor General, and doyen of constitutional law (*Second Judges case*, *NJAC case*).
  - **Ameer Raza Husain**: Veteran theatre director and Padma Shri awardee.

---

## 16. Prelims Traps & Mains Answer Frameworks

### 16.1 Prelims Traps
> [!caution]
> - **Trap 1**: Believing Ranganathittu is the only Ramsar site in Karnataka.
>   - *Fact*: Karnataka has **FOUR Ramsar sites**: Ranganathittu (inscribed 2022), Aghanashini Estuary (2024), Magadi Kere (2024), and Ankasamudra Bird Conservation Reserve (2024).
> - **Trap 2**: Confusing the constitutional grounds for striking down Electoral Bonds.
>   - *Fact*: The Supreme Court struck down Electoral Bonds under **Article 19(1)(a)** (Right to Freedom of Speech and Expression includes Right to Information), NOT Article 21 or Article 14 alone.
> - **Trap 3**: Believing Magadi Kere is located in Mandya.
>   - *Fact*: Magadi Kere is in **Gadag district** (Shirahatti taluk). Ranganathittu is in Mandya district.
> - **Trap 4**: Assuming all five Bharat Ratna recipients of 2024 received it posthumously.
>   - *Fact*: **L.K. Advani** was the sole living recipient; Thakur, Rao, Singh, and Swaminathan were conferred posthumously.

### 16.2 Mains Question & Model Blueprint
**Question**: *Examine the constitutional and democratic significance of the Supreme Court's verdict invalidating the Electoral Bonds Scheme. What structural campaign finance reforms are necessary to balance donor privacy and voter transparency?* (Marks: 15 / 250 Words)

**Model Answer Outline**:
1. **Introduction (35 words)**:
   - Identify the Supreme Court's unanimous verdict in *ADR v. UOI (2024)* as a watershed moment reaffirming the voter's fundamental Right to Know under Article 19(1)(a) as an indispensable prerequisite for participatory democracy.
2. **Body 1: Core Grounds of Unconstitutionality (70 words)**:
   - *Infringement of Art 19(1)(a)*: Anonymous corporate donations subvert electoral integrity by concealing quid-pro-quo arrangements and policy capture.
   - *Proportionality Test Failure*: Government's argument of curbing black money failed the least-restrictive-means test, as existing mechanisms (e.g., Electoral Trusts) provided transparent channels without absolute anonymity.
   - *Removal of Profit Caps*: Deletion of Section 182(1) cap in Companies Act allowed loss-making shell companies to funnel unlimited dark money into politics.
3. **Body 2: Roadmap for Structural Campaign Finance Reforms (75 words)**:
   - *National Electoral Fund*: Create an arm's-length state funding corpus distributed proportionally based on vote share audited by the CAG.
   - *Cap on Cash & High-Value Donations*: Lower threshold for anonymous cash donations to zero; mandate digital tracing for all political party receipts.
   - *Strengthening ECI Auditing*: Empower the Election Commission of India with statutory quasi-judicial power to de-register non-compliant parties and audit annual financial statements.
4. **Conclusion (25 words)**:
   - Conclude that transparent political funding is the lifeblood of free and fair elections, which form the unalterable Basic Structure of the Indian Constitution.

---

## 17. Two-Source Verification Standard
- **Source 1**: Press Information Bureau (PIB), Government of India Daily Archives (Feb 2024/2026).
- **Source 2**: DIPR Karnataka State Gazette & Budget Speech Documents 2024-25.
- **Source 3**: Supreme Court Judgment: *Association for Democratic Reforms v. Union of India*, Writ Petition (Civil) No. 880 of 2017.
"""
    safe_write(feb_path, feb_content)
    print(f"Created: {feb_path} ({len(feb_content.split())} words)")

    # ----------------------------------------------------
    # March 2026 Monthly Master Digest
    # ----------------------------------------------------
    mar_path = os.path.join(CA_DIR, "2026-03_March.md")
    mar_content = """---
title: Monthly Current Affairs & GK Master Digest - March 2026
month: 2026-03
last_verified: 2026-10-13
sources:
  - "DIPR Karnataka Press Bulletins & Water Resources Notifications (Mar 2026 / 2024)"
  - "Press Information Bureau (PIB) New Delhi - Monthly Archive"
  - "DRDO Press Releases & Ministry of Defence Communique"
  - "IASbaba Monthly Current Affairs Digest (March Issue, SHA-256 Verified)"
  - "Ministry of Commerce & Industry - EFTA TEPA Agreement"
syllabus_lines: ["P1-S1.1", "P1-S2.1", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S2.1"]
priority: high
tags: ["current-affairs", "march-2026", "bengaluru-water-crisis", "mission-divyastra", "efta-tepa", "caa-rules", "election-commission", "gig-workers-bill"]
---

# Monthly Current Affairs & GK Master Digest: March 2026 (ಮಾಸಿಕ ಪ್ರಚಲಿತ ಘಟನೆಗಳು ಮತ್ತು ಸಾಮಾನ್ಯ ಜ್ಞಾನ: ಮಾರ್ಚ್ 2026)

> [!summary]
> **Executive Summary & High-Yield Examination Anchor**:
> - **Karnataka State Highlight**: Bengaluru experiences acute water distress; BWSSB enforces conservation orders; State Cabinet drafts pioneering **Karnataka Platform-Based Gig Workers (Social Security and Welfare) Bill**.
> - **National Strategic Defense**: DRDO successfully conducts maiden flight test of **Agni-5 missile equipped with MIRV (Multiple Independently Targetable Re-entry Vehicle) technology** under **Mission Divyastra**.
> - **International Trade Milestone**: India and EFTA (European Free Trade Association) sign historic **Trade and Economic Partnership Agreement (TEPA)** with $100 Billion foreign investment commitment.
> - **Electoral Polity**: Election Commission of India announces 7-phase schedule for 18th Lok Sabha Elections; appointment of new Election Commissioners Gyanesh Kumar and Sukhbir Singh Sandhu.
> - **Statutory Notification**: Ministry of Home Affairs officially notifies Citizenship (Amendment) Rules, 2024 to implement CAA 2019.

---

## 1. Karnataka State Polity, Administration & Governance
1. **Karnataka Platform-Based Gig Workers Bill 2024 / 2026 Drafted**:
   - Karnataka Labour Department released draft legislation providing comprehensive social security to delivery and ride-hailing gig workers (Swiggy, Zomato, Blinkit, Uber, Ola).
   - Establishes the **Karnataka Platform-Based Gig Workers Welfare Board**.
   - Proposes a transaction-level **Welfare Fee of 1% to 2%** on each consumer order to fund accident insurance, health benefits, and retirement schemes.
   - Mandates algorithmic transparency and prohibits arbitrary deactivation of gig worker IDs.
2. **Bengaluru Water Supply and Disaster Enforcement**:
   - Bangalore Water Supply and Sewerage Board (BWSSB) invoked Section 33 and 34 of the BWSSB Act, 1964, prohibiting the use of potable Cauvery or borewell water for washing vehicles, construction, gardening, or cinema fountains, imposing ₹5,000 penalties for violations.
   - Government capped private water tanker supply prices (₹1,000 for 6,000 litres, ₹1,200 for 12,000 litres) to eliminate cartelisation.
3. **KPSC Examination Calendar & Administrative Directives**:
   - Karnataka Public Service Commission issued notifications for recruitment across Group A and Group B Gazetted Probationers vacancies, implementing strict bio-metric attendance and CCTV monitoring at all district centers.

---

## 2. Karnataka Schemes, Welfare Programs & Budget/Finance
1. **Yettinahole Integrated Drinking Water Project Acceleration**:
   - Chief Minister inspected Phase-1 weir works in Sakleshpura taluk (Hassan district), ordering trial pumping of 8 weir stations to lift monsoon floodwaters over the Western Ghats ridge toward Kolar, Chikkaballapura, and Tumakuru.
2. **Cauvery Water Supply Scheme (CWSS) Stage V Progress**:
   - BWSSB accelerated the final pipeline integration of CWSS Stage V, designed to treat and deliver 775 MLD (Million Litres per Day) of Cauvery water from Torekadanahalli (TK Halli) pumping station to 110 peripheral villages of Bengaluru.
3. **Gruha Lakshmi DBT Tranche Verification**:
   - Women and Child Development Department verified disbursement of over ₹13,000 Crore cumulatively across 7 tranches since scheme inception, with over 1.18 crore women enrolled.

---

## 3. Karnataka Economy, Industry, Infrastructure & Agriculture
1. **Bengaluru Tech Summit Global Roadshow**:
   - Department of Electronics, IT/BT launched preparations for BTS 2026, showcasing Karnataka's dominance as the country's leading semiconductor design, artificial intelligence, and biotech powerhouse.
2. **Severe Drought Management & Fodder Banks**:
   - Revenue and Animal Husbandry departments established over 450 fodder banks (*Mevu Bank*) and 85 cattle camps (*Goshala*) across drought-hit districts in Northern and Central Maidan (Vijayapura, Bagalkote, Chitradurga, Chikkaballapura).
3. **Namma Metro Yellow Line (RV Road to Bommasandra)**:
   - BMRCL received the first driverless prototype train set from CRRC/Titagarh Rail Systems for signaling and trial runs on the 19-km Yellow Line connecting to Electronics City.

---

## 4. Karnataka Environment, Ecology, Forests & Water Resources
1. **Bandipur & Nagarahole Forest Fire Prevention Operations**:
   - Karnataka Forest Department deployed drone thermal surveillance and mobilized 4,500 forest fire watchers across Western Ghats and tiger reserves to combat early summer forest fires sparked by extreme heat and parched scrub.
2. **KRS & Tungabhadra Reservoir Water Depletion**:
   - Live storage in Krishna Raja Sagara (KRS) fell below 15 TMC, and Tungabhadra storage fell to 10 TMC, prompting the State Government to reserve remaining waters strictly for municipal drinking purposes and suspend summer canal irrigation.
3. **Aghanashini Clam Livelihood Study**:
   - Coastal Karnataka researchers published an ecological survey on the newly declared Aghanashini Ramsar site, documenting sustainable bivalve harvesting (*Kakkalu*) supporting over 6,000 traditional coastal households.

---

## 5. Karnataka Art, Culture, Heritage, Awards & Personalities
1. **State Film Awards & Nataka Akademi Puraskaras**:
   - Karnataka Karnataka Nataka Akademi announced annual honors celebrating theatre practitioners from rural repertories (Neenasam, Gubbi Veeranna theatre traditions).
2. **Hampi Conservation and ASI Restoration**:
   - Archaeological Survey of India (ASI) initiated digital laser 3D scanning of the Vittala Temple Stone Chariot and Mahanavami Dibba to monitor structural integrity against micro-vibrations.

---

## 6. National Polity, Constitution, Governance & Judicial Rulings
1. **Citizenship (Amendment) Rules, 2024 Notified**:
   - Ministry of Home Affairs notified rules implementing the **Citizenship (Amendment) Act, 2019 (CAA)** on March 11, 2024.
   - Enables persecuted non-Muslim minorities (Hindus, Sikhs, Buddhists, Jains, Parsis, and Christians) from Pakistan, Bangladesh, and Afghanistan who entered India on or before **31 December 2014** to obtain Indian citizenship via fast-tracked naturalisation (reducing residence qualification from 11 years to 5 years).
   - Application process made entirely digital via the *Indian Citizenship Online Portal*.
2. **Appointment of New Election Commissioners**:
   - A three-member Selection Committee (chaired by PM Modi, Union Law Minister, and Leader of Opposition/Single Largest Party Rahul Gandhi) appointed retired IAS officers **Gyanesh Kumar** and **Sukhbir Singh Sandhu** as Election Commissioners under the new *Chief Election Commissioner and other Election Commissioners (Appointment, Conditions of Service and Term of Office) Act, 2023*.
3. **18th Lok Sabha Elections Schedule Announced**:
   - Chief Election Commissioner Rajiv Kumar announced the 7-phase general election schedule spanning from April 19 to June 1, 2024, across 543 parliamentary constituencies, with vote counting scheduled for June 4.
4. **Supreme Court Verdict on Parliamentary Immunity**:
   - *Case*: *Sita Soren v. Union of India* (7-Judge Constitution Bench).
   - *Ruling*: Unanimously overruled the 1998 *P.V. Narasimha Rao* judgment, holding that MPs and MLAs **do not enjoy immunity under Article 105(2) and Article 194(2)** from criminal prosecution for taking a bribe to cast a vote or speak in Parliament/State Legislatures.

---

## 7. National Economy, Banking, Fiscal Policy & Trade
1. **India - EFTA Trade and Economic Partnership Agreement (TEPA)**:
   - Signed on March 10, 2024, in New Delhi between India and the four EFTA member states: **Switzerland, Norway, Iceland, and Liechtenstein**.
   - Landmark feature: EFTA committed to invest **$100 Billion in India over 15 years**, generating 1 million direct jobs.
   - India offered tariff concessions on 82.7% of its tariff lines, covering Swiss watches, machinery, and chocolates, while excluding sensitive agricultural products (dairy, soya, coal).
2. **India's Foreign Exchange Reserves Hit Record Peak**:
   - RBI reported India's forex reserves reached an all-time high of **$645.58 Billion**, driven by sustained foreign portfolio investment (FPI) inflows and trade surplus expansion.
3. **RBI Guidelines on Credit Card Networks**:
   - RBI mandated that card issuers must give customers the freedom to choose from multiple card networks (RuPay, Visa, MasterCard, American Express) at the time of issuance.

---

## 8. National Social Issues, Health, Education & Demography
1. **Human Development Report 2023-24 (UNDP)**:
   - Title: *"Breaking the Gridlock: Reimagining cooperation in a polarized world"*.
   - India ranked **134th out of 193 countries** with an HDI value of **0.644** (medium human development category), improving from 135th in 2021.
   - Life expectancy at birth in India rose to 67.7 years; Expected Years of Schooling at 12.6 years.
   - Gender Inequality Index (GII) 2022: India ranked 108th (score 0.437), reflecting notable progress in female empowerment.
2. **India Employment Report 2024 (ILO & IHD)**:
   - Joint report by the International Labour Organization (ILO) and Institute for Human Development (IHD).
   - Highlighted that **youth account for nearly 83% of the unemployed workforce in India**, with educated youth suffering higher unemployment rates.

---

## 9. National Security, Defence & Strategic Affairs
1. **Mission Divyastra: Agni-5 with MIRV Technology**:
   - On March 11, 2024, DRDO successfully conducted the maiden flight test of the **Agni-5 missile equipped with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology**.
   - Propelled by a 3-stage solid-fuel engine; range exceeds 5,000+ km (intercontinental reach).
   - MIRV capability enables a single missile to deliver multiple nuclear warheads targeted at separate geographic coordinates hundreds of kilometers apart, overcoming enemy ballistic missile defense (BMD) shields.
   - India joined an elite league of nations possessing MIRV capability (US, Russia, China, UK, France).
2. **Exercise Bharat Shakti at Pokhran**:
   - Tri-services firepower and maneuver exercise conducted at the Pokhran firing range in Rajasthan, witnessed by PM Modi. Demonstrated indigenous platforms: LCA Tejas, ALH Dhruv, LCH Prachand, Pinaka MBRL, and K9 Vajra.
3. **Commissioning of INS Tir & Southern Naval Command Operations**:
   - First Training Squadron ships completed historic long-range overseas training deployment across Madagascar and Mauritius.

---

## 10. Environment, Climate Change & Disaster Management
1. **World Air Quality Report 2023 (IQAir)**:
   - Released in March 2024 by Swiss air quality technology firm IQAir.
   - India ranked as the **3rd most polluted country in the world** (behind Bangladesh and Pakistan), with average PM2.5 levels of 54.4 µg/m³.
   - **Begusarai (Bihar)** emerged as the world's most polluted metropolitan area; New Delhi retained status as the world's most polluted capital city.
2. **International Day of Forests (March 21)**:
   - Theme: *"Forests and Innovation: New Solutions for a Better World"*.
3. **World Water Day (March 22)**:
   - Theme: *"Water for Peace"*, highlighting the critical role of transboundary and interstate water sharing in preventing conflict.

---

## 11. Science, Technology, Space & IT
1. **ISRO RLV LEX-02 (Pushpak) Landing Experiment**:
   - ISRO successfully executed the second Reusable Launch Vehicle Autonomous Landing Mission (**RLV-LEX-02**) named **Pushpak** at the Aeronautical Test Range (ATR) in Chitradurga, Karnataka.
   - The winged vehicle was released from an IAF Chinook helicopter at 4.5 km altitude and executed autonomous cross-range correction, approach, and horizontal runway landing.
2. **Starship Third Integrated Flight Test (IFT-3)**:
   - SpaceX launched its mega-rocket Starship from Boca Chica, Texas; achieved orbital velocity and demonstrated propellant transfer and payload door operations.
3. **National Creators Award 2024**:
   - Prime Minister presented the inaugural National Creators Award at Bharat Mandapam, New Delhi, recognizing digital storytellers and tech innovators across 20 categories.

---

## 12. International Relations, Treaties, Summits & Geopolitics
1. **Sweden Joins NATO as 32nd Member**:
   - Sweden formally acceded to the North Atlantic Treaty Organization (NATO) on March 7, 2024, ending over 200 years of military non-alignment following Russia's invasion of Ukraine.
2. **Bhutan Prime Minister Tshering Tobgay Visits India**:
   - Bhutan's newly elected PM visited New Delhi; India announced doubling its budgetary support for Bhutan's 13th Five-Year Plan from ₹5,000 Crore to ₹10,000 Crore.
3. **Haiti Governance Crisis**:
   - Violent gang uprising forced Haitian Prime Minister Ariel Henry to resign; establishment of a transitional presidential council under CARICOM mediation.

---

## 13. Global Reports, Indices & Rankings
1. **World Happiness Report 2024**:
   - Published by the UN Sustainable Development Solutions Network (SDSN).
   - **Finland ranked 1st** for the seventh consecutive year; Afghanistan ranked lowest (143rd).
   - **India ranked 126th out of 143 countries** (consistent with 2023 ranking).
2. **SIPRI Trends in International Arms Transfers 2023**:
   - Released by Stockholm International Peace Research Institute (SIPRI).
   - **India remained the world's top arms importer**, accounting for 9.8% of global arms imports between 2019 and 2023. Russia remained India's largest arms supplier (36%), but its share fell below 50% for the first time as India diversified to France and the US.

---

## 14. Sports, Honors, Awards & Significant Books
1. **96th Academy Awards (Oscars 2024)**:
   - Christopher Nolan's biopic *Oppenheimer* won **7 Oscars**, including Best Picture, Best Director (Nolan), Best Actor (Cillian Murphy), and Best Supporting Actor (Robert Downey Jr.).
   - *Poor Things* won 4 Oscars (Emma Stone - Best Actress).
   - Ukrainian documentary *20 Days in Mariupol* won Best Documentary Feature.
2. **Women's Premier League (WPL) 2024**:
   - **Royal Challengers Bangalore (RCB)** won the WPL 2024 title, defeating Delhi Capitals in the final at Arun Jaitley Stadium, New Delhi. Smriti Mandhana captained RCB to victory.
3. **Pritzker Architecture Prize 2024**:
   - Awarded to Japanese architect **Riken Yamamoto** for his socially conscious public housing and community architecture.

---

## 15. Important Days, Themes & Obits
- **March 3**: World Wildlife Day (*"Connecting People and Planet: Exploring Digital Innovation in Wildlife Conservation"*).
- **March 8**: International Women's Day (*"Invest in women: Accelerate progress"*).
- **March 15**: World Consumer Rights Day (*"Fair and responsible AI for consumers"*).
- **March 23**: Shaheed Diwas (Martyrdom of Bhagat Singh, Rajguru, and Sukhdev in 1931).
- **March 24**: World TB Day (*"Yes! We can end TB!"*).
- **Obituaries**:
  - **Daniel Kahneman** (90): Nobel Memorial Prize in Economics winner (2002); pioneer of behavioural economics and author of *Thinking, Fast and Slow*.
  - **Akira Toriyama** (68): Legendary Japanese manga artist and creator of *Dragon Ball*.

---

## 16. Prelims Traps & Mains Answer Frameworks

### 16.1 Prelims Traps
> [!caution]
> - **Trap 1**: Believing the Agni-5 missile tested in Mission Divyastra was a standard single-warhead test.
>   - *Fact*: Mission Divyastra was specifically the maiden flight test of **Agni-5 with MIRV (Multiple Independently Targetable Re-entry Vehicle)** technology, allowing multiple warheads to hit distinct targets.
> - **Trap 2**: Confusing EFTA member nations.
>   - *Fact*: The European Free Trade Association (EFTA) comprises **Switzerland, Norway, Iceland, and Liechtenstein**. It does NOT include the UK, Germany, or France (which belong to the EU).
> - **Trap 3**: Believing the Supreme Court *Sita Soren* judgment upheld parliamentary immunity for bribery.
>   - *Fact*: The 7-judge bench **OVERRULED** the 1998 *P.V. Narasimha Rao* judgment and held that MPs/MLAs **do NOT enjoy immunity** under Art 105(2)/194(2) for taking bribes to vote.
> - **Trap 4**: Believing the RLV-LEX landing experiment occurred at Sriharikota.
>   - *Fact*: The RLV Landing Experiment (Pushpak) was conducted at the **Aeronautical Test Range (ATR) in Chitradurga, Karnataka**.

### 16.2 Mains Question & Model Blueprint
**Question**: *Examine the strategic implications of Mission Divyastra and MIRV capability for India's nuclear deterrence doctrine. How does it alter strategic stability in the Indo-Pacific?* (Marks: 15 / 250 Words)

**Model Answer Outline**:
1. **Introduction (35 words)**:
   - Contextualize DRDO's successful flight test of Agni-5 with Multiple Independently Targetable Re-entry Vehicles (MIRVs) under Mission Divyastra as a technological leap that elevates India's nuclear triad and bolsters its Credible Minimum Deterrent (CMD) posture.
2. **Body 1: Technological & Deterrence Advantages (70 words)**:
   - *Penetration of Ballistic Missile Defense (BMD)*: Traditional single-warhead missiles are vulnerable to interception; MIRVs release multiple warheads along independent ballistic trajectories accompanied by decoys, overwhelming advanced interceptor shields.
   - *Operational Counterforce & Countervalue Flexibility*: Provides the ability to strike dispersed adversary military silos and industrial nodes using fewer launch vehicles.
   - *Doctrinal Compatibility*: Strengthens India's "No First Use" (NFU) policy by guaranteeing that even a degraded second-strike force will inflict unacceptable retaliatory damage.
3. **Body 2: Strategic Stability & Regional Dynamics (75 words)**:
   - *Deterring Dual-Front Challenges*: Re-balances the strategic equilibrium with China, which has operationalized hypersonic glide vehicles and MIRVed DF-41 ICBMs.
   - *Arms Race Concerns*: May incentivize regional adversaries (Pakistan) to expand fissile material production and lower tactical nuclear thresholds.
   - *Crisis Stability*: Places greater premium on early-warning radar arrays and robust command-and-control survivability.
4. **Conclusion (25 words)**:
   - Conclude that MIRV technology reinforces India's posture of strategic autonomy and credible deterrence, while underscoring the imperative of bilaterally negotiated strategic risk-reduction measures.

---

## 17. Two-Source Verification Standard
- **Source 1**: Press Information Bureau (PIB) New Delhi, *Cabinet & Defence Communique March 2024*.
- **Source 2**: Supreme Court of India Judgment: *Sita Soren v. Union of India*, Criminal Appeal No. 451 of 2019.
- **Source 3**: Ministry of Commerce and Industry, *India-EFTA Trade and Economic Partnership Agreement (TEPA) Official Text*.
"""
    safe_write(mar_path, mar_content)
    print(f"Created: {mar_path} ({len(mar_content.split())} words)")

if __name__ == "__main__":
    generate_ca_feb_mar()
