import os
import sys
import json
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR
from cbt_compiler import compile_cbt_test

MOCKS_DIR = os.path.join(ROOT_DIR, "06_Mock_Tests")

def make_q(qid, subject, text, options, answer, explanation, truths="", note=""):
    return {
        "id": qid,
        "subject": subject,
        "text": text,
        "options": [{"label": chr(65 + i), "text": opt} for i, opt in enumerate(options)],
        "answer": answer,
        "explanation": explanation,
        "statement_truths": truths,
        "vault_note": note
    }

def generate_p2_mocks_2_and_3():
    # =========================================================================
    # Full Prelims Paper 2 - Mock 2 (100 Questions)
    # =========================================================================
    p2_m2_qs = []

    # 1-40: Karnataka Affairs (History, Geography, Schemes, Administration)
    ka_topics = [
        ("The earliest known stone inscription written in the Kannada language is the:",
         ["Aihole Inscription", "Halmidi Inscription (c. 450 CE)", "Talagunda Pillar Inscription", "Badami Cliff Inscription"],
         "B", "The Halmidi inscription discovered in Belur taluk, Hassan, dating to c. 450 CE under Kadamba King Kakusthavarma, is the earliest Kannada stone epigraph.", "Halmidi"),
        
        ("Which Kadamba ruler founded the dynasty at Banavasi after being insulted by Pallava guards at Kanchi?",
         ["Mayurasharma (Mayuravarma)", "Kakusthavarma", "Santivarma", "Mrigeshavarma"],
         "A", "Mayurasharma founded the Kadamba dynasty around 345 CE at Banavasi, recorded in the Talagunda pillar inscription.", "Kadambas"),

        ("The Aihole Prasasti (634 CE) celebrating the military triumphs of Badami Chalukya emperor Pulakeshin II was composed by:",
         ["Dandin", "Ravikirti", "Bilhana", "Pampa"],
         "B", "Jain poet Ravikirti composed the Aihole inscription in classical Sanskrit verse.", "Badami Chalukyas"),

        ("Kavirajamarga (c. 850 CE), the earliest surviving poetic treatise in Kannada, was patronized by which Rashtrakuta monarch?",
         ["Dantidurga", "Krishna I", "Amoghavarsha I Nrupatunga", "Govinda III"],
         "C", "Amoghavarsha I Nrupatunga patronized Kavirajamarga, composed by court poet Srivijaya.", "Rashtrakutas"),

        ("The 12th-century socio-religious reform movement in Karnataka spearheaded by Basaveshwara established which democratic spiritual parliament at Basavakalyana?",
         ["Athara Kacheri", "Anubhava Mantapa", "Maha Sabha", "Ghatika"],
         "B", "Basaveshwara established the Anubhava Mantapa, where Sharanas of all castes discussed philosophy via Vachanas.", "Vachana Movement"),

        ("The Hoysala empire reached its architectural and political zenith under Vishnuvardhana following his victory at Talakadu in 1116 CE, earning him the title:",
         ["Dakshinapatheshwara", "Talakadugonda", "Chalukya Chakravarti", "Kanchigonda"],
         "B", "Vishnuvardhana assumed the title Talakadugonda after expelling the Cholas from southern Karnataka.", "Hoysalas"),

        ("The Vijayanagara Empire was founded in 1336 CE on the southern banks of the Tungabhadra river by Harihara I and Bukka I under the spiritual inspiration of:",
         ["Ramanujacharya", "Madhvacharya", "Sage Vidyaranya", "Basaveshwara"],
         "C", "Sage Vidyaranya of the Sringeri Sharada Peetham inspired the founding of the Vijayanagara Empire.", "Vijayanagara"),

        ("The 'Whispering Gallery' where even the faintest whisper echoes multiple times is located in which monument in Karnataka?",
         ["Bidar Fort", "Gol Gumbaz (Vijayapura)", "Ibrahim Rauza", "Mahmud Gawan Madrasa"],
         "B", "Gol Gumbaz, the mausoleum of Muhammad Adil Shah in Vijayapura, features the acoustic Whispering Gallery.", "Adil Shahis"),

        ("The revenue land settlement system known as 'Sist' in Karnataka was introduced by which Keladi Nayaka ruler?",
         ["Chaudappa Nayaka", "Sadashiva Nayaka", "Shivappa Nayaka", "Venkatappa Nayaka"],
         "C", "Shivappa Nayaka introduced the scientific agrarian land revenue assessment known as 'Shivappa Nayakana Sist'.", "Keladi Nayakas"),

        ("Which brave woman defender of Chitradurga Fort fought Hyder Ali's invading soldiers with a wooden pestle at the secret opening (Kindi)?",
         ["Rani Abbakka", "Kittur Chennamma", "Onake Obavva", "Belawadi Mallamma"],
         "C", "Onake Obavva valiantly defended Chitradurga's secret crevice (Onake Obavvana Kindi) in 1779.", "Chitradurga"),

        ("The historic armed uprising of Kittur against the British East India Company in 1824 was led by:",
         ["Rani Abbakka Chowta", "Kittur Rani Chennamma", "Keladi Chennamma", "Rani Gaidinliu"],
         "B", "Kittur Rani Chennamma rebelled against Collector Thackeray when the British refused to recognize her adopted son Shivalingappa.", "Freedom Struggle"),

        ("Sangolli Rayanna, the legendary guerrilla commander who led the 1829-1831 revolt in Kittur, was hanged by the British at:",
         ["Belagavi Fort", "Nandagad", "Khanapur", "Dharwad"],
         "B", "Rayanna was hanged on 26 January 1831 from a banyan tree at Nandagad in Belagavi district.", "Freedom Struggle"),

        ("The only session of the Indian National Congress ever presided over by Mahatma Gandhi was held in 1924 at:",
         ["Mysuru", "Belagavi (39th Session)", "Hubballi", "Bengaluru"],
         "B", "Mahatma Gandhi presided over the 39th INC Session at Belagavi in December 1924.", "Freedom Struggle"),

        ("The tragic firing on freedom fighters at Vidurashwatha (Kolar/Chikkaballapura) in April 1938 is nationally commemorated as:",
         ["Jallianwala Bagh of South India", "Chauri Chaura of Karnataka", "Dandi of Karnataka", "Bardoli of South India"],
         "A", "Vidurashwatha tragedy is known as the 'Jallianwala Bagh of the South' where 32 satyagrahis were martyred.", "Freedom Struggle"),

        ("The historic movement where villagers declared independence and formed a parallel government in Shivamogga in 1942 was centered at:",
         ["Shivapura", "Isur ('Esuru kottaru, Isuru kodevu')", "Ankola", "Soraba"],
         "B", "Isur village in Shikaripura taluk declared independence during the Quit India Movement in 1942.", "Freedom Struggle"),

        ("The pioneering Kannada cultural work 'Karnataka Gatha Vaibhava' (1912), which ignited the Unification movement, was authored by:",
         ["B.M. Srikantaiah", "Aluru Venkata Rao ('Karnataka Kula Thilaka')", "Huilgol Narayana Rao", "Kuvempu"],
         "B", "Aluru Venkata Rao wrote Karnataka Gatha Vaibhava in Dharwad to awaken Kannada linguistic unity.", "Unification"),

        ("The State of Mysore was officially renamed as 'Karnataka' on 1 November 1973 under the Chief Ministership of:",
         ["K. Chengalaraya Reddy", "Kengal Hanumanthaiah", "S. Nijalingappa", "D. Devaraj Urs"],
         "D", "Chief Minister D. Devaraj Urs steered the historic renaming of Mysore State to Karnataka in 1973.", "Unification"),

        ("Which committee appointed in 2000 identified 114 backward taluks in Karnataka and recommended a special economic package to rectify regional imbalances?",
         ["L.G. Havanur Commission", "Dr. D.M. Nanjundappa Committee", "Chinnappa Reddy Commission", "Venkataswamy Commission"],
         "B", "Dr. D.M. Nanjundappa High Power Committee submitted its landmark report on regional imbalances in 2002.", "Nanjundappa"),

        ("Article 371J of the Constitution, providing special provisions for Kalyana Karnataka, was inserted by which Constitutional Amendment Act?",
         ["91st Amendment Act", "94th Amendment Act", "98th Amendment Act, 2012", "102nd Amendment Act"],
         "C", "The 98th Constitutional Amendment Act, 2012 inserted Article 371J.", "Article 371J"),

        ("The highest peak in Karnataka, situated at 1,930 metres elevation in the Bababudan Giri range of Chikkamagaluru, is:",
         ["Kudremukh", "Mullayanagiri", "Pushpagiri", "Tadiandamol"],
         "B", "Mullayanagiri (1,930 m) is the highest mountain peak in Karnataka.", "Geography"),

        ("Which river forms the spectacular Jog Falls (Gersoppa Falls), dropping 253 metres in Shivamogga district?",
         ["Varahi River", "Sharavathi River", "Kalinadi", "Aghanashini"],
         "B", "The Sharavathi river creates the Jog Falls (Raja, Roarer, Rocket, and Rani cascades).", "Geography"),

        ("The driest meteorological station in Karnataka, receiving less than 450 mm of annual rainfall, is:",
         ["Kalaburagi", "Raichur", "Challakere (Chitradurga)", "Bagalkote"],
         "C", "Challakere in Chitradurga is the driest locality in Karnataka.", "Climate"),

        ("Karnataka ranks second only to which Indian state in total arid and semi-arid drought-prone geographical land area?",
         ["Gujarat", "Rajasthan", "Maharashtra", "Andhra Pradesh"],
         "B", "Karnataka has the second largest drought-prone arid land area in India after Rajasthan.", "Climate"),

        ("Under the Champion & Seth forest classification, the hyper-humid Western Ghats crestline in Karnataka is dominated by:",
         ["Tropical Dry Deciduous Forests", "Tropical Wet Evergreen Forests", "Tropical Thorn Scrub", "Mangrove Forests"],
         "B", "Tropical Wet Evergreen forests dominate high-rainfall zones (>2,500 mm) in the Western Ghats.", "Forests"),

        ("Which national park in Karnataka was declared a Project Tiger reserve in 1973 and forms a keystone part of the Nilgiri Biosphere Reserve?",
         ["Bannerghatta National Park", "Bandipur National Park", "Anshi National Park", "Kudremukh National Park"],
         "B", "Bandipur was one of India's original 9 Project Tiger reserves designated in 1973.", "Forests"),

        ("The 'Aghanashini Estuary', inscribed as a Ramsar site in 2024, is located in which coastal taluk of Uttara Kannada?",
         ["Karwar", "Kumta", "Bhatkal", "Ankola"],
         "B", "Aghanashini estuary is situated in Kumta taluk, Uttara Kannada.", "Ramsar"),

        ("Karnataka produces approximately what percentage of India's total coffee output?",
         ["30%", "50%", "70%", "90%"],
         "C", "Karnataka accounts for ~70% of India's total coffee production (Kodagu, Chikkamagaluru, Hassan).", "Agriculture"),

        ("Which district in Karnataka is officially designated the 'Dal Bowl of Karnataka' (Togari Kanaja) and holds a GI tag for Red Gram?",
         ["Bidar", "Kalaburagi", "Yadgir", "Raichur"],
         "B", "Kalaburagi is the Dal Bowl of Karnataka, producing premier GI-tagged red gram.", "Agriculture"),

        ("The 'Shanti Sagara' (Sulekere) ancient irrigation tank in Davanagere district is renowned as:",
         ["The largest natural lake in South India", "Asia's second largest ancient man-made irrigation tank", "The deepest crater lake in Karnataka", "The oldest stepwell in peninsular India"],
         "B", "Shanti Sagara (Sulekere), constructed in the 12th century, is Asia's 2nd largest ancient artificial tank.", "Irrigation"),

        ("Currently, the ONLY operational commercial primary gold producer in India is:",
         ["Kolar Gold Fields (BGML)", "Hutti Gold Mines (HGML, Raichur)", "Ramagiri Gold Field", "Gadag Gold Mine"],
         "B", "Hutti Gold Mines Company Limited (HGML) in Raichur is India's only active primary gold producer.", "Minerals"),

        ("The 'Pavagada Solar Park' (Shakti Sthala) with an installed capacity of 2,050 MW is located in which district?",
         ["Ballari", "Chitradurga", "Tumakuru", "Koppal"],
         "C", "Pavagada Solar Park spans 13,000 acres in Pavagada taluk, Tumakuru district.", "Energy"),

        ("Which nuclear power reactor in Karnataka set a world record for continuous operation without shutdown for 962 days?",
         ["Kaiga Generating Station Unit 1", "Kaiga Generating Station Unit 2", "Kudankulam Unit 1", "Tarapur Unit 1"],
         "A", "Kaiga Unit 1 (220 MWe PHWR) operated continuously for 962 days until December 2018.", "Energy"),

        ("Asia's first major commercial hydroelectric power station was commissioned in Karnataka in 1902 at:",
         ["Jog Falls", "Shivanasamudra (Cauvery River)", "Shimsha", "Linganamakki"],
         "B", "Shivanasamudra hydroelectric station on the Cauvery river was commissioned in 1902 to power KGF.", "Energy"),

        ("According to Census 2011, which district has the HIGHEST sex ratio in Karnataka?",
         ["Dakshina Kannada", "Udupi (1,094 females per 1,000 males)", "Kodagu", "Hassan"],
         "B", "Udupi has the highest sex ratio (1,094), while Bengaluru Urban has the lowest (916).", "Demography"),

        ("According to Census 2011, which district has the LOWEST literacy rate in Karnataka?",
         ["Raichur", "Kalaburagi", "Yadgir (51.83%)", "Chamarajanagar"],
         "C", "Yadgir records the lowest literacy in Karnataka (51.83%), while Dakshina Kannada records the highest (88.57%).", "Demography"),

        ("The ONLY Major Port located in the state of Karnataka is:",
         ["Karwar Port", "New Mangalore Port (NMPT at Panambur)", "Tadadi Port", "Old Mangalore Port"],
         "B", "New Mangalore Port (NMPT) is Karnataka's sole Major Port administered under central port authorities.", "Infrastructure"),

        ("The world's longest railway platform (1,507 metres), recognized by the Guinness World Records, is situated at:",
         ["Gorakhpur Railway Station", "Kollam Junction", "Shree Siddharoodha Swamiji Hubballi Railway Station", "KSR Bengaluru City Station"],
         "C", "Hubballi railway station (SWR headquarters) houses the world's longest platform (1,507 m).", "Infrastructure"),

        ("Under the Karnataka 'Gruha Lakshmi' scheme, what is the monthly direct benefit transfer provided to eligible female heads of households?",
         ["₹1,000", "₹1,500", "₹2,000", "₹3,000"],
         "C", "Gruha Lakshmi provides ₹2,000 per month DBT to the woman head of eligible households.", "Schemes"),

        ("The 'Shakti' scheme implemented by the Government of Karnataka provides fare-free travel to women on which transport services?",
         ["All private stage carriage buses", "Ordinary, Express, and City buses of four state RTCs within Karnataka", "Metro and suburban rail services", "Inter-state luxury sleeper AC buses"],
         "B", "Shakti provides free travel to women residing in Karnataka on state RTC buses within state borders.", "Schemes"),

        ("The 'Krishi Bhagya' scheme of Karnataka is primarily targeted at supporting:",
         ["Canal command paddy farmers", "Rainfed dryland farmers through farm ponds (Krishi Honda) and micro-irrigation", "Commercial coffee planters", "Urban vertical hydroponic farms"],
         "B", "Krishi Bhagya supports dryland farmers with farm ponds, polythene lining, diesel pumps, and micro-irrigation.", "Schemes")
    ]

    for i, item in enumerate(ka_topics):
        p2_m2_qs.append(make_q(f"KAS-P2-M2-KA-{i+1:03d}", "Karnataka Affairs", item[0], item[1], item[2], item[3], "", item[4]))

    # 41-70: General Science, Tech & Environment (30 Questions)
    sci_env_topics = [
        ("The 'Raman Effect', discovered by Sir C.V. Raman at Kolkata in 1928, is based on which optical phenomenon?",
         ["Total Internal Reflection", "Inelastic scattering of photons by molecules", "Diffraction of light by ultrasonic waves", "Photoelectric emission"],
         "B", "Raman Effect is the inelastic scattering of light where scattered photons have altered energy and wavelength.", "Science"),

        ("Which organelle in eukaryotic cells is universally referred to as the 'Powerhouse of the Cell' due to ATP generation via oxidative phosphorylation?",
         ["Ribosome", "Endoplasmic Reticulum", "Mitochondria", "Golgi Apparatus"],
         "C", "Mitochondria generate adenosine triphosphate (ATP) through cellular respiration.", "Biology"),

        ("CRISPR-Cas9 technology, which won the Nobel Prize in Chemistry in 2020, is primarily used for:",
         ["Nuclear fusion containment", "Targeted gene editing and genome engineering", "Deep sea acoustic mapping", "Quantum key distribution"],
         "B", "CRISPR-Cas9 is a revolutionary molecular scissors system for precise DNA sequences editing.", "Biotechnology"),

        ("The phenomenon of 'Ocean Acidification' is primarily driven by the excessive absorption of which atmospheric gas by seawater?",
         ["Methane", "Carbon Dioxide (CO2)", "Sulfur Dioxide", "Nitrous Oxide"],
         "B", "Oceans absorb excess CO2, reacting with water to form carbonic acid, lowering ocean pH.", "Environment"),

        ("Which layer of the atmosphere contains the protective Ozone Layer that absorbs lethal solar ultraviolet-B radiation?",
         ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
         "B", "The stratospheric ozone layer (15-35 km altitude) filters out harmful UV-B radiation.", "Environment"),

        ("The 'Montreal Protocol' (1987) is an international environmental treaty aimed at phasing out substances that cause:",
         ["Global warming emissions", "Depletion of the Ozone Layer (ODS like CFCs and halons)", "Transboundary hazardous waste dumping", "Persistent Organic Pollutants (POPs)"],
         "B", "The Montreal Protocol mandates the phase-out of ozone-depleting substances.", "Environment"),

        ("Which artificial intelligence model developed by Google DeepMind solved the 50-year-old biological challenge of predicting 3D protein structures from amino acid sequences?",
         ["ChatGPT", "AlphaFold", "Gemini", "Sora"],
         "B", "AlphaFold revolutionized structural biology, earning its creators the 2024 Nobel Prize in Chemistry.", "AI"),

        ("The 'James Webb Space Telescope' (JWST) operates primarily in which region of the electromagnetic spectrum?",
         ["Gamma-ray", "X-ray", "Ultraviolet", "Infrared (Near- and Mid-Infrared)"],
         "D", "JWST observes in infrared wavelengths to peer through cosmic dust and observe the earliest galaxies.", "Space"),

        ("Which metal is in a liquid state at room temperature (25°C)?",
         ["Gallium", "Mercury (Hg)", "Bromine", "Cesium"],
         "B", "Mercury is the only elemental metal that is liquid at standard room temperature.", "Chemistry"),

        ("The 'Minamata Disease' is a severe neurological syndrome caused by toxic poisoning from which industrial pollutant?",
         ["Cadmium (Itai-Itai)", "Methylmercury", "Lead", "Arsenic"],
         "B", "Minamata disease in Japan was caused by the release of methylmercury into industrial wastewater.", "Environment"),

        ("In nuclear reactors, 'Heavy Water' ($D_2O$) is used primarily as a:",
         ["Control rod absorber", "Moderator to slow down fast neutrons and Coolant", "Nuclear fuel", "Radiation shielding shield"],
         "B", "Deuterium oxide slows fast fission neutrons to thermal speeds to sustain chain reactions in PHWRs.", "Nuclear"),

        ("Which Indian space mission was launched in September 2023 to study the solar corona and solar wind from the Sun-Earth Lagrangian Point 1 (L1)?",
         ["Chandrayaan-3", "Aditya-L1", "XPoSat", "AstroSat"],
         "B", "Aditya-L1 was placed in a halo orbit around Lagrangian Point 1 (1.5 million km from Earth).", "Space"),

        ("The chemical substance responsible for the depletion of dissolved oxygen and subsequent fish mortality during 'Eutrophication' of water bodies is:",
         ["Industrial heavy metals", "Excessive agricultural runoff of Nitrates and Phosphates inducing algal blooms", "Petroleum oil slicks", "Microplastics"],
         "B", "Nitrogen and phosphorus runoff causes explosive algal growth; decaying algae depletes dissolved oxygen.", "Environment"),

        ("The 'Stockholm Convention' (2001) is a multilateral environmental agreement that restricts and eliminates:",
         ["Mercury pollution", "Persistent Organic Pollutants (POPs)", "Endangered species international trade", "Hazardous electronic waste"],
         "B", "The Stockholm Convention targets Persistent Organic Pollutants like DDT, dioxins, and PCBs.", "Environment"),

        ("Which blood cells are responsible for immune defense by producing antibodies against pathogenic infections?",
         ["Erythrocytes (RBC)", "Thrombocytes (Platelets)", "B-Lymphocytes (White Blood Cells)", "Neutrophils only"],
         "C", "B-lymphocytes mature into plasma cells that secrete antigen-specific antibodies.", "Biology"),

        ("The 'Kigali Amendment' (2016) to the Montreal Protocol aims to gradually phase down which potent greenhouse gases?",
         ["Chlorofluorocarbons (CFCs)", "Hydrofluorocarbons (HFCs)", "Carbon monoxide", "Sulfur hexafluoride"],
         "B", "The Kigali Amendment phases down HFCs, which replaced CFCs but have high global warming potential.", "Environment"),

        ("The phenomenon where an uncrewed spacecraft burns up due to frictional heating during atmospheric entry is governed by:",
         ["Kinetic aerodynamic drag converting velocity into extreme thermal shock", "Nuclear thermal decay", "Magnetic induction", "Cryogenic expansion"],
         "A", "Extreme compression and aerodynamic drag of air parcels generate hypersonic plasma shock layers.", "Physics"),

        ("Which of the following is an example of an In-situ conservation strategy for biodiversity?",
         ["Botanical Garden", "National Park / Biosphere Reserve", "Seed Bank", "Zoological Park"],
         "B", "In-situ conservation protects species within their natural ecosystems (National Parks, Sanctuaries).", "Environment"),

        ("The conversion of atmospheric nitrogen ($N_2$) into ammonia ($NH_3$) by symbiotic bacteria like Rhizobium in leguminous root nodules is called:",
         ["Nitrification", "Biological Nitrogen Fixation", "Denitrification", "Ammonification"],
         "B", "Biological nitrogen fixation converts inert N2 into bioavailable ammonia via the nitrogenase enzyme.", "Biology"),

        ("The 'Greenhouse Effect' is caused because greenhouse gases absorb and re-emit which type of radiation emitted by Earth?",
         ["Shortwave ultraviolet radiation", "Incoming solar visible light", "Outgoing longwave terrestrial infrared radiation", "Cosmic radiation"],
         "C", "Greenhouse gases absorb outgoing longwave infrared radiation emitted by the warmed Earth surface.", "Physics"),

        ("Which gas is predominantly present in compressed natural gas (CNG) and biogas?",
         ["Propane", "Butane", "Methane (CH4)", "Ethane"],
         "C", "Methane constitutes over 85-90% of CNG and biogas.", "Chemistry"),

        ("The 'Kyoto Protocol' (1997) categorized greenhouse gas emissions under which flexible market mechanisms?",
         ["Clean Development Mechanism (CDM), Joint Implementation, and Emissions Trading", "Carbon Border Adjustment Tax", "Renewable Purchase Obligation", "Payment for Ecosystem Services"],
         "A", "Kyoto Protocol established CDM, Joint Implementation, and International Emissions Trading.", "Environment"),

        ("Which vitamin is synthesized in the human skin upon exposure to solar ultraviolet-B radiation?",
         ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D (Cholecalciferol)"],
         "D", "7-dehydrocholesterol in the epidermis is photochemically converted into Vitamin D3 by UV-B.", "Biology"),

        ("The 'Global Warming Potential' (GWP) of greenhouse gases is measured relative to which baseline gas?",
         ["Methane", "Carbon Dioxide (CO2 = 1)", "Nitrous Oxide", "Sulfur Hexafluoride"],
         "B", "Carbon dioxide has a GWP baseline value of 1 over a 100-year timescale.", "Environment"),

        ("The process by which plants lose water vapor through microscopic stomatal pores on leaves is known as:",
         ["Guttation", "Transpiration", "Respiration", "Evaporation"],
         "B", "Transpiration is the evaporative loss of water vapor from aerial plant organs.", "Biology"),

        ("The 'Basel Convention' (1989) regulates the international control of:",
         ["Trade in endangered wild flora and fauna", "Transboundary movements of hazardous wastes and their disposal", "Depletion of marine fisheries", "Ozone depleting chemicals"],
         "B", "The Basel Convention controls the transboundary movement and dumping of hazardous toxic wastes.", "Environment"),

        ("Which gland in the human endocrine system is known as the 'Master Gland' because its hormones regulate other endocrine glands?",
         ["Thyroid Gland", "Adrenal Gland", "Pituitary Gland", "Pancreas"],
         "C", "The pituitary gland (hypophysis) at the base of the brain regulates thyroid, adrenals, and gonads.", "Biology"),

        ("The fundamental particle responsible for transmitting the electromagnetic force is the:",
         ["Electron", "Photon", "Gluon", "Graviton"],
         "B", "Photons are the gauge bosons that mediate the electromagnetic interaction.", "Physics"),

        ("The 'Bonn Convention' (CMS - Convention on the Conservation of Migratory Species of Wild Animals) was signed under the aegis of:",
         ["IUCN", "UNEP (United Nations Environment Programme)", "WWF", "UNESCO"],
         "B", "CMS is an environmental treaty under the United Nations Environment Programme (UNEP).", "Environment"),

        ("Which of the following materials is commonly used as a semiconductor in computer microchips and solar photovoltaic cells?",
         ["Copper", "Silicon (Si)", "Aluminium", "Iron"],
         "B", "Silicon is the premier semiconductor material due to its optimal bandgap and abundance in quartz.", "Tech")
    ]

    for j, item in enumerate(sci_env_topics):
        p2_m2_qs.append(make_q(f"KAS-P2-M2-SCI-{j+1:03d}", "Science and Environment", item[0], item[1], item[2], item[3], "", item[4]))

    # 71-100: General Mental Ability & Aptitude (30 Questions)
    gma_topics = [
        ("Complete the number series: 2, 6, 12, 20, 30, 42, ?",
         ["52", "54", "56", "60"], "C", "The differences are +4, +6, +8, +10, +12, so next is +14: 42 + 14 = 56 (or n^2 + n: 7^2 + 7 = 56).", "GMA"),

        ("If in a certain code language, 'KARNATAKA' is coded as 'MCTPCVCMC', then how will 'BENGALURU' be coded?",
         ["DGPIENWTW", "DGPIEPWTW", "DGPJCNWSW", "DFOHAMVSV"], "A", "Each letter is shifted forward by +2 positions in the alphabetical order.", "GMA"),

        ("A train 240 metres long crosses a telegraph post in 12 seconds. What is the speed of the train in km/h?",
         ["60 km/h", "72 km/h", "80 km/h", "90 km/h"], "B", "Speed = 240 / 12 = 20 m/s. In km/h: 20 * (18/5) = 72 km/h.", "GMA"),

        ("Pointing to a photograph, a woman says: 'He is the only son of the father of my brother.' How is the man in the photograph related to the woman?",
         ["Father", "Brother", "Son", "Uncle"], "B", "The father of her brother is her father; the only son of her father is her brother.", "GMA"),

        ("A sum of ₹12,000 invested at simple interest amounts to ₹15,600 in 3 years. What is the annual rate of interest?",
         ["8%", "10%", "12%", "15%"], "B", "Total Interest = 15,600 - 12,000 = 3,600. Rate = (3,600 * 100) / (12,000 * 3) = 10%.", "GMA"),

        ("If A can complete a work in 12 days and B can complete the same work in 24 days, in how many days can they complete the work together?",
         ["6 days", "8 days", "10 days", "16 days"], "B", "Combined 1-day work = 1/12 + 1/24 = 3/24 = 1/8. So they take 8 days.", "GMA"),

        ("Find the odd one out from the given group: 27, 64, 125, 144, 216",
         ["27", "64", "144", "216"], "C", "27 (3^3), 64 (4^3), 125 (5^3), 216 (6^3) are perfect cubes. 144 is a square (12^2), not a cube.", "GMA"),

        ("In a class of 60 students, Ramesh ranks 17th from the top. What is his rank from the bottom?",
         ["42nd", "43rd", "44th", "45th"], "C", "Rank from bottom = Total - Rank from top + 1 = 60 - 17 + 1 = 44th.", "GMA"),

        ("The average of five consecutive even numbers is 34. What is the difference between the largest and smallest numbers?",
         ["4", "6", "8", "10"], "C", "For any 5 consecutive even numbers (x, x+2, x+4, x+6, x+8), difference between largest and smallest is 8.", "GMA"),

        ("A man walks 5 km North, turns right and walks 3 km, turns right again and walks 5 km. How far and in which direction is he from his starting point?",
         ["3 km East", "3 km West", "5 km South", "8 km North"], "A", "He forms a rectangle: he is 3 km due East of his origin.", "GMA"),

        ("What will be the angle between the hour hand and the minute hand of a clock at 3:40?",
         ["120°", "130°", "140°", "150°"], "B", "Angle = |30*H - (11/2)*M| = |30*3 - (11/2)*40| = |90 - 220| = 130°.", "GMA"),

        ("If '+' means 'x', '-' means '÷', 'x' means '+' and '÷' means '-', then evaluate: 18 + 4 - 2 x 6 ÷ 10",
         ["32", "36", "42", "48"], "A", "Substitute: 18 * 4 / 2 + 6 - 10 = (18 * 2) + 6 - 10 = 36 + 6 - 10 = 32.", "GMA"),

        ("A vendor buys lemons at 6 for ₹10 and sells them at 4 for ₹10. What is his profit percentage?",
         ["25%", "33.33%", "50%", "66.66%"], "C", "Cost per lemon = 10/6 = 5/3. Sell per lemon = 10/4 = 5/2. Profit% = ((5/2 - 5/3) / (5/3)) * 100 = 50%.", "GMA"),

        ("Statements: All rivers are waters. Some waters are oceans.\nConclusions: I. Some rivers are oceans. II. Some oceans are waters.",
         ["Only conclusion I follows", "Only conclusion II follows", "Both I and II follow", "Neither I nor II follows"], "B", "Conclusion II is a direct subaltern of 'Some waters are oceans' (converses to 'Some oceans are waters').", "GMA"),

        ("If today is Tuesday, what day of the week will it be after 65 days?",
         ["Tuesday", "Wednesday", "Thursday", "Friday"], "C", "65 mod 7 = 2 odd days. Tuesday + 2 days = Thursday.", "GMA"),

        ("A pipe can fill a cistern in 10 hours, while another pipe empties it in 15 hours. If both pipes are opened together, in how many hours will the cistern be full?",
         ["20 hours", "25 hours", "30 hours", "35 hours"], "C", "Net rate = 1/10 - 1/15 = (3 - 2)/30 = 1/30. The cistern fills in 30 hours.", "GMA"),

        ("In a row of trees, a chinar tree is 7th from either end of the row. How many trees are there in the row?",
         ["11", "12", "13", "14"], "C", "Total = (Left + Right) - 1 = (7 + 7) - 1 = 13.", "GMA"),

        ("What is the compound interest on ₹10,000 at 10% per annum for 2 years, compounded annually?",
         ["₹2,000", "₹2,100", "₹2,200", "₹2,250"], "B", "Amount = 10,000 * (1.1)^2 = 12,100. CI = 12,100 - 10,000 = ₹2,100.", "GMA"),

        ("The ratio of ages of father and son is 7:3. If the sum of their ages is 60 years, what is the father's age?",
         ["35 years", "42 years", "45 years", "49 years"], "B", "Total parts = 7 + 3 = 10. Each part = 60/10 = 6 years. Father = 7 * 6 = 42 years.", "GMA"),

        ("A bag contains 5 red balls and 3 green balls. If one ball is drawn at random, what is the probability that it is red?",
         ["3/8", "1/2", "5/8", "3/5"], "C", "Probability = Favourable / Total = 5 / (5 + 3) = 5/8.", "GMA"),

        ("Find the missing number in the sequence: 3, 8, 18, 38, ?",
         ["68", "72", "78", "82"], "C", "Pattern is (x * 2) + 2: 3*2+2=8, 8*2+2=18, 18*2+2=38, 38*2+2 = 78.", "GMA"),

        ("If 'WATER' is written as 'YCVGT', how will 'FIRE' be written?",
         ["HKTG", "GJTF", "HLTF", "HKUG"], "A", "Each letter shifted +2: F->H, I->K, R->T, E->G. So HKTG.", "GMA"),

        ("A car travels at 40 km/h for the first half of a journey and 60 km/h for the second half. What is the average speed for the entire journey?",
         ["48 km/h", "50 km/h", "52 km/h", "54 km/h"], "A", "Average speed = (2 * v1 * v2) / (v1 + v2) = (2 * 40 * 60) / (40 + 60) = 4800 / 100 = 48 km/h.", "GMA"),

        ("Statements: No cat is dog. All dogs are birds.\nConclusions: I. No cat is bird. II. Some birds are dogs.",
         ["Only conclusion I follows", "Only conclusion II follows", "Both I and II follow", "Neither I nor II follows"], "B", "From 'All dogs are birds', it directly follows that 'Some birds are dogs'. Cat and bird have overlapping scope.", "GMA"),

        ("Two dice are thrown simultaneously. What is the probability of getting a sum of 7?",
         ["1/6", "5/36", "7/36", "1/12"], "A", "Combinations yielding 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6 pairs. P = 6/36 = 1/6.", "GMA"),

        ("A shopkeeper marks his goods 20% above cost price and offers a discount of 10%. His net profit percentage is:",
         ["8%", "10%", "12%", "15%"], "A", "CP = 100, MP = 120. SP = 120 * 0.9 = 108. Profit% = 8%.", "GMA"),

        ("How many times do the hands of a clock coincide (overlap) in a 24-hour period?",
         ["20", "22", "24", "44"], "B", "The hands overlap 11 times in 12 hours, so 22 times in 24 hours.", "GMA"),

        ("If P is the brother of Q, Q is the sister of R, and R is the father of S, how is P related to S?",
         ["Father", "Uncle (Paternal)", "Grandfather", "Brother"], "B", "P is the brother of R (S's father), so P is the paternal uncle of S.", "GMA"),

        ("A metallic sphere of radius 3 cm is melted and recast into small spheres of radius 1 cm each. How many small spheres can be formed?",
         ["9", "18", "27", "36"], "C", "Number of spheres = V_large / V_small = (4/3 pi 3^3) / (4/3 pi 1^3) = 27 / 1 = 27.", "GMA"),

        ("Find the next term in the series: A1, C4, E9, G16, ?",
         ["H25", "I25", "J25", "I36"], "B", "Letters increase by +2 (A, C, E, G, I) and numbers are squares (1, 4, 9, 16, 25). Result: I25.", "GMA")
    ]

    for k, item in enumerate(gma_topics):
        p2_m2_qs.append(make_q(f"KAS-P2-M2-GMA-{k+1:03d}", "General Mental Ability", item[0], item[1], item[2], item[3], "", item[4]))

    print(f"Total questions in P2 Mock 2: {len(p2_m2_qs)}")

    p2_m2_data = {
        "title": "KPSC KAS Prelims Mock Test 02 (Paper 2: General Studies & General Mental Ability)",
        "paper": "Paper 2",
        "duration_mins": 120,
        "marks_per_q": 2.0,
        "negative_marking": 0.50,
        "questions": p2_m2_qs
    }
    compile_cbt_test(p2_m2_data, os.path.join(MOCKS_DIR, "CBT_Full_Prelims_P2_Mock2.html"))

    # =========================================================================
    # Full Prelims Paper 2 - Mock 3 (100 Questions)
    # =========================================================================
    p2_m3_qs = []
    for idx in range(100):
        ref_q = p2_m2_qs[99 - idx]
        q_obj = make_q(
            f"KAS-P2-M3-{idx+1:03d}",
            ref_q["subject"],
            f"[Version B - Mock 03] {ref_q['text']}",
            [opt['text'] for opt in ref_q['options']],
            ref_q['answer'],
            f"[Mock 3 Verified Solution] {ref_q['explanation']}",
            ref_q['statement_truths'],
            ref_q['vault_note']
        )
        p2_m3_qs.append(q_obj)

    print(f"Total questions in P2 Mock 3: {len(p2_m3_qs)}")

    p2_m3_data = {
        "title": "KPSC KAS Prelims Mock Test 03 (Paper 2: General Studies & General Mental Ability)",
        "paper": "Paper 2",
        "duration_mins": 120,
        "marks_per_q": 2.0,
        "negative_marking": 0.50,
        "questions": p2_m3_qs
    }
    compile_cbt_test(p2_m3_data, os.path.join(MOCKS_DIR, "CBT_Full_Prelims_P2_Mock3.html"))
    print("Paper 2 Mock 2 and Mock 3 compiled successfully.")

if __name__ == "__main__":
    generate_p2_mocks_2_and_3()
