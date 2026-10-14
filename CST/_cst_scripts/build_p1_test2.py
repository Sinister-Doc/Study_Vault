# -*- coding: utf-8 -*-
"""
Generate complete 150 distinct, syllabus-locked, authentic questions for Paper 1 Test 2.
Sections:
S1: 20 GK (Q1 to Q20)
S2: 15 CA (Q21 to Q35)
S3: 25 Kannada (Q36 to Q60)
S4: 25 English (Q61 to Q85)
S5: 25 Educational Psychology (Q86 to Q110)
S6: 20 Computer Literacy (Q111 to Q130)
S7: 10 Health Education (Q131 to Q140)
S8: 10 Value Education (Q141 to Q150)
Total = 150 Questions.
"""

def get_paper1_test2_questions():
    qs = []

    # ----------------------------------------------------
    # SECTION 1: GENERAL KNOWLEDGE (20 QUESTIONS: Q1 to Q20)
    # ----------------------------------------------------
    gk = [
        {
            "id": "P1-T2-GK-01", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "The magnificent monolithic rock-cut Kailasanatha temple at Ellora (Cave 16) was excavated during the reign of which Rashtrakuta monarch?",
            "text_alt": "ಎಲ್ಲೋರಾದ ಭವ್ಯ ಏಕಶಿಲಾ ಕೈಲಾಸನಾಥ ದೇವಾಲಯವನ್ನು (ಗುಹೆ 16) ಯಾವ ರಾಷ್ಟ್ರಕೂಟ ದೊರೆಯ ಆಳ್ವಿಕೆಯಲ್ಲಿ ನಿರ್ಮಿಸಲಾಯಿತು?",
            "options": [{"label": "A", "text": "Dantidurga"}, {"label": "B", "text": "Krishna I"}, {"label": "C", "text": "Dhruva Dharavarsha"}, {"label": "D", "text": "Govinda III"}],
            "answer": "B",
            "explanation": "Rashtrakuta king Krishna I (756–774 CE) commissioned the monolithic rock-cut Kailasa temple at Ellora, carved top-to-bottom from a single basalt cliff."
        },
        {
            "id": "P1-T2-GK-02", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which ancient capital city was founded by Pulakeshin I as the seat of the Early Chalukya dynasty in 543 CE?",
            "text_alt": "ಕ್ರಿ.ಶ. 543 ರಲ್ಲಿ ಆರಂಭಿಕ ಚಾಲುಕ್ಯ ರಾಜವಂಶದ ರಾಜಧಾನಿಯಾಗಿ ಒಂದನೇ ಪುಲಕೇಶಿ ಸ್ಥಾಪಿಸಿದ ಐತಿಹಾಸಿಕ ನಗರ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Vatapi (Badami)"}, {"label": "B", "text": "Kalyana"}, {"label": "C", "text": "Aihole"}, {"label": "D", "text": "Pattadakal"}],
            "answer": "A",
            "explanation": "Pulakeshin I established his capital at Vatapi (modern Badami in Bagalkote district) and performed the Ashvamedha sacrifice to assert sovereign power."
        },
        {
            "id": "P1-T2-GK-03", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "medium",
            "text": "The world-famous 57-foot monolithic statue of Lord Gommateshwara (Bahubali) at Shravanabelagola was consecrated in 981 CE by which Western Ganga prime minister?",
            "text_alt": "ಶ್ರವಣಬೆಳಗೊಳದ ಪ್ರಸಿದ್ಧ 57 ಅಡಿ ಎತ್ತರದ ಗೊಮ್ಮಟೇಶ್ವರ ಏಕಶಿಲಾ ವಿಗ್ರಹವನ್ನು ಕ್ರಿ.ಶ. 981 ರಲ್ಲಿ ಕೆತ್ತಿಸಿ ಪ್ರತಿಷ್ಠಾಪಿಸಿದ ಪಶ್ಚಿಮ ಗಂಗರ ಮಂತ್ರಿ ಯಾರು?",
            "options": [{"label": "A", "text": "Chavundaraya"}, {"label": "B", "text": "Marasimha II"}, {"label": "C", "text": "Durvinita"}, {"label": "D", "text": "Madhavavarma"}],
            "answer": "A",
            "explanation": "Chavundaraya, military commander and prime minister to Ganga king Rachamalla IV, consecrated the Gommateshwara colossus atop Vindhyagiri hill in 981 CE."
        },
        {
            "id": "P1-T2-GK-04", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "The twin-temple Hoysaleshwara temple at Halebidu, famous for its intricate soapstone relief friezes, was dedicated to Lord Shiva during the reign of which king?",
            "text_alt": "ಸೋಪಸ್ಟೋನ್ ಶಿಲ್ಪಕಲೆಗೆ ಹೆಸರಾದ ಹಳೇಬೀಡಿನ ಹೊಯ್ಸಳೇಶ್ವರ ಜೋಡಿ ದೇವಾಲಯವನ್ನು ಯಾವ ರಾಜನ ಆಳ್ವಿಕೆಯಲ್ಲಿ ನಿರ್ಮಿಸಲಾಯಿತು?",
            "options": [{"label": "A", "text": "King Vishnuvardhana"}, {"label": "B", "text": "Veera Ballala II"}, {"label": "C", "text": "Narasimha III"}, {"label": "D", "text": "Somesvara"}],
            "answer": "A",
            "explanation": "The Hoysaleshwara temple at Halebidu (Dorasamudra) was initiated under King Vishnuvardhana around 1121 CE by his noble Ketamalla and chief architect Kedaroja."
        },
        {
            "id": "P1-T2-GK-05", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "medium",
            "text": "The Vijayanagara monarch Krishnadevaraya authored which classical political treatise in Telugu describing statecraft and kingly duties?",
            "text_alt": "ವಿಜಯನಗರದ ಸಾರ್ವಭೌಮ ಶ್ರೀ ಕೃಷ್ಣದೇವರಾಯರು ರಾಜಧರ್ಮ ಮತ್ತು ಆಡಳಿತವನ್ನು ವಿವರಿಸುವ ಯಾವ ಪ್ರಸಿದ್ಧ ತೆಲುಗು ಕೃತಿಯನ್ನು ರಚಿಸಿದರು?",
            "options": [{"label": "A", "text": "Amuktamalyada"}, {"label": "B", "text": "Jambavati Kalyanam"}, {"label": "C", "text": "Usha Parinayam"}, {"label": "D", "text": "Madura Vijayam"}],
            "answer": "A",
            "explanation": "Krishnadevaraya authored 'Amuktamalyada' in Telugu celebrating Andal's life and detailing statecraft, while his Sanskrit works include 'Jambavati Kalyanam'."
        },
        {
            "id": "P1-T2-GK-06", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Gol Gumbaz in Vijayapura, famous for its unsupported dome and acoustical Whispering Gallery, is the mausoleum of which Adil Shahi sultan?",
            "text_alt": "ಪ್ರಪಂಚದ ಎರಡನೇ ಅತಿ ದೊಡ್ಡ ಗುಮ್ಮಟ ಹಾಗೂ ಪ್ರತಿಧ್ವನಿ ದ್ವಾರ ಹೊಂದಿರುವ ವಿಜಯಪುರದ ಗೋಲ್ ಗುಂಬಜ್ ಯಾವ ಆದಿಲ್ ಶಾಹಿ ಸುಲ್ತಾನನ ಸಮಾಧಿಯಾಗಿದೆ?",
            "options": [{"label": "A", "text": "Ibrahim Adil Shah II"}, {"label": "B", "text": "Mohammed Adil Shah"}, {"label": "C", "text": "Ali Adil Shah I"}, {"label": "D", "text": "Yusuf Adil Shah"}],
            "answer": "B",
            "explanation": "Constructed in 1656 CE by master architect Yaqut of Dabul, Gol Gumbaz houses the mortal remains of Mohammed Adil Shah."
        },
        {
            "id": "P1-T2-GK-07", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "Which Mysore ruler established the royal tradition of celebrating the grand Mysore Dasara festival at Srirangapatna in 1610 CE?",
            "text_alt": "ಕ್ರಿ.ಶ. 1610 ರಲ್ಲಿ ಶ್ರೀರಂಗಪಟ್ಟಣದಲ್ಲಿ ಅದ್ಧೂರಿ ಮೈಸೂರು ದಸರಾ ಮಹೋತ್ಸವದ ಸಂಪ್ರದಾಯವನ್ನು ಆರಂಭಿಸಿದ ಮೈಸೂರಿನ ಒಡೆಯರ್ ದೊರೆ ಯಾರು?",
            "options": [{"label": "A", "text": "Raja Wodeyar I"}, {"label": "B", "text": "Ranadheera Kanteerava Narasaraja"}, {"label": "C", "text": "Chikka Devaraja Wodeyar"}, {"label": "D", "text": "Mummadi Krishnaraja Wodeyar"}],
            "answer": "A",
            "explanation": "Raja Wodeyar I seized Srirangapatna from the Vijayanagara viceroy Tirumala in 1610 and decreed that the Navaratri / Dasara festival be celebrated annually with royal grandeur."
        },
        {
            "id": "P1-T2-GK-08", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "Under the Treaty of Seringapatam (1792) that ended the Third Anglo-Mysore War, Tipu Sultan ceded which territory to the British East India Company?",
            "text_alt": "ಮೂರನೇ ಆಂಗ್ಲೋ-ಮೈಸೂರು ಯುದ್ಧವನ್ನು ಕೊನೆಗೊಳಿಸಿದ ಶ್ರೀರಂಗಪಟ್ಟಣ ಒಪ್ಪಂದದ (1792) ಅನ್ವಯ ಟಿಪ್ಪು ಸುಲ್ತಾನ್ ಬ್ರಿಟಿಷರಿಗೆ ಬಿಟ್ಟುಕೊಟ್ಟ ಪ್ರದೇಶ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Malabar, Dindigul, and Baramahal"}, {"label": "B", "text": "Raichur Doab"}, {"label": "C", "text": "Northern Circars"}, {"label": "D", "text": "Thanjavur and Madurai"}],
            "answer": "A",
            "explanation": "Lord Cornwallis forced Tipu Sultan to surrender half his kingdom (including Malabar coast, Coorg protectorate, Dindigul, and Baramahal) and pay 3 crore rupees in indemnity."
        },
        {
            "id": "P1-T2-GK-09", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "easy",
            "text": "The heroic freedom fighter Sangolli Rayanna, who continued armed guerrilla warfare after the fall of Kittur, was captured through betrayal and hanged at:",
            "text_alt": "ಕಿತ್ತೂರಿನ ಪತನದ ನಂತರವೂ ಬ್ರಿಟಿಷರ ವಿರುದ್ಧ ಗೆರಿಲ್ಲಾ ಹೋರಾಟ ಮುಂದುವರಿಸಿದ ಕ್ರಾಂತಿವೀರ ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣನನ್ನು ಎಲ್ಲಿ ಗಲ್ಲಿಗೇರಿಸಲಾಯಿತು?",
            "options": [{"label": "A", "text": "Nandagad (Belagavi)"}, {"label": "B", "text": "Khanapur"}, {"label": "C", "text": "Bailhongal"}, {"label": "D", "text": "Soundatti"}],
            "answer": "A",
            "explanation": "Sangolli Rayanna was captured by British treacherous machinations and hanged from a banyan tree at Nandagad in Belagavi district on 26 January 1831."
        },
        {
            "id": "P1-T2-GK-10", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "The armed rebellion of the Bedas of Halagali in Mudhol state against British rule in November 1857 was provoked by which oppressive legislation?",
            "text_alt": "1857 ರ ನವೆಂಬರ್‌ನಲ್ಲಿ ಮುಧೋಳ ಸಂಸ್ಥಾನದ ಹಲಗಲಿ ಬೇಡರು ಬ್ರಿಟಿಷರ ವಿರುದ್ಧ ನಡೆಸಿದ ಸಶಸ್ತ್ರ ದಂಗೆಗೆ ಕಾರಣವಾದ ಬ್ರಿಟಿಷ್ ಕಾಯ್ದೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Disarming Act of 1857"}, {"label": "B", "text": "Doctrine of Lapse"}, {"label": "C", "text": "Vernacular Press Act"}, {"label": "D", "text": "Salt Tax Regulation"}],
            "answer": "A",
            "explanation": "The Disarming Act of 1857 required all Indians to surrender their traditional weapons and firearms; the hunting martial Bedas of Halagali heroically refused and revolted."
        },
        {
            "id": "P1-T2-GK-11", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.1",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "easy",
            "text": "The unified state of Mysore was officially renamed as 'Karnataka' on 1 November 1973 under the tenure of which Chief Minister?",
            "text_alt": "ವಿಶಾಲ ಮೈಸೂರು ರಾಜ್ಯವನ್ನು 1973 ರ ನವೆಂಬರ್ 1 ರಂದು ಅಧಿಕೃತವಾಗಿ 'ಕರ್ನಾಟಕ' ಎಂದು ಮರುನಾಮಕರಣ ಮಾಡಿದ ಮುಖ್ಯಮಂತ್ರಿ ಯಾರು?",
            "options": [{"label": "A", "text": "D. Devaraj Urs"}, {"label": "B", "text": "Kengal Hanumanthaiah"}, {"label": "C", "text": "S. Nijalingappa"}, {"label": "D", "text": "B. D. Jatti"}],
            "answer": "A",
            "explanation": "Chief Minister D. Devaraj Urs spearheaded the historic legislative declaration on November 1, 1973, renaming Mysore State to Karnataka."
        },
        {
            "id": "P1-T2-GK-12", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the total coastline length of Karnataka stretching along the Arabian Sea from Karwar to Mangaluru?",
            "text_alt": "ಕಾರವಾರದಿಂದ ಮಂಗಳೂರಿನವರೆಗೆ ಅರಬ್ಬಿ ಸಮುದ್ರದ ತೀರದಲ್ಲಿ ಹರಡಿರುವ ಕರ್ನಾಟಕದ ಕರಾವಳಿ ತೀರದ ಒಟ್ಟು ಉದ್ದ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "320 kilometers"}, {"label": "B", "text": "450 kilometers"}, {"label": "C", "text": "210 kilometers"}, {"label": "D", "text": "560 kilometers"}],
            "answer": "A",
            "explanation": "Karnataka's coastal belt (Karavali / Canara) stretches approximately 320 km across three coastal districts: Uttara Kannada, Udupi, and Dakshina Kannada."
        },
        {
            "id": "P1-T2-GK-13", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which of the following is NOT a right-bank tributary of the Krishna river flowing through Karnataka?",
            "text_alt": "ಕರ್ನಾಟಕದಲ್ಲಿ ಹರಿಯುವ ಕೃಷ್ಣಾ ನದಿಯ ಬಲದಂಡೆಯ ಉಪನದಿಯಲ್ಲದ ನದಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Bhima"}, {"label": "B", "text": "Ghataprabha"}, {"label": "C", "text": "Malaprabha"}, {"label": "D", "text": "Tungabhadra"}],
            "answer": "A",
            "explanation": "Bhima is the major left-bank tributary of Krishna; Ghataprabha, Malaprabha, and Tungabhadra are right-bank tributaries."
        },
        {
            "id": "P1-T2-GK-14", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The Donimalai and Sandur hill ranges in Ballari district are world-famous for their high-grade reserves of:",
            "text_alt": "ಬಳ್ಳಾರಿ ಜಿಲ್ಲೆಯ ದೋಣಿಮಲೈ ಮತ್ತು ಸಂಡೂರು ಬೆಟ್ಟಗಳು ಯಾವ ಉತ್ತಮ ದರ್ಜೆಯ ಅದಿರಿನ ನಿಕ್ಷೇಪಗಳಿಗೆ ಪ್ರಸಿದ್ಧವಾಗಿವೆ?",
            "options": [{"label": "A", "text": "Hematite Iron Ore"}, {"label": "B", "text": "Bauxite"}, {"label": "C", "text": "Mica"}, {"label": "D", "text": "Uranium"}],
            "answer": "A",
            "explanation": "The Sandur-Hospete-Ballari mineral belt possesses abundant rich reserves of high-grade hematite iron ore (NMDC operates Donimalai iron mines)."
        },
        {
            "id": "P1-T2-GK-15", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.2",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "easy",
            "text": "Which National Park in Karnataka, situated across Mysuru and Kodagu districts, is also designated as the Rajiv Gandhi National Park?",
            "text_alt": "ಮೈಸೂರು ಮತ್ತು ಕೊಡಗು ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಹರಡಿರುವ ಹಾಗೂ ರಾಜೀವ್ ಗಾಂಧಿ ರಾಷ್ಟ್ರೀಯ ಉದ್ಯಾನವನವೆಂದು ಕರೆಯಲ್ಪಡುವ ಕರ್ನಾಟಕದ ರಾಷ್ಟ್ರೀಯ ಉದ್ಯಾನ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Nagarahole National Park"}, {"label": "B", "text": "Bandipur National Park"}, {"label": "C", "text": "Kudremukh National Park"}, {"label": "D", "text": "Anshi National Park"}],
            "answer": "A",
            "explanation": "Nagarahole National Park was renamed Rajiv Gandhi National Park in 1992 and forms a core part of the Nilgiri Biosphere Reserve."
        },
        {
            "id": "P1-T2-GK-16", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "easy",
            "text": "Which three words were added to the Preamble of the Indian Constitution by the 42nd Constitutional Amendment Act of 1976?",
            "text_alt": "1976 ರ 42 ನೇ ಸಂವಿಧಾನ ತಿದ್ದುಪಡಿ ಕಾಯ್ದೆಯ ಮೂಲಕ ಭಾರತ ಸಂವಿಧಾನದ ಪ್ರಸ್ತಾವನೆಗೆ ಸೇರಿಸಲಾದ ಮೂರು ಪದಗಳು ಯಾವುವು?",
            "options": [{"label": "A", "text": "Socialist, Secular, Integrity (ಸಮಾಜವಾದಿ, ಜಾತ್ಯತೀತ, ಸಮಗ್ರತೆ)"}, {"label": "B", "text": "Liberty, Equality, Fraternity"}, {"label": "C", "text": "Justice, Democracy, Republic"}, {"label": "D", "text": "Sovereign, Federal, Parliamentary"}],
            "answer": "A",
            "explanation": "The 42nd Amendment Act (1976) amended the Preamble to change 'Sovereign Democratic Republic' to 'Sovereign Socialist Secular Democratic Republic' and added 'and integrity'."
        },
        {
            "id": "P1-T2-GK-17", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The Supreme Court of India held that the Right to Privacy is an intrinsic part of the Right to Life and Personal Liberty under Article 21 in which landmark verdict?",
            "text_alt": "ಖಾಸಗಿತನದ ಹಕ್ಕು (Right to Privacy) 21 ನೇ ವಿಧಿಯಡಿ ಜೀವಿಸುವ ಹಕ್ಕಿನ ಮೂಲಭೂತ ಭಾಗವೆಂದು ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಯಾವ ಮಹತ್ವದ ತೀರ್ಪಿನಲ್ಲಿ ಎತ್ತಿಹಿಡಿಯಿತು?",
            "options": [{"label": "A", "text": "Justice K. S. Puttaswamy v. Union of India (2017)"}, {"label": "B", "text": "Kesavananda Bharati v. State of Kerala (1973)"}, {"label": "C", "text": "Maneka Gandhi v. Union of India (1978)"}, {"label": "D", "text": "Navtej Singh Johar v. Union of India (2018)"}],
            "answer": "A",
            "explanation": "In Justice K. S. Puttaswamy (Retd.) v. Union of India (2017), a unanimous 9-judge Constitution Bench held that Privacy is protected under Article 21 and Part III."
        },
        {
            "id": "P1-T2-GK-18", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Under Article 51A of the Indian Constitution, how many Fundamental Duties are currently enshrined for every Indian citizen?",
            "text_alt": "ಭಾರತದ ಸಂವಿಧಾನದ 51ಎ ವಿಧಿಯ ಅಡಿಯಲ್ಲಿ ಪ್ರಸ್ತುತ ಪ್ರತಿಯೊಬ್ಬ ಭಾರತೀಯ ನಾಗರಿಕನಿಗೆ ಎಷ್ಟು ಮೂಲಭೂತ ಕರ್ತವ್ಯಗಳಿವೆ?",
            "options": [{"label": "A", "text": "10"}, {"label": "B", "text": "11"}, {"label": "C", "text": "12"}, {"label": "D", "text": "9"}],
            "answer": "B",
            "explanation": "Originally 10 Fundamental Duties were added by the 42nd Amendment in 1976; the 11th duty (education for children 6-14 yrs) was added by the 86th Amendment in 2002."
        },
        {
            "id": "P1-T2-GK-19", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "Who participates in the Electoral College for the election of the President of India under Article 54?",
            "text_alt": "54 ನೇ ವಿಧಿಯ ಅನ್ವಯ ಭಾರತದ ರಾಷ್ಟ್ರಪತಿಗಳ ಚುನಾವಣೆಯಲ್ಲಿ ಮತ ಚಲಾಯಿಸುವ ಚುನಾವಣಾ ಗಣದಲ್ಲಿ (Electoral College) ಭಾಗವಹಿಸುವವರು ಯಾರು?",
            "options": [{"label": "A", "text": "Elected members of both Houses of Parliament and elected members of State Legislative Assemblies"}, {"label": "B", "text": "All members of Lok Sabha, Rajya Sabha, and Legislative Councils"}, {"label": "C", "text": "Elected members of Lok Sabha only"}, {"label": "D", "text": "Governors of all States and Union Cabinet Ministers"}],
            "answer": "A",
            "explanation": "Article 54 provides that the Electoral College consists of elected members of Lok Sabha, Rajya Sabha, and Legislative Assemblies of States, including Delhi and Puducherry."
        },
        {
            "id": "P1-T2-GK-20", "paper": 1, "section_id": "S1", "subject": "General Knowledge", "syllabus_id": "P1-1.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "The 73rd Constitutional Amendment Act of 1992 inserted which Schedule into the Indian Constitution containing 29 functional items for Panchayati Raj institutions?",
            "text_alt": "1992 ರ 73 ನೇ ಸಂವಿಧಾನ ತಿದ್ದುಪಡಿ ಕಾಯ್ದೆಯು ಪಂಚಾಯತ್ ರಾಜ್ ಸಂಸ್ಥೆಗಳಿಗೆ 29 ಕಾರ್ಯಾತ್ಮಕ ವಿಷಯಗಳನ್ನು ನೀಡುವ ಯಾವ ಅನುಸೂಚಿಯನ್ನು ಸಂವಿಧಾನಕ್ಕೆ ಸೇರಿಸಿತು?",
            "options": [{"label": "A", "text": "10th Schedule"}, {"label": "B", "text": "11th Schedule"}, {"label": "C", "text": "12th Schedule"}, {"label": "D", "text": "9th Schedule"}],
            "answer": "B",
            "explanation": "The 73rd Amendment inserted Part IX and the 11th Schedule (29 matters for Panchayats); the 74th Amendment inserted the 12th Schedule (18 matters for Municipalities)."
        }
    ]
    qs.extend(gk)

    # ----------------------------------------------------
    # SECTION 2: CURRENT AFFAIRS (15 QUESTIONS: Q21 to Q35)
    # ----------------------------------------------------
    ca = [
        {
            "id": "P1-T2-CA-21", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Under the Gruha Lakshmi guarantee scheme in Karnataka, which category of women is strictly ineligible to receive the ₹2,000 monthly financial aid?",
            "text_alt": "ಕರ್ನಾಟಕದ ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಯಡಿ ತಿಂಗಳಿಗೆ ₹2,000 ಪಡೆಯಲು ಯಾವ ವರ್ಗದ ಮಹಿಳೆಯರು ಅರ್ಹರಲ್ಲ?",
            "options": [{"label": "A", "text": "Women who are income tax payers or whose husbands file income tax/GST"}, {"label": "B", "text": "Women holding Antyodaya ration cards"}, {"label": "C", "text": "Widows receiving Sandhya Suraksha pension"}, {"label": "D", "text": "Unemployed housewives in rural areas"}],
            "answer": "A",
            "explanation": "Women heads of households (or their spouses) who pay Income Tax or file Goods and Services Tax (GST) returns are excluded from Gruha Lakshmi benefits."
        },
        {
            "id": "P1-T2-CA-22", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "The Shakti scheme launched by the Government of Karnataka grants free bus travel to domicile women across all of the following EXCEPT:",
            "text_alt": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಶಕ್ತಿ ಯೋಜನೆಯು ರಾಜ್ಯದ ಮಹಿಳೆಯರಿಗೆ ಈ ಕೆಳಗಿನ ಯಾವ ಬಸ್ ಸೇವೆಗಳಲ್ಲಿ ಉಚಿತ ಪ್ರಯಾಣವನ್ನು ಕಲ್ಪಿಸುವುದಿಲ್ಲ?",
            "options": [{"label": "A", "text": "KSRTC Rajahamsa and Airavat Club Class buses"}, {"label": "B", "text": "BMTC Ordinary City buses"}, {"label": "C", "text": "NWKRTC ordinary express buses"}, {"label": "D", "text": "KKRTC ordinary rural buses"}],
            "answer": "A",
            "explanation": "Shakti scheme covers ordinary city, suburban, and rural express buses of KSRTC, BMTC, NWKRTC, and KKRTC, but excludes luxury, AC, sleeper, Rajahamsa, and Airavat coaches."
        },
        {
            "id": "P1-T2-CA-23", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Under the Gruha Jyothi scheme, how is the entitlement of free domestic power calculated for an eligible household?",
            "text_alt": "ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಯಡಿ ಗೃಹಬಳಕೆಯ ಉಚಿತ ವಿದ್ಯುತ್ ಅರ್ಹತೆಯನ್ನು ಹೇಗೆ ಲೆಕ್ಕಹಾಕಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Average monthly consumption of previous 12 months + 10% buffer, subject to a maximum cap of 200 units"}, {"label": "B", "text": "Flat 300 units for every consumer irrespective of past usage"}, {"label": "C", "text": "100 units for urban areas and 50 units for rural areas"}, {"label": "D", "text": "Calculated on number of family members multiplied by 20 units"}],
            "answer": "A",
            "explanation": "Gruha Jyothi entitles domestic consumers to free electricity calculated as their average monthly usage over the previous fiscal year plus a 10% buffer, capped at 200 units/month."
        },
        {
            "id": "P1-T2-CA-24", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Under the Anna Bhagya scheme, when physical rice procurement was constrained, what cash DBT rate per kilogram was transferred directly to BPL beneficiaries in lieu of the additional 5 kg rice?",
            "text_alt": "ಅನ್ನಭಾಗ್ಯ ಯೋಜನೆಯಡಿ ಅಕ್ಕಿಯ ಕೊರತೆ ಉಂಟಾದಾಗ ಹೆಚ್ಚುವರಿ 5 ಕೆಜಿ ಅಕ್ಕಿಯ ಬದಲಾಗಿ ಪ್ರತಿ ಕೆಜಿಗೆ ಎಷ್ಟು ದರದಲ್ಲಿ ನಗದು ಡಿಬಿಟಿ ಜಮೆ ಮಾಡಲಾಯಿತು?",
            "options": [{"label": "A", "text": "₹34 per kg"}, {"label": "B", "text": "₹25 per kg"}, {"label": "C", "text": "₹40 per kg"}, {"label": "D", "text": "₹50 per kg"}],
            "answer": "A",
            "explanation": "The Karnataka government initiated direct cash transfer of ₹170 per person per month (at ₹34/kg for 5 kg) into the bank accounts of BPL cardholders."
        },
        {
            "id": "P1-T2-CA-25", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the maximum duration for which an eligible unemployed degree holder can receive the ₹3,000 monthly allowance under the Yuva Nidhi scheme?",
            "text_alt": "ಯುವನಿಧಿ ಯೋಜನೆಯಡಿ ನಿರುದ್ಯೋಗಿ ಪದವೀಧರರು ಗರಿಷ್ಠ ಎಷ್ಟು ಅವಧಿಯವರೆಗೆ ತಿಂಗಳಿಗೆ ₹3,000 ಭತ್ಯೆಯನ್ನು ಪಡೆಯಬಹುದು?",
            "options": [{"label": "A", "text": "2 years (or until employment is secured, whichever is earlier)"}, {"label": "B", "text": "5 years"}, {"label": "C", "text": "1 year"}, {"label": "D", "text": "Until age 35"}],
            "answer": "A",
            "explanation": "Yuva Nidhi is tenable for a maximum period of 2 years from the date of enrollment or until the beneficiary secures employment/self-employment."
        },
        {
            "id": "P1-T2-CA-26", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "In the Bharatiya Nyaya Sanhita (BNS 2023) enforced on 1 July 2024, the colonial offense of 'Sedition' (Section 124A of IPC) was repealed and replaced by Section 152 penalizing:",
            "text_alt": "2024 ರ ಜುಲೈ 1 ರಿಂದ ಜಾರಿಗೆ ಬಂದ ಭಾರತೀಯ ನ್ಯಾಯ ಸಂಹಿತೆಯಲ್ಲಿ (ಬಿಎನ್‌ಎಸ್) ರಾಜದ್ರೋಹವನ್ನು ರದ್ದುಗೊಳಿಸಿ 152 ನೇ ಸೆಕ್ಷನ್‌ನಲ್ಲಿ ಯಾವ ಕೃತ್ಯವನ್ನು ಶಿಕ್ಷಾರ್ಹಗೊಳಿಸಲಾಗಿದೆ?",
            "options": [{"label": "A", "text": "Acts endangering sovereignty, unity, and integrity of India"}, {"label": "B", "text": "Contempt of Parliament"}, {"label": "C", "text": "Defamation of public servants"}, {"label": "D", "text": "Criticism of foreign diplomatic missions"}],
            "answer": "A",
            "explanation": "Section 152 of BNS penalizes acts endangering the sovereignty, unity, and integrity of India, eliminating the colonial term 'sedition' and protecting legitimate speech."
        },
        {
            "id": "P1-T2-CA-27", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which landmark procedural reform has been codified under Section 173 of the Bharatiya Nagarik Suraksha Sanhita (BNSS 2023), allowing citizens to lodge complaints at any police station irrespective of jurisdiction?",
            "text_alt": "ಭಾರತೀಯ ನಾಗರಿಕ ಸುರಕ್ಷಾ ಸಂಹಿತೆಯಡಿ (ಬಿಎನ್‌ಎಸ್‌ಎಸ್) ಯಾವುದೇ ಪೊಲೀಸ್ ಠಾಣೆಯಲ್ಲೂ ನ್ಯಾಯವ್ಯಾಪ್ತಿಯ ಹಂಗಿಲ್ಲದೆ ದೂರು ದಾಖಲಿಸಲು ಅವಕಾಶ ಕಲ್ಪಿಸಿದ ಸುಧಾರಣೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Zero FIR"}, {"label": "B", "text": "Anticipatory Bail"}, {"label": "C", "text": "Habeas Corpus Petition"}, {"label": "D", "text": "Suo Motu Cognitive Cognizance"}],
            "answer": "A",
            "explanation": "BNSS 2023 formally mandates 'Zero FIR', requiring police to register an FIR for cognizable offenses anywhere and subsequently transfer it to the jurisdictional station."
        },
        {
            "id": "P1-T2-CA-28", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The Constitution (106th Amendment) Act, 2023, widely known as Nari Shakti Vandan Adhiniyam, provides what percentage of reservation for women in Lok Sabha and State Legislative Assemblies?",
            "text_alt": "ನಾರಿ ಶಕ್ತಿ ವಂದನ್ ಅಧಿನಿಯಮ (106 ನೇ ಸಂವಿಧಾನ ತಿದ್ದುಪಡಿ ಕಾಯ್ದೆ 2023) ಲೋಕಸಭೆ ಮತ್ತು ರಾಜ್ಯ ವಿಧಾನಸಭೆಗಳಲ್ಲಿ ಮಹಿಳೆಯರಿಗೆ ಎಷ್ಟು ಶೇಕಡಾ ಮೀಸಲಾತಿ ನೀಡುತ್ತದೆ?",
            "options": [{"label": "A", "text": "33% (One-third of total seats)"}, {"label": "B", "text": "50%"}, {"label": "C", "text": "25%"}, {"label": "D", "text": "27%"}],
            "answer": "A",
            "explanation": "The 106th Amendment reserves 33% (one-third) of seats for women in Lok Sabha, State Legislative Assemblies, and NCT of Delhi, effective after census and delimitation."
        },
        {
            "id": "P1-T2-CA-29", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Who headed the High-Level Committee on 'One Nation, One Election' that submitted its recommendations to the President of India in March 2024?",
            "text_alt": "2024 ರ ಮಾರ್ಚ್‌ನಲ್ಲಿ ಭಾರತದ ರಾಷ್ಟ್ರಪತಿಗಳಿಗೆ ತನ್ನ ವರದಿಯನ್ನು ಸಲ್ಲಿಸಿದ 'ಒಂದು ರಾಷ್ಟ್ರ, ಒಂದು ಚುನಾವಣೆ' ಉನ್ನತ ಮಟ್ಟದ ಸಮಿತಿಯ ಅಧ್ಯಕ್ಷರು ಯಾರು?",
            "options": [{"label": "A", "text": "Shri Ram Nath Kovind (Former President of India)"}, {"label": "B", "text": "Justice N. V. Ramana"}, {"label": "C", "text": "Shri N. K. Singh"}, {"label": "D", "text": "Shri Suresh Prabhu"}],
            "answer": "A",
            "explanation": "Former President of India Ram Nath Kovind chaired the 8-member High-Level Committee on Simultaneous Elections recommending a two-phase synchronization."
        },
        {
            "id": "P1-T2-CA-30", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Who was appointed as the Chairman of the 16th Finance Commission constituted by the President of India under Article 280?",
            "text_alt": "280 ನೇ ವಿಧಿಯಡಿ ರಚಿಸಲಾದ 16 ನೇ ಹಣಕಾಸು ಆಯೋಗದ ಅಧ್ಯಕ್ಷರಾಗಿ ನೇಮಕಗೊಂಡ ಪ್ರಸಿದ್ಧ ಅರ್ಥಶಾಸ್ತ್ರಜ್ಞರು ಯಾರು?",
            "options": [{"label": "A", "text": "Dr. Arvind Panagariya"}, {"label": "B", "text": "Shri N. K. Singh"}, {"label": "C", "text": "Dr. Y. V. Reddy"}, {"label": "D", "text": "Dr. Vijay Kelkar"}],
            "answer": "A",
            "explanation": "Dr. Arvind Panagariya (former Vice Chairman of NITI Aayog) was appointed Chairman of the 16th Finance Commission for the award period 2026–2031."
        },
        {
            "id": "P1-T2-CA-31", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "What official name was designated by Prime Minister Narendra Modi for the lunar south pole touchdown location of Chandrayaan-3's Vikram Lander?",
            "text_alt": "ಚಂದ್ರಯಾನ-3 ರ ವಿಕ್ರಮ್ ಲ್ಯಾಂಡರ್ ಇಳಿದ ಚಂದ್ರನ ದಕ್ಷಿಣ ಧ್ರುವದ ಸ್ಥಳಕ್ಕೆ ಪ್ರಧಾನಿ ನರೇಂದ್ರ ಮೋದಿಯವರು ನೀಡಿದ ಅಧಿಕೃತ ಹೆಸರೇನು?",
            "options": [{"label": "A", "text": "Shiv Shakti Point"}, {"label": "B", "text": "Tiranga Point"}, {"label": "C", "text": "Jawahar Point"}, {"label": "D", "text": "Atal Point"}],
            "answer": "A",
            "explanation": "The Chandrayaan-3 landing site was named 'Shiv Shakti Point', while the Chandrayaan-2 impact spot was named 'Tiranga Point'; August 23 is National Space Day."
        },
        {
            "id": "P1-T2-CA-32", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "India's first dedicated solar observatory satellite Aditya-L1 was successfully placed into halo orbit around which point located ~1.5 million km from Earth?",
            "text_alt": "ಭೂಮಿಯಿಂದ ಸುಮಾರು 15 ಲಕ್ಷ ಕಿ.ಮೀ ದೂರದಲ್ಲಿರುವ ಯಾವ ಹಾಲೋ ಕಕ್ಷೆಗೆ ಭಾರತದ ಪ್ರಥಮ ಸೌರ ವೀಕ್ಷಣಾಲಯ ಆದಿತ್ಯ-ಎಲ್1 ನ್ನು ಸೇರಿಸಲಾಯಿತು?",
            "options": [{"label": "A", "text": "Sun-Earth Lagrangian Point 1 (L1)"}, {"label": "B", "text": "Lagrangian Point 2 (L2)"}, {"label": "C", "text": "Geostationary Transfer Orbit"}, {"label": "D", "text": "Lunar Orbit"}],
            "answer": "A",
            "explanation": "Aditya-L1 was placed in a halo orbit around Lagrangian Point 1 (L1) on 6 January 2024, enabling unhindered 24/7 continuous view of the Sun."
        },
        {
            "id": "P1-T2-CA-33", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "Which Indian Air Force test pilot, among the four designated Gaganyaan astronaut-elects, was chosen to fly to the International Space Station (ISS) on the Axiom-4 mission?",
            "text_alt": "ಗಗನ್‌ಯಾನ್‌ನ ನಾಲ್ಕು ಗಗನಯಾತ್ರಿಗಳಲ್ಲಿ ಅಮೆರಿಕದ ಆಕ್ಸಿಯಂ-4 ಮಿಷನ್ ಮೂಲಕ ಅಂತರರಾಷ್ಟ್ರೀಯ ಬಾಹ್ಯಾಕಾಶ ನಿಲ್ದಾಣಕ್ಕೆ (ಐಎಸ್‌ಎಸ್) ಪ್ರಯಾಣಿಸಲು ಆಯ್ಕೆಯಾದ ಐಎಎಫ್ ಪೈಲಟ್ ಯಾರು?",
            "options": [{"label": "A", "text": "Wing Commander Shubhanshu Shukla"}, {"label": "B", "text": "Group Captain Prashanth Nair"}, {"label": "C", "text": "Group Captain Ajit Krishnan"}, {"label": "D", "text": "Group Captain Angad Pratap"}],
            "answer": "A",
            "explanation": "Wing Commander Shubhanshu Shukla was selected as prime astronaut for the joint Indo-US Axiom-4 commercial mission to the International Space Station."
        },
        {
            "id": "P1-T2-CA-34", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Who among the following agricultural scientists was posthumously conferred the Bharat Ratna in 2024 for pioneering India's Green Revolution?",
            "text_alt": "2024 ರಲ್ಲಿ ಭಾರತದ ಹಸಿರು ಕ್ರಾಂತಿಯ ಹರಿಕಾರರಾದ ಯಾವ ಕೃಷಿ ವಿಜ್ಞಾನಿಗಳಿಗೆ ಮರಣೋತ್ತರವಾಗಿ 'ಭಾರತ ರತ್ನ' ಪ್ರಶಸ್ತಿ ನೀಡಿ ಗೌರವಿಸಲಾಯಿತು?",
            "options": [{"label": "A", "text": "Dr. M. S. Swaminathan"}, {"label": "B", "text": "Dr. Verghese Kurien"}, {"label": "C", "text": "Dr. Norman Borlaug"}, {"label": "D", "text": "Dr. Homi Bhabha"}],
            "answer": "A",
            "explanation": "Dr. M. S. Swaminathan was posthumously conferred the Bharat Ratna in 2024 alongside Karpoori Thakur, P. V. Narasimha Rao, Chaudhary Charan Singh, and L. K. Advani."
        },
        {
            "id": "P1-T2-CA-35", "paper": 1, "section_id": "S2", "subject": "Current Affairs", "syllabus_id": "P1-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The 58th Jnanpith Award (for 2023) was jointly conferred upon celebrated Urdu poet Gulzar and which eminent Sanskrit scholar?",
            "text_alt": "58 ನೇ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿಯನ್ನು ಪ್ರಸಿದ್ಧ ಉರ್ದು ಕವಿ ಗುಲ್ಜಾರ್ ಅವರೊಂದಿಗೆ ಯಾವ ಸಂಸ್ಕೃತ ವಿದ್ವಾಂಸರಿಗೆ ಜಂಟಿಯಾಗಿ ನೀಡಲಾಯಿತು?",
            "options": [{"label": "A", "text": "Jagadguru Rambhadracharya"}, {"label": "B", "text": "Acharya Vidyanand"}, {"label": "C", "text": "Pandit Ravi Shankar"}, {"label": "D", "text": "Sri Sri Ravi Shankar"}],
            "answer": "A",
            "explanation": "The 58th Jnanpith Award was jointly awarded to renowned lyricist/filmmaker Gulzar (Urdu) and Sanskrit polymath Jagadguru Rambhadracharya."
        }
    ]
    qs.extend(ca)

    # ----------------------------------------------------
    # SECTION 3: GENERAL KANNADA (25 QUESTIONS: Q36 to Q60)
    # ----------------------------------------------------
    kan = [
        {
            "id": "P1-T2-KAN-36", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "easy",
            "text": "ಕನ್ನಡ ವರ್ಣಮಾಲೆಯಲ್ಲಿರುವ ಯೋಗವಾಹಗಳ ಒಟ್ಟು ಸಂಖ್ಯೆ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "೨ (ಅನುಸ್ವಾರ ಮತ್ತು ವಿಸರ್ಗ)"}, {"label": "B", "text": "೪"}, {"label": "C", "text": "೯"}, {"label": "D", "text": "೨೫"}],
            "answer": "A",
            "explanation": "ಯೋಗವಾಹಗಳು ಎರಡು: ಅನುಸ್ವಾರ (o) ಮತ್ತು ವಿಸರ್ಗ (:). ಇವು ಸ್ವತಂತ್ರವಾಗಿ ಉಚ್ಚಾರವಾಗದೆ ಸ್ವರದ ಸಹಾಯದಿಂದ ಉಚ್ಚಾರವಾಗುತ್ತವೆ."
        },
        {
            "id": "P1-T2-KAN-37", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "ಕನ್ನಡ ವರ್ಣಮಾಲೆಯಲ್ಲಿರುವ ಹ್ರಸ್ವ ಸ್ವರಗಳ ಸಂಖ್ಯೆ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "೬ (ಅ, ಇ, ಉ, ಋ, ಎ, ಒ)"}, {"label": "B", "text": "೭"}, {"label": "C", "text": "೮"}, {"label": "D", "text": "೫"}],
            "answer": "A",
            "explanation": "ಒಂದು ಮಾತ್ರಾ ಕಾಲದಲ್ಲಿ ಉಚ್ಚರಿಸಲಾಗುವ ಸ್ವರಗಳಿಗೆ ಹ್ರಸ್ವ ಸ್ವರಗಳೆನ್ನುವರು. ಅವು ೬: ಅ, ಇ, ಉ, ಋ, ಎ, ಒ."
        },
        {
            "id": "P1-T2-KAN-38", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "ಕನ್ನಡ ವರ್ಣಮಾಲೆಯಲ್ಲಿರುವ ಒಟ್ಟು ವರ್ಗೀಯ ವ್ಯಂಜನಗಳ ಸಂಖ್ಯೆ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "೨೫"}, {"label": "B", "text": "೩೪"}, {"label": "C", "text": "೯"}, {"label": "D", "text": "೧೪"}],
            "answer": "A",
            "explanation": "ಕ-ವರ್ಗದಿಂದ ಮ-ವರ್ಗದವರೆಗೆ ಇರುವ ೨೫ ವ್ಯಂಜನಗಳನ್ನು ವರ್ಗೀಯ ವ್ಯಂಜನಗಳೆಂದು ಕರೆಯಲಾಗುತ್ತದೆ."
        },
        {
            "id": "P1-T2-KAN-39", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "medium",
            "text": "'ಊರಲ್ಲಿ' (ಊರು + ಅಲ್ಲಿ) - ಈ ಪದದಲ್ಲಿ ಆಗಿರುವ ಸಂಧಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಲೋಪ ಸಂಧಿ"}, {"label": "B", "text": "ಆಗಮ ಸಂಧಿ"}, {"label": "C", "text": "ಆದೇಶ ಸಂಧಿ"}, {"label": "D", "text": "ಗುಣ ಸಂಧಿ"}],
            "answer": "A",
            "explanation": "ಊರು (ಉ) + ಅಲ್ಲಿ (ಅ) = ಊರಲ್ಲಿ. ಪೂರ್ವಪದದ ಅಂತ್ಯದಲ್ಲಿರುವ 'ಉ' ಸ್ವರವು ಲೋಪವಾಗಿರುವುದರಿಂದ ಇದು ಲೋಪ ಸಂಧಿ."
        },
        {
            "id": "P1-T2-KAN-40", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "'ಮನೆಯನ್ನು' (ಮನೆ + ಅನ್ನು) - ಈ ಪದದಲ್ಲಿ ಆಗಿರುವ ಸಂಧಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಯಕಾರಾಗಮ ಸಂಧಿ"}, {"label": "B", "text": "ವಕಾರಾಗಮ ಸಂಧಿ"}, {"label": "C", "text": "ಲೋಪ ಸಂಧಿ"}, {"label": "D", "text": "ಆದೇಶ ಸಂಧಿ"}],
            "answer": "A",
            "explanation": "ಮನೆ (ಎ) + ಅನ್ನು = ಮನೆಯನ್ನು. ಪೂರ್ವಪದದ ಅಂತ್ಯದಲ್ಲಿ ಎ/ಏ/ಐ ಸ್ವರಗಳಿದ್ದು ಉತ್ತರಪದದಲ್ಲಿ ಸ್ವರ ಪರವಾದಾಗ 'ಯ್' ಆಗಮವಾಗುವುದು ಯಕಾರಾಗಮ ಸಂಧಿ."
        },
        {
            "id": "P1-T2-KAN-41", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "medium",
            "text": "'ಮಳೆಗಾಲ' (ಮಳೆ + ಕಾಲ) - ಈ ಪದದಲ್ಲಿ ಯಾವ ಸಂಧಿಕಾರ್ಯ ನಡೆದಿದೆ?",
            "options": [{"label": "A", "text": "ಆದೇಶ ಸಂಧಿ (ಕ-ಕಾರಕ್ಕೆ ಗ-ಕಾರ ಆದೇಶ)"}, {"label": "B", "text": "ಲೋಪ ಸಂಧಿ"}, {"label": "C", "text": "ಆಗಮ ಸಂಧಿ"}, {"label": "D", "text": "ಗುಣ ಸಂಧಿ"}],
            "answer": "A",
            "explanation": "ಉತ್ತರಪದದ ಆದಿಯಲ್ಲಿರುವ ಕ, ತ, ಪ ವ್ಯಂಜನಗಳಿಗೆ ಕ್ರಮವಾಗಿ ಗ, ದ, ಬ ಗಳು ಆದೇಶವಾಗಿ ಬರುವುದು ಆದೇಶ ಸಂಧಿ (ಕಾಲ $\to$ ಗಾಲ)."
        },
        {
            "id": "P1-T2-KAN-42", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "'ದೇವೇಂದ್ರ' (ದೇವ + ಇಂದ್ರ) - ಈ ಪದವು ಯಾವ ಸಂಸ್ಕೃತ ಸಂಧಿಗೆ ಉದಾಹರಣೆಯಾಗಿದೆ?",
            "options": [{"label": "A", "text": "ಗುಣ ಸಂಧಿ"}, {"label": "B", "text": "ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ"}, {"label": "C", "text": "ವೃದ್ಧಿ ಸಂಧಿ"}, {"label": "D", "text": "ಯಣ್ ಸಂಧಿ"}],
            "answer": "A",
            "explanation": "ಅ/ಆ ಕಾರಗಳಿಗೆ ಇ/ಈ ಕಾರಗಳು ಪರವಾದಾಗ 'ಏ' ಕಾರ ಬರುವುದು ಗುಣ ಸಂಧಿ (ದೇವ + ಇಂದ್ರ = ದೇವೇಂದ್ರ)."
        },
        {
            "id": "P1-T2-KAN-43", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "'ಏಕೈಕ' (ಏಕ + ಏಕ) - ಈ ಪದದಲ್ಲಿ ಆಗಿರುವ ಸಂಧಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ವೃದ್ಧಿ ಸಂಧಿ"}, {"label": "B", "text": "ಗುಣ ಸಂಧಿ"}, {"label": "C", "text": "ಯಣ್ ಸಂಧಿ"}, {"label": "D", "text": "ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ"}],
            "answer": "A",
            "explanation": "ಅ/ಆ ಕಾರಗಳಿಗೆ ಏ/ಐ ಕಾರಗಳು ಪರವಾದಾಗ 'ಐ' ಕಾರವೂ, ಓ/ಔ ಪರವಾದಾಗ 'ಔ' ಕಾರವೂ ಬರುವುದು ವೃದ್ಧಿ ಸಂಧಿ."
        },
        {
            "id": "P1-T2-KAN-44", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "'ಪ್ರತ್ಯುತ್ತರ' (ಪ್ರತಿ + ಉತ್ತರ) - ಈ ಪದದಲ್ಲಿ ಆಗಿರುವ ಸಂಧಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಯಣ್ ಸಂಧಿ"}, {"label": "B", "text": "ಗುಣ ಸಂಧಿ"}, {"label": "C", "text": "ವೃದ್ಧಿ ಸಂಧಿ"}, {"label": "D", "text": "ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ"}],
            "answer": "A",
            "explanation": "ಇ, ಈ ಕಾರಗಳಿಗೆ ಅನ್ಯಸ್ವರ ಪರವಾದಾಗ 'ಯ್' ಕಾರ ಬರುವುದು ಯಣ್ ಸಂಧಿ (ಪ್ರತಿ + ಉತ್ತರ = ಪ್ರತ್ಯುತ್ತರ)."
        },
        {
            "id": "P1-T2-KAN-45", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.1",
            "origin_tag": "PYQ - GPSTR 2015", "label": "PYQ", "difficulty": "easy",
            "text": "'ವಿದ್ಯಾಭ್ಯಾಸ' (ವಿದ್ಯಾ + ಅಭ್ಯಾಸ) - ಈ ಪದವು ಯಾವ ಸಂಧಿಗೆ ಉದಾಹರಣೆ?",
            "options": [{"label": "A", "text": "ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ"}, {"label": "B", "text": "ಗುಣ ಸಂಧಿ"}, {"label": "C", "text": "ಯಣ್ ಸಂಧಿ"}, {"label": "D", "text": "ವೃದ್ಧಿ ಸಂಧಿ"}],
            "answer": "A",
            "explanation": "ಸವರ್ಣ ಸ್ವರಗಳು ಪರವಾದಾಗ ಅದೇ ಜಾತಿಯ ದೀರ್ಘ ಸ್ವರ ಬರುವುದು ಸವರ್ಣದೀರ್ಘ ಸಂಧಿ (ವಿದ್ಯಾ + ಅಭ್ಯಾಸ = ವಿದ್ಯಾಭ್ಯಾಸ)."
        },
        {
            "id": "P1-T2-KAN-46", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "'ಬೆಟ್ಟಾವರೆ' (ಬೆಟ್ಟದ + ತಾವರೆ) - ಇದು ಯಾವ ಸಮಾಸಕ್ಕೆ ಉದಾಹರಣೆಯಾಗಿದೆ?",
            "options": [{"label": "A", "text": "ತತ್ಪುರುಷ ಸಮಾಸ"}, {"label": "B", "text": "ಕರ್ಮಧಾರಯ ಸಮಾಸ"}, {"label": "C", "text": "ದ್ವಿಗು ಸಮಾಸ"}, {"label": "D", "text": "ಬಹುಬ್ರೀಹಿ ಸಮಾಸ"}],
            "answer": "A",
            "explanation": "ಉತ್ತರಪದದ ಅರ್ಥವು ಪ್ರಧಾನವಾಗಿರುವ ಸಮಾಸವೇ ತತ್ಪುರುಷ ಸಮಾಸ (ಬೆಟ್ಟದ + ತಾವರೆ = ಬೆಟ್ಟಾವರೆ)."
        },
        {
            "id": "P1-T2-KAN-47", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.2",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "'ಹೆಜ್ಜೇನು' (ಹಿರಿದು + ಜೇನು) - ಇದು ಯಾವ ಸಮಾಸಕ್ಕೆ ಉದಾಹರಣೆಯಾಗಿದೆ?",
            "options": [{"label": "A", "text": "ಕರ್ಮಧಾರಯ ಸಮಾಸ"}, {"label": "B", "text": "ತತ್ಪುರುಷ ಸಮಾಸ"}, {"label": "C", "text": "ಗಮಕ ಸಮಾಸ"}, {"label": "D", "text": "ದ್ವಂದ್ವ ಸಮಾಸ"}],
            "answer": "A",
            "explanation": "ಪೂರ್ವಪದವು ವಿಶೇಷಣವಾಗಿಯೂ, ಉತ್ತರಪದವು ವಿಶೇಷ್ಯವಾಗಿಯೂ ಇರುವ ಸಮಾಸವು ಕರ್ಮಧಾರಯ ಸಮಾಸ (ಹಿರಿದು + ಜೇನು = ಹೆಜ್ಜೇನು)."
        },
        {
            "id": "P1-T2-KAN-48", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "'ಮುಲ್ಲೋಕ' (ಮೂರು + ಲೋಕ) - ಪೂರ್ವಪದವು ಸಂಖ್ಯಾವಾಚಕವಾಗಿರುವ ಈ ಸಮಾಸ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ದ್ವಿಗು ಸಮಾಸ"}, {"label": "B", "text": "ದ್ವಂದ್ವ ಸಮಾಸ"}, {"label": "C", "text": "ತತ್ಪುರುಷ ಸಮಾಸ"}, {"label": "D", "text": "ಬಹುಬ್ರೀಹಿ ಸಮಾಸ"}],
            "answer": "A",
            "explanation": "ಪೂರ್ವಪದವು ಸಂಖ್ಯಾವಾಚಕವಾಗಿದ್ದು ನಾಮಪದದೊಂದಿಗೆ ಸೇರಿ ಆಗುವ ಸಮಾಸವೇ ದ್ವಿಗು ಸಮಾಸ."
        },
        {
            "id": "P1-T2-KAN-49", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.2",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "medium",
            "text": "'ಮುಕ್ಕಣ್ಣ' (ಮೂರು ಕಣ್ಣುಗಳುಳ್ಳವನು - ಶಿವ) - ಅನ್ಯಪದದ ಅರ್ಥ ಪ್ರಧಾನವಾಗಿರುವ ಈ ಸಮಾಸ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಬಹುಬ್ರೀಹಿ ಸಮಾಸ"}, {"label": "B", "text": "ಕರ್ಮಧಾರಯ ಸಮಾಸ"}, {"label": "C", "text": "ದ್ವಿಗು ಸಮಾಸ"}, {"label": "D", "text": "ತತ್ಪುರುಷ ಸಮಾಸ"}],
            "answer": "A",
            "explanation": "ಸಮಸ್ತಪದದಲ್ಲಿರುವ ಪದಗಳ ಅರ್ಥವಲ್ಲದೆ ಬೇರೊಂದು ಅನ್ಯಪದದ ಅರ್ಥ ಪ್ರಧಾನವಾಗಿದ್ದರೆ ಅದು ಬಹುಬ್ರೀಹಿ ಸಮಾಸ."
        },
        {
            "id": "P1-T2-KAN-50", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "'ಗಿಡಮರಬಳ್ಳಿಗಳು' - ಎಲ್ಲಾ ಪದಗಳ ಅರ್ಥವೂ ಪ್ರಧಾನವಾಗಿರುವ ಈ ಸಮಾಸ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ದ್ವಂದ್ವ ಸಮಾಸ"}, {"label": "B", "text": "ದ್ವಿಗು ಸಮಾಸ"}, {"label": "C", "text": "ಬಹುಬ್ರೀಹಿ ಸಮಾಸ"}, {"label": "D", "text": "ಕ್ರಿಯಾ ಸಮಾಸ"}],
            "answer": "A",
            "explanation": "ಉಭಯಪದಗಳ ಅಥವಾ ಎಲ್ಲಾ ಪದಗಳ ಅರ್ಥವು ಸಮಾನ ಪ್ರಾಧಾನ್ಯ ಪಡೆದಿರುವ ಸಮಾಸವೇ ದ್ವಂದ್ವ ಸಮಾಸ."
        },
        {
            "id": "P1-T2-KAN-51", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.2",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "'ಅಕ್ಕಲ್ಲು' (ಆ + ಕಲ್ಲು) - ಪೂರ್ವಪದವು ಸರ್ವನಾಮವಾಗಿದ್ದು ಉತ್ತರಪದವು ನಾಮಪದವಾಗಿರುವ ಈ ಸಮಾಸ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಗಮಕ ಸಮಾಸ"}, {"label": "B", "text": "ಸಂಧಿ ಸಮಾಸ"}, {"label": "C", "text": "ಕ್ರಿಯಾ ಸಮಾಸ"}, {"label": "D", "text": "ಕರ್ಮಧಾರಯ ಸಮಾಸ"}],
            "answer": "A",
            "explanation": "ಪೂರ್ವಪದವು ಸರ್ವನಾಮ ಅಥವಾ ಕೃದಂತವಾಗಿದ್ದು, ಉತ್ತರಪದವು ನಾಮಪದವಾಗಿರುವ ಸಮಾಸಕ್ಕೆ ಗಮಕ ಸಮಾಸವೆನ್ನುತ್ತಾರೆ."
        },
        {
            "id": "P1-T2-KAN-52", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.2",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "ಕನ್ನಡದ 'ಪಂಚಮೀ ವಿಭಕ್ತಿ'ಯ ಪ್ರತ್ಯಯ ಮತ್ತು ಕಾರಕಾರ್ಥ ಯಾವುದು?",
            "options": [{"label": "A", "text": "'ದೆಸೆಯಿಂದ' - ಅಪಾದಾನ ಕಾರಕ"}, {"label": "B", "text": "'ಅನ್ನು' - ಕರ್ಮ ಕಾರಕ"}, {"label": "C", "text": "'ಇಂದ' - ಕರಣ ಕಾರಕ"}, {"label": "D", "text": "'ಅಲ್ಲಿ' - ಅಧಿಕರಣ ಕಾರಕ"}],
            "answer": "A",
            "explanation": "ಪಂಚಮೀ ವಿಭಕ್ತಿಯ ಪ್ರತ್ಯಯ 'ದೆಸೆಯಿಂದ', ಇದರ ಕಾರಕಾರ್ಥ ಅಪಾದಾನ (ಒಂದರಿಂದ ಇನ್ನೊಂದು ಅಗಲುವಿಕೆ/ಬೇರ್ಪಡುವಿಕೆ)."
        },
        {
            "id": "P1-T2-KAN-53", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.3",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "easy",
            "text": "'ವರ್ಷ' ಎಂಬ ಸಂಸ್ಕೃತ ತತ್ಸಮ ಪದದ ಸರಿಯಾದ ತದ್ಭವ ರೂಪ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ವರುಷ"}, {"label": "B", "text": "ಬರಿಸ"}, {"label": "C", "text": "ವಾರ"}, {"label": "D", "text": "ವಾಸ"}],
            "answer": "A",
            "explanation": "ತತ್ಸಮ 'ವರ್ಷ' ಪದದ ತದ್ಭವ ರೂಪ 'ವರುಷ' (ಅಥವಾ ವರುಷಂ)."
        },
        {
            "id": "P1-T2-KAN-54", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "'ಕಾರ್ಯ' ಎಂಬ ತತ್ಸಮ ಪದದ ಸರಿಯಾದ ತದ್ಭವ ರೂಪ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಕಜ್ಜ"}, {"label": "B", "text": "ಕರ"}, {"label": "C", "text": "ಕಾರು"}, {"label": "D", "text": "ಕಸುಬು"}],
            "answer": "A",
            "explanation": "'ಕಾರ್ಯ' ಪದದ ಕನ್ನಡ ತದ್ಭವ ರೂಪ 'ಕಜ್ಜ'."
        },
        {
            "id": "P1-T2-KAN-55", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "'ಅರ್ಥ' ಎಂಬ ಪದಕ್ಕಿರುವ ನಾನಾರ್ಥಗಳನ್ನು ಗುರುತಿಸಿ:",
            "options": [{"label": "A", "text": "ಹೊನ್ನು, ಧನ, ಕಾರಣ, ತಾತ್ಪರ್ಯ"}, {"label": "B", "text": "ಅರ್ಧ, ಕಾಲು, ಮುಕ್ಕಾಲು"}, {"label": "C", "text": "ಆಕಾಶ, ಭೂಮಿ, ಪಾತಾಳ"}, {"label": "D", "text": "ಸ್ವರ, ವ್ಯಂಜನ, ಮಾತ್ರಾ"}],
            "answer": "A",
            "explanation": "'ಅರ್ಥ' ಪದವು ಧನ/ಸಂಪತ್ತು (ಅರ್ಥಶಾಸ್ತ್ರ), ಕಾರಣ/ಉದ್ದೇಶ, ಹಾಗೂ ತಾತ್ಪರ್ಯ/ಅಭಿಪ್ರಾಯ ಎಂಬ ನಾನಾರ್ಥಗಳನ್ನು ಹೊಂದಿದೆ."
        },
        {
            "id": "P1-T2-KAN-56", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "'ಅಂಬರ' ಎಂಬ ಪದದ ಸಮಾನಾರ್ಥಕ ಪದ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಆಕಾಶ (ಗಗನ) / ವಸ್ತ್ರ"}, {"label": "B", "text": "ಸಮುದ್ರ"}, {"label": "C", "text": "ಪರ್ವತ"}, {"label": "D", "text": "ಅಗ್ನಿ"}],
            "answer": "A",
            "explanation": "'ಅಂಬರ' ಎಂದರೆ ಆಕಾಶ (ಆಕಾಶ ನೀಲಿ) ಹಾಗೂ ಬಟ್ಟೆ/ವಸ್ತ್ರ (ಪೀತಾಂಬರ) ಎಂದರ್ಥ."
        },
        {
            "id": "P1-T2-KAN-57", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "'ಪ್ರತ್ಯಕ್ಷ' ಪದದ ಸರಿಯಾದ ವಿರುದ್ಧ ಪದ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಪರೋಕ್ಷ"}, {"label": "B", "text": "ಅಪ್ರತ್ಯಕ್ಷ"}, {"label": "C", "text": "ಅಪರೋಕ್ಷ"}, {"label": "D", "text": "ವಿಪರೀತ"}],
            "answer": "A",
            "explanation": "'ಪ್ರತ್ಯಕ್ಷ' (ಕಣ್ಣಿಗೆ ಕಾಣುವಂತಹುದು) ಪದದ ಸರಿಯಾದ ವ್ಯಾಕರಣಬದ್ಧ ವಿರುದ್ಧ ಪದ 'ಪರೋಕ್ಷ'."
        },
        {
            "id": "P1-T2-KAN-58", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "'ಉಪ್ಪಿಗಿಂತ ರುಚಿಯಿಲ್ಲ, ___________ ಬಂಧುವಿಲ್ಲ' - ಈ ಗಾದೆ ಮಾತಿನ ಬಿಟ್ಟ ಪದವನ್ನು ಭರ್ತಿ ಮಾಡಿ:",
            "options": [{"label": "A", "text": "ತಾಯಿಗಿಂತ"}, {"label": "B", "text": "ತಂದೆಗಿಂತ"}, {"label": "C", "text": "ಗುರುವಿಗಿಂತ"}, {"label": "D", "text": "ಅಣ್ಣನಿಗಿಂತ"}],
            "answer": "A",
            "explanation": "ಪ್ರಸಿದ್ಧ ಕನ್ನಡ ಗಾದೆ: 'ಉಪ್ಪಿಗಿಂತ ರುಚಿಯಿಲ್ಲ, ತಾಯಿಗಿಂತ ಬಂಧುವಿಲ್ಲ'."
        },
        {
            "id": "P1-T2-KAN-59", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "'ಮುಖವು ಕಮಲದಂತೆ ಸುಂದರವಾಗಿದೆ' - ಈ ವಾಕ್ಯದಲ್ಲಿರುವ ಉಪಮಾನ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ಕಮಲ"}, {"label": "B", "text": "ಮುಖ"}, {"label": "C", "text": "ಅಂತೆ"}, {"label": "D", "text": "ಸುಂದರವಾಗಿದೆ"}],
            "answer": "A",
            "explanation": "ಹೋಲಿಕೆಗೆ ಬಳಸಲಾದ ಪ್ರಸಿದ್ಧ ವಸ್ತು 'ಕಮಲ' ಉಪಮಾನ; ಹೋಲಿಸಲ್ಪಡುವ ವಸ್ತು 'ಮುಖ' ಉಪಮೇಯ; 'ಅಂತೆ' ಉಪಮಾವಾಚಕ; 'ಸುಂದರ' ಸಮಾನಧರ್ಮ."
        },
        {
            "id": "P1-T2-KAN-60", "paper": 1, "section_id": "S3", "subject": "General Kannada", "syllabus_id": "P1-3.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "ಕಂದ ಪದ್ಯದಲ್ಲಿರುವ ನಾಲ್ಕು ಪಾದಗಳ ಒಟ್ಟು ಮಾತ್ರಾ ಸಂಖ್ಯೆ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "೬೪ ಮಾತ್ರಾಗಳು (೧೨ + ೨೦ + ೧೨ + ೨೦)"}, {"label": "B", "text": "೬೦ ಮಾತ್ರಾಗಳು"}, {"label": "C", "text": "೪೮ ಮಾತ್ರಾಗಳು"}, {"label": "D", "text": "೭೨ ಮಾತ್ರಾಗಳು"}],
            "answer": "A",
            "explanation": "ಕಂದ ಪದ್ಯದ ೧ ಮತ್ತು ೩ ನೇ ಪಾದಗಳಲ್ಲಿ ತಲಾ ೧೨ ಮಾತ್ರಾಗಳು (೩ ಚತುರ್ಮಾತ್ರೆಗಳು), ೨ ಮತ್ತು ೪ ನೇ ಪಾದಗಳಲ್ಲಿ ತಲಾ ೨೦ ಮಾತ್ರಾಗಳು (೫ ಚತುರ್ಮಾತ್ರೆಗಳು) ಒಟ್ಟು ೬೪ ಮಾತ್ರಾಗಳಿರುತ್ತವೆ."
        }
    ]
    qs.extend(kan)

    # ----------------------------------------------------
    # SECTION 4: GENERAL ENGLISH (25 QUESTIONS: Q61 to Q85)
    # ----------------------------------------------------
    eng = [
        {
            "id": "P1-T2-ENG-61", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "Neither the teacher nor the students _______ present in the laboratory yesterday.",
            "options": [{"label": "A", "text": "were"}, {"label": "B", "text": "was"}, {"label": "C", "text": "is"}, {"label": "D", "text": "are"}],
            "answer": "A",
            "explanation": "When two subjects are joined by 'neither... nor', the verb agrees with the closer subject ('the students', plural), hence 'were'."
        },
        {
            "id": "P1-T2-ENG-62", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "If she _______ studied diligently, she would have passed the teacher recruitment examination.",
            "options": [{"label": "A", "text": "had"}, {"label": "B", "text": "has"}, {"label": "C", "text": "have"}, {"label": "D", "text": "would have"}],
            "answer": "A",
            "explanation": "Third conditional structure requires 'If + past perfect (had + V3), ... would have + V3'."
        },
        {
            "id": "P1-T2-ENG-63", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "medium",
            "text": "Convert into Passive Voice: 'The committee has submitted the evaluation report.'",
            "options": [{"label": "A", "text": "The evaluation report has been submitted by the committee."}, {"label": "B", "text": "The evaluation report had been submitted by the committee."}, {"label": "C", "text": "The evaluation report was submitted by the committee."}, {"label": "D", "text": "The evaluation report is submitted by the committee."}],
            "answer": "A",
            "explanation": "Present perfect active ('has submitted') changes to passive with 'has been submitted'."
        },
        {
            "id": "P1-T2-ENG-64", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Convert into Indirect Speech: He said, 'I am working on my lesson plan.'",
            "options": [{"label": "A", "text": "He said that he was working on his lesson plan."}, {"label": "B", "text": "He said that I am working on my lesson plan."}, {"label": "C", "text": "He told that he is working on his lesson plan."}, {"label": "D", "text": "He said that he had been working on his lesson plan."}],
            "answer": "A",
            "explanation": "Present continuous ('am working') shifts to past continuous ('was working') in reported speech."
        },
        {
            "id": "P1-T2-ENG-65", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "The headmaster is very proud _______ his school's academic achievements.",
            "options": [{"label": "A", "text": "of"}, {"label": "B", "text": "on"}, {"label": "C", "text": "at"}, {"label": "D", "text": "for"}],
            "answer": "A",
            "explanation": "The adjective 'proud' takes the fixed preposition 'of' ('proud of something')."
        },
        {
            "id": "P1-T2-ENG-66", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "medium",
            "text": "Choose the correct article: 'He is _______ European scholar visiting our university.'",
            "options": [{"label": "A", "text": "a"}, {"label": "B", "text": "an"}, {"label": "C", "text": "the"}, {"label": "D", "text": "no article"}],
            "answer": "A",
            "explanation": "'European' begins with the consonant sound /j/ (yoo-ro-pee-an), hence takes the indefinite article 'a'."
        },
        {
            "id": "P1-T2-ENG-67", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the meaning of the idiom 'To burn the candle at both ends'?",
            "options": [{"label": "A", "text": "To work excessively hard from early morning until late night"}, {"label": "B", "text": "To waste money recklessly"}, {"label": "C", "text": "To cause accidental fire"}, {"label": "D", "text": "To be very generous"}],
            "answer": "A",
            "explanation": "'To burn the candle at both ends' means exhausting oneself by working early and late without rest."
        },
        {
            "id": "P1-T2-ENG-68", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Choose the synonym of the word 'METICULOUS':",
            "options": [{"label": "A", "text": "Careful and thorough"}, {"label": "B", "text": "Careless"}, {"label": "C", "text": "Rapid"}, {"label": "D", "text": "Stubborn"}],
            "answer": "A",
            "explanation": "'Meticulous' means showing great attention to detail; very careful and precise."
        },
        {
            "id": "P1-T2-ENG-69", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Choose the antonym of the word 'OBSOLETE':",
            "options": [{"label": "A", "text": "Modern / Contemporary"}, {"label": "B", "text": "Ancient"}, {"label": "C", "text": "Outdated"}, {"label": "D", "text": "Extinct"}],
            "answer": "A",
            "explanation": "'Obsolete' means no longer produced or used (out of date); its antonym is 'modern' or 'current'."
        },
        {
            "id": "P1-T2-ENG-70", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Identify the correctly spelt word:",
            "options": [{"label": "A", "text": "Accommodation"}, {"label": "B", "text": "Accomodation"}, {"label": "C", "text": "Acommodation"}, {"label": "D", "text": "Accomadation"}],
            "answer": "A",
            "explanation": "'Accommodation' is spelled with double 'c' and double 'm'."
        },
        {
            "id": "P1-T2-ENG-71", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "Find the error in: 'Each of the girls (A) / have brought (B) / their homework (C) / No error (D)'",
            "options": [{"label": "A", "text": "Part B ('have brought' should be 'has brought')"}, {"label": "B", "text": "Part A"}, {"label": "C", "text": "Part C"}, {"label": "D", "text": "Part D"}],
            "answer": "A",
            "explanation": "'Each' takes a singular verb, so 'have brought' must be replaced by 'has brought'."
        },
        {
            "id": "P1-T2-ENG-72", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The phrasal verb 'call off' means:",
            "options": [{"label": "A", "text": "To cancel"}, {"label": "B", "text": "To postpone"}, {"label": "C", "text": "To shout loudly"}, {"label": "D", "text": "To visit unexpectedly"}],
            "answer": "A",
            "explanation": "'To call off' means to cancel an event or arrangement ('The strike was called off')."
        },
        {
            "id": "P1-T2-ENG-73", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Scarcely had the teacher entered the classroom _______ the bell rang.",
            "options": [{"label": "A", "text": "when"}, {"label": "B", "text": "than"}, {"label": "C", "text": "then"}, {"label": "D", "text": "that"}],
            "answer": "A",
            "explanation": "'Scarcely... when' and 'Hardly... when' are standard correlative conjunction pairs ('No sooner... than')."
        },
        {
            "id": "P1-T2-ENG-74", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "A person who loves and collects books is called a:",
            "options": [{"label": "A", "text": "Bibliophile"}, {"label": "B", "text": "Philatelist"}, {"label": "C", "text": "Numismatist"}, {"label": "D", "text": "Polyglot"}],
            "answer": "A",
            "explanation": "A 'bibliophile' is a lover and collector of books (philatelist collects stamps; numismatist collects coins)."
        },
        {
            "id": "P1-T2-ENG-75", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "Identify the figure of speech in: 'The classroom was a zoo during the lunch break.'",
            "options": [{"label": "A", "text": "Metaphor"}, {"label": "B", "text": "Simile"}, {"label": "C", "text": "Personification"}, {"label": "D", "text": "Oxymoron"}],
            "answer": "A",
            "explanation": "A direct comparison equating the classroom to a zoo without 'like' or 'as' is a Metaphor."
        },
        {
            "id": "P1-T2-ENG-76", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Select the correct tag question: 'She plays the veena exceptionally well, _______?'",
            "options": [{"label": "A", "text": "doesn't she?"}, {"label": "B", "text": "does she?"}, {"label": "C", "text": "isn't she?"}, {"label": "D", "text": "won't she?"}],
            "answer": "A",
            "explanation": "Positive present simple with third person singular takes the negative question tag 'doesn't she?'."
        },
        {
            "id": "P1-T2-ENG-77", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "He has been absent from school _______ Monday last.",
            "options": [{"label": "A", "text": "since"}, {"label": "B", "text": "for"}, {"label": "C", "text": "from"}, {"label": "D", "text": "in"}],
            "answer": "A",
            "explanation": "'Since' denotes a specific point in past time from which an action has continued up to the present."
        },
        {
            "id": "P1-T2-ENG-78", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "What is the antonym of 'BENEVOLENT'?",
            "options": [{"label": "A", "text": "Malevolent"}, {"label": "B", "text": "Generous"}, {"label": "C", "text": "Charitable"}, {"label": "D", "text": "Helpful"}],
            "answer": "A",
            "explanation": "'Benevolent' means well-meaning and kindly; 'Malevolent' means having or showing a wish to do evil."
        },
        {
            "id": "P1-T2-ENG-79", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "medium",
            "text": "Identify the part of speech of the underlined word: 'The brave soldier fought *courageously*.'",
            "options": [{"label": "A", "text": "Adverb"}, {"label": "B", "text": "Adjective"}, {"label": "C", "text": "Noun"}, {"label": "D", "text": "Verb"}],
            "answer": "A",
            "explanation": "'Courageously' modifies the verb 'fought', describing how the soldier fought, hence an Adverb."
        },
        {
            "id": "P1-T2-ENG-80", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Choose the correct collective noun: 'A _______ of wolves was spotted near the forest reserve.'",
            "options": [{"label": "A", "text": "pack"}, {"label": "B", "text": "herd"}, {"label": "C", "text": "flock"}, {"label": "D", "text": "swarm"}],
            "answer": "A",
            "explanation": "Wolves assemble in a 'pack' (birds in a flock, cattle in a herd, bees in a swarm)."
        },
        {
            "id": "P1-T2-ENG-81", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which sentence is grammatically correct?",
            "options": [{"label": "A", "text": "One of my friends is an engineer."}, {"label": "B", "text": "One of my friend are an engineer."}, {"label": "C", "text": "One of my friends are an engineer."}, {"label": "D", "text": "One of my friend is an engineer."}],
            "answer": "A",
            "explanation": "'One of + plural noun' takes a singular verb: 'One of my friends is an engineer'."
        },
        {
            "id": "P1-T2-ENG-82", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What does the Latin phrase 'DE FACTO' mean?",
            "options": [{"label": "A", "text": "In reality / in practice (whether by right or not)"}, {"label": "B", "text": "According to lawful decree"}, {"label": "C", "text": "For the public good"}, {"label": "D", "text": "Without prior preparation"}],
            "answer": "A",
            "explanation": "'De facto' denotes existing in actual fact or practice, distinct from 'de jure' (according to law)."
        },
        {
            "id": "P1-T2-ENG-83", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The teacher told the students that oil _______ on water.",
            "options": [{"label": "A", "text": "floats"}, {"label": "B", "text": "floated"}, {"label": "C", "text": "was floating"}, {"label": "D", "text": "had floated"}],
            "answer": "A",
            "explanation": "Universal truths and scientific facts remain in the simple present tense even in indirect speech."
        },
        {
            "id": "P1-T2-ENG-84", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Choose the synonym of 'CANDID':",
            "options": [{"label": "A", "text": "Frank and outspoken"}, {"label": "B", "text": "Deceitful"}, {"label": "C", "text": "Shy"}, {"label": "D", "text": "Arrogant"}],
            "answer": "A",
            "explanation": "'Candid' means truthful, straightforward, and sincere in expression."
        },
        {
            "id": "P1-T2-ENG-85", "paper": 1, "section_id": "S4", "subject": "General English", "syllabus_id": "P1-4.1",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "Identify the clause type of the underlined group: 'I do not know *where he lives*.'",
            "options": [{"label": "A", "text": "Noun clause (Object of the verb 'know')"}, {"label": "B", "text": "Adverb clause of place"}, {"label": "C", "text": "Adjective clause"}, {"label": "D", "text": "Prepositional clause"}],
            "answer": "A",
            "explanation": "'Where he lives' functions as the direct object of the transitive verb 'know', hence it is a Noun clause."
        }
    ]
    qs.extend(eng)

    # ----------------------------------------------------
    # SECTION 5: EDUCATIONAL PSYCHOLOGY (25 QUESTIONS: Q86 to Q110)
    # ----------------------------------------------------
    psy = [
        {
            "id": "P1-T2-PSY-86", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "According to Jean Piaget, the cognitive ability of 'Conservation' (understanding that quantity remains unchanged despite perceptual alterations in shape) develops during which stage?",
            "text_alt": "ಜೀನ್ ಪಿಯಾಜೆ ಪ್ರಕಾರ, ಆಕಾರ ಬದಲಾದರೂ ಪ್ರಮಾಣ ಬದಲಾಗುವುದಿಲ್ಲ ಎಂಬ 'ಸಂರಕ್ಷಣಾ' (Conservation) ಪರಿಕಲ್ಪನೆ ಯಾವ ಹಂತದಲ್ಲಿ ವಿಕಾಸಗೊಳ್ಳುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Concrete Operational Stage (7–11 years)"}, {"label": "B", "text": "Sensorimotor Stage (0–2 years)"}, {"label": "C", "text": "Pre-operational Stage (2–7 years)"}, {"label": "D", "text": "Formal Operational Stage (11+ years)"}],
            "answer": "A",
            "explanation": "Conservation and reversibility emerge during the Concrete Operational Stage (7–11 years), whereas centration dominates the Pre-operational stage."
        },
        {
            "id": "P1-T2-PSY-87", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "medium",
            "text": "In Lev Vygotsky's socio-cultural theory, the gap between what a child can do independently and what they can achieve with guidance is termed:",
            "text_alt": "ವೈಗೋಟ್ಸ್ಕಿ ಸಿದ್ಧಾಂತದಲ್ಲಿ ಮಗು ಸ್ವತಂತ್ರವಾಗಿ ಮಾಡಬಲ್ಲ ಮತ್ತು ಹಿರಿಯರ ಮಾರ್ಗದರ್ಶನದಲ್ಲಿ ಸಾಧಿಸಬಹುದಾದ ಕಲಿಕೆಯ ನಡುವಿನ ಅಂತರವೇನು?",
            "options": [{"label": "A", "text": "Zone of Proximal Development (ZPD)"}, {"label": "B", "text": "Schema"}, {"label": "C", "text": "Equilibration"}, {"label": "D", "text": "Metacognition"}],
            "answer": "A",
            "explanation": "ZPD represents the learning sweet spot where scaffolding from a More Knowledgeable Other (MKO) facilitates mastery."
        },
        {
            "id": "P1-T2-PSY-88", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Lawrence Kohlberg's theory of moral development, universal ethical principles and conscience belong to which moral level?",
            "text_alt": "ಕೊಹ್ಲ್‌ಬರ್ಗ್ ನೈತಿಕ ವಿಕಾಸ ಸಿದ್ಧಾಂತದಲ್ಲಿ ಸಾರ್ವತ್ರಿಕ ನೈತಿಕ ತತ್ವಗಳು ಮತ್ತು ಆತ್ಮಸಾಕ್ಷಿಯ ತೀರ್ಪುಗಳು ಯಾವ ಹಂತಕ್ಕೆ ಸೇರುತ್ತವೆ?",
            "options": [{"label": "A", "text": "Post-conventional Morality"}, {"label": "B", "text": "Pre-conventional Morality"}, {"label": "C", "text": "Conventional Morality"}, {"label": "D", "text": "Heteronomous Morality"}],
            "answer": "A",
            "explanation": "Stage 6 (Universal Ethical Principles) is the highest stage of Post-conventional morality, transcending social laws when laws conflict with justice."
        },
        {
            "id": "P1-T2-PSY-89", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "According to Erik Erikson's psychosocial theory, which developmental crisis characterizes adolescence (12–18 years)?",
            "text_alt": "ಎರಿಕ್ ಎರಿಕ್ಸನ್ ಸಿದ್ಧಾಂತದ ಪ್ರಕಾರ ಹದಿಹರೆಯದಲ್ಲಿ (12-18 ವರ್ಷ) ಉಂಟಾಗುವ ಮಾನಸಿಕ-ಸಾಮಾಜಿಕ ಬಿಕ್ಕಟ್ಟು ಯಾವುದು?",
            "options": [{"label": "A", "text": "Identity vs. Role Confusion"}, {"label": "B", "text": "Trust vs. Mistrust"}, {"label": "C", "text": "Industry vs. Inferiority"}, {"label": "D", "text": "Intimacy vs. Isolation"}],
            "answer": "A",
            "explanation": "Adolescents explore personal identity and values; failure to resolve this stage leads to role confusion and lack of direction."
        },
        {
            "id": "P1-T2-PSY-90", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "medium",
            "text": "Howard Gardner's Theory of Multiple Intelligences identifies eight distinct intelligences. The ability to understand others' motives and moods is called:",
            "text_alt": "ಗಾರ್ಡ್ನರ್ ಬಹುಮುಖಿ ಬುದ್ಧಿಶಕ್ತಿ ಸಿದ್ಧಾಂತದಲ್ಲಿ ಇತರರ ಭಾವನೆಗಳು, ಪ್ರೇರಣೆಗಳು ಮತ್ತು ಮನಸ್ಥಿತಿಯನ್ನು ಗ್ರಹಿಸುವ ಸಾಮರ್ಥ್ಯಕ್ಕೆ ಏನೆನ್ನುತ್ತಾರೆ?",
            "options": [{"label": "A", "text": "Interpersonal Intelligence"}, {"label": "B", "text": "Intrapersonal Intelligence"}, {"label": "C", "text": "Spatial Intelligence"}, {"label": "D", "text": "Linguistic Intelligence"}],
            "answer": "A",
            "explanation": "Interpersonal intelligence relates to understanding other people; Intrapersonal intelligence is self-awareness of one's own feelings and goals."
        },
        {
            "id": "P1-T2-PSY-91", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Robert Sternberg's Triarchic Theory of Intelligence, which three components constitute human intelligence?",
            "text_alt": "ರಾಬರ್ಟ್ ಸ್ಟರ್ನ್‌ಬರ್ಗ್ ಅವರ ಬುದ್ಧಿಶಕ್ತಿ ಸಿದ್ಧಾಂತದಲ್ಲಿ ಪ್ರತಿಪಾದಿಸಲಾದ ಮೂರು ಅಂಶಗಳು ಯಾವುವು?",
            "options": [{"label": "A", "text": "Analytical, Creative, and Practical Intelligence"}, {"label": "B", "text": "Verbal, Mathematical, and Spatial"}, {"label": "C", "text": "Fluid, Crystallized, and General"}, {"label": "D", "text": "Cognitive, Affective, and Psychomotor"}],
            "answer": "A",
            "explanation": "Sternberg's Triarchic Theory posits Componential (Analytical), Experiential (Creative), and Contextual (Practical) intelligence."
        },
        {
            "id": "P1-T2-PSY-92", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "easy",
            "text": "Edward Thorndike's primary law of learning stating that responses followed by satisfaction are strengthened is known as the:",
            "text_alt": "ತೃಪ್ತಿಯನ್ನು ನೀಡುವ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಬಲಗೊಳ್ಳುತ್ತವೆ ಎಂದು ಪ್ರತಿಪಾದಿಸುವ ಥಾರ್ನ್‌ಡೈಕ್ ಕಲಿಕಾ ನಿಯಮ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Law of Effect (ಪರಿಣಾಮ ನಿಯಮ)"}, {"label": "B", "text": "Law of Readiness (ಸಿದ್ಧತಾ ನಿಯಮ)"}, {"label": "C", "text": "Law of Exercise (ಅಭ್ಯಾಸ ನಿಯಮ)"}, {"label": "D", "text": "Law of Associative Shifting"}],
            "answer": "A",
            "explanation": "The Law of Effect posits that behavior followed by satisfying consequences tends to be repeated, while annoying consequences weaken it."
        },
        {
            "id": "P1-T2-PSY-93", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "In B. F. Skinner's Operant Conditioning, which reinforcement schedule produces the highest resistance to extinction (as seen in slot machines)?",
            "text_alt": "ಸ್ಕಿನ್ನರ್ ಅವರ ಕಾರ್ಯಾತ್ಮಕ ಅಭಿವರ್ತನೆಯಲ್ಲಿ ನಷ್ಟವಾಗುವುದನ್ನು ಹೆಚ್ಚು ತಡೆಯುವ ಮತ್ತು ಅತಿ ಹೆಚ್ಚು ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುವ ಬಲವರ್ಧನಾ ವೇಳಾಪಟ್ಟಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Variable Ratio Schedule"}, {"label": "B", "text": "Fixed Interval Schedule"}, {"label": "C", "text": "Fixed Ratio Schedule"}, {"label": "D", "text": "Continuous Reinforcement"}],
            "answer": "A",
            "explanation": "Variable Ratio (VR) reinforcement provides rewards after an unpredictable number of responses, yielding steady, rapid rates resistant to extinction."
        },
        {
            "id": "P1-T2-PSY-94", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Ivan Pavlov's classical conditioning demonstrated that presenting a conditioned stimulus repeatedly without the unconditioned stimulus leads to:",
            "text_alt": "ಪಾವ್ಲೋವ್ ಅವರ ಅಭಿಜಾತ ಅಭಿವರ್ತನೆಯಲ್ಲಿ ಪ್ರಚೋದಕವನ್ನು ಪುನರಾವರ್ತಿಸಿದಾಗ ಬಲವರ್ಧನೆ ಇಲ್ಲದಿದ್ದರೆ ಉಂಟಾಗುವ ಪ್ರಕ್ರಿಯೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Extinction (ಲೋಪ/ನಷ್ಟ)"}, {"label": "B", "text": "Spontaneous Recovery"}, {"label": "C", "text": "Generalization"}, {"label": "D", "text": "Discrimination"}],
            "answer": "A",
            "explanation": "Extinction occurs when the conditioned stimulus (bell) is repeatedly presented without the unconditioned stimulus (food), causing the response to decline."
        },
        {
            "id": "P1-T2-PSY-95", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "medium",
            "text": "Albert Bandura's Social Learning Theory emphasizes that learning occurs through observation and modeling. What are the four observational processes in order?",
            "text_alt": "ಬಂಡೂರ ಅವರ ಸಾಮಾಜಿಕ ಕಲಿಕಾ ಸಿದ್ಧಾಂತದಲ್ಲಿ ಮಾದರಿ ವೀಕ್ಷಣಾ ಕಲಿಕೆಯ ನಾಲ್ಕು ಹಂತಗಳು ಕ್ರಮವಾಗಿ ಯಾವುವು?",
            "options": [{"label": "A", "text": "Attention $\\to$ Retention $\\to$ Reproduction $\\to$ Motivation"}, {"label": "B", "text": "Motivation $\\to$ Attention $\\to$ Retention $\\to$ Action"}, {"label": "C", "text": "Retention $\\to$ Attention $\\to$ Reinforcement $\\to$ Recall"}, {"label": "D", "text": "Stimulus $\\to$ Response $\\to$ Practice $\\to$ Reward"}],
            "answer": "A",
            "explanation": "Bandura's four observational learning sub-processes are: Attention (observing), Retention (remembering), Production/Motor Reproduction, and Motivation."
        },
        {
            "id": "P1-T2-PSY-96", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Under the Rights of Persons with Disabilities (RPwD) Act, 2016, how many categories of disabilities are officially recognized in India?",
            "text_alt": "ಅಂಗವಿಕಲರ ಹಕ್ಕುಗಳ ಕಾಯ್ದೆ 2016 ರ (RPwD Act) ಅನ್ವಯ ಭಾರತದಲ್ಲಿ ಅಧಿಕೃತವಾಗಿ ಗುರುತಿಸಲಾದ ನ್ಯೂನತೆಗಳ/ಅಂಗವೈಕಲ್ಯಗಳ ಸಂಖ್ಯೆ ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "21 categories"}, {"label": "B", "text": "7 categories"}, {"label": "C", "text": "14 categories"}, {"label": "D", "text": "28 categories"}],
            "answer": "A",
            "explanation": "The RPwD Act 2016 expanded recognized disabilities from 7 to 21, including autism, intellectual disability, acid attack survivors, and specific learning disabilities."
        },
        {
            "id": "P1-T2-PSY-97", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "easy",
            "text": "A specific learning disability primarily characterized by persistent difficulties in reading decoding, spelling, and word recognition is called:",
            "text_alt": "ಓದುವಿಕೆ, ಕಾಗುಣಿತ ಮತ್ತು ಪದಗಳನ್ನು ಗುರುತಿಸುವಲ್ಲಿ ನಿರಂತರ ತೊಂದರೆ ಪಡುವ ಕಲಿಕಾ ನ್ಯೂನತೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Dyslexia (ಡಿಸ್ಲೆಕ್ಸಿಯಾ)"}, {"label": "B", "text": "Dyscalculia (ಡಿಸ್ಕ್ಯಾಲ್ಕುಲಿಯಾ)"}, {"label": "C", "text": "Dysgraphia (ಡಿಸ್ಗ್ರಾಫಿಯಾ)"}, {"label": "D", "text": "Dyspraxia (ಡಿಸ್ಪ್ರ್ಯಾಕ್ಸಿಯಾ)"}],
            "answer": "A",
            "explanation": "Dyslexia affects reading decoding; Dyscalculia affects mathematical calculations; Dysgraphia impairs handwriting and fine motor transcription."
        },
        {
            "id": "P1-T2-PSY-98", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Section 12(1)(c) of the Right to Education (RTE) Act, 2009 mandates what percentage of reservation in private unaided schools for children from disadvantaged groups?",
            "text_alt": "ಶಿಕ್ಷಣ ಹಕ್ಕು ಕಾಯ್ದೆ 2009 ರ ಕಲಂ 12(1)(c) ಅನ್ವಯ ಖಾಸಗಿ ಅನುದಾನರಹಿತ ಶಾಲೆಗಳಲ್ಲಿ ಹಿಂದುಳಿದ ವರ್ಗದ ಮಕ್ಕಳಿಗೆ ಎಷ್ಟು ಶೇಕಡಾ ಸೀಟುಗಳನ್ನು ಮೀಸಲಿಡಬೇಕು?",
            "options": [{"label": "A", "text": "25%"}, {"label": "B", "text": "33%"}, {"label": "C", "text": "50%"}, {"label": "D", "text": "15%"}],
            "answer": "A",
            "explanation": "RTE Section 12(1)(c) requires private unaided schools to admit at least 25% children from weaker sections and disadvantaged groups in Grade 1/pre-primary."
        },
        {
            "id": "P1-T2-PSY-99", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.5",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "In the revised Bloom's Taxonomy of educational objectives (Anderson & Krathwohl, 2001), what is the highest cognitive process level?",
            "text_alt": "ಆ್ಯಂಡರ್ಸನ್ ಮತ್ತು ಕ್ರಾತ್‌ವೋಲ್ ಅವರ ಪರಿಷ್ಕೃತ ಬ್ಲೂಮ್ಸ್ ವರ್ಗೀಕರಣದಲ್ಲಿ ಅತಿ ಉನ್ನತ ಮಟ್ಟದ ಜ್ಞಾನಾತ್ಮಕ ಪ್ರಕ್ರಿಯೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Creating (ಸೃಷ್ಟಿಸುವುದು)"}, {"label": "B", "text": "Evaluating (ಮೌಲ್ಯಮಾಪನ)"}, {"label": "C", "text": "Analyzing (ವಿಶ್ಲೇಷಿಸುವುದು)"}, {"label": "D", "text": "Applying (ಅನ್ವಯಿಸುವುದು)"}],
            "answer": "A",
            "explanation": "Revised Bloom's taxonomy hierarchy (bottom to top): Remembering $\\to$ Understanding $\\to$ Applying $\\to$ Analyzing $\\to$ Evaluating $\\to$ Creating."
        },
        {
            "id": "P1-T2-PSY-100", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.5",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Assessment conducted continuously during instructional teaching to diagnose learning gaps and adapt classroom pedagogy is called:",
            "text_alt": "ಬೋಧನಾ ಅವಧಿಯಲ್ಲಿ ಕಲಿಕಾ ನ್ಯೂನತೆಗಳನ್ನು ಗುರುತಿಸಿ ಬೋಧನೆಯನ್ನು ಸುಧಾರಿಸಲು ನಿರಂತರವಾಗಿ ನಡೆಸುವ ಮೌಲ್ಯಮಾಪನ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Formative Assessment (ರೂಪಣಾತ್ಮಕ ಮೌಲ್ಯಮಾಪನ)"}, {"label": "B", "text": "Summative Assessment (ಸಂಕಲನಾತ್ಮಕ ಮೌಲ್ಯಮಾಪನ)"}, {"label": "C", "text": "Norm-Referenced Assessment"}, {"label": "D", "text": "Standardized Testing"}],
            "answer": "A",
            "explanation": "Formative assessment ('assessment for learning') occurs during instruction to provide constructive developmental feedback."
        },
        {
            "id": "P1-T2-PSY-101", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "According to Carl Rogers' Humanistic Theory of Personality, healthy personal growth and self-actualization require:",
            "text_alt": "ಕಾರ್ಲ್ ರೋಜರ್ಸ್ ಅವರ ಮಾನವತಾವಾದಿ ಸಿದ್ಧಾಂತದ ಪ್ರಕಾರ ವ್ಯಕ್ತಿಯ ಆತ್ಮಸಾಕ್ಷಾತ್ಕಾರ ಮತ್ತು ನೈಜ ಬೆಳವಣಿಗೆಗೆ ಅತ್ಯಗತ್ಯವಾದ ವಾತಾವರಣ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Unconditional Positive Regard (ಷರತ್ತುರಹಿತ ಸಕಾರಾತ್ಮಕ ಗೌರವ)"}, {"label": "B", "text": "Strict Discipline and Punishment"}, {"label": "C", "text": "Competitive Comparison with Peers"}, {"label": "D", "text": "Fixed Behaviorist Conditioning"}],
            "answer": "A",
            "explanation": "Carl Rogers highlighted that congruence and unconditional positive regard create a safe psychological environment for self-actualization."
        },
        {
            "id": "P1-T2-PSY-102", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The psychological phenomenon where previous learning hinders or interferes with the acquisition of new material is known as:",
            "text_alt": "ಹಿಂದಿನ ಕಲಿಕೆಯು ಹೊಸ ವಿಷಯವನ್ನು ಕಲಿಯಲು ಅಡ್ಡಿಯಾಗುವ ಪ್ರಕ್ರಿಯೆಗೆ ಏನೆನ್ನುತ್ತಾರೆ?",
            "options": [{"label": "A", "text": "Proactive Interference (ಪೂರ್ವಾನ್ವಯ ಪ್ರತಿಬಂಧ)"}, {"label": "B", "text": "Retroactive Interference (ಪಶ್ಚಾತ್ತಾಪ ಪ್ರತಿಬಂಧ)"}, {"label": "C", "text": "Positive Transfer of Learning"}, {"label": "D", "text": "Bilateral Transfer"}],
            "answer": "A",
            "explanation": "Proactive interference occurs when old memories disrupt the retrieval of newly acquired information (e.g. typing old password instead of new)."
        },
        {
            "id": "P1-T2-PSY-103", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In psychoanalytic theory, Sigmund Freud conceptualized the moral regulator of personality acting on the 'morality principle' as the:",
            "text_alt": "ಸಿಗ್ಮಂಡ್ ಫ್ರಾಯ್ಡ್ ಅವರ ಮನೋವಿಶ್ಲೇಷಣಾ ಸಿದ್ಧಾಂತದಲ್ಲಿ ನೈತಿಕ ತತ್ವಗಳ ಆಧಾರದ ಮೇಲೆ ನಿಯಂತ್ರಿಸುವ ವ್ಯಕ್ತಿತ್ವದ ಭಾಗ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Superego (ಸೂಪರ್ ಈಗೋ)"}, {"label": "B", "text": "Id (ಇದಮ್)"}, {"label": "C", "text": "Ego (ಈಗೋ)"}, {"label": "D", "text": "Libido"}],
            "answer": "A",
            "explanation": "Id operates on pleasure principle; Ego on reality principle; Superego represents internalized moral ideals and guilt (morality principle)."
        },
        {
            "id": "P1-T2-PSY-104", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "easy",
            "text": "The formula to calculate Intelligence Quotient (IQ) introduced by William Stern and standardized by Lewis Terman is:",
            "text_alt": "ವಿಲಿಯಂ ಸ್ಟರ್ನ್ ನೀಡಿದ ಮತ್ತು ಟರ್ಮನ್ ಪ್ರಮಾಣೀಕರಿಸಿದ ಬುದ್ಧಿಶಕ್ತಿ ಲಬ್ಧಾಂಕದ (IQ) ಸೂತ್ರ ಯಾವುದು?",
            "options": [{"label": "A", "text": "IQ = (Mental Age / Chronological Age) × 100"}, {"label": "B", "text": "IQ = (Chronological Age / Mental Age) × 100"}, {"label": "C", "text": "IQ = Mental Age × Chronological Age"}, {"label": "D", "text": "IQ = (Mental Age + Chronological Age) / 2"}],
            "answer": "A",
            "explanation": "IQ = (MA / CA) × 100, where MA is Mental Age determined by standardized testing and CA is actual chronological age."
        },
        {
            "id": "P1-T2-PSY-105", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Wolfgang Köhler's famous experiments with chimpanzees (Sultan) demonstrated learning by:",
            "text_alt": "ಸುಲ್ತಾನ್ ಎಂಬ ಚಿಂಪಾಂಜಿಯ ಮೇಲೆ ಕೊಹ್ಲರ್ ನಡೆಸಿದ ಪ್ರಸಿದ್ಧ ಪ್ರಯೋಗಗಳು ಯಾವ ಕಲಿಕೆಯನ್ನು ಸಾಬೀತುಪಡಿಸುತ್ತವೆ?",
            "options": [{"label": "A", "text": "Insightful Learning (ಒಳನೋಟ ಕಲಿಕೆ)"}, {"label": "B", "text": "Trial and Error Learning"}, {"label": "C", "text": "Conditioned Reflex"}, {"label": "D", "text": "Rote Memorization"}],
            "answer": "A",
            "explanation": "Köhler's Gestalt research demonstrated Insight Learning (the 'Aha!' phenomenon), where the learner suddenly reorganizes perceptual fields to solve a problem."
        },
        {
            "id": "P1-T2-PSY-106", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Carol Gilligan criticized Lawrence Kohlberg's theory of moral development primarily on the grounds of:",
            "text_alt": "ಕ್ಯಾರೊಲ್ ಗಿಲ್ಲಿಗನ್ ಕೊಹ್ಲ್‌ಬರ್ಗ್ ಅವರ ನೈತಿಕ ವಿಕಾಸ ಸಿದ್ಧಾಂತವನ್ನು ಮುಖ್ಯವಾಗಿ ಯಾವ ಕಾರಣಕ್ಕಾಗಿ ಟೀಕಿಸಿದರು?",
            "options": [{"label": "A", "text": "Gender bias ignoring the feminine 'Ethic of Care'"}, {"label": "B", "text": "Ignoring cultural differences in Asia"}, {"label": "C", "text": "Overemphasizing early childhood"}, {"label": "D", "text": "Lack of empirical data"}],
            "answer": "A",
            "explanation": "Gilligan argued Kohlberg's all-male sample overvalued abstract male 'justice' morality while neglecting female relationship-oriented 'care' morality."
        },
        {
            "id": "P1-T2-PSY-107", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "A student who attributes academic failure to 'bad luck' or an 'unfair question paper' exhibits an:",
            "text_alt": "ಪರೀಕ್ಷೆಯಲ್ಲಿ ಅನುತ್ತೀರ್ಣನಾದಾಗ 'ಪತ್ರಿಕೆ ಕಠಿಣವಾಗಿತ್ತು' ಅಥವಾ 'ದುರದೃಷ್ಟ' ಎಂದು ಆರೋಪಿಸುವ ವಿದ್ಯಾರ್ಥಿಯ ನಿಯಂತ್ರಣ ಕೇಂದ್ರ ಯಾವುದು?",
            "options": [{"label": "A", "text": "External Locus of Control"}, {"label": "B", "text": "Internal Locus of Control"}, {"label": "C", "text": "Self-Efficacy Mastery"}, {"label": "D", "text": "Intrinsic Motivation"}],
            "answer": "A",
            "explanation": "Julian Rotter's locus of control posits that external locus attributes outcomes to environmental forces, while internal locus attributes results to personal effort."
        },
        {
            "id": "P1-T2-PSY-108", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Under the RPwD Act 2016, what percentage of reservation in government jobs is provided for persons with benchmark disabilities?",
            "text_alt": "RPwD ಕಾಯ್ದೆ 2016 ರ ಅನ್ವಯ ಸರ್ಕಾರಿ ಉದ್ಯೋಗಗಳಲ್ಲಿ ಅಂಗವಿಕಲರಿಗೆ ಎಷ್ಟು ಶೇಕಡಾ ಮೀಸಲಾತಿ ನಿಗದಿಪಡಿಸಲಾಗಿದೆ?",
            "options": [{"label": "A", "text": "4% (increased from 3%)"}, {"label": "B", "text": "5%"}, {"label": "C", "text": "10%"}, {"label": "D", "text": "2%"}],
            "answer": "A",
            "explanation": "The 2016 Act increased the reservation quota in government employment from 3% to 4%, and in higher education institutions to 5%."
        },
        {
            "id": "P1-T2-PSY-109", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.5",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "In diagnostic educational evaluation, a test designed to compare a student's score against a pre-established performance standard rather than other peers is a:",
            "text_alt": "ವಿದ್ಯಾರ್ಥಿಯ ಸಾಧನೆಯನ್ನು ಇತರ ವಿದ್ಯಾರ್ಥಿಗಳ ಬದಲಾಗಿ ಮೊದಲೇ ನಿಗದಿತ ಮಾನದಂಡಕ್ಕೆ ಹೋಲಿಸಿ ಮೌಲ್ಯಮಾಪನ ಮಾಡುವ ಪರೀಕ್ಷೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Criterion-Referenced Test (ಮಾನದಂಡ ಆಧಾರಿತ ಪರೀಕ್ಷೆ)"}, {"label": "B", "text": "Norm-Referenced Test"}, {"label": "C", "text": "Ipsative Assessment"}, {"label": "D", "text": "Aptitude Test"}],
            "answer": "A",
            "explanation": "Criterion-referenced assessment measures student performance against explicit learning objectives or criteria (e.g. achieving 75%), not peer ranks."
        },
        {
            "id": "P1-T2-PSY-110", "paper": 1, "section_id": "S5", "subject": "Educational Psychology", "syllabus_id": "P1-5.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "According to David Ausubel's Meaningful Verbal Learning theory, instructional material presented prior to the learning task to bridge existing cognitive schemas with new information is called an:",
            "text_alt": "ಆಸುಬೆಲ್ ಸಿದ್ಧಾಂತದಲ್ಲಿ ಹೊಸ ವಿಷಯವನ್ನು ಕಲಿಯುವ ಮುನ್ನ ಹಿಂದಿನ ಜ್ಞಾನದೊಂದಿಗೆ ಬೆಸೆಯಲು ಶಿಕ್ಷಕರು ನೀಡುವ ಪರಿಕಲ್ಪನಾ ಚೌಕಟ್ಟಿಗೆ ಏನೆನ್ನುತ್ತಾರೆ?",
            "options": [{"label": "A", "text": "Advance Organizer (ಮುಂಚಿತ ಸಂಘಟಕ)"}, {"label": "B", "text": "Concept Map"}, {"label": "C", "text": "Operant Reinforcer"}, {"label": "D", "text": "Mnemonic Device"}],
            "answer": "A",
            "explanation": "David Ausubel introduced 'Advance Organizers' (comparative or expository) to anchor new learning into existing cognitive schema hierarchically."
        }
    ]
    qs.extend(psy)

    # ----------------------------------------------------
    # SECTION 6: COMPUTER LITERACY (20 QUESTIONS: Q111 to Q130)
    # ----------------------------------------------------
    comp = [
        {
            "id": "P1-T2-COMP-111", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "easy",
            "text": "Which register in the Central Processing Unit (CPU) holds the memory address of the next instruction to be fetched and executed?",
            "text_alt": "ಸಿಪಿಯು ನಲ್ಲಿ ಮುಂದಿನ ಆದೇಶವನ್ನು ತರಲು ಮೆಮೊರಿ ವಿಳಾಸವನ್ನು ಹೊಂದಿರುವ ರಿಜಿಸ್ಟರ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Program Counter (PC)"}, {"label": "B", "text": "Instruction Register (IR)"}, {"label": "C", "text": "Memory Buffer Register (MBR)"}, {"label": "D", "text": "Accumulator (AC)"}],
            "answer": "A",
            "explanation": "The Program Counter (PC) automatically increments to hold the memory address of the next consecutive instruction to be executed."
        },
        {
            "id": "P1-T2-COMP-112", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which of the following primary storage media is non-volatile and permanently stores the basic bootstrap startup instructions (BIOS)?",
            "text_alt": "ಕಂಪ್ಯೂಟರ್ ಪ್ರಾರಂಭವಾಗಲು ಅಗತ್ಯವಾದ ಮೂಲ ಬೂಟ್‌ಸ್ಟ್ರ್ಯಾಪ್ (BIOS) ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಶಾಶ್ವತವಾಗಿ ಸಂಗ್ರಹಿಸುವ ಮೆಮೊರಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "ROM (Read Only Memory)"}, {"label": "B", "text": "RAM"}, {"label": "C", "text": "SRAM"}, {"label": "D", "text": "Cache"}],
            "answer": "A",
            "explanation": "ROM retains its stored firmware permanently even when the power is turned off (non-volatile), housing the BIOS bootstrap program."
        },
        {
            "id": "P1-T2-COMP-113", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Solid-State Drives (SSDs) are much faster than traditional Hard Disk Drives (HDDs) because they utilize:",
            "text_alt": "ಹಾರ್ಡ್ ಡಿಸ್ಕ್‌ಗಳಿಗಿಂತ ಎಸ್‌ಎಸ್‌ಡಿ ಗಳು ಅತಿ ವೇಗವಾಗಿರಲು ಕಾರಣ ಅವುಗಳಲ್ಲಿ ಬಳಸಲಾಗುವ ತಂತ್ರಜ್ಞಾನ ಯಾವುದು?",
            "options": [{"label": "A", "text": "NAND Flash Memory chips with no moving mechanical parts"}, {"label": "B", "text": "Magnetic spinning platters"}, {"label": "C", "text": "Optical laser beams"}, {"label": "D", "text": "Liquid cooling tubes"}],
            "answer": "A",
            "explanation": "SSDs use semiconductor non-volatile NAND flash memory chips, eliminating mechanical seek times and rotating latency of HDDs."
        },
        {
            "id": "P1-T2-COMP-114", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "In Microsoft Windows, which keyboard shortcut allows a user to lock the computer screen instantly?",
            "text_alt": "ವಿಂಡೋಸ್ ಆಪರೇಟಿಂಗ್ ಸಿಸ್ಟಮ್‌ನಲ್ಲಿ ಕಂಪ್ಯೂಟರ್ ಪರದೆಯನ್ನು ತಕ್ಷಣ ಲಾಕ್ ಮಾಡಲು ಬಳಸುವ ಶಾರ್ಟ್‌ಕಟ್ ಕೀ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Windows Key + L"}, {"label": "B", "text": "Ctrl + Shift + Esc"}, {"label": "C", "text": "Alt + F4"}, {"label": "D", "text": "Windows Key + D"}],
            "answer": "A",
            "explanation": "Windows Key + L immediately locks the computer session; Windows Key + D toggles desktop display."
        },
        {
            "id": "P1-T2-COMP-115", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In the Linux file system hierarchy, which directory contains essential system configuration files including user passwords and network setups?",
            "text_alt": "ಲಿನಕ್ಸ್ ಫೈಲ್ ಸಿಸ್ಟಮ್‌ನಲ್ಲಿ ಬಳಕೆದಾರರ ಪಾಸ್‌ವರ್ಡ್ ಹಾಗೂ ಸಿಸ್ಟಮ್ ಕಾನ್ಫಿಗರೇಶನ್ ಫೈಲ್‌ಗಳನ್ನು ಹೊಂದಿರುವ ಡೈರೆಕ್ಟರಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "/etc"}, {"label": "B", "text": "/bin"}, {"label": "C", "text": "/home"}, {"label": "D", "text": "/dev"}],
            "answer": "A",
            "explanation": "The `/etc` directory in Linux contains system-wide configuration files (such as `/etc/passwd`, `/etc/network/interfaces`)."
        },
        {
            "id": "P1-T2-COMP-116", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "easy",
            "text": "In Microsoft Word, what is the default keyboard shortcut to open the 'Find and Replace' dialog box?",
            "text_alt": "ಮೈಕ್ರೋಸಾಫ್ಟ್ ವರ್ಡ್‌ನಲ್ಲಿ 'ಫೈಂಡ್ ಆಂಡ್ ರಿಪ್ಲೇಸ್' ಸಂವಾದ ಪೆಟ್ಟಿಗೆಯನ್ನು ತೆರೆಯಲು ಬಳಸುವ ಕೀಲಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Ctrl + H"}, {"label": "B", "text": "Ctrl + F"}, {"label": "C", "text": "Ctrl + R"}, {"label": "D", "text": "Ctrl + G"}],
            "answer": "A",
            "explanation": "Ctrl + H opens Find and Replace; Ctrl + F opens Navigation/Find; Ctrl + K inserts Hyperlink."
        },
        {
            "id": "P1-T2-COMP-117", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Microsoft Excel, what symbol is prefixed to create an absolute cell reference that does not change when copied across rows or columns?",
            "text_alt": "ಎಂಎಸ್ ಎಕ್ಸೆಲ್‌ನಲ್ಲಿ ಫಾರ್ಮುಲಾವನ್ನು ಕಾಪಿ ಮಾಡಿದಾಗ ಸೆಲ್ ವಿಳಾಸ ಬದಲಾಗದಂತೆ ಮಾಡಲು ಯಾವ ಚಿಹ್ನೆಯನ್ನು ಬಳಸಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "$ (Dollar symbol, e.g., $A$1)"}, {"label": "B", "text": "# (Hash symbol)"}, {"label": "C", "text": "& (Ampersand)"}, {"label": "D", "text": "@ (At symbol)"}],
            "answer": "A",
            "explanation": "The dollar sign (`$`) locks rows and columns to create absolute references (`$A$1`), toggleable with the F4 key."
        },
        {
            "id": "P1-T2-COMP-118", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Microsoft Excel, which function searches for a value in the leftmost column of a table and returns a value in the same row from a specified column?",
            "text_alt": "ಎಂಎಸ್ ಎಕ್ಸೆಲ್‌ನಲ್ಲಿ ಮೊದಲ ಕಾಲಂನಲ್ಲಿ ಮೌಲ್ಯವನ್ನು ಹುಡುಕಿ ಅದೇ ಅಡ್ಡಸಾಲಿನ ಮತ್ತೊಂದು ಕಾಲಂನ ಮೌಲ್ಯವನ್ನು ಪಡೆಯುವ ಫಂಕ್ಷನ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "VLOOKUP"}, {"label": "B", "text": "HLOOKUP"}, {"label": "C", "text": "COUNTIF"}, {"label": "D", "text": "CONCATENATE"}],
            "answer": "A",
            "explanation": "VLOOKUP (Vertical Lookup) searches for a key in column 1 of a table array and retrieves data from column index `n`."
        },
        {
            "id": "P1-T2-COMP-119", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "In Microsoft PowerPoint, which feature allows consistent formatting, fonts, and logos across all slides in a presentation?",
            "text_alt": "ಪವರ್ ಪಾಯಿಂಟ್‌ನಲ್ಲಿ ಎಲ್ಲಾ ಸ್ಲೈಡ್‌ಗಳಲ್ಲೂ ಏಕರೂಪದ ಫಾಂಟ್, ಬಣ್ಣ ಮತ್ತು ಲೋಗೋ ಅನ್ವಯಿಸಲು ಬಳಸುವ ವೈಶಿಷ್ಟ್ಯ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Slide Master"}, {"label": "B", "text": "Animation Pane"}, {"label": "C", "text": "Slide Sorter"}, {"label": "D", "text": "Format Painter"}],
            "answer": "A",
            "explanation": "The Slide Master is the top slide in a hierarchy that stores information about the theme, fonts, and layout across the entire deck."
        },
        {
            "id": "P1-T2-COMP-120", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.3",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "Which network topology connects all client nodes directly to a central hub or switch?",
            "text_alt": "ಎಲ್ಲಾ ಕಂಪ್ಯೂಟರ್‌ಗಳನ್ನು ಒಂದು ಕೇಂದ್ರ ಸ್ವಿಚ್ ಅಥವಾ ಹಬ್‌ಗೆ ನೇರವಾಗಿ ಸಂಪರ್ಕಿಸುವ ನೆಟ್‌ವರ್ಕ್ ಟೋಪಾಲಜಿ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Star Topology"}, {"label": "B", "text": "Ring Topology"}, {"label": "C", "text": "Bus Topology"}, {"label": "D", "text": "Mesh Topology"}],
            "answer": "A",
            "explanation": "In a Star topology, all devices connect to a central controller (switch); cable failure in one node does not disrupt the rest of the network."
        },
        {
            "id": "P1-T2-COMP-121", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "How many bits are used in IPv4 and IPv6 internet addresses respectively?",
            "text_alt": "IPv4 ಮತ್ತು IPv6 ಇಂಟರ್ನೆಟ್ ವಿಳಾಸಗಳು ಕ್ರಮವಾಗಿ ಎಷ್ಟು ಬಿಟ್‌ಗಳನ್ನು ಹೊಂದಿರುತ್ತವೆ?",
            "options": [{"label": "A", "text": "32 bits and 128 bits"}, {"label": "B", "text": "64 bits and 256 bits"}, {"label": "C", "text": "16 bits and 64 bits"}, {"label": "D", "text": "32 bits and 64 bits"}],
            "answer": "A",
            "explanation": "IPv4 addresses are 32 bits long (e.g. 192.168.1.1); IPv6 addresses are 128 bits long (represented as 8 hexadecimal groups)."
        },
        {
            "id": "P1-T2-COMP-122", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "The protocol responsible for translating human-readable domain names (like www.google.com) into numerical IP addresses is:",
            "text_alt": "ವೆಬ್‌ಸೈಟ್ ಹೆಸರುಗಳನ್ನು ಕಂಪ್ಯೂಟರ್‌ಗೆ ಅರ್ಥವಾಗುವ ಸಂಖ್ಯಾತ್ಮಕ ಐಪಿ ವಿಳಾಸಗಳಿಗೆ ಪರಿವರ್ತಿಸುವ ಪ್ರೋಟೋಕಾಲ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "DNS (Domain Name System)"}, {"label": "B", "text": "DHCP"}, {"label": "C", "text": "FTP"}, {"label": "D", "text": "SMTP"}],
            "answer": "A",
            "explanation": "DNS translates domain names into numerical IP addresses; DHCP dynamically assigns IP addresses to hosts."
        },
        {
            "id": "P1-T2-COMP-123", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What does the 'S' stand for in HTTPS protocol used in secure web browsing?",
            "text_alt": "ಸುರಕ್ಷಿತ ವೆಬ್ ಬ್ರೌಸಿಂಗ್‌ನಲ್ಲಿ ಬಳಸಲಾಗುವ HTTPS ನ 'S' ಅಕ್ಷರದ ಅರ್ಥವೇನು?",
            "options": [{"label": "A", "text": "Secure (utilizing SSL/TLS encryption)"}, {"label": "B", "text": "System"}, {"label": "C", "text": "Standard"}, {"label": "D", "text": "Socket"}],
            "answer": "A",
            "explanation": "HTTPS stands for HyperText Transfer Protocol Secure, encrypting HTTP traffic over Transport Layer Security (TLS/SSL)."
        },
        {
            "id": "P1-T2-COMP-124", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "easy",
            "text": "A cyberattack that uses deceptive emails mimicking trusted banks to trick victims into revealing sensitive passwords and OTPs is known as:",
            "text_alt": "ಬ್ಯಾಂಕ್ ಅಥವಾ ವಿಶ್ವಾಸಾರ್ಹ ಸಂಸ್ಥೆಯ ಹೆಸರಿನಲ್ಲಿ ನಕಲಿ ಇಮೇಲ್ ಕಳುಹಿಸಿ ಪಾಸ್‌ವರ್ಡ್ ಕದಿಯುವ ಸೈಬರ್ ವಂಚನೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Phishing"}, {"label": "B", "text": "Spooling"}, {"label": "C", "text": "Paging"}, {"label": "D", "text": "Defragmentation"}],
            "answer": "A",
            "explanation": "Phishing is social engineering using spoofed communications to harvest credentials; Ransomware encrypts files for extortion."
        },
        {
            "id": "P1-T2-COMP-125", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Malware that encrypts a victim's files and demands payment in cryptocurrency to provide the decryption key is termed:",
            "text_alt": "ಬಳಕೆದಾರರ ಫೈಲ್‌ಗಳನ್ನು ಲಾಕ್ ಮಾಡಿ ಬಿಡುಗಡೆ ಮಾಡಲು ಹಣಕ್ಕೆ ಬೇಡಿಕೆ ಇಡುವ ಮಾಲ್‌ವೇರ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Ransomware"}, {"label": "B", "text": "Spyware"}, {"label": "C", "text": "Adware"}, {"label": "D", "text": "Worm"}],
            "answer": "A",
            "explanation": "Ransomware (e.g. WannaCry) encrypts user storage and demands ransom payments in untraceable cryptocurrency."
        },
        {
            "id": "P1-T2-COMP-126", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "A security device that monitors and filters incoming and outgoing network traffic based on predefined security rules is a:",
            "text_alt": "ಅನಧಿಕೃತ ಪ್ರವೇಶವನ್ನು ತಡೆಗಟ್ಟಲು ಕಂಪ್ಯೂಟರ್ ನೆಟ್‌ವರ್ಕ್‌ನಲ್ಲಿ ಟ್ರಾಫಿಕ್ ಅನ್ನು ಪರಿಶೀಲಿಸುವ ಭದ್ರತಾ ತಂತ್ರಜ್ಞಾನ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Firewall"}, {"label": "B", "text": "Modem"}, {"label": "C", "text": "Repeater"}, {"label": "D", "text": "Gateway"}],
            "answer": "A",
            "explanation": "A Firewall acts as a security barrier filtering packets between trusted internal networks and untrusted external networks."
        },
        {
            "id": "P1-T2-COMP-127", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "How many Bytes are there in exactly One Kilobyte (1 KB) in binary computing storage?",
            "text_alt": "ಕಂಪ್ಯೂಟರ್ ಮೆಮೊರಿ ಲೆಕ್ಕಾಚಾರದಲ್ಲಿ 1 ಕಿಲೋಬೈಟ್ (1 KB) ನಲ್ಲಿರುವ ಒಟ್ಟು ಬೈಟ್‌ಗಳು ಎಷ್ಟು?",
            "options": [{"label": "A", "text": "1024 Bytes"}, {"label": "B", "text": "1000 Bytes"}, {"label": "C", "text": "1048 Bytes"}, {"label": "D", "text": "512 Bytes"}],
            "answer": "A",
            "explanation": "Binary storage uses powers of 2: 1 KB = $2^{10}$ = 1024 Bytes; 1 MB = $2^{20}$ Bytes; 1 GB = $2^{30}$ Bytes."
        },
        {
            "id": "P1-T2-COMP-128", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which port number is standardly used by unencrypted HyperText Transfer Protocol (HTTP)?",
            "text_alt": "ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡದ ಹೆಚ್‌ಟಿಟಿಪಿ (HTTP) ಸಂವಹನಕ್ಕೆ ಬಳಸಲಾಗುವ ಪ್ರಮಾಣಿತ ಪೋರ್ಟ್ ಸಂಖ್ಯೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Port 80"}, {"label": "B", "text": "Port 443"}, {"label": "C", "text": "Port 21"}, {"label": "D", "text": "Port 25"}],
            "answer": "A",
            "explanation": "HTTP standardly uses Port 80; HTTPS uses Port 443; FTP uses Port 21; SMTP uses Port 25."
        },
        {
            "id": "P1-T2-COMP-129", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "What does Two-Factor Authentication (2FA) require to verify user identity securely?",
            "text_alt": "ಟು-ಫ್ಯಾಕ್ಟರ್ ಅಥೆಂಟಿಕೇಶನ್‌ನಲ್ಲಿ (2FA) ಬಳಕೆದಾರರ ದೃಢೀಕರಣಕ್ಕೆ ಯಾವ ಎರಡು ಅಂಶಗಳನ್ನು ಬಳಸಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Something you know (password) and something you have (OTP / authenticator token)"}, {"label": "B", "text": "Two separate passwords"}, {"label": "C", "text": "Password and security question only"}, {"label": "D", "text": "User name and email address"}],
            "answer": "A",
            "explanation": "Multi-factor authentication combines two distinct factors: knowledge (password/PIN), possession (smartphone/OTP token), or inherence (fingerprint)."
        },
        {
            "id": "P1-T2-COMP-130", "paper": 1, "section_id": "S6", "subject": "Computer Literacy", "syllabus_id": "P1-6.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "Which wireless network standard operates on IEEE 802.11 specifications?",
            "text_alt": "IEEE 802.11 ವಿಶೇಷಣಗಳ ಅಡಿಯಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ವೈರ್‌ಲೆಸ್ ನೆಟ್‌ವರ್ಕ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Wi-Fi"}, {"label": "B", "text": "Bluetooth (802.15)"}, {"label": "C", "text": "Ethernet (802.3)"}, {"label": "D", "text": "Zigbee"}],
            "answer": "A",
            "explanation": "IEEE 802.11 specifies Wireless LAN (Wi-Fi); IEEE 802.3 specifies Ethernet; IEEE 802.15 specifies Bluetooth personal area networks."
        }
    ]
    qs.extend(comp)

    # ----------------------------------------------------
    # SECTION 7: HEALTH EDUCATION (10 QUESTIONS: Q131 to Q140)
    # ----------------------------------------------------
    health = [
        {
            "id": "P1-T2-HLT-131", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "easy",
            "text": "Which of the following vitamins is water-soluble and must be regularly replenished through daily diet?",
            "text_alt": "ನೀರಿನಲ್ಲಿ ಕರಗುವ ಮತ್ತು ದೈನಂದಿನ ಆಹಾರದ ಮೂಲಕ ನಿಯಮಿತವಾಗಿ ಸೇವಿಸಬೇಕಾದ ವಿಟಮಿನ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Vitamin C (Ascorbic Acid)"}, {"label": "B", "text": "Vitamin A (Retinol)"}, {"label": "C", "text": "Vitamin D (Calciferol)"}, {"label": "D", "text": "Vitamin K"}],
            "answer": "A",
            "explanation": "Vitamins B and C are water-soluble; Vitamins A, D, E, and K are fat-soluble and stored in liver and adipose tissue."
        },
        {
            "id": "P1-T2-HLT-132", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "PYQ - GPSTR 2017", "label": "PYQ", "difficulty": "easy",
            "text": "Bleeding gums, delayed wound healing, and painful joints are hallmark clinical symptoms of which deficiency disease?",
            "text_alt": "ವಸಡಿನಿಂದ ರಕ್ತ ಸುರಿಯುವುದು ಮತ್ತು ಗಾಯಗಳು ಬೇಗ ಗುಣವಾಗದಿರುವುದು ಯಾವ ಕೊರತೆಯ ಲಕ್ಷಣ?",
            "options": [{"label": "A", "text": "Scurvy (Vitamin C deficiency)"}, {"label": "B", "text": "Rickets (Vitamin D deficiency)"}, {"label": "C", "text": "Beri-Beri (Vitamin B1 deficiency)"}, {"label": "D", "text": "Night Blindness"}],
            "answer": "A",
            "explanation": "Scurvy is caused by Vitamin C deficiency, which impairs collagen synthesis essential for blood vessels and connective tissues."
        },
        {
            "id": "P1-T2-HLT-133", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Nutritional anemia commonly observed among adolescent school girls in India is primarily caused by dietary deficiency of:",
            "text_alt": "ಹದಿಹರೆಯದ ಶಾಲಾ ಬಾಲಕಿಯರಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿ ಕಂಡುಬರುವ ರಕ್ತಹೀನತೆಗೆ (ಅನೀಮಿಯಾ) ಮುಖ್ಯ ಕಾರಣವಾದ ಪೋಷಕಾಂಶ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Iron and Folic Acid"}, {"label": "B", "text": "Calcium"}, {"label": "C", "text": "Sodium"}, {"label": "D", "text": "Potassium"}],
            "answer": "A",
            "explanation": "Iron deficiency impairs hemoglobin synthesis, causing microcytic anemia, addressed under the National Iron Plus Initiative."
        },
        {
            "id": "P1-T2-HLT-134", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which of the following is a non-communicable, chronic lifestyle disease?",
            "text_alt": "ಈ ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಸಾಂಕ್ರಾಮಿಕವಲ್ಲದ ದೀರ್ಘಕಾಲಿಕ ಜೀವನಶೈಲಿಯ ಕಾಯಿಲೆ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Type 2 Diabetes Mellitus"}, {"label": "B", "text": "Tuberculosis"}, {"label": "C", "text": "Cholera"}, {"label": "D", "text": "Malaria"}],
            "answer": "A",
            "explanation": "Type 2 Diabetes, hypertension, and cardiovascular diseases are non-communicable; Tuberculosis is bacterial and Malaria is parasitic."
        },
        {
            "id": "P1-T2-HLT-135", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In First Aid for acute muscle sprains and soft tissue sports injuries, what does the clinical acronym 'RICE' stand for?",
            "text_alt": "ಕ್ರೀಡಾ ಗಾಯಗಳು ಮತ್ತು ಸ್ನಾಯು ಉಳುಕುಗಳಿಗೆ ನೀಡುವ ಪ್ರಥಮ ಚಿಕಿತ್ಸೆಯಲ್ಲಿ 'RICE' ನ ವಿಸ್ತೃತ ರೂಪವೇನು?",
            "options": [{"label": "A", "text": "Rest, Ice, Compression, Elevation"}, {"label": "B", "text": "Run, Inhale, Clean, Exercise"}, {"label": "C", "text": "Rub, Immobilize, Cool, Examine"}, {"label": "D", "text": "Rescue, Inject, Calm, Evacuate"}],
            "answer": "A",
            "explanation": "RICE protocol minimizes swelling and pain: Rest the injured area, apply Ice packs, Compress with bandage, and Elevate above heart level."
        },
        {
            "id": "P1-T2-HLT-136", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "How is Body Mass Index (BMI) standardly calculated for physical fitness evaluation?",
            "text_alt": "ದೈಹಿಕ ಸಾಮರ್ಥ್ಯ ಮೌಲ್ಯಮಾಪನಕ್ಕಾಗಿ ಬಾಡಿ ಮಾಸ್ ಇಂಡೆಕ್ಸ್ (BMI) ಲೆಕ್ಕಾಚಾರ ಮಾಡುವ ಸೂತ್ರ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Weight in kilograms divided by height in meters squared (kg/m²)"}, {"label": "B", "text": "Height in meters divided by weight in kg"}, {"label": "C", "text": "Weight in kg multiplied by height in cm"}, {"label": "D", "text": "Weight in pounds divided by age in years"}],
            "answer": "A",
            "explanation": "BMI = weight (kg) / [height (m)]². Normal BMI range is 18.5 to 24.9; ≥ 25 is overweight; ≥ 30 is obese."
        },
        {
            "id": "P1-T2-HLT-137", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Under the PM POSHAN (Mid-Day Meal) scheme, what is the mandatory nutritional norm per day for upper primary students (Classes 6–8)?",
            "text_alt": "ಪಿಎಂ ಪೋಷಣ್ (ಬಿಸಿಯೂಟ) ಯೋಜನೆಯಡಿ 6-8 ನೇ ತರಗತಿಯ ಹಿರಿಯ ಪ್ರಾಥಮಿಕ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ದಿನಕ್ಕೆ ನಿಗದಿಪಡಿಸಲಾದ ಪೌಷ್ಟಿಕಾಂಶದ ಪ್ರಮಾಣವೆಷ್ಟು?",
            "options": [{"label": "A", "text": "700 Calories and 20 grams of Protein"}, {"label": "B", "text": "450 Calories and 12 grams of Protein"}, {"label": "C", "text": "1000 Calories and 35 grams of Protein"}, {"label": "D", "text": "500 Calories and 15 grams of Protein"}],
            "answer": "A",
            "explanation": "PM POSHAN prescribes: Primary (Classes 1–5): 450 calories and 12g protein; Upper Primary (Classes 6–8): 700 calories and 20g protein."
        },
        {
            "id": "P1-T2-HLT-138", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which chemical compound is standardly added in drinking water treatment to destroy pathogenic bacteria through chlorination?",
            "text_alt": "ಕುಡಿಯುವ ನೀರಿನಲ್ಲಿ ರೋಗಾಣುಗಳನ್ನು ನಾಶಪಡಿಸಲು ಜಲ ಶುದ್ಧೀಕರಣದಲ್ಲಿ ಸೇರಿಸುವ ರಾಸಾಯನಿಕ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Bleaching powder / Chlorine gas"}, {"label": "B", "text": "Alum (Potash alum) only"}, {"label": "C", "text": "Sodium chloride"}, {"label": "D", "text": "Calcium carbonate"}],
            "answer": "A",
            "explanation": "Chlorine (or calcium hypochlorite/bleaching powder) is the primary disinfectant killing waterborne pathogens."
        },
        {
            "id": "P1-T2-HLT-139", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Goitre, characterized by enlargement of the thyroid gland in the neck, is caused by nutritional deficiency of:",
            "text_alt": "ಥೈರಾಯ್ಡ್ ಗ್ರಂಥಿ ಊದಿಕೊಳ್ಳುವ ಗಳಗಂಡ (Goitre) ರೋಗವು ಯಾವ ಪೋಷಕಾಂಶದ ಕೊರತೆಯಿಂದ ಉಂಟಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Iodine"}, {"label": "B", "text": "Iron"}, {"label": "C", "text": "Zinc"}, {"label": "D", "text": "Fluoride"}],
            "answer": "A",
            "explanation": "Iodine deficiency causes hypothyroid enlargement (Goitre) and mental retardation; combated through iodized salt."
        },
        {
            "id": "P1-T2-HLT-140", "paper": 1, "section_id": "S7", "subject": "Health Education", "syllabus_id": "P1-7.2",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "Cardiopulmonary Resuscitation (CPR) performed on an unresponsive non-breathing individual follows which recommended ratio of chest compressions to rescue breaths?",
            "text_alt": "ಉಸಿರಾಟ ನಿಂತ ವ್ಯಕ್ತಿಗೆ ಸಿಪಿಆರ್ (CPR) ಮಾಡುವಾಗ ಎದೆ ಒತ್ತಡ (Chest Compressions) ಮತ್ತು ಕೃತಕ ಉಸಿರಾಟದ ಶಿಫಾರಸು ಅನುಪಾತ ಯಾವುದು?",
            "options": [{"label": "A", "text": "30 compressions to 2 rescue breaths"}, {"label": "B", "text": "15 compressions to 5 rescue breaths"}, {"label": "C", "text": "10 compressions to 1 rescue breath"}, {"label": "D", "text": "50 compressions to 2 rescue breaths"}],
            "answer": "A",
            "explanation": "Standard CPR protocol (American Heart Association & Red Cross) recommends 30 chest compressions followed by 2 rescue breaths at 100–120 bpm."
        }
    ]
    qs.extend(health)

    # ----------------------------------------------------
    # SECTION 8: VALUE EDUCATION (10 QUESTIONS: Q141 to Q150)
    # ----------------------------------------------------
    val = [
        {
            "id": "P1-T2-VAL-141", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "PYQ - GPSTR 2019", "label": "PYQ", "difficulty": "medium",
            "text": "Article 51A(h) of the Constitution of India identifies which of the following as a Fundamental Duty of every Indian citizen?",
            "text_alt": "ಭಾರತ ಸಂವಿಧಾನದ 51ಎ(ಹೆಚ್) ವಿಧಿಯ ಪ್ರಕಾರ ಪ್ರತಿಯೊಬ್ಬ ನಾಗರಿಕನ ಮೂಲಭೂತ ಕರ್ತವ್ಯ ಯಾವುದು?",
            "options": [{"label": "A", "text": "To develop the scientific temper, humanism and the spirit of inquiry and reform"}, {"label": "B", "text": "To promote industrial growth"}, {"label": "C", "text": "To participate in competitive politics"}, {"label": "D", "text": "To pay taxes regularly"}],
            "answer": "A",
            "explanation": "Article 51A(h) enjoins citizens 'to develop the scientific temper, humanism and the spirit of inquiry and reform'."
        },
        {
            "id": "P1-T2-VAL-142", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "The Code of Professional Ethics for School Teachers formulated by the National Council for Teacher Education (NCTE) requires teachers to:",
            "text_alt": "ರಾಷ್ಟ್ರೀಯ ಶಿಕ್ಷಕರ ಶಿಕ್ಷಣ ಮಂಡಳಿಯು (NCTE) ರೂಪಿಸಿದ ವೃತ್ತಿಪರ ನೀತಿ ಸಂಹಿತೆಯ ಪ್ರಕಾರ ಶಿಕ್ಷಕರು ಪಾಲಿಸಬೇಕಾದ ಮುಖ್ಯ ಕರ್ತವ್ಯ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Treat all students with equality, respect, and zero discrimination on caste, creed, or gender"}, {"label": "B", "text": "Compel students to attend private tuitions"}, {"label": "C", "text": "Prioritize only high-scoring students"}, {"label": "D", "text": "Use physical force to maintain discipline"}],
            "answer": "A",
            "explanation": "NCTE professional ethics mandate equitable treatment, non-discrimination, confidentiality, and nurturing student dignity."
        },
        {
            "id": "P1-T2-VAL-143", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "PYQ - GPSTR 2022", "label": "PYQ", "difficulty": "easy",
            "text": "Section 17 of the Right to Education (RTE) Act, 2009 strictly prohibits:",
            "text_alt": "ಶಿಕ್ಷಣ ಹಕ್ಕು ಕಾಯ್ದೆ 2009 ರ ಕಲಂ 17 ಕಟ್ಟುನಿಟ್ಟಾಗಿ ಏನನ್ನು ನಿಷೇಧಿಸುತ್ತದೆ?",
            "options": [{"label": "A", "text": "Physical punishment and mental harassment of children in schools"}, {"label": "B", "text": "Co-curricular activities"}, {"label": "C", "text": "Periodic parent-teacher meetings"}, {"label": "D", "text": "Mid-day meal distribution"}],
            "answer": "A",
            "explanation": "Section 17 of RTE completely bans corporal punishment and mental harassment, making it a punishable disciplinary offense."
        },
        {
            "id": "P1-T2-VAL-144", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Under Section 19 of the POCSO Act (Protection of Children from Sexual Offences Act, 2012), what is the legal obligation of a school teacher who suspects child sexual abuse?",
            "text_alt": "ಪೋಕ್ಸೋ ಕಾಯ್ದೆ 2012 ರ ಸೆಕ್ಷನ್ 19 ರ ಪ್ರಕಾರ ಶಾಲಾ ಶಿಕ್ಷಕರಿಗೆ ಮಕ್ಕಳ ಲೈಂಗಿಕ ದೌರ್ಜನ್ಯದ ಬಗ್ಗೆ ಮಾಹಿತಿ ತಿಳಿದಾಗ ಅವರ ಕಾನೂನುಬದ್ಧ ಕರ್ತವ್ಯವೇನು?",
            "options": [{"label": "A", "text": "Mandatory reporting immediately to the Special Juvenile Police Unit or local police"}, {"label": "B", "text": "Keep the matter confidential without informing authorities"}, {"label": "C", "text": "Settle the dispute informally with parents"}, {"label": "D", "text": "Wait until the end of the academic year"}],
            "answer": "A",
            "explanation": "Section 19 mandates immediate reporting of suspected child abuse; failure to report is a cognizable punishable offense under Section 21."
        },
        {
            "id": "P1-T2-VAL-145", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The famous Appiko environmental conservation movement in Karnataka, inspired by the Himalayan Chipko movement, was launched in 1983 in which district?",
            "text_alt": "1983 ರಲ್ಲಿ ಹಿಮಾಲಯದ ಚಿಪ್ಕೋ ಚಳವಳಿಯಿಂದ ಪ್ರೇರಿತಗೊಂಡು ಕರ್ನಾಟಕದಲ್ಲಿ ಆರಂಭವಾದ ಪ್ರಸಿದ್ಧ 'ಅಪ್ಪಿಕೋ ಚಳವಳಿ' ಯಾವ ಜಿಲ್ಲೆಯಲ್ಲಿ ನಡೆಯಿತು?",
            "options": [{"label": "A", "text": "Uttara Kannada (Gubbigadde, Salkani forest)"}, {"label": "B", "text": "Kodagu"}, {"label": "C", "text": "Chikkamagaluru"}, {"label": "D", "text": "Shivamogga"}],
            "answer": "A",
            "explanation": "Pandurang Hegde led the Appiko movement in Uttara Kannada district in September 1983 to embrace and protect Western Ghats forests from logging."
        },
        {
            "id": "P1-T2-VAL-146", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which core value involves putting oneself in another person's shoes and understanding their feelings from their perspective?",
            "text_alt": "ಇನ್ನೊಬ್ಬರ ಪರಿಸ್ಥಿತಿಯನ್ನು ಅವರ ದೃಷ್ಟಿಕೋನದಿಂದ ಅರ್ಥಮಾಡಿಕೊಂಡು ಅನುಭವಿಸುವ ಉನ್ನತ ನೈತಿಕ ಮೌಲ್ಯ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Empathy (ಸಹಾನುಭೂತಿ)"}, {"label": "B", "text": "Apathy (ನಿರಾಸಕ್ತಿ)"}, {"label": "C", "text": "Selfishness"}, {"label": "D", "text": "Arrogance"}],
            "answer": "A",
            "explanation": "Empathy is cognitive and affective understanding of another's lived experience, deeper than sympathy (which is merely feeling pity)."
        },
        {
            "id": "P1-T2-VAL-147", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which philosophy of value education advocates that values are best caught through teacher modeling and school climate rather than rote textbook lectures?",
            "text_alt": "ಮೌಲ್ಯಗಳನ್ನು ಬಾಯಿಪಾಠ ಮಾಡುವ ಬದಲು ಶಿಕ್ಷಕರ ಆದರ್ಶ ನಡವಳಿಕೆ ಮತ್ತು ಶಾಲಾ ವಾತಾವರಣದ ಮೂಲಕ ಮೈಗೂಡಿಸಿಕೊಳ್ಳಬೇಕು ಎಂದು ಪ್ರತಿಪಾದಿಸುವ ತತ್ವ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Values are caught, not taught"}, {"label": "B", "text": "Rote conditioning"}, {"label": "C", "text": "Dogmatic indoctrination"}, {"label": "D", "text": "Authoritarian obedience"}],
            "answer": "A",
            "explanation": "'Values are caught, not taught' emphasizes experiential learning, teacher modeling, restorative justice, and an inclusive school culture."
        },
        {
            "id": "P1-T2-VAL-148", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Gender sensitization in school classrooms is best promoted by:",
            "text_alt": "ಶಾಲಾ ತರಗತಿಯಲ್ಲಿ ಲಿಂಗ ಸಂವೇದನೆಯನ್ನು (Gender Sensitization) ಉತ್ತೇಜಿಸುವ ಅತ್ಯುತ್ತಮ ವಿಧಾನ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Assigning sports, leadership, and tasks equally to boys and girls without gender stereotypes"}, {"label": "B", "text": "Assigning cleaning only to girls and heavy lifting only to boys"}, {"label": "C", "text": "Segregating seating in all academic activities"}, {"label": "D", "text": "Encouraging gender-biased textbook depictions"}],
            "answer": "A",
            "explanation": "Gender equity deconstructs stereotypes by ensuring equal opportunity in leadership, participation, sports, and collaborative learning."
        },
        {
            "id": "P1-T2-VAL-149", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The Universal Declaration of Human Rights (UDHR) was adopted by the United Nations General Assembly on which historic date observed annually as Human Rights Day?",
            "text_alt": "ವಿಶ್ವ ಮಾನವ ಹಕ್ಕುಗಳ ದಿನವನ್ನು ಪ್ರತಿವರ್ಷ ಯಾವ ದಿನಾಂಕದಂದು ಆಚರಿಸಲಾಗುತ್ತದೆ?",
            "options": [{"label": "A", "text": "10 December (1948)"}, {"label": "B", "text": "24 October"}, {"label": "C", "text": "5 June"}, {"label": "D", "text": "8 March"}],
            "answer": "A",
            "explanation": "The UN General Assembly adopted the UDHR on 10 December 1948 in Paris, observed worldwide as International Human Rights Day."
        },
        {
            "id": "P1-T2-VAL-150", "paper": 1, "section_id": "S8", "subject": "Value Education", "syllabus_id": "P1-8.1",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "Dr. B. R. Ambedkar emphasized that political democracy cannot last unless there lies at the base of it:",
            "text_alt": "ಡಾ. ಬಿ. ಆರ್. ಅಂಬೇಡ್ಕರ್ ಅವರು ರಾಜಕೀಯ ಪ್ರಜಾಪ್ರಭುತ್ವವು ಶಾಶ್ವತವಾಗಿ ಉಳಿಯಲು ಅದರ ತಳಹದಿಯಲ್ಲಿ ಯಾವುದು ಅತ್ಯಗತ್ಯ ಎಂದು ಪ್ರತಿಪಾದಿಸಿದರು?",
            "options": [{"label": "A", "text": "Social Democracy recognizing liberty, equality, and fraternity as principles of life"}, {"label": "B", "text": "Military strength"}, {"label": "C", "text": "Monetary capitalism"}, {"label": "D", "text": "Religious orthodoxy"}],
            "answer": "A",
            "explanation": "Dr. Ambedkar stated: 'Political democracy cannot last unless there lies at the base of it social democracy, which recognizes liberty, equality and fraternity as a trinity'."
        }
    ]
    qs.extend(val)

    return qs

print("Paper 1 Test 2 all 150 questions assembled.")
