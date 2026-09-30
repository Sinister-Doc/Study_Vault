// LS Paper-2 smoke test: jsdom end-to-end (sectioning, palette, scoring, review).
// Usage: node _ls_smoke.js [mockfile]  (default mock1.html)
const fs = require("fs");
const path = require("path");
const { JSDOM } = require("jsdom");

const file = process.argv[2] || "mock1.html";
const fp = path.isAbsolute(file) ? file : path.join(__dirname, path.basename(file));
const html = fs.readFileSync(fp, "utf8");
const dom = new JSDOM(html, {
  runScripts: "dangerously",
  pretendToBeVisual: true,
  url: "http://localhost/",
  beforeParse(w) {
    w.scrollTo = () => {};
    if (w.Element && w.Element.prototype)
      w.Element.prototype.scrollIntoView = function () {};
  },
});
const w = dom.window;
const fail = (m) => { console.error("FAIL:", m); process.exit(1); };
const safe = (fn, dflt) => { try { const v = fn(); return v === undefined ? dflt : v; } catch (e) { return dflt; } };

// --- data checks
const Q = w.eval("QUESTIONS");
if (!Array.isArray(Q) || Q.length !== 100) fail("QUESTIONS length " + (Q && Q.length));
const SEC = w.eval("SECTIONS");
const BOUNDS = safe(() => w.eval("SECTION_BOUNDS"), null);
if (!BOUNDS || BOUNDS[0] !== 0 || BOUNDS[BOUNDS.length - 1] !== 100)
  fail("SECTION_BOUNDS bad: " + JSON.stringify(BOUNDS));
// expected block totals: Maths 40 / Modern 20 / Computer 20 / Physics 10 / Geography 10
const counts = {};
Q.forEach((q) => { counts[q.section] = (counts[q.section] || 0) + 1; });
const sum = (ks) => ks.reduce((a, k) => a + (counts[k] || 0), 0);
if (sum(["maths_arith", "maths_alg", "maths_geo"]) !== 40) fail("maths != 40: " + JSON.stringify(counts));
if (sum(["modern_photo", "modern_rs", "modern_gnss"]) !== 20) fail("modern != 20");
if (sum(["comp_office", "comp_gis", "comp_it"]) !== 20) fail("computer != 20");
if ((counts.physics || 0) !== 10) fail("physics != 10");
if ((counts.geography || 0) !== 10) fail("geography != 10");
const labels = new Set(Q.map((q) => q.label));
if (!labels.has("PYQ-style") || !labels.has("expected"))
  fail("both PYQ-style and expected tags must appear: " + [...labels]);
for (const q of Q) {
  if (!q.q || !Array.isArray(q.opts) || q.opts.length !== 4) fail("bad shape Q" + q.id);
  if (typeof q.ans !== "number" || q.ans < 0 || q.ans > 3) fail("bad ans Q" + q.id);
  if (!q.exp || q.exp.length < 5) fail("missing explanation Q" + q.id);
}
console.log("data ok:", file, "| PYQ-style:", Q.filter((q) => q.label === "PYQ-style").length,
  "| expected:", Q.filter((q) => q.label === "expected").length);

// --- UI flow: start, answer 30 (20 right / 10 wrong), check palette + tabs
w.document.getElementById("startBtn").click();
if (!w.document.getElementById("shell").classList.contains("on")) fail("shell did not open");
let tabs = w.document.querySelectorAll("#tabs .tab").length;
if (tabs < 5) fail("expected >=5 section tabs, got " + tabs);
// tag visible on first question
let tagTxt = (w.document.querySelector("#qbox .tag") || {}).textContent || "";
if (!/PYQ-style|expected/.test(tagTxt)) fail("question tag missing: " + tagTxt);
const NEG = w.eval("NEG");
if (NEG !== 0.25) fail("NEG != 0.25");
const st = w.eval("state");
Q.slice(0, 30).forEach((q, i) => {
  st.answers[q.id] = i < 20 ? q.ans : (q.ans + 1) % 4; // 20 right, 10 wrong
});
w.eval("save(); render(); updateMeta(); palette();");
const palBtns = w.document.querySelectorAll("#palette button");
if (palBtns.length !== 100) fail("palette buttons " + palBtns.length);
const attempted = [...palBtns].filter((b) => b.classList.contains("attempted")).length;
if (attempted !== 30) fail("attempted " + attempted + " != 30");

// --- submit + result math: 20 right, 10 wrong => 20 - 2.50 = 17.50
w.eval("showResult();");
const resHtml = w.document.getElementById("result").innerHTML;
const dec = (s) => s.replace(/&amp;/g, "&");
if (!/17\.50/.test(resHtml)) fail("score 17.50 missing");
if (!/2\.50/.test(resHtml)) fail("penalty 2.50 missing");
if (!/Mathematics|Physics|Geography|Computer|Modern/.test(dec(resHtml)))
  fail("per-block breakdown missing");
// --- review: explanations + PYQ/expected flags
w.eval("renderReview();");
const rev = w.document.getElementById("review").innerHTML;
if (!/Explanation/.test(rev)) fail("review explanations missing");
if (!/PYQ-style|expected/.test(rev)) fail("review tags missing");
console.log("PASS:", file, "(data + UI + scoring + review)");
dom.window.close();
process.exit(0);
