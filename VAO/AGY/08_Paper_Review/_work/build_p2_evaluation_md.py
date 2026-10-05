# -*- coding: utf-8 -*-
"""
Script to build Paper 2 Evaluation report for KEA VAO 2026
"""
import json, re

with open('VAO/AGY/08_Paper_Review/_work/p2_parsed_eval.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Comprehensive reasoning dictionary for Paper 2
explanations = {
    # Part A: General Kannada (Q1 to Q35)
    1: "ಸೂರ್ಯೋದಯ = ಸೂರ್ಯ+ಉದಯ (ಗುಣ ಸಂಧಿ); ವಿದ್ಯಾಭ್ಯಾಸ = ವಿದ್ಯಾ+ಅಭ್ಯಾಸ (ಸವರ್ಣದೀರ್ಘ); ಗುರೂಪದೇಶ = ಗುರು+ಉಪದೇಶ (ಸವರ್ಣದೀರ್ಘ). ಕ್ರಮ: ಗುಣ - ಸವರ್ಣದೀರ್ಘ - ಸವರ್ಣದೀರ್ಘ.",
    2: "ಪ್ಲುತ ಸ್ವರಗಳ ಮುಂದೆ ಸ್ವರ ಪರವಾದಾಗ ಹಾಗೂ ಭಾವಸೂಚಕ ಅವ್ಯಯಗಳ ಮುಂದೆ ಸ್ವರ ಪರವಾದಾಗ ಸಂಧಿಕಾರ್ಯವಾಗದೆ ಪ್ರಕೃತಿಭಾವ ಉಳಿಯುತ್ತದೆ; ಎರಡೂ ಹೇಳಿಕೆಗಳು ಸರಿ.",
    3: "ವಾಕ್ಯಗಳೆರಡರ ನಡುವೆ ಉಪಮಾವಾಚಕವಿಲ್ಲದೆ ಬಿಂಬ-ಪ್ರತಿಬಿಂಬ ಭಾವದಿಂದ ಅರ್ಥ ವ್ಯಕ್ತವಾಗುವುದರಿಂದ ಇದು ದೃಷ್ಟಾಂತಾಲಂಕಾರವಾಗಿದೆ.",
    4: "ಕಂದಪದ್ಯದ 1ನೇ ಪಾದದಲ್ಲಿ 12 ಮಾತ್ರೆಗಳು, ಮಂದಾನಿಲ ರಗಳೆಯಲ್ಲಿ 16, ಲಲಿತ ರಗಳೆಯಲ್ಲಿ 20 ಮಾತ್ರೆಗಳಿರುತ್ತವೆ (ಭಾಮಿನಿ ಷಟ್ಪದಿಯ 1ನೇ ಪಾದದಲ್ಲಿ 14 ಮಾತ್ರೆಗಳು). (a), (b), (d) ಸರಿ.",
    5: "ಅ/ಆ ಜೊತೆ ಇ/ಈ ಸೇರಿದಾಗ ಕಂಠ ಮತ್ತು ತಾಲವ್ಯ ಸ್ಥಾನಗಳ ಸಂಯೋಗದಿಂದ ‘ಐ’ ವರ್ಣವು ಉತ್ಪತ್ತಿಯಾಗುವುದರಿಂದ ಇದು ಕಂಠತಾಲವ್ಯವಾಗಿದೆ.",
    6: "ಉತ್ತ/ದ/ವ ಕಾಲಸೂಚಕಗಳು (ii), ಅವನು/ಅವಳು/ಅದು ಪ್ರಥಮ ಪುರುಷ (iv), ಅನು/ಇಳು/ಇವೆ ಆಖ್ಯಾತ ಪ್ರತ್ಯಯಗಳು (iii), ಬರೆ/ಆಡಿ/ಬಾ ಧಾತು/ವಿದ್ಯರ್ಥಕ (i). ಕ್ರಮ: a-ii, b-iv, c-iii, d-i.",
    7: "ಆಖ್ಯಾತ ಪ್ರತ್ಯಯಗಳು ಕ್ರಿಯಾಪದದ ಕೊನೆಯಲ್ಲಿ ಸೇರಿ ಕ್ರಿಯೆಯ ಭಾವ/ಅರ್ಥ ಮತ್ತು ಲಿಂಗ-ವಚನ-ಪುರುಷಗಳನ್ನು ಪ್ರಧಾನವಾಗಿ ವ್ಯಕ್ತಪಡಿಸುತ್ತವೆ.",
    8: "ಅನುಕರಣ ಅವ್ಯಯ (ಜುಳುಜುಳು - ii), ಭಾವಸೂಚಕ (ಅಯ್ಯೋ - iii), ಕ್ರಿಯಾರ್ಥಕ (ಬೇಕು - iv), ಸಂಬಂಧಾರ್ಥಕ (ಆದ್ದರಿಂದ - i). ಸಂಕೇತ: a-ii, b-iii, c-iv, d-i.",
    9: "ರುಧಿರ/ರಕ್ತ, ರಾತ್ರಿ/ನಿಶಾ, ರೋದನ/ಗೋಳಾಟ ಸಮಾನಾರ್ಥಕಗಳು; ರಸನ ಎಂದರೆ ನಾಲಿಗೆ/ರುಚಿ (ಜಲನಿಧಿ ಎಂದರೆ ಸಮುದ್ರ). ಆದ್ದರಿಂದ (d) ಮಾತ್ರ ತಪ್ಪಾಗಿದೆ.",
    10: "ಪ್ರಕಾರವಾಚಕ (ಇಂಥವನು - v), ಪರಿಮಾಣವಾಚಕ (ಕೆಲವು - iv), ದಿಗ್ವಾಚಕ (ಬಡಗಲು - i), ಸಂಖ್ಯೇಯವಾಚಕ (ನಾಲ್ವರು - ii). ಸಂಕೇತ: a-v, b-iv, c-i, d-ii.",
    11: "‘ಸರಸರ’ ಎಂಬುದು ಶಬ್ದಾನುಕರಣೆ (ಅನುಕರಣಾವ್ಯಯ), ದ್ವಿರುಕ್ತಿಯಲ್ಲ. ಆದ್ದರಿಂದ (b) ತಪ್ಪಾದ ಜೋಡಿಯಾಗಿದೆ.",
    12: "‘ಭೂತಯ್ಯನ ಮಗ ಅಯ್ಯು’ ಎಂಬ ಪ್ರಸಿದ್ಧ ಗ್ರಾಮೀಣ ಕಥೆಯನ್ನು ರಚಿಸಿದವರು ಗೊರೂರು ರಾಮಸ್ವಾಮಿ ಐಯ್ಯಂಗಾರ್.",
    13: "ಭಾರತೀಪ್ರಿಯ (ರುದ್ರವೀಣೆ - iii), ಕೊಡಗಿನ ಗೌರಮ್ಮ (ಕಂಬನಿ - iv), ಚದುರಂಗ (ಶವದ ಮನೆ - ii), ಯು.ಆರ್. ಅನಂತಮೂರ್ತಿ (ಸೂರ್ಯನ ಕುದುರೆ - i).",
    14: "ಯಶೋಧರ ಚರಿತೆ (ಕಂದ - ii), ವೀರೇಶ್ವರ ಚರಿತೆ (ಷಟ್ಪದಿ - iii), ಯೋಗಾಂಗ ತ್ರಿವಿಧಿ (ತ್ರಿಪದಿ - iv), ಮೋಹನ ತರಂಗಿಣಿ (ಸಾಂಗತ್ಯ - i).",
    15: "“ನೀನ್ಯಾಕೋ ನಿನ್ನ ಹಂಗ್ಯಾಕೋ ನಿನ್ನ ನಾಮದ ಬಲವೊಂದಿದ್ದರೆ ಸಾಕೋ” ಎಂಬುದು ಕರ್ನಾಟಕ ಸಂಗೀತ ಪಿತಾಮಹ ಪುರಂದರದಾಸರ ಪ್ರಸಿದ್ಧ ಕೀರ್ತನೆಯಾಗಿದೆ.",
    16: "ದ್ವಿತೀಯಾ ವಿಭಕ್ತಿಯು ವ್ಯಾಕರಣದಲ್ಲಿ ಕ್ರಿಯೆಯ ಫಲವನ್ನು ಅನುಭವಿಸುವ ಕರ್ಮಾರ್ಥ (ಕರ್ಮ ಕಾರಕ) ಕಾರಕಾರ್ಥವನ್ನು ಬಯಸುತ್ತದೆ.",
    17: "ವಿರುದ್ಧ ಪದಗಳು: ವ್ಯಷ್ಟಿ × ಸಮಷ್ಟಿ (iv), ಲೇಪ × ನಿರ್ಲೇಪ (iii), ಮುಗ್ಧ × ಕಪಟ (i), ವಂದ್ಯ × ನಿಂದ್ಯ (ii). ಸಂಕೇತ: a-iv, b-iii, c-i, d-ii.",
    18: "‘ಈ ಕಿವಿಯಲ್ಲಿ ಕೇಳು, ಆ ಕಿವಿಯಲ್ಲಿ ಬಿಡು’ ಎಂಬ ನುಡಿಗಟ್ಟು ಕೇಳಿದ ವಿಷಯವನ್ನು ಗಮನಿಸದೆ ನಿರ್ಲಕ್ಷಿಸುವುದನ್ನು ಸೂಚಿಸುತ್ತದೆ.",
    19: "‘ಮನೀಷಿ’ ಎಂಬ ಸಂಸ್ಕೃತ ತತ್ಸಮ ಪದವು ಬುದ್ಧಿವಂತ, ಪಂಡಿತ, ವಿದ್ವಾಂಸ ಎಂಬ ಅರ್ಥವನ್ನು ನೀಡುತ್ತದೆ.",
    20: "ಗುಂಪಿಗೆ ಸೇರದ ಪದಗಳು: (a) ಯಲ್ಲಿ ಶರ್ವ (ಶಿವ; ಉಳಿದವು ಮನ್ಮಥ), (d) ಯಲ್ಲಿ ಶಾಂಡಿಲ್ಯ (ಋಷಿ; ಉಳಿದವು ಬಿಲ್ಲು). ಆದ್ದರಿಂದ (a) ಮತ್ತು (d) ಗುಂಪಿಗೆ ಸೇರಿಲ್ಲ.",
    21: "‘ನೀನ್’ (ನೀನು) ಎಂಬುದು ಎದುರಿಗಿರುವ ವ್ಯಕ್ತಿಯನ್ನು ಸಂಬೋಧಿಸುವ ದ್ವಿತೀಯ ಪುರುಷ / ಮಧ್ಯಮ ಪುರುಷ ಸರ್ವನಾಮವಾಗಿದೆ.",
    22: "ಊರಲ್ಲಿ (ಉಕಾರ ಲೋಪ - ii), ನಿನಗಲ್ಲದೆ (ಎಕಾರ ಲೋಪ - iv), ಕೈಯನ್ನು (ಯಕಾರಾಗಮ - i), ಗೋವಿಂದ (ವಕಾರಾಗಮ - iii). ಸಂಕೇತ: a-ii, b-iv, c-i, d-iii.",
    23: "ನಾವಿಕ -> ನಾವಿಗ (ಆವಿಕ ತಪ್ಪು), ಪಾರ್ಶ್ವ -> ಪಕ್ಕ/ಪಸ (ಪಂಚೆತ್ತು ತಪ್ಪು). ಆದ್ದರಿಂದ ಹೊಂದಾಣಿಕೆಯಾಗದ ಜೋಡಿಗಳು (a) ಮತ್ತು (d).",
    24: "ವಾಕ್ಯದಲ್ಲಿ ನೇರವಾಗಿ ಹೇಳದಿದ್ದರೂ ಸಂದರ್ಭಾನುಸಾರ ಅರ್ಥ ಪೂರ್ತಿಗಾಗಿ ಊಹಿಸಿ ಗ್ರಹಿಸುವ ಪದಸೇರ್ಪಡೆಗೆ ವ್ಯಾಕರಣದಲ್ಲಿ ‘ಅಧ್ಯಾಹಾರ’ ಎನ್ನುತ್ತಾರೆ.",
    25: "ದೇವನೂ, ಋಷಿಯೂ, ಧರ್ಮವೂ - ಎಲ್ಲ ಪೂರ್ವ ಮತ್ತು ಉತ್ತರ ಪದಗಳೂ ಪ್ರಧಾನವಾಗಿರುವ ಸಮಸ್ತ ಪದವು ದ್ವಂದ್ವ ಸಮಾಸವಾಗಿದೆ.",
    26: "ಕನ್ನಡ-ಸಂಸ್ಕೃತ ಬೆರೆಸಿದರೆ ಅರಿಸಮಾಸವೆಂಬ ನಿಯಮ ಹಾಗೂ ಪ್ರಾಚೀನ ಕವಿಪ್ರಯೋಗ, ಬಿರುದಾವಳಿ, ಗಮಕ/ಕ್ರಿಯಾಸಮಾಸಗಳಲ್ಲಿ ದೋಷವಿಲ್ಲವೆಂಬ ವಿನಾಯಿತಿ ಎರಡೂ ಸರಿ.",
    27: "ಹಳಗನ್ನಡದಲ್ಲಿ ‘ಕಾರ್ವಳ್’ (ಕಾರ್+ಒಳ್) ಪದವು ಗಾಢವಾದ ಕತ್ತಲು ಎಂಬ ಅರ್ಥವನ್ನು ಕೊಡುತ್ತದೆ.",
    28: "ದುರ್ಜನರು ನಿಂದಿಸುತ್ತಾರೆಂದು ಕವಿ ಕೃತಿ ರಚಿಸದೆ ಇರಲಾರನೆಂಬ ವಿಶೇಷವನ್ನು ಸಾಮಾನ್ಯ ಲೋಕನೀತಿಯಿಂದ ಸಮರ್ಥಿಸಿರುವುದರಿಂದ ಇದು ಅರ್ಥಾಂತರನ್ಯಾಸಾಲಂಕಾರ.",
    29: "ಪರಸ್ಪರ ಅವಲಂಬಿತ ಹಲವು ಉಪವಾಕ್ಯಗಳು ಪ್ರಧಾನ ವಾಕ್ಯದೊಡನೆ ಸೇರಿರುವುದರಿಂದ ಇದು ಸಂಯೋಜಿತ ವಾಕ್ಯವಾಗಿದೆ.",
    30: "ಸಂಧಿ ನಿಯಮದಂತೆ ಪೂರ್ಣ ಪದ ವಿಂಗಡಣೆ: ಅನುಜರು + ಅವರು + ಇರಲು + ಏಕೆ = ಅನುಜರವರಿರಲೇಕೆ (ಲೋಪ ಸಂಧಿ ಸರಣಿ).",
    31: "ಉತ್ತರ ಕರ್ನಾಟಕದ ಜನಪದ ಆಡುಭಾಷೆಯಲ್ಲಿ ‘ಸೊಲ/ಸೊಲಗು’ ಎಂದರೆ ಹಾಲು ಕರೆಯುವ ಎಮ್ಮೆ ಅಥವಾ ಆಕಳಿನ ಪಶುಧನವನ್ನು ಸೂಚಿಸುತ್ತದೆ.",
    32: "ಷಷ್ಠೀ ವಿಭಕ್ತಿಯು ಕೇವಲ ನಾಮಪದಗಳ ನಡುವಿನ ಸ್ವಾಮಿ-ಸೇವಕ, ಜನ್ಯ-ಜನಕ ಮುಂತಾದ ಸಂಬಂಧಾರ್ಥವನ್ನು ಹೇಳುವುದರಿಂದ ಇದಕ್ಕೆ ಸ್ವತಂತ್ರ ಕಾರಕಾರ್ಥವಿಲ್ಲ.",
    33: "ಸಂಬೋಧನೆ ಹಾಗೂ ಪ್ರಶ್ನಾರ್ಥಕ ರಚನೆಯಿರುವ ವಾಕ್ಯಕ್ಕೆ ಸರಿಯಾದ ಲೇಖನ ಚಿಹ್ನೆ: ಅಣ್ಣ, ಅಣ್ಣ, ಈ ಸಂಕಟವನ್ನು ಹೇಗೆ ನೋಡಲಿ?",
    34: "ಆ, ಕ, ಹ ಕಂಠ್ಯಗಳು ✔; ಡ, ರ, ಣ, ಷ ಮೂರ್ಧನ್ಯಗಳು ✔; (c) ಓಷ್ಠ್ಯಗಳು ಹಾಗೂ (d) ಮಿಶ್ರವರ್ಣಗಳಾಗಿರುವುದರಿಂದ ಕೇವಲ ಎರಡು ಹೇಳಿಕೆಗಳು ಸರಿಯಾಗಿವೆ.",
    35: "ಡಮರುಕ, ಮಲ್ಲಿಕಾ, ಭೂತಿ ತತ್ಸಮ ಪದಗಳು; ‘ಬಜಿ’ ಎಂಬುದು ದೇಶ್ಯ/ಅನ್ಯ ಶಬ್ದವಾಗಿರುವುದರಿಂದ ಗುಂಪಿಗೆ ಸೇರುವುದಿಲ್ಲ.",

    # Part B: General English (Q36 to Q70)
    36: "Future continuous tense ('will be working') expresses an action ongoing at a specified future reference point ('when I meet her next').",
    37: "Asylum is a Noun (ii), Ourselves is a Pronoun (iv), Scarcely is an Adverb (i), First is an Adjective (iii). Sequence: a-ii, b-iv, c-i, d-iii.",
    38: "In second conditional sentences (If + Past Simple), the main clause uses 'would + bare infinitive': 'I would be grateful to him'.",
    39: "Before specific official titles and formal meals: 'A dinner is organised by the President to the members'.",
    40: "General singular countable noun with generic reference takes 'A', while definite branch of mind takes 'the': 'A teacher should know the psychology'.",
    41: "'Adopt' means to legally take another's child as one's own; 'adapt' means to adjust, 'adept' means skilled.",
    42: "Logical syntactic sequence: The Uttar Pradesh Government's (R) -> move to withdraw charges against those (P) -> accused of lynching Person 'A' is (S) -> a brazen attack on rule of law and justice (Q).",
    43: "'Had we not been living...' is in the Past Perfect Continuous tense, making it the non-present tense form among the choices.",
    44: "Syntactic coherence: Mohan, the son of my friend who died in an accident (S), while working in Japan (R), gave me a set of pens (P) which is very precious (Q).",
    45: "The active voice of the future perfect passive ('will have been completed by the team') is 'The team will have completed the work by next week'.",
    46: "Correct prepositional collocations: arrive at a specific location ('at the station') and arrive timely ('just in time for boarding').",
    47: "A compound sentence connects two independent coordinate clauses with an adversative conjunction: 'I worked hard, yet did not succeed'.",
    48: "The coordinating conjunction 'for' functions as a literary equivalent of 'because', giving the reason why the boxer trained rigorously.",
    49: "Following a superlative adjective ('the greatest blessing'), standard grammar prescribes the relative pronoun 'that' rather than 'which'.",
    50: "Direct speech requires comma after reporting verb, opening capital letter inside quotation marks, and terminal question mark: The teacher said, \"Why are you shouting in the class?\"",
    51: "A phrase is a grammatically connected group of words that makes sense but does not express a complete thought (lacks subject-predicate nexus).",
    52: "The standard negative prefix attaching to the root 'bearable' is 'un-', producing 'unbearable' (incapable of being endured).",
    53: "Animal young matching: Frog - Tadpole (ii), Cow - Calf (iii), Swan - Signet/Cygnet (iv), Duck - Duckling (i). Sequence: a-ii, b-iii, c-iv, d-i.",
    54: "'Forlorn' denotes desolate, lonely, abandoned, or pitifully uncared for.",
    55: "The standard and correct English spelling is 'buffalo' (b-u-f-f-a-l-o).",
    56: "'Benevolent' signifies kind, charitable, and well-meaning; its direct antonym is 'cruel' or malicious.",
    57: "Animal offspring matching: Elephant - Calf (ii), Tiger - Cub (iii), Tortoise - Hatchling (iv), Horse - Foal (i). Sequence: a-ii, b-iii, c-iv, d-i.",
    58: "The idiomatic phrase 'at stake' means in danger of being lost, at risk, or in jeopardy.",
    59: "'To break the ice' means to initiate social interaction or begin a conversation to overcome initial awkwardness.",
    60: "The passage directly asserts that students engaging in pleasure reading perform better academically than those reading solely for exams.",
    61: "The text notes modern students are hindered by digital distractions and online gaming, implying they are bogged down by excessive connectivity.",
    62: "The passage explicitly discusses the curricular debate over whether schools should incorporate popular fiction or restrict time to academic texts.",
    63: "'Stationery' (with -ery) denotes writing materials and paper goods, whereas 'stationary' (with -ary) means immobile.",
    64: "'Squandered' means wasted or dissipated money, resources, or time foolishly and recklessly.",
    65: "'Megalomania' is a psychological condition characterized by delusional fantasies of wealth, power, and grandiose self-importance.",
    66: "The exclamation expressing victory, triumph, and collective rejoicing is 'Hurrah!'.",
    67: "The misspelt word is 'Asiduous'; the correct orthography requires double 's': 'Assiduous' (meaning diligent and persistent).",
    68: "Compound nouns modify the principal noun for pluralization: 'Daughters-in-law', and the plural of loaf with f-to-ves mutation is 'loaves'.",
    69: "When inquiring about an individual's personal identity as an author, the interrogative pronoun 'Who' is required: 'Who is your favourite author?'.",
    70: "The irregular adjective 'much' has comparative 'more' and superlative 'most'; 'mucher' and 'muchest' are grammatically invalid.",

    # Part C: Computer Knowledge (Q71 to Q100)
    71: "EDSAC, built by Maurice Wilkes at Cambridge in 1949, stands for Electronic Delay Storage Automatic Calculator.",
    72: "A Primary Key is a minimal superkey that uniquely identifies each individual record/tuple in a relational database table.",
    73: "Ray Tomlinson developed ARPANET's networked email application in 1971 and introduced the universal '@' addressing convention.",
    74: "Unicode provides a universal encoding standard for representing every character and script across global digital platforms.",
    75: "HTTP method mapping: GET reads resource (ii), HEAD fetches header only (iii), POST appends data (i), TRACE echoes request (v), CONNECT establishes tunnel (iv).",
    76: "In PowerPoint, text requires a placeholder/text box; pictures are inserted via Insert menu (b), toolbars toggled (c), and ink annotations drawn (d).",
    77: "Storage capacity hierarchy from smallest to largest: Registers (c) < Cache (d) < Main memory (b) < Magnetic disks (e) < Magnetic tapes (a).",
    78: "SoftMurmur (thesoftmurmur.com) is an ambient sound generator used by professionals to mask background noise and maintain focus.",
    79: "Browser development match: Google -> Chrome (iii), Microsoft -> Edge (iv), Apple -> Safari (i), Mozilla Foundation -> Firefox (ii).",
    80: "Both statements are correct: Black hat hackers intrude without authorization with malicious intent; White hat ethical hackers use identical tools legitimately.",
    81: "ChatGPT is a Large Language Model whose responses are probabilistically predicted based on user prompts and vast pre-trained transformer corpora.",
    82: "The Slide Master controls the top-level hierarchy, setting default typography, color themes, placeholders, and layouts for all presentation slides.",
    83: "DevOps is an operational and cultural methodology integrating software Development (Dev) and IT Operations (Ops) for continuous delivery.",
    84: "In a Man-in-the-Middle (MitM) session interception, the attacker eavesdrops on and tampers with credentials exchanged between client and banking server.",
    85: "Transferring and storing a file from a local client computer to a remote network server is called 'Uploading'.",
    86: "A system Bus provides the high-bandwidth parallel or high-speed serialized pathway for moving large data volumes between system components.",
    87: "Microsoft 365 includes Office apps (a), Teams collaboration (c), and MFA security (d); statement (b) is false as it includes 1 TB OneDrive cloud storage.",
    88: "In Microsoft Word Track Changes, 'No Markup' displays the finished document view with all revisions cleanly incorporated without inline markup bars.",
    89: "The world's first commercial notebook/laptop computer, the Epson HX-20 with built-in screen and keyboard, was released by Epson in 1981.",
    90: "Windows Vista was an operating system; Microsoft never released an office suite called 'Office Vista' (the contemporaneous suite was Office 2007).",
    91: "Dynamic named ranges in Excel are created through the 'Define Name' dialog using flexible dynamic formulas such as OFFSET() and COUNTA().",
    92: "Binary notation permits only bits 0 and 1; '1 0 2 1 1 1' contains the digit 2, making it an invalid binary representation.",
    93: "An Overlay Network is a virtual computer network layered on top of an underlying physical network infrastructure (e.g., VPNs, Tor, P2P).",
    94: "An 8-pin RJ45 connector is the standard physical termination interface used for Ethernet twisted-pair cabling in Local Area Networks (LAN).",
    95: "In the Domain Name System hierarchy, the top-level domain '.com' stands for 'commercial' business entities.",
    96: "Physical transmission impairments affecting signal fidelity across communication media include ambient noise (a) and signal attenuation (d).",
    97: "The baseline single-speed (1x) CD-ROM drive standard transfers data at an exact sustained rate of 150 KB/s (Kilobytes per second).",
    98: "Prior to its rebranding as Google Workspace in October 2020, Google's integrated enterprise productivity platform was named G-Suite.",
    99: "Application match: Microsoft Project manages schedules and budgets (ii), OneNote provides digital note taking (i), Access manages databases (iii).",
    100: "Internet of Things (IoT) sensor nodes are deployed to monitor physical ambient parameters (temperature, pressure, motion) and transmit data."
}

# Calculate statistics
total_q = len(items)
attempted = sum(1 for it in items if it['marked'] != 5)
correct = sum(1 for it in items if it['status'] == 'CORRECT')
wrong = sum(1 for it in items if it['status'] == 'WRONG')
unatt = sum(1 for it in items if it['status'] == 'UNANSWERED')
marks_pos = correct * 1.0
marks_neg = wrong * 0.25
net_score = marks_pos - marks_neg
accuracy = (correct / attempted * 100) if attempted > 0 else 0

# Sectional statistics
kan_items = items[0:35]
eng_items = items[35:70]
cmp_items = items[70:100]

def get_stats(sec_items):
    att = sum(1 for it in sec_items if it['marked'] != 5)
    c = sum(1 for it in sec_items if it['status'] == 'CORRECT')
    w = sum(1 for it in sec_items if it['status'] == 'WRONG')
    u = sum(1 for it in sec_items if it['status'] == 'UNANSWERED')
    net = c * 1.0 - w * 0.25
    acc = (c / att * 100) if att > 0 else 0
    return len(sec_items), att, c, w, u, net, acc

k_tot, k_att, k_c, k_w, k_u, k_net, k_acc = get_stats(kan_items)
e_tot, e_att, e_c, e_w, e_u, e_net, e_acc = get_stats(eng_items)
c_tot, c_att, c_c, c_w, c_u, c_net, c_acc = get_stats(cmp_items)

md = []
md.append("# KEA Village Administrative Officer (VAO) 2026 — Paper 2 (Language & Computer Knowledge) Evaluation Report\n")

md.append("| Examination Parameter | Candidate / Paper Record |")
md.append("| :--- | :--- |")
md.append("| **Examination** | KEA Village Administrative Officer (VAO / ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ) Competitive Examination 2026 |")
md.append("| **Department** | Department of Revenue (ಕಂದಾಯ ಇಲಾಖೆ), Government of Karnataka |")
md.append("| **Paper Name** | Paper 2: General Kannada, General English & Computer Knowledge (Afternoon Session) |")
md.append("| **Sections** | **Part A:** General Kannada (Q001–Q035)<br>**Part B:** General English (Q036–Q070)<br>**Part C:** Computer Knowledge (Q071–Q100) |")
md.append("| **Subject Code** | `NHKGA41026A` |")
md.append("| **Booklet Series** | **B1** |")
md.append("| **Total Questions** | 100 Multiple-Choice Questions |")
md.append("| **Maximum Marks** | 100.00 Marks |")
md.append("| **Marking Scheme** | +1.0 for Correct, -0.25 for Wrong / Multiple, 0.0 for Option (5) (Unattempted) |")
md.append("| **Evaluation Basis** | Official KEA answer key baseline, linguistic rules, computer science standards & verified solutions |\n")

md.append("## 1. Executive Performance Scorecard\n")

md.append("### Overall Paper 2 Performance")
md.append("| Metric | Count | Marks Contributed |")
md.append("| :--- | :--- | :--- |")
md.append(f"| **Total Questions in Paper** | **{total_q}** | — |")
md.append(f"| **Attempted (Options 1–4)** | **{attempted}** | — |")
md.append(f"| **Correct Answers** | **{correct}** | **+{marks_pos:.2f}** |")
md.append(f"| **Incorrect Answers** | **{wrong}** | **-{marks_neg:.2f}** |")
md.append(f"| **Unanswered (Option 5 Marked)** | **{unatt}** | **0.00** (Safe, no penalty) |")
md.append(f"| **Blank / Unmarked Questions** | **0** | **0.00** (100% OMR compliance) |")
md.append(f"| **NET TOTAL SCORE** | **—** | **`{net_score:.2f} / 100.00`** |")
md.append(f"| **Accuracy on Attempted** | **{accuracy:.2f}%** | — |\n")

md.append("### Section-Wise Performance Breakdown")
md.append("| Section / Subject | Questions | Attempted | Correct | Wrong | Unattempted | Accuracy | Net Marks Contributed |")
md.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
md.append(f"| **Part A: General Kannada** | 35 | {k_att} | {k_c} | {k_w} | {k_u} | {k_acc:.2f}% | **`{k_net:.2f} / 35.00`** |")
md.append(f"| **Part B: General English** | 35 | {e_att} | {e_c} | {e_w} | {e_u} | {e_acc:.2f}% | **`{e_net:.2f} / 35.00`** |")
md.append(f"| **Part C: Computer Knowledge** | 30 | {c_att} | {c_c} | {c_w} | {c_u} | {c_acc:.2f}% | **`{c_net:.2f} / 30.00`** |")
md.append(f"| **Total Paper 2** | **100** | **{attempted}** | **{correct}** | **{wrong}** | **{unatt}** | **{accuracy:.2f}%** | **`{net_score:.2f} / 100.00`** |\n")

md.append("### Combined Examination Merit Scorecard")
md.append("| Paper Component | Max Marks | Attempted | Correct | Wrong | Unanswered | Net Score Achieved |")
md.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
md.append("| **Paper 1: General Knowledge** | 100.00 | 80 | 47 | 33 | 20 | **`38.75 / 100.00`** |")
md.append(f"| **Paper 2: Language & Computers** | 100.00 | {attempted} | {correct} | {wrong} | {unatt} | **`{net_score:.2f} / 100.00`** |")
md.append(f"| **COMBINED MERIT TOTAL** | **200.00** | **{80 + attempted}** | **{47 + correct}** | **{33 + wrong}** | **{20 + unatt}** | **`{38.75 + net_score:.2f} / 200.00`** |\n")

md.append("> [!NOTE] Scoring Compliance & Option (5) Regulation")
md.append("> Marking Option (5) indicates an intentional decision to leave the question unanswered and incurs **zero penalty (0.00 marks)**. The candidate appropriately utilized Option (5) across 17 questions in Paper 2, completely avoiding negative penalties on doubtful questions.\n")

md.append("## 2. Question-by-Question Detailed Evaluation\n")
md.append("| Q# | Question ID | Question Summary | Marked | Key | Status | Marks | One-Line Reasoning / Solution |")
md.append("| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |")

for it in items:
    qn = it['q_num']
    qid = it['q_id']
    q_txt = it['question']
    marked_str = str(it['marked'])
    key_str = str(it['key'])
    status = it['status']
    marks = it['marks']
    marks_str = f"+{marks:.2f}" if marks > 0 else (f"{marks:.2f}" if marks < 0 else "0.00")
    
    if status == 'CORRECT':
        badge = "✅ `CORRECT`"
    elif status == 'WRONG':
        badge = "❌ `WRONG`"
    else:
        badge = "⚪ `UNANSWERED`"
        
    summary = q_txt
    if len(summary) > 75:
        summary = summary[:72].rstrip() + "..."
    summary = summary.replace('|', '/')
    
    exp = explanations.get(qn, f"Correct answer is option ({it['key']}).")
    exp = exp.replace('|', '/')
    
    md.append(f"| {qn} | `{qid}` | {summary} | `{marked_str}` | `{key_str}` | {badge} | {marks_str} | {exp} |")

md.append("\n---\n")
md.append("## 3. Sectional Analysis & Strategic Recommendations\n")

md.append("""### A. Domain Performance Breakdown

1. **Part A: General Kannada (`7.50 / 35.00` — Accuracy: 50.00%)**
   - **Strong Areas**: Sound understanding of Sandhi rules (Lopa, Agama, Prakrutibhava), basic Vibhakti/Karaka relationships, and Alankaras (Drishtanta, Arthantaranyasa).
   - **Improvement Areas**: Conservative attempt rate (15 questions left unattempted via Option 5). Questions covering classical Kannada literature (Janna, Raghavanka, classical metre like Ragale and Kanda) and medieval prose collections require systematic reinforcement.
   - **Vault Recommendation**: Revise `[[01_General_Kannada_Grammar_and_Vocabulary]]` and literature summary tables.

2. **Part B: General English (`30.00 / 35.00` — Accuracy: 88.57%)**
   - **Exceptional Strength**: Outstanding command over syntax, conditional clauses, voice conversion, prepositions, reading comprehension, idioms, and one-word substitutions (31 correct out of 35).
   - **Minor Slip-ups**: Isolated errors occurred in superlative relative pronoun conventions ('that' vs 'which'), active-to-passive nuances under time pressure, and specific antonym traps.
   - **Vault Recommendation**: Quick review of tricky pronoun and preposition exceptions in `[[02_General_English_Grammar_and_Composition]]`.

3. **Part C: Computer Knowledge (`24.25 / 30.00` — Accuracy: 89.29%)**
   - **Exceptional Strength**: Superior command over modern IT, networking protocols (HTTP, RJ45, Overlay networks), DevOps, Cloud platforms (M365, Google Workspace), and database concepts (Primary Keys) (25 correct out of 30).
   - **Minor Traps**: Missed historical computer models (Epson HX-20, 1981) and PowerPoint Slide Master definition versus Slide Sorter.
   - **Vault Recommendation**: Revisit MS Office hierarchy and computer hardware generations in `[[03_Computer_Knowledge_and_MS_Office]]`.

---

### B. Summary of Exam Strengths & Strategic Takeaways

- **Combined Merit Standing**: **`100.50 / 200.00`** represents a highly competitive benchmark for the KEA Village Administrative Officer (VAO) Group-C recruitment.
- **Asymmetric Strength**: The candidate exhibited elite performance in Paper 2's English and Computer sections (~89% accuracy), offsetting the cautious attempt rate in General Kannada and the challenging current-affairs penalty drag in Paper 1.
- **Option (5) Mastery**: Candidate demonstrated exemplary examination discipline with zero anti-tamper penalties (0 blank questions) and tactical neutral scoring across 37 total unattempted questions between both papers.
""")

with open('VAO/AGY/08_Paper_Review/Paper2_Evaluation.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

print("Successfully generated VAO/AGY/08_Paper_Review/Paper2_Evaluation.md")
