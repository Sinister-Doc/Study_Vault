# -*- coding: utf-8 -*-
"""
Build the three VAO 2026 offline mock tests from the audited Land Surveyor engine.

The engine (timer + auto-submit, palette, mark-for-review, section tabs, scored
result with a per-section breakdown, and an explained answer review) is reused
verbatim from:
    LandSurveyor\\ClaudeCode\\06_Mock_Tests\\mock1.html
Only the data block, the section table, the headings and the localStorage keys are
substituted. Nothing else in the template is touched, so every VAO mock behaves
exactly like the audited Land Surveyor mock.

Papers built (official pattern: each paper 100 Q / 100 marks / 120 min / 0.25 negative):
  mock1  Paper 1  General Knowledge                        100 Q
  mock2  Paper 2  Kannada 35 + English 35 + Computer 30    100 Q
  mock3  Revision mixed: GK 50 + Kannada 20 + Eng 15 + Comp 15   100 Q

Question pools are sliced so that mock1 and mock2 use the FIRST 100 questions of
each pool and mock3 uses the REMAINDER plus the supplementary pool, i.e. no
question is repeated between papers.
"""

import importlib.util
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TEMPLATE = os.path.join(
    ROOT, "LandSurveyor", "ClaudeCode", "06_Mock_Tests", "mock1.html"
)


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gk = load_module(os.path.join(HERE, "_bank_gk.py"), "bank_gk")
gk2 = load_module(os.path.join(HERE, "_bank_gk2.py"), "bank_gk2")
p2 = load_module(os.path.join(HERE, "_bank_p2.py"), "bank_p2")
p2b = load_module(os.path.join(HERE, "_bank_p2b.py"), "bank_p2b")


def take(bank, start, end):
    """Slice a bank, keeping the (question, opts, ans, exp, label) shape."""
    return list(bank[start:end])


# ---------------------------------------------------------------- paper recipes
# Each section: (key, display name, list of bank items in paper order)
PAPERS = {
    "mock1": {
        "title": "Mock Test 1 — Paper 1: General Knowledge",
        "sub": "KEA Karnataka VAO 2026 &middot; Paper 1 (GK) &middot; Full-length 100-question paper (offline, self-contained)",
        "brand": "Mock Test 1 &mdash; Paper 1 GK",
        "sections": [
            ("history", "Indian History (with Karnataka)",
             take(gk.HISTORY, 0, 20)),
            ("geography", "Indian &amp; Karnataka Geography",
             take(gk.GEOGRAPHY, 0, 15)),
            ("polity", "Indian Constitution &amp; Polity",
             take(gk.POLITY, 0, 25)),
            ("economy", "Economy &amp; Rural Development",
             take(gk.ECONOMY, 0, 15)),
            ("science", "Everyday Science",
             take(gk.SCIENCE, 0, 10)),
            ("ca", "Current Events",
             take(gk.CA, 0, 15)),
        ],
    },
    "mock2": {
        "title": "Mock Test 2 — Paper 2: Kannada, English &amp; Computer",
        "sub": "KEA Karnataka VAO 2026 &middot; Paper 2 (Kannada + English + Computer Knowledge) &middot; Full-length 100-question paper (offline, self-contained)",
        "brand": "Mock Test 2 &mdash; Paper 2",
        "sections": [
            ("kannada", "Paper 2 (ಎ) General Kannada",
             take(p2.KANNADA, 0, 35)),
            ("english", "Paper 2 (ಬಿ) General English",
             take(p2.ENGLISH, 0, 35)),
            ("computer", "Paper 2 (ಸಿ) Computer Knowledge",
             take(p2.COMPUTER, 0, 30)),
        ],
    },
    "mock3": {
        "title": "Mock Test 3 — Mixed Revision Paper",
        "sub": "KEA Karnataka VAO 2026 &middot; Mixed revision paper — GK 50 + Kannada 20 + English 15 + Computer 15 &middot; (offline, self-contained)",
        "brand": "Mock Test 3 &mdash; Mixed Revision",
        "sections": [
            ("gk", "General Knowledge (revision set)", (
                take(gk.HISTORY, 20, 29) + take(gk.GEOGRAPHY, 15, 21) +
                take(gk.POLITY, 25, 31) + take(gk.ECONOMY, 15, 23) +
                take(gk.SCIENCE, 10, 20) + take(gk.CA, 15, 16) +
                take(gk2.EXTRA_HISTORY, 0, 2) + take(gk2.EXTRA_GEOGRAPHY, 0, 2) +
                take(gk2.EXTRA_POLITY, 0, 3) + take(gk2.EXTRA_ECONOMY, 0, 1) +
                take(gk2.EXTRA_SCIENCE, 0, 1) + take(gk2.EXTRA_CA, 0, 1)
            )),
            ("kannada", "General Kannada (revision set)", (
                take(p2.KANNADA, 35, 41) + take(p2b.EXTRA_KANNADA, 0, 14)
            )),
            ("english", "General English (revision set)",
             take(p2.ENGLISH, 35, 50)),
            ("computer", "Computer Knowledge (revision set)",
             take(p2.COMPUTER, 30, 45)),
        ],
    },
}


# ------------------------------------------------------------------- validation
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
                problems.append("%s/%s[%d]: contains '</' (breaks <script>)" % (name, key, i))
    if total != 100:
        problems.append("%s: %d questions, expected 100" % (name, total))
    return problems, total


ALL_PROBLEMS = []
for nm in ("mock1", "mock2", "mock3"):
    probs, tot = validate(nm, PAPERS[nm])
    ALL_PROBLEMS.extend(probs)
    print("%s: %d questions, %d problems" % (nm, tot, len(probs)))

if ALL_PROBLEMS:
    print("\nVALIDATION FAILED:")
    for p in ALL_PROBLEMS:
        print("  -", p)
    raise SystemExit(1)

# mock3 must not reuse anything from mock1/mock2
pool_1_2 = set()
for nm in ("mock1", "mock2"):
    for _k, _l, items in PAPERS[nm]["sections"]:
        for it in items:
            pool_1_2.add(it[0])
overlap = [it[0] for _k, _l, items in PAPERS["mock3"]["sections"] for it in items
           if it[0] in pool_1_2]
print("cross-paper repeats:", len(overlap))
if overlap:
    for o in overlap[:5]:
        print("  !", o[:70])
    raise SystemExit("mock3 must be disjoint from mock1/mock2")


# ------------------------------------------------------------------- rendering
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
    # never let a literal "</" reach the HTML parser inside <script>
    return s.replace("</", "<\\/")


def build(name, template):
    paper = PAPERS[name]
    qs = js_questions(paper)
    n = len(qs)

    # ---- DATA block ---------------------------------------------------------
    start = template.index("const QUESTIONS = [")
    end = template.index("\nconst TOTAL_SECONDS", start)
    new_data = "const QUESTIONS = %s;" % json_js(qs)
    t = template[:start] + new_data + template[end:]

    # ---- SECTIONS + assignment block ---------------------------------------
    # NOTE: indices must be recomputed on `t`, not on `template` — the DATA
    # splice above changed every offset after `start`.
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
    new_secs = "\n".join(sec_lines)

    t = t[:sec_start] + new_secs + t[sec_end:]

    # ---- headings -----------------------------------------------------------
    t = re.sub(r"<title>.*?</title>",
               "<title>%s &mdash; KEA Karnataka VAO 2026</title>" % name.replace("mock", "Mock Test "),
               t, count=1)
    t = re.sub(r"<h1>.*?</h1>", "<h1>%s</h1>" % paper["title"], t, count=1)
    t = re.sub(r'<div class="sub">.*?</div>',
               '<div class="sub">%s</div>' % paper["sub"], t, count=1)
    t = re.sub(r'<div class="brand">.*?</div>',
               '<div class="brand">%s<small>KEA Karnataka VAO 2026</small></div>' % paper["brand"],
               t, count=1)

    # ---- welcome section table ---------------------------------------------
    rows = []
    for key, label, items in paper["sections"]:
        rows.append("      <tr><td>%s</td><td>%d</td><td>%d</td></tr>" % (label, len(items), len(items)))
    rows.append("      <tr><td><b>Total</b></td><td><b>%d</b></td><td><b>%d</b></td></tr>" % (n, n))
    new_rows = "\n".join(rows)
    t = re.sub(r"(<tbody>\s*\n)(.*?)(\s*</tbody>)",
               lambda m: m.group(1) + new_rows + m.group(3), t, count=1, flags=re.S)

    # ---- localStorage keys --------------------------------------------------
    t = t.replace('const KEY = "Mock Test 1_state";',
                  'const KEY = "VAO %s_state";' % name)
    t = t.replace('const WELCOMED = "Mock Test 1_welcomed";',
                  'const WELCOMED = "VAO %s_welcomed";' % name)

    # ---- welcome note -------------------------------------------------------
    t = re.sub(
        r'Each question carries 1 mark\..*?without losing answers\.',
        "Each question carries 1 mark. <b>0.25 mark is deducted for every wrong answer</b> "
        "and, on the real OMR sheet, a further 0.25 is deducted for a question left with "
        "no circle shaded at all &mdash; so always shade the 5th (not-answered) circle for "
        "anything you skip. This offline paper scores an unattempted question as 0 so it "
        "does not train blind guessing. The timer counts down from <b>120:00</b> and the "
        "paper auto-submits at <b>00:00:00</b>. Progress is saved in your browser, so you "
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

print("\nAll three VAO mocks built and validated.")
