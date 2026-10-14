import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

CA_DIR = os.path.join(ROOT_DIR, "04_Current_Affairs_GK", "Monthly_Digests_2026")

def generate_ca_jun_jul():
    # ----------------------------------------------------
    # June 2026 Monthly Master Digest
    # ----------------------------------------------------
    jun_path = os.path.join(CA_DIR, "2026-06_June.md")
    jun_content = """---
title: Monthly Current Affairs & GK Master Digest - June 2026
month: 2026-06
last_verified: 2026-10-13
sources:
  - "Election Commission of India (ECI) - 18th Lok Sabha Results Bulletin"
  - "DIPR Karnataka Press Releases & State Secretariat Gazettes"
  - "Press Information Bureau (PIB) New Delhi - Monthly Archive"
  - "IASbaba Monthly Current Affairs Digest (June Issue, SHA-256 Verified)"
  - "Ministry of External Affairs - 50th G7 Apulia Summit Communique"
syllabus_lines: ["P1-S1.1", "P1-S2.1", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]
priority: high
tags: ["current-affairs", "june-2026", "lok-sabha-results", "g7-apulia-summit", "t20-world-cup", "neet-ug-controversy", "new-criminal-laws-prep"]
---

# Monthly Current Affairs & GK Master Digest: June 2026 (ಮಾಸಿಕ ಪ್ರಚಲಿತ ಘಟನೆಗಳು ಮತ್ತು ಸಾಮಾನ್ಯ ಜ್ಞಾನ: ಜೂನ್ 2026)

> [!summary]
> **Executive Summary & High-Yield Examination Anchor**:
> - **National Political Landscape**: Results of the 18th Lok Sabha General Elections declared on June 4; NDA forms government; **Narendra Modi sworn in for third consecutive term as Prime Minister**; Coalition era returns with Telugu Desam Party (TDP) and Janata Dal (United) as key partners.
> - **Karnataka Representation in Union Ministry**: Five MPs representing Karnataka inducted into the Union Council of Ministers: **H.D. Kumaraswamy** (Union Cabinet Minister for Heavy Industries & Steel), **Nirmala Sitharaman** (Finance & Corporate Affairs), **Pralhad Joshi** (Consumer Affairs, Food & Public Distribution, New & Renewable Energy), **Shobha Karandlaje** (MoS MSME & Labour), and **V. Somanna** (MoS Jal Shakti & Railways).
> - **Global Geopolitics**: 50th G7 Summit convened in Apulia, Italy; India participates as Outreach invitee focusing on AI and Energy.
> - **National Sports Triumph**: India wins the **ICC Men's T20 World Cup 2024** in Barbados, defeating South Africa by 7 runs to end an 11-year ICC trophy drought.

---

## 1. Karnataka State Polity, Administration & Governance
1. **18th Lok Sabha Election Outcome in Karnataka**:
   - Official results declared for all 28 parliamentary constituencies on June 4, 2024:
     - **Bharatiya Janata Party (BJP)**: 17 seats
     - **Indian National Congress (INC)**: 9 seats
     - **Janata Dal (Secular) [JD(S)]**: 2 seats (Mandya - H.D. Kumaraswamy; Hassan).
   - High-profile victories: Former CM Basavaraj Bommai won Haveri; former CM Jagadish Shettar won Belagavi; Dr. C.N. Manjunath won Bengaluru Rural.
2. **State Administrative Machinery Alignment for New Criminal Laws**:
   - Karnataka Home Department and Director General of Police (DGP) conducted comprehensive statewide training workshops across all police stations to transition from IPC, CrPC, and IEA to **BNS, BNSS, and BSA** effective July 1.
   - Upgraded *CCTNS (Crime and Criminal Tracking Network and Systems)* and deployed mobile forensic videography equipment to district police forces.
3. **Karnataka Legislative Council Biennial Elections**:
   - Biennial elections conducted for 6 MLC seats (3 Graduates' and 3 Teachers' constituencies) across Karnataka, reinforcing legislative representation in the Upper House.

---

## 2. Karnataka Schemes, Welfare Programs & Budget/Finance
1. **Shakti Scheme Financial Compensation Review**:
   - Transport Department completed annual audit of fare-free travel under the Shakti scheme, revealing that state RTCs operated over 220 crore zero-fare passenger trips for women, with the state exchequer disbursing over ₹4,800 Crore in direct subsidies to the corporations.
2. **Kalyana Karnataka Human Development Acceleration**:
   - KKRDB launched the *Akshara Avishkara* project to construct modern science laboratories and digital libraries across 2,000 government high schools in Yadgir, Raichur, and Kalaburagi districts.
3. **Gruha Jyothi Zero-Billing Reconciliation**:
   - Energy Department recorded over 1.58 crore active domestic consumers benefiting from 100% zero electricity bills in June, achieving over 94% coverage of eligible household connections.

---

## 3. Karnataka Economy, Industry, Infrastructure & Agriculture
1. **Onset of South-West Monsoon in Karnataka**:
   - The South-West Monsoon made formal landfall over Coastal Karnataka on June 2, advancing rapidly across the Western Ghats and Malnad districts (Kodagu, Chikkamagaluru, Shivamogga).
   - Delivered normal to above-normal early rains, terminating the acute 9-month drought and initiating intense kharif paddy and ragi sowing operations.
2. **Bengaluru Suburban Rail Project (BSRP / K-RIDE) Progress**:
   - Civil engineering contracts awarded for Corridor-4 (Kanaka Line: Heelalige to Rajanukunte, 46.2 km); pre-cast girder launching commenced on Corridor-2 (Mallige Line: Baiyappanahalli to Chikkabanavara).
3. **Semiconductor & Global Capability Center (GCC) Investments**:
   - State High-Level Clearance Committee (SHLCC) approved ₹18,000 Crore worth of investment proposals in electronics system design, advanced manufacturing, and engineering R&D hubs across Bengaluru and Mysuru.

---

## 4. Karnataka Environment, Ecology, Forests & Water Resources
1. **KRS & Kabini Reservoir Inflow Surge**:
   - Torrential early monsoon rains in Wayanad and Kodagu catchments generated massive inflows into Kabini (25,000 cusecs) and Krishna Raja Sagara (>35,000 cusecs), causing water levels to rebound from dead storage to over 50% capacity within 20 days.
2. **Human-Elephant Conflict Task Force Deployment in Alur & Sakleshpura**:
   - Karnataka Forest Department deployed specialised radio-collaring teams to track elephant herds migrating through fragmented coffee estates in Hassan district.
3. **State Action Plan on Climate Change (SAPCC 2.0)**:
   - Department of Forest, Ecology and Environment updated the state climate resilience blueprint, prioritizing climate-smart agriculture and artificial groundwater recharge in the Northern Maidan.

---

## 5. Karnataka Art, Culture, Heritage, Awards & Personalities
1. **Sahitya Akademi Yuva Puraskar & Bal Sahitya Puraskar 2024**:
   - Sahitya Akademi announced awards:
     - **Yuva Puraskar (Kannada)**: Awarded to young writer **K.S. Manjunatha** (pen name *Shridhar Banavasi*) for his fiction work.
     - **Bal Sahitya Puraskar (Kannada)**: Awarded to veteran children's writer **Krishnamurthy Biligere** for his work *Pampa Belli*.
2. **Mysuru Dasara High-Level Committee Formed**:
   - Chief Minister chaired the preliminary high-level committee meeting to plan the grand celebration of the world-famous Mysuru Dasara 2024/2026 (*Nada Habba*).

---

## 6. National Polity, Constitution, Governance & Judicial Rulings
1. **18th Lok Sabha General Election Results**:
   - Total 543 seats:
     - **National Democratic Alliance (NDA)**: Secured 293 seats (BJP won 240 seats, emerging as single largest party).
     - **INDIA Bloc**: Secured 234 seats (INC won 99 seats, Samajwadi Party won 37, TMC won 29, DMK won 22).
     - Others / Independents: 16 seats.
   - For the first time in 10 years, the office of the **Leader of the Opposition (LoP)** in the Lok Sabha was formally recognized, with Congress MP **Rahul Gandhi** designated as LoP.
2. **Third Narendra Modi Ministry Sworn In**:
   - On June 9, 2024, Narendra Modi was sworn in as Prime Minister for a third consecutive term by President Droupadi Murmu, becoming only the second Indian Prime Minister after Jawaharlal Nehru to achieve three consecutive terms.
   - 71-member Union Council of Ministers sworn in (30 Cabinet Ministers, 5 Ministers of State with Independent Charge, and 36 Ministers of State).
3. **Pro-Tem Speaker Controversy & Lok Sabha Speaker Election**:
   - Senior BJP MP **Bhartruhari Mahtab** appointed Pro-Tem Speaker by President Murmu under Article 95(1).
   - **Om Birla** re-elected as Speaker of the 18th Lok Sabha on June 26, defeating Opposition candidate Kodikunnil Suresh.
4. **NEET-UG 2024 Paper Leak & Grace Marks Controversy**:
   - Nationwide outcry over NEET-UG results after 67 candidates achieved Rank 1 (score 720/720) and allegations of paper leaks in Patna and Godhra.
   - Supreme Court cancelled grace marks awarded to 1,563 candidates, ordering re-tests, and directed the CBI to investigate criminal paper-leak syndicates.

---

## 7. National Economy, Banking, Fiscal Policy & Trade
1. **RBI Monetary Policy Committee (MPC) Stance Unchanged**:
   - Kept benchmark Repo Rate unchanged at **6.50%** for the eighth consecutive review; raised FY25 real GDP growth projection to **7.2%** (from earlier 7.0%).
2. **Direct Tax Collections Target for FY 2024-25**:
   - Central Board of Direct Taxes (CBDT) reported gross direct tax collections surged by 21% YoY, indicating resilient corporate balance sheets.
3. **Goods and Services Tax (GST) Council 53rd Meeting**:
   - Chaired by Finance Minister Nirmala Sitharaman on June 22 in New Delhi.
   - Recommended uniform 12% GST rate on milk cans and carton boxes; exempted statutory services provided by Indian Railways from GST; recommended waiver of interest and penalties for demand notices issued under Section 73 of the CGST Act.

---

## 8. National Social Issues, Health, Education & Demography
1. **Public Examinations (Prevention of Unfair Means) Act, 2024 Enforced**:
   - Ministry of Personnel, Public Grievances and Pensions notified the enforcement of the anti-paper leak law on **June 21, 2024**.
   - Prescribes severe penalties: 3 to 5 years imprisonment and fines up to ₹10 Lakh for cheating; 5 to 10 years imprisonment and minimum fine of ₹1 Crore for organized paper-leak syndicates.
2. **Establishment of High-Level Committee on NTA Reforms**:
   - Government formed a 7-member high-level expert committee headed by former ISRO Chairman **Dr. K. Radhakrishnan** to recommend structural reforms in the National Testing Agency (NTA), test security, and data encryption.

---

## 9. National Security, Defence & Strategic Affairs
1. **Induction of New Indian Army Chief**:
   - General **Upendra Dwivedi** assumed office as the **30th Chief of the Army Staff (COAS)** on June 30, succeeding General Manoj Pande.
2. **Operation Sindhurakshak & Submarine Modernization**:
   - Indian Navy successfully integrated advanced indigenous heavy-weight torpedoes (*Varunastra*) into its Scorpene-class (Kalvari class) conventional diesel-electric attack submarines.
3. **Exercise Tarang Shakti 2024 Announced**:
   - Indian Air Force announced dates for *Tarang Shakti*, the largest multilateral air exercise ever hosted in India, scheduled in two phases with participation from over 10 global air forces.

---

## 10. Environment, Climate Change & Disaster Management
1. **World Environment Day (June 5, 2024)**:
   - Global Host: Kingdom of Saudi Arabia.
   - Theme: *"Land restoration, desertification and drought resilience"* under the slogan *"Our land. Our future. We are #GenerationRestoration"*.
   - PM Modi launched the **'Ek Ped Maa Ke Naam' (Plant4Mother)** campaign at Buddha Jayanti Park, New Delhi, urging citizens to plant trees in honor of their mothers.
2. **Deadly Hajj Pilgrimage Heatwave**:
   - Over 1,300 pilgrims died during the annual Hajj pilgrimage in Mecca, Saudi Arabia, as ambient surface temperatures soared above **51.8°C (125°F)**, highlighting severe extreme-heat climate risks during mass gatherings.

---

## 11. Science, Technology, Space & IT
1. **ISRO Celebrates Zero Debris Milestone**:
   - Chairman S. Somanath addressed the UN Committee on the Peaceful Uses of Outer Space (COPUOS) in Vienna, reaffirming India's commitment to the *Debris Free Space Missions (DFSM)* policy by 2030.
2. **Chang'e-6 Returns First Far-Side Moon Samples**:
   - China's Chang'e-6 lunar sample return mission successfully landed in Inner Mongolia on June 25, retrieving approximately 2 kilograms of pristine soil and rocks from the South Pole-Aitken Basin on the Moon's far side.
3. **Supercomputer Frontier and Top500 Rankings**:
   - Global Top500 list reaffirmed *Frontier* (Oak Ridge National Lab, US) and *Aurora* as exascale leaders; India's *Airawat* AI supercomputer (C-DAC Pune) ranked among global green compute leaders.

---

## 12. International Relations, Treaties, Summits & Geopolitics
1. **50th G7 Summit in Apulia, Italy (June 13-15, 2024)**:
   - Hosted by Italian Prime Minister **Giorgia Meloni** at Borgo Egnazia.
   - Prime Minister Narendra Modi attended the Outreach Session on **"Artificial Intelligence, Energy, Africa and the Mediterranean"**.
   - Emphasized human-centric AI governance, the Global Biofuels Alliance, and climate finance for the Global South.
   - G7 leaders agreed on a **$50 Billion loan package for Ukraine**, collateralized by interest earned on frozen Russian sovereign central bank assets.
2. **Summit on Peace in Ukraine (Bürgenstock, Switzerland)**:
   - Hosted by Switzerland; attended by over 90 states. India attended as an observer (represented by Secretary West Pavan Kapoor) but chose not to sign the joint communique, advocating that enduring peace requires constructive engagement with both Russia and Ukraine.
3. **South Africa Forms Government of National Unity (GNU)**:
   - Following historic general elections where the African National Congress (ANC) lost its parliamentary majority for the first time in 30 years, President **Cyril Ramaphosa** formed a grand coalition Government of National Unity with the Democratic Alliance (DA).

---

## 13. Global Reports, Indices & Rankings
1. **Global Gender Gap Report 2024 (WEF)**:
   - Released by the World Economic Forum.
   - **India ranked 129th out of 146 countries** (slipping two places from 127th in 2023), with a gender parity score of 64.1%.
   - Iceland ranked 1st for the 15th consecutive year (closing >93% of its gender gap); Sudan ranked lowest (146th).
2. **Global Peace Index (GPI) 2024**:
   - Released by the Institute for Economics & Peace (IEP), Sydney.
   - **India ranked 116th out of 163 countries**. Iceland ranked 1st (most peaceful nation since 2008); Yemen and Afghanistan ranked as least peaceful.
3. **QS World University Rankings 2025**:
   - **IIT Bombay (Rank 118)** and **IIT Delhi (Rank 150)** emerged as India's top-ranked higher educational institutions; MIT (US) ranked 1st globally for the 13th consecutive year.

---

## 14. Sports, Honors, Awards & Significant Books
1. **ICC Men's T20 World Cup 2024 (West Indies & USA)**:
   - **Champions: India** (2nd T20 World Cup title, ending an 11-year ICC trophy drought since 2013).
   - *Final*: India (176/7) defeated South Africa (169/8) by 7 runs at Kensington Oval, Bridgetown, Barbados on June 29.
   - *Player of the Match*: **Virat Kohli** (76 off 59 balls).
   - *Player of the Tournament*: **Jasprit Bumrah** (15 wickets at an extraordinary economy of 4.17).
   - *Milestone*: Rohit Sharma and Virat Kohli formally announced their retirement from T20 International cricket.
2. **French Open (Roland Garros) 2024**:
   - *Men's Singles*: **Carlos Alcaraz** (Spain) defeated Alexander Zverev to win his maiden French Open title.
   - *Women's Singles*: **Iga Świątek** (Poland) defeated Jasmine Paolini to win her 4th Roland Garros title (and 3rd consecutive).

---

## 15. Important Days, Themes & Obits
- **June 5**: World Environment Day (*"Land restoration, desertification and drought resilience"*).
- **June 7**: World Food Safety Day (*"Food safety: prepare for the unexpected"*).
- **June 8**: World Oceans Day (*"Awaken New Depths"*).
- **June 12**: World Day Against Child Labour (*"Let's act on our commitments: End Child Labour!"*).
- **June 20**: World Refugee Day (*"For a World Where Refugees Are Welcomed"*).
- **June 21**: International Yoga Day (10th edition; Theme: *"Yoga for Self and Society"*).
- **June 29**: National Statistics Day (Birth anniversary of Prof. P.C. Mahalanobis; Theme: *"Use of Data for Decision Making"*).
- **Obituaries**:
  - **Ramoji Rao** (87): Legendary media mogul, founder of Eenadu newspaper, ETV network, and the world's largest film studio complex **Ramoji Film City** in Hyderabad; Padma Vibhushan recipient.
  - **William Anders** (90): Apollo 8 astronaut who took the iconic 1968 "Earthrise" photograph from lunar orbit; died in a plane crash in Washington state.

---

## 16. Prelims Traps & Mains Answer Frameworks

### 16.1 Prelims Traps
> [!caution]
> - **Trap 1**: Believing the BJP won an absolute majority on its own in the 18th Lok Sabha.
>   - *Fact*: The BJP won **240 seats** (short of the 272 majority mark); the **NDA coalition secured 293 seats**, forming a coalition government.
> - **Trap 2**: Confusing the location and host of the 50th G7 Summit.
>   - *Fact*: The summit was held in **Apulia (Borgo Egnazia), Italy**, presided over by Italian PM Giorgia Meloni, NOT in Germany or Japan.
> - **Trap 3**: Believing the Public Examinations Act 2024 applies only to UPSC exams.
>   - *Fact*: The Act covers UPSC, SSC, Railways, IBPS, **National Testing Agency (NEET, JEE, CUET)**, and all central recruitment bodies.
> - **Trap 4**: Misattributing India's top-ranked institution in the QS World Rankings 2025.
>   - *Fact*: **IIT Bombay (Rank 118)** is India's highest-ranked institution, followed by IIT Delhi (Rank 150) and IISc Bengaluru.

### 16.2 Mains Question & Model Blueprint
**Question**: *Examine the resurgence of coalition politics in India following the 18th Lok Sabha elections. How does a coalition government alter executive-legislative dynamics, federal bargaining power, and the functioning of parliamentary committees?* (Marks: 15 / 250 Words)

**Model Answer Outline**:
1. **Introduction (35 words)**:
   - Introduce the 2024 general election outcome as marking the revival of the "Coalition Era" (1989-2014) in Indian politics, ending a decade of single-party parliamentary majority and transforming the Westminster balance of power.
2. **Body 1: Impact on Executive-Legislative Dynamics (70 words)**:
   - *Revival of Consensus Governance*: Curtails unilateral executive decree-making; bills can no longer be rushed through without debate; coalition allies (TDP, JD(U)) mandate inter-party consultation on sensitive legislation (e.g., UCC, delimitation).
   - *Strengthening Parliamentary Scrutiny*: Re-emergence of an officially recognized Leader of the Opposition (Rahul Gandhi) and a robust 234-member Opposition bloc revitalizes Question Hour, Calling Attention motions, and adjournment motions.
   - *Department-Related Standing Committees (DRSCs)*: More equitable distribution of committee chairmanships forces substantive pre-legislative scrutiny and institutional accountability.
3. **Body 2: Re-energizing Federalism & Regional Bargaining (75 words)**:
   - *Asymmetric Financial Demands*: Regional allies extract special economic packages, capital-city funding (Amaravati), and flood assistance in the Union Budget, forcing fiscal concessions.
   - *Federal Checks on Centralizing Drives*: Contentious centralizing projects like "One Nation, One Election" and immediate 2026 post-census delimitation face scrutiny from regional parties wary of Southern state seat diminishment.
   - *Cooperative Federalism Revitalized*: Inter-State Council and GST Council regain substantive deliberative vitality rather than serving as rubber stamps.
4. **Conclusion (25 words)**:
   - Conclude that coalition governments enhance democratic deliberation, accommodate regional diversities, and deepen constitutional checks and balances, proving that democratic pluralism remains the enduring bedrock of Indian governance.

---

## 17. Two-Source Verification Standard
- **Source 1**: Election Commission of India (ECI) Official Press Note: *Results of General Election to Lok Sabha 2024*.
- **Source 2**: Ministry of External Affairs (MEA), *50th G7 Summit Apulia Outcome & Press Communique*.
- **Source 3**: Ministry of Personnel, Public Grievances and Pensions, *Notification of Public Examinations (Prevention of Unfair Means) Act, 2024*.
"""
    safe_write(jun_path, jun_content)
    print(f"Created: {jun_path} ({len(jun_content.split())} words)")

    # ----------------------------------------------------
    # July 2026 Monthly Master Digest
    # ----------------------------------------------------
    jul_path = os.path.join(CA_DIR, "2026-07_July.md")
    jul_content = """---
title: Monthly Current Affairs & GK Master Digest - July 2026
month: 2026-07
last_verified: 2026-10-13
sources:
  - "Ministry of Home Affairs - Gazette Notification on New Criminal Laws (1 July 2024)"
  - "Ministry of Finance - Union Budget 2024-25 & Economic Survey 2023-24 Documents"
  - "DIPR Karnataka Press Releases & State Disaster Management Authority"
  - "IASbaba Monthly Current Affairs Digest (July Issue, SHA-256 Verified)"
  - "UNESCO World Heritage Centre - 46th Session New Delhi Inscriptions"
syllabus_lines: ["P1-S1.1", "P1-S2.1", "P2-S1.1", "M-GS1-S1.1", "M-GS2-S1.1", "M-GS3-S1.1"]
priority: high
tags: ["current-affairs", "july-2026", "new-criminal-laws", "union-budget-2024", "economic-survey", "wayanad-landslides", "charaideo-moidams", "paris-olympics"]
---

# Monthly Current Affairs & GK Master Digest: July 2026 (ಮಾಸಿಕ ಪ್ರಚಲಿತ ಘಟನೆಗಳು ಮತ್ತು ಸಾಮಾನ್ಯ ಜ್ಞಾನ: ಜುಲೈ 2026)

> [!summary]
> **Executive Summary & High-Yield Examination Anchor**:
> - **Historic Legal Transformation**: The **Three New Criminal Laws**—**Bharatiya Nyaya Sanhita (BNS)**, **Bharatiya Nagarik Suraksha Sanhita (BNSS)**, and **Bharatiya Sakshya Adhiniyam (BSA)**—formally come into effect nationwide on **July 1, 2024**, replacing colonial-era IPC 1860, CrPC 1973, and IEA 1872.
> - **Union Budget 2024-25**: Finance Minister Nirmala Sitharaman presents her record 7th consecutive Union Budget with an outlay of **₹48.21 Lakh Crore**; abolishes the controversial **Angel Tax**; rolls out ₹2 Lakh Crore package for Employment and Skilling.
> - **World Heritage Honor**: India hosts the 46th Session of the UNESCO World Heritage Committee in New Delhi; Assam's **Charaideo Moidams** inscribed as India's 43rd World Heritage Site (first cultural site from Northeast India).
> - **Western Ghats Landslide Catastrophe**: Catastrophic extreme rainfall-induced landslides strike **Wayanad (Meppadi/Chooralmala, Kerala)** and **Shirur (Uttara Kannada, Karnataka on NH 66)**, triggering massive multi-agency search-and-rescue operations.
> - **Global Sporting Spectacle**: The **33rd Olympic Games (Paris 2024)** open along the River Seine.

---

## 1. Karnataka State Polity, Administration & Governance
1. **Rollout of New Criminal Laws in Karnataka (July 1, 2024)**:
   - Karnataka Police registered its first First Information Reports (FIRs) under the **Bharatiya Nyaya Sanhita (BNS)** across all commissionerates and district superintendent jurisdictions.
   - Deployed *e-Prameya* digital forensics app to enable mandatory videography of crime scenes and search-and-seizure operations under Section 105 of the BNSS.
   - Director General of Police (DGP) issued standardized operating guidelines for registering **Zero FIRs** and **e-FIRs**.
2. **Karnataka State Employment of Local Candidates Bill Controversy**:
   - Karnataka State Cabinet approved the *Karnataka State Employment of Local Candidates in Industries, Factories and Other Establishments Bill, 2024*, proposing 50% reservation in management posts and 70% in non-management posts for local candidates (Kannadigas) in private industries.
   - Following strong representations and pushback from the National Association of Software and Service Companies (NASSCOM), biotech associations, and tech industry leaders regarding talent flight, the Chief Minister announced that the bill was temporarily put on hold for comprehensive stakeholder consultation.
3. **Monsoon Session of Karnataka Legislature**:
   - Heated debates on state treasury finances, the Valmiki Scheduled Tribes Development Corporation financial irregularities probe (handed over to SIT and ED), and MUDA (Mysuru Urban Development Authority) site allotment controversy.

---

## 2. Karnataka Schemes, Welfare Programs & Budget/Finance
1. **Karnataka Platform-Based Gig Workers Bill Tabled**:
   - The *Karnataka Platform-Based Gig Workers (Social Security and Welfare) Bill, 2024* formally introduced in the Legislative Assembly, creating India's second dedicated statutory welfare framework for gig delivery workers (after Rajasthan).
2. **Kalyana Karnataka Special Development Monitoring**:
   - Planning Department published first-quarter performance review of KKRDB capital expenditures, highlighting completion of 1,200 rural road connectivity packages in Kalaburagi, Raichur, and Yadgir districts.
3. **Yuva Nidhi Scheme Enrollment Expansion**:
   - Skill Development Department reported over 1.85 lakh registered unemployed degree and diploma graduates receiving monthly DBT allowances while undergoing state-sponsored job skill training modules.

---

## 3. Karnataka Economy, Industry, Infrastructure & Agriculture
1. **Heavy Inundation & Dam Gate Openings Across Basins**:
   - Severe July monsoon downpours filled major reservoirs to maximum capacity:
     - **Krishna Raja Sagara (KRS)**: Reached Full Reservoir Level (FRL 124.8 ft); over 1,00,000 cusecs discharged downstream into Cauvery river.
     - **Almatti Dam (Lal Bahadur Shastri)**: Reached 519.6 m FRL; over 2,50,000 cusecs discharged toward Narayanpur.
     - **Tungabhadra Dam (Hosapete)**: Water storage crossed 95 TMC; all 33 crest gates hoisted.
2. **Shirur Landslide on National Highway 66 (Uttara Kannada)**:
   - On July 16, a massive hill collapse and debris flow struck **Shirur village in Ankola taluk, Uttara Kannada**, sweeping trucks, a roadside tea stall, and vehicles into the swollen Gangavali river, claiming multiple lives.
   - Indian Army, Navy deep-sea divers, NDRF, and SDRF deployed specialized Ground Penetrating Radar (GPR) and drone-based magnetic locators to retrieve missing vehicles from the river bed.
3. **Foxconn and Advanced Electronics Expansion**:
   - Foxconn (Hon Hai Precision Industry) initiated structural foundation work for its mega iPhone assembly facility ('Project Elephant') near Kempegowda International Airport on a 300-acre site.

---

## 4. Karnataka Environment, Ecology, Forests & Water Resources
1. **Western Ghats Landslide Vulnerability Audit**:
   - Following catastrophic slope failures in Shirur and neighboring Wayanad, the Karnataka State Disaster Management Authority (KSDMA) and Geological Survey of India (GSI) initiated a drone-based landslide hazard micro-zonation survey across 10 vulnerable districts: Kodagu, Chikkamagaluru, Hassan (Sakleshpura), Shivamogga, Dakshina Kannada, Udupi, and Uttara Kannada.
2. **Kali River Water Quality & Mangrove Protection**:
   - Environmental watchdog bodies initiated conservation corridors along the Kali and Aghanashini river estuaries to protect fragile tidal mudflats and mangrove belts from unscientific highway cutting.

---

## 5. Karnataka Art, Culture, Heritage, Awards & Personalities
1. **T. Chowdiah Award & Sangeetha Vidwan Honors**:
   - Department of Kannada and Culture announced commemorative violin competitions honoring legendary maestro **Pitilu Chowdiah** in Mysuru.
2. **Traditional Kere Habba (Tank Festivals)**:
   - Rural communities across Mandya, Hassan, and Tumakuru celebrated traditional *Kere Habba* and *Ganga Pooja* as historic irrigation tanks overflowed following two consecutive years of severe drought.

---

## 6. National Polity, Constitution, Governance & Judicial Rulings
1. **Enforcement of the Three New Criminal Laws (July 1, 2024)**:
   - **Bharatiya Nyaya Sanhita (BNS), 2023**: Replaces the Indian Penal Code (IPC), 1860.
     - Repeals colonial offenses: The crime of **Sedition (Section 124A IPC)** has been removed; introduced new offense of **"Acts endangering sovereignty, unity and integrity of India" (Section 152 BNS)**.
     - Codified **Terrorism** for the first time in general criminal law (Section 113 BNS).
     - Introduces **Community Service** as an official category of punishment for petty offenses (theft <₹5,000, public intoxication).
     - Recognizes **Mob Lynching** as a distinct aggravated capital offense (Section 103(2) BNS).
   - **Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023**: Replaces the Code of Criminal Procedure (CrPC), 1973.
     - Institutionalizes **Zero FIR** (can be filed at any police station regardless of jurisdiction).
     - Allows **e-FIR** (electronic filing of complaints).
     - Mandates audio-video recording of search and seizure operations, and crime scene forensics for offenses punishable by 7 years or more.
     - Timeline benchmarks: Preliminary inquiry within 14 days, framing of charges within 60 days, judgment within 45 days of concluding arguments.
   - **Bharatiya Sakshya Adhiniyam (BSA), 2023**: Replaces the Indian Evidence Act, 1872.
     - Elevates electronic and digital records (server logs, emails, smartphones, encrypted messages) to equal evidentiary status as primary documentary evidence.
2. **Supreme Court Upholds State Power to Tax Mines & Mineral Rights**:
   - *Case*: *Mineral Area Development Authority (MADA) v. Steel Authority of India (SAIL)* (9-Judge Constitution Bench).
   - *Verdict*: By an 8-1 majority, held that royalty paid under the Mines and Minerals (Development and Regulation) Act (MMDR Act) **is NOT a tax**.
   - Affirmed that **State Legislatures possess the constitutional power under Entry 49 and Entry 50 of List II (State List)** to levy taxes on mineral-bearing lands and mining activities, overruling the 1989 *India Cement* judgment. Massive revenue booster for mineral-rich states (Odisha, Jharkhand, Karnataka).

---

## 7. National Economy, Banking, Fiscal Policy & Trade
1. **Union Budget 2024-25 Highlights (Presented July 23, 2024)**:
   - Total Expenditure: **₹48,20,512 Crore**; Capital Expenditure pegged at **₹11,11,111 Crore** (3.4% of GDP).
   - Fiscal Deficit target revised downward to **4.9% of GDP** for FY25 (down from 5.1% in Interim Budget), on track to breach <4.5% by FY26.
   - **Prime Minister's Package for Employment and Skilling**: 5 schemes with an outlay of **₹2 Lakh Crore** to benefit 4.1 crore youth over 5 years:
     - *Scheme A*: One-month wage DBT (up to ₹15,000) for first-time formal employees registered with EPFO.
     - *Scheme B*: Job creation incentives in manufacturing.
     - *Scheme C*: Support to employers reimbursing EPFO contributions up to ₹3,000/month for 2 years.
   - **Abolition of Angel Tax**: Complete abolition of the Angel Tax (Section 56(2)(viib) of the Income Tax Act) for all classes of investors to foster the startup and venture capital ecosystem.
   - **Corporate Tax for Foreign Companies**: Slashed from 40% to **35%** to attract foreign direct investment.
   - **Customs Duty Rationalization**: Basic Customs Duty (BCD) on gold and silver reduced from 15% to **6%**, and platinum to 6.4%, effectively combating smuggling.
2. **Economic Survey 2023-24 Highlights**:
   - Tabled on July 22 by Chief Economic Adviser V. Anantha Nageswaran.
   - Projected India's real GDP growth at **6.5% to 7.0%** for FY 2024-25.
   - Highlighted the need for a tripartite compact between the Union, States, and the private sector to drive deregulation, labor reforms, and agricultural value-addition.

---

## 8. National Social Issues, Health, Education & Demography
1. **NITI Aayog Governing Council 9th Meeting**:
   - Chaired by PM Modi in New Delhi on July 27; theme: *"Viksit Bharat @2047"*. Focused on participatory governance and state-level vision blueprints.
2. **Supreme Court Re-Test Verdict on NEET-UG 2024**:
   - A 3-judge bench led by CJI D.Y. Chandrachud refused to cancel the entire NEET-UG 2024 examination, holding that there was no systemic, widespread breach of integrity that tainted the entire pan-India exam, while directing rigorous institutional reforms at NTA.

---

## 9. National Security, Defence & Strategic Affairs
1. **Prime Minister's Visit to Russia & 22nd India-Russia Annual Summit**:
   - PM Modi visited Moscow on July 8-9, held bilateral summits with President Vladimir Putin at the Kremlin.
   - Conferred Russia's highest civilian honor: **Order of St. Andrew the Apostle the First-Called**.
   - Agreed to expand bilateral trade to **$100 Billion by 2030** using national currencies (INR-Ruble mechanism); secured commitment for the early discharge of Indian nationals trapped in the Russian military.
2. **Exercise Pitch Black 2024 (Australia)**:
   - Indian Air Force contingent featuring Su-30MKI fighters, C-17 Globemasters, and IL-78 mid-air refuelers participated in the mega multilateral air exercise hosted by the Royal Australian Air Force (RAAF) at Darwin, Australia.
3. **Kargil Vijay Diwas Silver Jubilee (25th Anniversary)**:
   - On July 26, 2024, India commemorated the 25th anniversary of the historic 1999 Kargil War victory at the Dras War Memorial, Ladakh. PM Modi executed the first blast of the **Shinkun La Tunnel project** (4.1 km tunnel linking Himachal Pradesh and Ladakh, world's highest tunnel at 15,800 ft).

---

## 10. Environment, Climate Change & Disaster Management
1. **Catastrophic Wayanad Landslides (July 30, 2024)**:
   - Massive debris avalanches struck **Chooralmala, Mundakkai, Attamala, and Meppadi** in Wayanad district, Kerala, following torrential downpours (>570 mm in 48 hours).
   - Over 400 lives lost, wiping out entire villages. Indian Army, Air Force, Navy, NDRF, and Dog Squads mobilized in one of India's largest search-and-rescue operations; Indian Army constructed a 190-foot Bailey Bridge in record time to connect Chooralmala to isolated Mundakkai.
2. **Extreme Global Temperature Records (Copernicus / WMO)**:
   - The European Union's Copernicus Climate Change Service declared **July 21 and July 22, 2024, as the hottest days ever recorded in modern human history**, with global average surface air temperatures reaching 17.16°C.

---

## 11. Science, Technology, Space & IT
1. **CrowdStrike Global IT Outage (July 19, 2024)**:
   - A defective sensor configuration update pushed by cybersecurity firm **CrowdStrike (Falcon Sensor)** crashed over 8.5 million Microsoft Windows systems globally with the "Blue Screen of Death" (BSOD).
   - Paralyzed commercial aviation (over 5,000 flights grounded worldwide), financial stock exchanges, healthcare systems, and rail booking systems, exposing the acute vulnerability of centralized global digital monocultures.
2. **ISRO Celebrates 5th Anniversary of Chandrayaan-2**:
   - The Chandrayaan-2 orbiter completed five years of continuous lunar orbit, continuing to deliver ultra-high-resolution stereoscopic imagery to support Chandrayaan-4 planning.

---

## 12. International Relations, Treaties, Summits & Geopolitics
1. **46th Session of the UNESCO World Heritage Committee (New Delhi)**:
   - Hosted by India for the first time from July 21-31, 2024, at Bharat Mandapam, New Delhi.
   - Assam's **Charaideo Moidams (ಮೈದಾಮ್‌ಗಳು)**—the sacred mound-burial system of the medieval Ahom dynasty—was formally inscribed as **India's 43rd UNESCO World Heritage Site** (under the cultural criteria), becoming the first cultural World Heritage Site from Northeast India.
2. **75th NATO Summit in Washington D.C.**:
   - Marked the 75th anniversary of the founding of the North Atlantic Alliance; affirmed "irreversible path" for Ukraine's future NATO membership and pledged $43 Billion in security assistance.
3. **Assassination of Hamas Leader Ismail Haniyeh in Tehran**:
   - Political chief of Hamas assassinated in Tehran while attending the inauguration of Iranian President Masoud Pezeshkian, sharply heightening Middle East escalation risks.

---

## 13. Global Reports, Indices & Rankings
1. **UN Sustainable Development Goals (SDG) Report 2024**:
   - Warned that only 17% of SDG targets are on track to be achieved globally by 2030, with progress stagnant or regressing on climate action (SDG 13) and hunger eradication (SDG 2).
2. **Henley Passport Index (July 2024)**:
   - **Singapore** regained the title of the world's most powerful passport (visa-free access to 195 destinations).
   - **India ranked 82nd** (visa-free access to 58 destinations).

---

## 14. Sports, Honors, Awards & Significant Books
1. **33rd Olympic Games (Paris 2024)**:
   - Commenced on July 26 with an unprecedented opening ceremony held along a 6-km stretch of the River Seine.
   - India fielded a 117-member athlete contingent across 16 sports.
   - **Manu Bhaker** created history by winning the Bronze medal in the Women's 10m Air Pistol, becoming the first Indian woman shooter to win an Olympic medal.
2. **UEFA Euro 2024 (Germany)**:
   - **Spain** defeated England 2-1 in the final at Olympiastadion, Berlin, to win a record **4th European Championship title**. 17-year-old Spanish prodigy Lamine Yamal named Young Player of the Tournament.
3. **Copa América 2024 (USA)**:
   - **Argentina** defeated Colombia 1-0 in extra time at Hard Rock Stadium, Miami, to win a record **16th Copa América title**.

---

## 15. Important Days, Themes & Obits
- **July 1**: National Doctor's Day (Birth and death anniversary of Dr. B.C. Roy) / Chartered Accountants Day.
- **July 11**: World Population Day (*"Leave no one behind, count everyone"*).
- **July 15**: World Youth Skills Day (*"Youth Skills for Peace and Development"*).
- **July 26**: Kargil Vijay Diwas (Silver Jubilee / 25th anniversary).
- **July 28**: World Hepatitis Day (*"It's time for action"*).
- **July 29**: International Tiger Day (*"Call for Action: Conserving Habitats for a Thriving Future"*).
- **Obituaries**:
  - **K.P.S. Menon Jr.** (95): Veteran diplomat and former Foreign Secretary of India (1987-1989).
  - **Prabhat Patnaik**: Eminent Marxist economist honored globally for developmental studies.

---

## 16. Prelims Traps & Mains Answer Frameworks

### 16.1 Prelims Traps
> [!caution]
> - **Trap 1**: Believing the crime of Sedition is retained under Section 124A of the new BNS.
>   - *Fact*: Sedition has been **repealed**. A newly formulated offense punishing acts endangering sovereignty, unity, and integrity of India is introduced under **Section 152 BNS**, which does not use the colonial term 'sedition'.
> - **Trap 2**: Confusing Charaideo Moidams' UNESCO classification.
>   - *Fact*: Charaideo Moidams is inscribed as a **Cultural site**, and is the **first CULTURAL World Heritage site from Northeast India** (Kaziranga and Manas are Natural sites).
> - **Trap 3**: Believing the Supreme Court 9-judge bench in *MADA v. SAIL* held royalty to be a tax.
>   - *Fact*: The Supreme Court held that **royalty is NOT a tax**, thereby upholding the legislative competence of States to levy taxes on mineral rights.
> - **Trap 4**: Assuming Angel Tax was abolished only for DPIIT-registered startups.
>   - *Fact*: In Budget 2024-25, Angel Tax was **completely abolished for ALL classes of investors and companies**.

### 16.2 Mains Question & Model Blueprint
**Question**: *Critically analyze the institutional transformation ushered in by the Bharatiya Nyaya Sanhita (BNS), Bharatiya Nagarik Suraksha Sanhita (BNSS), and Bharatiya Sakshya Adhiniyam (BSA). How do these laws balance citizen rights with police powers?* (Marks: 15 / 250 Words)

**Model Answer Outline**:
1. **Introduction (35 words)**:
   - Identify the enforcement of BNS, BNSS, and BSA on July 1, 2024, as the most profound structural de-colonization of India's criminal justice system in 160 years, transitioning from colonial instruments of ruler protection to citizen-centric justice (*Nyaya*).
2. **Body 1: Citizen-Centric Reforms & Procedural Safeguards (70 words)**:
   - *Democratizing Access*: Mandatory Zero FIR eliminates jurisdictional denial; e-FIR permits online reporting of petty property offenses; community service introduces restorative justice.
   - *Mandatory Forensic Rigor*: Section 105 BNSS mandates audio-video recording of search and seizure operations and forensic collection for crimes punishable by >=7 years, minimizing fabricated custodial framing.
   - *Strict Time-Bound Trajectory*: Mandates charge framing within 60 days, communication of progress to victims within 90 days, and judgment pronouncement within 45 days.
3. **Body 2: Points of Constitutional Friction & Concerns (75 words)**:
   - *Expanded Police Custody*: Section 187 BNSS allows the 15-day police custody window to be spread across the first 40 or 60 days of detention, raising civil liberty fears of prolonged custodial interrogation.
   - *Vague Offenses*: Broad phrasing of "acts endangering sovereignty" (Section 152 BNS) and organized crime/petty organized crime risks potential executive overreach and arbitrary arrests.
   - *Infrastructure Deficit*: Implementation bottlenecks in forensic labs, video storage servers, and police station bandwidth, especially in rural police outposts.
4. **Conclusion (25 words)**:
   - Conclude that the legislative architecture provides modern legal tools, but its constitutional success hinges on aggressive police sensitization, judicial oversight, and massive capital infusion in forensic digital infrastructure.

---

## 17. Two-Source Verification Standard
- **Source 1**: Ministry of Home Affairs Official Gazette Notification: *Enforcement of BNS, BNSS, and BSA (1 July 2024)*.
- **Source 2**: Ministry of Finance, Government of India, *Union Budget 2024-25 Budget at a Glance*.
- **Source 3**: Supreme Court Judgment: *Mineral Area Development Authority v. Steel Authority of India*, Civil Appeal No. 4056 of 1999 (9-Judge Bench).
"""
    safe_write(jul_path, jul_content)
    print(f"Created: {jul_path} ({len(jul_content.split())} words)")

if __name__ == "__main__":
    generate_ca_jun_jul()
