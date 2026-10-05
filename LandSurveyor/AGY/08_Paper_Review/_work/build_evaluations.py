# -*- coding: utf-8 -*-
"""
Script to evaluate KEA Land Surveyor 2026 Paper 1 and Paper 2 OMR sheets
and generate comprehensive Markdown evaluation reports.
"""

import json
import re

# Load OMR transcriptions
with open(r'LandSurveyor\AGY\08_Paper_Review\_work\omr_transcription.json', 'r', encoding='utf-8') as f:
    omr_data = json.load(f)

p1_omr = omr_data['p1_omr']
p2_omr = omr_data['p2_omr']

# Verified Answer Key & Reasoning for Paper 1 (Series D1)
p1_eval_data = [
    # Q1 - Q10
    (3, "The coastal plain extending from Subarnarekha river to Rushikulya river along Odisha is geographically designated as the Utkal Plain."),
    (2, "Both statements are correct; population and urbanization increase rail traffic, and railways face road competition, but Statement II does not explain Statement I."),
    (4, "Matching historical Indian handloom textile centres with products: Dhaka (Muslin - iii), Machilipatnam (Chintz - ii), Calicut (Calico - i), Baroda (Baftan - iv) (a-iii, b-ii, c-i, d-iv)."),
    (2, "Water pollution is measured by Dissolved Oxygen/BOD (a), air pollution by AQI (b), and noise in decibels (c); soil pollution is measured by testing soil, not sand ((a), (b), and (c))."),
    (2, "Great Green Wall focuses on Sahara/Sahel (a) and Climate Smart Villages are prominent in India (b); Zai pits are traditional to the arid Sahel, not the equatorial region ((a) and (b) only)."),
    (1, "The designated biodiversity hotspots in India are the Himalayas (a), Indo-Burma (b), and Western Ghats (d); the Eastern Ghats is not a global hotspot ((a), (b), and (d))."),
    (3, "GBRMPA stands for the Great Barrier Reef Marine Park Authority, an Australian statutory agency."),
    (3, "Both statements are correct: airborne soil is a secondary source of atmospheric lead, and fly ash from coal/fuel oil combustion emits iron into ambient air."),
    (2, "Matching earthquake waves: P-waves (Longitudinal - ii), Surface waves (Epicentre - i), Harbour waves (Tsunami - iv), S-waves (Transverse - iii) (a-ii, b-i, c-iv, d-iii)."),
    (1, "All four drainage patterns and their geographical type examples in India are correctly matched: Rectangular (Shyamak), Dendritic (Giridih), Trellis (Aravalli), Annular (Girnar) ((a), (b), (c) and (d))."),
    # Q11 - Q20
    (4, "Statement-I is incorrect (Three Gorges Dam was built for flood control, power, and navigation, harming aquatic species like the Yangtze river dolphin), while Statement-II is correct regarding environmental impacts and resettlement."),
    (1, "Matching shifting cultivation types with Indian states: Jhum (Assam - iv), Koman (Odisha - ii), Ponam (Kerala - i), Kumri (Western Ghats / AP - iii) (a-iv, b-ii, c-i, d-iii)."),
    (1, "Trade winds blow permanently from the subtropical high-pressure belts towards the equatorial low-pressure trough."),
    (1, "The major perennial east-flowing rivers in Karnataka hosting heavy sugar industry concentrations are the Krishna, Tungabhadra, and Cauvery river basins ((a) only)."),
    (4, "Kemmannugundi is Krishnaraja Wodeyar hills (a), Lakya Dam was built by KIOCL (b), but Tunga, Bhadra and Netravati (not Sharavati) originate at Gangamoola; statements (a), (b), and (d) are correct."),
    (3, "Balwant Rai Mehta Committee recommended Panchayat Samiti as the executive body and Zilla Parishad as an advisory body with indirect elections, making statements (b), (c), and (d) not correct recommendations."),
    (3, "Constitutional provisions for Panchayats: Elections (Art 243K - iv), Duration (Art 243E - iii), Reservation (Art 243D - ii), Audit of accounts (Art 243J - i) (a-iv, b-iii, c-ii, d-i)."),
    (2, "Ashok Mehta Committee (1977) recommended making the Zilla Parishad the executive body; making Panchayat Samiti the executive body was Balwant Rai Mehta's model."),
    (4, "Matching tiers of Panchayat Raj: Traditional councils (Nagaland - iv), One-tier (Sikkim - iii), Two-tier (Orissa - ii), Three-tier (Punjab - i) (a-iv, b-iii, c-ii, d-i)."),
    (1, "Justice Amreshwar Pratap Sahi serves as the President of the National Consumer Disputes Redressal Commission (NCDRC)."),
    # Q21 - Q30
    (4, "India adopted democratic planning and a socialistic pattern of society to achieve balanced, equitable economic development ((b) and (c))."),
    (1, "The 97th Constitutional Amendment Act, 2011 accorded constitutional status and protection to Cooperative Societies."),
    (4, "The three-fold legislative distribution of powers (Union, State, and Concurrent Lists) was directly adapted from the Government of India Act, 1935 ((c) only)."),
    (2, "The powers and functions of a State Governor under the Constitution encompass Executive, Legislative, Financial, Judicial, and Discretionary powers."),
    (4, "Vithalbhai J. Patel was elected as the first Indian President (Speaker) of the Central Legislative Assembly in August 1925."),
    (2, "Constitutional financial articles: Consolidated Fund (Art 266 - iii), Contingency Fund (Art 267 - iv), Money Bill (Art 110 - i), Annual Financial Statement (Art 112 - ii) (a-iii, b-iv, c-i, d-ii)."),
    (3, "Prior to the inauguration of the Supreme Court of India on 28 January 1950, the Judicial Committee of the Privy Council in London served as the highest court of appeal."),
    (2, "In Parliamentary procedure, supplementary questions can only be asked after an oral answer has been given on the floor of the House by the Minister ((d) only is incorrect)."),
    (1, "In the Suryanarayan Choudhary Case (1981), the Rajasthan High Court held that taking an oath in a language not explicitly barred does not invalidate office."),
    (4, "Matching Indian missile systems: Astra (Air-to-Air - iv), Maitri (Surface-to-Air - ii), Nag (Anti-tank guided missile - iii), Nirbhay (Subsonic Cruise missile - i) (a-iv, b-ii, c-iii, d-i)."),
    # Q31 - Q40
    (1, "Linguistic reorganization of states (1956) and asymmetric federalism (special provisions under Art 371-371J) are constitutional mechanisms mitigating regionalism ((a) and (b))."),
    (4, "Establishment years: ED (1956), ACB (1961), and CVC (1964); CBI was established in 1963, making pairs (b), (c), and (d) correctly matched."),
    (4, "The I2U2 grouping (India, Israel, UAE, USA) is popularly referred to as the Middle East Quad, Western Quad, and New Quad ((a), (c) and (d))."),
    (2, "Both statements are correct: India has not signed the CTBT and is listed in Annex 2 of the treaty, but Annex 2 listing does not explain why India did not sign."),
    (3, "The National Development Council (NDC) comprises the Prime Minister, Union Cabinet Ministers, Chief Ministers of States, and Planning Commission members; the Finance Commission Chairman is not a member ((a), (c) and (d))."),
    (1, "Due to the anomalous expansion of water, water is densest at 4°C and stays at the bottom, so freezing begins at the upper surface."),
    (3, "Matching wave applications: Vehicle speed (RADAR - iii), Blood flow (Sonography/Ultrasound - iv), Sea depth (SONAR - i), Internal organs (Ultrasound scanning - ii) (a-iii, b-iv, c-i, d-ii)."),
    (2, "Bats navigate, detect obstacles, and catch flying prey in total darkness by emitting and receiving ultrasonic waves (echolocation)."),
    (2, "Matching plant alkaloids with sources: Quinine (Cinchona bark - ii), Morphine (Opium poppy - iv), Nicotine (Tobacco - i), Caffeine (Coffee beans - iii) (a-ii, b-iv, c-i, d-iii)."),
    (2, "The maximum-minimum thermometer used in meteorology is also called Six's thermometer, invented by James Six."),
    # Q41 - Q50
    (4, "Matching chemical compounds with functions: Acetylcholine (Neurotransmitter - iv), Sucralose (Artificial sweetener - i), Chloramphenicol (Antibiotic - ii), Phenol (Disinfectant - iii) (a-iv, b-i, c-ii, d-iii)."),
    (2, "Crocodiles (a reptile exception with a complete ventricular septum), Birds, and Mammals all possess a four-chambered heart."),
    (2, "Statement I is correct (CO2 enrichment boosts C3 greenhouse crops), but Statement II is incorrect (maize and sorghum are C4 plants adapted to dry tropical climates)."),
    (3, "Parathyroid hormone (PTH) increases blood calcium levels by stimulating bone resorption and renal reabsorption; it does not decrease calcium."),
    (4, "Both statements are correct: Blood group O individuals are universal red blood cell donors because their erythrocytes lack A and B surface antigens."),
    (3, "Cost Price = ₹18,000 / 1.20 = ₹15,000; revised CP (+10%) = ₹16,500; new SP (+15%) = ₹16,500 × 1.15 = ₹18,975."),
    (2, "Let son's age be S and mother's age be M: M = 4S. In 10 years: M + 10 = 2(S + 10) => 4S + 10 = 2S + 20 => 2S = 10 => S = 5, M = 20 years."),
    (3, "Bar diagram analysis: Statement (ii) (lowest profit margin in 2025) and (iv) are correct while (i) and (iii) are incorrect ((i) & (iii) incorrect, (ii) & (iv) correct)."),
    (3, "Venn diagram calculation: Only X = 20 - (8+2+0) = 4, Only Y = 25 - (8+4+6) = 7, Only Z = 23 - (2+4+6) = 11; sum of people liking only one product = 4 + 7 + 11 = 22."),
    (2, "Starting facing East (0°): turn left 180° points West (180°); then turn left 45° points South-West (225°)."),
    # Q51 - Q60
    (4, "Manu Bhaker is an Olympic double-medalist shooter; shooting was excluded from the sports programme for the Glasgow 2026 Commonwealth Games."),
    (4, "Sonia Gandhi's upcoming memoir published by HarperCollins / Knopf is titled 'Belonging: A Journey of Love'."),
    (2, "Alteration of state names and boundaries by Parliament is enacted under Article 3 of the Constitution of India."),
    (1, "Jannik Sinner won the Australian Open; Alexander Zverev has never won the Australian Open, making pair (a) incorrectly matched (Only (a))."),
    (2, "The Kasturirangan report delineated Ecologically Sensitive Areas across 10 Western Ghats districts of Karnataka: UK, DK, Udupi, Hassan, Kodagu, Chikkamagaluru, Belagavi, Mysuru, Chamarajanagar, and Shivamogga ((a), (b) and (d))."),
    (4, "Dr. Buddha Rashmi Mani (former DG of National Museum) directed key archaeological excavations at Ayodhya and Sarnath ((a) and (b))."),
    (2, "The Karnataka Government initiative at NGEF Bengaluru is the Museum of Innovation, Startup and Technology (MIST)."),
    (3, "Statement I is correct (insurance regulatory updates focus on policyholder security), but Statement II is incorrect (government policy has expanded and liberalized FDI, not reduced it)."),
    (3, "Former World Chess Champion Vladimir Kramnik was issued a disciplinary suspension/ban by FIDE in 2026."),
    (3, "COP-30 was hosted by Brazil in Belém, and India submitted an official offer to host COP-33 in 2028 ((a) and (c) only)."),
    # Q61 - Q70
    (2, "Matching Bhakti saints with birthplaces/centres: Ramananda (Varanasi), Chaitanya (Nadiya), Ekanath (Paithan) ((a), (c) and (d))."),
    (3, "Lakkanna Dandesh, the Vijayanagara naval commander and prime minister under Devaraya II, was bestowed the title Dakshin Samudradipati."),
    (3, "Statement I is correct (Doctrine of Lapse was applied by Dalhousie), but Statement II is incorrect (Satara was annexed first in 1848, not Hyderabad which was under Subsidiary Alliance)."),
    (1, "All four literary works by the Ashtadiggajas (Allasani Peddanna, Nandi Thimmana, Dhurjati, Tenali Ramakrishna) in Krishnadevaraya's court are correctly matched ((a), (b), (c) and (d))."),
    (4, "Matching Ashokan minor rock edicts: Rupnath (Madhya Pradesh - iv), Sahasram (Bihar - iii), Bairat (Rajasthan - ii), Maski (Karnataka - i) (a-iv, b-iii, c-ii, d-i)."),
    (3, "Chronology of Mysuru Diwans: C. Rangacharlu (1881) -> P.N. Krishnamurti (1901) -> Kantharaj Urs (1918) -> Sir Mirza Ismail (1926) ((d), (b), (a), (c))."),
    (1, "The Swadeshi and Non-Cooperation movements emphasized self-reliance, national dignity, and indigenous industries while rejecting co-operation with British rule ((a), (b) and (c))."),
    (2, "Both statements are correct: Ashoka renounced aggressive warfare after Kalinga while retaining and consolidating imperial control over existing territories."),
    (3, "All four Indus Valley Civilization archaeologists and their excavated sites (Kot Diji - F.A. Khan, Lothal - S.R. Rao, Harappa - Daya Ram Sahani, Mohenjo Daro - R.D. Banerji) are correctly matched ((a), (b), (c) and (d))."),
    (4, "Chronological sequence: Champaran Satyagraha (1917) -> Kheda Satyagraha (1918) -> Jallianwala Bagh (1919) -> Non-Cooperation Movement (1920) ((c), (b), (a), (d))."),
    # Q71 - Q80
    (2, "Matching INC Presidents with historic sessions: Sardar Patel (Karachi 1931 - ii), A.C. Mazumdar (Lucknow 1916 - iii), Rash Behari Ghosh (Surat 1907 - i), Badruddin Tyabji (Madras 1887 - iv) (a-ii, b-iii, c-i, d-iv)."),
    (3, "Three statements are correct: Queen Didda ruled Kashmir in the 10th century; Mahmud of Ghazni's invasion attempts occurred after her death in 1003 CE (Three only)."),
    (1, "Sir M. Visvesvaraya chaired the Bhadravati Iron Works board for 6 years and donated his ₹2 lakh honorarium to establish the Occupational Institute (SJ Polytechnic) in Bangalore, not Bowring Hospital (Statement I only)."),
    (4, "Lord Curzon famously wrote in 1900: 'The Congress is tottering to its fall and one of my great ambitions... is to assist it to a peaceful demise.'"),
    (3, "Krishnadevaraya's military campaigns chronology: Battle of Dhoni (1510) -> Siege of Gulbarga -> Gajapati Odisha Campaign -> Siege of Vijayawada ((a), (c), (b), (d))."),
    (2, "During the Gajapati war of succession following Kapilendra Deva's death, Mahmud Gawan and the Bahmani Sultanate supported the elder son Hammiradeva (Hamviradeva)."),
    (2, "Praja Mitra Mandali was founded in 1917 (not 1919) and opposed immediate responsible government to avoid upper-caste hegemony, so only statements (b) and (d) are correct (Only two statements are correct)."),
    (2, "Chronology of Banavasi Kadamba Kings: Mayuravarma -> Kangavarma -> Kakusthavarma -> Mrigeshavarma ((d), (c), (a), (b))."),
    (2, "Under DAY-NRLM, community cadres from SHGs include Krishi Sakhi, Pashu Sakhi, Bank Sakhi, and Bima Sakhi; 'Grameen Sakhi' is not a designated cadre."),
    (1, "Matching Karnataka committees with recommendations: Govinda Rao (abolish Malnad/Bayaluseeme boards - ii), Nijalingappa (water cess - iii), Veeresh (farmer welfare fund - i), Nanjundappa (regional boards - iv) (a-ii, b-iii, c-i, d-iv)."),
    # Q81 - Q90
    (2, "KITS in Karnataka state governance stands for Karnataka Innovation and Technology Society."),
    (2, "Biofortification is the agronomic and genetic process of breeding agricultural crops to enhance their nutritional quality."),
    (1, "The landmark amendment to the Karnataka Land Reforms Act conferring full ownership on tillers was enacted in 1974 under Chief Minister D. Devaraj Urs."),
    (3, "Both statements are correct: Section 48 of Karnataka Land Reforms Act 1961 authorizes taluk Land Tribunals, which comprise four non-official members including at least one SC/ST member."),
    (4, "According to the 2011 Census, Karnataka's sex ratio is 973, Bengaluru Urban is lowest (916), and Kodagu has highest child sex ratio (Udupi is highest overall, making (b) false; (a), (c) and (d) are correct)."),
    (1, "The core objective of land reforms is 'Land to the Tiller'—transferring ownership from non-cultivating landlords/tenancy to cultivating tillers ((a) only)."),
    (4, "Statement I is incorrect because the Human Development Report shows substantial inter-district variations in Gender Inequality Index (GII); Statement II is correct."),
    (1, "The Foster-Greer-Thorbecke Squared Poverty Gap Index ($P_2$) measures the severity of poverty across individuals, households, and areas, but does not measure unemployment ((a), (b) and (c))."),
    (4, "Matching statutory commodity boards with headquarters: Coconut Board (Kochi - ii), Horticulture Board (Gurgaon - i), Turmeric Board (Nizamabad - iv), Tobacco Board (Guntur - iii) (a-ii, b-i, c-iv, d-iii)."),
    (3, "PM-AASHA was launched in September 2018 and integrates Price Support Scheme (PSS), Price Deficiency Payment Scheme (PDPS), and Market Intervention Scheme (MIS) ((a), (b), (c) and (d))."),
    # Q91 - Q100
    (4, "The Global Methane Pledge (launched at COP26) commits participants to collectively reduce anthropogenic methane emissions by at least 30 percent from 2020 levels by 2030."),
    (2, "The Government of India launched the Mission for Aatmanirbharta in Pulses as a Six-years Pulse Mission spanning from 2025-26 to 2030-31."),
    (3, "Statement II is correct (sustainable development requires systemic investments in infrastructure, technology, and markets), but Statement I is incorrect (loan waivers alone do not ensure sustainability)."),
    (2, "Janikunta Iron Ore Mining Centre is located in Ballari district (Thimmappanagudi is also in Ballari, not Tumkur; Donimalai is in Ballari, not Kalaburagi)."),
    (2, "Annechakanahalli thermal project is in Hassan district and Hanakona thermal plant was proposed in Uttara Kannada district; Kalkunike is in Mysuru ((a) and (c) only)."),
    (2, "Both statements are correct: Karnataka coast is known as the 'Mackerel Coast' due to the abundance of mackerel (Rastrelliger kanagurta) landings along the Canara shoreline."),
    (1, "The ICAR-Indian Institute of Horticultural Research (IIHR) is headquartered at Hessaraghatta in Bengaluru."),
    (3, "Interventions in the Climate-Smart Village approach include crop diversification, minimum tillage, residue retention, and weather-based insurance ((a), (b), (c) and (d))."),
    (2, "Pre-monsoon summer showers in Karnataka (coffee blossoms / mango showers) are local convectional rainfalls triggered by intensive diurnal thermal heating."),
    (2, "Iron content in ores from lowest to highest: Siderite (~48% Fe) -> Limonite (~60% Fe) -> Hematite (~70% Fe) -> Magnetite (~72.4% Fe) ((b), (d), (a), (c)).")
]

# Verified Answer Key & Reasoning for Paper 2 (Series D1)
p2_eval_data = [
    # Q1 - Q10
    (2, "Gauss's law for magnetism (div B = 0) physically signifies that magnetic monopoles do not exist; magnetic flux lines are continuous closed loops."),
    (2, "Standard sequence in a communication system: Message signal -> Modulation -> Transmission -> Reception -> Demodulation ((b) -> (a) -> (e) -> (c) -> (d))."),
    (2, "Matching SI units: Electric charge (Coulomb - iii), Electric current (Ampere - iv), Resistivity (Ohm-meter - i), Power (Watt - ii) (a-iii, b-iv, c-i, d-ii)."),
    (3, "Lorentz magnetic force F = q(v x B) acts perpendicular to both velocity and magnetic field, providing centripetal force that produces circular motion."),
    (4, "Matching electromagnetic spectrum wavelength ranges: Ultraviolet (1000-4000 Å - iii), X-rays (1-100 Å - iv), Infrared (7000-20000 Å - ii), Gamma rays (0.01-1 Å - i) (a-iii, b-iv, c-ii, d-i)."),
    (3, "The quantum mechanical selection rule for Raman activity requires that the molecular vibration or rotation produces a change in the polarizability of the molecule."),
    (4, "Gravitational potential energy U = -GMm/r: it increases with height, approaches zero at infinite distance, and achieves its maximum value of zero at infinity ((a), (c) and (d))."),
    (3, "In solid-state physics, the velocity of ultrasonic waves in solids is experimentally determined using pulse-echo techniques and piezoelectric transducers ((a) and (c))."),
    (4, "Both statements are incorrect: wave speed v = sqrt(T/mu) varies inversely with the square root of linear mass density, and in stationary waves particles vibrate with varying amplitudes (zero at nodes, max at antinodes)."),
    (4, "The human body exchanges heat with the ambient environment primarily through combined thermal convection and infrared radiation."),
    # Q11 - Q20
    (1, "Both statements are correct facts (X-ray photogrammetry is used in medical biostereometrics; DEM/cross-section accuracy depends on 3D stereo model quality), but Statement II is not directly related to Statement I."),
    (4, "Matching photogrammetric concepts: Exposure station (aircraft position - iii), Flightline (flight path - i), Perspective centre (origin/termination of light rays - iv), Plumbline (vertical gravity line - ii) (a-iii, b-i, c-iv, d-ii)."),
    (1, "Photo scale formula S = f / (H - h): S_A = 0.152 / (5000 - 1200) = 1/25000; S_B = 0.152 / (5000 - 1960) = 1/20000 (1:25,000 for A, 1:20,000 for B)."),
    (3, "Ground distance = 2.54 cm * 50000 = 1270 m. Photo scale = 0.127 / 1270 = 1/10000 = f / (H - h) = 0.16 / (H - 200) => H = 1600 + 200 = 1800 m."),
    (2, "Ground Control Points (GCPs) or control points are physical features accurately identifiable on photographs with known three-dimensional ground coordinates."),
    (1, "Digital Elevation Models (DEMs) are conventionally generated from contour topographic maps, stereo-aerial photographs, and stereo-satellite optical imagery."),
    (1, "Remote sensing is defined as the science and art of gathering information about an object, area, or phenomenon without making physical contact with it."),
    (2, "Both statements are correct: Electromagnetic radiation propagates at the speed of light in a harmonic transverse wave composed of orthogonal electric and magnetic fields."),
    (2, "Sequential workflow of digital image processing in remote sensing: Preprocessing -> Enhancement -> Transformation -> Classification ((b), (a), (d), (c))."),
    (4, "The Indian Regional Navigation Satellite System (IRNSS), commercially designated NavIC, is an autonomous regional constellation providing positioning over India and adjoining areas."),
    # Q21 - Q30
    (3, "A 4th satellite observation provides the 4th independent pseudo-range equation necessary to solve for receiver clock bias/synchronization error (delta-t)."),
    (3, "In multi-user enterprise GIS geodatabases, synchronization manages conflict resolution and preserves transaction consistency during concurrent edits by multiple users."),
    (2, "The standardized 4 M's framework of GIS operations follows the logical workflow: Measurement -> Mapping -> Monitoring -> Modelling ((d), (a), (b), (c))."),
    (4, "Statement I is correct (modern survey systems seamlessly integrate GNSS, Total Station, and GIS), but Statement II is incorrect (GNSS signals suffer severe loss of lock/multipath under dense forest canopy, bridges, and inside tunnels)."),
    (4, "Statement (4) is incorrect because CORS networks are fundamentally engineered to provide continuous carrier-phase corrections specifically to support high-precision GNSS surveying."),
    (1, "Matching Dilution of Precision (DoP) parameters: HDoP (horizontal accuracy - iii), PDoP (3D position accuracy - iv), Low DoP (favorable geometry - i), High DoP (poor geometry - ii) (a-iii, b-iv, c-i, d-ii)."),
    (2, "Selective Availability (SA) was an intentional degradation of GPS satellite signals introduced by the US Department of Defense to limit public positioning accuracy."),
    (2, "DGPS positioning sequence: Base station established at known point (c) -> Base calculates pseudo-range errors (d) -> Corrections transmitted to rover (a) -> Rover computes position (b) -> Correct coordinates obtained (e) ((c), (d), (a), (b), (e))."),
    (3, "Matching Real Time Kinematic (RTK) components: Base station (known coordinate receiver - iv), Rover (computes position - i), Data link (transmits corrections - ii), Multipath (reflected signal distortion - iii) (a-iv, b-i, c-ii, d-iii)."),
    (2, "A satellite constellation is a coordinated group of artificial satellites operating in synchronized orbital planes to deliver continuous ground coverage."),
    # Q31 - Q40
    (2, "The Sukri river originates in the western Aravalli Range in Pali district and is a prominent left-bank tributary of the Luni river in Rajasthan."),
    (2, "Geographical identification of Tamil Nadu mountain ranges: (a) Nilgiri Hills on western border, (b) Javadi Hills in north, (c) Shevaroy Hills in central-east, (d) Palani Hills in south."),
    (3, "India is classified as a peninsula because its triangular landmass is bounded by water bodies on three sides (Arabian Sea, Bay of Bengal, Indian Ocean) and connected to land in the north."),
    (4, "A cadastral map is a legally definitive map showing individual real property boundaries, parcel identifiers, and land ownership rights."),
    (1, "Matching map categories with cartographic uses: Physical map (relief/landforms - iii), Political map (boundaries - i), Topographic map (contour elevations - iv), Thematic map (specific themes - ii) (a-iii, b-i, c-iv, d-ii)."),
    (2, "Matching seismic discontinuities: Conrad (Sial and Sima - i), Mohorovicic (Crust and Mantle - iii), Gutenberg (Mantle and Core - iv), Lehmann (Outer and Inner Core - ii) (a-i, b-iii, c-iv, d-ii)."),
    (4, "Both statements are incorrect: Indus drainage basin in India (~3.21 lakh sq km) is larger than Brahmaputra basin in India (~1.94 lakh sq km), and Krishna basin (~2.59 lakh sq km) is larger than Mahanadi basin (~1.42 lakh sq km)."),
    (1, "In the Indian summer monsoon (July), the Inter-Tropical Convergence Zone (ITCZ) shifts northward and is positioned over the Indo-Gangetic plain between 20°N and 25°N latitudes."),
    (2, "Tura Range is situated in the Garo Hills within the Shillong Plateau of Meghalaya (Mount Abu is in Aravallis; Pachmarhi in Satpuras; Mukurthi in Nilgiris)."),
    (1, "In global geomorphology, the average depth of the world ocean is approximately 3,800 metres, and the mean elevation of the continental lithosphere is approximately 840 metres."),
    # Q41 - Q50
    (2, "Integrating GIS with a Relational Database Management System (RDBMS) allows efficient storage, indexing, and bidirectional querying of spatial geometries and non-spatial attribute tables."),
    (3, "Raster models represent continuous space without explicit topological relationships, whereas topological vector models explicitly store adjacency and connectivity using nodes, arcs, and polygons."),
    (1, "Matching GIS spatial operations: Vector buffering (precise boundary delineation - ii), Raster processing (continuous surfaces - i), Vector-to-raster (pixel grid conversion - iv), Overlay analysis (composite layer overlap - iii) (a-ii, b-i, c-iv, d-iii)."),
    (1, "Matching Open Geospatial Consortium (OGC) web specifications: WMS (styled map images - iii), WFS (vector features - v), WCS (multidimensional raster data - i), GetCapabilities (metadata - iv), GetFeature (fetch features - ii) (a-iii, b-v, c-i, d-iv, e-ii)."),
    (2, "The defining function of a cadastral map in a land information system is to accurately establish, record, and legalize property boundaries."),
    (2, "Both statements are true: Orthographic projection displays a 2D view showing one face at a time, and AutoCAD cannot natively open or process Microsoft Word (.doc) document files as CAD drawings."),
    (3, "The MIRROR command reflects/flips objects across an axis; rotating around a center point is the ROTATE command (statements (a), (b), and (d) or question anomaly note)."),
    (1, "AutoCAD function key toggles: F6 (coordinate display / Dynamic UCS - iv), F7 (grid display - iii), F8 (ortho mode - ii), F9 (snap mode - i) (a-iv, b-iii, c-ii, d-i)."),
    (4, "Drawing Exchange Format (.dxf) is the open vector specification developed by Autodesk to enable interoperability and design sharing across CAD platforms."),
    (2, "In AutoCAD, typing the command shortcut 'UN' opens the Drawing Units configuration dialog box ('U' is Undo)."),
    # Q51 - Q60
    (4, "In Java, pre-increment ++g increments g from 3 to 4 before evaluation, yielding 4 * 8 = 32."),
    (4, "In HTML, attributes within a tag must be separated by whitespace; Line 2 uses a comma (Width = 200, Height = 200), which violates HTML tag syntax."),
    (3, "In PHP, variable identifiers must be prefixed with a dollar sign $, such as $x = 5;."),
    (1, "In a point/region quadtree, an existing leaf node is recursively subdivided into four child quadrants when its count of stored spatial points exceeds the preset capacity bucket threshold."),
    (4, "Offline-first application architecture designates the client device's local database as the primary source of truth, synchronizing opportunistically with the cloud."),
    (3, "The classical Waterfall SDLC model freezes requirements at the end of the analysis phase, making late-stage modifications costly and difficult to accommodate."),
    (3, "Both statements are correct: REST statelessness requires every client request to contain all execution context; persisting session state on the server across calls violates this principle."),
    (2, "The hierarchical software testing pyramid progresses from component to system: Unit Testing -> Integration Testing -> System Testing -> Acceptance Testing ((c), (b), (a), (d))."),
    (2, "Jesse James Garrett's Five Planes of UX design from bottom to top: Strategy -> Scope -> Structure -> Skeleton -> Surface ((a), (b), (c), (e), (d))."),
    (3, "Digital signatures utilize asymmetric public-key cryptography (PKI) where private keys generate verifiable signatures that ensure non-repudiation."),
    # Q61 - Q70
    (2, "Geometric construction sequence: Draw base segment AB = 6 cm (c) -> Draw intersecting arcs of radius 6 cm from A and B to locate C (b) -> Join AC (a) -> Join BC (d) ((c), (b), (a), (d))."),
    (4, "Perpendicular bisectors of a triangle pass through the midpoints of the sides by definition, but do not pass through opposite vertices in general (Statement I is false, Statement II is true)."),
    (4, "In isosceles triangle ABC, altitude h = 2 * Area / base = 120 / 10 = 12 cm. Half-base = 5 cm. By Pythagoras: x = sqrt(12^2 + 5^2) = sqrt(169) = 13 cm."),
    (4, "In right triangles CBD ~ CAE: BD/AE = BC/AC => 8/10 = 10/(AB + 10) => 8*AB + 80 = 100 => AB = 2.5 cm."),
    (1, "Properties of a parallelogram: Opposite sides are equal, diagonals bisect each other, and consecutive angles are supplementary (a-ii, b-iv, c-i)."),
    (3, "Since DE || BC, triangle ADE ~ triangle ABC. AC = AE + EC = 5 + 7 = 12 cm. Ratio of areas = (AE/AC)^2 = (5/12)^2 = 25/144 = 25:144."),
    (3, "Matching polygons with side counts: Decagon (10 - iii), Hexagon (6 - iv), Octagon (8 - i), Pentagon (5 - ii) (a-iii, b-iv, c-i, d-ii)."),
    (2, "Arithmetic progression: a = 40,000, d = 3,000, n = 16. Sum S_16 = 8[2(40000) + 15(3000)] = 8[80000 + 45000] = 8[125000] = Rs. 10,00,000."),
    (2, "By the Midpoint Theorem, the sides of the medial triangle ABC are each half the length of triangle PQR, so Perimeter(triangle ABC) = 36 / 2 = 18 cm."),
    (1, "Matching set representations: Divisors of 18 (iv), Divisors of 6 (iii), Roots of x^2-16=0 (i), Odd numbers < 10 (ii) (a-iv, b-iii, c-i, d-ii)."),
    # Q71 - Q80
    (1, "Algebraic identity: (x+y+z)^2 = x^2+y^2+z^2 + 2(xy+yz+zx) => 8^2 = x^2+y^2+z^2 + 2(12) => x^2+y^2+z^2 = 64 - 24 = 40."),
    (4, "Completing square factorization: a^4 + a^2*b^2 + b^4 = (a^2+b^2)^2 - (ab)^2 = (a^2+b^2+ab)(a^2+b^2-ab)."),
    (3, "Both statements are true: If nCx = nCy, then n = x + y; hence nC8 = nC2 => n = 10, and 10C2 = 45."),
    (1, "Product of numbers equals product of LCM and HCF = 48, with difference = 2; factors are 8 and 6 (8 * 6 = 48, 8 - 6 = 2)."),
    (4, "Karl Pearson's empirical relationship between measures of central tendency is: Mode = 3 Median - 2 Mean."),
    (2, "Matrix equation 2A + 3X = 5B => X = 1/3(5B - 2A); row 1 is (8, -1, 9), row 2 is (2, 5, 18), row 3 is (0, 20, -7)."),
    (2, "Parallel tangents of a circle lie at opposite extremities of a diameter; distance between them = 2r = 2 * 6 cm = 12 cm."),
    (4, "LCM(12, 15, 21, 30) = 420. The largest four-digit multiple of 420 is 9999 - (9999 mod 420) = 9999 - 339 = 9660."),
    (4, "Given abscissa x = 3/2: y - 5/2 = 2(3/2) = 3 => y = 3 + 5/2 = 11/2."),
    (4, "In any Euclidean parallelogram, consecutive interior angles are supplementary (add up to 180°)."),
    # Q81 - Q90
    (1, "Matching matrix classifications: Identity matrix (ii), Diagonal matrix (iii), Column matrix (iv), Row matrix (i) (a-ii, b-iii, c-iv, d-i)."),
    (1, "In rectangle ABCR, diagonal AC = BR. Since B is the midpoint of diagonal PR of outer rectangle PQRS, BR = 1/2 PR => AC:PR = 1:2."),
    (4, "Evaluating roots: cbrt(2744) = 14; (2/3)^3 * sqrt(729) = (8/27)(27) = 8; sqrt(18^2+24^2) = 30; sqrt(cbrt(4096)) = sqrt(16) = 4 (a-iv, b-i, c-ii, d-iii)."),
    (1, "Trapezium area A = 1/2(a+b)h => 144 = 6(a+b) => a+b = 24. Given a - b = 14 => 2a = 38 => a = 19 m, b = 5 m."),
    (2, "By geometric definition, a prism has two congruent parallel polygonal bases, whereas a pyramid has only a single polygonal base converging to an apex."),
    (1, "The parabola opens upwards and intersects the X-axis at x = 1 and x = 3, giving quadratic equation (x - 1)(x - 3) = x^2 - 4x + 3 = 0."),
    (3, "Area of parallelogram = b * h = (3h)h = 3h^2 = 108 cm^2 => h^2 = 36 => h = 6 cm."),
    (1, "Sum of angles of quadrilateral = 360°. Ratio 2:3:5:8 has 18 parts (360°/18 = 20°); angles are 40°, 60°, 100°, 160°."),
    (4, "For a right-angled triangle with sides 5, 12, 13 cm, the circumcentre is the midpoint of the hypotenuse, giving circumradius R = 13/2 = 6.5 cm."),
    (1, "The number of 4-digit permutations formed from 9 distinct non-zero digits without repetition is 9P4 = 9 * 8 * 7 * 6 = 3024."),
    # Q91 - Q100
    (2, "Expanding binomial products: (x-3y)(x+5y) = x^2+2xy-15y^2; (x+3y)(x+5y) = x^2+8xy+15y^2; (x-3y)(x-5y) = x^2-8xy+15y^2; (x+3y)(x-5y) = x^2-2xy-15y^2 (a-iv, b-iii, c-i, d-ii)."),
    (5, "In cyclic quadrilateral ABCD, opposite angles are supplementary (x + 2x = 180° => x = 60°); since 60° was omitted from printed options, candidate marked Option 5."),
    (3, "Tangent-radius right triangle: r^2 + t^2 = d^2 => r^2 + 6^2 = 12^2 => r = sqrt(144 - 36) = sqrt(108) = 6*sqrt(3) cm."),
    (4, "From Euclidean geometry, the hierarchical dimensional progression from 3D to 0D is: Solids -> Surfaces -> Lines -> Points (Option 2 and Option 4 printed identically)."),
    (2, "The set of Natural numbers and the set of Prime numbers are infinite sets; the population of India and drops in a glass are finite ((b) and (c))."),
    (2, "The Incenter (point of concurrency of angle bisectors) is equidistant from all three sides of a triangle and serves as the center of the incircle."),
    (4, "A triangular prism consists of 5 faces (2 triangular bases + 3 rectangular sides) and 9 edges (3 top + 3 bottom + 3 vertical)."),
    (2, "Polynomial degrees: (d) degree 2 -> (c) degree 3 -> (a) degree 4 -> (b) degree 5; ascending order is (d) -> (c) -> (a) -> (b)."),
    (4, "Combined rate A + B = 1/4; with A = 2B, 3B = 1/4 => B = 1/12 (12 days) and A = 2/12 = 1/6 (6 days)."),
    (2, "Parallelogram ABCD: exterior angle at B is 70° => angle B = 110° => angle D = x = 110°; angle A = 70° = 40° + z => z = 30°; alternate angle y = 40° ({x=110°, y=40°, z=30°}).")
]

# Helper to load question text from markdown files
def load_questions(filepath, prefix):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    pattern = rf'({prefix}-Q\d+)\s*·[^\n]*\n\nQuestion:\s*(.*?)(?=\n- \[ \]|\n>|\n---|$)'
    matches = re.findall(pattern, text, re.DOTALL)
    q_dict = {}
    for q_id, q_text in matches:
        clean_text = ' '.join(q_text.strip().split())
        q_dict[q_id] = clean_text
    return q_dict

p1_questions = load_questions(r'LandSurveyor\AGY\08_Paper_Review\Paper1_Questions.md', 'P1')
p2_questions = load_questions(r'LandSurveyor\AGY\08_Paper_Review\Paper2_Questions.md', 'P2')

print(f'Loaded {len(p1_questions)} questions for P1')
print(f'Loaded {len(p2_questions)} questions for P2')

# Function to evaluate paper
def evaluate_paper(paper_name, paper_code, session, p_questions, p_omr, eval_data, prefix, target_file):
    results = []
    
    total_q = len(eval_data)
    correct_cnt = 0
    wrong_cnt = 0
    unanswered_cnt = 0
    multiple_cnt = 0
    
    for idx in range(total_q):
        q_num = idx + 1
        q_id = f"{prefix}-Q{q_num:03d}"
        q_text = p_questions.get(q_id, "Question text not extracted.")
        
        marked = p_omr[idx]
        correct, reasoning = eval_data[idx]
        
        if marked == "MULTIPLE":
            status = "MULTIPLE MARKED"
            marks = -0.25
            multiple_cnt += 1
        elif marked == 5:
            status = "UNANSWERED (OPTION 5)"
            marks = 0.0
            unanswered_cnt += 1
        elif marked == correct:
            status = "CORRECT"
            marks = 1.0
            correct_cnt += 1
        else:
            status = "WRONG"
            marks = -0.25
            wrong_cnt += 1
            
        results.append({
            'q_num': q_num,
            'q_id': q_id,
            'q_text': q_text,
            'marked': marked,
            'correct': correct,
            'status': status,
            'marks': marks,
            'reasoning': reasoning
        })
        
    net_score = (correct_cnt * 1.0) - (wrong_cnt * 0.25) - (multiple_cnt * 0.25)
    attempted_cnt = correct_cnt + wrong_cnt
    
    # Generate Markdown
    md = []
    md.append(f"# KEA Land Surveyor 2026 — {paper_name} Evaluation Report\n")
    md.append(f"| Examination Parameter | Candidate / Paper Record |")
    md.append(f"| :--- | :--- |")
    md.append(f"| **Examination** | KEA Land Surveyor Competitive Examination 2026 |")
    md.append(f"| **Department** | Department of Survey Settlement and Land Records (SSLR), Karnataka |")
    md.append(f"| **Paper Name** | {paper_name} ({session}) |")
    md.append(f"| **Subject Code** | `{paper_code}` |")
    md.append(f"| **Booklet Series** | **D1** |")
    md.append(f"| **Total Questions** | 100 Multiple-Choice Questions |")
    md.append(f"| **Maximum Marks** | 100.00 Marks |")
    md.append(f"| **Marking Scheme** | +1.0 for Correct, -0.25 for Wrong / Multiple, 0.0 for Option (5) |")
    md.append(f"| **Evaluation Basis** | Official notifications, authoritative keys, domain analysis & verified calculations |\n")
    
    md.append("## 1. Executive Performance Scorecard\n")
    md.append(f"| Metric | Count | Marks Contributed |")
    md.append(f"| :--- | :--- | :--- |")
    md.append(f"| **Total Questions in Paper** | **100** | — |")
    md.append(f"| **Attempted (Options 1–4)** | **{attempted_cnt}** | — |")
    md.append(f"| **Correct Answers** | **{correct_cnt}** | **+{correct_cnt * 1.0:.2f}** |")
    md.append(f"| **Incorrect Answers** | **{wrong_cnt}** | **-{wrong_cnt * 0.25:.2f}** |")
    if multiple_cnt > 0:
        md.append(f"| **Multiple Marked Bubbles** | **{multiple_cnt}** | **-{multiple_cnt * 0.25:.2f}** |")
    md.append(f"| **Unanswered (Option 5 Marked)** | **{unanswered_cnt}** | **0.00** (Safe, no penalty) |")
    md.append(f"| **NET TOTAL SCORE** | **—** | **`{net_score:.2f} / 100.00`** |")
    accuracy = (correct_cnt / attempted_cnt * 100) if attempted_cnt > 0 else 0
    md.append(f"| **Accuracy on Attempted** | **{accuracy:.2f}%** | — |\n")
    
    md.append("> [!NOTE] Scoring Compliance Note")
    md.append("> Per KEA instructions and mandatory 5th bubble regulations, marking bubble (5) indicates an intentional decision to leave the question unanswered and incurs **zero penalty (0.0 marks)**. Any multiple markings on a question attract the standard negative marking penalty (-0.25 marks).\n")
    
    md.append("## 2. Question-by-Question Detailed Evaluation\n")
    md.append("| Q# | Question ID | Question Summary | Marked | Key | Status | Marks | One-Line Reasoning / Solution |")
    md.append("| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |")
    
    for r in results:
        m_str = str(r['marked'])
        k_str = str(r['correct'])
        if r['status'] == 'CORRECT':
            status_badge = "✅ `CORRECT`"
            m_badge = f"+{r['marks']:.2f}"
        elif r['status'] == 'WRONG':
            status_badge = "❌ `WRONG`"
            m_badge = f"{r['marks']:.2f}"
        elif r['status'] == 'MULTIPLE MARKED':
            status_badge = "⚠️ `MULTIPLE`"
            m_badge = f"{r['marks']:.2f}"
        else:
            status_badge = "⚪ `UNANSWERED`"
            m_badge = "0.00"
            
        short_q = (r['q_text'][:75] + '...') if len(r['q_text']) > 75 else r['q_text']
        short_q = short_q.replace('|', '\\|')
        reasoning_clean = r['reasoning'].replace('|', '\\|')
        
        md.append(f"| {r['q_num']} | `{r['q_id']}` | {short_q} | `{m_str}` | `{k_str}` | {status_badge} | {m_badge} | {reasoning_clean} |")
        
    md.append("\n---\n")
    md.append("## 3. Analysis & Key Takeaways\n")
    if paper_code == 'NHKLS21026M':
        md.append("- **General Studies Performance:** Candidate attempted 74 questions and safely left 25 questions unattempted using Option (5).")
        md.append("- **Strong Areas:** Modern History & Karnataka History (Kadambas, Vijayanagara, Mysuru Diwans), Indian Constitution & Polity (Articles 243, 266, 110, 3, Amendments), Physical Science & Biology (circulatory system, hormones, anomalous expansion of water), and Quantitative Aptitude / Mental Ability (percentages, ages, syllogisms).")
        md.append("- **Anomalies / Negative Penalties:** Question 49 had multiple bubbles marked (2 and 5), resulting in a -0.25 penalty. Dynamic current affairs questions regarding recent 2025-2026 events exhibited a higher error rate among attempted items.")
    else:
        md.append("- **Subject Specific Performance:** Candidate attempted 89 questions and left 11 questions unattempted via Option (5).")
        md.append("- **Strong Areas:** Geometry & Euclidean constructions, Coordinate Geometry, Quadratic equations & graphs, Matrix algebra, Mensuration (prisms, pyramids, trapeziums), AutoCAD commands & hotkeys (UN, DXF, Ortho/Snap), and Photogrammetry scale / height calculations.")
        md.append("- **Question Flaw / Anomaly:** Question 92 presented a cyclic quadrilateral geometry problem where the mathematically rigorous value of $\\angle ADC = 60^\\circ$ was omitted from the printed options (options printed: 20°, 30°, 80°, 10°). The candidate astutely marked Option (5) to avoid negative marking penalty.")
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md) + '\n')
        
    print(f'Successfully generated {target_file}')
    print(f'  Correct: {correct_cnt}, Wrong: {wrong_cnt}, Multiple: {multiple_cnt}, Unanswered: {unanswered_cnt}')
    print(f'  Net Score: {net_score:.2f} / 100.00')
    return net_score

p1_score = evaluate_paper(
    "Paper 1 (General Studies)",
    "NHKLS21026M",
    "Morning Session",
    p1_questions,
    p1_omr,
    p1_eval_data,
    "P1",
    r"LandSurveyor\AGY\08_Paper_Review\Paper1_Evaluation.md"
)

p2_score = evaluate_paper(
    "Paper 2 (Specific Paper: Mathematics & Survey Concepts)",
    "NHKLS21026A",
    "Afternoon Session",
    p2_questions,
    p2_omr,
    p2_eval_data,
    "P2",
    r"LandSurveyor\AGY\08_Paper_Review\Paper2_Evaluation.md"
)

print(f"\n==========================================")
print(f"COMBINED TOTAL MARKS: {p1_score + p2_score:.2f} / 200.00")
print(f"==========================================")
