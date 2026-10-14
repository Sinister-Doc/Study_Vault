import os
import sys
import json
import re
sys.path.insert(0, os.path.dirname(__file__))
from safe_ops import safe_write, ROOT_DIR

CBT_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__EXAM_TITLE__</title>
<style>
:root {
  --bg-primary: #f8fafc;
  --bg-surface: #ffffff;
  --bg-surface-secondary: #f1f5f9;
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #64748b;
  --border-color: #cbd5e1;
  --primary-color: #1e3a8a;
  --primary-hover: #1e40af;
  --accent-color: #0284c7;
  
  /* Status Palette Colors (KPSC/NTA Standard) */
  --status-not-visited: #94a3b8;
  --status-not-answered: #dc2626;
  --status-answered: #16a34a;
  --status-marked: #9333ea;
  --status-marked-answered: #7e22ce;
  
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}

[data-theme="dark"] {
  --bg-primary: #0f172a;
  --bg-surface: #1e293b;
  --bg-surface-secondary: #334155;
  --text-primary: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --border-color: #334155;
  --primary-color: #3b82f6;
  --primary-hover: #60a5fa;
  --accent-color: #38bdf8;
  
  --status-not-visited: #64748b;
  --status-not-answered: #ef4444;
  --status-answered: #22c55e;
  --status-marked: #a855f7;
  --status-marked-answered: #9333ea;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-sans);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.5;
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
}

/* Header */
header {
  background-color: var(--bg-surface);
  border-bottom: 2px solid var(--border-color);
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
}
.header-title {
  display: flex;
  align-items: center;
  gap: 12px;
}
.exam-badge {
  background: var(--primary-color);
  color: #fff;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.exam-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
}
.header-controls {
  display: flex;
  align-items: center;
  gap: 20px;
}
.candidate-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-surface-secondary);
  padding: 6px 12px;
  border-radius: 20px;
  border: 1px solid var(--border-color);
  font-size: 0.85rem;
  font-weight: 600;
}
.candidate-avatar {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--primary-color);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
}
.timer-container {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-surface-secondary);
  padding: 6px 14px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
}
.timer-label { font-size: 0.8rem; font-weight: 600; color: var(--text-secondary); }
.timer-clock { font-family: var(--font-mono); font-size: 1.2rem; font-weight: 700; color: #dc2626; }
.theme-toggle-btn {
  background: none;
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
}

/* Main Container */
.cbt-container {
  display: flex;
  flex: 1;
  overflow: hidden;
}

/* Question Area */
.question-pane {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: var(--bg-surface);
  border-right: 2px solid var(--border-color);
  overflow: hidden;
}
.section-tabs-bar {
  background: var(--bg-surface-secondary);
  border-bottom: 1px solid var(--border-color);
  padding: 6px 16px;
  display: flex;
  gap: 8px;
  overflow-x: auto;
}
.section-tab {
  padding: 6px 16px;
  border-radius: 4px;
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  color: var(--text-secondary);
}
.section-tab.active {
  background: var(--primary-color);
  color: #fff;
  border-color: var(--primary-color);
}
.question-meta-bar {
  padding: 10px 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  background: var(--bg-surface);
}
.q-number-title { font-weight: 700; font-size: 1rem; color: var(--text-primary); }
.q-marks-badge {
  background: var(--bg-surface-secondary);
  border: 1px solid var(--border-color);
  padding: 2px 8px;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-weight: 600;
}
.question-scroll-content {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}
.question-text {
  font-size: 1.05rem;
  font-weight: 500;
  margin-bottom: 20px;
  white-space: pre-wrap;
  color: var(--text-primary);
}
.question-text table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 0.95rem;
}
.question-text th, .question-text td {
  border: 1px solid var(--border-color);
  padding: 8px 12px;
  text-align: left;
}
.question-text th {
  background: var(--bg-surface-secondary);
  font-weight: 600;
}
.options-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.option-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 16px;
  border: 1.5px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  background: var(--bg-surface);
  transition: all 0.15s ease;
}
.option-item:hover {
  border-color: var(--accent-color);
  background: var(--bg-surface-secondary);
}
.option-item.selected {
  border-color: var(--primary-color);
  background: rgba(30, 58, 138, 0.08);
}
[data-theme="dark"] .option-item.selected {
  background: rgba(59, 130, 246, 0.15);
}
.option-radio {
  margin-top: 4px;
  accent-color: var(--primary-color);
  width: 18px;
  height: 18px;
  cursor: pointer;
}
.option-label-pill {
  font-weight: 700;
  min-width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  background: var(--bg-surface-secondary);
  border: 1px solid var(--border-color);
  font-size: 0.85rem;
}
.option-text {
  flex: 1;
  font-size: 0.98rem;
  color: var(--text-primary);
}

/* Action Footer */
.question-footer {
  padding: 12px 20px;
  border-top: 2px solid var(--border-color);
  background: var(--bg-surface);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
}
.footer-left, .footer-right {
  display: flex;
  gap: 10px;
}
.btn {
  padding: 8px 16px;
  font-size: 0.88rem;
  font-weight: 600;
  border-radius: 6px;
  border: 1px solid transparent;
  cursor: pointer;
  transition: background 0.15s;
}
.btn-primary { background: var(--primary-color); color: #fff; }
.btn-primary:hover { background: var(--primary-hover); }
.btn-secondary { background: var(--bg-surface-secondary); border-color: var(--border-color); color: var(--text-primary); }
.btn-secondary:hover { background: var(--border-color); }
.btn-warning { background: #d97706; color: #fff; }
.btn-warning:hover { background: #b45309; }
.btn-purple { background: var(--status-marked); color: #fff; }
.btn-purple:hover { background: #7e22ce; }
.btn-danger { background: #dc2626; color: #fff; }
.btn-danger:hover { background: #b91c1c; }

/* Palette Pane */
.palette-pane {
  width: 320px;
  background: var(--bg-surface-secondary);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  flex-shrink: 0;
}
.palette-header {
  padding: 12px 16px;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-color);
  font-weight: 700;
  font-size: 0.95rem;
}
.palette-legend {
  padding: 12px 16px;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-color);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  font-size: 0.75rem;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
}
.legend-badge {
  width: 22px;
  height: 22px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: 700;
  font-size: 0.7rem;
}
.badge-not-visited { background: var(--status-not-visited); }
.badge-not-answered { background: var(--status-not-answered); }
.badge-answered { background: var(--status-answered); }
.badge-marked { background: var(--status-marked); }
.badge-marked-answered {
  background: var(--status-marked-answered);
  position: relative;
}
.badge-marked-answered::after {
  content: '';
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 5px;
  height: 5px;
  background: #22c55e;
  border-radius: 50%;
}
.palette-grid-container {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
}
.palette-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
}
.palette-btn {
  aspect-ratio: 1;
  border-radius: 6px;
  border: 1px solid rgba(0,0,0,0.1);
  color: #fff;
  font-weight: 700;
  font-size: 0.85rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.palette-btn.active-q {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}
.palette-footer {
  padding: 12px 16px;
  background: var(--bg-surface);
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: center;
}
.btn-submit-exam {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
}

/* Modals */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.modal-overlay.active { display: flex; }
.modal-dialog {
  background: var(--bg-surface);
  border-radius: 10px;
  width: 90%;
  max-width: 520px;
  padding: 24px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.3);
  border: 1px solid var(--border-color);
}
.modal-title { font-size: 1.2rem; font-weight: 700; margin-bottom: 12px; }
.summary-table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 0.9rem; }
.summary-table th, .summary-table td { padding: 8px 12px; border: 1px solid var(--border-color); }
.summary-table th { background: var(--bg-surface-secondary); }
.modal-actions { display: flex; justify-content: flex-end; gap: 10px; margin-top: 20px; }

/* Scorecard & Review Screen */
#screen-result {
  display: none;
  flex: 1;
  overflow-y: auto;
  padding: 30px 40px;
  background: var(--bg-primary);
}
.result-card {
  max-width: 900px;
  margin: 0 auto;
  background: var(--bg-surface);
  border-radius: 10px;
  padding: 30px;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.score-hero {
  display: flex;
  justify-content: space-around;
  padding: 24px;
  background: var(--bg-surface-secondary);
  border-radius: 8px;
  margin: 20px 0;
  text-align: center;
}
.hero-stat-value { font-size: 2.2rem; font-weight: 800; color: var(--primary-color); }
.hero-stat-label { font-size: 0.85rem; font-weight: 600; color: var(--text-secondary); text-transform: uppercase; }

.review-item {
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  background: var(--bg-surface);
}
.review-header { display: flex; justify-content: space-between; margin-bottom: 10px; font-weight: 700; }
.review-status-correct { color: #16a34a; }
.review-status-incorrect { color: #dc2626; }
.review-status-skipped { color: #64748b; }
.review-explanation {
  background: var(--bg-surface-secondary);
  border-left: 4px solid var(--primary-color);
  padding: 12px 16px;
  margin-top: 14px;
  border-radius: 0 4px 4px 0;
  font-size: 0.92rem;
}
.truth-value-box {
  background: rgba(2, 132, 199, 0.08);
  border: 1px solid var(--accent-color);
  padding: 8px 12px;
  border-radius: 4px;
  margin: 10px 0;
  font-size: 0.88rem;
}
</style>
</head>
<body data-theme="light">

<!-- Header -->
<header>
  <div class="header-title">
    <span class="exam-badge">KPSC KAS CBT</span>
    <span class="exam-name" id="exam-title-text">__EXAM_TITLE__</span>
  </div>
  <div class="header-controls">
    <div class="candidate-badge">
      <div class="candidate-avatar">C</div>
      <span>Candidate ID: KAS-2026-ONLINE</span>
    </div>
    <div class="timer-container">
      <span class="timer-label">Time Left:</span>
      <span class="timer-clock" id="timer-display">120:00</span>
    </div>
    <button class="theme-toggle-btn" id="btn-theme-toggle" title="Toggle Dark/Light Mode">🌓 Theme</button>
  </div>
</header>

<!-- Exam Screen -->
<div class="cbt-container" id="screen-exam">
  <!-- Left: Question Panel -->
  <div class="question-pane">
    <div class="section-tabs-bar" id="section-tabs">
      <!-- Section tabs injected via JS -->
    </div>
    <div class="question-meta-bar">
      <span class="q-number-title" id="q-title">Question No. 1</span>
      <span class="q-marks-badge">Marks: <span id="q-marks">+2.0 / -0.5</span></span>
    </div>
    <div class="question-scroll-content">
      <div class="question-text" id="q-text">Loading question text...</div>
      <div class="options-list" id="q-options">
        <!-- Options injected via JS -->
      </div>
    </div>
    <div class="question-footer">
      <div class="footer-left">
        <button class="btn btn-purple" id="btn-save-mark">Save & Mark for Review</button>
        <button class="btn btn-warning" id="btn-mark-next">Mark for Review & Next</button>
        <button class="btn btn-secondary" id="btn-clear">Clear Response</button>
      </div>
      <div class="footer-right">
        <button class="btn btn-secondary" id="btn-prev">Previous</button>
        <button class="btn btn-primary" id="btn-save-next">Save & Next</button>
      </div>
    </div>
  </div>

  <!-- Right: Palette Panel -->
  <div class="palette-pane">
    <div class="palette-header">Question Palette</div>
    <div class="palette-legend">
      <div class="legend-item"><div class="legend-badge badge-answered" id="count-answered">0</div><span>Answered</span></div>
      <div class="legend-item"><div class="legend-badge badge-not-answered" id="count-not-answered">0</div><span>Not Answered</span></div>
      <div class="legend-item"><div class="legend-badge badge-not-visited" id="count-not-visited">0</div><span>Not Visited</span></div>
      <div class="legend-item"><div class="legend-badge badge-marked" id="count-marked">0</div><span>Marked Review</span></div>
      <div class="legend-item" style="grid-column: span 2;"><div class="legend-badge badge-marked-answered" id="count-marked-answered">0</div><span>Ans & Marked (Evaluated)</span></div>
    </div>
    <div class="palette-grid-container">
      <div class="palette-grid" id="palette-grid">
        <!-- Palette buttons injected via JS -->
      </div>
    </div>
    <div class="palette-footer">
      <button class="btn btn-danger btn-submit-exam" id="btn-trigger-submit">Submit Exam</button>
    </div>
  </div>
</div>

<!-- Submit Confirmation Modal -->
<div class="modal-overlay" id="modal-submit">
  <div class="modal-dialog">
    <div class="modal-title">Exam Submission Confirmation</div>
    <p style="font-size: 0.9rem; color: var(--text-secondary);">Are you sure you want to finish the exam? Review your status below:</p>
    <table class="summary-table">
      <tr><th>Total Questions</th><td id="modal-total">0</td></tr>
      <tr><th>Answered</th><td id="modal-answered" style="color: #16a34a; font-weight: 700;">0</td></tr>
      <tr><th>Not Answered</th><td id="modal-not-answered" style="color: #dc2626; font-weight: 700;">0</td></tr>
      <tr><th>Marked for Review</th><td id="modal-marked" style="color: #9333ea; font-weight: 700;">0</td></tr>
      <tr><th>Not Visited</th><td id="modal-not-visited">0</td></tr>
    </table>
    <div class="modal-actions">
      <button class="btn btn-secondary" id="btn-modal-cancel">Return to Exam</button>
      <button class="btn btn-primary" id="btn-modal-confirm">Confirm & Submit</button>
    </div>
  </div>
</div>

<!-- Result & Review Screen -->
<div id="screen-result">
  <div class="result-card">
    <h2 style="font-size: 1.6rem; color: var(--primary-color);">Examination Performance & Diagnostic Scorecard</h2>
    <p style="color: var(--text-secondary); margin-top: 4px;">KPSC Gazetted Probationers (KAS) Preliminary Simulator</p>
    
    <div class="score-hero">
      <div>
        <div class="hero-stat-value" id="res-score">0.0</div>
        <div class="hero-stat-label">Net Marks (Max: __MAX_MARKS__)</div>
      </div>
      <div>
        <div class="hero-stat-value" id="res-accuracy">0%</div>
        <div class="hero-stat-label">Accuracy Rate</div>
      </div>
      <div>
        <div class="hero-stat-value" id="res-attempted">0/0</div>
        <div class="hero-stat-label">Attempted / Total</div>
      </div>
    </div>

    <div style="display: flex; gap: 12px; margin-bottom: 24px;">
      <button class="btn btn-primary" id="btn-view-all">Full Answer Review</button>
      <button class="btn btn-warning" id="btn-retry-flawed">Retry Incorrect & Marked</button>
    </div>

    <h3 style="margin-bottom: 16px; border-bottom: 2px solid var(--border-color); padding-bottom: 8px;">Detailed Question Analysis</h3>
    <div id="review-list">
      <!-- Detailed review items injected via JS -->
    </div>
  </div>
</div>

<script>
// QUESTION DATA PAYLOAD
const EXAM_DATA = __EXAM_JSON__;

// STATE MANAGEMENT
let currentQuestionIndex = 0;
let userAnswers = {}; // { qIndex: { selectedOption: 'A', status: 'answered'|'marked'|'marked-answered'|'not-answered' } }
let questionStatuses = []; // Array of statuses for 0..N-1
let visitedQuestions = new Set([0]);
let timeRemaining = EXAM_DATA.duration_minutes * 60;
let timerInterval = null;
let STORAGE_KEY = 'KAS_CBT_' + EXAM_DATA.test_id;

// DOM Elements
const qTitleEl = document.getElementById('q-title');
const qTextEl = document.getElementById('q-text');
const qOptionsEl = document.getElementById('q-options');
const paletteGridEl = document.getElementById('palette-grid');
const timerDisplayEl = document.getElementById('timer-display');
const sectionTabsEl = document.getElementById('section-tabs');

// Initialise Theme
function initTheme() {
  const savedTheme = localStorage.getItem('cbt_theme');
  if (savedTheme) {
    document.body.setAttribute('data-theme', savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.body.setAttribute('data-theme', 'dark');
  }
}
document.getElementById('btn-theme-toggle').addEventListener('click', () => {
  const current = document.body.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.body.setAttribute('data-theme', next);
  try { localStorage.setItem('cbt_theme', next); } catch(e){}
});

// Initialise Statuses
function initExam() {
  initTheme();
  const total = EXAM_DATA.questions.length;
  questionStatuses = new Array(total).fill('not-visited');
  questionStatuses[0] = 'not-answered';

  // Load cached progress if available
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      const parsed = JSON.parse(saved);
      userAnswers = parsed.userAnswers || {};
      questionStatuses = parsed.questionStatuses || questionStatuses;
      timeRemaining = parsed.timeRemaining || timeRemaining;
    }
  } catch(e) {}

  renderSectionTabs();
  renderPalette();
  loadQuestion(0);
  startTimer();
}

function renderSectionTabs() {
  sectionTabsEl.innerHTML = '';
  const sections = EXAM_DATA.sections || [{ name: 'General Studies', start: 0, end: EXAM_DATA.questions.length - 1 }];
  sections.forEach((sec, idx) => {
    const tab = document.createElement('div');
    tab.className = 'section-tab ' + (idx === 0 ? 'active' : '');
    tab.textContent = sec.name;
    tab.addEventListener('click', () => {
      document.querySelectorAll('.section-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      jumpToQuestion(sec.start);
    });
    sectionTabsEl.appendChild(tab);
  });
}

function renderPalette() {
  paletteGridEl.innerHTML = '';
  let counts = { answered: 0, 'not-answered': 0, 'not-visited': 0, marked: 0, 'marked-answered': 0 };

  EXAM_DATA.questions.forEach((q, idx) => {
    const status = questionStatuses[idx] || 'not-visited';
    counts[status]++;

    const btn = document.createElement('button');
    btn.className = `palette-btn badge-${status} ${idx === currentQuestionIndex ? 'active-q' : ''}`;
    btn.textContent = idx + 1;
    btn.addEventListener('click', () => jumpToQuestion(idx));
    paletteGridEl.appendChild(btn);
  });

  document.getElementById('count-answered').textContent = counts.answered;
  document.getElementById('count-not-answered').textContent = counts['not-answered'];
  document.getElementById('count-not-visited').textContent = counts['not-visited'];
  document.getElementById('count-marked').textContent = counts.marked;
  document.getElementById('count-marked-answered').textContent = counts['marked-answered'];
}

function loadQuestion(idx) {
  currentQuestionIndex = idx;
  visitedQuestions.add(idx);
  const q = EXAM_DATA.questions[idx];

  qTitleEl.textContent = `Question No. ${idx + 1} (${q.subject || 'General Studies'})`;
  qTextEl.innerHTML = formatQuestionText(q.text);
  qOptionsEl.innerHTML = '';

  const currentSelection = userAnswers[idx]?.selectedOption || null;

  q.options.forEach(opt => {
    const item = document.createElement('div');
    item.className = `option-item ${currentSelection === opt.label ? 'selected' : ''}`;

    const radio = document.createElement('input');
    radio.type = 'radio';
    radio.name = 'opt-choice';
    radio.className = 'option-radio';
    radio.value = opt.label;
    radio.checked = (currentSelection === opt.label);

    const labelPill = document.createElement('div');
    labelPill.className = 'option-label-pill';
    labelPill.textContent = opt.label;

    const optText = document.createElement('div');
    optText.className = 'option-text';
    optText.textContent = opt.text;

    item.appendChild(radio);
    item.appendChild(labelPill);
    item.appendChild(optText);

    item.addEventListener('click', () => {
      document.querySelectorAll('.option-item').forEach(i => i.classList.remove('selected'));
      item.classList.add('selected');
      radio.checked = true;
    });

    qOptionsEl.appendChild(item);
  });

  renderPalette();
  saveState();
}

function formatQuestionText(txt) {
  // Escapes and formats text cleanly
  return txt.replace(/\\n/g, '<br>');
}

function getSelectedOption() {
  const checked = document.querySelector('input[name="opt-choice"]:checked');
  return checked ? checked.value : null;
}

function jumpToQuestion(idx) {
  if (idx < 0 || idx >= EXAM_DATA.questions.length) return;
  // If moving away from current question and no answer selected yet, mark not-answered
  if (questionStatuses[currentQuestionIndex] === 'not-visited') {
    questionStatuses[currentQuestionIndex] = 'not-answered';
  }
  loadQuestion(idx);
}

// Button actions
document.getElementById('btn-save-next').addEventListener('click', () => {
  const sel = getSelectedOption();
  if (sel) {
    userAnswers[currentQuestionIndex] = { selectedOption: sel };
    questionStatuses[currentQuestionIndex] = 'answered';
  } else {
    questionStatuses[currentQuestionIndex] = 'not-answered';
  }
  if (currentQuestionIndex < EXAM_DATA.questions.length - 1) {
    jumpToQuestion(currentQuestionIndex + 1);
  } else {
    renderPalette();
  }
});

document.getElementById('btn-save-mark').addEventListener('click', () => {
  const sel = getSelectedOption();
  if (sel) {
    userAnswers[currentQuestionIndex] = { selectedOption: sel };
    questionStatuses[currentQuestionIndex] = 'marked-answered';
  } else {
    questionStatuses[currentQuestionIndex] = 'marked';
  }
  if (currentQuestionIndex < EXAM_DATA.questions.length - 1) {
    jumpToQuestion(currentQuestionIndex + 1);
  } else {
    renderPalette();
  }
});

document.getElementById('btn-mark-next').addEventListener('click', () => {
  const sel = getSelectedOption();
  if (sel) {
    userAnswers[currentQuestionIndex] = { selectedOption: sel };
    questionStatuses[currentQuestionIndex] = 'marked-answered';
  } else {
    delete userAnswers[currentQuestionIndex];
    questionStatuses[currentQuestionIndex] = 'marked';
  }
  if (currentQuestionIndex < EXAM_DATA.questions.length - 1) {
    jumpToQuestion(currentQuestionIndex + 1);
  } else {
    renderPalette();
  }
});

document.getElementById('btn-clear').addEventListener('click', () => {
  delete userAnswers[currentQuestionIndex];
  document.querySelectorAll('.option-item').forEach(i => i.classList.remove('selected'));
  document.querySelectorAll('input[name="opt-choice"]').forEach(r => r.checked = false);
  questionStatuses[currentQuestionIndex] = 'not-answered';
  renderPalette();
});

document.getElementById('btn-prev').addEventListener('click', () => {
  if (currentQuestionIndex > 0) {
    jumpToQuestion(currentQuestionIndex - 1);
  }
});

// Keyboard shortcuts (Alt+N: Next, Alt+P: Prev, Alt+C: Clear)
window.addEventListener('keydown', (e) => {
  if (e.altKey && e.key.toLowerCase() === 'n') {
    e.preventDefault();
    document.getElementById('btn-save-next').click();
  } else if (e.altKey && e.key.toLowerCase() === 'p') {
    e.preventDefault();
    document.getElementById('btn-prev').click();
  }
});

// Timer
function startTimer() {
  timerInterval = setInterval(() => {
    timeRemaining--;
    const mins = Math.floor(timeRemaining / 60);
    const secs = timeRemaining % 60;
    timerDisplayEl.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

    if (timeRemaining <= 300) {
      timerDisplayEl.style.color = '#ef4444';
    }

    if (timeRemaining <= 0) {
      clearInterval(timerInterval);
      submitExam();
    }
  }, 1000);
}

function saveState() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      userAnswers,
      questionStatuses,
      timeRemaining
    }));
  } catch(e) {}
}

// Submit Flow
const submitModal = document.getElementById('modal-submit');
document.getElementById('btn-trigger-submit').addEventListener('click', () => {
  let answered = 0, notAnswered = 0, marked = 0, notVisited = 0;
  questionStatuses.forEach(s => {
    if (s === 'answered' || s === 'marked-answered') answered++;
    else if (s === 'not-answered') notAnswered++;
    else if (s === 'marked') marked++;
    else notVisited++;
  });

  document.getElementById('modal-total').textContent = EXAM_DATA.questions.length;
  document.getElementById('modal-answered').textContent = answered;
  document.getElementById('modal-not-answered').textContent = notAnswered;
  document.getElementById('modal-marked').textContent = marked;
  document.getElementById('modal-not-visited').textContent = notVisited;

  submitModal.classList.add('active');
});

document.getElementById('btn-modal-cancel').addEventListener('click', () => {
  submitModal.classList.remove('active');
});

document.getElementById('btn-modal-confirm').addEventListener('click', () => {
  submitModal.classList.remove('active');
  submitExam();
});

function submitExam() {
  clearInterval(timerInterval);
  document.getElementById('screen-exam').style.display = 'none';
  document.getElementById('screen-result').style.display = 'block';

  // Calculate Scores
  const total = EXAM_DATA.questions.length;
  let correctCount = 0;
  let incorrectCount = 0;
  let attemptedCount = 0;

  EXAM_DATA.questions.forEach((q, idx) => {
    const userSel = userAnswers[idx]?.selectedOption;
    if (userSel) {
      attemptedCount++;
      if (userSel === q.answer) {
        correctCount++;
      } else {
        incorrectCount++;
      }
    }
  });

  // KPSC Negative Marking: -0.25 of marks (Marks = +2.0, Penalty = -0.50)
  const positiveMarks = correctCount * 2.0;
  const negativeMarks = incorrectCount * 0.50;
  const netScore = Math.max(0, positiveMarks - negativeMarks);
  const accuracy = attemptedCount > 0 ? ((correctCount / attemptedCount) * 100).toFixed(1) : 0;

  document.getElementById('res-score').textContent = netScore.toFixed(2);
  document.getElementById('res-accuracy').textContent = accuracy + '%';
  document.getElementById('res-attempted').textContent = `${attemptedCount} / ${total}`;

  renderReviewList();
}

function renderReviewList(filter = 'all') {
  const listEl = document.getElementById('review-list');
  listEl.innerHTML = '';

  EXAM_DATA.questions.forEach((q, idx) => {
    const userSel = userAnswers[idx]?.selectedOption || null;
    const isCorrect = (userSel === q.answer);
    const isAttempted = !!userSel;

    if (filter === 'flawed' && isCorrect) return;

    const item = document.createElement('div');
    item.className = 'review-item';

    let statusText = '';
    if (!isAttempted) {
      statusText = '<span class="review-status-skipped">Not Attempted (0.0 Marks)</span>';
    } else if (isCorrect) {
      statusText = '<span class="review-status-correct">Correct (+2.0 Marks)</span>';
    } else {
      statusText = '<span class="review-status-incorrect">Incorrect (-0.50 Marks)</span>';
    }

    item.innerHTML = `
      <div class="review-header">
        <span>Q${idx + 1}. [${q.subject || 'GS'}] ID: ${q.id}</span>
        ${statusText}
      </div>
      <div style="font-size: 1rem; font-weight: 500; margin-bottom: 12px;">${formatQuestionText(q.text)}</div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px; font-size: 0.9rem;">
        ${q.options.map(o => {
          let bg = 'var(--bg-surface-secondary)';
          let border = 'var(--border-color)';
          if (o.label === q.answer) {
            bg = 'rgba(22, 163, 74, 0.15)';
            border = '#16a34a';
          } else if (o.label === userSel) {
            bg = 'rgba(220, 38, 38, 0.15)';
            border = '#dc2626';
          }
          return `<div style="padding: 8px 12px; border-radius: 6px; border: 1.5px solid ${border}; background: ${bg};">
            <strong>${o.label}:</strong> ${o.text}
          </div>`;
        }).join('')}
      </div>
      <div style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 8px;">
        <strong>Your Choice:</strong> ${userSel || 'None'} | <strong>Official Key:</strong> ${q.answer}
      </div>
      ${q.statement_truths ? `<div class="truth-value-box"><strong>Per-Statement Verification:</strong><br>${q.statement_truths}</div>` : ''}
      <div class="review-explanation">
        <strong>Official Explanation & Vault Reference:</strong><br>
        ${q.explanation || 'No explanation available.'}
        ${q.vault_note ? `<br><small style="color: var(--accent-color);">Relevant Note: [[${q.vault_note}]]</small>` : ''}
      </div>
    `;

    listEl.appendChild(item);
  });
}

document.getElementById('btn-view-all').addEventListener('click', () => renderReviewList('all'));
document.getElementById('btn-retry-flawed').addEventListener('click', () => renderReviewList('flawed'));

// Start
window.addEventListener('DOMContentLoaded', initExam);
</script>
</body>
</html>
"""

def compile_cbt_test(test_dict: dict, out_html_path: str):
    """Compile test data dict into self-contained CBT HTML file."""
    title = test_dict.get("title", "KPSC KAS Online Mock Examination")
    max_marks = len(test_dict.get("questions", [])) * 2
    
    html = CBT_HTML_TEMPLATE
    html = html.replace("__EXAM_TITLE__", title)
    html = html.replace("__MAX_MARKS__", str(max_marks))
    html = html.replace("__EXAM_JSON__", json.dumps(test_dict, ensure_ascii=False))
    
    safe_write(out_html_path, html)
    print(f"CBT HTML compiled: {out_html_path} ({len(test_dict['questions'])} Qs)")

if __name__ == "__main__":
    print("CBT Compiler module ready.")
