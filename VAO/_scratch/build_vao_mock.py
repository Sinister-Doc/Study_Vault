import os
import re
import json

BASE_DIR = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\VAO"
REVIEW_DIR = os.path.join(BASE_DIR, r"AGY\08_Paper_Review")
OUTPUT_HTML = os.path.join(BASE_DIR, "VAO_MockTest.html")

def md_table_to_html(text):
    lines = text.split('\n')
    output = []
    in_table = False
    table_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            in_table = True
            table_lines.append(stripped)
        else:
            if in_table:
                output.append(render_table(table_lines))
                table_lines = []
                in_table = False
            output.append(line)
            
    if in_table:
        output.append(render_table(table_lines))
        
    return '\n'.join(output)

def render_table(lines):
    if not lines:
        return ""
    html = ['<table class="content-table">']
    has_header = False
    
    if len(lines) > 1 and re.match(r'^\|[\s:-|-]+\|$', lines[1]):
        has_header = True
        
    if has_header:
        headers = [c.strip() for c in lines[0].split('|')[1:-1]]
        html.append('<thead><tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr></thead>')
        body_lines = lines[2:]
    else:
        body_lines = lines
        
    html.append('<tbody>')
    for row in body_lines:
        cells = [c.strip() for c in row.split('|')[1:-1]]
        html.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
    html.append('</tbody></table>')
    return ''.join(html)

def clean_formatting(text):
    if not text:
        return ""
    # Remove null bytes / bad OCR chars
    text = text.replace('\x00', '').replace('\u0000', '')
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Convert tables
    text = md_table_to_html(text)
    # Convert line breaks
    text = re.sub(r'\n{2,}', '<br><br>', text)
    text = text.replace('\n', '<br>')
    return text.strip()

def parse_evaluation(file_path):
    answers = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for line in content.splitlines():
        line = line.strip()
        if not line.startswith('|'):
            continue
        cols = [c.strip() for c in line.split('|')]
        # Expected: ['', 'Q#', 'QID', 'Summary', 'Marked', 'Key', 'Status', 'Marks', 'Reasoning', '']
        if len(cols) >= 9:
            raw_id = cols[2].replace('`', '').strip()
            if not re.match(r'^P[12]-Q\d{3}$', raw_id):
                continue
            raw_key = cols[5].replace('`', '').strip()
            rationale = cols[8].strip().replace('\x00', '')
            try:
                key_int = int(raw_key)
            except ValueError:
                key_int = None
            answers[raw_id] = {
                'key': key_int,
                'rationale': rationale
            }
    return answers

def parse_questions(file_path, answers):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = re.compile(r'(?m)^(P[12]-Q\d{3})\s*·\s*p\.(\d+)\s*·\s*confidence:\s*(\w+)')
    matches = list(pattern.finditer(content))
    
    questions = []
    
    for i, m in enumerate(matches):
        qid = m.group(1)
        qnum = int(qid.split('-Q')[1])
        start_idx = m.end()
        end_idx = matches[i+1].start() if i+1 < len(matches) else len(content)
        chunk = content[start_idx:end_idx]
        
        # Extract Question text
        q_match = re.search(r'Question:\s*(.*?)(?=\n-\s*\[\s*\]\s*\(1\))', chunk, re.DOTALL)
        if not q_match:
            print(f"WARNING: Question text not found for {qid}")
            q_text = "Question text missing"
        else:
            q_text = q_match.group(1).strip()
            
        # Extract options
        opt_matches = [
            re.search(r'-\s*\[\s*\]\s*\(1\)\s*(.*?)(?=\n-\s*\[\s*\]\s*\(2\))', chunk, re.DOTALL),
            re.search(r'-\s*\[\s*\]\s*\(2\)\s*(.*?)(?=\n-\s*\[\s*\]\s*\(3\))', chunk, re.DOTALL),
            re.search(r'-\s*\[\s*\]\s*\(3\)\s*(.*?)(?=\n-\s*\[\s*\]\s*\(4\))', chunk, re.DOTALL),
            re.search(r'-\s*\[\s*\]\s*\(4\)\s*(.*?)(?=\n(?:-\s*\[\s*\]\s*\(5\)|>\s*\[!warning\]|---|P[12]-Q|\Z))', chunk, re.DOTALL)
        ]
        
        options = []
        for opt_idx, om in enumerate(opt_matches):
            if om:
                raw_opt = om.group(1).strip()
                raw_opt = re.split(r'\n>\s*\[!warning\]', raw_opt)[0].strip()
                options.append(clean_formatting(raw_opt))
            else:
                options.append(f"Option {opt_idx + 1}")
                
        ans_info = answers.get(qid, {})
        key = ans_info.get('key', None)
        rationale = ans_info.get('rationale', "Answer not available")
        
        questions.append({
            "id": qid,
            "number": qnum,
            "text": clean_formatting(q_text),
            "options": options,
            "correct_answer": key,
            "rationale": clean_formatting(rationale)
        })
        
    return questions

def generate_html(exam_data):
    json_data_str = json.dumps(exam_data, ensure_ascii=False)
    
    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KEA VAO 2026 — Mock Test & Answer Key (ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ)</title>
<style>
:root {{
    --bg-page: #f8f9fa;
    --bg-card: #ffffff;
    --text-primary: #1f2328;
    --text-secondary: #656d76;
    --border-color: #d0d7de;
    --border-light: #eaeef2;
    --btn-primary-bg: #24292f;
    --btn-primary-text: #ffffff;
    --btn-primary-hover: #32383f;
    --btn-secondary-bg: #ffffff;
    --btn-secondary-text: #24292f;
    --btn-secondary-hover: #f3f4f6;
    --success-bg: #dafbe1;
    --success-border: #4ac26b;
    --success-text: #1a7f37;
    --danger-bg: #ffebe9;
    --danger-border: #ff8182;
    --danger-text: #cf222e;
    --warning-bg: #fff8c5;
    --warning-border: #d4a72c;
    --warning-text: #9a6700;
    --active-outline: #0969da;
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans Kannada", "Tunga", "Kedage", sans-serif;
    background-color: var(--bg-page);
    color: var(--text-primary);
    line-height: 1.6;
    font-size: 15px;
}}

.app-header {{
    background: var(--bg-card);
    border-bottom: 1px solid var(--border-color);
    padding: 16px 24px;
}}

.app-header-content {{
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.app-header h1 {{
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
}}

.app-header p {{
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-top: 2px;
}}

.container {{
    max-width: 1200px;
    margin: 24px auto;
    padding: 0 20px;
}}

/* Cards & Layout */
.card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 24px;
    margin-bottom: 20px;
}}

.landing-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
    gap: 20px;
    margin-top: 20px;
}}

.paper-card h2 {{
    font-size: 1.2rem;
    margin-bottom: 8px;
    font-weight: 600;
}}

.paper-meta {{
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-bottom: 16px;
    line-height: 1.6;
}}

.btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 16px;
    font-size: 0.875rem;
    font-weight: 500;
    border-radius: 6px;
    border: 1px solid var(--border-color);
    cursor: pointer;
    background: var(--btn-secondary-bg);
    color: var(--btn-secondary-text);
    text-decoration: none;
    transition: background 0.1s ease;
}}

.btn:hover {{
    background: var(--btn-secondary-hover);
}}

.btn-primary {{
    background: var(--btn-primary-bg);
    color: var(--btn-primary-text);
    border-color: var(--btn-primary-bg);
}}

.btn-primary:hover {{
    background: var(--btn-primary-hover);
}}

.btn:disabled {{
    opacity: 0.5;
    cursor: not-allowed;
}}

.button-group {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}}

/* Test Layout */
.test-layout {{
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 20px;
    align-items: start;
}}

@media (max-width: 900px) {{
    .test-layout {{
        grid-template-columns: 1fr;
    }}
}}

.test-topbar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 12px 20px;
    margin-bottom: 20px;
}}

.timer-box {{
    font-size: 1.15rem;
    font-weight: 700;
    font-family: monospace;
    background: #f6f8fa;
    padding: 6px 14px;
    border-radius: 4px;
    border: 1px solid var(--border-color);
}}

.q-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-light);
}}

.q-title {{
    font-weight: 600;
    font-size: 1.1rem;
}}

.q-body {{
    font-size: 1.05rem;
    line-height: 1.6;
    margin-bottom: 24px;
}}

/* Content Table inside questions */
.content-table {{
    border-collapse: collapse;
    margin: 14px 0;
    width: 100%;
    font-size: 0.95rem;
}}

.content-table th, .content-table td {{
    border: 1px solid var(--border-color);
    padding: 8px 12px;
    text-align: left;
}}

.content-table th {{
    background-color: #f6f8fa;
    font-weight: 600;
}}

/* Options */
.options-list {{
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 24px;
}}

.option-item {{
    display: flex;
    align-items: flex-start;
    padding: 12px 16px;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    cursor: pointer;
    background: var(--bg-card);
    transition: border-color 0.1s ease;
}}

.option-item:hover {{
    background: #f6f8fa;
}}

.option-item input[type="radio"] {{
    margin-top: 4px;
    margin-right: 12px;
    cursor: pointer;
}}

.option-text {{
    flex: 1;
    font-size: 1rem;
    line-height: 1.5;
}}

/* Palette */
.palette-card {{
    position: sticky;
    top: 20px;
}}

.palette-legend {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin-bottom: 14px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border-light);
}}

.legend-item {{
    display: flex;
    align-items: center;
    gap: 6px;
}}

.legend-swatch {{
    width: 12px;
    height: 12px;
    border-radius: 2px;
    border: 1px solid var(--border-color);
}}

.palette-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 6px;
    max-height: 400px;
    overflow-y: auto;
    padding-right: 4px;
    margin-bottom: 16px;
}}

.pal-btn {{
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    background: #ffffff;
    font-size: 0.85rem;
    font-weight: 500;
    cursor: pointer;
}}

.pal-btn:hover {{
    filter: brightness(0.95);
}}

.pal-btn.answered {{
    background: var(--success-bg);
    border-color: var(--success-border);
    color: var(--success-text);
}}

.pal-btn.marked {{
    background: var(--warning-bg);
    border-color: var(--warning-border);
    color: var(--warning-text);
}}

.pal-btn.active {{
    outline: 2px solid var(--active-outline);
    outline-offset: 1px;
    font-weight: 700;
}}

/* Post-Test & Review */
.score-summary {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin: 20px 0;
}}

.score-box {{
    background: #f6f8fa;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 16px;
    text-align: center;
}}

.score-box .num {{
    font-size: 1.75rem;
    font-weight: 700;
    margin-top: 4px;
}}

.badge {{
    display: inline-block;
    padding: 3px 8px;
    font-size: 0.75rem;
    font-weight: 600;
    border-radius: 12px;
    margin-bottom: 8px;
}}

.badge-correct {{ background: var(--success-bg); color: var(--success-text); border: 1px solid var(--success-border); }}
.badge-wrong {{ background: var(--danger-bg); color: var(--danger-text); border: 1px solid var(--danger-border); }}
.badge-unattempted {{ background: #f6f8fa; color: var(--text-secondary); border: 1px solid var(--border-color); }}

.review-item {{
    border-bottom: 1px solid var(--border-color);
    padding: 24px 0;
}}

.review-item:last-child {{
    border-bottom: none;
}}

.opt-review {{
    padding: 10px 14px;
    border-radius: 4px;
    border: 1px solid var(--border-light);
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
}}

.opt-review.is-correct {{
    background: var(--success-bg);
    border-color: var(--success-border);
    color: var(--success-text);
    font-weight: 500;
}}

.opt-review.is-wrong {{
    background: var(--danger-bg);
    border-color: var(--danger-border);
    color: var(--danger-text);
}}

.rationale-box {{
    background: #fcfcfc;
    border-left: 3px solid #656d76;
    padding: 12px 16px;
    margin-top: 14px;
    font-size: 0.95rem;
    color: #24292f;
}}

/* Modal */
.modal-overlay {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.4);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}}

.modal {{
    background: #ffffff;
    border-radius: 6px;
    padding: 24px;
    max-width: 480px;
    width: 90%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}}

.modal h3 {{
    margin-bottom: 12px;
}}

.modal-stats {{
    background: #f6f8fa;
    padding: 12px 16px;
    border-radius: 4px;
    margin: 16px 0;
    font-size: 0.9rem;
    line-height: 1.8;
}}

@media print {{
    .app-header, .btn, .palette-card, .controls, .test-topbar {{
        display: none !important;
    }}
    .test-layout {{
        display: block;
    }}
    body {{
        background: #ffffff;
    }}
    .card {{
        border: none;
        padding: 0;
    }}
}}
</style>
</head>
<body>

<header class="app-header">
    <div class="app-header-content">
        <div>
            <h1>KEA VAO 2026 Examination (ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ)</h1>
            <p>Official Paper Review & Interactive Mock Test Portal</p>
        </div>
        <div id="header-nav">
            <!-- Nav buttons populated by JS -->
        </div>
    </div>
</header>

<main class="container" id="main-view">
    <!-- Dynamic views rendered here -->
</main>

<div class="modal-overlay" id="submit-modal">
    <div class="modal">
        <h3>Submit Mock Examination</h3>
        <p>Are you sure you want to conclude and submit your exam?</p>
        <div class="modal-stats" id="modal-summary"></div>
        <div class="button-group" style="justify-content: flex-end;">
            <button class="btn" onclick="closeSubmitModal()">Continue Exam</button>
            <button class="btn btn-primary" onclick="confirmSubmit()">Confirm & Submit</button>
        </div>
    </div>
</div>

<script>
const EXAM_DATA = {json_data_str};

const state = {{
    view: 'home',
    paperIndex: 0,
    currentQuestion: 0,
    answers: {{}},
    markedReview: {{}},
    timeRemaining: 0,
    timerId: null,
    submitted: false
}};

function init() {{
    render();
}}

function render() {{
    const main = document.getElementById('main-view');
    const nav = document.getElementById('header-nav');
    
    if (state.view === 'home') {{
        nav.innerHTML = '';
        main.innerHTML = renderHome();
    }} else if (state.view === 'mock') {{
        nav.innerHTML = '<button class="btn" onclick="confirmExitTest()">Exit to Home</button>';
        main.innerHTML = renderMockTest();
        updatePalette();
    }} else if (state.view === 'result') {{
        nav.innerHTML = '<button class="btn" onclick="goHome()">Home</button>';
        main.innerHTML = renderResults();
    }} else if (state.view === 'key') {{
        nav.innerHTML = '<button class="btn" onclick="goHome()">Home</button> <button class="btn btn-primary" onclick="window.print()">Print Key</button>';
        main.innerHTML = renderAnswerKey();
    }}
}}

function renderHome() {{
    let html = `
        <div class="card">
            <h2>Welcome to KEA VAO 2026 Test Engine</h2>
            <p style="color: var(--text-secondary); margin-top: 4px;">
                Digitized from official Village Administrative Officer question papers and authoritative evaluation reports.
                Practice under real exam conditions or review full question solutions offline.
            </p>
        </div>
        <div class="landing-grid">
    `;
    
    EXAM_DATA.papers.forEach((p, idx) => {{
        html += `
            <div class="card paper-card">
                <h2>${{p.paper}}: ${{p.title}}</h2>
                <div class="paper-meta">
                    <strong>Duration:</strong> ${{p.duration_minutes}} Minutes (2 Hours)<br>
                    <strong>Questions:</strong> ${{p.total_questions}} Multiple-Choice Questions<br>
                    <strong>Marking:</strong> +${{p.marking.correct}} for correct, ${{p.marking.wrong}} for incorrect, 0.00 for unattempted
                </div>
                <div class="button-group">
                    <button class="btn btn-primary" onclick="startMockTest(${{idx}})">Take Mock Test</button>
                    <button class="btn" onclick="viewAnswerKey(${{idx}})">View Answer Key</button>
                </div>
            </div>
        `;
    }});
    
    html += '</div>';
    return html;
}}

function startMockTest(paperIdx) {{
    state.view = 'mock';
    state.paperIndex = paperIdx;
    state.currentQuestion = 0;
    state.answers = {{}};
    state.markedReview = {{}};
    state.submitted = false;
    state.timeRemaining = EXAM_DATA.papers[paperIdx].duration_minutes * 60;
    
    clearInterval(state.timerId);
    state.timerId = setInterval(() => {{
        if (state.timeRemaining > 0) {{
            state.timeRemaining--;
            updateTimerDisplay();
        }} else {{
            clearInterval(state.timerId);
            alert("Exam duration ended. Your test will now be submitted automatically.");
            confirmSubmit();
        }}
    }}, 1000);
    
    render();
}}

function updateTimerDisplay() {{
    const el = document.getElementById('timer-display');
    if (!el) return;
    const m = Math.floor(state.timeRemaining / 60);
    const s = state.timeRemaining % 60;
    el.textContent = `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
}}

function renderMockTest() {{
    const paper = EXAM_DATA.papers[state.paperIndex];
    const q = paper.questions[state.currentQuestion];
    const userAns = state.answers[state.currentQuestion];
    const isMarked = !!state.markedReview[state.currentQuestion];
    
    let optionsHtml = '';
    for (let i = 0; i < 4; i++) {{
        const optNum = i + 1;
        const checked = userAns === optNum ? 'checked' : '';
        optionsHtml += `
            <label class="option-item">
                <input type="radio" name="mock_opt" value="${{optNum}}" ${{checked}} onchange="selectOption(${{optNum}})">
                <div class="option-text"><strong>(${{optNum}})</strong> ${{q.options[i]}}</div>
            </label>
        `;
    }}
    
    let paletteBtns = '';
    paper.questions.forEach((_, idx) => {{
        let cls = 'pal-btn';
        if (state.answers[idx]) cls += ' answered';
        if (state.markedReview[idx]) cls += ' marked';
        if (idx === state.currentQuestion) cls += ' active';
        paletteBtns += `<button class="${{cls}}" id="pal-btn-${{idx}}" onclick="jumpToQuestion(${{idx}})">${{idx + 1}}</button>`;
    }});
    
    const m = Math.floor(state.timeRemaining / 60);
    const s = state.timeRemaining % 60;
    const timeStr = `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
    
    return `
        <div class="test-topbar">
            <div>
                <strong>${{paper.paper}}: ${{paper.title}}</strong>
                <span style="color: var(--text-secondary); margin-left: 12px;">Question ${{state.currentQuestion + 1}} of ${{paper.total_questions}}</span>
            </div>
            <div class="timer-box" id="timer-display">${{timeStr}}</div>
        </div>
        
        <div class="test-layout">
            <div class="card" style="margin-bottom: 0;">
                <div class="q-header">
                    <div class="q-title">Question ${{q.number}} (${{q.id}})</div>
                    <div>
                        <button class="btn" style="${{isMarked ? 'background: var(--warning-bg); border-color: var(--warning-border); color: var(--warning-text);' : ''}}" onclick="toggleMarkReview()">
                            ${{isMarked ? '★ Marked for Review' : '☆ Mark for Review'}}
                        </button>
                    </div>
                </div>
                
                <div class="q-body">${{q.text}}</div>
                
                <div class="options-list">${{optionsHtml}}</div>
                
                <div class="button-group" style="justify-content: space-between; border-top: 1px solid var(--border-light); padding-top: 16px;">
                    <div>
                        <button class="btn" onclick="clearResponse()" ${{userAns ? '' : 'disabled'}}>Clear Response</button>
                    </div>
                    <div class="button-group">
                        <button class="btn" onclick="prevQuestion()" ${{state.currentQuestion === 0 ? 'disabled' : ''}}>Previous</button>
                        <button class="btn btn-primary" onclick="nextQuestion()" ${{state.currentQuestion === paper.total_questions - 1 ? 'disabled' : ''}}>Next</button>
                    </div>
                </div>
            </div>
            
            <div class="card palette-card">
                <h3 style="font-size: 1rem; margin-bottom: 12px;">Question Navigator</h3>
                <div class="palette-legend">
                    <div class="legend-item"><div class="legend-swatch" style="background: var(--success-bg); border-color: var(--success-border);"></div> Answered</div>
                    <div class="legend-item"><div class="legend-swatch" style="background: var(--warning-bg); border-color: var(--warning-border);"></div> Marked</div>
                    <div class="legend-item"><div class="legend-swatch" style="background: #ffffff;"></div> Unanswered</div>
                    <div class="legend-item"><div class="legend-swatch" style="border: 2px solid var(--active-outline);"></div> Current</div>
                </div>
                <div class="palette-grid">${{paletteBtns}}</div>
                <button class="btn btn-primary" style="width: 100%; margin-top: 8px;" onclick="openSubmitModal()">Submit Test</button>
            </div>
        </div>
    `;
}}

function selectOption(optNum) {{
    state.answers[state.currentQuestion] = optNum;
    updatePalette();
    const clearBtn = document.querySelector('button[onclick="clearResponse()"]');
    if (clearBtn) clearBtn.disabled = false;
}}

function clearResponse() {{
    delete state.answers[state.currentQuestion];
    render();
}}

function toggleMarkReview() {{
    if (state.markedReview[state.currentQuestion]) {{
        delete state.markedReview[state.currentQuestion];
    }} else {{
        state.markedReview[state.currentQuestion] = true;
    }}
    render();
}}

function nextQuestion() {{
    const paper = EXAM_DATA.papers[state.paperIndex];
    if (state.currentQuestion < paper.total_questions - 1) {{
        state.currentQuestion++;
        render();
    }}
}}

function prevQuestion() {{
    if (state.currentQuestion > 0) {{
        state.currentQuestion--;
        render();
    }}
}}

function jumpToQuestion(idx) {{
    state.currentQuestion = idx;
    render();
}}

function updatePalette() {{
    const paper = EXAM_DATA.papers[state.paperIndex];
    paper.questions.forEach((_, idx) => {{
        const btn = document.getElementById(`pal-btn-${{idx}}`);
        if (!btn) return;
        btn.className = 'pal-btn';
        if (state.answers[idx]) btn.classList.add('answered');
        if (state.markedReview[idx]) btn.classList.add('marked');
        if (idx === state.currentQuestion) btn.classList.add('active');
    }});
}}

function openSubmitModal() {{
    const paper = EXAM_DATA.papers[state.paperIndex];
    const total = paper.total_questions;
    const answered = Object.keys(state.answers).length;
    const marked = Object.keys(state.markedReview).length;
    const unattempted = total - answered;
    
    document.getElementById('modal-summary').innerHTML = `
        <strong>Total Questions:</strong> ${{total}}<br>
        <strong>Answered:</strong> ${{answered}}<br>
        <strong>Marked for Review:</strong> ${{marked}}<br>
        <strong>Unattempted:</strong> ${{unattempted}}
    `;
    document.getElementById('submit-modal').style.display = 'flex';
}}

function closeSubmitModal() {{
    document.getElementById('submit-modal').style.display = 'none';
}}

function confirmSubmit() {{
    clearInterval(state.timerId);
    closeSubmitModal();
    state.view = 'result';
    state.submitted = true;
    render();
}}

function confirmExitTest() {{
    if (confirm("Are you sure you want to exit the mock test? Current progress will be lost.")) {{
        clearInterval(state.timerId);
        goHome();
    }}
}}

function renderResults() {{
    const paper = EXAM_DATA.papers[state.paperIndex];
    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;
    
    paper.questions.forEach((q, idx) => {{
        const userAns = state.answers[idx];
        if (userAns === undefined || userAns === null) {{
            unattemptedCount++;
        }} else if (userAns === q.correct_answer) {{
            correctCount++;
        }} else {{
            wrongCount++;
        }}
    }});
    
    const netMarks = (correctCount * paper.marking.correct) + (wrongCount * paper.marking.wrong);
    const attempted = correctCount + wrongCount;
    const accuracy = attempted > 0 ? ((correctCount / attempted) * 100).toFixed(1) : 0;
    
    let reviewHtml = '';
    paper.questions.forEach((q, idx) => {{
        const userAns = state.answers[idx];
        const isCorrect = userAns === q.correct_answer;
        const isUnattempted = userAns === undefined || userAns === null;
        
        let badgeClass = isUnattempted ? 'badge-unattempted' : (isCorrect ? 'badge-correct' : 'badge-wrong');
        let badgeText = isUnattempted ? 'Unattempted (0.00)' : (isCorrect ? `Correct (+${{paper.marking.correct.toFixed(2)}})` : `Incorrect (${{paper.marking.wrong.toFixed(2)}})`);
        
        let optionsHtml = '';
        for (let i = 0; i < 4; i++) {{
            const optNum = i + 1;
            let optClass = 'opt-review';
            let label = '';
            
            if (optNum === q.correct_answer) {{
                optClass += ' is-correct';
                label = ' ✓ Correct Answer';
            }}
            if (optNum === userAns) {{
                if (!isCorrect) optClass += ' is-wrong';
                label += ' (Your Response)';
            }}
            
            optionsHtml += `
                <div class="${{optClass}}">
                    <div><strong>(${{optNum}})</strong> ${{q.options[i]}}</div>
                    <div style="font-size: 0.85rem; font-weight: 600;">${{label}}</div>
                </div>
            `;
        }}
        
        reviewHtml += `
            <div class="review-item">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="badge ${{badgeClass}}">${{badgeText}}</span>
                    <span style="font-size: 0.85rem; color: var(--text-secondary);">Question ${{q.number}} (${{q.id}})</span>
                </div>
                <div style="font-size: 1.05rem; margin: 12px 0;">${{q.text}}</div>
                <div style="margin-bottom: 12px;">${{optionsHtml}}</div>
                <div class="rationale-box">
                    <strong>Official Rationale / Solution:</strong><br>
                    ${{q.rationale}}
                </div>
            </div>
        `;
    }});
    
    return `
        <div class="card">
            <h2>Examination Performance Summary</h2>
            <p style="color: var(--text-secondary);">${{paper.paper}}: ${{paper.title}}</p>
            
            <div class="score-summary">
                <div class="score-box">
                    <div style="color: var(--text-secondary); font-size: 0.85rem;">NET SCORE</div>
                    <div class="num" style="color: ${{netMarks >= 50 ? 'var(--success-text)' : 'var(--text-primary)'}};">${{netMarks.toFixed(2)}}</div>
                    <div style="font-size: 0.8rem; color: var(--text-secondary);">out of ${{paper.total_questions}}.00</div>
                </div>
                <div class="score-box">
                    <div style="color: var(--text-secondary); font-size: 0.85rem;">ACCURACY</div>
                    <div class="num">${{accuracy}}%</div>
                    <div style="font-size: 0.8rem; color: var(--text-secondary);">${{correctCount}} / ${{attempted}} attempted</div>
                </div>
                <div class="score-box">
                    <div style="color: var(--text-secondary); font-size: 0.85rem;">CORRECT</div>
                    <div class="num" style="color: var(--success-text);">${{correctCount}}</div>
                    <div style="font-size: 0.8rem; color: var(--text-secondary);">+${{(correctCount * paper.marking.correct).toFixed(2)}} Marks</div>
                </div>
                <div class="score-box">
                    <div style="color: var(--text-secondary); font-size: 0.85rem;">WRONG</div>
                    <div class="num" style="color: var(--danger-text);">${{wrongCount}}</div>
                    <div style="font-size: 0.8rem; color: var(--text-secondary);">${{(wrongCount * paper.marking.wrong).toFixed(2)}} Marks</div>
                </div>
                <div class="score-box">
                    <div style="color: var(--text-secondary); font-size: 0.85rem;">UNATTEMPTED</div>
                    <div class="num" style="color: var(--text-secondary);">${{unattemptedCount}}</div>
                    <div style="font-size: 0.8rem; color: var(--text-secondary);">0.00 Penalty</div>
                </div>
            </div>
            
            <div class="button-group" style="margin-top: 20px;">
                <button class="btn btn-primary" onclick="startMockTest(${{state.paperIndex}})">Retake Mock Test</button>
                <button class="btn" onclick="goHome()">Back to Home</button>
                <button class="btn" onclick="window.print()">Print Scorecard</button>
            </div>
        </div>
        
        <div class="card">
            <h3>Detailed Question-by-Question Review</h3>
            ${{reviewHtml}}
        </div>
    `;
}}

function viewAnswerKey(paperIdx) {{
    state.view = 'key';
    state.paperIndex = paperIdx;
    render();
}}

function renderAnswerKey() {{
    const paper = EXAM_DATA.papers[state.paperIndex];
    
    let listHtml = '';
    paper.questions.forEach((q) => {{
        let optionsHtml = '';
        for (let i = 0; i < 4; i++) {{
            const optNum = i + 1;
            let optClass = 'opt-review';
            let label = '';
            if (optNum === q.correct_answer) {{
                optClass += ' is-correct';
                label = ' ✓ Official Key';
            }}
            optionsHtml += `
                <div class="${{optClass}}">
                    <div><strong>(${{optNum}})</strong> ${{q.options[i]}}</div>
                    <div style="font-size: 0.85rem; font-weight: 600;">${{label}}</div>
                </div>
            `;
        }}
        
        listHtml += `
            <div class="review-item">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 600; font-size: 1.05rem;">Question ${{q.number}} (${{q.id}})</span>
                    <span class="badge badge-correct">Key: Option (${{q.correct_answer}})</span>
                </div>
                <div style="font-size: 1.05rem; margin: 12px 0;">${{q.text}}</div>
                <div style="margin-bottom: 12px;">${{optionsHtml}}</div>
                <div class="rationale-box">
                    <strong>Official Rationale / Solution:</strong><br>
                    ${{q.rationale}}
                </div>
            </div>
        `;
    }});
    
    return `
        <div class="card">
            <h2>Official Answer Key & Detailed Rationale</h2>
            <p style="color: var(--text-secondary); margin-bottom: 16px;">${{paper.paper}}: ${{paper.title}} · 100 Questions</p>
            <div class="button-group">
                <button class="btn btn-primary" onclick="startMockTest(${{state.paperIndex}})">Take This Mock Test</button>
                <button class="btn" onclick="goHome()">Back to Home</button>
                <button class="btn" onclick="window.print()">Print Answer Key</button>
            </div>
        </div>
        <div class="card">
            ${{listHtml}}
        </div>
    `;
}}

function goHome() {{
    state.view = 'home';
    render();
}}

init();
</script>
</body>
</html>
"""
    return html

def main():
    p1_eval = os.path.join(REVIEW_DIR, "Paper1_Evaluation.md")
    p1_ques = os.path.join(REVIEW_DIR, "Paper1_Questions.md")
    p2_eval = os.path.join(REVIEW_DIR, "Paper2_Evaluation.md")
    p2_ques = os.path.join(REVIEW_DIR, "Paper2_Questions.md")
    
    print("Parsing VAO evaluations...")
    ans1 = parse_evaluation(p1_eval)
    ans2 = parse_evaluation(p2_eval)
    print(f"Paper 1 evaluation entries: {len(ans1)}")
    print(f"Paper 2 evaluation entries: {len(ans2)}")
    
    print("Parsing VAO questions...")
    q1 = parse_questions(p1_ques, ans1)
    q2 = parse_questions(p2_ques, ans2)
    print(f"Paper 1 questions parsed: {len(q1)}")
    print(f"Paper 2 questions parsed: {len(q2)}")
    
    assert len(q1) == 100, f"Expected 100 questions in P1, got {len(q1)}"
    assert len(q2) == 100, f"Expected 100 questions in P2, got {len(q2)}"
    
    for q in q1 + q2:
        assert q['correct_answer'] in [1, 2, 3, 4], f"Invalid answer key for {q['id']}: {q['correct_answer']}"
        assert len(q['options']) == 4, f"Options count != 4 for {q['id']}: {len(q['options'])}"
        assert q['rationale'] and q['rationale'] != "Answer not available", f"Missing rationale for {q['id']}"
        
    print("All 200 questions, options, keys, and rationales validated 100%!")
    
    exam_data = {
        "exam": "KEA Village Administrative Officer (VAO) Competitive Examination 2026",
        "papers": [
            {
                "paper": "Paper 1",
                "title": "General Knowledge (ಸಾಮಾನ್ಯ ಜ್ಞಾನ)",
                "duration_minutes": 120,
                "total_questions": 100,
                "marking": { "correct": 1.0, "wrong": -0.25, "unattempted": 0.0 },
                "questions": q1
            },
            {
                "paper": "Paper 2",
                "title": "General Kannada, General English & Computer Knowledge",
                "duration_minutes": 120,
                "total_questions": 100,
                "marking": { "correct": 1.0, "wrong": -0.25, "unattempted": 0.0 },
                "questions": q2
            }
        ]
    }
    
    html = generate_html(exam_data)
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Successfully generated VAO_MockTest.html ({len(html)} bytes)")

if __name__ == "__main__":
    main()
