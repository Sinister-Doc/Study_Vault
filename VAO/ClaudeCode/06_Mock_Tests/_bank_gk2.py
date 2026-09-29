# -*- coding: utf-8 -*-
"""
Supplementary GK bank — VAO 2026 (Karnataka).
Second pool, drawn on by mock3 so its 50 GK questions are disjoint from mock1's 100.
Same item shape as _bank_gk.py: (question, [4 options], correct_index, explanation, label).

Label convention:
  "PYQ-style" = written in the style of questions repeatedly asked in Karnataka
                PSC / KEA recruitment papers (topic recurring, exact wording not claimed).
  "expected"  = compiled from the standard PSC/KEA syllabus and typical coaching
                question sets. NOT independently fact-checked; see mock_test_notes.md.
"""

EXTRA_HISTORY = [
("The Battle of Talikota (1565) was fought between Vijayanagara and:",
 ["The Deccan Sultanates", "The Mughals", "The Marathas", "The Portuguese"], 0,
 "A combined Deccan Sultanate force defeated Vijayanagara at Talikota (Rakshasa-Tangadi).", "PYQ-style"),
("The Chalukyas of Kalyani are also known as the:",
 ["Badami Chalukyas", "Western Chalukyas", "Eastern Chalukyas", "Vengi Chalukyas"], 1,
 "Chalukyas of Kalyani (Basavakalyana) = Western Chalukyas; Badami = Chalukyas of Vatapi.", "expected"),
]

EXTRA_GEOGRAPHY = [
("Which is the highest peak in Karnataka?",
 ["Kudremukh", "Mullayanagiri", "Baba Budangiri", "Pushpagiri"], 1,
 "Mullayanagiri (Chikkamagaluru district, Baba Budangiri range) is the highest peak in Karnataka, about 1,930 m.", "PYQ-style"),
("The Krishna basin drains approximately what share of Karnataka's area?",
 ["About 25%", "About 40%", "About 60%", "About 80%"], 2,
 "The Krishna and its tributaries drain roughly 60% of the state — the largest basin in Karnataka.", "expected"),
]

EXTRA_POLITY = [
("The 74th Constitutional Amendment deals with:",
 ["Panchayati Raj", "Municipalities and urban local bodies", "Reservation in education", "Anti-defection"], 1,
 "73rd = Panchayati Raj (rural); 74th = Municipalities (urban).", "PYQ-style"),
("How many schedules does the Constitution of India have at present?",
 ["8", "10", "12", "14"], 2,
 "There are 12 schedules. The 9th and 10th were added by amendments.", "expected"),
("The term of a Karnataka Gram Panchayat is:",
 ["3 years", "4 years", "5 years", "6 years"], 2,
 "All three tiers of Panchayati Raj bodies have a five-year term under the 73rd Amendment.", "PYQ-style"),
]

EXTRA_ECONOMY = [
("NITI Aayog replaced which body?",
 ["Finance Commission", "Planning Commission", "Election Commission", "UGC"], 1,
 "NITI Aayog (1 January 2015) replaced the Planning Commission.", "PYQ-style"),
]

EXTRA_SCIENCE = [
("Which gas is most abundant in the Earth's atmosphere?",
 ["Oxygen", "Carbon dioxide", "Nitrogen", "Argon"], 2,
 "Nitrogen is about 78% of the atmosphere by volume; oxygen about 21%.", "expected"),
]

EXTRA_CA = [
("Karnataka's 'Gruha Lakshmi' scheme provides financial assistance to:",
 ["School children", "Women heads of households", "Farmers", "Auto drivers"], 1,
 "Gruha Lakshmi gives a monthly payment to the woman head of an eligible household.", "PYQ-style"),
]
