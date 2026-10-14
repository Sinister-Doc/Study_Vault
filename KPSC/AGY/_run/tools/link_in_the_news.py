import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_append, ROOT_DIR

def append_in_the_news():
    # 1. Drainage and Rivers note
    p1 = os.path.join(ROOT_DIR, "03_Notes", "03_Geography_Karnataka_and_World", "Karnataka_Drainage_and_River_Basins.md")
    if os.path.exists(p1):
        add1 = """

---

## 9. Recent Developments & In the News (2026 Updates)
- **Yettinahole Project Phase 1 Trial Run (Sept 2024 / 2026)**: Pumping operations inaugurated at Hebbanahalli (Sakleshpura), lifting floodwaters toward Vani Vilasa Sagara to benefit 7 drought-prone districts. (See [[2026-09_September#2-karnataka-schemes-welfare-programs--budgetfinance|September 2026 Digest]]).
- **Tungabhadra Dam Crest Gate No. 19 Chain Rupture (Aug 2024 / 2026)**: Emergency stop-log element barrier engineered within 6 days under expert N. Kannaiah Naidu, averting catastrophic water loss. (See [[2026-08_August#3-karnataka-economy-industry-infrastructure--agriculture|August 2026 Digest]]).
- **Cauvery CWSS Stage V Operationalisation (Oct 2024 / 2026)**: 775 MLD commissioned from TK Halli to serve 110 peripheral villages of Bengaluru. (See [[2026-10_October#3-karnataka-economy-industry-infrastructure--agriculture|October 2026 Digest]]).
"""
        with open(p1, "a", encoding="utf-8") as f:
            f.write(add1)
        print("Updated Karnataka_Drainage_and_River_Basins.md")

    # 2. Forests & Wildlife note
    p2 = os.path.join(ROOT_DIR, "03_Notes", "03_Geography_Karnataka_and_World", "Karnataka_Forests_Wildlife_and_Biodiversity.md")
    if os.path.exists(p2):
        add2 = """

---

## 10. Recent Developments & In the News (2026 Updates)
- **Addition of 3 New Ramsar Sites in Karnataka (Feb 2024 / 2026)**: Aghanashini Estuary (Uttara Kannada), Magadi Kere (Gadag), and Ankasamudra Bird Conservation Reserve (Vijayanagara) bring state total to 4 sites. (See [[2026-02_February#4-karnataka-environment-ecology-forests--water-resources|February 2026 Digest]]).
- **Western Ghats Landslide Vulnerability (July 2024 / 2026)**: Devastating landslides in Shirur (NH 66, Ankola) and Wayanad prompt GSI and KSDMA drone hazard micro-zonation across 10 Malnad districts. (See [[2026-07_July#3-karnataka-economy-industry-infrastructure--agriculture|July 2026 Digest]]).
"""
        with open(p2, "a", encoding="utf-8") as f:
            f.write(add2)
        print("Updated Karnataka_Forests_Wildlife_and_Biodiversity.md")

    # 3. Schemes note
    p3 = os.path.join(ROOT_DIR, "04_Current_Affairs_GK", "02_Karnataka_State_Schemes_and_Policies", "State_Flagship_Schemes.md")
    if os.path.exists(p3):
        add3 = """

---

## 7. Recent Developments & In the News (2026 Updates)
- **Karnataka Platform-Based Gig Workers Bill 2024 / 2026**: Tabled in state assembly; mandates 1-2% welfare fee per transaction and algorithmic transparency. (See [[2026-03_March#1-karnataka-state-polity-administration--governance|March 2026 Digest]]).
- **Five Guarantees 1-Year Financial Review**: Over ₹52,000 Crore allocated in Budget 2024-25; Gruha Lakshmi disbursing ₹2,000/mo to 1.18 cr women; Shakti crossing 220 cr zero-fare trips. (See [[2026-02_February#2-karnataka-schemes-welfare-programs--budget-outlays|February 2026 Digest]]).
"""
        with open(p3, "a", encoding="utf-8") as f:
            f.write(add3)
        print("Updated State_Flagship_Schemes.md")

if __name__ == "__main__":
    append_in_the_news()
