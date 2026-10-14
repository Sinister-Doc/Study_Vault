import os
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_mkdir, safe_move, safe_write, ROOT_DIR

HIST_DIR = os.path.join(ROOT_DIR, "03_Notes", "01_Karnataka_History_and_Culture")
GEO_DIR = os.path.join(ROOT_DIR, "03_Notes", "03_Geography_Karnataka_and_World")

def run_reorganisation():
    print("=== Executing Workstream C: Reorganise History & Geography Notes ===")

    # 1. Create target directories
    hist_textbook_dir = safe_mkdir(os.path.join(HIST_DIR, "01_Textbook_Notes"))
    hist_quick_dir = safe_mkdir(os.path.join(HIST_DIR, "Quick_Revision"))
    geo_textbook_dir = safe_mkdir(os.path.join(GEO_DIR, "01_Textbook_Notes"))
    geo_quick_dir = safe_mkdir(os.path.join(GEO_DIR, "Quick_Revision"))

    # 2. History Quick Revision moves and alias injection
    hist_quick_moves = [
        ("Early_Karnataka_Dynasties.md", "Early Karnataka Dynasties - Quick Revision.md", ["Early_Karnataka_Dynasties", "Early Karnataka Dynasties"]),
        ("Vijayanagara_and_Mysore_Kingdom.md", "Vijayanagara and Mysore Kingdom - Quick Revision.md", ["Vijayanagara_and_Mysore_Kingdom", "Vijayanagara and Mysore Kingdom"]),
        ("Freedom_Struggle_in_Karnataka.md", "Freedom Struggle in Karnataka - Quick Revision.md", ["Freedom_Struggle_in_Karnataka", "Freedom Struggle in Karnataka"]),
        ("Karnataka_Unification_and_Social_Movements.md", "Karnataka Unification and Social Movements - Quick Revision.md", ["Karnataka_Unification_and_Social_Movements", "Karnataka Unification and Social Movements"])
    ]

    for src_name, dst_name, aliases in hist_quick_moves:
        src_path = os.path.join(HIST_DIR, src_name)
        dst_path = os.path.join(hist_quick_dir, dst_name)
        if os.path.exists(src_path):
            # Inject aliases into frontmatter
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
            alias_str = "aliases: [" + ", ".join([f'"{a}"' for a in aliases]) + "]\n"
            if "aliases:" not in content and content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = "---" + parts[1].rstrip() + "\n" + alias_str + "---" + parts[2]
                    safe_write(src_path, content)

            safe_move(src_path, dst_path)
            print(f"Moved History Quick Revision: {src_name} -> Quick_Revision/{dst_name}")

    # 3. History Textbook Notes moves
    hist_textbook_files = [
        "Prehistory_and_Protohistory_Karnataka.md",
        "Early_Dynasties_Kadambas_and_Gangas.md",
        "Badami_Chalukyas_Architecture_and_Empire.md",
        "Rashtrakutas_of_Manyakheta_and_Kavirajamarga.md",
        "Kalyana_Chalukyas_Kalachuris_and_Vachana_Movement.md",
        "Hoysalas_of_Dwarasamudra_and_Seunas.md",
        "Vijayanagara_Empire_Polity_and_Culture.md",
        "Bahmani_and_Adil_Shahi_Sultanates.md",
        "Nayakas_of_Keladi_and_Chitradurga.md",
        "Mysore_Kingdom_Wodeyars_and_Dewans.md",
        "Freedom_Struggle_and_Armed_Revolts_in_Karnataka.md",
        "Karnataka_Unification_Social_Reforms_and_Culture.md"
    ]

    for fn in hist_textbook_files:
        src_path = os.path.join(HIST_DIR, fn)
        dst_path = os.path.join(hist_textbook_dir, fn)
        if os.path.exists(src_path):
            safe_move(src_path, dst_path)
            print(f"Moved History Textbook Note: {fn} -> 01_Textbook_Notes/{fn}")

    # 4. Geography Quick Revision moves and alias injection
    geo_quick_moves = [
        ("Karnataka_Physiography_and_Rivers.md", "Karnataka Physiography and Rivers - Quick Revision.md", ["Karnataka_Physiography_and_Rivers", "Karnataka Physiography and Rivers"])
    ]

    for src_name, dst_name, aliases in geo_quick_moves:
        src_path = os.path.join(GEO_DIR, src_name)
        dst_path = os.path.join(geo_quick_dir, dst_name)
        if os.path.exists(src_path):
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
            alias_str = "aliases: [" + ", ".join([f'"{a}"' for a in aliases]) + "]\n"
            if "aliases:" not in content and content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = "---" + parts[1].rstrip() + "\n" + alias_str + "---" + parts[2]
                    safe_write(src_path, content)

            safe_move(src_path, dst_path)
            print(f"Moved Geography Quick Revision: {src_name} -> Quick_Revision/{dst_name}")

    # 5. Geography Textbook Notes moves
    geo_textbook_files = [
        "Karnataka_Location_Physiography_and_Geology.md",
        "Karnataka_Drainage_and_River_Basins.md",
        "Karnataka_Climate_and_Rainfall_Patterns.md",
        "Karnataka_Soils_and_Land_Degradation.md",
        "Karnataka_Forests_Wildlife_and_Biodiversity.md",
        "Karnataka_Agro_Climatic_Zones_and_Agriculture.md",
        "Karnataka_Mineral_Resources_and_Energy.md",
        "Karnataka_Demography_Urbanisation_and_Infrastructure.md",
        "World_Physical_Geography.md"
    ]

    for fn in geo_textbook_files:
        src_path = os.path.join(GEO_DIR, fn)
        dst_path = os.path.join(geo_textbook_dir, fn)
        if os.path.exists(src_path):
            safe_move(src_path, dst_path)
            print(f"Moved Geography Textbook Note: {fn} -> 01_Textbook_Notes/{fn}")

    # 6. Create Subject Hubs
    create_history_hub()
    create_geography_hub()

def create_history_hub():
    hub_path = os.path.join(HIST_DIR, "Karnataka_History_Hub.md")
    hub_content = """---
title: Karnataka History and Culture Master Hub (ಕರ್ನಾಟಕ ಇತಿಹಾಸ ಮತ್ತು ಸಂಸ್ಕೃತಿ)
syllabus_refs: [P1-S2.1, P1-S2.2, M-GS1-S1.1, M-GS1-S1.2, M-GS1-S1.3, M-GS1-S1.4, M-GS1-S1.5]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources:
  - "Dr. Suryanath Kamath, A Concise History of Karnataka"
  - "Karnataka State Textbooks (KTBS) - 1st & 2nd PUC History"
  - "KPSC Official Syllabus & Gazetted Probationers Notification"
priority: hub
---

# Karnataka History and Culture Master Subject Hub
**ಕರ್ನಾಟಕ ಇತಿಹಾಸ ಮತ್ತು ಸಂಸ್ಕೃತಿ ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶಿ**

This hub connects the comprehensive **Textbook-Depth Master Notes** (for in-depth Mains analysis and conceptual mastery) with the **Quick Revision Sheets** (for rapid Prelims revision and last-minute fact recall).

---

## 1. Topic-by-Topic Comparative Syllabus Navigator

| Syllabus Module & Historical Era | Textbook-Depth Master Chapter (2,000–3,500+ Words) | Quick Revision Sheet (Fast Recall) | Core Examination Focus & Primary Evidence |
| :--- | :--- | :--- | :--- |
| **Prehistory & Ashokan Edicts** | [[Prehistory_and_Protohistory_Karnataka]] | [[Early Karnataka Dynasties - Quick Revision]] | Maski edict (Devanampriya Asoka), Brahmagiri, Sanganakallu ash mounds, Kupgal petroglyphs. |
| **Early Dynasties: Kadambas & Gangas** | [[Early_Dynasties_Kadambas_and_Gangas]] | [[Early Karnataka Dynasties - Quick Revision]] | Mayurasharma, Talagunda pillar inscription, Halmidi inscription (450 CE), Ganga Talakadu polity. |
| **Imperial Badami Chalukyas** | [[Badami_Chalukyas_Architecture_and_Empire]] | [[Early Karnataka Dynasties - Quick Revision]] | Pulakeshin II, Ravikirti's Aihole Prashasti (634 CE), Narmada battle, Badami rock-cut cave temples. |
| **Rashtrakutas of Manyakheta** | [[Rashtrakutas_of_Manyakheta_and_Kavirajamarga]] | [[Early Karnataka Dynasties - Quick Revision]] | Amoghavarsha Nrupatunga, *Kavirajamarga* (850 CE), Ellora Kailasanatha temple, Sulaiman travelogues. |
| **Kalyana Chalukyas & Vachana Movement** | [[Kalyana_Chalukyas_Kalachuris_and_Vachana_Movement]] | [[Early Karnataka Dynasties - Quick Revision]] | Tailapa II, Vikramaditya VI (Vikrama Era 1076), Basaveshwara, Anubhava Mantapa, Sharana revolution. |
| **Hoysalas of Dwarasamudra & Seunas** | [[Hoysalas_of_Dwarasamudra_and_Seunas]] | [[Early Karnataka Dynasties - Quick Revision]] | Vishnuvardhana, Belur Chennakeshava, Halebidu Hoysaleshwara (UNESCO 2023), Vesara architecture. |
| **Vijayanagara Empire: Polity & Art** | [[Vijayanagara_Empire_Polity_and_Culture]] | [[Vijayanagara and Mysore Kingdom - Quick Revision]] | Sangama to Aravidu, Krishnadevaraya (*Amuktamalyada*), Nayankara system, Hampi monuments. |
| **Bahmani & Adil Shahi Sultanates** | [[Bahmani_and_Adil_Shahi_Sultanates]] | [[Vijayanagara and Mysore Kingdom - Quick Revision]] | Mahmud Gawan Bidar Madrasa, Ibrahim Adil Shah II (*Kitab-i-Navras*), Gol Gumbaz whispering gallery. |
| **Nayakas of Keladi & Chitradurga** | [[Nayakas_of_Keladi_and_Chitradurga]] | [[Vijayanagara and Mysore Kingdom - Quick Revision]] | Shivappa Nayaka *Sistu* land revenue, Rani Chennamma, Madakari Nayaka, Onake Obavva heroism. |
| **Mysore Kingdom: Wodeyars & Dewans** | [[Mysore_Kingdom_Wodeyars_and_Dewans]] | [[Vijayanagara and Mysore Kingdom - Quick Revision]] | Chikka Devaraja Wodeyar, Hyder-Tipu Anglo-Mysore wars, Krishnaraja Wodeyar IV, Sir MV, Mirza Ismail. |
| **Freedom Struggle & Armed Resistance** | [[Freedom_Struggle_and_Armed_Revolts_in_Karnataka]] | [[Freedom Struggle in Karnataka - Quick Revision]] | Kittur Chennamma (1824), Sangolli Rayanna, Halagali Bedas, Belagavi INC 1924, Vidurashwatha, Isur. |
| **Unification & Social Movements** | [[Karnataka_Unification_Social_Reforms_and_Culture]] | [[Karnataka Unification and Social Movements - Quick Revision]] | Alur Venkata Rao, Fazal Ali SRC (1956), Renaming 1973, Land reforms 1974, DSS, KRRS, Gokak agitation. |

---

## 2. Interactive Mock Tests & Practice Drills
- **Dedicated Subject Drill**: [[06_Mock_Tests/CBT_Sectional_Karnataka_History.html|CBT Sectional Mock — Karnataka History (50 Qs)]]
- **Companion Key & Rationale**: [[CBT_Sectional_Karnataka_History_Key]]
"""
    safe_write(hub_path, hub_content)
    print("Created Karnataka_History_Hub.md")

def create_geography_hub():
    hub_path = os.path.join(GEO_DIR, "Karnataka_Geography_Hub.md")
    hub_content = """---
title: Karnataka and World Geography Master Hub (ಕರ್ನಾಟಕ ಮತ್ತು ವಿಶ್ವ ಭೂಗೋಳಶಾಸ್ತ್ರ)
syllabus_refs: [P1-S2.3, P1-S2.4, M-GS2-S1.1, M-GS2-S1.2, M-GS3-S3.1]
syllabus_refs_partial: []
last_verified: 2026-10-13
sources:
  - "NCERT Physical Geography Class XI & XII"
  - "Karnataka State Textbooks (KTBS) - Geography"
  - "ISFR 2021 & Karnataka State of Environment Report"
priority: hub
---

# Karnataka and World Geography Master Subject Hub
**ಕರ್ನಾಟಕ ಮತ್ತು ವಿಶ್ವ ಭೂಗೋಳಶಾಸ್ತ್ರ ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶಿ**

This hub integrates the **Textbook-Depth Master Notes** for physical, economic, and human geography with the **Quick Revision Sheets** for high-yield map and fact recall.

---

## 1. Topic-by-Topic Comparative Syllabus Navigator

| Geography Domain | Textbook-Depth Master Chapter (2,000–3,500+ Words) | Quick Revision Sheet (Fast Recall) | Core Examination Focus & Spatial Data |
| :--- | :--- | :--- | :--- |
| **Physiography & Geology** | [[Karnataka_Location_Physiography_and_Geology]] | [[Karnataka Physiography and Rivers - Quick Revision]] | Karavali coastline (320 km), Malnad (Mullayanagiri 1,925m), Northern/Southern Maidan, Dharwar craton. |
| **Drainage & River Basins** | [[Karnataka_Drainage_and_River_Basins]] | [[Karnataka Physiography and Rivers - Quick Revision]] | Krishna basin (Upper Krishna, Almatti 519.6m, Tungabhadra), Cauvery basin (KRS, Kabini, CWMA), west-flowing rivers. |
| **Climate & Rainfall** | [[Karnataka_Climate_and_Rainfall_Patterns]] | [[Karnataka Physiography and Rivers - Quick Revision]] | Tropical monsoon, Agumbe/Amagaon orographic rainfall, interior rain-shadow drought vulnerability. |
| **Soils & Land Degradation** | [[Karnataka_Soils_and_Land_Degradation]] | [[Karnataka Physiography and Rivers - Quick Revision]] | Red sandy/loamy (50%), Black cotton *Regur* (27%), Laterite soils, saline-alkali reclamation, watersheds. |
| **Forests & Biodiversity** | [[Karnataka_Forests_Wildlife_and_Biodiversity]] | [[Karnataka Physiography and Rivers - Quick Revision]] | 20.11% forest cover (ISFR), 5 Tiger Reserves, 5 Ramsar sites (Magadi, Aghanashini, Ankasamudra), Western Ghats. |
| **Agro-Climatic Zones & Agriculture** | [[Karnataka_Agro_Climatic_Zones_and_Agriculture]] | [[Karnataka Physiography and Rivers - Quick Revision]] | 10 NARP agro-climatic zones, millets (*Ragi*, *Jowar*), horticulture, micro-irrigation, *Raitha Siri*. |
| **Minerals & Energy** | [[Karnataka_Mineral_Resources_and_Energy]] | [[Karnataka Physiography and Rivers - Quick Revision]] | Sandur/Kudremukh iron ore, Pavagada Solar Park (2,050 MW), wind corridors, Sharavathi pumped storage. |
| **Demography & Infrastructure** | [[Karnataka_Demography_Urbanisation_and_Infrastructure]] | [[Karnataka Physiography and Rivers - Quick Revision]] | 2011 Census (6.11 cr, 75.36% lit, 973 sex ratio, 38.67% urban), Greater Bengaluru, Namma Metro, NH corridors. |
| **World Physical Geography** | [[World_Physical_Geography]] | — | Plate tectonics, ocean currents, pressure belts, monsoons, geomorphology, UNCLOS zones. |

---

## 2. Interactive Mock Tests & Practice Drills
- **Dedicated Subject Drill**: [[06_Mock_Tests/CBT_Sectional_Karnataka_Geography.html|CBT Sectional Mock — Karnataka Geography (50 Qs)]]
- **Companion Key & Rationale**: [[CBT_Sectional_Karnataka_Geography_Key]]
"""
    safe_write(hub_path, hub_content)
    print("Created Karnataka_Geography_Hub.md")

if __name__ == "__main__":
    run_reorganisation()
