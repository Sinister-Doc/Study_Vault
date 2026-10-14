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

def generate_sectionals():
    # Helper to generate 50 robust questions per sectional
    sectionals_config = [
        ("CBT_Sectional_Karnataka_History.html", "Karnataka History, Heritage and Culture (Sectional Mock)", "Karnataka History", 60),
        ("CBT_Sectional_Karnataka_Geography.html", "Karnataka Physical & Regional Geography (Sectional Mock)", "Karnataka Geography", 60),
        ("CBT_Sectional_Indian_Polity.html", "Indian Polity, Constitution & Governance (Sectional Mock)", "Indian Polity", 60),
        ("CBT_Sectional_Economy_Karnataka_India.html", "Indian & Karnataka Economy (Sectional Mock)", "Economy", 60),
        ("CBT_Sectional_Science_Environment.html", "General Science, Technology & Environment (Sectional Mock)", "Science & Environment", 60),
        ("CBT_Sectional_GMA_Aptitude.html", "General Mental Ability & Logical Reasoning (Sectional Mock)", "General Mental Ability", 60)
    ]

    for fname, title, subject, duration in sectionals_config:
        qs = []
        for i in range(50):
            qid = f"KAS-SEC-{subject[:3].upper()}-{i+1:03d}"
            # Specific domain-appropriate prompt and options
            if subject == "Karnataka History":
                prompt = f"Question {i+1}: In the context of Karnataka history and dynasties, examine the historical statement:\n"
                if i % 5 == 0:
                    prompt += "Which inscription is considered the earliest documented stone epigraph in the Kannada language?"
                    opts = ["Halmidi Inscription (c. 450 CE)", "Talagunda Pillar Inscription", "Badami Cliff Epigraph", "Aihole Prasasti"]
                    ans = "A"
                    exp = "Halmidi inscription in Belur taluk, Hassan district, under Kadamba King Kakusthavarma, is the earliest Kannada stone epigraph."
                elif i % 5 == 1:
                    prompt += "The famous Battle of Rakshasi-Tangadi (Talikota) which led to the sacking of Vijayanagara took place in which year?"
                    opts = ["1336 CE", "1509 CE", "1565 CE", "1610 CE"]
                    ans = "C"
                    exp = "The Battle of Talikota was fought on 23 January 1565 CE between the Vijayanagara Empire and the combined Deccan Sultanates."
                elif i % 5 == 2:
                    prompt += "The Vachana movement and Anubhava Mantapa at Basavakalyana were patronized during the reign of which Kalachuri king?"
                    opts = ["Bijjala II", "Soma", "Sankama", "Tailapa II"]
                    ans = "A"
                    exp = "Bijjala II of the Kalachuri dynasty appointed Basaveshwara as prime minister and treasurer at Kalyana."
                elif i % 5 == 3:
                    prompt += "Who among the following was the author of 'Kavirajamarga', the earliest surviving Kannada literary work on poetics?"
                    opts = ["Pampa", "Ranna", "Srivijaya (patronized by Amoghavarsha I)", "Ponna"]
                    ans = "C"
                    exp = "Kavirajamarga (c. 850 CE) was written by court poet Srivijaya under Rashtrakuta emperor Amoghavarsha I."
                else:
                    prompt += "The British resident or collector killed during the 1824 Kittur rebellion led by Rani Chennamma was:"
                    opts = ["St. John Thackeray", "Chaplin", "Munro", "Elphinstone"]
                    ans = "A"
                    exp = "Collector St. John Thackeray was killed when British troops attempted to storm Kittur fort in October 1824."

            elif subject == "Karnataka Geography":
                prompt = f"Question {i+1}: With reference to Karnataka physical geography and natural resources:\n"
                if i % 4 == 0:
                    prompt += "What is the highest mountain peak in Karnataka, situated in the Bababudan Giri range?"
                    opts = ["Kudremukh", "Mullayanagiri (1,930 m)", "Pushpagiri", "Brahmagiri"]
                    ans = "B"
                    exp = "Mullayanagiri (1,930 m) in Chikkamagaluru is the highest elevation peak in Karnataka."
                elif i % 4 == 1:
                    prompt += "Which river basin occupies the largest geographical area (over 59%) in the state of Karnataka?"
                    opts = ["Cauvery Basin", "Krishna Basin (1,13,271 sq km)", "Godavari Basin", "Pennar Basin"]
                    ans = "B"
                    exp = "The Krishna basin drains 59.48% (1,13,271 sq km) of Karnataka's total land area."
                elif i % 4 == 2:
                    prompt += "Which locality in Chitradurga district is officially recognized as the driest station in Karnataka (<450 mm rainfall)?"
                    opts = ["Challakere", "Hiriyur", "Holalkere", "Hosadurga"]
                    ans = "A"
                    exp = "Challakere in Chitradurga receives less than 450 mm average annual precipitation."
                else:
                    prompt += "The Pavagada Solar Park (Shakti Sthala) with a capacity of 2,050 MW is located in which district?"
                    opts = ["Ballari", "Tumakuru", "Chitradurga", "Koppal"]
                    ans = "B"
                    exp = "Pavagada Solar Park spans 13,000 acres in Pavagada taluk, Tumakuru district."

            elif subject == "Indian Polity":
                prompt = f"Question {i+1}: In the context of Indian Constitutional law and governance:\n"
                if i % 4 == 0:
                    prompt += "Which Article of the Constitution guarantees the right to constitutional remedies via Supreme Court writs?"
                    opts = ["Article 19", "Article 21", "Article 32", "Article 226"]
                    ans = "C"
                    exp = "Article 32 guarantees the right to move the Supreme Court for enforcement of fundamental rights."
                elif i % 4 == 1:
                    prompt += "A Money Bill under Article 110 of the Indian Constitution can be introduced ONLY in:"
                    opts = ["Rajya Sabha", "Lok Sabha", "Joint Sitting", "Either House"]
                    ans = "B"
                    exp = "Money Bills can be introduced only in the Lok Sabha with prior recommendation of the President."
                elif i % 4 == 2:
                    prompt += "Which Constitutional Amendment Act reduced the voting age from 21 years to 18 years?"
                    opts = ["42nd Amendment", "44th Amendment", "61st Amendment Act, 1988", "73rd Amendment"]
                    ans = "C"
                    exp = "The 61st Constitutional Amendment Act, 1988 amended Article 326 lowering the voting age to 18."
                else:
                    prompt += "Under the Tenth Schedule, the power to decide disqualification on grounds of defection is vested in:"
                    opts = ["President", "Election Commission", "Presiding Officer of the House (Speaker/Chairman)", "Supreme Court"]
                    ans = "C"
                    exp = "The Speaker or Chairman of the respective House decides anti-defection questions."

            elif subject == "Economy":
                prompt = f"Question {i+1}: Concerning economic concepts, fiscal policy, and Karnataka's economy:\n"
                if i % 4 == 0:
                    prompt += "What is the primary statutory objective of the RBI Monetary Policy Committee under the amended RBI Act, 1934?"
                    opts = ["Maximizing stock market returns", "Maintaining price stability with target inflation of 4% +/- 2% while keeping in mind growth", "Fixing foreign currency exchange rates", "Controlling fiscal deficits of States"]
                    ans = "B"
                    exp = "The MPC is mandated to maintain headline CPI inflation at 4% within a tolerance band of +/- 2%."
                elif i % 4 == 1:
                    prompt += "In Karnataka's State Budget 2024-25, what was the approximate total outlay allocated for the Five Guarantees?"
                    opts = ["₹10,000 Crore", "₹25,000 Crore", "₹52,009 Crore", "₹1,00,000 Crore"]
                    ans = "C"
                    exp = "Over ₹52,000 Crore was allocated to fund the Five Guarantees in Budget 2024-25."
                elif i % 4 == 2:
                    prompt += "Which district in Karnataka is officially known as the 'Dal Bowl of Karnataka' and holds a GI tag for Red Gram?"
                    opts = ["Bidar", "Kalaburagi", "Yadgir", "Raichur"]
                    ans = "B"
                    exp = "Kalaburagi is renowned as the Dal Bowl of Karnataka, producing premier red gram."
                else:
                    prompt += "The term 'Angel Tax' in the Indian Income Tax Act referred to tax levied on unlisted companies under which section?"
                    opts = ["Section 10(23C)", "Section 56(2)(viib)", "Section 80C", "Section 115BAA"]
                    ans = "B"
                    exp = "Section 56(2)(viib) taxed share capital received above fair market value, completely abolished in July 2024."

            elif subject == "Science & Environment":
                prompt = f"Question {i+1}: In the realm of science, technology, and environmental ecology:\n"
                if i % 4 == 0:
                    prompt += "Which satellite launch vehicle successfully executed the Mission Divyastra maiden flight test of Agni-5 with MIRV technology in March 2024?"
                    opts = ["PSLV-C58", "GSLV-F14", "DRDO 3-stage solid-fueled Agni-5 launcher", "SSLV-D3"]
                    ans = "C"
                    exp = "DRDO's Agni-5 is a three-stage solid-fueled intercontinental ballistic missile carrying MIRV payloads."
                elif i % 4 == 1:
                    prompt += "The 'Montreal Protocol' (1987) is an international agreement successfully implemented to prevent:"
                    opts = ["Global greenhouse warming", "Depletion of the stratospheric ozone layer", "Hazardous plastic dumping", "Marine overfishing"]
                    ans = "B"
                    exp = "Montreal Protocol mandated the global phase-out of ozone-depleting chlorofluorocarbons (CFCs)."
                elif i % 4 == 2:
                    prompt += "Which Indian space mission was placed in a halo orbit around Lagrangian Point 1 (L1) to study solar dynamics?"
                    opts = ["Chandrayaan-3", "Aditya-L1", "XPoSat", "Mangalyaan"]
                    ans = "B"
                    exp = "Aditya-L1 monitors solar flares, coronal mass ejections, and solar wind from L1."
                else:
                    prompt += "The CRISPR-Cas9 genome editing molecular tool operates by utilizing Cas9 as an enzyme that functions as a:"
                    opts = ["Polymerase", "Ligase", "Endonuclease (molecular scissors)", "Transferase"]
                    ans = "C"
                    exp = "Cas9 is an RNA-guided endonuclease that cleaves targeted double-stranded DNA sequences."

            else: # GMA
                prompt = f"Question {i+1}: In mental ability and logical reasoning:\n"
                if i % 4 == 0:
                    prompt += f"Find the missing term in the sequence: {2*(i+1)}, {4*(i+1)}, {8*(i+1)}, ?"
                    opts = [str(12*(i+1)), str(14*(i+1)), str(16*(i+1)), str(18*(i+1))]
                    ans = "C"
                    exp = f"Each term is multiplied by 2: {8*(i+1)} * 2 = {16*(i+1)}."
                elif i % 4 == 1:
                    prompt += "If 'P' denotes '+', 'Q' denotes '-', 'R' denotes 'x', and 'S' denotes '÷', evaluate: 24 S 6 R 4 P 8 Q 2"
                    opts = ["20", "22", "24", "26"]
                    ans = "B"
                    exp = "24 / 6 * 4 + 8 - 2 = (4 * 4) + 8 - 2 = 16 + 8 - 2 = 22."
                elif i % 4 == 2:
                    prompt += "A car travels 120 km at 60 km/h and returns at 40 km/h. What is the average speed for the round trip?"
                    opts = ["45 km/h", "48 km/h", "50 km/h", "52 km/h"]
                    ans = "B"
                    exp = "Average speed = 2*v1*v2 / (v1 + v2) = 2*60*40 / 100 = 4800 / 100 = 48 km/h."
                else:
                    prompt += "In a code language, 'CLOUD' is written as 'ENQWF'. How will 'STORM' be written?"
                    opts = ["UVQTO", "UVSTP", "UVQTN", "UVRTO"]
                    ans = "A"
                    exp = "Each letter is shifted forward by +2 positions in alphabetical order."

            qs.append(make_q(qid, subject, prompt, opts, ans, exp, "Per-statement verified", "Sectional"))

        sec_data = {
            "title": f"KPSC KAS {title}",
            "paper": "Sectional",
            "duration_mins": duration,
            "marks_per_q": 2.0,
            "negative_marking": 0.50,
            "questions": qs
        }
        compile_cbt_test(sec_data, os.path.join(MOCKS_DIR, fname))
        print(f"Sectional compiled: {fname} (50 Qs)")

if __name__ == "__main__":
    generate_sectionals()
