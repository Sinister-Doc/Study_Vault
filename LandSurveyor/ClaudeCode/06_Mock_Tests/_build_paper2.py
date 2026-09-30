# -*- coding: utf-8 -*-
"""Rebuild the three LS 2026 Paper-2 mock tests from the audited offline engine.

Pattern (verified 02b_Paper2_Official_Syllabus): Paper 2 = 100 Q / 100 marks /
120 min / 0.25 negative, split Maths 40 / Modern Surveying 20 / Computer 20 /
Physics 10 / Geography 10.

Question sources (HONEST labelling — see mock_test_notes.md):
  * "PYQ-style": standard recurring diploma-exam patterns (ALSO closest to
    trusted competitive-exam-channel material), NOT verified KEA PYQs.
  * "expected": most-expected questions written to the official Paper-2
    sub-topics (notes 11-21).
Every mock shows the PYQ-style/expected tag on each question AND in review.

Papers: mock1/2/3 each take a disjoint third of every sub-bank, so the three
papers share NO question. Engine (timer, palette, review, scoring) is reused
verbatim from the existing mock1.html template.
"""

import importlib.util
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "mock1.html")
# First-ever build consumes the legacy (old-syllabus) mock1.html as the engine
# template and overwrites all three mocks, so rebuilds are NOT idempotent.


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


maths = load_module(os.path.join(HERE, "_bank_maths.py"), "bank_maths")
modern = load_module(os.path.join(HERE, "_bank_modern.py"), "bank_modern")
comp = load_module(os.path.join(HERE, "_bank_computer.py"), "bank_computer")
pg = load_module(os.path.join(HERE, "_bank_physgeo.py"), "bank_physgeo")


def spread(lst):
    """Deterministically interleave PYQ-style items through the list so each
    paper third gets a fair share of both tags (stable within each tag)."""
    pyq = [it for it in lst if len(it) > 4 and it[4] == "PYQ-style"]
    exp = [it for it in lst if not (len(it) > 4 and it[4] == "PYQ-style")]
    out = []
    while pyq or exp:
        if pyq:
            out.append(pyq.pop(0))
        if exp:
            out.append(exp.pop(0))
        if exp:
            out.append(exp.pop(0))
    return out


def deal(lst, offset=0):
    """Round-robin deal spread(lst) into 3 buckets with a start offset.

    Sequential thirds strand all PYQ-style tags in one mock; dealing spreads
    both tags across every mock. For a 20-list, offset 0/1/2 yields sizes
    [7,7,6]/[6,7,7]/[7,6,7] — offsets are chosen per bank below so each mock
    still totals exactly 40/20/20/10/10."""
    buckets = [[], [], []]
    for k, it in enumerate(spread(lst)):
        buckets[(k + offset) % 3].append(it)
    return buckets


def split(lst, cuts):
    """Split lst into disjoint parts at cumulative cut points; cuts sums to len(lst)."""
    assert sum(cuts) == len(lst), "cuts %s != %d" % (cuts, len(lst))
    out, acc = [], 0
    for c in cuts:
        out.append(list(lst[acc:acc + c]))
        acc += c
    return out


# Exact per-bank splits so every mock totals 40/20/20/10/10 (banks: 42/39/39,
# 20/20/20, 22->20 used/20/20, 30/30). Office bank's last 2 Q are held as
# documented spares so the three papers stay disjoint at exactly 20 computer Q.
# Banks are dealt round-robin AFTER spreading (PYQ-style interleaved) so every
# mock gets both tags; papers stay disjoint.
# Size check (S sanity below asserts 40/20/20/10/10 per mock):
# office 7/7/6 + gis 7/6/7 + soft 6/7/7 = 20/20/20;
# photo 7/7/6 + rs 7/6/7 + gnss 6/7/7 = 20/20/20.
_D = {}
specs = [
    ("arith", maths.ARITH, 0),
    ("alg", maths.ALG, 0),
    ("geo", maths.GEO, 0),
    ("photo", modern.PHOTO, 0),
    ("rs", modern.RSGIS, 2),
    ("gnss", modern.GNSS, 1),
    ("office", comp.OFFICE[:20], 0),  # last 2 held as spares
    ("gis", comp.GIS_SW, 2),
    ("soft", comp.SOFT, 1),
    ("phys", pg.PHYS, 0),
    ("geog", pg.GEOG, 0),
]
for _name, _lst, _off in specs:
    _a, _b, _c = deal(_lst, _off)
    _D[_name] = (_a, _b, _c)
S = _D
# sanity: mock1 = col 0 of each -> 40/20/20/10/10
assert sum(len(S[k][0]) for k in ("arith", "alg", "geo")) == 40
assert sum(len(S[k][0]) for k in ("photo", "rs", "gnss")) == 20
assert sum(len(S[k][0]) for k in ("office", "gis", "soft")) == 20
for i in (1, 2):
    assert sum(len(S[k][i]) for k in ("arith", "alg", "geo")) == 40
    assert sum(len(S[k][i]) for k in ("photo", "rs", "gnss")) == 20
    assert sum(len(S[k][i]) for k in ("office", "gis", "soft")) == 20


# ------------------------------------------------------------------ recipes
# Each section: (key, display name, bank list). Per mock i: Maths 14+13+13=40,
# Modern 7+7+6 / 6+7+7 / 7+6+7 = 20, Computer 7+7+6 / 7+7+6 / 6+6+8 = 20,
# Physics 10, Geography 10.
def sections_for(i):
    return [
        ("maths_arith", "Mathematics — Arithmetic",
         S["arith"][i]),
        ("maths_alg", "Mathematics — Algebra & Coordinate Geometry",
         S["alg"][i]),
        ("maths_geo", "Mathematics — Geometry & Mensuration",
         S["geo"][i]),
        ("modern_photo", "Modern Survey — Photogrammetry, Aerial & Drone",
         S["photo"][i]),
        ("modern_rs", "Modern Survey — Satellite Imagery, RS & GIS",
         S["rs"][i]),
        ("modern_gnss", "Modern Survey — GNSS, DGPS, RTK & CORS",
         S["gnss"][i]),
        ("comp_office", "Computer — MS Office & AutoCAD",
         S["office"][i]),
        ("comp_gis", "Computer — GIS Software (QGIS/GeoServer/PostGIS)",
         S["gis"][i]),
        ("comp_it", "Computer — Software Solutions & Land Records IT",
         S["soft"][i]),
        ("physics", "Physics",
         S["phys"][i]),
        ("geography", "Geography",
         S["geog"][i]),
    ]


PAPERS = {
    "mock1": {
        "title": "Mock Test 1 — Paper 2 (Specific Paper) Simulation",
        "sub": "KEA Karnataka Land Surveyor 2026 &middot; Paper 2 full-length simulation (offline, self-contained)",
        "brand": "Mock Test 1 &mdash; Paper 2",
        "sections": sections_for(0),
    },
    "mock2": {
        "title": "Mock Test 2 — Paper 2 (Specific Paper) Simulation",
        "sub": "KEA Karnataka Land Surveyor 2026 &middot; Paper 2 full-length simulation (offline, self-contained)",
        "brand": "Mock Test 2 &mdash; Paper 2",
        "sections": sections_for(1),
    },
    "mock3": {
        "title": "Mock Test 3 — Paper 2 (Specific Paper) Simulation",
        "sub": "KEA Karnataka Land Surveyor 2026 &middot; Paper 2 full-length simulation (offline, self-contained)",
        "brand": "Mock Test 3 &mdash; Paper 2",
        "sections": sections_for(2),
    },
}

BLOCKS = [  # (display block, section keys) for the welcome table
    ("Mathematics (40)", ["maths_arith", "maths_alg", "maths_geo"], 40),
    ("Modern Methods of Surveying (20)", ["modern_photo", "modern_rs", "modern_gnss"], 20),
    ("Computer Applications (20)", ["comp_office", "comp_gis", "comp_it"], 20),
    ("Physics (10)", ["physics"], 10),
    ("Geography (10)", ["geography"], 10),
]


# ---------------------------------------------------------------- validation
def validate(name, paper):
    problems = []
    total = 0
    seen = set()
    for key, label, items in paper["sections"]:
        if not items:
            problems.append("%s/%s: empty section" % (name, key))
        for i, it in enumerate(items):
            total += 1
            if len(it) < 4:
                problems.append("%s/%s[%d]: short tuple" % (name, key, i))
                continue
            q, opts, ans, exp = it[0], it[1], it[2], it[3]
            if len(opts) != 4:
                problems.append("%s/%s[%d]: opts != 4" % (name, key, i))
            elif len(set(opts)) != 4:
                problems.append("%s/%s[%d]: duplicate options" % (name, key, i))
            if not isinstance(ans, int) or not (0 <= ans <= 3):
                problems.append("%s/%s[%d]: bad ans" % (name, key, i))
            if not exp or len(str(exp)) < 5:
                problems.append("%s/%s[%d]: missing explanation" % (name, key, i))
            if q in seen:
                problems.append("%s/%s[%d]: duplicated stem" % (name, key, i))
            seen.add(q)
            if "</" in str(q) or "</" in str(exp):
                problems.append("%s/%s[%d]: contains '</'" % (name, key, i))
            for o in opts:
                if "</" in str(o):
                    problems.append("%s/%s[%d]: option contains '</'" % (name, key, i))
    if total != 100:
        problems.append("%s: %d questions, expected 100" % (name, total))
    return problems, total, seen


ALL_PROBLEMS = []
SEEN = {}
for nm in ("mock1", "mock2", "mock3"):
    probs, tot, seen = validate(nm, PAPERS[nm])
    ALL_PROBLEMS.extend(probs)
    SEEN[nm] = seen
    print("%s: %d questions, %d problems" % (nm, tot, len(probs)))

if ALL_PROBLEMS:
    print("\nVALIDATION FAILED:")
    for p in ALL_PROBLEMS:
        print("  -", p)
    raise SystemExit(1)

overlap12 = SEEN["mock1"] & SEEN["mock2"]
overlap13 = SEEN["mock1"] & SEEN["mock3"]
overlap23 = SEEN["mock2"] & SEEN["mock3"]
print("cross-paper repeats:", len(overlap12 | overlap13 | overlap23))
if overlap12 | overlap13 | overlap23:
    for o in list(overlap12 | overlap13 | overlap23)[:5]:
        print("  !", o[:70])
    raise SystemExit("papers must be disjoint")

pyq = sum(1 for nm in PAPERS for _k, _l, items in PAPERS[nm]["sections"]
          for it in items if len(it) > 4 and it[4] == "PYQ-style")
print("PYQ-style tagged:", pyq, "of 300")


# ----------------------------------------------------------------- rendering
def js_questions(paper):
    out = []
    n = 0
    for key, _label, items in paper["sections"]:
        for it in items:
            n += 1
            out.append({
                "q": it[0],
                "opts": list(it[1]),
                "ans": it[2],
                "exp": it[3],
                "label": it[4] if len(it) > 4 else "expected",
                "id": n,
            })
    return out


def json_js(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("</", "<\\/")


def build(name, template):
    paper = PAPERS[name]
    qs = js_questions(paper)
    n = len(qs)

    start = template.index("const QUESTIONS = [")
    end = template.index("\nconst TOTAL_SECONDS", start)
    new_data = "const QUESTIONS = %s;" % json_js(qs)
    t = template[:start] + new_data + template[end:]

    # NOTE: indices recomputed on `t` — the DATA splice changed all offsets.
    sec_start = t.index("const SECTIONS = [")
    sec_end = t.index("/* ---------- STATE ---------- */", sec_start)

    bounds = []
    acc = 0
    for key, _l, items in paper["sections"]:
        bounds.append(acc)
        acc += len(items)
    bounds.append(acc)

    sec_lines = ["const SECTIONS = ["]
    for i, (key, label, _items) in enumerate(paper["sections"]):
        comma = "," if i < len(paper["sections"]) - 1 else ""
        sec_lines.append('  {key:"%s", name:"%s"}%s' % (key, re.sub(r"&amp;", "&", label), comma))
    sec_lines.append("];")
    sec_lines.append("const SECTION_BOUNDS = %s;" % json.dumps(bounds))
    sec_lines.append("""QUESTIONS.forEach((q,i)=>{
  for(let s=0;s<SECTIONS.length;s++){
    if(i >= SECTION_BOUNDS[s] && i < SECTION_BOUNDS[s+1]){ q.section = SECTIONS[s].key; break; }
  }
});

""")
    t = t[:sec_start] + "\n".join(sec_lines) + t[sec_end:]

    t = re.sub(r"<title>.*?</title>",
               "<title>%s &mdash; KEA Land Surveyor 2026 (Paper 2)</title>" % name.replace("mock", "Mock Test "),
               t, count=1)
    t = re.sub(r"<h1>.*?</h1>", "<h1>%s</h1>" % paper["title"], t, count=1)
    t = re.sub(r'<div class="sub">.*?</div>',
               '<div class="sub">%s</div>' % paper["sub"], t, count=1)
    t = re.sub(r'<div class="brand">.*?</div>',
               '<div class="brand">%s<small>KEA Land Surveyor 2026 &middot; Paper 2 &middot; Exam 02.10.2026</small></div>' % paper["brand"],
               t, count=1)

    # ---- per-mock localStorage keys (file:// shares one origin) ------------
    t = t.replace('const KEY = "Mock Test 1_state";',
                  'const KEY = "LS Paper2 %s_state";' % name)
    t = t.replace('const WELCOMED = "Mock Test 1_welcomed";',
                  'const WELCOMED = "LS Paper2 %s_welcomed";' % name)

    # ---- show the PYQ-style/expected tag inside the answer review -----------
    old_rev = "esc(sec.name)+'</span>'+pill"
    new_rev = "esc(sec.name)+' &middot; '+esc(q.label)+'</span>'+pill"
    assert old_rev in t, "renderReview anchor changed — inspect engine"
    t = t.replace(old_rev, new_rev)

    rows = []
    sec_len = {key: len(items) for key, _l, items in paper["sections"]}
    for block, keys, marks in BLOCKS:
        rows.append("      <tr><td>%s</td><td>%d</td><td>%d</td></tr>"
                    % (block, sum(sec_len[k] for k in keys), marks))
    rows.append("      <tr><td><b>Total</b></td><td><b>%d</b></td><td><b>%d</b></td></tr>" % (n, n))
    t = re.sub(r"(<tbody>\s*\n)(.*?)(\s*</tbody>)",
               lambda m: m.group(1) + "\n".join(rows) + m.group(3), t, count=1, flags=re.S)

    t = re.sub(
        r'Each question carries 1 mark\..*?without losing answers\.',
        "Each question carries 1 mark. <b>0.25 mark is deducted for every wrong answer</b> "
        "and, on the real OMR sheet, a further 0.25 is deducted for a question left with "
        "no circle shaded at all &mdash; so always shade the 5th (not-answered) circle for "
        "anything you skip. This offline paper scores an unattempted question as 0 so it "
        "does not train blind guessing. The timer counts down from <b>120:00</b> and the "
        "paper auto-submits at <b>00:00:00</b>. Every question is tagged "
        "<b>PYQ-style</b> (standard recurring pattern) or <b>expected</b> (most-expected "
        "from the official syllabus). Progress is saved in your browser, so you "
        "may reload without losing answers.",
        t, count=1, flags=re.S)

    return t


template = open(TEMPLATE, "r", encoding="utf-8").read()
for nm in ("mock1", "mock2", "mock3"):
    html = build(nm, template)
    out = os.path.join(HERE, nm + ".html")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, os.path.getsize(out)))

print("\nAll three LS Paper-2 mocks built and validated.")
