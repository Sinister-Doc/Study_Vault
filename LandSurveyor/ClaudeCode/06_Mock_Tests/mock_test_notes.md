# Mock Test Notes — KEA Karnataka Land Surveyor 2026 (Paper 2 simulations)

> **Last verified: 2026-09-30.** All three mocks below were rebuilt on 2026-09-30
> to the **verified Paper 2 syllabus** ([[02b_Paper2_Official_Syllabus]]):
> **Mathematics 40 · Modern Methods of Surveying 20 · Computer Applications 20 ·
> Physics 10 · Geography 10** (100 Q / 100 marks / 120 min, 0.25 negative per
> wrong answer, 35% per-paper minimum). **Exam date: 02.10.2026** (candidate-confirmed).

## What each mock is

| File | Content | Size |
|---|---|---|
| `mock1.html` | Paper 2 simulation, 100 Q (Maths 40 / Modern 20 / Computer 20 / Physics 10 / Geography 10) | ~45 KB |
| `mock2.html` | Paper 2 simulation, 100 Q, same split, **zero shared questions with mock1/3** | ~45 KB |
| `mock3.html` | Paper 2 simulation, 100 Q, same split, **zero shared questions with mock1/2** | ~46 KB |

Open any file directly in a browser (`file://` — no internet needed). 120-min
countdown with auto-submit, question palette, mark-for-review, section tabs,
per-block score breakdown, explained answer review.

## PYQ-style vs expected — honest labels

- **PYQ-style** (58 of 300 across the three papers) = standard recurring
  diploma/competitive-exam patterns from the official sub-topics — the closest
  available stand-in for trusted-channel PYQ material. **No verified KEA PYQ
  paper exists for this new syllabus** (see `05_Resources/pyq_analysis.md` §1),
  so no question is claimed as "asked in year X".
- **expected** (242 of 300) = most-expected questions written directly to the
  official Paper 2 sub-topics (notes 11–21).
- Every question shows its tag next to the question number **and** in the
  answer-review screen.

## How they were built (reproducible)

Banks (each item = question, 4 options, answer index, explanation, label):

| Bank file | Content | Count |
|---|---|---|
| `_bank_maths.py` | ARITH 42 / ALG 39 / GEO 39 (notes 11–13) | 120 |
| `_bank_modern.py` | PHOTO 20 / RSGIS 20 / GNSS 20 (notes 14–16) | 60 |
| `_bank_computer.py` | OFFICE 22 / GIS-SW 20 / SOFT 20 (notes 17–19) | 62 (2 office Q held as spares) |
| `_bank_physgeo.py` | PHYS 30 / GEOG 30 (notes 20–21) | 60 |

Builder: `_build_paper2.py` — validates (100 Q, 4 distinct options, ans 0–3,
explanation present, no literal `</`, papers disjoint), then splices the
question data + section table + headings into the audited offline engine
(timer/palette/review/scoring reused verbatim; only data and labels change).

Smoke test: `_ls_smoke.js` (jsdom end-to-end: 100 Q, block totals 40/20/20/10/10,
both tags present, tabs, palette, 20-right/10-wrong scoring → 17.50 with 2.50
penalty, review flags + explanations). All three mocks **PASS** (2026-09-30).

```mermaid
flowchart LR
    A["banks: maths / modern / computer / physgeo"] --> B["_build_paper2.py validates"]
    B --> C["splice into audited engine"]
    C --> D["mock1/2/3.html"]
    D --> E["_ls_smoke.js jsdom PASS"]
```

*Pipeline: banks → validated builder → offline mocks → headless-tested.*

Reproduce: `python 06_Mock_Tests/_build_paper2.py`, then
`node 06_Mock_Tests/_ls_smoke.js 06_Mock_Tests/mockN.html` (with jsdom on
`NODE_PATH`).

## Engine vs official OMR — one deliberate difference

The official notification deducts **0.25 for a wrong answer AND 0.25 if no
circle is shaded at all** (the 5th "not answered" circle exists so a deliberate
blank is not penalised). This offline mock scores unattempted questions as
**0** to avoid training blind guessing — but on the real OMR you **must shade
the 5th circle for any question you skip**, or you lose 0.25 anyway.

## History (superseded)

Mocks built before 2026-09-30 followed the old (wrong) surveying/GK/mental
split (Surveying 45 / GK 30 / Mental 25) and are fully superseded by the
Paper 2 simulations above. The old `pyq_analysis.md` Q1–Q60 bank covered
chain/compass/levelling/KLRA — background only, not Paper 2 examinable.
