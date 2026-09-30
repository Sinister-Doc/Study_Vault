---
exam: KEA Land Surveyor 2026
subject: Coverage audit of the AGY notes against the notified syllabus
last_updated: 2026-09-29
document_type: Audit + syllabus-to-note map
---

# 02b. Notified Syllabus → Note Map, Coverage Score & Placement Guide

> [!WARNING] Read this first
> The Paper-II syllabus in the KEA notification is **not** classical surveying (chain, compass, levelling, theodolite, curves). It is **Mathematics 40 + Modern Methods of Surveying 20 + Computer Applications 20 + Physics 10 + Geography 10**.
> Your existing `02_Syllabus_and_Pattern.md` and notes `03_Notes/01–07` are built on a different assumption. They are good notes, but on this syllabus they will earn few marks. Treat them as **low priority / only if time remains**.

**Exam schedule (revised):** 2 Oct 2026 — Paper-I 10:30–12:30, Paper-II 2:30–4:30 (per the revised KEA notice reported on Testbook; confirm on your hall ticket).

**Source caveat:** the syllabus pages you uploaded end in the middle of "Modern Methods of Surveying". I took Computer Applications, Physics, Geography and the Paper-I list from a syllabus page that reproduces the notification (Toppersexam). Compare those parts with the remaining pages of your notification PDF.

---

## 1. Paper-II map (100 marks)

| Notified section | Marks | Where covered (old notes) | New note added | Old coverage | New coverage (est.) |
| :--- | :---: | :--- | :--- | :---: | :---: |
| **A. Mathematics** — arithmetic, algebra, geometry | 40 | `09` (areas, coordinate geometry only) | `11`, `12`, `13` | ~5% | ~75% |
| **B. Modern Methods** — photogrammetry, drones, satellite imagery, RS, GPS, GIS, advanced GNSS/CORS | 20 | `08` (GPS basics, RS resolutions, raster/vector) | `14`, `15`, `16` | ~40% | ~85% |
| **C. Computer Applications** — MS Office, AutoCAD/DXF, GIS software, SDLC, APIs, land-records IT | 20 | `10` (Bhoomi/Mojini/Dishank) | `17`, `18`, `19` | ~10% | ~70% |
| **D. Physics** — magnetism to gravitation | 10 | `04` GK note, `09` (gravitation only) | `20` | ~20% | ~75% |
| **E. Geography** — Earth, lithosphere, maps, physical India | 10 | `02` (Karnataka-heavy) | `21` | ~25% | ~75% |
| **Paper-II weighted total** | 100 | | | **≈ 17%** | **≈ 76%** |

## 2. Paper-I map (100 marks)

The notification does not publish sub-weights, so the weights below are **my estimates** for scoring only.

| Notified topic | Est. weight | Old notes | New note | Old | New (est.) |
| :--- | :---: | :--- | :--- | :---: | :---: |
| Current events | 20 | `04/05` (Karnataka schemes, budget, ISRO) | — (check the verify boxes in `06`, `07`) | 60% | 60% |
| Daily comprehension / everyday science | 10 | `04` | — | 35% | 35% |
| Constitution of India | 12 | `03` | — | 70% | 70% |
| History of India with Karnataka | 18 | `01` (Karnataka strong, India thin) | — | 60% | 60% |
| Geography (Karnataka) | 15 | `02` | — | 75% | 75% |
| State & regional administration | 5 | `03` (part) | `08` | 40% | 60% |
| **Economy of Karnataka, rural development, Panchayat Raj, cooperatives** | 15 | `05` (budget/guarantees only) | `06`, `07`, `08` | 15% | 70% |
| Environment & development issues | 5 | none | `09` | 10% | 60% |
| **Paper-I weighted total** | 100 | | | **≈ 51%** | **≈ 62%** |

## 3. Overall score

| | Before | After adding the 15 new notes |
| :--- | :---: | :---: |
| Paper-II | ~17% | ~76% |
| Paper-I | ~51% | ~62% |
| **Both papers (average)** | **~34 / 100** | **~69 / 100** |

**How to read the score:** it is a judgement of *topic breadth × depth against the notified list*, not a measured number. Depth in the old notes is good (PYQ patterns, mnemonics, diagrams) where the topic is on the syllabus. Roughly **half of the existing study-note text (notes 01–07, about 83 KB of 171 KB) maps to nothing in the notified Paper-II list.** The new notes are compact and exam-oriented; they are faster to read than the old ones but do not replace a textbook.

**Still weak after these additions (not written):** Indian history (freedom movement, ancient/medieval India), daily comprehension passages, deeper current affairs (last 12 months). Use PYQs and a current-affairs source for these.

---

## 4. Where to place the files (Obsidian vault)

Vault root: `D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\AGY\`

```
AGY/
├── 00_START_HERE.md                        (edit: paste the block in §5)
├── 02_Syllabus_and_Pattern.md              (keep; this file supersedes its Paper-II section)
├── 02b_Syllabus_Coverage_Map_and_Score.md  ← NEW (this file)
├── 03_Notes/
│   ├── 01 … 10  (existing)
│   ├── 11_Maths_Arithmetic.md              ← NEW
│   ├── 12_Maths_Algebra_and_Coordinate_Geometry.md   ← NEW
│   ├── 13_Maths_Geometry_and_Mensuration.md          ← NEW
│   ├── 14_Photogrammetry_Aerial_and_Drone_Survey.md  ← NEW
│   ├── 15_Satellite_Imagery_Remote_Sensing_and_GIS.md ← NEW
│   ├── 16_GNSS_DGPS_RTK_and_CORS.md        ← NEW
│   ├── 17_Computer_MSOffice_and_AutoCAD.md ← NEW
│   ├── 18_Computer_GIS_Software_QGIS_GeoServer_PostGIS.md ← NEW
│   ├── 19_Computer_Software_Solutions_and_Land_Records_IT.md ← NEW
│   ├── 20_Physics_Full_Syllabus.md         ← NEW
│   └── 21_Geography_Earth_Lithosphere_Maps_India.md  ← NEW
└── 04_Current_Affairs_GK/
    ├── 01 … 05  (existing)
    ├── 06_Indian_Economy_Essentials.md     ← NEW
    ├── 07_Karnataka_Economy_Survey_and_Budget.md     ← NEW
    ├── 08_Rural_Development_Panchayat_Raj_Cooperatives.md ← NEW
    └── 09_Environment_and_Development_Issues.md      ← NEW
```

Simplest way: unzip `AGY_additions.zip` directly into the `AGY` folder. The paths inside the zip already match the tree above.

**Do not delete** notes 01–07. Just move them lower in your reading order.

## 5. Paste into `00_START_HERE.md` (new section)

```markdown
## 🎯 Notified-Syllabus Notes (READ THESE FIRST — added 29 Sep 2026)
Audit and map: [[02b_Syllabus_Coverage_Map_and_Score]]

**Paper-II (Mathematics 40 · Modern Methods 20 · Computer 20 · Physics 10 · Geography 10)**
- [[03_Notes/01_Mathematics_Arithmetic_and_Number_Systems]] · [[03_Notes/02_Mathematics_Algebra_and_Coordinate_Geometry]] · [[03_Notes/02_Mathematics_Algebra_and_Coordinate_Geometry]]
- [[03_Notes/03_Modern_Surveying_Photogrammetry_and_Remote_Sensing]] · [[03_Notes/04_Modern_Surveying_GPS_GIS_and_Advanced_Positioning]] · [[03_Notes/04_Modern_Surveying_GPS_GIS_and_Advanced_Positioning]]
- [[03_Notes/05_Computer_Applications_and_Land_Records_IT]] · [[03_Notes/05_Computer_Applications_and_Land_Records_IT]] · [[03_Notes/05_Computer_Applications_and_Land_Records_IT]]
- [[03_Notes/06_Applied_Physics_Gravitation_and_Mechanics]] · [[03_Notes/07_Physical_Geography_The_Earth_and_Lithosphere]]

**Paper-I (Economy · Rural development · Panchayat Raj · Environment)**
- [[04_Current_Affairs_GK/06_Indian_Economy_Essentials]] · [[04_Current_Affairs_GK/07_Karnataka_Economy_Survey_and_Budget]]
- [[04_Current_Affairs_GK/08_Rural_Development_Panchayat_Raj_Cooperatives]] · [[04_Current_Affairs_GK/09_Environment_and_Development_Issues]]
```

## 6. Suggested order for the days left (Paper-II is worth the most new marks)

| Slot | Do this |
| :--- | :--- |
| Day 1 | Notes 11 → 12 → 13 (Maths, 40 marks). Solve every worked example by hand. |
| Day 2 | Notes 14 → 15 → 16 (Modern methods), then 17 → 18 → 19 (Computer). |
| Day 3 (eve of exam) | Notes 20, 21 (Physics, Geography), then 06 → 07 → 08 → 09 for Paper-I. Read only the Quick Revision boxes. |
| Exam day | Paper-I at 10:30 and Paper-II at 2:30 (verify on hall ticket). Revise formula boxes only. |

> [!NOTE] Mock tests
> Your three HTML mocks were written against the old classical-surveying assumption, so Mock 2 and 3 will not match Paper-II. Use them for Paper-I GK practice only.
