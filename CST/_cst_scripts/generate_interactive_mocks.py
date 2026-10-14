import json
import os

qb_path = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy\05_Resources\Question_Bank\question_bank.json"
mock_dir = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy\06_Mock_Tests"

with open(qb_path, "r", encoding="utf-8") as f:
    qb = json.load(f)

questions = qb.get("questions", [])
p1_questions = [q for q in questions if q.get("paper") == "P1"]
p2_questions = [q for q in questions if q.get("paper") == "P2"]

def generate_html(title, paper_code, q_list):
    q_json_str = json.dumps(q_list, ensure_ascii=False)
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - GPT CST 2026</title>
<style>
:root {{
  --bg: #0f172a;
  --surface: #1e293b;
  --surface-alt: #334155;
  --text: #f8fafc;
  --text-dim: #94a3b8;
  --primary: #38bdf8;
  --primary-hover: #0284c7;
  --success: #22c55e;
  --danger: #ef4444;
  --warning: #f59e0b;
  --border: #475569;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
body {{ background-color: var(--bg); color: var(--text); padding: 20px; line-height: 1.6; }}
.container {{ max-width: 900px; margin: 0 auto; }}
header {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }}
h1 {{ font-size: 1.5rem; color: var(--primary); }}
.timer {{ font-size: 1.3rem; font-weight: bold; background: var(--surface-alt); padding: 8px 16px; border-radius: 8px; color: var(--warning); }}
.score-badge {{ font-size: 1.1rem; background: var(--surface-alt); padding: 8px 16px; border-radius: 8px; color: var(--success); display: none; }}
.filter-bar {{ display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; }}
.filter-btn {{ background: var(--surface); border: 1px solid var(--border); color: var(--text-dim); padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 0.9rem; transition: all 0.2s; }}
.filter-btn.active {{ background: var(--primary); color: #000; font-weight: bold; border-color: var(--primary); }}
.card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 20px; }}
.card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
.q-num {{ font-size: 1rem; font-weight: bold; color: var(--primary); }}
.tag {{ font-size: 0.75rem; padding: 4px 8px; border-radius: 4px; font-weight: 600; text-transform: uppercase; }}
.tag-pyq {{ background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }}
.tag-expected {{ background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid #38bdf8; }}
.tag-referenced {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #f59e0b; }}
.q-text {{ font-size: 1.1rem; margin-bottom: 8px; font-weight: 500; }}
.q-alt {{ font-size: 1rem; color: var(--text-dim); margin-bottom: 16px; }}
.options {{ display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px; }}
.option-label {{ display: flex; align-items: center; gap: 12px; background: var(--surface-alt); padding: 12px 16px; border-radius: 8px; cursor: pointer; border: 1px solid transparent; transition: all 0.2s; }}
.option-label:hover {{ border-color: var(--primary); }}
.option-label.correct {{ background: rgba(34, 197, 94, 0.25); border-color: var(--success); color: #4ade80; }}
.option-label.incorrect {{ background: rgba(239, 68, 68, 0.25); border-color: var(--danger); color: #f87171; }}
.explanation {{ background: #091e3a; border-left: 4px solid var(--primary); padding: 16px; border-radius: 4px; margin-top: 16px; display: none; font-size: 0.95rem; }}
.actions {{ display: flex; gap: 12px; justify-content: flex-end; margin-top: 24px; margin-bottom: 40px; }}
.btn {{ background: var(--primary); color: #000; font-weight: bold; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-size: 1rem; transition: background 0.2s; }}
.btn:hover {{ background: var(--primary-hover); }}
</style>
</head>
<body>
<div class="container">
  <header>
    <div>
      <h1>{title}</h1>
      <p style="color: var(--text-dim); font-size: 0.9rem;">Karnataka Teachers Recruitment (GPT - CST 1 to 8 Cadre)</p>
    </div>
    <div style="display: flex; gap: 12px; align-items: center;">
      <div id="timer" class="timer">Time: 30:00</div>
      <div id="score" class="score-badge">Score: 0 / {len(q_list)}</div>
    </div>
  </header>

  <div class="filter-bar">
    <button class="filter-btn active" onclick="filterQuestions('all', this)">All Questions ({len(q_list)})</button>
    <button class="filter-btn" onclick="filterQuestions('PYQ', this)">PYQ Past Papers</button>
    <button class="filter-btn" onclick="filterQuestions('expected', this)">Expected 2026</button>
    <button class="filter-btn" onclick="filterQuestions('referenced', this)">Referenced Resources</button>
  </div>

  <div id="questions-container"></div>

  <div class="actions">
    <button class="btn" id="submit-btn" onclick="submitTest()">Submit & View Explanations</button>
  </div>
</div>

<script>
const questions = {q_json_str};
let userAnswers = {{}};
let submitted = false;

function renderQuestions(filter = 'all') {{
  const container = document.getElementById('questions-container');
  container.innerHTML = '';

  questions.forEach((q, idx) => {{
    if (filter !== 'all' && q.label !== filter) return;

    const card = document.createElement('div');
    card.className = 'card';
    card.id = `q-card-${{idx}}`;

    let tagClass = 'tag-pyq';
    if (q.label === 'expected') tagClass = 'tag-expected';
    else if (q.label === 'referenced') tagClass = 'tag-referenced';

    let optionsHtml = '';
    q.options.forEach(opt => {{
      const isChecked = userAnswers[idx] === opt.label ? 'checked' : '';
      optionsHtml += `
        <label class="option-label" id="opt-${{idx}}-${{opt.label}}">
          <input type="radio" name="q-${{idx}}" value="${{opt.label}}" ${{isChecked}} onchange="selectAnswer(${{idx}}, '${{opt.label}}')" ${{submitted ? 'disabled' : ''}}>
          <span><strong>${{opt.label}}.</strong> ${{opt.text}}</span>
        </label>
      `;
    }});

    card.innerHTML = `
      <div class="card-header">
        <span class="q-num">Question ${{idx + 1}} (${{q.subject}})</span>
        <span class="tag ${{tagClass}}">${{q.label}}: ${{q.origin_tag || q.label}}</span>
      </div>
      <div class="q-text">${{q.text}}</div>
      ${{q.text_alt ? `<div class="q-alt">${{q.text_alt}}</div>` : ''}}
      <div class="options">
        ${{optionsHtml}}
      </div>
      <div class="explanation" id="exp-${{idx}}">
        <strong>Correct Answer: ${{q.answer}}</strong><br>
        ${{q.explanation}}
      </div>
    `;

    container.appendChild(card);
  }});
}}

function selectAnswer(qIdx, optLabel) {{
  userAnswers[qIdx] = optLabel;
}}

function filterQuestions(filter, btn) {{
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderQuestions(filter);
  if (submitted) updateSubmittedUI();
}}

function submitTest() {{
  if (submitted) return;
  submitted = true;
  clearInterval(timerInterval);

  let score = 0;
  questions.forEach((q, idx) => {{
    if (userAnswers[idx] === q.answer) score++;
  }});

  const scoreBadge = document.getElementById('score');
  scoreBadge.innerText = `Score: ${{score}} / ${{questions.length}} (${{Math.round((score / questions.length) * 100)}}%)`;
  scoreBadge.style.display = 'block';

  document.getElementById('submit-btn').innerText = 'Test Completed';
  document.getElementById('submit-btn').disabled = true;

  updateSubmittedUI();
}}

function updateSubmittedUI() {{
  questions.forEach((q, idx) => {{
    const exp = document.getElementById(`exp-${{idx}}`);
    if (exp) exp.style.display = 'block';

    q.options.forEach(opt => {{
      const optEl = document.getElementById(`opt-${{idx}}-${{opt.label}}`);
      if (optEl) {{
        if (opt.label === q.answer) {{
          optEl.classList.add('correct');
        }} else if (userAnswers[idx] === opt.label && opt.label !== q.answer) {{
          optEl.classList.add('incorrect');
        }}
      }}
    }});
  }});
}}

// Timer (30 minutes countdown)
let seconds = 30 * 60;
const timerEl = document.getElementById('timer');
const timerInterval = setInterval(() => {{
  if (seconds <= 0) {{
    clearInterval(timerInterval);
    submitTest();
    return;
  }}
  seconds--;
  const m = Math.floor(seconds / 60).toString().padStart(2, '0');
  const s = (seconds % 60).toString().padStart(2, '0');
  timerEl.innerText = `Time: ${{m}}:${{s}}`;
}}, 1000);

renderQuestions();
</script>
</body>
</html>
"""
    return html_content

# Write Paper 1 Mock
p1_html = generate_html("Paper 1 General Studies & Educational Mock Test", "P1", p1_questions)
p1_file = os.path.join(mock_dir, "Mock_P1_Full.html")
with open(p1_file, "w", encoding="utf-8") as f:
    f.write(p1_html)
print(f"Generated {p1_file} ({len(p1_questions)} questions)")

# Write Paper 2 Mock
p2_html = generate_html("Paper 2 Computer Science Technical Mock Test", "P2", p2_questions)
p2_file = os.path.join(mock_dir, "Mock_P2_Full.html")
with open(p2_file, "w", encoding="utf-8") as f:
    f.write(p2_html)
print(f"Generated {p2_file} ({len(p2_questions)} questions)")

# Remove legacy Mock_*_v1.html to ensure no -v1/-v2 duplicates remain
for legacy in ["Mock_P1_Full_v1.html", "Mock_P2_Full_v1.html"]:
    leg_path = os.path.join(mock_dir, legacy)
    if os.path.exists(leg_path):
        os.remove(leg_path)
        print(f"Removed legacy version: {legacy}")
