# -*- coding: utf-8 -*-
"""
Exhaustive Paper 1 Questions Dataset.
Contains:
- Test 1: 150 questions (S1: 20 GK, S2: 15 CA, S3: 25 Kannada, S4: 25 English, S5: 25 Ed Psych, S6: 20 Comp Lit, S7: 10 Health, S8: 10 Value Ed)
- Test 2: 150 questions (S1: 20 GK, S2: 15 CA, S3: 25 Kannada, S4: 25 English, S5: 25 Ed Psych, S6: 20 Comp Lit, S7: 10 Health, S8: 10 Value Ed)
Total = 300 Questions.
"""

def get_paper1_test1():
    qs = []
    
    # ----------------------------------------------------
    # SECTION 1: GENERAL KNOWLEDGE (20 QUESTIONS: Q1 to Q20)
    # ----------------------------------------------------
    gk = [
        {
            "id": "P1-T1-GK-01", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "Who among the following was the founder of the Kadamba dynasty of Banavasi?",
            "text_alt": "ಬನವಾಸಿಯ ಕದಂಬ ರಾಜವಂಶದ ಸಂಸ್ಥಾಪಕರು ಈ ಕೆಳಗಿನವರಲ್ಲಿ ಯಾರು?",
            "options": [{"label": "A", "text": "Mayurasharma"}, {"label": "B", "text": "Kakusthavarma"}, {"label": "C", "text": "Ravivarma"}, {"label": "D", "text": "Bhanuvarma"}],
            "answer": "A",
            "explanation": "Mayurasharma (c. 345–365 CE) founded the Kadamba dynasty of Banavasi after subduing the Pallavas, as recorded in the Talagunda pillar inscription."
        },
        {
            "id": "P1-T1-GK-02", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "The famous Aihole Inscription which records the achievements of Pulakeshin II was composed by which court poet?",
            "text_alt": "ಇಮ್ಮಡಿ ಪುಲಕೇಶಿಯ ಸಾಧನೆಗಳನ್ನು ದಾಖಲಿಸುವ ಪ್ರಸಿದ್ಧ ಐಹೊಳೆ ಶಾಸನವನ್ನು ರಚಿಸಿದ ಆಸ್ಥಾನ ಕವಿ ಯಾರು?",
            "options": [{"label": "A", "text": "Pampa"}, {"label": "B", "text": "Ravikirti"}, {"label": "C", "text": "Dandin"}, {"label": "D", "text": "Bilhana"}],
            "answer": "B",
            "explanation": "The Aihole inscription (634 CE) at the Meguti Jain temple was composed in Sanskrit by the Jain court poet Ravikirti."
        },
        {
            "id": "P1-T1-GK-03", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "easy",
            "text": "The earliest extant Kannada literary work 'Kavirajamarga' is attributed to which Rashtrakuta king?",
            "text_alt": "ಕನ್ನಡದ ಅತ್ಯಂತ ಪ್ರಾಚೀನ ಲಭ್ಯ ಸಾಹಿತ್ಯ ಕೃತಿ 'ಕವಿರಾಜಮಾರ್ಗ' ಯಾವ ರಾಷ್ಟ್ರಕೂಟ ದೊರೆಗೆ ಸಂಬಂಧಿಸಿದೆ?",
            "options": [{"label": "A", "text": "Dantidurga"}, {"label": "B", "text": "Krishna I"}, {"label": "C", "text": "Amoghavarsha Nrupatunga I"}, {"label": "D", "text": "Govinda III"}],
            "answer": "C",
            "explanation": "Kavirajamarga (c. 850 CE) was written during the reign of Rashtrakuta monarch Amoghavarsha I (with court poet Sri Vijaya contributing to its creation)."
        },
        {
            "id": "P1-T1-GK-04", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which Hoysala ruler built the magnificent Chennakeshava Temple at Belur to commemorate his victory over the Cholas in the Battle of Talakad?",
            "text_alt": "ತಲಕಾಡು ಕದನದಲ್ಲಿ ಚೋಳರ ಮೇಲಿನ ವಿಜಯದ ಸ್ಮರಣಾರ್ಥ ಬೇಲೂರಿನ ಚೆನ್ನಕೇಶವ ದೇವಾಲಯವನ್ನು ನಿರ್ಮಿಸಿದ ಹೊಯ್ಸಳ ದೊರೆ ಯಾರು?",
            "options": [{"label": "A", "text": "Vishnuvardhana (Bittideva)"}, {"label": "B", "text": "Veera Ballala II"}, {"label": "C", "text": "Narasimha I"}, {"label": "D", "text": "Somesvara"}],
            "answer": "A",
            "explanation": "Hoysala king Vishnuvardhana built the Vijayanarayana (Chennakeshava) temple at Belur in 1117 CE after capturing Talakad from the Cholas."
        },
        {
            "id": "P1-T1-GK-05", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "hard",
            "text": "In which year was the historic Battle of Talikota (Rakkasa-Tangadi) fought, leading to the collapse of the Vijayanagara Empire?",
            "text_alt": "ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯದ ಪತನಕ್ಕೆ ಕಾರಣವಾದ ಐತಿಹಾಸಿಕ ತಾಳಿಕೋಟೆ ಕಾಳಗ (ರಕ್ಕಸ-ತಂಗಡಿಗಿ) ಯಾವ ವರ್ಷದಲ್ಲಿ ನಡೆಯಿತು?",
            "options": [{"label": "A", "text": "1526 CE"}, {"label": "B", "text": "1556 CE"}, {"label": "C", "text": "1565 CE"}, {"label": "D", "text": "1576 CE"}],
            "answer": "C",
            "explanation": "The Battle of Talikota was fought on January 23, 1565, between the Vijayanagara army under Aliya Rama Raya and the combined Deccan Sultanates."
        },
        {
            "id": "P1-T1-GK-06", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Kittur Rani Chennamma led an armed rebellion against British East India Company rule in 1824 following the death of which British Collector of Dharwad?",
            "text_alt": "1824 ರಲ್ಲಿ ಕಿತ್ತೂರು ರಾಣಿ ಚೆನ್ನಮ್ಮ ಬ್ರಿಟಿಷರ ವಿರುದ್ಧ ನಡೆಸಿದ ದಂಗೆಯಲ್ಲಿ ಮಡಿದ ಧಾರವಾಡದ ಬ್ರಿಟಿಷ್ ಕಲೆಕ್ಟರ್ ಯಾರು?",
            "options": [{"label": "A", "text": "Thomas Munro"}, {"label": "B", "text": "St. John Thackeray"}, {"label": "C", "text": "Mark Cubbon"}, {"label": "D", "text": "Lord Elphinstone"}],
            "answer": "B",
            "explanation": "St. John Thackeray, Political Agent and Collector of Dharwad, was killed on October 23, 1824, when Kittur forces resisted British annexation under the Doctrine of Lapse."
        },
        {
            "id": "P1-T1-GK-07", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "Which historic event that occurred in Chikkaballapura district on 25 April 1938 is commemorated as the 'Jallianwala Bagh of Karnataka'?",
            "text_alt": "1938 ರ ಏಪ್ರಿಲ್ 25 ರಂದು ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಜಿಲ್ಲೆಯಲ್ಲಿ ನಡೆದ ಯಾವ ಘಟನೆಯನ್ನು 'ಕರ್ನಾಟಕದ ಜಲಿಯನ್ ವಾಲಾ ಬಾಗ್' ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Shivapura Flag Satyagraha"}, {"label": "B", "text": "Vidurashwatha Police Firing"}, {"label": "C", "text": "Isur Village Uprising"}, {"label": "D", "text": "Ankola Salt Satyagraha"}],
            "answer": "B",
            "explanation": "At Vidurashwatha on 25 April 1938, police opened fire on peaceful Congress satyagrahis gathered to unfurl the National Flag, killing over 10 people."
        },
        {
            "id": "P1-T1-GK-08", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Who authored the influential book 'Karnataka Gathavaibhava' (1917), which sparked the Karnataka Unification (Ekikarana) movement?",
            "text_alt": "ಕರ್ನಾಟಕ ಏಕೀಕರಣ ಚಳವಳಿಗೆ ಸ್ಫೂರ್ತಿ ನೀಡಿದ ಪ್ರಸಿದ್ಧ 'ಕರ್ನಾಟಕ ಗತವೈಭವ' (1917) ಕೃತಿಯ ಕರ್ತೃ ಯಾರು?",
            "options": [{"label": "A", "text": "Aluru Venkata Rao"}, {"label": "B", "text": "Huilgol Narayana Rao"}, {"label": "C", "text": "K. V. Puttappa (Kuvempu)"}, {"label": "D", "text": "Gorur Ramaswamy Iyengar"}],
            "answer": "A",
            "explanation": "Aluru Venkata Rao is revered as 'Karnataka Kulapurohita' for his seminal book 'Karnataka Gathavaibhava' which rekindled pride in Karnataka's glorious past."
        },
        {
            "id": "P1-T1-GK-09", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "easy",
            "text": "Which is the highest geographical peak in Karnataka?",
            "text_alt": "ಕರ್ನಾಟಕದ ಅತ್ಯುನ್ನತ ಭೌಗೋಳಿಕ ಶಿಖರ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Kudremukh"}, {"label": "B", "text": "Mullayanagiri"}, {"label": "C", "text": "Tadiandamol"}, {"label": "D", "text": "Pushpagiri"}],
            "answer": "B",
            "explanation": "Mullayanagiri in the Chandra Drona / Baba Budangiri range of Chikkamagaluru district is the highest peak in Karnataka with an altitude of 1,930 metres (6,332 ft)."
        },
        {
            "id": "P1-T1-GK-10", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "The famous Jog Falls (Gersoppa Falls) in Shivamogga district is created by which river?",
            "text_alt": "ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ಪ್ರಸಿದ್ಧ ಜೋಗ ಜಲಪಾತ (ಗೇರುಸೊಪ್ಪೆ) ಯಾವ ನದಿಯಿಂದ ನಿರ್ಮಾಣಗೊಂಡಿದೆ?",
            "options": [{"label": "A", "text": "Netravati"}, {"label": "B", "text": "Sharavathi"}, {"label": "C", "text": "Kali"}, {"label": "D", "text": "Aghanashini"}],
            "answer": "B",
            "explanation": "Jog Falls on the Sharavathi River drops 253 metres (830 ft) across four distinct cascades: Raja, Roarer, Rocket, and Rani."
        },
        {
            "id": "P1-T1-GK-11", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Which mountain pass (Ghat) in the Western Ghats connects Mangaluru with Sakleshpur and Hassan?",
            "text_alt": "ಪಶ್ಚಿಮ ಘಟ್ಟಗಳಲ್ಲಿ ಮಂಗಳೂರನ್ನು ಸಕಲೇಶಪುರ ಮತ್ತು ಹಾಸನಕ್ಕೆ ಸಂಪರ್ಕಿಸುವ ಘಾಟಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Charmadi Ghat"}, {"label": "B", "text": "Shiradi Ghat"}, {"label": "C", "text": "Agumbe Ghat"}, {"label": "D", "text": "Hulikal Ghat"}],
            "answer": "B",
            "explanation": "Shiradi Ghat (NH 75) connects Mangaluru with Hassan/Sakleshpur; Charmadi Ghat connects Mangaluru with Mudigere/Chikkamagaluru."
        },
        {
            "id": "P1-T1-GK-12", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "Which bird sanctuary in Mandya district was declared as Karnataka's first Ramsar Wetland Site of International Importance in 2022?",
            "text_alt": "2022 ರಲ್ಲಿ ಕರ್ನಾಟಕದ ಪ್ರಪ್ರಥಮ ರಾಮ್ಸರ್ ಜೌಗು ಪ್ರದೇಶವೆಂದು ಘೋಷಿಸಲ್ಪಟ್ಟ ಮಂಡ್ಯ ಜಿಲ್ಲೆಯ ಪಕ್ಷಿಧಾಮ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Gudavi Bird Sanctuary"}, {"label": "B", "text": "Ranganathittu Bird Sanctuary"}, {"label": "C", "text": "Mandagadde Bird Sanctuary"}, {"label": "D", "text": "Magadi Kere Bird Sanctuary"}],
            "answer": "B",
            "explanation": "Ranganathittu Bird Sanctuary along the Cauvery River in Mandya district was designated as Karnataka's 1st Ramsar site in August 2022."
        },
        {
            "id": "P1-T1-GK-13", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "easy",
            "text": "Which Article of the Constitution of India provides for the 'Right to Constitutional Remedies', described by Dr. B. R. Ambedkar as the 'Heart and Soul' of the Constitution?",
            "text_alt": "ಡಾ. ಬಿ. ಆರ್. ಅಂಬೇಡ್ಕರ್ ಅವರು ಸಂವಿಧಾನದ 'ಹೃದಯ ಮತ್ತು ಆತ್ಮ' ಎಂದು ಕರೆದ 'ಸಾಂವಿಧಾನಿಕ ಪರಿಹಾರಗಳ ಹಕ್ಕು' ಭಾರತ ಸಂವಿಧಾನದ ಯಾವ ವಿಧಿಯಲ್ಲಿದೆ?",
            "options": [{"label": "A", "text": "Article 19"}, {"label": "B", "text": "Article 21"}, {"label": "C", "text": "Article 32"}, {"label": "D", "text": "Article 226"}],
            "answer": "C",
            "explanation": "Article 32 confers the right to move the Supreme Court by appropriate proceedings for the enforcement of Fundamental Rights."
        },
        {
            "id": "P1-T1-GK-14", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "Under which Constitutional Amendment Act was Article 21A (Right to Free and Compulsory Education) inserted into the Indian Constitution?",
            "text_alt": "ಭಾರತದ ಸಂವಿಧಾನಕ್ಕೆ 21ಎ ವಿಧಿಯನ್ನು (ಉಚಿತ ಮತ್ತು ಕಡ್ಡಾಯ ಶಿಕ್ಷಣದ ಹಕ್ಕು) ಯಾವ ಸಂವಿಧಾನ ತಿದ್ದುಪಡಿ ಕಾಯ್ದೆಯ ಮೂಲಕ ಸೇರಿಸಲಾಯಿತು?",
            "options": [{"label": "A", "text": "42nd Amendment Act, 1976"}, {"label": "B", "text": "44th Amendment Act, 1978"}, {"label": "C", "text": "86th Amendment Act, 2002"}, {"label": "D", "text": "91st Amendment Act, 2003"}],
            "answer": "C",
            "explanation": "The 86th Constitutional Amendment Act, 2002, inserted Article 21A, making education a Fundamental Right for children aged 6 to 14 years."
        },
        {
            "id": "P1-T1-GK-15", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Which Article of the Indian Constitution grants special provisions and reservations in education and public employment for the Kalyana Karnataka (Hyderabad-Karnataka) region?",
            "text_alt": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ (ಹೈದರಾಬಾದ್-ಕರ್ನಾಟಕ) ಪ್ರದೇಶಕ್ಕೆ ಶಿಕ್ಷಣ ಮತ್ತು ಉದ್ಯೋಗದಲ್ಲಿ ವಿಶೇಷ ಮೀಸಲಾತಿ ನೀಡುವ ಸಂವಿಧಾನದ ವಿಧಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Article 370"}, {"label": "B", "text": "Article 371A"}, {"label": "C", "text": "Article 371J"}, {"label": "D", "text": "Article 371D"}],
            "answer": "C",
            "explanation": "Article 371J was inserted by the 98th Constitutional Amendment Act, 2012, providing special provisions for the six backward districts of Kalyana Karnataka."
        },
        {
            "id": "P1-T1-GK-16", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "PYQ - GPSTR 2015", "difficulty": "medium",
            "text": "Which writ is issued by a High Court or Supreme Court to quash an illegal order passed by a lower court or quasi-judicial tribunal lacking jurisdiction?",
            "text_alt": "ಕೆಳ ನ್ಯಾಯಾಲಯ ಅಥವಾ ನ್ಯಾಯಮಂಡಳಿ ತನ್ನ ವ್ಯಾಪ್ತಿ ಮೀರಿ ಹೊರಡಿಸಿದ ಕಾನೂನುಬಾಹಿರ ಆದೇಶವನ್ನು ರದ್ದುಗೊಳಿಸಲು ಹೊರಡಿಸುವ ರಿಟ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Habeas Corpus"}, {"label": "B", "text": "Mandamus"}, {"label": "C", "text": "Certiorari"}, {"label": "D", "text": "Quo-Warranto"}],
            "answer": "C",
            "explanation": "Certiorari is a corrective writ issued to quash the order of an inferior court or tribunal made without or in excess of jurisdiction."
        },
        {
            "id": "P1-T1-GK-17", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "The Directive Principles of State Policy (Part IV) in the Indian Constitution were borrowed from the constitution of which country?",
            "text_alt": "ಭಾರತ ಸಂವಿಧಾನದ ಭಾಗ IV ರಲ್ಲಿರುವ ರಾಜ್ಯ ನಿರ್ದೇಶಕ ತತ್ವಗಳನ್ನು ಯಾವ ದೇಶದ ಸಂವಿಧಾನದಿಂದ ಎರವಲು ಪಡೆಯಲಾಗಿದೆ?",
            "options": [{"label": "A", "text": "United States of America"}, {"label": "B", "text": "Ireland"}, {"label": "C", "text": "United Kingdom"}, {"label": "D", "text": "Canada"}],
            "answer": "B",
            "explanation": "The Directive Principles of State Policy (Articles 36–51) were inspired by the Irish Constitution of 1937 (which in turn borrowed from Spain)."
        },
        {
            "id": "P1-T1-GK-18", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "What is the minimum qualifying age for an Indian citizen to be elected as a Member of the Lok Sabha?",
            "text_alt": "ಲೋಕಸಭೆಯ ಸದಸ್ಯರಾಗಿ (ಎಂಪಿ) ಆಯ್ಕೆಯಾಗಲು ಭಾರತೀಯ ಪ್ರಜೆಗೆ ಇರಬೇಕಾದ ಕನಿಷ್ಠ ವಯಸ್ಸು ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "18 years"}, {"label": "B", "text": "21 years"}, {"label": "C", "text": "25 years"}, {"label": "D", "text": "30 years"}],
            "answer": "C",
            "explanation": "Under Article 84(b), the minimum age for election to the Lok Sabha is 25 years (and 30 years for the Rajya Sabha)."
        },
        {
            "id": "P1-T1-GK-19", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "The Shivanasamudra Hydro-electric Project established on the Cauvery River in 1902 was primarily built to supply electricity to which location?",
            "text_alt": "1902 ರಲ್ಲಿ ಕಾವೇರಿ ನದಿಗೆ ನಿರ್ಮಿಸಲಾದ ಶಿವನಸಮುದ್ರ ಜಲವಿದ್ಯುತ್ ಯೋಜನೆಯನ್ನು ಮುಖ್ಯವಾಗಿ ಯಾವ ಸ್ಥಳಕ್ಕೆ ವಿದ್ಯುತ್ ಪೂರೈಸಲು ಸ್ಥಾಪಿಸಲಾಯಿತು?",
            "options": [{"label": "A", "text": "Bengaluru City streetlights"}, {"label": "B", "text": "Kolar Gold Fields (KGF)"}, {"label": "C", "text": "Mysore Palace"}, {"label": "D", "text": "Bhadravati Iron Works"}],
            "answer": "B",
            "explanation": "Commissioned during the reign of Krishnaraja Wodeyar IV, the Shivanasamudra plant was designed to power the gold mines of Kolar Gold Fields (KGF)."
        },
        {
            "id": "P1-T1-GK-20", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "On which historic date was the newly unified state of Mysore officially rechristened as 'Karnataka'?",
            "text_alt": "ಏಕೀಕೃತ ಮೈಸೂರು ರಾಜ್ಯವನ್ನು ಅಧಿಕೃತವಾಗಿ 'ಕರ್ನಾಟಕ' ಎಂದು ಮರುನಾಮಕರಣ ಮಾಡಿದ ಐತಿಹಾಸಿಕ ದಿನಾಂಕ ಯಾವುದು?",
            "options": [{"label": "A", "text": "1 November 1956"}, {"label": "B", "text": "1 November 1960"}, {"label": "C", "text": "1 November 1973"}, {"label": "D", "text": "15 August 1974"}],
            "answer": "C",
            "explanation": "Under the Chief Ministership of D. Devaraj Urs, the state of Mysore was officially renamed 'Karnataka' on 1 November 1973."
        }
    ]
    qs.extend(gk)

    # ----------------------------------------------------
    # SECTION 2: CURRENT AFFAIRS (15 QUESTIONS: Q21 to Q35)
    # ----------------------------------------------------
    ca = [
        {
            "id": "P1-T1-CA-21", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "Under the Karnataka Government\'s flagship 'Gruha Lakshmi' scheme, what is the monthly financial assistance provided to the woman head of eligible households?",
            "text_alt": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಮಹತ್ವಾಕಾಂಕ್ಷೆಯ 'ಗೃಹಲಕ್ಷ್ಮಿ' ಯೋಜನೆಯಡಿ ಅರ್ಹ ಕುಟುಂಬದ ಮಹಿಳಾ ಯಜಮಾನಿಗೆ ನೀಡಲಾಗುವ ಮಾಸಿಕ ಆರ್ಥಿಕ ನೆರವು ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "₹1,000"}, {"label": "B", "text": "₹1,500"}, {"label": "C", "text": "₹2,000"}, {"label": "D", "text": "₹3,000"}],
            "answer": "C",
            "explanation": "Gruha Lakshmi provides ₹2,000 per month directly into the Aadhaar-linked bank account of the woman head of eligible households."
        },
        {
            "id": "P1-T1-CA-22", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "What benefit is guaranteed to women domiciled in Karnataka under the 'Shakti' scheme launched by the Karnataka State Government?",
            "text_alt": "ಕರ್ನಾಟಕ ಸರ್ಕಾರ ಜಾರಿಗೆ ತಂದಿರುವ 'ಶಕ್ತಿ' ಯೋಜನೆಯಡಿ ರಾಜ್ಯದ ಮಹಿಳೆಯರಿಗೆ ದೊರೆಯುವ ಸೌಲಭ್ಯ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Free bus travel in state-run road transport corporations (KSRTC, BMTC, NWKRTC, KKRTC)"}, {"label": "B", "text": "Free electricity up to 200 units"}, {"label": "C", "text": "Free health insurance coverage up to ₹5 Lakhs"}, {"label": "D", "text": "Subsidized electric scooters for working women"}],
            "answer": "A",
            "explanation": "The Shakti scheme provides free bus travel for women domiciled in Karnataka in non-premium services across all 4 state transport corporations."
        },
        {
            "id": "P1-T1-CA-23", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Under the Karnataka Government\'s 'Yuva Nidhi' guarantee scheme, what monthly unemployment allowance is provided to eligible unemployed graduates?",
            "text_alt": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 'ಯುವನಿಧಿ' ಖಾತರಿ ಯೋಜನೆಯಡಿ ನಿರುದ್ಯೋಗಿ ಪದವೀಧರರಿಗೆ ನೀಡಲಾಗುವ ಮಾಸಿಕ ನಿರುದ್ಯೋಗ ಭತ್ಯೆ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "₹1,500"}, {"label": "B", "text": "₹2,000"}, {"label": "C", "text": "₹3,000"}, {"label": "D", "text": "₹5,000"}],
            "answer": "C",
            "explanation": "Yuva Nidhi provides ₹3,000 per month to unemployed degree graduates and ₹1,500 per month to unemployed diploma holders for up to two years."
        },
        {
            "id": "P1-T1-CA-24", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "What is the official name given to the landing site of ISRO\'s Chandrayaan-3 lunar lander 'Vikram' on the Moon\'s south pole?",
            "text_alt": "ಇಸ್ರೋದ ಚಂದ್ರಯಾನ-3 ನೌಕೆಯ 'ವಿಕ್ರಮ್' ಲ್ಯಾಂಡರ್ ಚಂದ್ರನ ದಕ್ಷಿಣ ಧ್ರುವದಲ್ಲಿ ಇಳಿದ ಸ್ಥಳಕ್ಕೆ ಇಡಲಾದ ಅಧಿಕೃತ ಹೆಸರೇನು?",
            "options": [{"label": "A", "text": "Tiranga Point"}, {"label": "B", "text": "Shiv Shakti Point"}, {"label": "C", "text": "Atal Point"}, {"label": "D", "text": "Kalam Point"}],
            "answer": "B",
            "explanation": "Prime Minister Narendra Modi designated the Chandrayaan-3 touchdown site as 'Shiv Shakti Point' and August 23 as 'National Space Day'."
        },
        {
            "id": "P1-T1-CA-25", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "At which Lagrange Point is ISRO\'s solar observatory satellite 'Aditya-L1' stationed to continuously monitor the Sun without eclipses?",
            "text_alt": "ಯಾವುದೇ ಗ್ರಹಣಗಳಿಲ್ಲದೆ ಸೂರ್ಯನನ್ನು ನಿರಂತರವಾಗಿ ವೀಕ್ಷಿಸಲು ಇಸ್ರೋದ 'ಆದಿತ್ಯ-ಎಲ್1' ಸೌರ ವೀಕ್ಷಣಾಲಯವನ್ನು ಯಾವ ಲ್ಯากรಾಂಜ್ ಬಿಂದುವಿನಲ್ಲಿ ಸ್ಥಾಪಿಸಲಾಗಿದೆ?",
            "options": [{"label": "A", "text": "L1 (Lagrange Point 1, ~1.5 million km from Earth)"}, {"label": "B", "text": "L2 (Lagrange Point 2)"}, {"label": "C", "text": "L4 (Lagrange Point 4)"}, {"label": "D", "text": "L5 (Lagrange Point 5)"}],
            "answer": "A",
            "explanation": "Aditya-L1 is placed in a halo orbit around the Sun-Earth Lagrange Point 1 (L1), located approximately 1.5 million kilometers from Earth."
        },
        {
            "id": "P1-T1-CA-26", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "The Bharatiya Nyaya Sanhita (BNS), which came into enforcement in July 2024, replaced which historic penal statute?",
            "text_alt": "ಜುಲೈ 2024 ರಲ್ಲಿ ಜಾರಿಗೆ ಬಂದ ಭಾರತೀಯ ನ್ಯಾಯ ಸಂಹಿತೆ (BNS) ಯಾವ ಐತಿಹಾಸಿಕ ಕಾನೂನನ್ನು ಬದಲಾಯಿಸಿದೆ?",
            "options": [{"label": "A", "text": "Code of Criminal Procedure, 1973"}, {"label": "B", "text": "Indian Penal Code (IPC), 1860"}, {"label": "C", "text": "Indian Evidence Act, 1872"}, {"label": "D", "text": "Police Act, 1861"}],
            "answer": "B",
            "explanation": "The Bharatiya Nyaya Sanhita (BNS) replaced the colonial Indian Penal Code 1860; BNSS replaced CrPC 1973; BSA replaced Evidence Act 1872."
        },
        {
            "id": "P1-T1-CA-27", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Who among the following was awarded the Bharat Ratna posthumously in 2024 in recognition of his role as the architect of India\'s Green Revolution?",
            "text_alt": "ಭಾರತದ ಹಸಿರು ಕ್ರಾಂತಿಯ ಪಿತಾಮಹ ಎಂದು ಹೆಸರಾದ ಯಾರಿಗೆ 2024 ರಲ್ಲಿ ಮರಣೋತ್ತರವಾಗಿ 'ಭಾರತ ರತ್ನ' ಪ್ರಶಸ್ತಿ ನೀಡಿ ಗೌರವಿಸಲಾಯಿತು?",
            "options": [{"label": "A", "text": "Dr. Verghese Kurien"}, {"label": "B", "text": "Dr. M. S. Swaminathan"}, {"label": "C", "text": "Norman Borlaug"}, {"label": "D", "text": "C. Subramaniam"}],
            "answer": "B",
            "explanation": "Dr. M. S. Swaminathan was posthumously conferred the Bharat Ratna in 2024 alongside Karpoori Thakur, P. V. Narasimha Rao, and Chaudhary Charan Singh."
        },
        {
            "id": "P1-T1-CA-28", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Who was honoured with the prestigious 58th Jnanpith Award (for the year 2023, conferred in 2024)?",
            "text_alt": "ಪ್ರತಿಷ್ಠಿತ 58ನೇ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿಗೆ (2024 ರಲ್ಲಿ ಪ್ರದಾನ ಮಾಡಲಾದ) ಜಂಟಿಯಾಗಿ ಭಾಜನರಾದವರು ಯಾರು?",
            "options": [{"label": "A", "text": "Damodar Mauzo and Amitav Ghosh"}, {"label": "B", "text": "Gulzar (Urdu) and Jagadguru Rambhadracharya (Sanskrit)"}, {"label": "C", "text": "Akkitham and Shankha Ghosh"}, {"label": "D", "text": "Chandrashekhara Kambara and Girish Karnad"}],
            "answer": "B",
            "explanation": "The Jnanpith Selection Committee conferred the 58th Jnanpith Award jointly on Urdu poet/filmmaker Gulzar and Sanskrit scholar Jagadguru Rambhadracharya."
        },
        {
            "id": "P1-T1-CA-29", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which Indian shooter made history by winning two Olympic bronze medals at the Paris 2024 Olympic Games in the same edition?",
            "text_alt": "ಪ್ಯಾರಿಸ್ 2024 ಒಲಿಂಪಿಕ್ಸ್‌ನಲ್ಲಿ ಒಂದೇ ಆವೃತ್ತಿಯಲ್ಲಿ ಎರಡು ಕಂಚಿನ ಪದಕಗಳನ್ನು ಗೆದ್ದು ಇತಿಹಾಸ ನಿರ್ಮಿಸಿದ ಭಾರತದ ಶೂಟರ್ ಯಾರು?",
            "options": [{"label": "A", "text": "Manu Bhaker"}, {"label": "B", "text": "Sarabjot Singh"}, {"label": "C", "text": "Swapnil Kusale"}, {"label": "D", "text": "Avani Lekhara"}],
            "answer": "A",
            "explanation": "Manu Bhaker won bronze in Women\'s 10m Air Pistol and another bronze in Mixed 10m Air Pistol team event with Sarabjot Singh at Paris 2024."
        },
        {
            "id": "P1-T1-CA-30", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "Which national team emerged champions of the ICC Men\'s T20 World Cup 2024 held in the West Indies and USA?",
            "text_alt": "ವೆಸ್ಟ್ ಇಂಡೀಸ್ ಮತ್ತು ಯುಎಸ್ಎ ನಲ್ಲಿ ನಡೆದ ಐಸಿಸಿ ಪುರುಷರ ಟಿ20 ವಿಶ್ವಕಪ್ 2024 ಚಾಂಪಿಯನ್ ಆದ ದೇಶ ಯಾವುದು?",
            "options": [{"label": "A", "text": "South Africa"}, {"label": "B", "text": "India"}, {"label": "C", "text": "Australia"}, {"label": "D", "text": "England"}],
            "answer": "B",
            "explanation": "India defeated South Africa by 7 runs in the final at Kensington Oval, Barbados, on June 29, 2024, to lift their second T20 World Cup trophy."
        },
        {
            "id": "P1-T1-CA-31", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Which international multilateral organization was formally inducted as a permanent member of the G20 during India\'s G20 Presidency at the New Delhi Summit?",
            "text_alt": "ನವದೆಹಲಿಯಲ್ಲಿ ನಡೆದ ಜಿ20 ಶೃಂಗಸಭೆಯಲ್ಲಿ ಭಾರತದ ಅಧ್ಯಕ್ಷತೆಯಲ್ಲಿ ಜಿ20 ಕೂಟದ ಖಾಯಂ ಸದಸ್ಯನಾಗಿ ಸೇರ್ಪಡೆಗೊಂಡ ಅಂತರರಾಷ್ಟ್ರೀಯ ಸಂಘಟನೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Association of Southeast Asian Nations (ASEAN)"}, {"label": "B", "text": "African Union (AU)"}, {"label": "C", "text": "OPEC"}, {"label": "D", "text": "SAARC"}],
            "answer": "B",
            "explanation": "The 55-nation African Union (AU) was admitted as a permanent member of the G20 at the New Delhi G20 Leaders\' Summit in September 2023."
        },
        {
            "id": "P1-T1-CA-32", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "What is the maximum free domestic electricity consumption allowed per month per household under Karnataka\'s 'Gruha Jyothi' guarantee scheme?",
            "text_alt": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 'ಗೃಹಜ್ಯೋತಿ' ಯೋಜನೆಯಡಿ ಪ್ರತಿ ಕುಟುಂಬಕ್ಕೆ ಗರಿಷ್ಠ ಎಷ್ಟು ಯೂನಿಟ್‌ಗಳವರೆಗೆ ಉಚಿತ ಗೃಹಬಳಕೆ ವಿದ್ಯುತ್ ನೀಡಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "100 Units"}, {"label": "B", "text": "150 Units"}, {"label": "C", "text": "200 Units"}, {"label": "D", "text": "250 Units"}],
            "answer": "C",
            "explanation": "Gruha Jyothi provides up to 200 units of free electricity per month based on the household\'s average monthly consumption plus a 10% allowance."
        },
        {
            "id": "P1-T1-CA-33", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Which new Ramsar Wetland site from Karnataka was added to the Ramsar List in 2024, located in the estuary of Uttara Kannada district?",
            "text_alt": "2024 ರಲ್ಲಿ ರಾಮ್ಸರ್ ಪಟ್ಟಿಗೆ ಸೇರಿದ ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯ ನದೀಮುಖಜ ಪ್ರದೇಶದಲ್ಲಿರುವ ಕರ್ನಾಟಕದ ಜೌಗು ಪ್ರದೇಶ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Ankasamudra Bird Conservation Reserve"}, {"label": "B", "text": "Aghanashini Estuary"}, {"label": "C", "text": "Magadi Kere"}, {"label": "D", "text": "Karanji Lake"}],
            "answer": "B",
            "explanation": "Aghanashini Estuary in Uttara Kannada was declared a Ramsar Wetland of International Importance in January 2024 along with Magadi Kere and Ankasamudra."
        },
        {
            "id": "P1-T1-CA-34", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "The 2024 Nobel Peace Prize was awarded to Nihon Hidankyo, a grassroots movement representing atomic bomb survivors from which nation?",
            "text_alt": "ಪರಮಾಣು ಬಾಂಬ್ ದಾಳಿಯ ಸಂತ್ರಸ್ತರ ಜಪಾನಿನ 'ನಿಹೋನ್ ಹಿಡಾಂಕ್ಯೋ' ಸಂಸ್ಥೆಗೆ 2024 ರ ಯಾವ ನೊಬೆಲ್ ಪ್ರಶಸ್ತಿಯನ್ನು ನೀಡಲಾಯಿತು?",
            "options": [{"label": "A", "text": "Nobel Prize in Literature"}, {"label": "B", "text": "Nobel Peace Prize"}, {"label": "C", "text": "Nobel Prize in Chemistry"}, {"label": "D", "text": "Nobel Prize in Physiology or Medicine"}],
            "answer": "B",
            "explanation": "Nihon Hidankyo (Japan) was awarded the 2024 Nobel Peace Prize for its efforts to achieve a world free of nuclear weapons."
        },
        {
            "id": "P1-T1-CA-35", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Who among the following was conferred the prestigious Dadasaheb Phalke Award for the year 2022 (presented in 2024)?",
            "text_alt": "ಭಾರತೀಯ ಚಿತ್ರರಂಗದ ಅತ್ಯುನ್ನತ 'ದಾದಾಸಾಹೇಬ್ ಫಾಲ್ಕೆ' ಪ್ರಶಸ್ತಿಯನ್ನು (2024 ರಲ್ಲಿ ಪ್ರದಾನ ಮಾಡಿದ) ಪಡೆದ ಹಿರಿಯ ನಟ ಯಾರು?",
            "options": [{"label": "A", "text": "Mithun Chakraborty"}, {"label": "B", "text": "Waheeda Rehman"}, {"label": "C", "text": "Asha Parekh"}, {"label": "D", "text": "Rajinikanth"}],
            "answer": "A",
            "explanation": "Veteran actor and politician Mithun Chakraborty was conferred the 70th National Film Awards\' Dadasaheb Phalke Award."
        }
    ]
    qs.extend(ca)

    # ----------------------------------------------------
    # SECTION 3: GENERAL KANNADA (25 QUESTIONS: Q36 to Q60)
    # ----------------------------------------------------
    kan = [
        {
            "id": "P1-T1-KN-36", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "easy",
            "text": "ಕನ್ನಡ ವರ್ಣಮಾಲೆಯಲ್ಲಿರುವ ಒಟ್ಟು ಅಕ್ಷರಗಳ ಸಂಖ್ಯೆ ಎಷ್ಟು?",
            "text_alt": "How many letters are there in the standard Kannada Varnamale?",
            "options": [{"label": "A", "text": "48"}, {"label": "B", "text": "49"}, {"label": "C", "text": "50"}, {"label": "D", "text": "52"}],
            "answer": "B",
            "explanation": "ಕನ್ನಡ ವರ್ಣಮಾಲೆಯಲ್ಲಿ ಒಟ್ಟು 49 ಅಕ್ಷರಗಳಿವೆ (14 ಸ್ವರಗಳು + 2 ಯೋಗವಾಹಗಳು + 33 ವ್ಯಂಜನಗಳು)."
        },
        {
            "id": "P1-T1-KN-37", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "ಕನ್ನಡ ವರ್ಣಮಾಲೆಯಲ್ಲಿ 'ಐ' ಮತ್ತು 'ಔ' ಅಕ್ಷರಗಳನ್ನು ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "text_alt": "In Kannada Varnamale, what are 'Ai' and 'Au' classified as?",
            "options": [{"label": "A", "text": "ಹ್ರಸ್ವಸ್ವರಗಳು"}, {"label": "B", "text": "ದೀರ್ಘಸ್ವರಗಳು"}, {"label": "C", "text": "ಸಂಧ್ಯಾಕ್ಷರಗಳು"}, {"label": "D", "text": "ಪ್ಲುತಸ್ವರಗಳು"}],
            "answer": "C",
            "explanation": "ಎರಡು ಸ್ವರಗಳು ಕೂಡಿ ಆಗಿರುವ 'ಐ' ಮತ್ತು 'ಔ' ಅಕ್ಷರಗಳನ್ನು 'ಸಂಧ್ಯಾಕ್ಷರಗಳು' ಎನ್ನುತ್ತಾರೆ."
        },
        {
            "id": "P1-T1-KN-38", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "ವರ್ಗೀಯ ವ್ಯಂಜನಗಳಲ್ಲಿ ಪ್ರತಿ ವರ್ಗದ ಐದನೆಯ ಅಕ್ಷರಗಳನ್ನು (ಙ, ಞ, ಣ, ನ, ಮ) ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "text_alt": "What are the 5th letters of each consonant group called?",
            "options": [{"label": "A", "text": "ಅಲ್ಪಪ್ರಾಣಗಳು"}, {"label": "B", "text": "ಮಹಾಪ್ರಾಣಗಳು"}, {"label": "C", "text": "ಅನುನಾಸಿಕಗಳು"}, {"label": "D", "text": "ಯೋಗವಾಹಗಳು"}],
            "answer": "C",
            "explanation": "ಮೂಗಿನ ಸಹಾಯದಿಂದ ಉಚ್ಚರಿಸಲ್ಪಡುವ ವರ್ಗದ ಕೊನೆಯ ಅಕ್ಷರಗಳಿಗೆ 'ಅನುನಾಸಿಕಗಳು' ಎನ್ನಲಾಗುತ್ತದೆ."
        },
        {
            "id": "P1-T1-KN-39", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "medium",
            "text": "'ಊರೂರು' ಪದವು ಯಾವ ಸಂಧಿಗೆ ಉದಾಹರಣೆಯಾಗಿದೆ?",
            "text_alt": "The compound word 'Ururu' (Uru + Uru) is an example of which Sandhi?",
            "options": [{"label": "A", "text": "ಲೋಪ ಸಂಧಿ"}, {"label": "B", "text": "ಆಗಮ ಸಂಧಿ"}, {"label": "C", "text": "ಆದೇಶ ಸಂಧಿ"}, {"label": "D", "text": "ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ"}],
            "answer": "A",
            "explanation": "ಊರು + ಊರು = ಊರೂರು (ಪೂರ್ವಪದದ ಕೊನೆಯಲ್ಲಿರುವ 'ಉ' ಸ್ವರವು ಲೋಪವಾಗಿರುವುದರಿಂದ ಇದು ಲೋಪಸಂಧಿ)."
        },
        {
            "id": "P1-T1-KN-40", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "'ಮಳೆಗಾಲ' ಪದವನ್ನು ಬಿಡಿಸಿ ಬರೆದಾಗ ಯಾವ ಸಂಧಿಯಾಗುತ್ತದೆ?",
            "text_alt": "Which Sandhi is formed in 'Malegala' (Male + Kala)?",
            "options": [{"label": "A", "text": "ಲೋಪ ಸಂಧಿ"}, {"label": "B", "text": "ಆದೇಶ ಸಂಧಿ (ಕ-ಕಾರಕ್ಕೆ ಗ-ಕಾರ)"}, {"label": "C", "text": "ಆಗಮ ಸಂಧಿ"}, {"label": "D", "text": "ಜಶ್ತ್ವ ಸಂಧಿ"}],
            "answer": "B",
            "explanation": "ಮಳೆ + ಕಾಲ = ಮಳೆಗಾಲ. ಉತ್ತರಪದದ ಆದಿಯಲ್ಲಿರುವ 'ಕ' ಕಾರಕ್ಕೆ 'ಗ' ಕಾರ ಆದೇಶವಾಗಿ ಬಂದಿರುವುದರಿಂದ ಇದು ಆದೇಶ ಸಂಧಿ."
        },
        {
            "id": "P1-T1-KN-41", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "'ಸೂರ್ಯೋದಯ' (ಸೂರ್ಯ + ಉದಯ) ಪದವು ಯಾವ ಸಂಸ್ಕೃತ ಸಂಧಿಗೆ ಉದಾಹರಣೆಯಾಗಿದೆ?",
            "text_alt": "Which Sanskrit Sandhi is 'Suryodaya' an example of?",
            "options": [{"label": "A", "text": "ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ"}, {"label": "B", "text": "ಗುಣ ಸಂಧಿ"}, {"label": "C", "text": "ವೃದ್ಧಿ ಸಂಧಿ"}, {"label": "D", "text": "ಯಣ್ ಸಂಧಿ"}],
            "answer": "B",
            "explanation": "ಅ/ಆ ಕಾರಗಳಿಗೆ ಇ/ಈ ಪರವಾದರೆ 'ಏ', ಉ/ಊ ಪರವಾದರೆ 'ಓ', ಋ ಪರವಾದರೆ 'ಅರ್' ಬರುವುದು ಗುಣಸಂಧಿ (ಸೂರ್ಯ + ಉದಯ = ಸೂರ್ಯೋದಯ)."
        },
        {
            "id": "P1-T1-KN-42", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "'ಇತ್ಯಾದಿ' (ಇತಿ + ಆದಿ) ಪದವು ಯಾವ ಸಂಧಿಯಾಗಿದೆ?",
            "text_alt": "Which Sandhi is 'Ityadi' (Iti + Adi)?",
            "options": [{"label": "A", "text": "ಗುಣ ಸಂಧಿ"}, {"label": "B", "text": "ಯಣ್ ಸಂಧಿ"}, {"label": "C", "text": "ವೃದ್ಧಿ ಸಂಧಿ"}, {"label": "D", "text": "ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ"}],
            "answer": "B",
            "explanation": "ಇ, ಈ, ಉ, ಊ, ಋ ಗಳಿಗೆ ಸವರ್ಣವಲ್ಲದ ಸ್ವರ ಪರವಾದರೆ ಕ್ರಮವಾಗಿ ಯ್, ವ್, ರ್ ಗಳು ಬರುವುದು ಯಣ್ ಸಂಧಿ (ಇತಿ + ಆದಿ = ಇತ್ಯಾದಿ)."
        },
        {
            "id": "P1-T1-KN-43", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "'ಹೆಮ್ಮರ' (ಹಿರಿದು + ಮರ) ಎಂಬುದು ಯಾವ ಸಮಾಸಕ್ಕೆ ಉದಾಹರಣೆಯಾಗಿದೆ?",
            "text_alt": "Which Samasa is 'Hemmara' (Hiridu + Mara)?",
            "options": [{"label": "A", "text": "ತತ್ಪುರುಷ ಸಮಾಸ"}, {"label": "B", "text": "ಕರ್ಮಧಾರಯ ಸಮಾಸ"}, {"label": "C", "text": "ದ್ವಿಗು ಸಮಾಸ"}, {"label": "D", "text": "ಗಮಕ ಸಮಾಸ"}],
            "answer": "B",
            "explanation": "ವಿಶೇಷಣ ಮತ್ತು ವಿಶೇಷ್ಯಗಳು ಸೇರಿ ಆಗುವ ಸಮಾಸವನ್ನು 'ಕರ್ಮಧಾರಯ ಸಮಾಸ' ಎನ್ನುತ್ತಾರೆ (ಹಿರಿದಾದ ಮರ = ಹೆಮ್ಮರ)."
        },
        {
            "id": "P1-T1-KN-44", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "easy",
            "text": "'ಪಂಚವಟಿ' (ಐದು ವಟಗಳ ಸಮೂಹ) ಎಂಬುದು ಯಾವ ಸಮಾಸ?",
            "text_alt": "Which Samasa is 'Panchavati'?",
            "options": [{"label": "A", "text": "ದ್ವಂದ್ವ ಸಮಾಸ"}, {"label": "B", "text": "ದ್ವಿಗು ಸಮಾಸ"}, {"label": "C", "text": "ಬಹು Poly/ವ್ರೀಹಿ ಸಮಾಸ"}, {"label": "D", "text": "ತತ್ಪುರುಷ ಸಮಾಸ"}],
            "answer": "B",
            "explanation": "ಪೂರ್ವಪದವು ಸಂಖ್ಯಾ ವಾಚಕವಾಗಿದ್ದು ಉತ್ತರಪದವು ನಾಮಪದವಾಗಿದ್ದರೆ ಅದು 'ದ್ವಿಗು ಸಮಾಸ'."
        },
        {
            "id": "P1-T1-KN-45", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "'ಮುಕ್ಕಣ್ಣ' (ಮೂರು ಕಣ್ಣುಗಳುಳ್ಳವನು - ಶಿವ) ಎಂಬ ಪದವು ಯಾವ ಸಮಾಸಕ್ಕೆ ಉದಾಹರಣೆಯಾಗಿದೆ?",
            "text_alt": "Which Samasa is 'Mukkanna' (Shiva)?",
            "options": [{"label": "A", "text": "ದ್ವಿಗು ಸಮಾಸ"}, {"label": "B", "text": "ಕರ್ಮಧಾರಯ ಸಮಾಸ"}, {"label": "C", "text": "ಬಹುವ್ರೀಹಿ ಸಮಾಸ"}, {"label": "D", "text": "ಅಂಶಿ ಸಮಾಸ"}],
            "answer": "C",
            "explanation": "ಸಮಸ್ತಪದದಲ್ಲಿ ಬೇರೊಂದು ಮೂರನೆಯ ಪದದ ಅರ್ಥವು (ಅನ್ಯಪದಾರ್ಥ) ಪ್ರಧಾನವಾಗಿದ್ದರೆ ಅದು 'ಬಹುವ್ರೀಹಿ ಸಮಾಸ'."
        },
        {
            "id": "P1-T1-KN-46", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "ಕನ್ನಡ ವಿಭಕ್ತಿ ಪ್ರತ್ಯಯಗಳಲ್ಲಿ ತೃತೀಯಾ ವಿಭಕ್ತಿಯ ಕಾರಕಾರ್ಥ ಯಾವುದು?",
            "text_alt": "What is the Karaka of Triteeya Vibhakti?",
            "options": [{"label": "A", "text": "ಕರ್ತೃ ಕಾರಕ"}, {"label": "B", "text": "ಕರ್ಮ ಕಾರಕ"}, {"label": "C", "text": "ಕರಣ ಕಾರಕ (ಇಂದ)"}, {"label": "D", "text": "ಸಂಪ್ರದಾನ ಕಾರಕ"}],
            "answer": "C",
            "explanation": "ಪ್ರಥಮಾ: ಕರ್ತೃ, ದ್ವಿತೀಯಾ: ಕರ್ಮ, ತೃತೀಯಾ: ಕರಣ (ಸಾಧನ - 'ಇಂದ'), ಚತುರ್ಥಿ: ಸಂಪ್ರದಾನ, ಪಂಚಮೀ: ಅಪಾದಾನ, ಷಷ್ಠೀ: ಸಂಬಂಧ, ಸಪ್ತಮೀ: ಅಧಿಕರಣ."
        },
        {
            "id": "P1-T1-KN-47", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "ಧಾತುವಿಗೆ ಕೃತ್ ಪ್ರತ್ಯಯ ಸೇರಿ ನಾಮಪದವಾದರೆ ಅದನ್ನು ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "text_alt": "What is a noun formed by adding a Krit suffix to a verbal root called?",
            "options": [{"label": "A", "text": "ಕೃದಂತ ನಾಮ"}, {"label": "B", "text": "ತದ್ಧಿತಾಂತ ನಾಮ"}, {"label": "C", "text": "ಕೃದಂತ ಭಾವನಾಮ"}, {"label": "D", "text": "ತದ್ಧಿತಾಂತ ಭಾವನಾಮ"}],
            "answer": "A",
            "explanation": "ಧಾತುವಿಗೆ ಕೃತ್ ಪ್ರತ್ಯಯ ಸೇರಿ ಉಂಟಾಗುವ ಪದ 'ಕೃದಂತ ನಾಮ' (ಉದಾ: ಮಾಡು + ಅವನು = ಮಾಡಿದವನು)."
        },
        {
            "id": "P1-T1-KN-48", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "'ಮಾಟಗಾತಿ' (ಮಾಟ + ಗಾತಿ) ಎಂಬುದು ಯಾವ ವ್ಯಾಕರಣಾಂಶಕ್ಕೆ ಉದಾಹರಣೆಯಾಗಿದೆ?",
            "text_alt": "What grammatical category is 'Matagaati'?",
            "options": [{"label": "A", "text": "ಕೃದಂತ ನಾಮ"}, {"label": "B", "text": "ತದ್ಧಿತಾಂತ ನಾಮ"}, {"label": "C", "text": "ತದ್ಧಿತಾಂತ ಭಾವನಾಮ"}, {"label": "D", "text": "ಕೃದಂತಾವ್ಯಯ"}],
            "answer": "B",
            "explanation": "ನಾಮಪ್ರಕೃತಿಗೆ ತದ್ಧಿತ ಪ್ರತ್ಯಯ ಸೇರಿದಾಗ ಉಂಟಾಗುವ ಪದ 'ತದ್ಧಿತಾಂತ ನಾಮ' (ಮಾಟ + ಗಾತಿ = ಮಾಟಗಾತಿ)."
        },
        {
            "id": "P1-T1-KN-49", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "easy",
            "text": "'ವರ್ಷ' ಎಂಬ ತತ್ಸಮ ಪದದ ಸರಿಯಾದ ತದ್ಭವ ರೂಪ ಯಾವುದು?",
            "text_alt": "What is the Tadbhava form of the Tatsama word 'Varsha'?",
            "options": [{"label": "A", "text": "ವರುಷ"}, {"label": "B", "text": "ಬರಿಸ"}, {"label": "C", "text": "ವಾಸ"}, {"label": "D", "text": "ವಾರ"}],
            "answer": "A",
            "explanation": "ಸಂಸ್ಕೃತದ 'ವರ್ಷ' ಎಂಬ ತತ್ಸಮ ಪದದ ಕನ್ನಡ ತದ್ಭವ ರೂಪ 'ವರುಷ'."
        },
        {
            "id": "P1-T1-KN-50", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "'ಲಕ್ಷ್ಮಿ' ಎಂಬ ತತ್ಸಮ ಪದದ ತದ್ಭವ ರೂಪ ಯಾವುದು?",
            "text_alt": "What is the Tadbhava of 'Lakshmi'?",
            "options": [{"label": "A", "text": "ಲಕುಮಿ"}, {"label": "B", "text": "ಲಚ್ಛಿ"}, {"label": "C", "text": "ಲಕ್ಷಿ"}, {"label": "D", "text": "ಲಕ್ಷ್ಯ"}],
            "answer": "A",
            "explanation": "'ಲಕ್ಷ್ಮಿ' ತತ್ಸಮದ ಸರಿಯಾದ ತದ್ಭವ ರೂಪ 'ಲಕುಮಿ'."
        },
        {
            "id": "P1-T1-KN-51", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "'ಅಕ್ಷರ' ಪದದ ತದ್ಭವ ರೂಪ ಯಾವುದು?",
            "text_alt": "What is the Tadbhava of 'Akshara'?",
            "options": [{"label": "A", "text": "ಅಕ್ಕರ"}, {"label": "B", "text": "ಅಕ್ಷಿ"}, {"label": "C", "text": "ಆಖರ"}, {"label": "D", "text": "ಅಕ್ಕಸ"}],
            "answer": "A",
            "explanation": "'ಅಕ್ಷರ' ತತ್ಸಮದ ಕನ್ನಡ ತದ್ಭವ 'ಅಕ್ಕರ'."
        },
        {
            "id": "P1-T1-KN-52", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "hard",
            "text": "ಉಪಮೇಯ ಮತ್ತು ಉಪಮಾನಗಳಿಗೆ ಅಭೇದವನ್ನು (ಯಾವುದೇ ಭೇದವಿಲ್ಲವೆಂದು) ಕಲ್ಪಿಸಿ ಹೇಳುವ ಅಲಂಕಾರ ಯಾವುದು?",
            "text_alt": "Which Alankara states complete non-difference between Upameya and Upamana?",
            "options": [{"label": "A", "text": "ಉಪಮಾಲಂಕಾರ"}, {"label": "B", "text": "ರೂಪಕಾಲಂಕಾರ"}, {"label": "C", "text": "ದೃಷ್ಟಾಂತಾಲಂಕಾರ"}, {"label": "D", "text": "ಉತ್ಪ್ರೇಕ್ಷಾಲಂಕಾರ"}],
            "answer": "B",
            "explanation": "ಉಪಮೇಯ ಮತ್ತು ಉಪಮಾನಗಳು ಬೇರೆ ಬೇರೆ ಅಲ್ಲ, ಎರಡೂ ಒಂದೇ ಎಂದು ವರ್ಣಿಸುವುದು 'ರೂಪಕಾಲಂಕಾರ'."
        },
        {
            "id": "P1-T1-KN-53", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "ಷಟ್ಪದಿ ಛಂದಸ್ಸಿನಲ್ಲಿ 'ಭಾಮಿನಿ ಷಟ್ಪದಿ'ಯ ಪ್ರತಿ ಪಾದದಲ್ಲಿ ಬರುವ ಮಾತ್ರೆಗಳ ನಿಯಮವೇನು?",
            "text_alt": "What is the matra rule in Bhamini Shatpadi?",
            "options": [{"label": "A", "text": "3, 4, 3, 4 ಮಾತ್ರೆಗಳು (1 ಮತ್ತು 2 ನೇ ಸಾಲಿನಲ್ಲಿ 14 ಮಾತ್ರೆಗಳು, 3 ನೇ ಸಾಲಿನಲ್ಲಿ 23 ಮಾತ್ರೆಗಳು)"}, {"label": "B", "text": "4, 4, 4 ಮಾತ್ರೆಗಳು"}, {"label": "C", "text": "5, 5, 5 ಮಾತ್ರೆಗಳು"}, {"label": "D", "text": "3, 5, 3, 5 ಮಾತ್ರೆಗಳು"}],
            "answer": "A",
            "explanation": "ಭಾಮಿನಿ ಷಟ್ಪದಿಯಲ್ಲಿ 1, 2, 4, 5 ನೆಯ ಸಾಲುಗಳಲ್ಲಿ 3-4-3-4 (14 ಮಾತ್ರೆಗಳು), 3 ಮತ್ತು 6 ನೆಯ ಸಾಲುಗಳಲ್ಲಿ 3-4-3-4-3-4+ಗುರು (21+2=23 ಮಾತ್ರೆಗಳು) ಇರುತ್ತವೆ."
        },
        {
            "id": "P1-T1-KN-54", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "'ವಾರ್ಧಕ ಷಟ್ಪದಿ'ಯ ಪಾದಗಳಲ್ಲಿ ಯಾವ ಗಣಗಳ ಜೋಡಣೆ ಕಂಡುಬರುತ್ತದೆ?",
            "text_alt": "What matra gana pattern is found in Vardhaka Shatpadi?",
            "options": [{"label": "A", "text": "3 ಮಾತ್ರೆಗಳ ಗಣಗಳು"}, {"label": "B", "text": "4 ಮಾತ್ರೆಗಳ ಗಣಗಳು"}, {"label": "C", "text": "5 ಮಾತ್ರೆಗಳ ಗಣಗಳು"}, {"label": "D", "text": "6 ಮಾತ್ರೆಗಳ ಗಣಗಳು"}],
            "answer": "C",
            "explanation": "ವಾರ್ಧಕ ಷಟ್ಪದಿಯಲ್ಲಿ 5 ಮಾತ್ರೆಗಳ ಗಣಗಳು ಬರುತ್ತವೆ (1, 2, 4, 5 ಪಾದಗಳಲ್ಲಿ 4 ಪಂಚಮಾತ್ರಾಗಣಗಳು = 20 ಮಾತ್ರೆಗಳು; 3, 6 ಪಾದಗಳಲ್ಲಿ 6 ಪಂಚಮಾತ್ರಾಗಣಗಳು + 1 ಗುರು = 32 ಮಾತ್ರೆಗಳು)."
        },
        {
            "id": "P1-T1-KN-55", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "easy",
            "text": "'ಅತ್ತೆಗೊಂದು ಕಾಲ, ಸೊಸೆಗೊಂದು ಕಾಲ' ಎಂಬ ಗಾದೆ ಮಾತಿನ ಒಳಾರ್ಥವೇನು?",
            "text_alt": "What is the inner meaning of the Kannada proverb 'Attegondu kaala, sosegondu kaala'?",
            "options": [{"label": "A", "text": "ಕಾಲ ಯಾರನ್ನೂ ಕಾಯುವುದಿಲ್ಲ"}, {"label": "B", "text": "ಪ್ರತಿಯೊಬ್ಬರಿಗೂ ತಮ್ಮ ಪ್ರಭಾವ ಬೀರುವ ಕಾಲ ಅಥವಾ ಅವಕಾಶ ಬರುತ್ತದೆ"}, {"label": "C", "text": "ಅತ್ತೆ ಮತ್ತು ಸೊಸೆ ಯಾವಾಗಲೂ ಜಗಳವಾಡುತ್ತಾರೆ"}, {"label": "D", "text": "ಹಳೆಯ ಪೀಳಿಗೆಯೇ ಸದಾ ಶ್ರೇಷ್ಠ"}],
            "answer": "B",
            "explanation": "ಜೀವನದಲ್ಲಿ ಬದಲಾವಣೆ ಅನಿವಾರ್ಯ, ಪ್ರತಿಯೊಬ್ಬರಿಗೂ ತಮ್ಮ ಶಕ್ತಿ ಪ್ರದರ್ಶಿಸಲು ಕಾಲಾವಕಾಶ ಒದಗಿಬರುತ್ತದೆ ಎಂಬುದು ಇದರ ಆಶಯ."
        },
        {
            "id": "P1-T1-KN-56", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "ಕರ್ತೃವಿಗೆ ಪ್ರಾಧಾನ್ಯ ಕೊಟ್ಟು ಹೇಳುವ ಪ್ರಯೋಗವನ್ನು ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "text_alt": "What is the active voice called in Kannada grammar?",
            "options": [{"label": "A", "text": "ಕರ್ತರಿ ಪ್ರಯೋಗ"}, {"label": "B", "text": "ಕರ್ಮಣಿ ಪ್ರಯೋಗ"}, {"label": "C", "text": "ಭಾವೇ ಪ್ರಯೋಗ"}, {"label": "D", "text": "ಪ್ರೇರಣಾರ್ಥಕ ಪ್ರಯೋಗ"}],
            "answer": "A",
            "explanation": "ಕ್ರಿಯಾಪದದ ರೂಪವು ಕರ್ತೃವಿನ ಲಿಂಗ, ವಚನ, ಪುರುಷಗಳನ್ನು ಅನುಸರಿಸಿ ಬಂದರೆ ಅದು 'ಕರ್ತರಿ ಪ್ರಯೋಗ' (Active Voice)."
        },
        {
            "id": "P1-T1-KN-57", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "ಕರ್ಮಣಿ ಪ್ರಯೋಗದಲ್ಲಿ ಧಾತುವಿಗೆ ಸಾಮಾನ್ಯವಾಗಿ ಯಾವ ಪ್ರತ್ಯಯ ಸೇರುತ್ತದೆ?",
            "text_alt": "Which suffix is added to verbal root in Karmani Prayoga?",
            "options": [{"label": "A", "text": "'ಇಸು' ಪ್ರತ್ಯಯ"}, {"label": "B", "text": "'ಪಡು' ಧಾತುರೂಪ"}, {"label": "C", "text": "'ಅಲ್' ಪ್ರತ್ಯಯ"}, {"label": "D", "text": "'ಇಗೆ' ಪ್ರತ್ಯಯ"}],
            "answer": "B",
            "explanation": "ಕರ್ಮಣಿ ಪ್ರಯೋಗದಲ್ಲಿ ಕರ್ಮಪದಕ್ಕೆ ಪ್ರಾಧಾನ್ಯವಿದ್ದು, ಧಾತುವಿನ ಮುಂದೆ 'ಪಡು' ರೂಪ ಬರುತ್ತದೆ (ಉದಾ: ರಾವಣನು ರಾಮನಿಂದ ಕೊಲ್ಲಲ್ಪಟ್ಟನು)."
        },
        {
            "id": "P1-T1-KN-58", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "'ಅಮೃತ' ಪದದ ವಿರುದ್ಧಾರ್ಥಕ ಪದ ಯಾವುದು?",
            "text_alt": "What is the antonym of 'Amruta'?",
            "options": [{"label": "A", "text": "ಸುಧೆ"}, {"label": "B", "text": "ವಿಷ"}, {"label": "C", "text": "ಪೀಯೂಷ"}, {"label": "D", "text": "ಜೀವ"}],
            "answer": "B",
            "explanation": "ಅಮೃತ ಪದದ ವಿರುದ್ಧಾರ್ಥಕ ಪದ 'ವಿಷ' (ಅಥವಾ ಗರಳ)."
        },
        {
            "id": "P1-T1-KN-59", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "'ಚಂದ್ರ' ಪದಕ್ಕೆ ಸಮಾನಾರ್ಥಕವಲ್ಲದ ಪದವನ್ನು ಗುರುತಿಸಿ:",
            "text_alt": "Identify the word that is NOT a synonym for Chandrama/Moon:",
            "options": [{"label": "A", "text": "ಶಶಿ"}, {"label": "B", "text": "ತಿಂಗಳು"}, {"label": "C", "text": "ಭಾಸ್ಕರ"}, {"label": "D", "text": "ಸೋಮ"}],
            "answer": "C",
            "explanation": "'ಭಾಸ್ಕರ' ಎಂದರೆ ಸೂರ್ಯ. ಶಶಿ, ತಿಂಗಳು, ಸೋಮ, ಇಂದು ಇವೆಲ್ಲ ಚಂದ್ರನ ಸಮಾನಾರ್ಥಕ ಪದಗಳು."
        },
        {
            "id": "P1-T1-KN-60", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "'ಕುಂಬಾರನಿಗೆ ವರುಷ, ದಣ್ಣೆಗೊಂದು ನಿಮಿಷ' ಎಂಬ ಗಾದೆ ಮಾತು ಯಾವುದನ್ನು ಸೂಚಿಸುತ್ತದೆ?",
            "text_alt": "What does the proverb 'Kumbaranige varusha, dannegondu nimisha' signify?",
            "options": [{"label": "A", "text": "ಕುಂಬಾರನ ಕೆಲಸ ಬಹಳ ಸುಲಭ"}, {"label": "B", "text": "ಕಷ್ಟಪಟ್ಟು ನಿರ್ಮಿಸಲು ದೀರ್ಘಕಾಲ ಬೇಕು, ಆದರೆ ಅದನ್ನು ನಾಶಮಾಡಲು ಕೇವಲ ಕ್ಷಣಮಾತ್ರ ಸಾಕು"}, {"label": "C", "text": "ದಣ್ಣೆ ಬಹಳ ಬಲಶಾಲಿ"}, {"label": "D", "text": "ಕುಂಬಾರ ವರ್ಷಕ್ಕೆ ಒಮ್ಮೆ ಮಾತ್ರ ಮಡಕೆ ಮಾಡುತ್ತಾನೆ"}],
            "answer": "B",
            "explanation": "ಒಂದು ಒಳ್ಳೆಯ ವಸ್ತುವನ್ನು ಅಥವಾ ಸಂಬಂಧವನ್ನು ನಿರ್ಮಿಸಲು ವರ್ಷಗಟ್ಟಲೆ ಶ್ರಮ ಬೇಕು, ಆದರೆ ಅದನ್ನು ನಾಶಮಾಡಲು ಕ್ಷಣ ಸಾಕು ಎಂಬುದು ಇದರ ನೀತಿ."
        }
    ]
    qs.extend(kan)

    # ----------------------------------------------------
    # SECTION 4: GENERAL ENGLISH (25 QUESTIONS: Q61 to Q85)
    # ----------------------------------------------------
    eng = [
        {
            "id": "P1-T1-EN-61", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "easy",
            "text": "Fill in the blank with the correct tense form: 'The sun _____ in the east.'",
            "text_alt": "ಸರಿಯಾದ ಕಾಲರೂಪವನ್ನು ಆರಿಸಿ ಭರ್ತಿ ಮಾಡಿ: 'The sun _____ in the east.'",
            "options": [{"label": "A", "text": "rise"}, {"label": "B", "text": "rises"}, {"label": "C", "text": "is rising"}, {"label": "D", "text": "rose"}],
            "answer": "B",
            "explanation": "Universal truths and habitual actions take Simple Present Tense with third-person singular suffix '-s'/' -es' ('rises')."
        },
        {
            "id": "P1-T1-EN-62", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "Complete the sentence: 'She has been studying in this school _____ five years.'",
            "text_alt": "ವಾಕ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ: 'She has been studying in this school _____ five years.'",
            "options": [{"label": "A", "text": "since"}, {"label": "B", "text": "for"}, {"label": "C", "text": "from"}, {"label": "D", "text": "during"}],
            "answer": "B",
            "explanation": "'For' is used to denote a duration/period of time ('for five years'), whereas 'since' denotes a specific starting point."
        },
        {
            "id": "P1-T1-EN-63", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Identify the passive voice form of: 'The teacher praised the honest student.'",
            "text_alt": "ಕರ್ಮಣಿ ಪ್ರಯೋಗದ ರೂಪವನ್ನು ಗುರುತಿಸಿ: 'The teacher praised the honest student.'",
            "options": [{"label": "A", "text": "The honest student was praised by the teacher."}, {"label": "B", "text": "The honest student is praised by the teacher."}, {"label": "C", "text": "The honest student had been praised by the teacher."}, {"label": "D", "text": "The honest student praised the teacher."}],
            "answer": "A",
            "explanation": "Simple past active ('praised') changes into 'was/were + past participle' in the passive voice ('was praised by the teacher')."
        },
        {
            "id": "P1-T1-EN-64", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Choose the correct indirect speech form of: He said, 'I have finished my homework.'",
            "text_alt": "ಪರೋಕ್ಷ ಕಥನ ರೂಪವನ್ನು ಆರಿಸಿ: He said, 'I have finished my homework.'",
            "options": [{"label": "A", "text": "He said that he has finished his homework."}, {"label": "B", "text": "He said that he had finished his homework."}, {"label": "C", "text": "He said that he finished his homework."}, {"label": "D", "text": "He told that he had finished his homework."}],
            "answer": "B",
            "explanation": "In indirect speech with past reporting verb ('said'), Present Perfect ('have finished') shifts back to Past Perfect ('had finished')."
        },
        {
            "id": "P1-T1-EN-65", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "Fill in the blank with the appropriate preposition: 'He is proficient _____ computer programming.'",
            "text_alt": "ಸೂಕ್ತವಾದ ಪ್ರಿಪೊಸಿಷನ್ ಅನ್ನು ಆರಿಸಿ: 'He is proficient _____ computer programming.'",
            "options": [{"label": "A", "text": "at"}, {"label": "B", "text": "in"}, {"label": "C", "text": "with"}, {"label": "D", "text": "on"}],
            "answer": "B",
            "explanation": "The adjective 'proficient' takes the preposition 'in' when referring to a field, language, or subject."
        },
        {
            "id": "P1-T1-EN-66", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Choose the correct preposition: 'The principal congratulated the students _____ their outstanding performance.'",
            "text_alt": "ಸರಿಯಾದ ಪ್ರಿಪೊಸಿಷನ್ ಆರಿಸಿ: 'The principal congratulated the students _____ their outstanding performance.'",
            "options": [{"label": "A", "text": "for"}, {"label": "B", "text": "on"}, {"label": "C", "text": "at"}, {"label": "D", "text": "with"}],
            "answer": "B",
            "explanation": "'Congratulate' is followed by the preposition 'on' (congratulate someone on something)."
        },
        {
            "id": "P1-T1-EN-67", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "easy",
            "text": "Fill in the blank with the appropriate article: 'He is _____ European citizen residing in Karnataka.'",
            "text_alt": "ಸೂಕ್ತವಾದ ಉಪಪದವನ್ನು (article) ಆರಿಸಿ: 'He is _____ European citizen residing in Karnataka.'",
            "options": [{"label": "A", "text": "a"}, {"label": "B", "text": "an"}, {"label": "C", "text": "the"}, {"label": "D", "text": "no article"}],
            "answer": "A",
            "explanation": "Although 'European' begins with vowel letter 'E', it begins with the consonant glide sound /j/ (yu-), requiring indefinite article 'a'."
        },
        {
            "id": "P1-T1-EN-68", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Fill in the blank with the correct article: 'Copper is _____ useful metal.'",
            "text_alt": "ಖಾಲಿ ಜಾಗವನ್ನು ಭರ್ತಿ ಮಾಡಿ: 'Copper is _____ useful metal.'",
            "options": [{"label": "A", "text": "a"}, {"label": "B", "text": "an"}, {"label": "C", "text": "the"}, {"label": "D", "text": "no article"}],
            "answer": "A",
            "explanation": "'Useful' begins with the consonant sound /juː/ ('yoo'), so it takes 'a', not 'an'."
        },
        {
            "id": "P1-T1-EN-69", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "hard",
            "text": "Select the option with correct Subject-Verb Agreement: 'Neither the teacher nor the students _____ present in the auditorium.'",
            "text_alt": "ಕರ್ತೃ-ಕ್ರಿಯಾಪದ ಹೊಂದಾಣಿಕೆಯಿರುವ ಸರಿಯಾದ ವಾಕ್ಯವನ್ನು ಆರಿಸಿ:",
            "options": [{"label": "A", "text": "was"}, {"label": "B", "text": "were"}, {"label": "C", "text": "is"}, {"label": "D", "text": "has been"}],
            "answer": "B",
            "explanation": "When two subjects are joined by 'neither... nor', the verb agrees in number with the nearer subject ('students' is plural -> 'were')."
        },
        {
            "id": "P1-T1-EN-70", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Complete the conditional clause: 'If it rains tomorrow, we _____ the picnic.'",
            "text_alt": "ಷರತ್ತುಬದ್ಧ ವಾಕ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ: 'If it rains tomorrow, we _____ the picnic.'",
            "options": [{"label": "A", "text": "would cancel"}, {"label": "B", "text": "will cancel"}, {"label": "C", "text": "cancelled"}, {"label": "D", "text": "would have cancelled"}],
            "answer": "B",
            "explanation": "First conditional (real present/future possibility): 'If + Simple Present (rains)' takes 'will + base verb (will cancel)' in the main clause."
        },
        {
            "id": "P1-T1-EN-71", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Identify the grammatically correct sentence:",
            "text_alt": "ವ್ಯಾಕರಣಬದ್ಧವಾಗಿ ಸರಿಯಾದ ವಾಕ್ಯವನ್ನು ಗುರುತಿಸಿ:",
            "options": [{"label": "A", "text": "Scarcely had I entered the room when the lights went off."}, {"label": "B", "text": "Scarcely had I entered the room than the lights went off."}, {"label": "C", "text": "No sooner had I entered the room when the lights went off."}, {"label": "D", "text": "Hardly had I entered the room than the lights went off."}],
            "answer": "A",
            "explanation": "'Scarcely' and 'Hardly' correlate with 'when', while 'No sooner' correlates with 'than'."
        },
        {
            "id": "P1-T1-EN-72", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "easy",
            "text": "What is the synonym of the word 'BENEVOLENT'?",
            "text_alt": "'BENEVOLENT' ಪದದ ಸಮಾನಾರ್ಥಕ ಪದ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Cruel"}, {"label": "B", "text": "Generous and kind"}, {"label": "C", "text": "Selfish"}, {"label": "D", "text": "Arrogant"}],
            "answer": "B",
            "explanation": "'Benevolent' means well-meaning, kindly, and charitable ('Generous and kind')."
        },
        {
            "id": "P1-T1-EN-73", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "What is the antonym of the word 'CANDID'?",
            "text_alt": "'CANDID' ಪದದ ವಿರುದ್ಧಾರ್ಥಕ ಪದ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Frank"}, {"label": "B", "text": "Deceitful"}, {"label": "C", "text": "Honest"}, {"label": "D", "text": "Outspoken"}],
            "answer": "B",
            "explanation": "'Candid' means truthful, straightforward, and frank. Its opposite is 'deceitful' or secretive."
        },
        {
            "id": "P1-T1-EN-74", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "What is the meaning of the idiom 'To burn the midnight oil'?",
            "text_alt": "'To burn the midnight oil' ಎಂಬ ನುಡಿಗಟ್ಟಿನ ಅರ್ಥವೇನು?",
            "options": [{"label": "A", "text": "To waste kerosene oil"}, {"label": "B", "text": "To work or study late into the night"}, {"label": "C", "text": "To cause accidental fire"}, {"label": "D", "text": "To sleep soundly through the night"}],
            "answer": "B",
            "explanation": "'To burn the midnight oil' means to work hard late into the night (especially studying or preparing)."
        },
        {
            "id": "P1-T1-EN-75", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "medium",
            "text": "What does the idiom 'A blessing in disguise' mean?",
            "text_alt": "'A blessing in disguise' ನುಡಿಗಟ್ಟಿನ ಅರ್ಥವೇನು?",
            "options": [{"label": "A", "text": "A curse delivered by a holy man"}, {"label": "B", "text": "An apparent misfortune that eventually results in good outcome"}, {"label": "C", "text": "A visible miracle"}, {"label": "D", "text": "A deceptive promise"}],
            "answer": "B",
            "explanation": "A blessing in disguise refers to an unfortunate event that seemed bad initially but turned out to produce positive results."
        },
        {
            "id": "P1-T1-EN-76", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Choose the correctly spelled word:",
            "text_alt": "ಸರಿಯಾಗಿ ಕಾಗುಣಿತವಿರುವ (spelled) ಪದವನ್ನು ಆರಿಸಿ:",
            "options": [{"label": "A", "text": "Accommodate"}, {"label": "B", "text": "Acommodate"}, {"label": "C", "text": "Accomodate"}, {"label": "D", "text": "Acomodate"}],
            "answer": "A",
            "explanation": "The correct spelling is 'Accommodate' with double 'c' and double 'm'."
        },
        {
            "id": "P1-T1-EN-77", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Choose the correctly spelled word:",
            "text_alt": "ಸರಿಯಾದ ಕಾಗುಣಿತವಿರುವ ಪದವನ್ನು ಆರಿಸಿ:",
            "options": [{"label": "A", "text": "Maintanence"}, {"label": "B", "text": "Maintainence"}, {"label": "C", "text": "Maintenance"}, {"label": "D", "text": "Maintenence"}],
            "answer": "C",
            "explanation": "The correct spelling is 'Maintenance'."
        },
        {
            "id": "P1-T1-EN-78", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "hard",
            "text": "Spot the error in the sentence: 'One of the student (A) / was selected (B) / for the national award (C) / No error (D)'",
            "text_alt": "ವಾಕ್ಯದಲ್ಲಿನ ವ್ಯಾಕರಣ ದೋಷವಿರುವ ಭಾಗವನ್ನು ಗುರುತಿಸಿ:",
            "options": [{"label": "A", "text": "One of the student"}, {"label": "B", "text": "was selected"}, {"label": "C", "text": "for the national award"}, {"label": "D", "text": "No error"}],
            "answer": "A",
            "explanation": "The phrase 'one of the...' must be followed by a plural noun ('One of the students', not 'student')."
        },
        {
            "id": "P1-T1-EN-79", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Choose the one-word substitution for: 'A person who looks at the bright, hopeful side of things.'",
            "text_alt": "ಒಂದೇ ಪದದ ಬದಲಿ ಪದವನ್ನು ಆರಿಸಿ: 'A person who looks at the bright side.'",
            "options": [{"label": "A", "text": "Pessimist"}, {"label": "B", "text": "Optimist"}, {"label": "C", "text": "Altruist"}, {"label": "D", "text": "Philanthropist"}],
            "answer": "B",
            "explanation": "An 'optimist' is a person inclined to be hopeful and expect favorable outcomes."
        },
        {
            "id": "P1-T1-EN-80", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Choose the one-word substitution for: 'An autobiography is the life history of a person written by _____.'",
            "text_alt": "ಖಾಲಿ ಜಾಗವನ್ನು ಭರ್ತಿ ಮಾಡಿ: 'An autobiography is written by _____.'",
            "options": [{"label": "A", "text": "another author"}, {"label": "B", "text": "himself or herself"}, {"label": "C", "text": "a professional biographer"}, {"label": "D", "text": "an anonymous writer"}],
            "answer": "B",
            "explanation": "An autobiography is an account of a person\'s life written by that person."
        },
        {
            "id": "P1-T1-EN-81", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Fill in the blank with the appropriate question tag: 'She sings melodiously, _____?'",
            "text_alt": "ಸೂಕ್ತವಾದ ಪ್ರಶ್ನಾರ್ಥಕ ಟ್ಯಾಗ್ (question tag) ಆರಿಸಿ: 'She sings melodiously, _____?'",
            "options": [{"label": "A", "text": "does she"}, {"label": "B", "text": "doesn\'t she"}, {"label": "C", "text": "is she"}, {"label": "D", "text": "isn\'t she"}],
            "answer": "B",
            "explanation": "Positive statement in Simple Present ('sings') takes negative auxiliary question tag 'doesn\'t she?'."
        },
        {
            "id": "P1-T1-EN-82", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Fill in the blank with the appropriate question tag: 'Let us begin the session, _____?'",
            "text_alt": "ಸೂಕ್ತವಾದ ಪ್ರಶ್ನಾರ್ಥಕ ಟ್ಯಾಗ್ ಆರಿಸಿ: 'Let us begin the session, _____?'",
            "options": [{"label": "A", "text": "will we"}, {"label": "B", "text": "shall we"}, {"label": "C", "text": "can we"}, {"label": "D", "text": "should we"}],
            "answer": "B",
            "explanation": "Suggestions beginning with 'Let us' or 'Let\'s' conventionally take the tag 'shall we?'."
        },
        {
            "id": "P1-T1-EN-83", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "easy",
            "text": "What is the plural form of the noun 'Criterion'?",
            "text_alt": "'Criterion' ನಾಮಪದದ ಬಹುವಚನ ರೂಪ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Criterions"}, {"label": "B", "text": "Criteria"}, {"label": "C", "text": "Criterias"}, {"label": "D", "text": "Criterium"}],
            "answer": "B",
            "explanation": "'Criterion' (Greek origin) forms its plural as 'Criteria'."
        },
        {
            "id": "P1-T1-EN-84", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "What is the feminine gender form of 'Bachelor'?",
            "text_alt": "'Bachelor' ಪದದ ಸ್ತ್ರೀಲಿಂಗ ರೂಪ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Spinster / Bachelorette"}, {"label": "B", "text": "Widow"}, {"label": "C", "text": "Matron"}, {"label": "D", "text": "Dame"}],
            "answer": "A",
            "explanation": "The feminine counterpart of bachelor (unmarried man) is spinster or bachelorette."
        },
        {
            "id": "P1-T1-EN-85", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Identify the figure of speech in: 'The classroom was a zoo during the lunch break.'",
            "text_alt": "ವಾಕ್ಯದಲ್ಲಿರುವ ಅಲಂಕಾರವನ್ನು (figure of speech) ಗುರುತಿಸಿ:",
            "options": [{"label": "A", "text": "Simile"}, {"label": "B", "text": "Metaphor"}, {"label": "C", "text": "Personification"}, {"label": "D", "text": "Hyperbole"}],
            "answer": "B",
            "explanation": "A direct comparison equating two different entities without using 'like' or 'as' is a Metaphor."
        }
    ]
    qs.extend(eng)

    # ----------------------------------------------------
    # SECTION 5: EDUCATIONAL PSYCHOLOGY (25 QUESTIONS: Q86 to Q110)
    # ----------------------------------------------------
    psy = [
        {
            "id": "P1-T1-EP-86", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "According to Jean Piaget, at which cognitive developmental stage does a child achieve 'Object Permanence'?",
            "text_alt": "ಜೀನ್ ಪಿಯಾಜೆ ಪ್ರಕಾರ, ಮಗು ಯಾವ ಜ್ಞಾನಾತ್ಮಕ ವಿಕಾಸದ ಹಂತದಲ್ಲಿ 'ವಸ್ತು ಸ್ಥಿರತೆ'ಯನ್ನು (Object Permanence) ಸಾಧಿಸುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Sensorimotor Stage (0 to 2 Years)"}, {"label": "B", "text": "Pre-Operational Stage (2 to 7 Years)"}, {"label": "C", "text": "Concrete Operational Stage (7 to 11 Years)"}, {"label": "D", "text": "Formal Operational Stage (11+ Years)"}],
            "answer": "A",
            "explanation": "Object permanence emerges around 8–9 months of age during the Sensorimotor stage (0–2 years)."
        },
        {
            "id": "P1-T1-EP-87", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "A child in Piaget\'s Pre-Operational stage who believes that the sun follows them when they walk is demonstrating which cognitive characteristic?",
            "text_alt": "ತಾನು ನಡೆಯುವಾಗ ಸೂರ್ಯನೂ ತನ್ನನ್ನೇ ಹಿಂಬಾಲಿಸುತ್ತಾನೆ ಎಂದು ನಂಬುವ ಮಗುವಿನ ಈ ವರ್ತನೆಯು ಪಿಯಾಜೆಯ ಪ್ರಕಾರ ಯಾವುದನ್ನು ಸೂಚಿಸುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Object Permanence"}, {"label": "B", "text": "Egocentrism & Animism"}, {"label": "C", "text": "Conservation"}, {"label": "D", "text": "Reversibility"}],
            "answer": "B",
            "explanation": "Pre-operational children exhibit Egocentrism (assuming the world revolves around their perspective) and Animism (attributing consciousness to inanimate objects)."
        },
        {
            "id": "P1-T1-EP-88", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "According to Piaget, modifying existing mental schemas or creating brand new schemas when confronted with conflicting experiences is termed:",
            "text_alt": "ಹೊಸ ಅನುಭವಕ್ಕೆ ತಕ್ಕಂತೆ ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ಯೋಜನೆಗಳನ್ನು ಮಾರ್ಪಡಿಸುವುದು ಅಥವಾ ಹೊಸ ಯೋಜನೆಗಳನ್ನು ರಚಿಸುವುದನ್ನು ಪಿಯಾಜೆ ಏನೆಂದು ಕರೆದಿದ್ದಾರೆ?",
            "options": [{"label": "A", "text": "Assimilation"}, {"label": "B", "text": "Accommodation"}, {"label": "C", "text": "Equilibration"}, {"label": "D", "text": "Conservation"}],
            "answer": "B",
            "explanation": "Assimilation fits new data into old schemas; Accommodation modifies or creates new schemas when old schemas fail."
        },
        {
            "id": "P1-T1-EP-89", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "Lev Vygotsky defined the distance between what a child can do independently and what they can achieve with guidance as:",
            "text_alt": "ಮಗು ಸ್ವತಂತ್ರವಾಗಿ ಮಾಡಬಲ್ಲ ಮತ್ತು ಇತರರ ನೆರವಿನಿಂದ ಸಾಧಿಸಬಹುದಾದ ಸಾಮರ್ಥ್ಯದ ನಡುವಿನ ಅಂತರವನ್ನು ವೈಗೋಟ್ಸ್ಕಿ ಏನೆಂದು ಕರೆದಿದ್ದಾರೆ?",
            "options": [{"label": "A", "text": "Zone of Proximal Development (ZPD)"}, {"label": "B", "text": "Scaffolding Zone"}, {"label": "C", "text": "Equilibration Space"}, {"label": "D", "text": "Cognitive Schema"}],
            "answer": "A",
            "explanation": "The Zone of Proximal Development (ZPD) is the range of tasks a learner cannot yet perform alone but can accomplish with scaffolding from an MKO."
        },
        {
            "id": "P1-T1-EP-90", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Who coined the instructional term 'Scaffolding' to describe temporary teacher support that is gradually removed as the child gains mastery?",
            "text_alt": "ಕಲಿಕೆಯಲ್ಲಿ ಆರಂಭಿಕ ಹಂತದಲ್ಲಿ ನೀಡುವ ತಾತ್ಕಾಲಿಕ ಬೆಂಬಲವನ್ನು ಸೂಚಿಸುವ 'ಸ್ಕ್ಯಾಫೋಲ್ಡಿಂಗ್' (ಹಂದರ ಒದಗಿಸುವಿಕೆ) ಪದವನ್ನು ಮೊದಲು ಬಳಸಿದವರು ಯಾರು?",
            "options": [{"label": "A", "text": "Jean Piaget"}, {"label": "B", "text": "Jerome Bruner"}, {"label": "C", "text": "B. F. Skinner"}, {"label": "D", "text": "Edward Thorndike"}],
            "answer": "B",
            "explanation": "The term 'Scaffolding' was coined by Jerome Bruner, David Wood, and Gail Ross (1976) and operationalized within Vygotsky\'s ZPD framework."
        },
        {
            "id": "P1-T1-EP-91", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which developmental progression represents Jerome Bruner\'s Three Modes of Representation in correct chronological sequence?",
            "text_alt": "ಜೆರೋಮ್ ಬ್ರೂನರ್ ಅವರ ಜ್ಞಾನ ಪ್ರಾತಿನಿಧಿಕ ಹಂತಗಳ ಸರಿಯಾದ ಅನುಕ್ರಮ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Enactive -> Iconic -> Symbolic"}, {"label": "B", "text": "Iconic -> Enactive -> Symbolic"}, {"label": "C", "text": "Symbolic -> Iconic -> Enactive"}, {"label": "D", "text": "Enactive -> Symbolic -> Iconic"}],
            "answer": "A",
            "explanation": "Bruner posited: 1. Enactive (action-based, 0–1 yr), 2. Iconic (image-based, 1–6 yrs), 3. Symbolic (language/code-based, 7+ yrs)."
        },
        {
            "id": "P1-T1-EP-92", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "medium",
            "text": "Which Primary Law of Learning formulated by E. L. Thorndike states that connections are strengthened when followed by satisfaction/reward and weakened when followed by discomfort?",
            "text_alt": "ತೃಪ್ತಿದಾಯಕ ಫಲಿತಾಂಶ ನೀಡುವ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಬಲಗೊಳ್ಳುತ್ತವೆ ಎಂಬುದನ್ನು ತಿಳಿಸುವ ಇ. ಎಲ್. ಥಾರ್ನ್‌ಡೈಕ್ ಅವರ ನಿಯಮ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Law of Readiness"}, {"label": "B", "text": "Law of Exercise"}, {"label": "C", "text": "Law of Effect"}, {"label": "D", "text": "Law of Multiple Response"}],
            "answer": "C",
            "explanation": "Thorndike\'s Law of Effect established that responses followed by satisfying consequences are more likely to recur, directly anticipating operant conditioning."
        },
        {
            "id": "P1-T1-EP-93", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "hard",
            "text": "In B. F. Skinner\'s Operant Conditioning, which reinforcement schedule produces the highest rate of responses and the greatest resistance to extinction?",
            "text_alt": "ಬಿ. ಎಫ್. ಸ್ಕಿನ್ನರ್ ಅವರ ಕಾರ್ಯಾಚರಣೆ ಅನುಬಂಧನದಲ್ಲಿ, ಅತ್ಯಂತ ಹೆಚ್ಚಿನ ಪ್ರತಿಕ್ರಿಯಾ ದರ ಮತ್ತು ಅಳಿಸಿಹೋಗುವಿಕೆಗೆ ಗರಿಷ್ಠ ಪ್ರತಿರೋಧ ಒದಗಿಸುವ ವೇಳಾಪಟ್ಟಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Fixed Ratio (FR)"}, {"label": "B", "text": "Fixed Interval (FI)"}, {"label": "C", "text": "Variable Ratio (VR)"}, {"label": "D", "text": "Variable Interval (VI)"}],
            "answer": "C",
            "explanation": "Variable Ratio (VR) schedule (exemplified by gambling/slot machines) reinforces after unpredictable numbers of responses, yielding intense persistence."
        },
        {
            "id": "P1-T1-EP-94", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "In Ivan Pavlov\'s classical experiment with dogs, what was the Conditioned Stimulus (CS)?",
            "text_alt": "ಇವಾನ್ ಪಾವ್ಲೋವ್ ಅವರ ಪ್ರಸಿದ್ಧ ಪ್ರಯೋಗದಲ್ಲಿ 'ಅನುಬಂಧಿತ ಉದ್ದೀಪನ' (CS) ಯಾವುದಾಗಿತ್ತು?",
            "options": [{"label": "A", "text": "Meat powder (Food)"}, {"label": "B", "text": "Salivation to food"}, {"label": "C", "text": "Sound of the Bell"}, {"label": "D", "text": "Salivation to bell"}],
            "answer": "C",
            "explanation": "Food is Unconditioned Stimulus (UCS); Bell initially is Neutral Stimulus (NS), and after repeated pairing becomes the Conditioned Stimulus (CS)."
        },
        {
            "id": "P1-T1-EP-95", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "What are the four essential sub-processes of Observational Learning identified in Albert Bandura\'s Social Cognitive Theory?",
            "text_alt": "ಆಲ್ಬರ್ಟ್ ಬಂಡೂರ ಅವರ ಸಾಮಾಜಿಕ ಕಲಿಕಾ ಸಿದ್ಧಾಂತದಲ್ಲಿ ವೀಕ್ಷಣಾ ಕಲಿಕೆಯ ನಾಲ್ಕು ಮುಖ್ಯ ಹಂತಗಳು ಯಾವುವು?",
            "options": [{"label": "A", "text": "Attention -> Retention -> Reproduction -> Motivation"}, {"label": "B", "text": "Perception -> Assimilation -> Storage -> Retrieval"}, {"label": "C", "text": "Readiness -> Exercise -> Effect -> Feedback"}, {"label": "D", "text": "Stimulus -> Response -> Reinforcement -> Generalization"}],
            "answer": "A",
            "explanation": "Bandura specified: 1. Attention (observing), 2. Retention (memorizing), 3. Reproduction (motor execution), 4. Motivation (incentive/reinforcement)."
        },
        {
            "id": "P1-T1-EP-96", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Wolfgang Köhler\'s famous experiment with Sultan the chimpanzee using bamboo sticks to reach bananas demonstrated which form of learning?",
            "text_alt": "ಚಿಂಪಾಂಜಿ ಸುಲ್ತಾನ್ ಮೇಲೆ ವುಲ್ಫ್‌ಗ್ಯಾಂಗ್ ಕೊಹ್ಲರ್ ನಡೆಸಿದ ಪ್ರಯೋಗವು ಯಾವ ಬಗೆಯ ಕಲಿಕೆಯನ್ನು ಸಾಬೀತುಪಡಿಸಿತು?",
            "options": [{"label": "A", "text": "Trial and Error Learning"}, {"label": "B", "text": "Operant Conditioning"}, {"label": "C", "text": "Insight Learning (Gestalt)"}, {"label": "D", "text": "Classical Conditioning"}],
            "answer": "C",
            "explanation": "Köhler showed that problem-solving occurs through sudden cognitive restructuring of the perceptual whole, termed Insight Learning (Aha! experience)."
        },
        {
            "id": "P1-T1-EP-97", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "Howard Gardner proposed the Multiple Intelligences theory. Which of the following is NOT one of Gardner\'s original multiple intelligences?",
            "text_alt": "ಹೋವರ್ಡ್ ಗಾರ್ಡ್ನರ್ ಅವರ ಬಹುಮುಖಿ ಬುದ್ಧಿಶಕ್ತಿ ಸಿದ್ಧಾಂತದಲ್ಲಿ ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಸೇರಿಲ್ಲ?",
            "options": [{"label": "A", "text": "Bodily-Kinesthetic Intelligence"}, {"label": "B", "text": "Interpersonal Intelligence"}, {"label": "C", "text": "General General-g Intelligence"}, {"label": "D", "text": "Musical Intelligence"}],
            "answer": "C",
            "explanation": "Gardner explicitly rejected Charles Spearman\'s unitary general factor ('g-factor') in favor of 8+ independent modular intelligences."
        },
        {
            "id": "P1-T1-EP-98", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "In Robert Sternberg\'s Triarchic Theory of Intelligence, what are the three sub-theories of intelligence?",
            "text_alt": "ರಾಬರ್ಟ್ ಸ್ಟರ್ನ್‌ಬರ್ಗ್ ಅವರ ತ್ರಿಮುಖ ಬುದ್ಧಿಶಕ್ತಿ ಸಿದ್ಧಾಂತದ ಮೂರು ವಿಧಗಳು ಯಾವುವು?",
            "options": [{"label": "A", "text": "Analytical, Creative, and Practical"}, {"label": "B", "text": "Linguistic, Spatial, and Logical"}, {"label": "C", "text": "Fluid, Crystallized, and General"}, {"label": "D", "text": "Verbal, Performance, and Motor"}],
            "answer": "A",
            "explanation": "Sternberg\'s Triarchic Theory comprises: 1. Analytical (Componential), 2. Creative (Experiential), and 3. Practical (Contextual) intelligences."
        },
        {
            "id": "P1-T1-EP-99", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "PYQ - GPSTR 2017", "difficulty": "easy",
            "text": "What is the standard formula for calculating the Intelligence Quotient (IQ) developed by William Stern and adopted by Lewis Terman?",
            "text_alt": "ವಿಲಿಯಂ ಸ್ಟರ್ನ್ ನೀಡಿದ ಬುದ್ಧಿಶಕ್ತಿ ಲಬ್ಧಿ (IQ) ಕಂಡುಹಿಡಿಯುವ ಸೂತ್ರ ಯಾವುದು?",
            "options": [{"label": "A", "text": "IQ = (Chronological Age / Mental Age) * 100"}, {"label": "B", "text": "IQ = (Mental Age / Chronological Age) * 100"}, {"label": "C", "text": "IQ = (Mental Age + Chronological Age) / 2"}, {"label": "D", "text": "IQ = (Mental Age * Chronological Age) / 100"}],
            "answer": "B",
            "explanation": "IQ = (Mental Age / Chronological Age) * 100."
        },
        {
            "id": "P1-T1-EP-100", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "According to Terman\'s Stanford-Binet IQ classification, what is the IQ score range for an individual categorized as having 'Average / Normal' intelligence?",
            "text_alt": "ಟರ್ಮನ್ ಅವರ ವರ್ಗೀಕರಣದ ಪ್ರಕಾರ 'ಸಾಮಾನ್ಯ / ಸರಾಸರಿ' ಬುದ್ಧಿಶಕ್ತಿಯ ಐಕ್ಯೂ (IQ) ಶ್ರೇಣಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "70 – 79"}, {"label": "B", "text": "80 – 89"}, {"label": "C", "text": "90 – 109"}, {"label": "D", "text": "120 – 139"}],
            "answer": "C",
            "explanation": "An IQ score between 90 and 109 represents Average or Normal intelligence (spanning approximately 50% of the human population)."
        },
        {
            "id": "P1-T1-EP-101", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "In Sigmund Freud\'s psychoanalytic model of personality, which structural component operates strictly on the 'Reality Principle' as an executive mediator?",
            "text_alt": "ಸಿಗ್ಮಂಡ್ ಫ್ರಾಯ್ಡ್ ಅವರ ಮನೋವಿಶ್ಲೇಷಣಾ ಸಿದ್ಧಾಂತದಲ್ಲಿ 'ವಾಸ್ತವತೆಯ ತತ್ವ'ದ (Reality Principle) ಮೇಲೆ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ವ್ಯಕ್ತಿತ್ವದ ಅಂಗ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Id"}, {"label": "B", "text": "Ego"}, {"label": "C", "text": "Superego"}, {"label": "D", "text": "Libido"}],
            "answer": "B",
            "explanation": "The Ego operates on the Reality Principle, mediating realistic compromises between primal demands of the Id and moral ideals of the Superego."
        },
        {
            "id": "P1-T1-EP-102", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "A student who fails an examination and makes excuses by blaming the strict evaluator ('The paper was out of syllabus; teacher hates me') is using which ego defense mechanism?",
            "text_alt": "ಪರೀಕ್ಷೆಯಲ್ಲಿ ಅನುತ್ತೀರ್ಣನಾದ ವಿದ್ಯಾರ್ಥಿಯು 'ಪ್ರಶ್ನೆಪತ್ರಿಕೆ ಕಠಿಣವಾಗಿತ್ತು, ಮೌಲ್ಯಮಾಪಕರಿಗೆ ನನ್ನ ಕಂಡರೆ ಆಗಲ್ಲ' ಎಂದು ಸಮರ್ಥಿಸಿಕೊಳ್ಳುವುದು ಯಾವ ಮನೋರಕ್ಷಣಾ ತಂತ್ರ?",
            "options": [{"label": "A", "text": "Projection"}, {"label": "B", "text": "Rationalization"}, {"label": "C", "text": "Sublimation"}, {"label": "D", "text": "Regression"}],
            "answer": "B",
            "explanation": "Rationalization involves creating plausible, socially acceptable excuses to justify failure and preserve self-esteem (popularly known as 'sour grapes')."
        },
        {
            "id": "P1-T1-EP-103", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "A child suffering from severe difficulty with reading fluency, letter reversals (confusing 'b' and 'd'), and word decoding is characterized by which specific learning disorder?",
            "text_alt": "ಓದುವಿಕೆ, ಅಕ್ಷರಗಳ ಗುರುತಿಸುವಿಕೆಯಲ್ಲಿ ತೀವ್ರ ತೊಂದರೆ ('b' ಮತ್ತು 'd' ಗೊಂದಲ) ಅನುಭವಿಸುವ ಮಗುವಿನ ಕಲಿಕಾ ನ್ಯೂನತೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Dyslexia"}, {"label": "B", "text": "Dysgraphia"}, {"label": "C", "text": "Dyscalculia"}, {"label": "D", "text": "Dyspraxia"}],
            "answer": "A",
            "explanation": "Dyslexia is a specific learning disability characterized by difficulties with accurate and fluent word recognition, decoding, and spelling."
        },
        {
            "id": "P1-T1-EP-104", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "Under the Rights of Persons with Disabilities (RPwD) Act, 2016, how many categories of disabilities are officially recognized in India?",
            "text_alt": "ಭಿಕಲಾಂಗ ವ್ಯಕ್ತಿಗಳ ಹಕ್ಕುಗಳ ಕಾಯ್ದೆ (RPwD Act) 2016 ರ ಅಡಿಯಲ್ಲಿ ಅಧಿಕೃತವಾಗಿ ಗುರುತಿಸಲಾದ ಅಂಗವೈಕಲ್ಯಗಳ ಸಂಖ್ಯೆ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "7 categories"}, {"label": "B", "text": "14 categories"}, {"label": "C", "text": "21 categories"}, {"label": "D", "text": "28 categories"}],
            "answer": "C",
            "explanation": "The RPwD Act 2016 expanded the number of recognized benchmark disabilities from 7 (under the 1995 Act) to 21 categories."
        },
        {
            "id": "P1-T1-EP-105", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "What is the primary objective of Continuous and Comprehensive Evaluation (CCE) in school education?",
            "text_alt": "ಶಾಲಾ ಶಿಕ್ಷಣದಲ್ಲಿ ನಿರಂತರ ಮತ್ತು ಸಮಗ್ರ ಮೌಲ್ಯಮಾಪನದ (CCE) ಮುಖ್ಯ ಉದ್ದೇಶವೇನು?",
            "options": [{"label": "A", "text": "To classify students into pass and fail categories strictly"}, {"label": "B", "text": "To evaluate both scholastic and co-scholastic holistic development of the child"}, {"label": "C", "text": "To reduce the number of working days for teachers"}, {"label": "D", "text": "To emphasize only end-of-year pen-and-paper tests"}],
            "answer": "B",
            "explanation": "CCE aims to cover all aspects of child growth: scholastic (cognitive) and co-scholastic (affective, psychomotor, life skills, values)."
        },
        {
            "id": "P1-T1-EP-106", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "Assessment conducted 'during' the teaching-learning process to diagnose learning gaps and adapt instructional methods is termed:",
            "text_alt": "ಕಲಿಕಾ ಪ್ರಕ್ರಿಯೆ ನಡೆಯುತ್ತಿರುವಾಗಲೇ ಕಲಿಕಾ ಕೊರತೆಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಮತ್ತು ಬೋಧನೆಯನ್ನು ಸುಧಾರಿಸಲು ನಡೆಸುವ ಮೌಲ್ಯಮಾಪನ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Summative Assessment (Assessment of Learning)"}, {"label": "B", "text": "Formative Assessment (Assessment for Learning)"}, {"label": "C", "text": "Prognostic Assessment"}, {"label": "D", "text": "Standardized Norm Assessment"}],
            "answer": "B",
            "explanation": "Formative assessment is 'Assessment for Learning', carried out during instruction to provide continuous pedagogical feedback."
        },
        {
            "id": "P1-T1-EP-107", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "If a test produces consistent and stable scores across repeated administrations to the same cohort under identical conditions, the test possesses high:",
            "text_alt": "ಒಂದು ಪರೀಕ್ಷೆಯನ್ನು ಒಂದೇ ಗುಂಪಿಗೆ ಪುನರಾವರ್ತಿತವಾಗಿ ನಡೆಸಿದಾಗ ಸ್ಥಿರವಾದ ಅಂಕಗಳು ಬಂದರೆ, ಆ ಪರೀಕ್ಷೆಯು ಏನನ್ನು ಹೊಂದಿದೆ ಎನ್ನಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Validity (ಸಿಂಧುತ್ವ)"}, {"label": "B", "text": "Reliability (ವಿಶ್ವಾಸಾರ್ಹತೆ)"}, {"label": "C", "text": "Objectivity (ವಸ್ತುನಿಷ್ಠತೆ)"}, {"label": "D", "text": "Usability (ಉಪಯುಕ್ತತೆ)"}],
            "answer": "B",
            "explanation": "Reliability is the degree of consistency and repeatability of test scores. (Validity measures whether the test measures what it claims to measure)."
        },
        {
            "id": "P1-T1-EP-108", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "In the Revised Bloom\'s Taxonomy (Anderson & Krathwohl, 2001), which is the highest cognitive process dimension?",
            "text_alt": "ಪರಿಷ್ಕೃತ ಬ್ಲೂಮ್ಸ್ ಜ್ಞಾನಾತ್ಮಕ ಶ್ರೇಣೀಕರಣದಲ್ಲಿ (2001) ಅತ್ಯುನ್ನತ ಹಂತ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Analyze"}, {"label": "B", "text": "Evaluate"}, {"label": "C", "text": "Create (ಸೃಜಿಸುವುದು)"}, {"label": "D", "text": "Apply"}],
            "answer": "C",
            "explanation": "The revised hierarchy is: Remember -> Understand -> Apply -> Analyze -> Evaluate -> Create (highest level)."
        },
        {
            "id": "P1-T1-EP-109", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "The flat horizontal portion of a learning curve that indicates no visible improvement in performance despite ongoing practice is called a:",
            "text_alt": "ಅಭ್ಯಾಸ ಮುಂದುವರಿದಿದ್ದರೂ ಕಲಿಕೆಯಲ್ಲಿ ಯಾವುದೇ ಗೋಚರ ಪ್ರಗತಿ ಕಾಣದಿರುವ ಕಲಿಕಾ ರೇಖೆಯ ಸಮತಟ್ಟಾದ ಭಾಗವನ್ನು ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "options": [{"label": "A", "text": "Learning Peak"}, {"label": "B", "text": "Learning Plateau (ಕಲಿಕಾ ಪ್ರಸ್ಥಭೂಮಿ)"}, {"label": "C", "text": "Extinction Point"}, {"label": "D", "text": "Ceiling Effect"}],
            "answer": "B",
            "explanation": "A Learning Plateau occurs when progress stalls due to fatigue, loss of interest, reaching limits of current strategy, or physiological ceiling."
        },
        {
            "id": "P1-T1-EP-110", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "At which level of Abraham Maslow\'s Hierarchy of Needs does an individual strive to realize their fullest creative human potential?",
            "text_alt": "ಅಬ್ರಹಾಂ ಮಾಸ್ಲೋ ಅವರ ಅಗತ್ಯಗಳ ಶ್ರೇಣೀಕರಣದಲ್ಲಿ ವ್ಯಕ್ತಿಯು ತನ್ನ ಗರಿಷ್ಠ ಸೃಜನಶೀಲ ಸಾಮರ್ಥ್ಯವನ್ನು ಸಾಧಿಸಲು ಬಯಸುವ ಉನ್ನತ ಹಂತ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Safety Needs"}, {"label": "B", "text": "Esteem Needs"}, {"label": "C", "text": "Self-Actualisation (ಸ್ವಯಂ ಸಾಕ್ಷಾತ್ಕಾರ)"}, {"label": "D", "text": "Belongingness Needs"}],
            "answer": "C",
            "explanation": "Self-Actualization is the pinnacle growth need where a person seeks fulfillment of personal potential, self-fulfillment, and peak experiences."
        }
    ]
    qs.extend(psy)

    # ----------------------------------------------------
    # SECTION 6: COMPUTER LITERACY (20 QUESTIONS: Q111 to Q130)
    # ----------------------------------------------------
    comp = [
        {
            "id": "P1-T1-CL-111", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "easy",
            "text": "Which of the following is considered the 'Brain' of a computer system that performs all arithmetic and logical operations?",
            "text_alt": "ಗಣಕಯಂತ್ರದ ಎಲ್ಲಾ ಅಂಕಗಣಿತ ಮತ್ತು ತಾರ್ಕಿಕ ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಕಂಪ್ಯೂಟರ್‌ನ 'ಮೆದುಳು' ಯಾವುದು?",
            "options": [{"label": "A", "text": "RAM"}, {"label": "B", "text": "Central Processing Unit (CPU)"}, {"label": "C", "text": "Hard Disk"}, {"label": "D", "text": "Motherboard"}],
            "answer": "B",
            "explanation": "The Central Processing Unit (CPU), comprising the ALU and Control Unit, executes program instructions."
        },
        {
            "id": "P1-T1-CL-112", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "easy",
            "text": "Which type of computer memory is volatile, losing all its stored contents when the electric power is turned off?",
            "text_alt": "ವಿದ್ಯುತ್ ಸ್ಥಗಿತಗೊಂಡಾಗ ತನ್ನಲ್ಲಿ ಸಂಗ್ರಹವಾಗಿರುವ ಮಾಹಿತಿಯನ್ನು ಕಳೆದುಕೊಳ್ಳುವ ಅಸ್ಥಿರ (Volatile) ಮೆಮೊರಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Read Only Memory (ROM)"}, {"label": "B", "text": "Random Access Memory (RAM)"}, {"label": "C", "text": "Flash Memory"}, {"label": "D", "text": "Hard Disk"}],
            "answer": "B",
            "explanation": "RAM is volatile primary memory requiring constant electrical power to maintain stored data."
        },
        {
            "id": "P1-T1-CL-113", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "What is the primary function of high-speed Cache Memory positioned between the CPU and main RAM?",
            "text_alt": "ಸಿಪಿಯು ಮತ್ತು ಮುಖ್ಯ ಮೆಮೊರಿ ನಡುವೆ ಇರುವ ಹೈ-ಸ್ಪೀಡ್ ಕ್ಯಾಶ್ ಮೆಮೊರಿಯ ಮುಖ್ಯ ಕಾರ್ಯವೇನು?",
            "options": [{"label": "A", "text": "To permanently store operating system installation files"}, {"label": "B", "text": "To bridge the speed disparity between fast CPU registers and slower RAM"}, {"label": "C", "text": "To protect the computer from network viruses"}, {"label": "D", "text": "To connect peripheral I/O devices"}],
            "answer": "B",
            "explanation": "Cache memory holds frequently accessed instructions and data to minimize memory latency."
        },
        {
            "id": "P1-T1-CL-114", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "easy",
            "text": "In Microsoft Word, which keyboard shortcut is used to 'Paste' copied or cut text from the clipboard?",
            "text_alt": "ಎಂಎಸ್ ವರ್ಡ್‌ನಲ್ಲಿ ನಕಲು ಮಾಡಿದ ಪಠ್ಯವನ್ನು ಅಂಟಿಸಲು (Paste) ಬಳಸುವ ಕೀಬೋರ್ಡ್ ಶಾರ್ಟ್‌ಕಟ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Ctrl + C"}, {"label": "B", "text": "Ctrl + P"}, {"label": "C", "text": "Ctrl + V"}, {"label": "D", "text": "Ctrl + X"}],
            "answer": "C",
            "explanation": "Ctrl + C copies, Ctrl + X cuts, and Ctrl + V pastes from the clipboard."
        },
        {
            "id": "P1-T1-CL-115", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which feature in Microsoft Word is used to generate personalized letters, certificates, or envelopes in bulk from a single data source table?",
            "text_alt": "ಒಂದೇ ಮೂಲ ಪಟ್ಟಿಯಿಂದ ನೂರಾರು ವೈಯಕ್ತಿಕಗೊಳಿಸಿದ ಪತ್ರಗಳು ಅಥವಾ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಮುದ್ರಿಸಲು ಬಳಸುವ ಎಂಎಸ್ ವರ್ಡ್ ಸೌಲಭ್ಯ ಯಾವುದು?",
            "options": [{"label": "A", "text": "AutoCorrect"}, {"label": "B", "text": "Mail Merge"}, {"label": "C", "text": "Track Changes"}, {"label": "D", "text": "Cross-Reference"}],
            "answer": "B",
            "explanation": "Mail Merge merges a template document with a data source (e.g., an Excel sheet or Access database) to produce customized bulk letters."
        },
        {
            "id": "P1-T1-CL-116", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "In Microsoft Excel, every formula or calculation MUST begin with which character?",
            "text_alt": "ಎಂಎಸ್ ಎಕ್ಸೆಲ್‌ನಲ್ಲಿ ಪ್ರತಿಯೊಂದು ಸೂತ್ರವು (formula) ಕಡ್ಡಾಯವಾಗಿ ಯಾವ ಚಿಹ್ನೆಯಿಂದ ಪ್ರಾರಂಭವಾಗಬೇಕು?",
            "options": [{"label": "A", "text": "# (Hash)"}, {"label": "B", "text": "= (Equal)"}, {"label": "C", "text": "@ (At rate)"}, {"label": "D", "text": "+ (Plus)"}],
            "answer": "B",
            "explanation": "Excel interprets an entry as a formula only if it begins with an equals sign ('=')."
        },
        {
            "id": "P1-T1-CL-117", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "In Microsoft Excel, how is an Absolute Cell Reference denoted to prevent cell coordinates from changing during formula autofill?",
            "text_alt": "ಎಂಎಸ್ ಎಕ್ಸೆಲ್‌ನಲ್ಲಿ ಸೂತ್ರವನ್ನು ಕಾಪಿ ಮಾಡುವಾಗ ಕೋಶದ ವಿಳಾಸ ಬದಲಾಗದಂತೆ ನಿಶ್ಚಿತಗೊಳಿಸಲು (Absolute Cell Reference) ಯಾವ ಚಿಹ್ನೆಯನ್ನು ಬಳಸಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "$A$1"}, {"label": "B", "text": "#A#1"}, {"label": "C", "text": "&A&1"}, {"label": "D", "text": "*A*1"}],
            "answer": "A",
            "explanation": "The dollar sign '$' locks the column and row (e.g., `$A$1` keeps both column A and row 1 absolute when copied)."
        },
        {
            "id": "P1-T1-CL-118", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which function key is pressed in Microsoft PowerPoint to launch the full-screen Slide Show from the beginning?",
            "text_alt": "ಎಂಎಸ್ ಪವರ್‌ಪಾಯಿಂಟ್‌ನಲ್ಲಿ ಮೊದಲ ಸ್ಲೈಡ್‌ನಿಂದ ಸ್ಲೈಡ್ ಶೋ ಪ್ರಾರಂಭಿಸಲು ಬಳಸುವ ಫಂಕ್ಷನ್ ಕೀ ಯಾವುದು?",
            "options": [{"label": "A", "text": "F2"}, {"label": "B", "text": "F5"}, {"label": "C", "text": "F7"}, {"label": "D", "text": "F11"}],
            "answer": "B",
            "explanation": "F5 starts the presentation from Slide 1; Shift + F5 starts from the currently active slide."
        },
        {
            "id": "P1-T1-CL-119", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.3",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "Which standardized Kannada software and font engine was officially adopted and distributed by the Government of Karnataka?",
            "text_alt": "ಕರ್ನಾಟಕ ಸರ್ಕಾರವು ಅಧಿಕೃತವಾಗಿ ಅಂಗೀಕರಿಸಿ ವಿತರಿಸಿದ ಪ್ರಮಾಣಿತ ಕನ್ನಡ ತಂತ್ರಾಂಶ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Nudi (ನುಡಿ)"}, {"label": "B", "text": "Baraha (ಬರಹ)"}, {"label": "C", "text": "Shreelipi"}, {"label": "D", "text": "Prakrut"}],
            "answer": "A",
            "explanation": "Nudi was developed by the Kannada Ganaka Parishat and officially adopted by the Government of Karnataka for administrative Kannada word processing."
        },
        {
            "id": "P1-T1-CL-120", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.3",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "What is the standard keyboard toggle shortcut used in Nudi software to switch between English and Kannada typing mode?",
            "text_alt": "ನುಡಿ ತಂತ್ರಾಂಶದಲ್ಲಿ ಇಂಗ್ಲಿಷ್ ಮತ್ತು ಕನ್ನಡ ಟೈಪಿಂಗ್ ನಡುವೆ ಬದಲಾಯಿಸಲು ಬಳಸುವ ಕೀಲಿ ಶಾರ್ಟ್‌ಕಟ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "F12"}, {"label": "B", "text": "Scroll Lock"}, {"label": "C", "text": "Caps Lock"}, {"label": "D", "text": "Shift + Alt"}],
            "answer": "B",
            "explanation": "In standard Nudi direct typing mode, pressing 'Scroll Lock' toggles Kannada phonetic typing on and off."
        },
        {
            "id": "P1-T1-CL-121", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "How many bits constitute a single Byte in modern digital computing?",
            "text_alt": "ಡಿಜಿಟಲ್ ಗಣಕಯಂತ್ರದಲ್ಲಿ ಒಂದು ಬೈಟ್ (Byte) ಎಷ್ಟು ಬಿಟ್‌ಗಳಿಗೆ (Bits) ಸಮನಾಗಿರುತ್ತದೆ?",
            "options": [{"label": "A", "text": "4 Bits (Nibble)"}, {"label": "B", "text": "8 Bits"}, {"label": "C", "text": "16 Bits"}, {"label": "D", "text": "32 Bits"}],
            "answer": "B",
            "explanation": "8 bits make 1 byte. 4 bits make 1 nibble."
        },
        {
            "id": "P1-T1-CL-122", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which of the following is an open-source, multi-user, multitasking operating system?",
            "text_alt": "ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಮುಕ್ತ ಮೂಲದ (Open Source), ಬಹು-ಬಳಕೆದಾರ ಆಪರೇಟಿಂಗ್ ಸಿಸ್ಟಂ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Microsoft Windows 11"}, {"label": "B", "text": "Linux (Ubuntu / Debian)"}, {"label": "C", "text": "macOS Sonoma"}, {"label": "D", "text": "MS-DOS"}],
            "answer": "B",
            "explanation": "Linux is a free and open-source operating system kernel created by Linus Torvalds."
        },
        {
            "id": "P1-T1-CL-123", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "What does the 'S' stand for in the secure web address protocol 'HTTPS'?",
            "text_alt": "ವೆಬ್ ವಿಳಾಸದಲ್ಲಿರುವ 'HTTPS' ನಲ್ಲಿ 'S' ಅಕ್ಷರದ ಅರ್ಥವೇನು?",
            "options": [{"label": "A", "text": "Server"}, {"label": "B", "text": "Secure (SSL/TLS Encrypted)"}, {"label": "C", "text": "System"}, {"label": "D", "text": "Standard"}],
            "answer": "B",
            "explanation": "HTTPS stands for HyperText Transfer Protocol Secure, encrypting transmission via Transport Layer Security (TLS)."
        },
        {
            "id": "P1-T1-CL-124", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "The fraudulent practice of sending deceptive emails purporting to be from reputable banks to steal user credentials is known as:",
            "text_alt": "ಬ್ಯಾಂಕುಗಳ ಹೆಸರಿನಲ್ಲಿ ನಕಲಿ ಇಮೇಲ್‌ಗಳನ್ನು ಕಳುಹಿಸಿ ಬಳಕೆದಾರರ ಪಾಸ್‌ವರ್ಡ್ ಕದಿಯುವ ಸೈಬರ್ ವಂಚನೆಯನ್ನು ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "options": [{"label": "A", "text": "Phishing"}, {"label": "B", "text": "Spamming"}, {"label": "C", "text": "Sniffing"}, {"label": "D", "text": "DDoS Attack"}],
            "answer": "A",
            "explanation": "Phishing is a social engineering cyberattack designed to trick users into disclosing sensitive information."
        },
        {
            "id": "P1-T1-CL-125", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Malicious software that encrypts a victim\'s files and demands payment in cryptocurrency to restore access is termed:",
            "text_alt": "ಬಳಕೆದಾರರ ಕಂಪ್ಯೂಟರ್ ಫೈಲ್‌ಗಳನ್ನು ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಿ ಲಾಕ್ ಮಾಡಿ ಹಣಕ್ಕಾಗಿ ಒತ್ತಾಯಿಸುವ ಮಾಲ್‌ವೇರ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Adware"}, {"label": "B", "text": "Ransomware"}, {"label": "C", "text": "Spyware"}, {"label": "D", "text": "Worm"}],
            "answer": "B",
            "explanation": "Ransomware (such as WannaCry) extorts payments by holding user data hostage under encryption."
        },
        {
            "id": "P1-T1-CL-126", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "What is the primary function of an input device?",
            "text_alt": "ಇನ್‌ಪುಟ್ ಸಾಧನದ ಮುಖ್ಯ ಕಾರ್ಯವೇನು?",
            "options": [{"label": "A", "text": "To feed raw data and instructions into the computer system"}, {"label": "B", "text": "To print processed output on paper"}, {"label": "C", "text": "To compute mathematical calculations"}, {"label": "D", "text": "To store archival files permanently"}],
            "answer": "A",
            "explanation": "Input devices (keyboard, mouse, scanner, microphone) convert external data into digital signals readable by the CPU."
        },
        {
            "id": "P1-T1-CL-127", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "Which keyboard shortcut is used in Microsoft Windows to undo the most recent action?",
            "text_alt": "ವಿಂಡೋಸ್‌ನಲ್ಲಿ ಕೊನೆಯದಾಗಿ ಮಾಡಿದ ಕ್ರಿಯೆಯನ್ನು ರದ್ದುಗೊಳಿಸಲು (Undo) ಬಳಸುವ ಶಾರ್ಟ್‌ಕಟ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Ctrl + Y"}, {"label": "B", "text": "Ctrl + Z"}, {"label": "C", "text": "Ctrl + U"}, {"label": "D", "text": "Ctrl + W"}],
            "answer": "B",
            "explanation": "Ctrl + Z undoes the previous action; Ctrl + Y redoes it."
        },
        {
            "id": "P1-T1-CL-128", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "What is the purpose of the Domain Name System (DNS) on the internet?",
            "text_alt": "ಅಂತರ್ಜಾಲದಲ್ಲಿ ಡೊಮೇನ್ ನೇಮ್ ಸಿಸ್ಟಮ್‌ನ (DNS) ಮುಖ್ಯ ಕಾರ್ಯವೇನು?",
            "options": [{"label": "A", "text": "Translating human-readable domain names (like www.google.com) into numerical IP addresses"}, {"label": "B", "text": "Formatting HTML web pages"}, {"label": "C", "text": "Encrypting credit card transactions"}, {"label": "D", "text": "Regulating computer clock speed"}],
            "answer": "A",
            "explanation": "DNS acts as the phonebook of the internet, mapping hostnames to IP addresses."
        },
        {
            "id": "P1-T1-CL-129", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Which Indian Act enacted in 2000 provides the legal framework for electronic governance, digital signatures, and cybercrimes?",
            "text_alt": "ಭಾರತದಲ್ಲಿ ಸೈಬರ್ ಅಪರಾಧಗಳು ಮತ್ತು ಡಿಜಿಟಲ್ ಸಹಿಗಳಿಗೆ ಕಾನೂನು ಚೌಕಟ್ಟು ಒದಗಿಸುವ 2000 ರ ಕಾಯ್ದೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Information Technology (IT) Act, 2000"}, {"label": "B", "text": "Indian Cyber Security Act, 2000"}, {"label": "C", "text": "Digital Communication Act, 2000"}, {"label": "D", "text": "Electronic Commerce Act, 2000"}],
            "answer": "A",
            "explanation": "The Information Technology Act, 2000 (amended in 2008) is the primary law in India dealing with cybercrime and electronic commerce."
        },
        {
            "id": "P1-T1-CL-130", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "In Microsoft PowerPoint, what is the term used to describe the visual effect that occurs when one slide moves to the next during a slide show?",
            "text_alt": "ಎಂಎಸ್ ಪವರ್‌ಪಾಯಿಂಟ್‌ನಲ್ಲಿ ಒಂದು ಸ್ಲೈಡ್‌ನಿಂದ ಇನ್ನೊಂದು ಸ್ಲೈಡ್‌ಗೆ ಚಲಿಸುವಾಗ ಉಂಟಾಗುವ ದೃಶ್ಯ ಪರಿಣಾಮವನ್ನು ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "options": [{"label": "A", "text": "Custom Animation"}, {"label": "B", "text": "Slide Transition"}, {"label": "C", "text": "Slide Sorter"}, {"label": "D", "text": "Trigger Effect"}],
            "answer": "B",
            "explanation": "Transitions control the motion between slides; Animations control motion of individual elements on a slide."
        }
    ]
    qs.extend(comp)

    # ----------------------------------------------------
    # SECTION 7: HEALTH EDUCATION (10 QUESTIONS: Q131 to Q140)
    # ----------------------------------------------------
    health = [
        {
            "id": "P1-T1-HE-131", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "easy",
            "text": "The deficiency of Vitamin C in human diet causes which of the following diseases?",
            "text_alt": "ಮಾನವನ ಆಹಾರದಲ್ಲಿ 'ಸಿ' ವಿಟಮಿನ್ ಕೊರತೆಯಿಂದ ಉಂಟಾಗುವ ಕಾಯಿಲೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Beriberi"}, {"label": "B", "text": "Scurvy (ರಕ್ತಪಿತ್ತ)"}, {"label": "C", "text": "Rickets"}, {"label": "D", "text": "Night Blindness"}],
            "answer": "B",
            "explanation": "Vitamin C (ascorbic acid) deficiency causes Scurvy, leading to bleeding gums and skin spots."
        },
        {
            "id": "P1-T1-HE-132", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "easy",
            "text": "Night blindness (Nyctalopia) and Xerophthalmia are caused by the nutritional deficiency of:",
            "text_alt": "ಇರುಳುಗಣ್ಣು ರೋಗವು ಯಾವ ಜೀವಸತ್ವದ ಕೊರತೆಯಿಂದ ಉಂಟಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Vitamin A"}, {"label": "B", "text": "Vitamin B1"}, {"label": "C", "text": "Vitamin D"}, {"label": "D", "text": "Vitamin K"}],
            "answer": "A",
            "explanation": "Vitamin A (Retinol) is essential for rhodopsin synthesis in the retina; its deficiency causes night blindness."
        },
        {
            "id": "P1-T1-HE-133", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Severe protein deficiency in infants and young children results in which clinical nutritional disorder characterized by swollen belly and edema?",
            "text_alt": "ಚಿಕ್ಕ ಮಕ್ಕಳಲ್ಲಿ ಪ್ರೋಟೀನ್ ಕೊರತೆಯಿಂದ ಉಂಟಾಗುವ, ಊದಿಕೊಂಡ ಹೊಟ್ಟೆ ಲಕ್ಷಣವಿರುವ ಪೌಷ್ಟಿಕಾಂಶದ ಕಾಯಿಲೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Kwashiorkor"}, {"label": "B", "text": "Marasmus"}, {"label": "C", "text": "Anemia"}, {"label": "D", "text": "Pellagra"}],
            "answer": "A",
            "explanation": "Kwashiorkor is caused by severe protein deficiency; Marasmus is caused by total calorie and protein starvation."
        },
        {
            "id": "P1-T1-HE-134", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "Which mineral is essential for the synthesis of thyroid hormones (Thyroxine), the deficiency of which causes Goitre?",
            "text_alt": "ಥೈರಾಯ್ಡ್ ಹಾರ್ಮೋನ್ ಉತ್ಪಾದನೆಗೆ ಅತ್ಯಗತ್ಯವಾದ, ಕೊರತೆಯಿಂದ ಗಳಗಂಡ ರೋಗಕ್ಕೆ ಕಾರಣವಾಗುವ ಖನಿಜ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Iron"}, {"label": "B", "text": "Calcium"}, {"label": "C", "text": "Iodine"}, {"label": "D", "text": "Phosphorus"}],
            "answer": "C",
            "explanation": "Iodine is critical for thyroxine hormone synthesis in the thyroid gland; deficiency causes simple goitre."
        },
        {
            "id": "P1-T1-HE-135", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which of the following is a waterborne bacterial disease transmitted through contaminated food and drinking water?",
            "text_alt": "ಕಲುಷಿತ ನೀರು ಮತ್ತು ಆಹಾರದಿಂದ ಹರಡುವ ಬ್ಯಾಕ್ಟೀರಿಯಾ ರೋಗ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Malaria"}, {"label": "B", "text": "Cholera (ಕಾಲೆರಾ)"}, {"label": "C", "text": "Dengue"}, {"label": "D", "text": "Tuberculosis"}],
            "answer": "B",
            "explanation": "Cholera is caused by the bacterium Vibrio cholerae and spreads through contaminated water."
        },
        {
            "id": "P1-T1-HE-136", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.2",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Malaria is caused by the protozoan parasite Plasmodium and is transmitted to humans by the bite of:",
            "text_alt": "ಮಲೇರಿಯಾ ರೋಗವನ್ನು ಹರಡುವ ಸೊಳ್ಳೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Female Anopheles mosquito"}, {"label": "B", "text": "Female Aedes aegypti mosquito"}, {"label": "C", "text": "Culex mosquito"}, {"label": "D", "text": "Tsetse fly"}],
            "answer": "A",
            "explanation": "Female Anopheles mosquitoes transmit Plasmodium parasites causing malaria."
        },
        {
            "id": "P1-T1-HE-137", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.3",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "What does the first-aid acronym 'R.I.C.E.' stand for in the immediate management of acute soft-tissue sprains and muscle strains?",
            "text_alt": "ಸ್ನಾಯು ಉಳುಕುಗಳಿಗೆ ಪ್ರಥಮ ಚಿಕಿತ್ಸೆಯಲ್ಲಿ 'R.I.C.E.' ನ ವಿಸ್ತೃತ ರೂಪವೇನು?",
            "options": [{"label": "A", "text": "Rest, Ice, Compression, Elevation"}, {"label": "B", "text": "Run, Incline, Cool, Exercise"}, {"label": "C", "text": "Relief, Immobilize, Clean, Examine"}, {"label": "D", "text": "Respiration, Injection, Care, Energy"}],
            "answer": "A",
            "explanation": "RICE protocol: Rest the injured limb, Ice application, Compression bandage, and Elevation above heart level."
        },
        {
            "id": "P1-T1-HE-138", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.3",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "In Cardiopulmonary Resuscitation (CPR) guidelines for an adult in cardiac arrest, what is the recommended ratio of chest compressions to rescue breaths?",
            "text_alt": "ವಯಸ್ಕರ ಸಿಪಿಆರ್ (CPR) ನಲ್ಲಿ ಎದೆ ಒತ್ತಡ ಮತ್ತು ಕೃತಕ ಉಸಿರಾಟದ ಶಿಫಾರಸು ಮಾಡಲಾದ ಅನುಪಾತ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "15 compressions to 2 breaths"}, {"label": "B", "text": "30 compressions to 2 breaths"}, {"label": "C", "text": "50 compressions to 5 breaths"}, {"label": "D", "text": "10 compressions to 1 breath"}],
            "answer": "B",
            "explanation": "Standard AHA CPR guidelines recommend 30 chest compressions followed by 2 rescue breaths (30:2 ratio)."
        },
        {
            "id": "P1-T1-HE-139", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.3",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "On which date is International Yoga Day celebrated globally every year?",
            "text_alt": "ಅಂತರರಾಷ್ಟ್ರೀಯ ಯೋಗ ದಿನವನ್ನು ಪ್ರತಿವರ್ಷ ಯಾವ ದಿನಾಂಕದಂದು ಆಚರಿಸಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "5 June"}, {"label": "B", "text": "21 June"}, {"label": "C", "text": "15 August"}, {"label": "D", "text": "7 April"}],
            "answer": "B",
            "explanation": "The United Nations General Assembly declared 21 June as International Day of Yoga in 2014."
        },
        {
            "id": "P1-T1-HE-140", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which component of food acts as the primary immediate source of energy for the human body during cellular respiration?",
            "text_alt": "ಮಾನವ ದೇಹಕ್ಕೆ ತಕ್ಷಣದ ಶಕ್ತಿ ಒದಗಿಸುವ ಮುಖ್ಯ ಪೋಷಕಾಂಶ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Carbohydrates (ಗ್ಲುಕೋಸ್)"}, {"label": "B", "text": "Proteins"}, {"label": "C", "text": "Vitamins"}, {"label": "D", "text": "Minerals"}],
            "answer": "A",
            "explanation": "Carbohydrates are broken down into glucose, the primary cellular fuel producing ATP energy."
        }
    ]
    qs.extend(health)

    # ----------------------------------------------------
    # SECTION 8: VALUE EDUCATION (10 QUESTIONS: Q141 to Q150)
    # ----------------------------------------------------
    val = [
        {
            "id": "P1-T1-VE-141", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "In Lawrence Kohlberg\'s Theory of Moral Development, an individual who obeys rules solely to avoid physical punishment is operating at:",
            "text_alt": "ಲಾರೆನ್ಸ್ ಕೋಲ್ಬರ್ಗ್ ಅವರ ಪ್ರಕಾರ, ಕೇವಲ ದೈಹಿಕ ಶಿಕ್ಷೆಯಿಂದ ತಪ್ಪಿಸಿಕೊಳ್ಳಲು ನಿಯಮಗಳನ್ನು ಪಾಲಿಸುವ ವ್ಯಕ್ತಿಯ ನೈತಿಕ ಹಂತ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Stage 1: Punishment and Obedience Orientation (Pre-Conventional Level)"}, {"label": "B", "text": "Stage 3: Good Boy / Nice Girl Orientation"}, {"label": "C", "text": "Stage 4: Law and Order Orientation"}, {"label": "D", "text": "Stage 5: Social Contract Orientation"}],
            "answer": "A",
            "explanation": "Stage 1 of the Pre-Conventional level evaluates morality strictly by physical consequences: obedience to authority to escape punishment."
        },
        {
            "id": "P1-T1-VE-142", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "PYQ - GPSTR 2019", "difficulty": "medium",
            "text": "Which moral dilemma was famously used by Lawrence Kohlberg in his interviews to assess the moral reasoning of adolescents?",
            "text_alt": "ಕೋಲ್ಬರ್ಗ್ ತನ್ನ ಸಂಶೋಧನೆಯಲ್ಲಿ ನೈತಿಕ ತೀರ್ಮಾನಗಳನ್ನು ಪರೀಕ್ಷಿಸಲು ಬಳಸಿದ ಪ್ರಸಿದ್ಧ ನೈತಿಕ ಸಂದಿಗ್ಧತೆ (Dilemma) ಯಾವುದು?",
            "options": [{"label": "A", "text": "The Heinz Dilemma (stealing drug to save dying wife)"}, {"label": "B", "text": "The Trolley Problem"}, {"label": "C", "text": "The Prisoner\'s Dilemma"}, {"label": "D", "text": "The Ship of Theseus"}],
            "answer": "A",
            "explanation": "The Heinz Dilemma asks whether a man named Heinz should steal an overpriced drug to save his dying wife."
        },
        {
            "id": "P1-T1-VE-143", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "According to Jean Piaget\'s Theory of Moral Development, what characterizes the stage of 'Heteronomous Morality' (Moral Realism, ages 4–7)?",
            "text_alt": "ಜೀನ್ ಪಿಯಾಜೆ ಅವರ ಪ್ರಕಾರ 'ಪರಾಯತ್ತ ನೈತಿಕತೆ'ಯ (Heteronomous Morality) ಪ್ರಮುಖ ಲಕ್ಷಣವೇನು?",
            "options": [{"label": "A", "text": "Rules are social agreements that can be altered by mutual consensus"}, {"label": "B", "text": "Rules are sacred, immutable decrees of God/adults, and belief in Immanent Justice"}, {"label": "C", "text": "Moral decisions are based on abstract ethical justice principles"}, {"label": "D", "text": "Complete rejection of all authority figures"}],
            "answer": "B",
            "explanation": "Heteronomous morality views rules as unalterable absolutes handed down by authority, accompanied by belief in immanent justice."
        },
        {
            "id": "P1-T1-VE-144", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Carol Gilligan critiqued Kohlberg\'s moral development model as male-biased and proposed that women\'s moral reasoning centers on an:",
            "text_alt": "ಕೋಲ್ಬರ್ಗ್ ಸಿದ್ಧಾಂತವನ್ನು ವಿಮರ್ಶಿಸಿದ ಕ್ಯಾರೋಲ್ ಗಿಲ್ಲಿಗನ್, ಮಹಿಳೆಯರ ನೈತಿಕತೆಯು ಯಾವುದರ ಮೇಲೆ ಆಧಾರಿತವಾಗಿದೆ ಎಂದು ಪ್ರತಿಪಾದಿಸಿದರು?",
            "options": [{"label": "A", "text": "Ethic of Justice"}, {"label": "B", "text": "Ethic of Care, Relationships, and Responsibility"}, {"label": "C", "text": "Ethic of Strict Compliance"}, {"label": "D", "text": "Ethic of Intellectual Supremacy"}],
            "answer": "B",
            "explanation": "In 'In a Different Voice' (1982), Gilligan showed that women prioritize care, empathy, and maintaining human connections over abstract rules of justice."
        },
        {
            "id": "P1-T1-VE-145", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "PYQ - GPSTR 2022", "difficulty": "medium",
            "text": "Under Section 17 of the Right to Education (RTE) Act, 2009, which of the following is STRICTLY prohibited in all Indian schools?",
            "text_alt": "ಶಿಕ್ಷಣ ಹಕ್ಕು ಕಾಯ್ದೆ 2009 ರ ಕಲಂ 17 ರ ಅಡಿಯಲ್ಲಿ ಶಾಲೆಗಳಲ್ಲಿ ಕಟ್ಟುನಿಟ್ಟಾಗಿ ನಿಷೇಧಿಸಲಾಗಿರುವುದು ಯಾವುದು?",
            "options": [{"label": "A", "text": "Conducting monthly unit tests"}, {"label": "B", "text": "Inflicting physical punishment or mental harassment on children"}, {"label": "C", "text": "Assigning weekend homework"}, {"label": "D", "text": "Parent-teacher consultations"}],
            "answer": "B",
            "explanation": "Section 17 bans physical punishment and mental harassment, making violators subject to disciplinary action."
        },
        {
            "id": "P1-T1-VE-146", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "difficulty": "hard",
            "text": "Under Section 19 of the Protection of Children from Sexual Offences (POCSO) Act, 2012, what is the mandatory legal duty of a school teacher who gains knowledge of sexual abuse of a student?",
            "text_alt": "ಪೋಕ್ಸೊ (POCSO) ಕಾಯ್ದೆ 2012 ರ ಕಲಂ 19 ರ ಪ್ರಕಾರ ಶಾಲಾ ಶಿಕ್ಷಕರಿಗೆ ಇರುವ ಕಡ್ಡಾಯ ಕರ್ತವ್ಯ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Must report the offence immediately to the Special Juvenile Police Unit (SJPU) or local police"}, {"label": "B", "text": "Settle the dispute quietly with the student\'s family"}, {"label": "C", "text": "Wait for final annual school examination results"}, {"label": "D", "text": "Dismiss the student from the school rolls"}],
            "answer": "A",
            "explanation": "Section 19 makes reporting mandatory; Section 21 penalizes failure to report with imprisonment up to one year."
        },
        {
            "id": "P1-T1-VE-147", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "According to the NCTE Code of Professional Ethics for School Teachers, which of the following practices is considered UNETHICAL?",
            "text_alt": "ಎನ್‌ಸಿಟಿಇ (NCTE) ಶಿಕ್ಷಕರ ವೃತ್ತಿಪರ ನೀತಿ ಸಂಹಿತೆಯ ಪ್ರಕಾರ ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಅನೈತಿಕ ನಡವಳಿಕೆ?",
            "options": [{"label": "A", "text": "Treating students of all communities with equality and dignity"}, {"label": "B", "text": "Engaging in private paid tuition for enrolled students for personal commercial gain"}, {"label": "C", "text": "Participating in continuous teacher training programs"}, {"label": "D", "text": "Maintaining cordial relations with parents"}],
            "answer": "B",
            "explanation": "The NCTE code explicitly bars teachers from undertaking commercial private coaching or soliciting monetary benefits from students."
        },
        {
            "id": "P1-T1-VE-148", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Which Fundamental Duty under Article 51A of the Constitution of India enjoins citizens to develop the 'scientific temper, humanism, and the spirit of inquiry and reform'?",
            "text_alt": "'ವೈಜ್ಞಾನಿಕ ಮನೋಭಾವ, ಮಾನವೀಯತೆ ಮತ್ತು ಸುಧಾರಣಾ ಮನೋಭಾವ'ವನ್ನು ಬೆಳೆಸಿಕೊಳ್ಳುವುದು ಭಾರತೀಯ ಸಂವಿಧಾನದ ಯಾವ ವಿಧಿಯ ಅಡಿಯಲ್ಲಿ ಮೂಲಭೂತ ಕರ್ತವ್ಯವಾಗಿದೆ?",
            "options": [{"label": "A", "text": "Article 51A(a)"}, {"label": "B", "text": "Article 51A(e)"}, {"label": "C", "text": "Article 51A(h)"}, {"label": "D", "text": "Article 51A(k)"}],
            "answer": "C",
            "explanation": "Article 51A(h) directs every Indian citizen to develop the scientific temper, humanism, and the spirit of inquiry and reform."
        },
        {
            "id": "P1-T1-VE-149", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "difficulty": "medium",
            "text": "Inculcating moral and social values through regular school subjects (history, literature, science) and school assemblies rather than separate lectures is called the:",
            "text_alt": "ಪ್ರತ್ಯೇಕ ಬೋಧನೆಯ ಬದಲು ನಿಯಮಿತ ಪಠ್ಯವಿಷಯಗಳು ಮತ್ತು ಪ್ರಾರ್ಥನಾ ಸಭೆಗಳ ಮೂಲಕ ಮೌಲ್ಯಗಳನ್ನು ಕಲಿಸುವ ವಿಧಾನವನ್ನು ಏನೆಂದು ಕರೆಯುತ್ತಾರೆ?",
            "options": [{"label": "A", "text": "Direct Approach"}, {"label": "B", "text": "Indirect / Integrated Approach (ಸಂಯೋಜಿತ ವಿಧಾನ)"}, {"label": "C", "text": "Rote Memorization Method"}, {"label": "D", "text": "Punitive Approach"}],
            "answer": "B",
            "explanation": "The Integrated (Indirect) Approach infuses values seamlessly across existing curricula, co-curricular activities, and the hidden curriculum."
        },
        {
            "id": "P1-T1-VE-150", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "difficulty": "easy",
            "text": "Which four core values are solemnized in the Preamble to the Constitution of India?",
            "text_alt": "ಭಾರತೀಯ ಸಂವಿಧಾನದ ಪ್ರಸ್ತಾವನೆಯಲ್ಲಿ ಪ್ರತಿಪಾದಿಸಲಾದ ನಾಲ್ಕು ಆದರ್ಶ ಮೌಲ್ಯಗಳು ಯಾವುವು?",
            "options": [{"label": "A", "text": "Justice, Liberty, Equality, Fraternity (ನ್ಯಾಯ, ಸ್ವಾತಂತ್ರ್ಯ, ಸಮಾನತೆ, ಭ್ರಾತೃತ್ವ)"}, {"label": "B", "text": "Monarchy, Autocracy, Religion, Wealth"}, {"label": "C", "text": "Power, Territory, Defense, Industry"}, {"label": "D", "text": "Competition, Capitalism, Profit, Hierarchy"}],
            "answer": "A",
            "explanation": "The Preamble secures to all citizens: JUSTICE (Social, Economic, Political), LIBERTY, EQUALITY, and FRATERNITY."
        }
    ]
    qs.extend(val)

    return qs

