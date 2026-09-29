/**
 * Headless functional smoke test for the generated VAO mocks.
 *
 * Loads each mock in jsdom, drives it the way a candidate would (Start →
 * answer 30 questions → mark one for review → submit), and asserts that the
 * result screen really renders a per-section breakdown, correct/wrong counts,
 * the unexplained-answer penalty and an explained answer review.
 *
 * The page's top-level `const`/`let` live in the global *lexical* scope, not on
 * `window`, so everything is read through `dom.window.eval(...)`.
 *
 * Run:  NODE_PATH="<global node_modules>" node _smoke_test.js [dir] [name ...]
 *       defaults to this folder with mock1 mock2 mock3
 */
const fs = require("fs");
const path = require("path");
const { JSDOM } = require("jsdom");

const argv = process.argv.slice(2);
const DIR = argv.length && !argv[0].endsWith(".html") && fs.existsSync(argv[0])
  ? path.resolve(argv.shift())
  : __dirname;
const MOCKS = argv.length
  ? argv.map((a) => a.replace(/\.html$/, ""))
  : ["mock1", "mock2", "mock3"];

// How many questions the page must hold — read from the welcome table's Total row.
let failures = 0;
const ok = (cond, msg) => {
  console.log((cond ? "  PASS  " : "  FAIL  ") + msg);
  if (!cond) failures++;
};

for (const name of MOCKS) {
  const html = fs.readFileSync(path.join(DIR, name + ".html"), "utf8");
  console.log("\n=== " + name + ".html ===");

  const dom = new JSDOM(html, {
    runScripts: "dangerously",
    pretendToBeVisual: true,
    url: "http://localhost/",
  });
  const w = dom.window;
  const d = w.document;
  const ev = (expr) => w.eval(expr);
  const safe = (expr) => { try { return ev(expr); } catch (e) { return undefined; } };
  // jsdom does not implement these two; the engine calls them for smooth UX only.
  w.scrollTo = () => {};
  w.Element.prototype.scrollIntoView = () => {};
  const decode = (s) => String(s).replace(/&amp;/g, "&").replace(/&middot;/g, "·");

  // ---- data ---------------------------------------------------------------
  const Q = ev("QUESTIONS");
  const N = Q.length;
  ok(Array.isArray(Q) && N > 0, N + " questions loaded");
  ok(N === 100, "100 questions (official paper size)");

  const secs = ev("SECTIONS");
  const perSection = {};
  Q.forEach((q) => { perSection[q.section] = (perSection[q.section] || 0) + 1; });
  ok(Object.keys(perSection).length === secs.length,
     "every question carries a section: " + JSON.stringify(perSection));
  ok(Object.values(perSection).every((n) => n > 0), "no section is empty");
  const bounds = safe("SECTION_BOUNDS");
  ok(bounds === undefined || bounds.length === secs.length + 1,
     "SECTION_BOUNDS has n+1 edges (or engine uses a hard-coded split)");

  // ---- start --------------------------------------------------------------
  d.getElementById("startBtn").click();
  ok(d.getElementById("shell").classList.contains("on"), "exam shell opens on Start");
  ok(d.getElementById("welcome").classList.contains("hidden"), "welcome screen hides");

  const tabText = d.getElementById("tabs").textContent;
  ok(new RegExp("All Questions \\(" + N + "\\)").test(tabText),
     "'All Questions (" + N + ")' tab present");
  secs.forEach((s) => {
    ok(tabText.includes(s.name + " (" + perSection[s.key] + ")"),
       "tab shows correct count for " + s.key + " (" + perSection[s.key] + ")");
  });

  ok(d.getElementById("palette").children.length === N, "palette has " + N + " buttons");

  // ---- answer 30 questions: 20 right, 10 wrong ---------------------------
  ev(`(function(){
        for(let i=0;i<30;i++){
          const q = QUESTIONS[i];
          state.answers[q.id] = i<20 ? q.ans : (q.ans+1)%4;
        }
        state.marked[QUESTIONS[0].id] = true;
        save(); updateMeta(); palette();
      })()`);
  ok(d.getElementById("sAns").textContent === "30", "attempted counter reads 30");
  ok(d.getElementById("sMark").textContent === "1", "mark-for-review counter reads 1");
  ok(/Attempted 30 \/ /.test(d.getElementById("barLbl").textContent), "progress bar label updates");

  // ---- submit -------------------------------------------------------------
  d.getElementById("submitBtn").click();
  ok(!!d.querySelector(".modal"), "submit raises a confirmation modal");
  d.querySelector(".modal #mYes").click();

  const resultHTML = d.getElementById("result").innerHTML;
  ok(!d.getElementById("result").classList.contains("hidden"), "result panel is shown");
  ok(/Your Score/.test(resultHTML), "score banner rendered");

  // per-section breakdown — the exact thing that was broken before
  const flatResult = decode(resultHTML);
  const missing = secs.filter((s) => !flatResult.includes(s.name));
  ok(missing.length === 0,
     "breakdown table has a row for all " + secs.length + " sections" +
     (missing.length ? " (missing: " + missing.map((s) => s.key).join(",") + ")" : ""));

  ok(/Correct/.test(resultHTML) && /Wrong/.test(resultHTML) &&
     /Unattempted/.test(resultHTML) && /Penalty/.test(resultHTML),
     "correct / wrong / unattempted / penalty tiles present");
  ok(/>20</.test(resultHTML), "20 correct shown");
  ok(/>10</.test(resultHTML), "10 wrong shown");
  ok(/2\.50/.test(resultHTML), "penalty 10 x 0.25 = 2.50 shown");
  ok(/17\.50/.test(resultHTML), "score 20 - 2.50 = 17.50 shown");

  ok(/>70</.test(resultHTML), (N - 30) + " unattempted shown");

  // ---- answer review ------------------------------------------------------
  d.getElementById("revBtn").click();
  const revHTML = d.getElementById("review").innerHTML;
  const found = Q.slice(0, 30).filter((q) => revHTML.includes(q.exp.slice(0, 25))).length;
  ok(found >= 28, "answer review explains the answered questions (" + found + "/30)");
  ok(/[←] correct/.test(revHTML), "review flags the correct option");
  ok(/[←] your answer/.test(revHTML), "review flags the candidate's wrong pick");
  ok(/Explanation:/.test(revHTML), "review carries an Explanation line");

  // ---- timer --------------------------------------------------------------
  ok(typeof ev("state.left") === "number" && ev("state.left") <= 7200,
     "countdown timer state present (left=" + ev("state.left") + ")");
  ok(/^\d+:\d\d:\d\d$/.test(d.getElementById("timer").textContent),
     "timer renders as h:mm:ss (" + d.getElementById("timer").textContent + ")");

  // ---- self-containment ---------------------------------------------------
  ok(!/src\s*=\s*["']http/.test(html) && !/href\s*=\s*["']http/.test(html),
     "no external http(s) assets — fully offline");

  dom.window.close();
}

console.log("\n" + (failures === 0
  ? "ALL SMOKE TESTS PASSED"
  : failures + " SMOKE TEST CHECK(S) FAILED"));
process.exit(failures === 0 ? 0 : 1);
