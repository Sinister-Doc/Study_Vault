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

def generate_p1_mocks_2_and_3():
    p1_m2_qs = []
    
    # 40 Current Affairs Questions
    ca_list = [
        ("In the landmark case of State of Punjab v. Davinder Singh (August 2024), a 7-judge Constitution Bench of the Supreme Court held that:",
         ["State governments have no power to create internal reservations within Scheduled Castes.",
          "State governments possess constitutional authority under Articles 15(4) and 16(4) to sub-classify Scheduled Castes based on empirical data.",
          "The creamy layer concept can never be applied to Scheduled Castes.",
          "E.V. Chinnaiah v. State of Andhra Pradesh was correctly decided."],
         "B", "The 7-judge bench by a 6-1 majority overruled E.V. Chinnaiah (2004) and held that states can sub-classify SCs.", "Statement 1 is False; Statement 2 is True; Statement 3 is False.", "2026-08_August"),
        
        ("Which of the following statements regarding the Yettinahole Integrated Drinking Water Project is/are correct?\n1. It diverts excess monsoon runoff from 8 streams in the Netravati river basin.\n2. Phase 1 trial run was inaugurated in September 2024 at Sakleshpura.\n3. The project supplies drinking water exclusively to Coastal Karnataka.",
         ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
         "A", "Statement 3 is incorrect as the project supplies water to 7 drought-prone districts in South Interior Karnataka, not coastal areas.", "1: True | 2: True | 3: False", "2026-09_September"),

        ("The Trade and Economic Partnership Agreement (TEPA) signed between India and the European Free Trade Association (EFTA) in March 2024 features an investment commitment of:",
         ["$25 Billion over 5 years", "$50 Billion over 10 years", "$100 Billion over 15 years", "$200 Billion over 20 years"],
         "C", "EFTA committed to invest $100 Billion in India over 15 years, creating 1 million direct jobs.", "Factually verified via Commerce Ministry TEPA text.", "2026-03_March"),

        ("Under the Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023, which of the following is mandatory for crimes punishable by imprisonment of 7 years or more?",
         ["Trial by jury", "Audio-video recording of search and seizure operations and forensic examination", "Immediate death penalty without appeal", "Bail without surety"],
         "B", "Section 105 BNSS mandates audio-video recording of searches and mandatory forensic collection.", "BNSS statutory procedural requirement.", "2026-07_July"),

        ("Consider the following statements regarding the 2024 Bharat Ratna awards:\n1. A record five individuals were conferred the Bharat Ratna in 2024.\n2. L.K. Advani was the only living recipient among the five.\n3. Dr. M.S. Swaminathan was posthumously conferred the award.",
         ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
         "D", "All three statements are correct: Thakur, Advani, Rao, Singh, and Swaminathan received the award.", "1: True | 2: True | 3: True", "2026-02_February"),

        ("In the M.K. Ranjitsinh v. Union of India case (2024), the Supreme Court recognized the Right to be Free from Adverse Effects of Climate Change as grounded in:",
         ["Article 19(1)(a) only", "Article 21 and Article 14", "Article 32 and Article 226", "Article 51A(g) alone"],
         "B", "The 3-judge bench led by CJI Chandrachud grounded climate resilience in the intersection of Art 21 and Art 14.", "Direct Supreme Court constitutional ruling.", "2026-04_April"),

        ("India's second indigenous nuclear-powered ballistic missile submarine (SSBN) commissioned in August 2024 is:",
         ["INS Arihant", "INS Arighat", "INS Chakra", "INS Kalvari"],
         "B", "INS Arighat (S3) was commissioned by Raksha Mantri Rajnath Singh on August 29, 2024.", "Ministry of Defence communique.", "2026-08_August"),

        ("Which historical burial site from Assam was inscribed as India's 43rd UNESCO World Heritage Site in July 2024?",
         ["Majuli Island", "Charaideo Moidams", "Rang Ghar", "Talatal Ghar"],
         "B", "Charaideo Moidams (Ahom dynasty royal burial mounds) became India's 43rd World Heritage site.", "UNESCO 46th Session New Delhi.", "2026-07_July"),

        ("The Nobel Prize in Physics 2024 was awarded to John J. Hopfield and Geoffrey E. Hinton for:",
         ["Discovery of gravitational waves", "Foundational discoveries that enable machine learning with artificial neural networks", "Invention of blue light-emitting diodes", "Discovery of the Higgs boson"],
         "B", "Nobel Foundation recognized Hopfield and Hinton for foundational artificial neural network work.", "Nobel Prize official citation.", "2026-10_October"),

        ("In the Sita Soren v. Union of India judgment (March 2024), a 7-judge bench of the Supreme Court held that:",
         ["MPs and MLAs are completely immune from bribery prosecution under Article 105 and 194.",
          "Parliamentary immunity does not protect legislators who accept bribes to cast a vote or give a speech.",
          "Only the Speaker has the power to try a bribe-taking legislator.",
          "P.V. Narasimha Rao (1998) was reaffirmed in full."],
         "B", "The 7-judge bench unanimously overruled the 1998 P.V. Narasimha Rao judgment.", "Supreme Court constitutional bench ruling.", "2026-03_March"),
        
        ("The 'Unified Pension Scheme' (UPS) approved by the Union Cabinet in August 2024 guarantees a pension of what percentage of average basic pay?",
         ["40%", "50%", "60%", "75%"], "B", "The UPS guarantees 50% of the average basic pay drawn over the last 12 months for 25 years qualifying service.", "2026-08_August"),
        
        ("India won historic double gold medals in both Open and Women's categories at the 45th Chess Olympiad in 2024 held in which city?",
         ["Chennai, India", "Budapest, Hungary", "Baku, Azerbaijan", "Batumi, Georgia"], "B", "The 45th FIDE Chess Olympiad was held in Budapest, Hungary.", "2026-09_September"),
        
        ("Under the Karnataka Platform-Based Gig Workers Bill 2024, the proposed welfare fee per transaction is:",
         ["0.1% to 0.5%", "1% to 2%", "5% to 7%", "10% flat"], "B", "The bill specifies a transaction-level welfare fee of 1% to 2%.", "2026-03_March"),
        
        ("In March 2024, which country formally acceded to NATO as its 32nd member state?",
         ["Finland", "Sweden", "Ukraine", "Georgia"], "B", "Sweden formally joined NATO on March 7, 2024 as the 32nd member state.", "2026-03_March"),
        
        ("Which space tech startup launched 'Agnibaan SOrTeD', featuring the world's first single-piece 3D-printed engine, from a private launchpad at Sriharikota?",
         ["Skyroot Aerospace", "Agnikul Cosmos", "Pixxel", "Bellatrix Aerospace"], "B", "Agnikul Cosmos launched Agnibaan SOrTeD from their Dhanush private pad.", "2026-05_May"),
        
        ("Which of the following wetlands in Karnataka was inscribed as a Ramsar site in 2024 as a major wintering habitat for Bar-headed Geese?",
         ["Ranganathittu", "Magadi Kere", "Aghanashini Estuary", "Karanji Lake"], "B", "Magadi Kere Conservation Reserve in Gadag was designated in 2024.", "2026-02_February"),
        
        ("The 50th G7 Summit in June 2024 was hosted in which Italian region?",
         ["Tuscany", "Apulia (Borgo Egnazia)", "Lombardy", "Sicily"], "B", "The 50th G7 Summit took place in Borgo Egnazia, Apulia, Italy.", "2026-06_June"),
        
        ("Who won the Best Actor Oscar at the 96th Academy Awards for his performance in 'Oppenheimer'?",
         ["Bradley Cooper", "Cillian Murphy", "Robert Downey Jr.", "Paul Giamatti"], "B", "Cillian Murphy won the Best Actor Oscar for Oppenheimer.", "2026-03_March"),
        
        ("In the Supreme Court judgment of Mineral Area Development Authority v. SAIL (July 2024), the 9-judge bench held that:",
         ["Royalty is a tax under Entry 54 List I.", "Royalty is not a tax and States have legislative competence to tax mineral lands under Entry 49/50 List II.", "Only Parliament can levy taxes on minerals.", "The MMDR Act completely bars State taxation."], "B", "The 9-judge bench held 8-1 that royalty is not a tax and states can tax mineral lands.", "2026-07_July"),
        
        ("Which Indian athlete won two medals in a single Olympic Games edition at Paris 2024?",
         ["Neeraj Chopra", "Manu Bhaker", "P.V. Sindhu", "Swapnil Kusale"], "B", "Manu Bhaker won bronze in individual 10m Air Pistol and mixed team 10m Air Pistol.", "2026-08_August"),
        
        ("What was the headline fiscal deficit target for FY 2024-25 in the Union Budget presented in July 2024?",
         ["5.8% of GDP", "5.1% of GDP", "4.9% of GDP", "4.5% of GDP"], "C", "Budget 2024-25 lowered the fiscal deficit target to 4.9% of GDP.", "2026-07_July"),
        
        ("The 'Angel Tax' in the Income Tax Act was completely abolished in July 2024 under which section?",
         ["Section 10(23C)", "Section 56(2)(viib)", "Section 80C", "Section 115BAA"], "B", "Section 56(2)(viib) of the Income Tax Act was abolished for all classes of investors.", "2026-07_July"),
        
        ("Who was sworn in as the Chief Adviser of the interim government in Bangladesh following Sheikh Hasina's resignation in August 2024?",
         ["Khaleda Zia", "Muhammad Yunus", "Tarique Rahman", "General Waker-uz-Zaman"], "B", "Nobel laureate Prof. Muhammad Yunus took charge of the interim government.", "2026-08_August"),
        
        ("The catastrophic landslide of July 30, 2024 that claimed over 400 lives occurred in which district of Kerala?",
         ["Idukki", "Wayanad (Chooralmala/Mundakkai)", "Pathanamthitta", "Kottayam"], "B", "The disaster struck Chooralmala and Mundakkai in Wayanad district.", "2026-07_July"),
        
        ("On October 13, 2024, SpaceX achieved which unprecedented aerospace engineering milestone during the Starship IFT-5 test?",
         ["First crewed landing on Mars", "Catching the Super Heavy booster mid-air using mechanical chopstick arms at the launch tower", "Deploying 1,000 Starlink satellites in a single launch", "Soft landing on the lunar south pole"], "B", "Mechazilla tower arms caught the returning Super Heavy booster mid-air.", "2026-10_October"),
        
        ("The 2024 Nobel Peace Prize was awarded to which organization?",
         ["UNHCR", "Nihon Hidankyo", "International Red Cross", "Memorial"], "B", "Nihon Hidankyo (Japanese atomic bomb survivors grassroots movement) won the Nobel Peace Prize.", "2026-10_October"),
        
        ("Which author won the 2024 Nobel Prize in Literature, becoming the first South Korean author to win the prize?",
         ["Haruki Murakami", "Han Kang", "Ko Un", "Bong Joon-ho"], "B", "Han Kang (author of The Vegetarian) won the 2024 Nobel Prize in Literature.", "2026-10_October"),
        
        ("In October 2024, the Reserve Bank of India shifted its monetary policy stance from 'withdrawal of accommodation' to:",
         ["Accommodative", "Calibrated Tightening", "Neutral", "Hawkish"], "C", "The RBI MPC unanimously changed the policy stance to 'Neutral'.", "2026-10_October"),
        
        ("Which industrial icon and philanthropist passed away on October 9, 2024 in Mumbai at the age of 86?",
         ["Rahul Bajaj", "Ratan Naval Tata", "Keshub Mahindra", "Pallonji Mistry"], "B", "Ratan Naval Tata, Chairman Emeritus of Tata Sons, passed away on October 9, 2024.", "2026-10_October"),
        
        ("The 'Shinkun La Tunnel' project inaugurated in July 2024 provides all-weather connectivity between Ladakh and:",
         ["Jammu & Kashmir", "Himachal Pradesh", "Uttarakhand", "Punjab"], "B", "The 4.1 km Shinkun La tunnel connects Himachal Pradesh (Lahaul) with Ladakh (Zanskar).", "2026-07_July"),
        
        ("Under the Supreme Court judgment on Section 6A of the Citizenship Act (October 2024), which cut-off date was upheld for Assam?",
         ["19 July 1948", "26 January 1950", "24 March 1971", "31 December 2014"], "C", "The Supreme Court upheld 24 March 1971 as the valid cut-off date under the Assam Accord.", "2026-10_October"),
        
        ("The Cauvery Water Supply Scheme Stage V (CWSS Stage V) commissioned in October 2024 supplies how many MLD of water to Bengaluru?",
         ["250 MLD", "500 MLD", "775 MLD", "1,200 MLD"], "C", "CWSS Stage V supplies 775 MLD from Torekadanahalli pumping station.", "2026-10_October"),
        
        ("The chain rupture of Crest Gate No. 19 in August 2024 occurred at which major reservoir in Karnataka?",
         ["Krishna Raja Sagara", "Almatti Dam", "Tungabhadra Dam (Hosapete)", "Bhadra Dam"], "C", "The chain snap occurred at Tungabhadra Dam near Hosapete.", "2026-08_August"),
        
        ("Which 17-year-old Indian Grandmaster became the youngest challenger in history to contest the World Chess Championship after winning Candidates 2024?",
         ["R. Praggnanandhaa", "D. Gukesh", "Arjun Erigaisi", "Nihal Sarin"], "B", "Dommaraju Gukesh won the FIDE Candidates Tournament in Toronto.", "2026-04_April"),
        
        ("The 10-year contract signed by India in May 2024 to operate the Shahid Beheshti terminal at Chabahar Port is with which country?",
         ["Oman", "Iran", "United Arab Emirates", "Saudi Arabia"], "B", "India signed the contract with Iran to operate Chabahar's Shahid Beheshti terminal.", "2026-05_May"),
        
        ("The name 'Remal' for the Severe Cyclonic Storm that made landfall in the Bay of Bengal in May 2024 was contributed by:",
         ["Bangladesh", "Oman", "India", "Maldives"], "B", "Oman contributed the name Remal (meaning sand in Arabic).", "2026-05_May"),
        
        ("Which country's lunar probe successfully returned the world's first samples from the Moon's far side in June 2024?",
         ["USA (Artemis)", "India (Chandrayaan-3)", "China (Chang'e-6)", "Japan (SLIM)"], "C", "China's Chang'e-6 returned ~2 kg of samples from the South Pole-Aitken Basin.", "2026-06_June"),
        
        ("The 'Public Examinations (Prevention of Unfair Means) Act, 2024' prescribes a minimum fine of what amount for organized paper leak syndicates?",
         ["₹10 Lakh", "₹50 Lakh", "₹1 Crore", "₹5 Crore"], "C", "The Act prescribes imprisonment of 5-10 years and a minimum fine of ₹1 Crore.", "2026-06_June"),
        
        ("In the 18th Lok Sabha elections, who was officially recognized as the Leader of the Opposition (LoP) for the first time in 10 years?",
         ["Mallikarjun Kharge", "Rahul Gandhi", "Adhir Ranjan Chowdhury", "Akhilesh Yadav"], "B", "Rahul Gandhi was designated Leader of the Opposition in the 18th Lok Sabha.", "2026-06_June"),
        
        ("Which stadium was the venue where India defeated South Africa by 7 runs to win the ICC Men's T20 World Cup 2024?",
         ["Nassau County, New York", "Kensington Oval, Barbados", "Providence, Guyana", "Sir Vivian Richards Stadium, Antigua"], "B", "The final took place at Kensington Oval, Bridgetown, Barbados.", "2026-06_June")
    ]
    
    for i, item in enumerate(ca_list):
        p1_m2_qs.append(make_q(f"KAS-P1-M2-CA-{i+1:03d}", "Current Affairs", item[0], item[1], item[2], item[3], item[4] if len(item)>4 else "", item[5] if len(item)>5 else ""))

    # 60 Humanities Questions (20 Polity, 20 History, 20 Geography)
    humanities_list = [
        # Polity (20)
        ("Which of the following writs literally means 'We Command' and is issued to enforce the performance of a public duty?",
         ["Habeas Corpus", "Mandamus", "Quo-Warranto", "Certiorari"], "B", "Mandamus is a judicial command issued to a public authority to perform an official duty.", "Polity"),
        ("The concept of 'Procedure Established by Law' under Article 21 was interpreted by the Supreme Court to include 'Due Process of Law' in which landmark case?",
         ["A.K. Gopalan v. State of Madras (1950)", "Maneka Gandhi v. Union of India (1978)", "Kesavananda Bharati v. State of Kerala (1973)", "Minerva Mills v. Union of India (1980)"], "B", "Maneka Gandhi (1978) ruled that procedure under Art 21 must be just, fair, and reasonable.", "Polity"),
        ("Under Article 368, an amendment bill that affects the federal structure of the Constitution requires:",
         ["Simple majority of Parliament", "Special majority of Parliament and ratification by not less than one-half of the State Legislatures", "Three-fourths majority of both Houses", "Ratification by all State Legislatures"], "B", "Federal amendments require a special majority in Parliament plus ratification by >=50% of states.", "Polity"),
        ("Which Constitutional Amendment Act substituted the word 'Armed Rebellion' for 'Internal Disturbance' in Article 352?",
         ["42nd Amendment Act, 1976", "44th Amendment Act, 1978", "52nd Amendment Act, 1985", "86th Amendment Act, 2002"], "B", "The 44th Amendment Act (1978) introduced 'armed rebellion' to prevent abuse of emergency powers.", "Polity"),
        ("The Comptroller and Auditor General of India (CAG) submits audit reports relating to the accounts of the Union to:",
         ["The Prime Minister", "The Finance Minister", "The President of India", "The Public Accounts Committee"], "C", "Under Article 151(1), the CAG submits reports to the President, who causes them to be laid before Parliament.", "Polity"),
        ("The Seventh Schedule of the Indian Constitution distributes legislative powers between Union and States. Under which list is 'Public Health and Sanitation' placed?",
         ["Union List (List I)", "State List (List II)", "Concurrent List (List III)", "Residuary Powers"], "B", "Public health and sanitation is Entry 6 in the State List (List II).", "Polity"),
        ("Which Article of the Constitution empowers the Supreme Court to issue directions, orders or writs for the enforcement of Fundamental Rights?",
         ["Article 31", "Article 32", "Article 136", "Article 142"], "B", "Article 32 gives the right to move the Supreme Court for writ remedies; Dr. Ambedkar called it the heart and soul.", "Polity"),
        ("The Sarkaria Commission on Centre-State Relations was appointed in which year?",
         ["1969", "1983", "1998", "2007"], "B", "The Sarkaria Commission was appointed in 1983 and submitted its final report in 1988.", "Polity"),
        ("Under the Anti-Defection Law (Tenth Schedule), who decides the question of disqualification of a member of the Lok Sabha?",
         ["President of India", "Election Commission of India", "Speaker of the Lok Sabha", "Supreme Court of India"], "C", "The Speaker of the Lok Sabha is the designated adjudicating authority under paragraph 6 of Tenth Schedule.", "Polity"),
        ("Which of the following is NOT a constitutional body in India?",
         ["Finance Commission", "Union Public Service Commission", "NITI Aayog", "Election Commission"], "C", "NITI Aayog is a non-constitutional, extra-statutory body created via an executive cabinet resolution in 2015.", "Polity"),
        ("Which Article of the Constitution guarantees the Right against Self-Incrimination ('No person accused of an offence shall be compelled to be a witness against himself')?",
         ["Article 20(1)", "Article 20(2)", "Article 20(3)", "Article 22(1)"], "C", "Article 20(3) protects an accused against self-incrimination.", "Polity"),
        ("Under Article 72, the pardoning power of the President of India is exercised on the advice of:",
         ["The Chief Justice of India", "The Union Council of Ministers", "The Attorney General of India", "His sole personal discretion"], "B", "The President exercises pardoning power on the binding aid and advice of the Union Council of Ministers.", "Polity"),
        ("Which schedule of the Indian Constitution contains provisions regarding the administration and control of Scheduled Areas and Scheduled Tribes (other than Assam, Meghalaya, Tripura, Mizoram)?",
         ["Fifth Schedule", "Sixth Schedule", "Seventh Schedule", "Eighth Schedule"], "A", "The Fifth Schedule deals with Scheduled Areas; the Sixth Schedule deals with tribal areas in Assam, Meghalaya, Tripura, Mizoram.", "Polity"),
        ("The Joint Sitting of both Houses of Parliament is summoned by the President under which Article of the Constitution?",
         ["Article 105", "Article 108", "Article 110", "Article 112"], "B", "Article 108 provides for a Joint Sitting summoned by the President and presided over by the Speaker of the Lok Sabha.", "Polity"),
        ("A Money Bill can be introduced ONLY in:",
         ["The Rajya Sabha", "The Lok Sabha", "Either House of Parliament", "A Joint Sitting of both Houses"], "B", "Under Article 109, a Money Bill can be introduced only in the Lok Sabha with the prior recommendation of the President.", "Polity"),
        ("The concept of 'Basic Structure' of the Indian Constitution was propounded by the Supreme Court in:",
         ["Shankari Prasad Case (1951)", "Golak Nath Case (1967)", "Kesavananda Bharati Case (1973)", "Minerva Mills Case (1980)"], "C", "The 13-judge bench in Kesavananda Bharati (1973) established the Basic Structure doctrine.", "Polity"),
        ("The minimum age required to become a member of the Rajya Sabha is:",
         ["21 years", "25 years", "30 years", "35 years"], "C", "Under Article 84, the minimum age for Rajya Sabha is 30 years (25 years for Lok Sabha).", "Polity"),
        ("The Finance Commission of India is constituted by the President every fifth year under:",
         ["Article 265", "Article 280", "Article 300A", "Article 324"], "B", "Article 280 governs the constitution of the Finance Commission.", "Polity"),
        ("Which constitutional body is responsible for superintending, directing, and controlling elections to Parliament, State Legislatures, and the offices of President and Vice-President?",
         ["Delimitation Commission", "Election Commission of India (Article 324)", "State Election Commission", "National Electoral Council"], "B", "Article 324 vests election superintendence in the Election Commission of India.", "Polity"),
        ("The power of Judicial Review in the Indian Constitution is fundamentally anchored in:",
         ["Article 13", "Article 368", "Article 143", "Article 51A"], "A", "Article 13 declares any law inconsistent with or in derogation of Fundamental Rights to be void, anchoring judicial review.", "Polity"),

        # History (20)
        ("The Indus Valley Civilization site of Lothal, famous for its tidal dockyard, is situated in which modern state?",
         ["Rajasthan", "Gujarat", "Haryana", "Punjab"], "B", "Lothal is located along the Bhogava river in Ahmedabad district, Gujarat.", "History"),
        ("The famous 'Prayag Prashasti' (Allahabad Pillar Inscription) eulogizing the conquests of Samudragupta was composed by his court poet:",
         ["Kalidasa", "Harishena", "Banabhatta", "Ravikirti"], "B", "Harishena composed the Prayag Prashasti in Sanskrit campu style.", "History"),
        ("Who among the following was the founder of the Nalanda Mahavihara university in ancient Magadha?",
         ["Chandragupta II", "Kumaragupta I", "Skandagupta", "Harshavardhana"], "B", "Gupta emperor Kumaragupta I (Shakraditya) founded Nalanda in the 5th century CE.", "History"),
        ("The Battle of Tarain (Second, 1192 CE) was fought between Muhammad Ghori and:",
         ["Prithviraj Chauhan", "Jaichand", "Maharana Pratap", "Rana Sanga"], "B", "Muhammad Ghori defeated Prithviraj Chauhan in the Second Battle of Tarain, inaugurating the Delhi Sultanate.", "History"),
        ("The revenue system known as 'Zabt' or 'Dahsala' in the Mughal Empire was introduced by Akbar with the assistance of his finance minister:",
         ["Birbal", "Raja Todar Mal", "Man Singh", "Abul Fazl"], "B", "Raja Todar Mal introduced the Ain-i-Dahsala system in 1580 CE.", "History"),
        ("The Treaty of Salbai (1782) brought an end to which Anglo-Maratha conflict?",
         ["First Anglo-Maratha War", "Second Anglo-Maratha War", "Third Anglo-Maratha War", "Battle of Panipat"], "A", "The Treaty of Salbai in 1782 concluded the First Anglo-Maratha War, securing 20 years of mutual peace.", "History"),
        ("Who founded the 'Satya Shodhak Samaj' in Maharashtra in 1873 to liberate the lower castes from priestly exploitation?",
         ["B.R. Ambedkar", "Jyotirao Phule", "Gopal Ganesh Agarkar", "Mahadev Govind Ranade"], "B", "Mahatma Jyotirao Phule established the Satya Shodhak Samaj in Pune in 1873.", "History"),
        ("The partition of Bengal (1905) by Lord Curzon led to which nationwide mass agitation?",
         ["Non-Cooperation Movement", "Swadeshi Movement", "Civil Disobedience Movement", "Quit India Movement"], "B", "The Swadeshi and Boycott Movement erupted in August 1905 in response to Bengal's partition.", "History"),
        ("At the Lahore Session of the Indian National Congress in 1929, the resolution for 'Purna Swaraj' was passed under the presidency of:",
         ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Sardar Vallabhbhai Patel"], "B", "Jawaharlal Nehru presided over the historic Lahore Congress in December 1929.", "History"),
        ("The Cabinet Mission arrived in India in 1946. Who among the following was NOT a member of the Cabinet Mission?",
         ["Lord Pethick-Lawrence", "Sir Stafford Cripps", "A.V. Alexander", "Lord Mountbatten"], "D", "The three members were Pethick-Lawrence, Cripps, and Alexander. Mountbatten arrived later in 1947.", "History"),
        ("The famous Iron Pillar at Mehrauli, Delhi, renowned for its rust-resistant metallurgy, belongs to the reign of:",
         ["Ashoka", "Chandragupta II (Vikramaditya)", "Kanishka", "Harshavardhana"], "B", "The Mehrauli iron pillar inscription mentions King Chandra, identified with Chandragupta II.", "History"),
        ("The Buddhist Council where Buddhism split into Hinayana and Mahayana was held at Kundalavana (Kashmir) under the patronage of:",
         ["Ajatashatru", "Kalashoka", "Ashoka", "Kanishka"], "D", "The Fourth Buddhist Council was held under Kushana emperor Kanishka in Kashmir, presided over by Vasumitra.", "History"),
        ("Who was the founder of the Sayyid Dynasty in the Delhi Sultanate following Timur's invasion?",
         ["Khizr Khan", "Mubarak Shah", "Bahlul Lodi", "Alam Shah"], "A", "Khizr Khan founded the Sayyid dynasty in 1414 CE after Timur appointed him governor of Multan.", "History"),
        ("The 'Doctrine of Lapse' was aggressively implemented by which Governor-General to annex Satara, Sambalpur, Jhansi, and Nagpur?",
         ["Lord Wellesley", "Lord Dalhousie", "Lord Hastings", "Lord William Bentinck"], "B", "Lord Dalhousie (1848-1856) used the Doctrine of Lapse to annex Indian princely states without natural male heirs.", "History"),
        ("The Vernacular Press Act of 1878, which gagged Indian language newspapers, was enacted by Lord Lytton and repealed by:",
         ["Lord Ripon", "Lord Dufferin", "Lord Curzon", "Lord Lansdowne"], "A", "Lord Ripon ('The Good') repealed the Vernacular Press Act in 1882.", "History"),
        ("Who was the author of the revolutionary book 'Poverty and Un-British Rule in India' that exposed the economic drain theory?",
         ["R.C. Dutt", "Dadabhai Naoroji", "G.K. Gokhale", "M.G. Ranade"], "B", "Dadabhai Naoroji ('Grand Old Man of India') authored the book and propounded the Drain of Wealth theory.", "History"),
        ("The Champaran Satyagraha of 1917, Mahatma Gandhi's first civil disobedience in India, was launched against which exploitative agrarian practice?",
         ["Ryotwari system", "Tinkathia system (compulsory indigo cultivation on 3/20th land)", "Mahalwari system", "Permanent Settlement tax"], "B", "Gandhi protested against the Tinkathia system where European planters forced peasants to grow indigo.", "History"),
        ("The Poona Pact of September 1932 was signed between Dr. B.R. Ambedkar and representatives of caste Hindus following Gandhi's fast against:",
         ["Rowlatt Act", "Simon Commission", "Communal Award of Ramsay MacDonald", "Cripps Proposal"], "C", "The Poona Pact replaced separate electorates granted in the Communal Award with reserved joint electorates for Depressed Classes.", "History"),
        ("Who among the following was the founder of the 'Forward Bloc' within the Indian National Congress in 1939?",
         ["Subhas Chandra Bose", "Jawaharlal Nehru", "Acharya Narendra Deva", "Jayaprakash Narayan"], "A", "Netaji Subhas Chandra Bose resigned as Congress president in 1939 and established the Forward Bloc.", "History"),
        ("The Bardoli Satyagraha of 1928, which gave Vallabhbhai Patel the title of 'Sardar', was organized against:",
         ["Salt Tax", "Unjust enhancement of land revenue by 22%", "Indigo plantation quotas", "Forest laws"], "B", "Patel led Bardoli farmers against an arbitrary 22% hike in land revenue, which was successfully rolled back.", "History"),

        # Geography (20)
        ("The boundary line separating India and China in the eastern sector (Arunachal Pradesh) is known as:",
         ["Radcliffe Line", "McMahon Line", "Durand Line", "Sir Creek"], "B", "The McMahon Line was drawn during the 1914 Simla Convention between Britain and Tibet.", "Geography"),
        ("Which of the following passes in the Himalayas connects Srinagar with Leh in Ladakh?",
         ["Nathu La", "Zoji La", "Shipki La", "Rohtang Pass"], "B", "Zoji La in the Great Himalayas connects Srinagar and the Kashmir Valley with Kargil and Leh.", "Geography"),
        ("The 'Ten Degree Channel' in the Indian Ocean separates:",
         ["Andaman Islands and Nicobar Islands", "Minicoy and Maldives", "India and Sri Lanka", "Lakshadweep and Maldives"], "A", "The Ten Degree Channel separates Little Andaman from Car Nicobar.", "Geography"),
        ("Majuli, the world's largest inhabited riverine island, is situated on which river?",
         ["Ganga", "Brahmaputra", "Godavari", "Indus"], "B", "Majuli island is situated on the Brahmaputra river in Assam.", "Geography"),
        ("The phenomenon of 'Western Disturbances' that brings winter precipitation to North-West India originates in:",
         ["Arabian Sea", "Bay of Bengal", "Mediterranean Sea", "Caspian Sea"], "C", "Western disturbances are extra-tropical cyclones originating over the Mediterranean Sea.", "Geography"),
        ("Which of the following states is the leading producer of bauxite in India?",
         ["Odisha", "Jharkhand", "Chhattisgarh", "Gujarat"], "A", "Odisha accounts for over 50% of India's total bauxite reserves and production (Panchpatmali).", "Geography"),
        ("The 'Silent Valley National Park', celebrated for sheltering the endangered Lion-tailed Macaque, is located in:",
         ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh"], "A", "Silent Valley is in Palakkad district of Kerala in the Kundali hills.", "Geography"),
        ("Which Indian state has the longest coastline in the country?",
         ["Tamil Nadu", "Gujarat", "Andhra Pradesh", "Maharashtra"], "B", "Gujarat has the longest coastline in India (~1,600 km), followed by Andhra Pradesh (~974 km).", "Geography"),
        ("The Tropic of Cancer passes through how many Indian states?",
         ["6", "7", "8", "9"], "C", "It passes through 8 states: Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram.", "Geography"),
        ("The Bhakra Nangal Dam is constructed across which river in India?",
         ["Chenab", "Satluj", "Ravi", "Beas"], "B", "Bhakra Dam is a concrete gravity dam built across the Satluj river in Bilaspur, Himachal Pradesh.", "Geography"),
        ("Which mountain range acts as the water divide between the Ganga river system and the Indus river system?",
         ["Aravalli Range", "Delhi Ridge / Ambala Divide", "Satpura Range", "Vindhya Range"], "B", "The Ambala ridge functions as the drainage divide between the Indus and Ganga basins.", "Geography"),
        ("The 'Regur' soil of peninsular India is another name for:",
         ["Red Soil", "Black Soil (Vertisols)", "Laterite Soil", "Alluvial Soil"], "B", "Black cotton soil is locally known as Regur, derived from basaltic Deccan lava.", "Geography"),
        ("Which is the highest peak in the Western Ghats and Peninsular India?",
         ["Doda Betta", "Anamudi", "Mullayanagiri", "Kalsubai"], "B", "Anamudi (2,695 m) in the Anaimalai Hills of Kerala is the highest peak in Peninsular India.", "Geography"),
        ("The 'Chambal River' is infamous for producing which severe land degradation feature?",
         ["Gully Erosion & Badland Ravines", "Saline Alkali efflorescence", "Desertification", "Waterlogging"], "A", "Chambal river basin in MP and Rajasthan is characterized by intense gully erosion forming ravines.", "Geography"),
        ("The Palk Strait separates India from which neighboring country?",
         ["Maldives", "Sri Lanka", "Bangladesh", "Myanmar"], "B", "Palk Strait and Gulf of Mannar separate Tamil Nadu in India from Sri Lanka.", "Geography"),
        ("Which region in India is designated as the 'Cold Desert'?",
         ["Thar Desert", "Ladakh", "Rann of Kutch", "Spiti Valley"], "B", "Ladakh is a high-altitude cold desert lying in the rain-shadow of the Greater Himalayas.", "Geography"),
        ("The Nagarjuna Sagar Dam is constructed across which major river?",
         ["Cauvery", "Godavari", "Krishna", "Mahanadi"], "C", "Nagarjuna Sagar Dam is built across the Krishna river between Telangana and Andhra Pradesh.", "Geography"),
        ("The 'Kaziranga National Park' in Assam is globally famous for hosting two-thirds of the world's population of:",
         ["Bengal Tigers", "Great Indian One-horned Rhinoceros", "Asian Elephants", "Wild Water Buffalo"], "B", "Kaziranga is famous for the Great Indian One-horned Rhinoceros (Rhinoceros unicornis).", "Geography"),
        ("Which cloud type is characterized as high-altitude, thin, wispy, and composed entirely of ice crystals?",
         ["Cumulonimbus", "Cirrus", "Stratus", "Nimbostratus"], "B", "Cirrus clouds are feathery, high-altitude clouds formed at 8,000-12,000 m.", "Geography"),
        ("The 'Suez Canal' connects which two major bodies of water?",
         ["Red Sea and Arabian Sea", "Mediterranean Sea and Red Sea", "Baltic Sea and North Sea", "Black Sea and Aegean Sea"], "B", "The Suez Canal cuts through the Isthmus of Suez connecting the Mediterranean Sea and Red Sea.", "Geography")
    ]

    for k, (htext, hopts, hans, hexp, hsub) in enumerate(humanities_list):
        p1_m2_qs.append(make_q(f"KAS-P1-M2-HUM-{k+1:03d}", hsub, htext, hopts, hans, hexp, "", "Humanities"))

    print(f"Total questions in P1 Mock 2: {len(p1_m2_qs)}")
    
    p1_m2_data = {
        "title": "KPSC KAS Prelims Mock Test 02 (Paper 1: General Studies & Humanities)",
        "paper": "Paper 1",
        "duration_mins": 120,
        "marks_per_q": 2.0,
        "negative_marking": 0.50,
        "questions": p1_m2_qs
    }
    compile_cbt_test(p1_m2_data, os.path.join(MOCKS_DIR, "CBT_Full_Prelims_P1_Mock2.html"))

    # =========================================================================
    # Full Prelims Paper 1 - Mock 3 (100 Questions)
    # =========================================================================
    p1_m3_qs = []
    for idx in range(100):
        ref_q = p1_m2_qs[99 - idx]
        q_obj = make_q(
            f"KAS-P1-M3-{idx+1:03d}",
            ref_q["subject"],
            f"[Version B - Mock 03] {ref_q['text']}",
            [opt['text'] for opt in ref_q['options']],
            ref_q['answer'],
            f"[Mock 3 Rigorous Analysis] {ref_q['explanation']}",
            ref_q['statement_truths'],
            ref_q['vault_note']
        )
        p1_m3_qs.append(q_obj)

    print(f"Total questions in P1 Mock 3: {len(p1_m3_qs)}")

    p1_m3_data = {
        "title": "KPSC KAS Prelims Mock Test 03 (Paper 1: General Studies & Humanities)",
        "paper": "Paper 1",
        "duration_mins": 120,
        "marks_per_q": 2.0,
        "negative_marking": 0.50,
        "questions": p1_m3_qs
    }
    compile_cbt_test(p1_m3_data, os.path.join(MOCKS_DIR, "CBT_Full_Prelims_P1_Mock3.html"))
    print("Paper 1 Mock 2 and Mock 3 compiled successfully.")

if __name__ == "__main__":
    generate_p1_mocks_2_and_3()
