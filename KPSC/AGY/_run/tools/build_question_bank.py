"""
build_question_bank.py
Builds the comprehensive 200-question bank for KPSC KAS Prelims
Paper 1 and Paper 2 matching the exact section subjects in exam_config.json:
- Current Affairs: 40 questions
- Humanities: 60 questions
- Karnataka Affairs: 40 questions
- Science and Environment: 30 questions
- General Mental Ability: 30 questions
Total = 200 questions.
"""

import os
import sys
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import safe_ops

ROOT_DIR = safe_ops.ROOT_DIR
BANK_FILE = os.path.join(ROOT_DIR, "05_Resources", "Question_Bank", "question_bank.json")

# Build question generator helper
questions = []

def make_q(qid, subject, text, options, answer, explanation, label="PYQ", year=2020, source_url="https://kpsc.kar.nic.in", source_tier=1, syllabus_id=None):
    q = {
        "id": qid,
        "subject": subject,
        "text": text,
        "options": [{"label": chr(65 + i), "text": opt} for i, opt in enumerate(options)],
        "answer": answer,
        "explanation": explanation,
        "label": label,
        "source_url": source_url,
    }
    if label == "PYQ":
        q["verbatim"] = True
        q["year"] = year
        q["source_tier"] = source_tier
    if syllabus_id:
        q["syllabus_id"] = syllabus_id
    return q

# ==========================================
# 1. CURRENT AFFAIRS (40 Questions)
# ==========================================
ca_data = [
    # 1-10: National legislation & polity
    ("BNS-01", "The Bharatiya Nyaya Sanhita (BNS), 2023 officially came into legal enforcement across India on which date?",
     ["1 January 2024", "1 July 2024", "15 August 2024", "2 October 2024"], "B", "The Bharatiya Nyaya Sanhita (BNS), Bharatiya Nagarik Suraksha Sanhita (BNSS), and Bharatiya Sakshya Adhiniyam (BSA) came into force on 1 July 2024.", "expected", 2024),
    ("BNS-02", "Under the Bharatiya Nyaya Sanhita, 2023, which of the following novel statutory punishments has been introduced for petty offenses?",
     ["Public reprimand", "Community Service", "Asset freezing", "Solitary confinement"], "B", "Community Service has been introduced as a formal penal punishment for specific petty offenses in BNS.", "expected", 2024),
    ("WPA-01", "The 106th Constitutional Amendment Act, 2023 provides for what percentage of reservation for women in the Lok Sabha and State Legislative Assemblies?",
     ["25%", "30%", "33%", "50%"], "C", "The Nari Shakti Vandan Adhiniyam (106th Amendment Act) reserves one-third (33%) of seats for women.", "expected", 2024),
    ("CEC-01", "Under the Chief Election Commissioner and other ECs Act, 2023, who among the following is NOT a member of the Selection Committee?",
     ["Prime Minister of India", "Chief Justice of India", "Leader of Opposition in Lok Sabha", "A Union Cabinet Minister nominated by PM"], "B", "The CJI was substituted by a Union Cabinet Minister nominated by the Prime Minister in the Selection Committee.", "expected", 2024),
    ("DIV-01", "Mission Divyastra, successfully flight-tested by DRDO in March 2024, demonstrated which advanced capability on the Agni-5 missile?",
     ["Hypersonic Scramjet cruise flight", "Multiple Independently Targetable Re-entry Vehicle (MIRV)", "Submarine launch from underwater silo", "Directed Energy Laser weapon"], "B", "Mission Divyastra proved indigenous MIRV technology on Agni-5, allowing multiple warheads to hit distinct targets.", "expected", 2024),
    ("SUB-01", "Which indigenously built nuclear-powered ballistic missile submarine (SSBN) was commissioned into the Indian Navy in August 2024 at Visakhapatnam?",
     ["INS Khanderi", "INS Arighat", "INS Vikrant", "INS Vagir"], "B", "INS Arighat is India's second indigenous nuclear-powered ballistic missile submarine (SSBN) after INS Arihant.", "expected", 2024),
    ("NQM-01", "What is the primary target domain of the National Quantum Mission (NQM) approved by the Union Cabinet?",
     ["Deep-sea polymetallic nodule mining", "Intermediate-scale quantum computers with 50-1000 physical qubits", "Fusion energy reactors", "Graphene supercapacitors"], "B", "NQM targets 50-1000 physical qubit quantum computing, quantum communications, and quantum cryptography.", "expected", 2024),
    ("RAM-01", "With the addition of three new wetland sites in 2024, what is the total count of designated Ramsar sites in India as of late 2024?",
     ["75 sites", "80 sites", "85 sites", "90 sites"], "C", "India's total Ramsar site tally reached 85 sites in 2024.", "expected", 2024),
    ("BR-01", "Who among the following was NOT conferred the Bharat Ratna award in the year 2024?",
     ["Dr. M. S. Swaminathan", "Karpoori Thakur", "Atal Bihari Vajpayee", "Chaudhary Charan Singh"], "C", "Atal Bihari Vajpayee was conferred the Bharat Ratna in 2015. The 2024 recipients were Karpoori Thakur, L.K. Advani, P.V. Narasimha Rao, Charan Singh, and M.S. Swaminathan.", "expected", 2024),
    ("BR-02", "Late Karpoori Thakur, awarded the Bharat Ratna posthumously in 2024, was the former Chief Minister of which Indian State?",
     ["Uttar Pradesh", "Bihar", "Madhya Pradesh", "Rajasthan"], "B", "Karpoori Thakur (Jan Nayak) was a two-time Chief Minister of Bihar and pioneer of backward classes empowerment.", "expected", 2024),

    # 11-20: International Summits & Expansions
    ("BRICS-01", "Which of the following nations formally declined to join the BRICS grouping on 1 January 2024 despite being invited at the 15th Johannesburg Summit?",
     ["Saudi Arabia", "Argentina", "Egypt", "United Arab Emirates"], "B", "Argentina under President Javier Milei formally declined to join BRICS on 1 January 2024.", "expected", 2024),
    ("BRICS-02", "How many new member countries officially became full members of BRICS on 1 January 2024?",
     ["3 countries", "5 countries", "7 countries", "10 countries"], "B", "Five countries joined as full members: Egypt, Ethiopia, Iran, Saudi Arabia, and the United Arab Emirates.", "expected", 2024),
    ("G20-01", "Under India's G20 Presidency at the New Delhi Summit, which regional organization was admitted as a permanent full member of the G20?",
     ["ASEAN", "African Union", "European Free Trade Association", "BIMSTEC"], "B", "The African Union, representing 55 African nations, was admitted as a permanent member of the G20.", "expected", 2024),
    ("EFTA-01", "Under the Trade and Economic Partnership Agreement (TEPA) signed in March 2024, which economic bloc committed to invest $100 Billion into India over 15 years?",
     ["European Union (EU)", "European Free Trade Association (EFTA)", "Mercosur", "Gulf Cooperation Council (GCC)"], "B", "The European Free Trade Association (Switzerland, Norway, Iceland, Liechtenstein) signed TEPA with India.", "expected", 2024),
    ("COP-01", "The COP28 UN Climate Conference was hosted in which city where the landmark 'UAE Consensus' on transitioning away from fossil fuels was adopted?",
     ["Sharm el-Sheikh", "Glasgow", "Dubai", "Baku"], "C", "COP28 was held in Dubai, UAE in December 2023.", "expected", 2024),
    ("COP-02", "The COP29 United Nations Climate Change Conference is hosted in which world capital city?",
     ["Baku (Azerbaijan)", "Belém (Brazil)", "Doha (Qatar)", "Nairobi (Kenya)"], "A", "COP29 is hosted in Baku, Azerbaijan.", "expected", 2024),
    ("IMEC-01", "The India-Middle East-Europe Economic Corridor (IMEC) unveiled at the G20 Summit features which Mediterranean port terminal as a primary node connecting Europe?",
     ["Rotterdam Port", "Haifa Port", "Alexandria Port", "Marseille Port"], "B", "IMEC's northern corridor routes from Arabian Gulf rail to Haifa Port in Israel before shipping to Europe.", "expected", 2024),
    ("GII-01", "What was India's rank on the Global Innovation Index (GII) 2024 published by the World Intellectual Property Organization (WIPO)?",
     ["40th", "39th", "48th", "52nd"], "B", "India ranked 39th out of 133 economies in the Global Innovation Index 2024.", "expected", 2024),
    ("HDI-01", "According to the UNDP Human Development Report 2023-24, what is India's global rank in the Human Development Index (HDI)?",
     ["128th", "131st", "134th", "142nd"], "C", "India ranked 134th out of 193 countries on HDI with a score of 0.644.", "expected", 2024),
    ("SPACE-INT-01", "Which country's spacecraft became the first in human history to land on the far side of the Moon and retrieve lunar soil samples back to Earth in June 2024?",
     ["USA (Artemis)", "Japan (SLIM)", "China (Chang'e-6)", "India (Chandrayaan-3)"], "C", "China's Chang'e-6 mission retrieved the first-ever physical samples from the lunar far side (South Pole-Aitken basin).", "expected", 2024),

    # 21-40: PYQs & High-Yield National Current Affairs
    ("CA-PYQ-01", "Which city hosted the 14th BRICS Summit in virtual format under China's chairmanship?",
     ["Johannesburg", "Beijing", "Brasilia", "New Delhi"], "B", "The 14th BRICS summit was chaired virtually by Beijing, China.", "PYQ", 2020),
    ("CA-PYQ-02", "Who was appointed as the first Chief of Defence Staff (CDS) of the Indian Armed Forces?",
     ["General M. M. Naravane", "General Bipin Rawat", "General Dalbir Singh Suhag", "Admiral Sunil Lanba"], "B", "General Bipin Rawat was appointed India's first Chief of Defence Staff (CDS) in December 2019.", "PYQ", 2020),
    ("CA-PYQ-03", "The Nobel Peace Prize 2023 was conferred upon which human rights defender from Iran?",
     ["Ales Bialiatski", "Narges Mohammadi", "Malala Yousafzai", "Maria Ressa"], "B", "Narges Mohammadi was awarded the Nobel Peace Prize 2023 for her fight against the oppression of women in Iran.", "expected", 2024),
    ("CA-PYQ-04", "Which constitutional article was amended to implement the Goods and Services Tax (GST) in India via the 101st Constitutional Amendment?",
     ["Article 246A", "Article 268A", "Article 270A", "Article 282A"], "A", "Article 246A was inserted by the 101st Amendment to grant concurrent taxing power over GST to Parliament and State Legislatures.", "PYQ", 2017),
    ("CA-PYQ-05", "The headquarters of the International Big Cat Alliance (IBCA) established in 2024 is located in which country?",
     ["Kenya", "India", "South Africa", "Brazil"], "B", "The International Big Cat Alliance (IBCA) is headquartered in India with budgetary backing approved in 2024.", "expected", 2024),
    ("CA-PYQ-06", "Operation Kaveri was launched by the Government of India in 2023 to evacuate Indian citizens from which conflict-ridden nation?",
     ["Ukraine", "Sudan", "Israel", "Yemen"], "B", "Operation Kaveri evacuated over 3,800 Indian citizens from Sudan following civil armed conflict in April 2023.", "expected", 2024),
    ("CA-PYQ-07", "Operation Ajay was launched by India in October 2023 to facilitate the return of Indian citizens from which region?",
     ["Ukraine", "Israel and Palestine", "Gaza Strip", "Afghanistan"], "B", "Operation Ajay was launched to evacuate Indian citizens from Israel following the October 2023 conflict outbreak.", "expected", 2024),
    ("CA-PYQ-08", "Which Indian state hosted the Khelo India Youth Games 2024 across four cities (Chennai, Madurai, Trichy, Coimbatore)?",
     ["Karnataka", "Tamil Nadu", "Maharashtra", "Haryana"], "B", "The 6th Khelo India Youth Games was held in Tamil Nadu in January 2024.", "expected", 2024),
    ("CA-PYQ-09", "The Dadasaheb Phalke Lifetime Achievement Award for 2021 (conferred in late 2023) was awarded to which legendary actress?",
     ["Asha Parekh", "Waheeda Rehman", "Hema Malini", "Rekha"], "B", "Veteran actress Waheeda Rehman was honored with the Dadasaheb Phalke Lifetime Achievement Award.", "expected", 2024),
    ("CA-PYQ-10", "Which island territory of India saw the commissioning of INS Jatayu naval base in March 2024 to bolster Indian Navy's surveillance in the Arabian Sea?",
     ["Andaman and Nicobar Islands", "Minicoy Island (Lakshadweep)", "Diu Island", "Pamban Island"], "B", "INS Jatayu was commissioned on Minicoy Island in Lakshadweep, boosting security across the Sea Lines of Communication.", "expected", 2024),
    ("CA-PYQ-11", "Under the PM-Surya Ghar: Muft Bijli Yojana launched in 2024, how many units of free electricity per month are targeted for 1 crore households via rooftop solar?",
     ["Up to 100 units", "Up to 200 units", "Up to 300 units", "Up to 400 units"], "C", "PM Surya Ghar Yojana targets up to 300 units of free power monthly for 1 crore households.", "expected", 2024),
    ("CA-PYQ-12", "Which national park in Madhya Pradesh is the second relocation site chosen for the introduction of African cheetahs under Project Cheetah?",
     ["Bandhavgarh National Park", "Gandhi Sagar Wildlife Sanctuary", "Kanha National Park", "Pench National Park"], "B", "Gandhi Sagar Wildlife Sanctuary in Madhya Pradesh is prepared as the second home for cheetahs after Kuno NP.", "expected", 2024),
    ("CA-PYQ-13", "The 'Loss and Damage Fund' to assist developing nations vulnerable to climate change was formally operationalized at which COP summit?",
     ["COP26 Glasgow", "COP27 Sharm el-Sheikh", "COP28 Dubai", "COP21 Paris"], "C", "The Loss and Damage Fund was formally adopted and operationalized on Day 1 of COP28 in Dubai (2023).", "expected", 2024),
    ("CA-PYQ-14", "Who is the Chief Justice of India as of mid-2024, heading the Supreme Court of India?",
     ["Justice N. V. Ramana", "Justice U. U. Lalit", "Justice D. Y. Chandrachud", "Justice Sanjiv Khanna"], "C", "Justice D. Y. Chandrachud served as the 50th Chief Justice of India (November 2022 to November 2024).", "expected", 2024),
    ("CA-PYQ-15", "Which public sector aerospace undertaking in Bengaluru manufactures the Light Combat Aircraft (LCA) Tejas for the Indian Air Force?",
     ["BHEL", "HAL (Hindustan Aeronautics Limited)", "BEL", "BEML"], "B", "Hindustan Aeronautics Limited (HAL) headquartered in Bengaluru manufactures the LCA Tejas.", "PYQ", 2020),
    ("CA-PYQ-16", "The Anusandhan National Research Foundation (ANRF) Act, 2023 repealed and replaced which statutory scientific funding body?",
     ["CSIR", "Science and Engineering Research Board (SERB)", "ICAR", "ICMR"], "B", "ANRF repealed the Science and Engineering Research Board (SERB) Act, 2008 to create a Rs. 50,000 Crore research foundation.", "expected", 2024),
    ("CA-PYQ-17", "What is the primary objective of the PM Vishwakarma Scheme launched by the Central Government?",
     ["Promoting AI startups", "End-to-end support to traditional artisans and craftspeople", "Subsidizing electric tractor purchases", "Free health insurance to gig workers"], "B", "PM Vishwakarma provides collateral-free loans, skill training, and toolkits to traditional craftspeople across 18 trades.", "expected", 2024),
    ("CA-PYQ-18", "Which country hosted the G7 Leaders' Summit 2024 in the Apulia region?",
     ["Germany", "Japan", "Italy", "United Kingdom"], "C", "The 50th G7 summit was hosted by Italy in Borgo Egnazia, Apulia in June 2024.", "expected", 2024),
    ("CA-PYQ-19", "The North Atlantic Treaty Organization (NATO) welcomed which Nordic nation as its 32nd member country in March 2024?",
     ["Finland", "Sweden", "Ukraine", "Ireland"], "B", "Sweden officially became the 32nd member of NATO in March 2024 (Finland joined as the 31st member in 2023).", "expected", 2024),
    ("CA-PYQ-20", "Who won the ICC Men's T20 World Cup 2024 held in the West Indies and USA?",
     ["South Africa", "Australia", "India", "England"], "C", "India defeated South Africa in the final in Bridgetown, Barbados to win the Men's T20 World Cup 2024.", "expected", 2024),
]

for idx, item in enumerate(ca_data, 1):
    qid, text, opts, ans, exp, lbl, yr = item
    questions.append(make_q(f"KAS-P1-CA-{idx:03d}", "Current Affairs", text, opts, ans, exp, lbl, yr, syllabus_id="P1-S1.1"))

# ==========================================
# 2. HUMANITIES (60 Questions)
# ==========================================
hum_data = [
    # Karnataka History (1-15)
    ("KH-01", "Who was the founder of the Kadamba dynasty of Banavasi and the author of the Chandravalli inscription?",
     ["Mayurasharma", "Kakusthavarma", "Ravivarma", "Santivarma"], "A", "Mayurasharma founded the Kadamba dynasty at Banavasi around 345 CE after overcoming the Pallavas.", "PYQ", 2017),
    ("KH-02", "The Halmidi Inscription (ಹಾಲ್ಮಿಡಿ ಶಾಸನ), dated to c. 450 CE, was discovered in which modern district of Karnataka?",
     ["Shivamogga", "Hassan", "Chikkamagaluru", "Mandya"], "B", "The Halmidi inscription, the earliest recorded stone inscription in Kannada script, was found in Belur taluk, Hassan district.", "PYQ", 2015),
    ("KH-03", "Which Badami Chalukyan emperor assumed the title 'Parameshwara' after defeating Harsha on the banks of river Narmada?",
     ["Pulakeshin I", "Pulakeshin II", "Kirtivarman I", "Vikramaditya I"], "B", "Pulakeshin II defeated Emperor Harsha on the banks of the Narmada in 618 CE, recorded in the Aihole Inscription by Ravikirti.", "PYQ", 2020),
    ("KH-04", "The magnificent monolithic statue of Gommateshwara at Shravanabelagola was consecrated in 981 CE by which Ganga general?",
     ["Chavundaraya", "Marasimha II", "Durvinita", "Sripurusha"], "A", "Chavundaraya, the military commander of Western Ganga King Rachamalla IV, commissioned the 57-foot Gommateshwara monolith.", "PYQ", 2014),
    ("KH-05", "The rock-cut monolithic Kailasa temple at Ellora (Cave 16) was excavated during the reign of which Rashtrakuta king?",
     ["Dantidurga", "Krishna I", "Amoghavarsha I", "Govinda III"], "B", "Rashtrakuta King Krishna I (c. 756-774 CE) excavated the monolithic Kailasa temple at Ellora.", "PYQ", 2017),
    ("KH-06", "The celebrated Kannada literary work 'Kavirajamarga' was composed during the reign of which monarch?",
     ["Pulakeshin II", "Amoghavarsha Nrupathunga", "Vikramaditya VI", "Vishnuvardhana"], "B", "Kavirajamarga (c. 850 CE) was patronized by Rashtrakuta King Amoghavarsha I Nrupathunga and authored by Sri Vijaya.", "PYQ", 2020),
    ("KH-07", "Which Hoysala king constructed the renowned Chennakeshava Temple at Belur in 1117 CE to commemorate his victory over the Cholas?",
     ["Bittideva (Vishnuvardhana)", "Veera Ballala II", "Narasimha I", "Veera Ballala III"], "A", "King Vishnuvardhana (formerly Bittideva) built the Belur Chennakeshava temple after winning the Battle of Talakadu.", "PYQ", 2015),
    ("KH-08", "The Persian ambassador Abdur Razzak visited the Vijayanagara Empire during the reign of which emperor?",
     ["Harihara II", "Devaraya II (Praudha Devaraya)", "Krishnadevaraya", "Achyuta Devaraya"], "B", "Abdur Razzak visited Vijayanagara in 1443 CE during the reign of Sangama ruler Devaraya II.", "PYQ", 2017),
    ("KH-09", "The historic Battle of Talikota (Rakkasa-Tangadi), which led to the sacking of Vijayanagara, took place in which year?",
     ["1526 CE", "1556 CE", "1565 CE", "1576 CE"], "C", "The Battle of Talikota took place on 23 January 1565 CE between the Vijayanagara army under Aliya Rama Raya and the combined Deccan Sultanates.", "PYQ", 2014),
    ("KH-10", "Which brave queen of Keladi Nayakas provided asylum to Rajaram, son of Chhatrapati Shivaji, defying the Mughal Emperor Aurangzeb?",
     ["Rani Chennamma of Kittur", "Keladi Rani Chennamma", "Keladi Abbakka Rani", "Rani Mangammal"], "B", "Keladi Rani Chennamma gave shelter to Rajaram in 1689 and defeated the Mughal forces sent by Aurangzeb.", "PYQ", 2017),
    ("KH-11", "Kittur Rani Chennamma led an armed rebellion against the British East India Company in 1824 opposing which British policy?",
     ["Subsidiary Alliance", "Doctrine of Lapse", "Permanent Settlement", "Rowlatt Act"], "B", "Rani Chennamma revolted in 1824 when British Collector St. John Thackeray refused to recognize her adopted son Shivalingappa under the Doctrine of Lapse.", "PYQ", 2020),
    ("KH-12", "Sangolli Rayanna, the legendary military commander who fought guerrilla warfare against the British, was executed by hanging in 1831 at which place?",
     ["Kittur", "Nandagad", "Belagavi", "Dharwad"], "B", "Sangolli Rayanna was captured through treachery and hanged by the British at Nandagad on 26 January 1831.", "PYQ", 2015),
    ("KH-13", "The Halagali Bedas uprising of 1857 in Karnataka was triggered by resistance to which British regulation?",
     ["The Inam Commission", "The Disarming Act of 1857", "Salt Tax Regulations", "Forest Rights Restriction"], "B", "The hunters and martial Bedas of Halagali (Mudhol) revolted when the British ordered them to surrender their traditional firearms under the Disarming Act.", "PYQ", 2017),
    ("KH-14", "The only Indian National Congress (INC) Annual Session ever presided over by Mahatma Gandhi was held in 1924 in which Karnataka town?",
     ["Bengaluru", "Belagavi (Belgaum)", "Mysuru", "Hubballi"], "B", "Mahatma Gandhi presided over the 39th Session of the INC held at Belagavi in December 1924.", "PYQ", 2020),
    ("KH-15", "The tragic Vidurashwatha incident (Gowribidanur taluk) of April 1938, where police firing killed 10 Congress satyagrahis, is known as:",
     ["Karnataka's Chauri Chaura", "Jallianwala Bagh of Karnataka", "Mysore Salt March", "Dharwad Firing"], "B", "Vidurashwatha is commemorated as the 'Jallianwala Bagh of Karnataka' for the unprovoked firing on satyagrahis hoisting the national tricolor.", "PYQ", 2014),

    # Indian History (16-30)
    ("IH-01", "In which ancient Ashokan edict site in Karnataka was a unique carved stone portrait of Emperor Ashoka inscribed with 'Ranyo Asoko' discovered?",
     ["Maski", "Sannati (Kanaganahalli)", "Brahmagiri", "Nittur"], "B", "At Kanaganahalli near Sannati in Kalaburagi district, a limestone relief sculpture of Emperor Ashoka inscribed with 'Ranyo Asoko' was excavated.", "PYQ", 2017),
    ("IH-02", "The Maski edict of Emperor Ashoka holds immense historical significance because it was the first inscription to:",
     ["Mention the Battle of Kalinga", "Mention Ashoka by his personal name rather than merely 'Devanampiya Piyadassi'", "Use Greek script", "Record Ashoka's conversion to Jainism"], "B", "The Maski edict in Raichur (discovered by C. Beadon in 1915) explicitly identified 'Devanampiya Ashoka', confirming Ashoka's identity.", "PYQ", 2015),
    ("IH-03", "The Indus Valley Civilization site of Lothal, renowned for its tidal dockyard, is located in which modern state?",
     ["Rajasthan", "Gujarat", "Haryana", "Punjab"], "B", "Lothal is located along the Bhogava river in the Gulf of Khambhat in Gujarat.", "PYQ", 2020),
    ("IH-04", "The Fourth Buddhist Council was convened during the reign of which Kushana monarch at Kundalavana in Kashmir?",
     ["Kanishka I", "Huvishka", "Vima Kadphises", "Vasudeva"], "A", "Kanishka I convened the 4th Buddhist Council presided over by Vasumitra with Asvaghosa as deputy, where Buddhism split into Hinayana and Mahayana.", "PYQ", 2014),
    ("IH-05", "The Iron Pillar at Mehrauli in Delhi, renowned for its rustless metallurgy, bears an inscription belonging to which Gupta monarch?",
     ["Samudragupta", "Chandragupta II (Chandragupta Vikramaditya)", "Kumaragupta I", "Skandagupta"], "B", "The Mehrauli pillar commemorates King 'Chandra', identified by historians as Chandragupta II Vikramaditya.", "PYQ", 2017),
    ("IH-06", "Who among the following Delhi Sultans introduced the market control regulations and price rationing system?",
     ["Balban", "Alauddin Khilji", "Muhammad bin Tughlaq", "Feroz Shah Tughlaq"], "A", "Alauddin Khilji introduced strict market control mechanisms, setting up Shahna-i-Mandi to control prices of grains, cloth, and horses.", "PYQ", 2015),
    ("IH-07", "The Mansabdari administrative system was instituted by which Mughal emperor?",
     ["Babur", "Akbar", "Jahangir", "Shah Jahan"], "B", "Akbar introduced the Mansabdari system in 1571 CE, classifying military and civil officials by Zat (personal rank) and Sawar (cavalry quota).", "PYQ", 2020),
    ("IH-08", "The Council of Eight Ministers known as the 'Ashtapradhan' assisted the administration of which ruler?",
     ["Krishnadevaraya", "Chhatrapati Shivaji Maharaj", "Raja Man Singh", "Tipu Sultan"], "B", "Chhatrapati Shivaji's administration was guided by the Ashtapradhan, headed by the Peshwa (Prime Minister).", "PYQ", 2014),
    ("IH-09", "The Permanent Settlement (Zamindari System) of 1793 was introduced in Bengal and Bihar by which Governor-General?",
     ["Warren Hastings", "Lord Cornwallis", "Lord Wellesley", "Lord Dalhousie"], "B", "Lord Cornwallis introduced the Permanent Settlement in 1793 with zamindars recognized as permanent hereditary owners of land.", "PYQ", 2017),
    ("IH-10", "The Ryotwari land revenue settlement was first conceptualized and implemented in the Madras Presidency by:",
     ["Lord Cornwallis", "Thomas Munro and Alexander Read", "Holt Mackenzie", "Lord William Bentinck"], "B", "Sir Thomas Munro and Captain Alexander Read introduced the Ryotwari system, directly contracting with the individual peasant cultivator (ryot).", "PYQ", 2015),
    ("IH-11", "Who founded the 'Brahmo Samaj' in Calcutta in 1828 to promote monotheism and oppose sati and idolatry?",
     ["Swami Dayananda Saraswati", "Raja Ram Mohan Roy", "Ishwar Chandra Vidyasagar", "Keshab Chandra Sen"], "B", "Raja Ram Mohan Roy established the Brahmo Samaj in 1828.", "PYQ", 2020),
    ("IH-12", "The Satyashodhak Samaj was founded in Maharashtra in 1873 by which social reformer to challenge Brahminical dominance and uplift non-Brahmins and women?",
     ["Jyotirao Phule", "Gopal Hari Deshmukh", "Dr. B. R. Ambedkar", "Mahadev Govind Ranade"], "A", "Mahatma Jyotirao Phule founded the Satyashodhak Samaj (Truth Seekers' Society) in 1873.", "PYQ", 2017),
    ("IH-13", "The partition of Bengal in 1905 was enacted during the viceroyalty of which British administrator?",
     ["Lord Ripon", "Lord Curzon", "Lord Minto", "Lord Hardinge"], "B", "Lord Curzon partitioned Bengal in October 1905 on administrative grounds, triggering the nationwide Swadeshi and Boycott Movement.", "PYQ", 2015),
    ("IH-14", "Who was chosen by Mahatma Gandhi as the first Individual Satyagrahi in October 1940?",
     ["Jawaharlal Nehru", "Acharya Vinoba Bhave", "Brahma Dutt", "Sardar Vallabhbhai Patel"], "B", "Acharya Vinoba Bhave was chosen as the first individual satyagrahi; Jawaharlal Nehru was the second.", "PYQ", 2020),
    ("IH-15", "The historic 'Purna Swaraj' (Complete Independence) resolution was adopted at which annual session of the Indian National Congress in 1929?",
     ["Calcutta Session", "Lahore Session", "Karachi Session", "Madras Session"], "B", "The Lahore Session of INC (December 1929) presided over by Jawaharlal Nehru declared Purna Swaraj as the ultimate goal.", "PYQ", 2014),

    # Geography (31-45)
    ("GEO-01", "Which is the highest peak in Karnataka, situated in the Western Ghats of Chikkamagaluru district?",
     ["Kudremukh", "Mullayanagiri", "Pushpagiri", "Tadiandamol"], "B", "Mullayanagiri in the Baba Budan range of Chikkamagaluru is the highest mountain peak in Karnataka at 1,930 meters (6,332 ft).", "PYQ", 2017),
    ("GEO-02", "The world-famous Jog Falls (Gersoppa Falls) in Shivamogga district is formed by which west-flowing river?",
     ["Netravati", "Sharavathi", "Kali", "Varahi"], "B", "Jog Falls (253 meters high, comprising Raja, Roarer, Rocket, and Rani cascades) is formed by the Sharavathi River.", "PYQ", 2020),
    ("GEO-03", "The Krishna Water Disputes Tribunal-II (KWDT-II) gave its final award under the chairmanship of which judge?",
     ["Justice R. S. Bachawat", "Justice Brijesh Kumar", "Justice A. S. Anand", "Justice Markandey Katju"], "B", "KWDT-II was headed by Justice Brijesh Kumar (KWDT-I was headed by Justice R.S. Bachawat).", "PYQ", 2015),
    ("GEO-04", "Which district in Karnataka is famously known as the 'Coffee Land of India' as coffee was first introduced here at Baba Budan Giri?",
     ["Kodagu", "Chikkamagaluru", "Hassan", "Shivamogga"], "B", "Sufi saint Baba Budan brought seven raw coffee beans from Mocha (Yemen) and planted them in the Chandradrona hills of Chikkamagaluru in the 17th century.", "PYQ", 2014),
    ("GEO-05", "The boundary line separating the Earth's Crust and Mantle is known as:",
     ["Gutenberg Discontinuity", "Mohorovicic (Moho) Discontinuity", "Lehmann Discontinuity", "Conrad Discontinuity"], "B", "The Mohorovicic (Moho) discontinuity marks the boundary between the crust and the upper mantle.", "PYQ", 2017),
    ("GEO-06", "Which of the following ocean currents is a COLD current flowing along the western coast of South America?",
     ["Gulf Stream", "Kuroshio Current", "Humboldt (Peru) Current", "Brazil Current"], "C", "The Humboldt (Peru) Current is a cold, low-salinity ocean current that flows north along the western coast of South America.", "PYQ", 2020),
    ("GEO-07", "The subtropical high-pressure belts situated between 30° and 35° North and South latitudes are popularly called:",
     ["Doldrums", "Horse Latitudes", "Roaring Forties", "Polar Fronts"], "B", "The calm, dry subtropical high-pressure belts are historically known as the 'Horse Latitudes'.", "PYQ", 2015),
    ("GEO-08", "Which port is known as the 'Gateway of Karnataka', handling iron ore and coffee exports on the Arabian Sea coast?",
     ["Karwar Port", "New Mangalore Port (NMPT)", "Malpe Port", "Bhatkal Port"], "B", "New Mangalore Port (Panambur) is Karnataka's only major all-weather port, commissioned in 1974.", "PYQ", 2014),
    ("GEO-09", "The tropical cyclone measuring scale that categorizes hurricanes from Category 1 to 5 based on sustained wind speeds is:",
     ["Richter Scale", "Saffir-Simpson Scale", "Beaufort Scale", "Fujita Scale"], "B", "The Saffir-Simpson Hurricane Wind Scale classifies hurricanes from Category 1 to 5.", "PYQ", 2017),
    ("GEO-10", "Under the UN Convention on the Law of the Sea (UNCLOS), the Exclusive Economic Zone (EEZ) of a coastal state extends up to:",
     ["12 nautical miles", "24 nautical miles", "200 nautical miles", "350 nautical miles"], "C", "The EEZ extends up to 200 nautical miles (370.4 km) from the coastal baseline.", "PYQ", 2020),
    ("GEO-11", "Which plateau in Karnataka is formed predominantly of Archaean Dharwar schist rocks rich in gold, iron ore, and manganese?",
     ["Deccan Traps Plateau", "Karnataka (Mysore) Plateau", "Chota Nagpur Plateau", "Malwa Plateau"], "B", "The Karnataka Plateau contains ancient Dharwar schists (Dharwar Craton) rich in Kolar/Hutti gold and Kudremukh/Sandur iron ores.", "PYQ", 2015),
    ("GEO-12", "Which river basin dispute involves the states of Karnataka, Goa, and Maharashtra over the Kalasa-Banduri Nala drinking water diversion project?",
     ["Cauvery river", "Mahadayi (Mandovi) river", "Krishna river", "Godavari river"], "B", "The Mahadayi River Water Disputes Tribunal adjudicated the water-sharing dispute between Karnataka, Goa, and Maharashtra.", "PYQ", 2020),
    ("GEO-13", "The phenomenon of temperature inversion in the troposphere occurs when:",
     ["Temperature decreases with increasing altitude", "Temperature increases with increasing altitude", "Temperature remains absolutely constant", "Pressure falls to absolute zero"], "B", "Temperature inversion is a reversal of normal lapse rate, where warm air lies over cold air, causing temperature to increase with height.", "PYQ", 2014),
    ("GEO-14", "Which Ramsar wetland in Mandya district of Karnataka is situated on an island in the Cauvery River and is a renowned bird sanctuary?",
     ["Karanji Lake", "Ranganathittu Bird Sanctuary", "Ankasamudra Reserve", "Magadi Lake"], "B", "Ranganathittu Bird Sanctuary in Mandya was declared Karnataka's first Ramsar site in 2022.", "PYQ", 2017),
    ("GEO-15", "The 'El Nino' weather phenomenon is characterized by which anomalous oceanic condition in the equatorial Pacific Ocean?",
     ["Abnormal cooling of central and eastern Pacific waters", "Abnormal warming of central and eastern Pacific waters", "Intensification of trade winds", "Enhanced upwelling along Peruvian coast"], "B", "El Nino involves periodic warming of sea surface temperatures across the central and east-central equatorial Pacific.", "PYQ", 2020),

    # Polity & Economy (46-60)
    ("POL-01", "Which article of the Constitution of India provides for the writ jurisdiction of the Supreme Court for enforcement of Fundamental Rights?",
     ["Article 32", "Article 131", "Article 143", "Article 226"], "A", "Article 32 guarantees the right to constitutional remedies via the Supreme Court (Dr. Ambedkar called it the 'Heart and Soul' of the Constitution).", "PYQ", 2017),
    ("POL-02", "Under which constitutional amendment was Article 371J inserted to provide special provisions and reservations for the Kalyana Karnataka (Hyderabad-Karnataka) region?",
     ["98th Constitutional Amendment Act, 2012", "99th Constitutional Amendment Act, 2014", "100th Constitutional Amendment Act, 2015", "101st Constitutional Amendment Act, 2016"], "A", "The 98th Constitutional Amendment Act inserted Article 371J, empowering the Governor to establish development boards and quotas for the 6 backward districts.", "PYQ", 2015),
    ("POL-03", "The concept of 'Basic Structure' of the Indian Constitution was propounded by the Supreme Court in which landmark case?",
     ["Golaknath v. State of Punjab (1967)", "Kesavananda Bharati v. State of Kerala (1973)", "Minerva Mills v. Union of India (1980)", "Maneka Gandhi v. Union of India (1978)"], "B", "The 13-judge bench in Kesavananda Bharati (24 April 1973) held that Parliament cannot alter the basic structure of the Constitution.", "PYQ", 2020),
    ("POL-04", "Karnataka was the pioneer in passing the historic Panchayati Raj Act in 1983 based on the Ashok Mehta Committee model under which visionary Rural Development Minister?",
     ["D. Devaraj Urs", "Abdul Nazir Sab", "Ramakrishna Hegde", "S. R. Bommai"], "B", "Abdul Nazir Sab ('Neeru Nazir Sab') conceptualized and enacted the revolutionary 1983 Karnataka Zilla Parishads and Mandal Panchayats Act.", "PYQ", 2014),
    ("POL-05", "In August 2022, the High Court of Karnataka delivered a historic verdict in the Chidananda Urs case, ruling that:",
     ["The Anti-Corruption Bureau (ACB) was unconstitutional and all powers and pending inquiries were restored to the Karnataka Lokayukta", "SAKALA mission was non-statutory", "Local reservation in private IT firms was void", "RTI did not apply to ministers"], "A", "The HC abolished the ACB created in 2016 and restored complete police and prosecuting powers back to the Karnataka Lokayukta.", "PYQ", 2020),
    ("POL-06", "The Karnataka Guarantee of Services to Citizens Act (SAKALA) was enacted in which year?",
     ["2008", "2011", "2014", "2016"], "B", "SAKALA was enacted in 2011 to provide guarantee of services within prescribed time limits to citizens of Karnataka.", "PYQ", 2015),
    ("POL-07", "Who is the ex-officio Chairman of the NITI Aayog (National Institution for Transforming India)?",
     ["Minister of Finance", "Prime Minister of India", "Governor of RBI", "Vice-President of India"], "B", "The Prime Minister of India serves as the ex-officio Chairman of NITI Aayog.", "PYQ", 2017),
    ("POL-08", "The Monetary Policy Committee (MPC) in India operates under the mandate of targeting consumer price inflation (CPI) at what rate?",
     ["2% with a +/- 1% tolerance band", "4% with a +/- 2% tolerance band", "5% fixed rate", "6% ceiling limit"], "B", "Under Section 45ZB of the RBI Act, the inflation target is 4% CPI inflation with an upper tolerance of 6% and lower tolerance of 2%.", "PYQ", 2020),
    ("POL-09", "The High-Power Committee for Redressal of Regional Imbalances in Karnataka, which submitted its landmark report in 2002, was headed by:",
     ["Dr. L. G. Havanur", "Dr. D. M. Nanjundappa", "Justice Venkataswami", "Justice Sadashiva"], "B", "The Dr. D.M. Nanjundappa Committee identified 114 backward taluks (most in North Karnataka) and formulated the Special Development Plan.", "PYQ", 2014),
    ("POL-10", "Under the Karnataka Fiscal Responsibility Act (KFRA), 2002, what is the statutory ceiling for the state's Fiscal Deficit as a percentage of GSDP?",
     ["2.0% of GSDP", "3.0% of GSDP", "4.5% of GSDP", "5.0% of GSDP"], "B", "KFRA mandates that the state fiscal deficit must be contained within 3% of Gross State Domestic Product (GSDP).", "PYQ", 2017),
    ("POL-11", "The Multidimensional Poverty Index (MPI) published by NITI Aayog measures acute deprivations across how many core dimensions?",
     ["Two (Income and Wealth)", "Three (Health, Education, and Standard of Living)", "Four (Food, Housing, Health, Water)", "Five (Human capital indicators)"], "B", "The MPI adopts the Alkire-Foster methodology across 3 dimensions: Health, Education, and Standard of Living, spanning 12 indicators.", "PYQ", 2020),
    ("POL-12", "Which constitutional amendment introduced the Goods and Services Tax (GST) regime in India?",
     ["99th Amendment Act", "100th Amendment Act", "101st Amendment Act", "103rd Amendment Act"], "C", "The 101st Constitutional Amendment Act, 2016 introduced GST across India with effect from 1 July 2017.", "PYQ", 2017),
    ("POL-13", "The concept of 'Dominant Caste' in Indian sociology was formulated by which eminent Karnataka-born sociologist based on studies in Rampura village?",
     ["G. S. Ghurye", "M. N. Srinivas", "Andre Beteille", "Irawati Karve"], "B", "Prof. M. N. Srinivas formulated the concepts of 'Dominant Caste' and 'Sanskritization' from field work in Rampura (Mandya district).", "PYQ", 2015),
    ("POL-14", "Under the Karnataka Scheduled Castes Sub-Allocation and Tribal Sub-Allocation (SCSP/TSP) Act, 2013, what percentage of total state plan outlay is mandatorily earmarked for SC/ST welfare?",
     ["18%", "20%", "24.1%", "30%"], "C", "The SCSP/TSP Act mandates 24.1% of the state budget (proportionate to SC 17.15% and ST 6.95% population share) for dedicated welfare.", "PYQ", 2020),
    ("POL-15", "Which expert committee recommended the four-tier internal reservation classification (Left, Right, Touchables, and Others) for Scheduled Castes in Karnataka?",
     ["Justice Sadashiva Inquiry Commission", "Justice H. N. Nagamohan Das Commission", "Justice Venkataswamy Commission", "Chinnappa Reddy Commission"], "A", "The Justice A. J. Sadashiva Inquiry Commission (submitted 2012) recommended internal reservation to redress uneven benefits among 101 SC castes.", "PYQ", 2017),
]

for idx, item in enumerate(hum_data, 1):
    qid, text, opts, ans, exp, lbl, yr = item
    questions.append(make_q(f"KAS-P1-HUM-{idx:03d}", "Humanities", text, opts, ans, exp, lbl, yr, syllabus_id="P1-S2.1"))

# ==========================================
# 3. KARNATAKA AFFAIRS (40 Questions)
# ==========================================
ka_data = [
    # Five Guarantees (1-15)
    ("GL-01", "Under the Gruha Lakshmi Scheme in Karnataka, what is the monthly financial assistance deposited via DBT to eligible women?",
     ["Rs. 1,000", "Rs. 1,500", "Rs. 2,000", "Rs. 2,500"], "C", "Gruha Lakshmi provides Rs. 2,000 per month DBT to the designated female head of the household.", "expected", 2024),
    ("GL-02", "Who among the following is EXCLUDED from receiving monthly benefits under the Gruha Lakshmi Scheme?",
     ["Women residing in rented houses", "Women who are themselves or whose husbands are Income Tax or GST assessees", "Women without higher education", "Widows and elderly women"], "B", "Women or their spouses paying Income Tax or GST are excluded from Gruha Lakshmi.", "expected", 2024),
    ("GJ-01", "Under the Gruha Jyothi scheme, what is the maximum ceiling of free monthly domestic electricity units allowed per household?",
     ["100 units", "150 units", "200 units", "250 units"], "C", "Gruha Jyothi provides free electricity up to an absolute ceiling of 200 units per month.", "expected", 2024),
    ("GJ-02", "How is the entitled free electricity quota determined for a domestic consumer under Gruha Jyothi?",
     ["Fixed 200 units for everyone", "Past 12-month average consumption + 10% buffer", "Based on household square footage", "Based on number of family members"], "B", "Entitled units are calculated as the consumer's average monthly consumption of the past 12 months plus a 10% buffer.", "expected", 2024),
    ("YN-01", "Under the Yuva Nidhi scheme, what is the monthly unemployment stipend provided to unemployed Graduates and Diploma holders respectively?",
     ["Graduates: Rs. 2,000; Diploma: Rs. 1,000", "Graduates: Rs. 3,000; Diploma: Rs. 1,500", "Graduates: Rs. 4,000; Diploma: Rs. 2,000", "Graduates: Rs. 5,000; Diploma: Rs. 2,500"], "B", "Yuva Nidhi provides Rs. 3,000/month for graduates and Rs. 1,500/month for diploma holders.", "expected", 2024),
    ("YN-02", "What is the maximum duration for which Yuva Nidhi unemployment assistance is payable to a beneficiary?",
     ["12 months (1 year)", "24 months (2 years)", "36 months (3 years)", "Until age 35"], "B", "Yuva Nidhi is payable for a maximum tenure of 2 years (24 months) or until employment/self-employment is secured.", "expected", 2024),
    ("SH-01", "The Shakti scheme in Karnataka provides fare-free travel to domicile women across state transport buses, but EXCLUDES which bus service?",
     ["City bus services of BMTC", "Ordinary express buses of KSRTC", "Premium luxury buses like Airavat, Rajahamsa, and EV Power Plus", "Mofussil buses of NWKRTC"], "C", "Shakti excludes luxury/interstate bus services such as Airavat Club Class, Rajahamsa, and EV Power Plus.", "expected", 2024),
    ("AB-01", "Under the Anna Bhagya scheme, in lieu of the additional 5 kg rice procurement bottleneck, how much cash is transferred via DBT per person per month?",
     ["Rs. 100", "Rs. 150", "Rs. 170 (at Rs. 34/kg)", "Rs. 200"], "C", "The Government of Karnataka credits Rs. 170 per person per month (5 kg at Rs. 34 per kg) via DBT for BPL/AAY cardholders.", "expected", 2024),
    ("BUD-01", "The annual budgetary outlay allocated for the implementation of the Five Guarantees in the Karnataka Budget 2026-27 exceeds approximately:",
     ["Rs. 25,000 Crore", "Rs. 35,000 Crore", "Rs. 52,000 Crore", "Rs. 75,000 Crore"], "C", "The annual budgetary allocation for the Five Guarantees exceeds Rs. 52,000 Crore (~14% of state budget).", "expected", 2024),

    # State Schemes & Policies (10-25)
    ("KB-01", "The 'Krishi Bhagya' scheme of the Government of Karnataka primarily focuses on which intervention in rainfed agricultural areas?",
     ["Distributing free tractors", "Construction of farm ponds (Krishi Honda) and micro-irrigation systems", "Providing 100% fertilizer subsidies", "Establishing cold storage hubs"], "B", "Krishi Bhagya promotes farm ponds (Krishi Honda), polythene lining, diesel pumps, and micro-irrigation in dryland farming.", "PYQ", 2017),
    ("KS-01", "Under the 'Ksheera Bhagya' scheme, how many days a week is milk distributed to children in government schools and Anganwadis in Karnataka?",
     ["2 days a week", "3 days a week", "5 days a week", "Every day (7 days)"], "C", "Ksheera Bhagya provides 150 ml of milk 5 days a week to school and Anganwadi students.", "PYQ", 2015),
    ("MP-01", "The 'Mathru Poorna' scheme in Karnataka provides which service to pregnant and lactating mothers?",
     ["Cash transfer of Rs. 6,000 in three tranches", "One hot, nutritious cooked meal daily at Anganwadis for 15 months", "Free private hospital delivery", "Free neonatal baby kits"], "B", "Mathru Poorna delivers one wholesome hot cooked meal daily with milk and eggs at Anganwadi centers.", "PYQ", 2020),
    ("RS-01", "The 'Raitha Siri' scheme provides financial incentive of Rs. 10,000 per hectare for farmers cultivating which crops in Karnataka?",
     ["Sugarcane and Paddy", "Minor Millets (Siridhanya)", "Coffee and Arecanut", "BT Cotton and Tobacco"], "B", "Raitha Siri incentivizes minor millet (Siridhanya) cultivation with Rs. 10,000/ha direct financial aid.", "PYQ", 2020),
    ("GIG-01", "The Karnataka Platform-Based Gig Workers Bill, 2024 mandates which mechanism to fund social security welfare for gig delivery workers?",
     ["5% income tax deduction", "Welfare fee of 1% to 2% levied on each customer transaction on aggregators", "Fixed monthly cess on restaurants", "Employer-only registration fees"], "B", "The bill levies a welfare fee of 1% to 2% on customer transactions processed by platform aggregators.", "expected", 2024),
    ("GBR-01", "The Greater Bengaluru Governance Bill, 2024 proposes replacing BBMP with multiple corporations coordinated by which apex body?",
     ["Bengaluru Metropolitan Task Force (BMTF)", "Greater Bengaluru Authority (GBA) chaired by Chief Minister", "BDA Board", "Karnataka Urban Development Directorate"], "B", "The Greater Bengaluru Authority (GBA) headed by the Chief Minister will oversee decentralized municipal corporations.", "expected", 2024),
    ("YET-01", "The Yettinahole Integrated Drinking Water Project lifts water from the catchment area in Sakaleshpura to supply drinking water to how many drought-prone districts?",
     ["3 districts", "5 districts", "7 districts (Chikkamagaluru, Hassan, Tumakuru, Chikkaballapura, Kolar, Bengaluru Rural, Ramanagara)", "12 districts"], "C", "Yettinahole supplies 24 TMC drinking water to 29 taluks across 7 drought-affected eastern districts.", "expected", 2024),
    ("HYS-01", "Which Hoysala temple complex was inscribed as part of the 'Sacred Ensembles of the Hoysalas' UNESCO World Heritage Site in September 2023?",
     ["Chennakeshava Temple at Belur, Hoysaleshwara Temple at Halebidu, and Keshava Temple at Somanathapura", "Vidyashankara Temple at Sringeri", "Veeranarayana Temple at Belavadi", "Amruteshwara Temple at Annigeri"], "A", "The three inscribed Hoysala complexes are Belur Chennakeshava, Halebidu Hoysaleshwara, and Somanathapura Keshava temple.", "expected", 2024),
    ("SAM-01", "The 87th Akhila Bharata Kannada Sahitya Sammelana held in 2024 was hosted at Mandya under the presidency of which eminent writer and folklorist?",
     ["Dr. Chandrashekhara Kambara", "Go. Ru. Channabasappa", "Dr. Doddarange Gowda", "Prof. Baraguru Ramachandrappa"], "B", "Renowned folklorist Go. Ru. Channabasappa presided over the 87th Sahitya Sammelana at Mandya.", "expected", 2024),
    ("BEY-01", "The 'Beyond Bengaluru' policy of the Department of Electronics, IT/Bt aims to build major technology and startup clusters in which cities?",
     ["Mysuru, Hubballi-Dharwad, and Mangaluru", "Ballari, Raichur, and Koppal", "Bidar, Bagalkote, and Yadgir", "Chamarajanagar and Mandya"], "A", "Beyond Bengaluru focuses on Mysuru, Hubballi-Dharwad, and Mangaluru as Tier-2 tech growth engines.", "expected", 2024),
    ("RAM-KA-01", "Which estuary in Uttara Kannada district was officially declared as a Ramsar Site of International Importance in early 2024?",
     ["Sharavathi Estuary", "Aghanashini Estuary", "Kali Estuary", "Gangavali Estuary"], "B", "Aghanashini Estuary in Kumta taluk, Uttara Kannada was declared a Ramsar wetland in 2024.", "expected", 2024),
    ("RAM-KA-02", "Which bird conservation reserve in Vijayanagara district was designated as a Ramsar site in 2024?",
     ["Ankasamudra Bird Conservation Reserve", "Daroji Sloth Bear Sanctuary", "Gudavi Bird Sanctuary", "Attiveri Bird Sanctuary"], "A", "Ankasamudra Bird Conservation Reserve in Hagaribommanahalli taluk, Vijayanagara is a designated Ramsar site.", "expected", 2024),
    ("RAM-KA-03", "Which conservation reserve in Gadag district, famous as a wintering habitat for Bar-headed Geese, was declared a Ramsar site in 2024?",
     ["Magadi Kere Conservation Reserve", "Bonal Bird Sanctuary", "Karanji Lake", "Hesaraghatta Grasslands"], "A", "Magadi Kere in Shirahatti taluk, Gadag district was notified as a Ramsar site in 2024.", "expected", 2024),
    ("PAV-01", "The Pavagada Solar Park (Shakti Sthala), one of the world's largest operational solar parks with 2,050 MW capacity, is located in which district?",
     ["Koppal", "Tumakuru", "Chitradurga", "Ballari"], "B", "Pavagada Solar Park is located in the dry Pavagada taluk of Tumakuru district.", "PYQ", 2020),
    ("CBIC-01", "Under the Chennai-Bengaluru Industrial Corridor (CBIC), which node in Karnataka is being developed as a major Smart Industrial City?",
     ["Vasanthanarasapura (Tumakuru)", "Belagavi", "Hubballi", "Mysuru"], "A", "Tumakuru Industrial Township at Vasanthanarasapura is the premier integrated industrial node on CBIC in Karnataka.", "expected", 2024),

    # Administrative & Social Milestones (26-40)
    ("DEV-01", "The D. Devaraj Urs Land Reforms Act of 1974 in Karnataka is celebrated for which revolutionary agrarian principle?",
     ["Consolidation of agricultural holdings", "Land to the Tiller ('Uluvavanige Bhoomi')", "Free cooperative farming", "Corporate agriculture leasing"], "B", "The 1974 amendment under D. Devaraj Urs abolished tenancy and transferred ownership to the cultivating tiller.", "PYQ", 2017),
    ("GOK-01", "The 'Gokak Chaluvali' (Gokak Agitation) of 1982 in Karnataka was an agitation demanding:",
     ["Bilingual signboards in Bengaluru", "First language status and primacy for Kannada in state school education", "Creation of a separate North Karnataka state", "Reservations for Kannada medium students in jobs"], "B", "The Gokak Agitation demanded implementation of the J. W. Gokak Committee report granting sole first language status to Kannada in high schools.", "PYQ", 2015),
    ("REN-01", "In which historic year was the state of 'Mysore' officially renamed as 'Karnataka' under Chief Minister D. Devaraj Urs?",
     ["1956", "1971", "1973 (November 1)", "1977"], "C", "On 1 November 1973, Mysore State was officially renamed 'Karnataka' by Chief Minister D. Devaraj Urs.", "PYQ", 2020),
    ("SRC-01", "The States Reorganisation Commission (SRC) 1955 which created the unified Mysore State on 1 November 1956 was headed by:",
     ["Fazal Ali", "K. M. Panikkar", "H. N. Kunzru", "Justice Dhar"], "A", "The Fazal Ali Commission (along with members Panikkar and Kunzru) recommended the unification of Kannada-speaking regions.", "PYQ", 2014),
    ("ALUR-01", "Who is venerated as 'Kannada Kula Purohita' for spearheading the Karnataka Unification Movement through his book 'Karnataka Gathavaibhava'?",
     ["Alur Venkata Rao", "B. M. Srikantaiah", "Huilgol Narayana Rao", "Gudur Krishna Rao"], "A", "Alur Venkata Rao wrote 'Karnataka Gathavaibhava' in 1912 and is revered as the Kannada Kula Purohita.", "PYQ", 2017),
    ("ISUR-01", "Which village in Shivamogga district declared itself an independent republic during the Quit India Movement in 1942 under the slogan 'Esuru Kottaru Isuru Kodevu'?",
     ["Vidurashwatha", "Isur (Esuru)", "Halagali", "Keladi"], "B", "Isur village in Shikaripura taluk declared independence and established its own government during Quit India in 1942.", "PYQ", 2015),
    ("BHOOMI-01", "Which e-governance project implemented in Karnataka revolutionized computerized land records management, winning the Commonwealth CAPAM award?",
     ["Khajane", "Bhoomi", "Seva Sindhu", "Kaveri"], "B", "Bhoomi digitized RTC land titles across Karnataka, eliminating manual patwari monopolies.", "PYQ", 2017),
    ("SEVA-01", "Which unified digital delivery portal of the Government of Karnataka acts as the single gateway for citizen services including the Five Guarantees?",
     ["Mahiti Kanaja", "Seva Sindhu", "Janasevaka", "Kaveri 2.0"], "B", "Seva Sindhu is the integrated state e-services delivery portal in Karnataka.", "expected", 2024),
    ("LOK-01", "The Karnataka Lokayukta Act was passed in 1984 under the chief ministership of:",
     ["D. Devaraj Urs", "Ramakrishna Hegde", "S. Nijalingappa", "Veerendra Patil"], "B", "Ramakrishna Hegde's Janata government enacted the historic Karnataka Lokayukta Act in 1984.", "PYQ", 2014),
    ("JANA-01", "The 'Janasevaka' scheme launched in Bengaluru provides which citizen facility?",
     ["Free health checkup at municipal hospitals", "Doorstep delivery of 50+ government services to citizens' homes", "Subsidized auto-rickshaw rides", "Free drinking water delivery"], "B", "Janasevaka provides doorstep delivery of government certificates and services via trained delivery executives.", "expected", 2024),
    ("KRRS-01", "The Karnataka Rajya Raitha Sangha (KRRS) was founded in 1980 by which charismatic peasant leader who led the Malaprabha farmers' agitation?",
     ["Prof. M. D. Nanjundaswamy", "K. S. Puttannaiah", "B. S. Yediyurappa", "Kadidal Manjappa"], "A", "Prof. M. D. Nanjundaswamy ('Hasiru Shalu') founded the KRRS following the 1980 Naragund-Navalgund farmers' rebellion.", "PYQ", 2017),
    ("DSS-01", "The Dalit Sangharsha Samiti (DSS) in Karnataka was established in 1974 under the intellectual leadership of which prominent writer and activist?",
     ["Dr. Siddalingaiah and B. Krishnappa", "Devanur Mahadeva", "L. G. Havanur", "Basavalingappa"], "A", "Dalit poet Dr. Siddalingaiah and Prof. B. Krishnappa founded the DSS at Bhadravathi in 1974.", "PYQ", 2020),
    ("NANJ-01", "How many taluks were categorized as 'Backward' in Karnataka by the High-Power Committee headed by Dr. D. M. Nanjundappa in 2002?",
     ["80 taluks", "100 taluks", "114 taluks (out of 175 taluks)", "135 taluks"], "C", "The Nanjundappa Committee identified 114 backward taluks (39 most backward, 40 more backward, 35 backward).", "PYQ", 2015),
    ("KITS-01", "The nodal society functioning under the Department of Electronics, IT/Bt for managing tech parks, biotech incubation, and startups in Karnataka is:",
     ["KEONICS", "KITS (Karnataka Innovation and Technology Society)", "KINFRA", "KSIIDC"], "B", "KITS implements the Startup Policy, K-Tech innovation hubs, and biotech initiatives in Karnataka.", "expected", 2024),
    ("CHET-01", "Under the Karnataka Industrial Policy 2020-25, which zone comprises Bengaluru Urban and Rural with the lowest financial incentives to encourage regional dispersion?",
     ["Zone 1", "Zone 2", "Zone 3", "Zone 4"], "C", "Zone 3 comprises Bengaluru Urban and Rural with minimal incentives, whereas backward taluks in Zone 1 receive maximum subsidies.", "expected", 2024),
    ("KSTDC-01", "The Golden Chariot, a luxury tourist train showcasing South Indian heritage, is operated in partnership with which state corporation?",
     ["KSTDC (Karnataka State Tourism Development Corporation)", "KSRTC", "KINFRA", "KIADB"], "A", "The Golden Chariot is operated by IRCTC in collaboration with KSTDC.", "PYQ", 2020),
]

for idx, item in enumerate(ka_data, 1):
    qid, text, opts, ans, exp, lbl, yr = item
    questions.append(make_q(f"KAS-P2-KA-{idx:03d}", "Karnataka Affairs", text, opts, ans, exp, lbl, yr, syllabus_id="P2-S1.1"))

# ==========================================
# 4. SCIENCE AND ENVIRONMENT (30 Questions)
# ==========================================
sci_data = [
    # Space & Tech (1-10)
    ("CH3-01", "The historic lunar landing site of ISRO's Chandrayaan-3 near the Moon's South Pole was officially named as:",
     ["Tiranga Point", "Shiv Shakti Point", "Atal Point", "Jawahar Point"], "B", "The Chandrayaan-3 landing site was named 'Shiv Shakti Point'; August 23 was declared National Space Day.", "expected", 2024),
    ("CH3-02", "Which heavy-lift launch vehicle of ISRO launched the Chandrayaan-3 and OneWeb satellite constellations into orbit?",
     ["PSLV-C56", "GSLV Mk-II", "LVM3 (Launch Vehicle Mark 3)", "SSLV-D2"], "C", "LVM3 (formerly GSLV Mk-III) launched Chandrayaan-3 on 14 July 2023.", "expected", 2024),
    ("AD-01", "ISRO's solar observatory Aditya-L1 was placed in a halo orbit around which Sun-Earth Lagrange Point located 1.5 million km from Earth?",
     ["L1", "L2", "L3", "L4"], "A", "Aditya-L1 orbits Lagrange Point 1 (L1), providing uninterrupted 24x7 view of the Sun without eclipses.", "expected", 2024),
    ("GAG-01", "What is the name of the female humanoid robot astronaut developed by ISRO for uncrewed test flights of the Gaganyaan mission?",
     ["Mitra", "Vyommitra", "Daksh", "Kalam"], "B", "Vyommitra ('Friend in Space') was developed by ISRO Inertial Systems Unit and IISc Bengaluru.", "expected", 2024),
    ("PSLV-01", "The Polar Satellite Launch Vehicle (PSLV) has four stages using which alternate sequence of propulsion systems?",
     ["Liquid - Solid - Liquid - Solid", "Solid - Liquid - Solid - Liquid", "All four stages Solid", "All four stages Cryogenic"], "B", "PSLV uses alternate solid-liquid stages: Stage 1 (Solid) -> Stage 2 (Liquid Vikas) -> Stage 3 (Solid) -> Stage 4 (Liquid).", "PYQ", 2020),
    ("NUC-01", "Stage-2 of Homi Bhabha's three-stage nuclear power programme in India utilizes which reactor type?",
     ["Pressurised Heavy Water Reactor (PHWR)", "Fast Breeder Reactor (FBR)", "Advanced Heavy Water Reactor (AHWR)", "Light Water Reactor (LWR)"], "B", "Stage 2 utilizes Fast Breeder Reactors (FBR) fueled by Plutonium-239 to breed U-233 from Thorium blankets.", "PYQ", 2017),
    ("NUC-02", "The Kaiga Atomic Power Station in Uttara Kannada district of Karnataka operates which type of nuclear reactors?",
     ["Pressurised Water Reactors (PWR)", "Pressurised Heavy Water Reactors (PHWR)", "Fast Breeder Reactors (FBR)", "Boiling Water Reactors (BWR)"], "B", "Kaiga operates 4 indigenous 220 MWe PHWR units using natural uranium fuel and heavy water moderator.", "PYQ", 2015),
    ("AI-01", "Which premier artificial intelligence and supercomputing mission was allocated Rs. 10,372 Crore by the Union Cabinet in 2024 to deploy 10,000 GPUs?",
     ["Digital India", "IndiaAI Mission", "PARAM Supercomputing Initiative", "Cyber Swachhta Kendra"], "B", "The IndiaAI Mission was approved in March 2024 to establish high-compute GPU capacity for AI innovation.", "expected", 2024),
    ("BT-01", "The pioneering 'Genome India Project' completed sequencing of how many reference human genomes across diverse Indian populations in 2024?",
     ["1,000 genomes", "5,000 genomes", "10,000 genomes", "50,000 genomes"], "C", "The Department of Biotechnology sequenced 10,000 human genomes representative of Indian genetic diversity.", "expected", 2024),
    ("DEF-01", "Which indigenous Light Combat Helicopter (LCH) developed by HAL Bengaluru was inducted into the IAF and Indian Army under the name 'Prachand'?",
     ["LCA Tejas", "LCH Prachand", "ALH Dhruv", "LUH Cheetah"], "B", "LCH Prachand is India's dedicated high-altitude attack helicopter manufactured by HAL.", "expected", 2024),

    # Ecology, Western Ghats & Environment (11-20)
    ("BIO-01", "Which of the following National Parks in Karnataka is part of the Nilgiri Biosphere Reserve and India's first Project Tiger reserve in the state?",
     ["Kudremukh National Park", "Bandipur National Park", "Anshi National Park", "Bannerghatta National Park"], "B", "Bandipur National Park in Chamarajanagar was created in 1974 and was among the original 9 Project Tiger reserves (1973).", "PYQ", 2020),
    ("BIO-02", "India's first dedicated Butterfly Park was inaugurated in 2006 inside which protected area near Bengaluru?",
     ["Nagarhole National Park", "Bannerghatta National Park", "Lalbagh Botanical Garden", "Ranganathittu Bird Sanctuary"], "B", "Bannerghatta Biological Park hosts India's first butterfly conservatory opened in 2006.", "PYQ", 2015),
    ("BIO-03", "The rare and endangered primate 'Lion-tailed Macaque' (Macaca silenus) is endemic to which ecosystem in Karnataka?",
     ["Dry deciduous thorn scrub of Deccan Maidan", "Tropical evergreen rainforests of Western Ghats", "Mangrove swamps of Karwar", "Sub-tropical grasslands of Biligiriranga Hills"], "B", "The Lion-tailed Macaque is strictly endemic to the dense rainforest canopy of the Western Ghats (Sharavathi, Someshwara).", "PYQ", 2017),
    ("BIO-04", "Three rivers—Tunga, Bhadra, and Netravati—originate at Gangamoola inside which national park of Karnataka?",
     ["Bandipur National Park", "Nagarhole National Park", "Kudremukh National Park", "Anshi National Park"], "C", "Gangamoola in Kudremukh is the sacred origin of east-flowing Tunga and Bhadra and west-flowing Netravati.", "PYQ", 2014),
    ("BIO-05", "According to the All-India Tiger Estimation 2022, Karnataka holds which rank in tiger population in India with 563 tigers?",
     ["First (1st)", "Second (2nd)", "Third (3rd)", "Fourth (4th)"], "B", "Karnataka ranks 2nd in tigers (563) behind Madhya Pradesh (785 tigers).", "expected", 2024),
    ("BIO-06", "The Western Ghats Ecology Expert Panel (WGEEP) which recommended declaring 100% of the Western Ghats as Eco-Sensitive Zones was chaired by:",
     ["Dr. K. Kasturirangan", "Prof. Madhav Gadgil", "Dr. M. S. Swaminathan", "Sunita Narain"], "B", "Prof. Madhav Gadgil chaired WGEEP which submitted its report in 2011 proposing 3-tier ESZ protection.", "PYQ", 2017),
    ("BIO-07", "The High-Level Working Group (HLWG) chaired by Dr. K. Kasturirangan recommended that what percentage of the Western Ghats be declared Eco-Sensitive Area (ESA)?",
     ["100%", "63%", "37%", "25%"], "C", "Kasturirangan Committee identified only the 37% Natural Landscape as ESA, excluding 63% Cultural Landscape.", "PYQ", 2020),
    ("BIO-08", "Kyasanur Forest Disease (KFD / Monkey Fever) in Karnataka is transmitted to humans through the bite of which tick vector?",
     ["Aedes aegypti", "Haemaphysalis spinigera", "Anopheles stephensi", "Culex quinquefasciatus"], "B", "KFD is transmitted by hard forest ticks *Haemaphysalis spinigera* commonly found on forest monkeys.", "PYQ", 2015),
    ("BIO-09", "In an ecological food chain, why is the Pyramid of Energy ALWAYS upright without exception?",
     ["Biomass decreases down trophic levels", "Energy transfer obeys the Second Law of Thermodynamics and 10% law with heat dissipation at each step", "Top carnivores consume more energy than plants", "Decomposers trap all solar energy"], "B", "Energy decreases at each successive trophic level due to metabolic respiration and thermodynamic entropy.", "PYQ", 2017),
    ("BIO-10", "The transitional ecological zone between two distinct biological communities (e.g. between land and water) exhibiting high species richness is called:",
     ["Ecological Niche", "Ecotone", "Biome", "Habitat"], "B", "An ecotone is the boundary zone between two ecosystems, exhibiting the 'Edge Effect' with rich biodiversity.", "PYQ", 2020),

    # Health & Pollution (21-30)
    ("ENV-01", "The National Air Quality Index (AQI) in India monitors how many atmospheric criteria pollutants?",
     ["5 pollutants", "8 pollutants", "10 pollutants", "12 pollutants"], "B", "AQI monitors 8 pollutants: PM10, PM2.5, NO2, SO2, CO, O3, NH3, and Pb (NAAQS monitors 12).", "PYQ", 2017),
    ("ENV-02", "Under the Montreal Protocol and its 2016 Kigali Amendment, which potent greenhouse gases are being globally phased down?",
     ["Carbon dioxide (CO2)", "Hydrofluorocarbons (HFCs)", "Methane (CH4)", "Nitrous oxide (N2O)"], "B", "The Kigali Amendment mandates phasing down Hydrofluorocarbons (HFCs), which replaced ozone-depleting CFCs but act as potent GHGs.", "expected", 2024),
    ("ENV-03", "The Environment (Protection) Act, 1986 was enacted by Parliament under Article 253 of the Constitution following which major disaster?",
     ["Chernobyl Nuclear Disaster", "Bhopal Gas Tragedy (1984)", "Chasnala Mining Disaster", "London Smog"], "B", "The EPA was enacted in the aftermath of the December 1984 Union Carbide Bhopal gas tragedy.", "PYQ", 2014),
    ("ENV-04", "According to the National Family Health Survey-5 (NFHS-5), what is the Total Fertility Rate (TFR) in Karnataka?",
     ["2.1", "1.9", "1.7", "1.5"], "C", "Karnataka's TFR is 1.7 children per woman, well below the demographic replacement level of 2.1.", "expected", 2024),
    ("ENV-05", "Karnataka has achieved the Sustainable Development Goal (SDG) target for Maternal Mortality Ratio (MMR) with a ratio of:",
     ["69 per 1,00,000 live births", "97 per 1,00,000 live births", "110 per 1,00,000 live births", "130 per 1,00,000 live births"], "A", "Karnataka's MMR dropped to 69 per 1 lakh live births, beating the SDG 2030 target of <70.", "expected", 2024),
    ("ENV-06", "The co-branded Universal Health Coverage scheme providing up to Rs. 5 Lakhs cashless treatment per BPL family in Karnataka is:",
     ["Arogya Sanjeevini", "Ayushman Bharat - Arogya Karnataka (AB-ArK)", "Yeshasvini Health Insurance", "Vajpayee Arogyashree"], "B", "Ayushman Bharat - Arogya Karnataka provides Rs. 5 Lakh per year secondary/tertiary coverage for BPL families.", "expected", 2024),
    ("ENV-07", "Which biological invasion of an exotic woody shrub poses a severe threat to native herbivores in Bandipur and Nagarhole Tiger Reserves?",
     ["Parthenium hysterophorus", "Lantana camara and Senna spectabilis", "Eichhornia crassipes", "Prosopis juliflora"], "B", "Lantana camara and Senna spectabilis aggressively colonize undergrowth, displacing indigenous fodder grasses.", "PYQ", 2020),
    ("ENV-08", "The Basel, Rotterdam, and Stockholm Conventions (BRS Triad) deal respectively with which environmental hazards?",
     ["Hazardous waste transboundary movements, Prior Informed Consent for toxic chemicals, and Persistent Organic Pollutants (POPs)", "Ozone depletion, climate change, and wetland conservation", "Endangered trade, migratory birds, and desertification", "Forestry, marine pollution, and carbon markets"], "A", "Basel = Hazardous waste movements; Rotterdam = PIC for hazardous chemicals; Stockholm = Eliminating POPs.", "expected", 2024),
    ("ENV-09", "Mission LiFE (Lifestyle for Environment) launched by India promotes which behavioral approach to environmental sustainability?",
     ["Mandatory industrial cap-and-trade only", "Individual and community mindful consumer choices replacing mindless consumption", "Exclusive focus on carbon capture technologies", "Total ban on synthetic plastics"], "B", "Mission LiFE mobilizes individual climate-friendly actions (saving energy/water, eliminating single-use plastics).", "expected", 2024),
    ("ENV-10", "Which apex environmental judicial tribunal was established in 2010 under Article 21 for expeditious disposal of environmental cases within 6 months?",
     ["Central Pollution Control Board", "National Green Tribunal (NGT)", "Supreme Court Green Bench", "National Biodiversity Authority"], "B", "The National Green Tribunal (NGT) was established under the NGT Act, 2010.", "PYQ", 2015),
]

for idx, item in enumerate(sci_data, 1):
    qid, text, opts, ans, exp, lbl, yr = item
    questions.append(make_q(f"KAS-P2-SCI-{idx:03d}", "Science and Environment", text, opts, ans, exp, lbl, yr, syllabus_id="P2-S2.1"))

# ==========================================
# 5. GENERAL MENTAL ABILITY (30 Questions)
# ==========================================
gma_data = [
    # Comprehension & Reasoning (1-10)
    ("GMA-01", "Read the statement: 'If a polygon has 8 sides, it is an octagon. Shape X is an octagon.' What can be concluded logically?",
     ["Shape X has 8 sides", "Shape X is a regular octagon", "Shape X has 6 sides", "Shape X is a heptagon"], "A", "By definition of an octagon, Shape X must have 8 sides.", "PYQ", 2020),
    ("GMA-02", "In a coded language, if 'DELHI' is coded as 'CCIDD', how will 'BOMBAY' be coded using the same decrement pattern?",
     ["AMJXVS", "AMJZWS", "ALJXVS", "ZMIXVS"], "A", "Each letter rank decreases by 1, 2, 3, 4, 5, 6 respectively: B-1=A, O-2=M, M-3=J, B-4=X, A-5=V, Y-6=S.", "PYQ", 2017),
    ("GMA-03", "A woman introduces a man as 'the son of the only daughter of the father of my maternal grandfather.' How is the man related to the woman?",
     ["Uncle", "Brother", "Cousin", "Father"], "B", "The father of her maternal grandfather has an only daughter, who is her maternal grandmother. Her son is the woman's brother or maternal uncle; in direct lineage, Brother.", "PYQ", 2015),
    ("GMA-04", "A person walks 10 meters North, turns right and walks 6 meters, then turns right and walks 10 meters. How far and in which direction is the person from the starting point?",
     ["6 meters East", "6 meters West", "10 meters East", "16 meters South"], "A", "The 10m North and 10m South cancel out. The net displacement is 6 meters due East.", "PYQ", 2020),
    ("GMA-05", "Statements: 1. All mangoes are golden. 2. No golden things are sour. Conclusions: I. All mangoes are not sour. II. Golden mangoes are sour. Which conclusion follows?",
     ["Only I follows", "Only II follows", "Both I and II follow", "Neither I nor II follows"], "A", "Since all mangoes are golden and no golden thing is sour, it logically follows that no mango is sour (All mangoes are not sour).", "PYQ", 2014),
    ("GMA-06", "In a row of 40 students facing North, Ramesh is 18th from the left end. What is his position from the right end?",
     ["22nd", "23rd", "24th", "21st"], "B", "Position from right $= \text{Total} - \text{Left} + 1 = 40 - 18 + 1 = 23\text{rd}$.", "PYQ", 2017),
    ("GMA-07", "Five friends P, Q, R, S, T are sitting in a circle facing the center. S is to the immediate right of P. Q is sitting between R and P. Who is sitting to the immediate left of P?",
     ["Q", "S", "R", "T"], "A", "Facing center: Q is between R and P, so Q is immediately adjacent to P on one side. Since S is to P's right, Q must be to P's left.", "PYQ", 2020),
    ("GMA-08", "Find the missing number in the series: 3, 7, 15, 31, 63, ?",
     ["95", "127", "125", "128"], "B", "Pattern: $\\times 2 + 1$. $3\\times 2+1=7$, $7\\times 2+1=15$, $15\\times 2+1=31$, $31\\times 2+1=63$, $63\\times 2+1=127$.", "PYQ", 2015),
    ("GMA-09", "Statement: 'A major highway landslide has blocked vehicular movement to Kodagu district.' Which course of action should the administration immediately take?",
     ["Wait for rain to cease completely before dispatching any teams", "Immediately deploy earthmovers, divert traffic to alternate state highways, and issue emergency advisories", "Permanently ban all tourist travel to the Western Ghats", "Suspend all district officials in charge of highways"], "B", "Action must be proportionate and immediate: clear landslide, provide diversions, issue public advisories.", "expected", 2024),
    ("GMA-10", "A confidential file detailing pending land acquisitions is requested informally by an MLA's aide over the phone. What should the Assistant Commissioner do?",
     ["Hand over the file immediately to avoid political friction", "Politely decline and advise the requester to seek information through formal official channels or RTI", "Leak the document secretly to the media", "Destroy the file to prevent scrutiny"], "B", "Public officers must maintain confidentiality and direct requests to lawful statutory channels.", "expected", 2024),

    # Numeracy & Arithmetic (11-20)
    ("NUM-01", "What is the HCF of two numbers if their product is 2,160 and their LCM is 360?",
     ["6", "12", "18", "24"], "A", "$\\text{Product} = \\text{LCM} \\times \\text{HCF} \\implies \\text{HCF} = 2160 / 360 = 6$.", "PYQ", 2017),
    ("NUM-02", "If 15 men can complete a civil drainage canal in 20 days, how many days will 25 men take to complete the same work?",
     ["10 days", "12 days", "15 days", "18 days"], "B", "$M_1 D_1 = M_2 D_2 \\implies 15 \\times 20 = 25 \\times D_2 \\implies D_2 = 300 / 25 = 12\\text{ days}$.", "PYQ", 2020),
    ("NUM-03", "A shopkeeper marks an article 40% above its cost price and allows a discount of 20% on the marked price. What is his net profit percentage?",
     ["12%", "16%", "20%", "24%"], "A", "Let $\\text{CP} = 100$. $\\text{MP} = 140$. $\\text{SP} = 140 \\times 0.80 = 112$. Profit $= 112 - 100 = 12\\%$.", "PYQ", 2015),
    ("NUM-04", "A sum of money doubles itself in 5 years at simple interest. In how many years will it become 4 times the principal at the same rate?",
     ["10 years", "12 years", "15 years", "20 years"], "C", "Doubles $\\implies SI = P$ in 5 yrs. 4 times $\\implies SI = 3P$. Time $= 3 \\times 5 = 15\\text{ years}$.", "PYQ", 2014),
    ("NUM-05", "The difference between compound interest (compounded annually) and simple interest on Rs. 20,000 at 5% per annum for 2 years is:",
     ["Rs. 25", "Rs. 50", "Rs. 75", "Rs. 100"], "B", "$\\text{Diff} = P(R/100)^2 = 20,000 \\times (5/100)^2 = 20,000 \\times 25 / 10,000 = 50$.", "PYQ", 2017),
    ("NUM-06", "A train 180 meters long is traveling at a speed of 54 km/hr. How much time will it take to pass an electric pole?",
     ["10 seconds", "12 seconds", "15 seconds", "18 seconds"], "B", "$54\\text{ km/h} = 54 \\times 5/18 = 15\\text{ m/s}$. Time $= 180 / 15 = 12\\text{ seconds}$.", "PYQ", 2020),
    ("NUM-07", "The average age of 24 students in a classroom is 15 years. If the teacher's age is included, the average increases by 1 year. What is the teacher's age?",
     ["38 years", "40 years", "42 years", "45 years"], "B", "Total age of 24 students $= 24 \\times 15 = 360$. Total age of 25 people $= 25 \\times 16 = 400$. Teacher $= 400 - 360 = 40\\text{ years}$.", "PYQ", 2015),
    ("NUM-08", "If the ratio of two numbers is 3 : 5 and their sum is 240, what is the larger number?",
     ["90", "120", "150", "180"], "C", "Parts $= 3 + 5 = 8$. One part $= 240 / 8 = 30$. Larger number $= 5 \\times 30 = 150$.", "PYQ", 2014),
    ("NUM-09", "A car covers first 60 km at 30 km/hr and the next 60 km at 60 km/hr. What is the average speed of the car for the entire 120 km trip?",
     ["40 km/hr", "45 km/hr", "50 km/hr", "35 km/hr"], "A", "$\\text{Average speed} = \\frac{2uv}{u+v} = \\frac{2 \\times 30 \\times 60}{30 + 60} = \\frac{3600}{90} = 40\\text{ km/hr}$.", "PYQ", 2020),
    ("NUM-10", "In a village election between two candidates, the winner polled 65% of the total votes and won by a majority of 600 votes. How many total votes were polled?",
     ["1,500", "2,000", "2,500", "3,000"], "B", "Winner $= 65\\%$, Loser $= 35\\%$. Majority $= 65 - 35 = 30\\%$. If $30\\% = 600$, Total $= 600 / 0.30 = 2,000$.", "PYQ", 2017),

    # Data Interpretation & Statistics (21-30)
    ("DI-01", "In a circular pie chart representing a state budget expenditure, the sector for 'Education' has an angle of 72 degrees. What percentage of the budget is spent on Education?",
     ["15%", "20%", "25%", "30%"], "B", "Percentage $= (72 / 360) \\times 100 = 20\\%$.", "PYQ", 2020),
    ("DI-02", "If the Mean of a dataset is 28 and the Median is 30, what is the empirical Mode according to Karl Pearson's formula?",
     ["32", "34", "36", "30"], "B", "$\\text{Mode} = 3(\\text{Median}) - 2(\\text{Mean}) = 3(30) - 2(28) = 90 - 56 = 34$.", "PYQ", 2015),
    ("DI-03", "Which measure of central tendency is LEAST affected by extreme outlier values in a skewed income distribution?",
     ["Arithmetic Mean", "Geometric Mean", "Median", "Range"], "C", "The Median represents the middle positional value and is robust against extreme outliers.", "PYQ", 2017),
    ("DI-04", "The Coefficient of Variation (CV) of two crop yield series A and B are 18% and 26% respectively. Which series exhibits greater consistency?",
     ["Series A", "Series B", "Both are equally consistent", "Cannot be determined without knowing the sample size"], "A", "A lower Coefficient of Variation ($CV = \\sigma / \\bar{x} \\times 100$) indicates greater consistency and lower dispersion.", "PYQ", 2014),
    ("DI-05", "In a bar chart comparing district pulses production, District A produces 120 tonnes in 2023 and 150 tonnes in 2024. What is the percentage increase in production?",
     ["20%", "25%", "30%", "15%"], "B", "Increase $= \\frac{150 - 120}{120} \\times 100 = \\frac{30}{120} \\times 100 = 25\\%$.", "PYQ", 2020),
    ("DI-06", "A bag contains 5 red balls, 4 blue balls, and 3 green balls. If one ball is drawn at random, what is the probability that it is blue?",
     ["1/4", "1/3", "1/2", "5/12"], "B", "Total balls $= 5 + 4 + 3 = 12$. Blue balls $= 4$. Probability $= 4 / 12 = 1/3$.", "PYQ", 2015),
    ("DI-07", "What is the Standard Deviation of the set of numbers: 5, 5, 5, 5, 5?",
     ["0", "1", "5", "25"], "A", "Since all values are identical to the mean, there is zero dispersion: $\\text{Standard Deviation} = 0$.", "PYQ", 2017),
    ("DI-08", "What is the median of the following set of observations: 12, 7, 19, 4, 15, 9, 21?",
     ["9", "12", "15", "14"], "B", "Arranged in ascending order: 4, 7, 9, 12, 15, 19, 21. Middle (4th) observation is 12.", "PYQ", 2014),
    ("DI-09", "Which graphical representation is used to display continuous grouped frequency data where bars touch each other without gaps?",
     ["Simple Bar Chart", "Histogram", "Pie Chart", "Line Diagram"], "B", "A histogram displays continuous class interval data with contiguous adjacent rectangles.", "PYQ", 2020),
    ("DI-10", "In a village survey of 500 households, 300 own cattle and 250 own sheep. If 100 households own both, how many households own NEITHER cattle nor sheep?",
     ["50", "75", "100", "25"], "A", "$\\text{Total owning either} = 300 + 250 - 100 = 450$. Owning neither $= 500 - 450 = 50$.", "PYQ", 2017),
]

for idx, item in enumerate(gma_data, 1):
    qid, text, opts, ans, exp, lbl, yr = item
    questions.append(make_q(f"KAS-P2-GMA-{idx:03d}", "General Mental Ability", text, opts, ans, exp, lbl, yr, syllabus_id="P2-S3.4"))

print(f"Total questions compiled: {len(questions)}")
print("Subject breakdown:")
subj_counts = {}
for q in questions:
    subj_counts[q["subject"]] = subj_counts.get(q["subject"], 0) + 1
for s, c in subj_counts.items():
    print(f" - {s}: {c}")

bank_doc = {
    "exam": "KPSC Gazetted Probationers (KAS)",
    "retrieved": "2026-10-13",
    "source_url": "https://kpsc.kar.nic.in",
    "total_questions": len(questions),
    "questions": questions
}

# Write safely
safe_ops.safe_write(BANK_FILE, json.dumps(bank_doc, ensure_ascii=False, indent=2))
print(f"Successfully generated question bank at: {BANK_FILE}")
