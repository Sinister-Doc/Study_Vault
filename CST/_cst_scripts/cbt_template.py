# -*- coding: utf-8 -*-
"""
CBT (Computer-Based Test) HTML Engine Template.
Emulates authentic NTA/KEA/TCS iON CBT interfaces with:
- Live test phase: Section tabs, real-time palette, countdown timer, speed control, mark-for-review.
- Two-phase post-test analytics:
  1. Executive Scorecard Dashboard (Marks, Accuracy, Section breakdown, Filter shortcuts).
  2. Interactive CBT Review Mode (Navigable question-by-question with palette, filter by Marked for Review,
     Correct, Incorrect, Unattempted, side-by-side user response vs official key, and verified rationales).
  3. Optional Full Printable Solution List.
100% standalone, zero external CDN dependencies, fully offline.
"""

def get_cbt_html(title, paper_id, duration_minutes, sections, questions):
    """
    Generate an interactive, standalone CBT HTML simulation.
    sections: list of dicts: [{"id": "S1", "name": "General Knowledge", "count": 20}, ...]
    questions: list of question dicts
    """
    import json
    questions_json = json.dumps(questions, ensure_ascii=False)
    sections_json = json.dumps(sections, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
:root {{
  --bg-primary: #f0f2f5;
  --bg-card: #ffffff;
  --text-main: #1f2937;
  --text-muted: #6b7280;
  --primary-blue: #1e40af;
  --primary-hover: #1d4ed8;
  --cbt-header: #0f172a;
  
  /* CBT Palette Standard Colors */
  --cbt-answered: #22c55e;        /* Green */
  --cbt-not-answered: #ef4444;    /* Red */
  --cbt-not-visited: #9ca3af;     /* Gray */
  --cbt-marked: #a855f7;          /* Purple */
  --cbt-ans-marked: #7e22ce;      /* Dark Purple */
  --cbt-border: #e2e8f0;

  /* Review Specific Colors */
  --rev-correct: #16a34a;
  --rev-incorrect: #dc2626;
  --rev-unatt: #64748b;
  --rev-marked: #9333ea;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
body {{ background-color: var(--bg-primary); color: var(--text-main); height: 100vh; display: flex; flex-direction: column; overflow: hidden; }}

/* Top Header */
.cbt-header {{
  background: var(--cbt-header);
  color: white;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 3px solid #3b82f6;
  flex-shrink: 0;
}}
.exam-title-box h1 {{ font-size: 1.15rem; font-weight: 700; color: #f8fafc; letter-spacing: 0.3px; }}
.exam-title-box p {{ font-size: 0.8rem; color: #94a3b8; margin-top: 2px; }}

.timer-candidate-box {{ display: flex; align-items: center; gap: 20px; }}
.timer-container {{
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 6px;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.timer-label {{ font-size: 0.75rem; text-transform: uppercase; color: #94a3b8; font-weight: 600; }}
.timer-display {{ font-family: "Courier New", Courier, monospace; font-size: 1.3rem; font-weight: 800; color: #38bdf8; }}
.timer-display.danger {{ color: #f87171; animation: pulse 1s infinite; }}
@keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} 100% {{ opacity: 1; }} }}

.speed-toggle {{
  background: #334155;
  color: #cbd5e1;
  border: 1px solid #475569;
  border-radius: 4px;
  font-size: 0.72rem;
  padding: 4px 8px;
  cursor: pointer;
  transition: all 0.2s;
}}
.speed-toggle:hover {{ background: #475569; color: white; }}

.candidate-badge {{
  display: flex;
  align-items: center;
  gap: 10px;
  background: #1e293b;
  padding: 4px 10px;
  border-radius: 6px;
  border: 1px solid #334155;
}}
.cand-avatar {{ width: 32px; height: 32px; border-radius: 50%; background: #3b82f6; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.8rem; }}
.cand-details {{ font-size: 0.75rem; line-height: 1.2; }}
.cand-name {{ font-weight: 600; color: #f1f5f9; }}
.cand-roll {{ color: #94a3b8; font-size: 0.7rem; }}

/* Section Bar */
.section-nav-bar {{
  background: #ffffff;
  border-bottom: 1px solid var(--cbt-border);
  display: flex;
  overflow-x: auto;
  padding: 0 16px;
  flex-shrink: 0;
}}
.section-tab {{
  padding: 10px 16px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-muted);
  cursor: pointer;
  border-bottom: 3px solid transparent;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s ease-in-out;
}}
.section-tab:hover {{ color: var(--primary-blue); background: #f8fafc; }}
.section-tab.active {{ color: var(--primary-blue); border-bottom-color: var(--primary-blue); background: #eff6ff; }}
.section-count-badge {{ background: #e2e8f0; color: #475569; padding: 2px 6px; border-radius: 10px; font-size: 0.72rem; }}
.section-tab.active .section-count-badge {{ background: #dbeafe; color: var(--primary-blue); }}

/* Main Layout Split */
.cbt-body-wrapper {{
  display: flex;
  flex: 1;
  overflow: hidden;
  height: calc(100vh - 110px);
}}

/* Left Question Panel */
.question-pane {{
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border-right: 1px solid var(--cbt-border);
  overflow: hidden;
}}

.question-meta-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 24px;
  background: #f8fafc;
  border-bottom: 1px solid var(--cbt-border);
  flex-shrink: 0;
}}
.q-number-box {{ font-size: 1rem; font-weight: 700; color: var(--text-main); display: flex; align-items: center; gap: 8px; }}
.q-meta-tags {{ display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }}
.badge {{ padding: 3px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 600; text-transform: uppercase; }}
.badge-marks {{ background: #e0e7ff; color: #3730a3; }}
.badge-origin {{ background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }}
.badge-diff-easy {{ background: #dcfce7; color: #166534; }}
.badge-diff-med {{ background: #fef9c3; color: #854d0e; }}
.badge-diff-hard {{ background: #fee2e2; color: #991b1b; }}
.badge-reviewed {{ background: #f3e8ff; color: #6b21a8; border: 1px solid #d8b4fe; font-weight: 700; }}

.question-content-scroll {{
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}}

.q-text-en {{ font-size: 1.05rem; line-height: 1.55; font-weight: 500; color: #0f172a; margin-bottom: 14px; }}
.q-text-alt {{ font-size: 0.98rem; line-height: 1.5; color: #334155; background: #f1f5f9; padding: 10px 14px; border-radius: 6px; border-left: 4px solid #3b82f6; margin-bottom: 20px; font-family: "Nirmala UI", "Tunga", sans-serif; }}

.options-container {{ display: flex; flex-direction: column; gap: 10px; margin-top: 10px; }}
.option-label-card {{
  display: flex;
  align-items: center;
  padding: 12px 16px;
  border: 1.5px solid #e2e8f0;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.15s ease-in-out;
  background: #ffffff;
}}
.option-label-card:hover {{ border-color: #93c5fd; background: #f8fafc; }}
.option-label-card.selected {{ border-color: var(--primary-blue); background: #eff6ff; box-shadow: 0 0 0 1px var(--primary-blue); }}
.option-radio {{ margin-right: 14px; width: 18px; height: 18px; accent-color: var(--primary-blue); }}
.option-label-letter {{ font-weight: 700; width: 24px; color: #475569; }}
.option-text {{ font-size: 0.95rem; line-height: 1.4; color: #1e293b; }}

/* Bottom Controls */
.question-footer-controls {{
  padding: 12px 24px;
  background: #f8fafc;
  border-top: 1px solid var(--cbt-border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
}}
.btn {{
  padding: 8px 18px;
  font-size: 0.85rem;
  font-weight: 600;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  transition: all 0.15s;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.btn-secondary {{ background: #e2e8f0; color: #334155; }}
.btn-secondary:hover {{ background: #cbd5e1; }}
.btn-warning {{ background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }}
.btn-warning:hover {{ background: #fde68a; }}
.btn-review {{ background: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff; }}
.btn-review:hover {{ background: #e9d5ff; }}
.btn-primary {{ background: var(--primary-blue); color: #ffffff; }}
.btn-primary:hover {{ background: var(--primary-hover); }}
.btn-success {{ background: #16a34a; color: white; }}
.btn-success:hover {{ background: #15803d; }}
.btn-purple {{ background: #9333ea; color: white; }}
.btn-purple:hover {{ background: #7e22ce; }}

/* Right Sidebar: Palette */
.palette-pane {{
  width: 340px;
  background: #ffffff;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  overflow: hidden;
}}

.palette-status-summary {{
  padding: 12px 14px;
  background: #f8fafc;
  border-bottom: 1px solid var(--cbt-border);
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  font-size: 0.72rem;
  flex-shrink: 0;
}}
.legend-item {{ display: flex; align-items: center; gap: 6px; }}
.legend-badge {{
  width: 20px;
  height: 20px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 0.68rem;
}}
.bg-ans {{ background: var(--cbt-answered); }}
.bg-not-ans {{ background: var(--cbt-not-answered); }}
.bg-not-vis {{ background: var(--cbt-not-visited); }}
.bg-marked {{ background: var(--cbt-marked); }}
.bg-ans-marked {{ background: var(--cbt-ans-marked); position: relative; }}
.bg-ans-marked::after {{ content: ''; position: absolute; bottom: 2px; right: 2px; width: 5px; height: 5px; background: #22c55e; border-radius: 50%; }}

.palette-grid-scroll {{
  flex: 1;
  padding: 14px;
  overflow-y: auto;
}}
.palette-grid-title {{ font-size: 0.8rem; font-weight: 700; color: #64748b; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.5px; }}

.palette-grid {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
}}
.pal-btn {{
  aspect-ratio: 1;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  background: #f1f5f9;
  color: #334155;
  font-weight: 700;
  font-size: 0.82rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.1s;
  position: relative;
}}
.pal-btn:hover {{ border-color: var(--primary-blue); transform: scale(1.04); }}
.pal-btn.current {{ box-shadow: 0 0 0 2.5px #2563eb !important; border-color: transparent !important; }}

/* Palette Status Applied */
.pal-btn.not-visited {{ background: #f1f5f9; color: #64748b; }}
.pal-btn.not-answered {{ background: var(--cbt-not-answered); color: white; border-color: transparent; }}
.pal-btn.answered {{ background: var(--cbt-answered); color: white; border-color: transparent; }}
.pal-btn.marked {{ background: var(--cbt-marked); color: white; border-color: transparent; }}
.pal-btn.ans-marked {{ background: var(--cbt-ans-marked); color: white; border-color: transparent; }}
.pal-btn.ans-marked::after {{ content: ''; position: absolute; bottom: 3px; right: 3px; width: 6px; height: 6px; background: #22c55e; border-radius: 50%; }}

.palette-submit-bar {{
  padding: 14px;
  background: #f8fafc;
  border-top: 1px solid var(--cbt-border);
  flex-shrink: 0;
}}
.btn-submit-exam {{
  width: 100%;
  padding: 10px;
  background: #2563eb;
  color: white;
  font-weight: 700;
  font-size: 0.95rem;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  transition: all 0.15s;
}}
.btn-submit-exam:hover {{ background: #1d4ed8; }}

/* Submit Modal */
.modal-overlay {{
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.65);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(3px);
}}
.modal-card {{
  background: white;
  width: 480px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}}
.modal-header {{ background: #0f172a; color: white; padding: 16px 20px; font-size: 1rem; font-weight: 700; }}
.modal-body {{ padding: 20px; }}
.summary-table {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.85rem; }}
.summary-table th, .summary-table td {{ border: 1px solid #e2e8f0; padding: 8px 12px; }}
.summary-table th {{ background: #f8fafc; text-align: left; }}
.modal-actions {{ padding: 14px 20px; background: #f8fafc; display: flex; justify-content: flex-end; gap: 10px; border-top: 1px solid var(--cbt-border); }}

/* =====================================================================
   RESULTS PHASE 1: Executive Scorecard Dashboard
===================================================================== */
.results-dashboard {{
  position: fixed;
  inset: 0;
  background: #f8fafc;
  display: none;
  flex-direction: column;
  z-index: 2000;
  overflow-y: auto;
}}
.dash-header {{
  background: #0f172a;
  color: white;
  padding: 16px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 3px solid #3b82f6;
}}
.dash-content {{ max-width: 1120px; margin: 26px auto; padding: 0 20px; width: 100%; }}
.scorecard-banner {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
  margin-bottom: 22px;
}}
.score-box {{
  background: white;
  padding: 18px 14px;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}}
.score-box-title {{ font-size: 0.75rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; }}
.score-box-val {{ font-size: 1.8rem; font-weight: 800; color: #0f172a; margin-top: 4px; }}
.score-box-val.score-green {{ color: #16a34a; }}
.score-box-val.score-blue {{ color: #2563eb; }}
.score-box-val.score-purple {{ color: #9333ea; }}

/* Action Hub on Results Dashboard */
.action-hub-card {{
  background: white;
  border: 1px solid #cbd5e1;
  border-radius: 10px;
  padding: 18px 24px;
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}}
.action-hub-text h3 {{ font-size: 1.15rem; font-weight: 800; color: #0f172a; }}
.action-hub-text p {{ font-size: 0.85rem; color: #475569; margin-top: 3px; }}
.action-hub-buttons {{ display: flex; gap: 10px; flex-wrap: wrap; }}

.sec-breakdown-table {{
  width: 100%;
  border-collapse: collapse;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #e2e8f0;
  margin-bottom: 26px;
}}
.sec-breakdown-table th, .sec-breakdown-table td {{ padding: 10px 14px; font-size: 0.85rem; border-bottom: 1px solid #f1f5f9; }}
.sec-breakdown-table th {{ background: #f8fafc; text-align: left; font-weight: 700; color: #475569; }}

/* =====================================================================
   RESULTS PHASE 2: Interactive Question-by-Question CBT Review Mode
===================================================================== */
.review-mode-overlay {{
  position: fixed;
  inset: 0;
  background: var(--bg-primary);
  display: none;
  flex-direction: column;
  z-index: 3000;
  overflow: hidden;
}}

.rev-header {{
  background: #0f172a;
  color: white;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 3px solid #10b981;
  flex-shrink: 0;
}}
.rev-header-left h2 {{ font-size: 1.1rem; font-weight: 800; color: #f8fafc; }}
.rev-header-left p {{ font-size: 0.78rem; color: #94a3b8; }}

.rev-filter-bar {{
  background: #ffffff;
  border-bottom: 1px solid var(--cbt-border);
  padding: 8px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-shrink: 0;
}}
.rev-filters-group {{ display: flex; gap: 8px; align-items: center; overflow-x: auto; }}
.rev-filter-pill {{
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.78rem;
  font-weight: 700;
  border: 1px solid #cbd5e1;
  background: white;
  color: #334155;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s;
}}
.rev-filter-pill:hover {{ background: #f8fafc; border-color: #94a3b8; }}
.rev-filter-pill.active {{ background: #0f172a; color: white; border-color: #0f172a; }}
.rev-filter-pill.pill-marked.active {{ background: #7e22ce; color: white; border-color: #7e22ce; }}
.rev-filter-pill.pill-correct.active {{ background: #16a34a; color: white; border-color: #16a34a; }}
.rev-filter-pill.pill-incorrect.active {{ background: #dc2626; color: white; border-color: #dc2626; }}
.pill-count {{
  background: rgba(0,0,0,0.1);
  padding: 1px 6px;
  border-radius: 10px;
  font-size: 0.7rem;
}}
.rev-filter-pill.active .pill-count {{ background: rgba(255,255,255,0.25); color: white; }}

/* Review Workspace Split (Identical to Test Phase) */
.rev-body-wrapper {{
  display: flex;
  flex: 1;
  overflow: hidden;
  height: calc(100vh - 105px);
}}

.rev-question-pane {{
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border-right: 1px solid var(--cbt-border);
  overflow: hidden;
}}

.rev-question-content {{
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}}

/* Outcome Status Banner */
.rev-status-banner {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 16px;
  border-radius: 8px;
  margin-bottom: 16px;
  font-size: 0.88rem;
  font-weight: 700;
}}
.rev-status-banner.status-correct {{ background: #dcfce7; color: #166534; border: 1px solid #86efac; }}
.rev-status-banner.status-incorrect {{ background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }}
.rev-status-banner.status-unattempted {{ background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }}

/* Option Cards in Review Mode */
.rev-option-card {{
  display: flex;
  align-items: flex-start;
  padding: 12px 16px;
  border-radius: 8px;
  border: 1.5px solid #e2e8f0;
  margin-bottom: 10px;
  font-size: 0.95rem;
  line-height: 1.45;
  background: #ffffff;
}}
.rev-option-card.is-official-correct {{
  background: #f0fdf4;
  border-color: #22c55e;
  box-shadow: 0 0 0 1px #22c55e;
}}
.rev-option-card.is-user-incorrect {{
  background: #fef2f2;
  border-color: #ef4444;
  box-shadow: 0 0 0 1px #ef4444;
}}
.rev-option-badge {{
  margin-left: auto;
  font-size: 0.72rem;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 4px;
  text-transform: uppercase;
  flex-shrink: 0;
}}
.badge-rev-correct {{ background: #22c55e; color: white; }}
.badge-rev-wrong {{ background: #ef4444; color: white; }}
.badge-rev-user {{ background: #3b82f6; color: white; }}

/* Explanation / Rationale Card */
.rev-rationale-box {{
  margin-top: 20px;
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-left: 5px solid #2563eb;
  border-radius: 8px;
  padding: 16px 20px;
}}
.rev-rationale-title {{
  font-size: 0.85rem;
  font-weight: 800;
  color: #1e3a8a;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.rev-rationale-text {{
  font-size: 0.92rem;
  line-height: 1.6;
  color: #334155;
}}

/* Review Palette Sidebar */
.rev-palette-pane {{
  width: 340px;
  background: #ffffff;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  overflow: hidden;
}}
.rev-pal-legend {{
  padding: 12px 14px;
  background: #f8fafc;
  border-bottom: 1px solid var(--cbt-border);
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  font-size: 0.72rem;
  flex-shrink: 0;
}}
.rev-pal-btn {{
  aspect-ratio: 1;
  border: 1.5px solid #cbd5e1;
  border-radius: 6px;
  font-weight: 700;
  font-size: 0.82rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.1s;
  position: relative;
}}
.rev-pal-btn:hover {{ transform: scale(1.04); }}
.rev-pal-btn.current {{ box-shadow: 0 0 0 3px #0284c7 !important; }}
.rev-pal-btn.btn-rev-correct {{ background: var(--rev-correct); color: white; border-color: transparent; }}
.rev-pal-btn.btn-rev-incorrect {{ background: var(--rev-incorrect); color: white; border-color: transparent; }}
.rev-pal-btn.btn-rev-unatt {{ background: #e2e8f0; color: #475569; border-color: #cbd5e1; }}
.rev-pal-btn.was-marked::after {{
  content: '★';
  position: absolute;
  top: 1px;
  right: 2px;
  font-size: 0.65rem;
  color: #fef08a;
}}
.rev-pal-btn.is-dimmed {{ opacity: 0.25; filter: grayscale(50%); }}

/* Full List Review (Alternative Scrollable View) */
.full-list-container {{ display: none; margin-top: 20px; }}
.list-q-card {{
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 16px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04);
}}
.list-q-card.correct {{ border-left: 5px solid #22c55e; }}
.list-q-card.incorrect {{ border-left: 5px solid #ef4444; }}
.list-q-card.unattempted {{ border-left: 5px solid #9ca3af; }}
</style>
</head>
<body>

<!-- ===================================================================
     PHASE 1: LIVE TEST TAKING INTERFACE
=================================================================== -->
<header class="cbt-header">
  <div class="exam-title-box">
    <h1>{title}</h1>
    <p>Department of School Education Karnataka • GPT CST Recruitment Examination</p>
  </div>
  <div class="timer-candidate-box">
    <div class="timer-container">
      <span class="timer-label">Time Left</span>
      <span class="timer-display" id="timeDisplay">{duration_minutes:02d}:00</span>
      <button class="speed-toggle" id="btnSpeedToggle" title="Toggle 10x Speed for quick practice">1x Speed</button>
    </div>
    <div class="candidate-badge">
      <div class="cand-avatar">ST</div>
      <div class="cand-details">
        <div class="cand-name">Candidate 2026</div>
        <div class="cand-roll">Roll: CST-{paper_id}-8812</div>
      </div>
    </div>
  </div>
</header>

<!-- Section Navigation Tabs -->
<nav class="section-nav-bar" id="sectionTabsContainer"></nav>

<!-- Main Test Body Wrapper -->
<div class="cbt-body-wrapper" id="testTakingWorkspace">
  <!-- Left: Question Workspace -->
  <main class="question-pane">
    <div class="question-meta-bar">
      <div class="q-number-box">
        <span id="qDisplayNum">Question No. 1</span>
        <span class="badge badge-marks">+1.00 / -0.25</span>
      </div>
      <div class="q-meta-tags">
        <span class="badge badge-origin" id="qOriginTag">Mock</span>
        <span class="badge" id="qDiffTag">Medium</span>
        <span class="badge" style="background:#f1f5f9; color:#475569;" id="qSyllabusTag">Ref</span>
      </div>
    </div>
    <div class="question-content-scroll">
      <div class="q-text-en" id="qTextEn">Loading Question...</div>
      <div class="q-text-alt" id="qTextAlt" style="display:none;"></div>
      <div class="options-container" id="optionsContainer"></div>
    </div>
    <footer class="question-footer-controls">
      <div style="display:flex; gap:10px;">
        <button class="btn btn-review" id="btnMarkReview">Mark for Review & Next</button>
        <button class="btn btn-warning" id="btnClearResponse">Clear Response</button>
      </div>
      <div style="display:flex; gap:10px;">
        <button class="btn btn-secondary" id="btnPrev">Previous</button>
        <button class="btn btn-primary" id="btnSaveNext">Save & Next</button>
      </div>
    </footer>
  </main>

  <!-- Right: Palette Sidebar -->
  <aside class="palette-pane">
    <div class="palette-status-summary">
      <div class="legend-item"><div class="legend-badge bg-ans" id="badgeCountAns">0</div> Answered</div>
      <div class="legend-item"><div class="legend-badge bg-not-ans" id="badgeCountNotAns">0</div> Not Answered</div>
      <div class="legend-item"><div class="legend-badge bg-not-vis" id="badgeCountNotVis">0</div> Not Visited</div>
      <div class="legend-item"><div class="legend-badge bg-marked" id="badgeCountMarked">0</div> Marked Review</div>
      <div class="legend-item" style="grid-column: span 2;"><div class="legend-badge bg-ans-marked" id="badgeCountAnsMarked">0</div> Ans & Marked for Review</div>
    </div>
    <div class="palette-grid-scroll">
      <div class="palette-grid-title" id="currentSectionTitle">SECTION: ALL</div>
      <div class="palette-grid" id="paletteGrid"></div>
    </div>
    <div class="palette-submit-bar">
      <button class="btn-submit-exam" id="btnOpenSubmitModal">Submit Test</button>
    </div>
  </aside>
</div>

<!-- Submit Confirmation Modal -->
<div class="modal-overlay" id="submitModal">
  <div class="modal-card">
    <div class="modal-header">Confirm Exam Submission</div>
    <div class="modal-body">
      <p style="font-size:0.9rem; color:#475569; margin-bottom:12px;">Are you sure you want to end the test? Here is the summary of your session:</p>
      <table class="summary-table">
        <tr><th>Total Questions</th><td id="mTotalQs">150</td></tr>
        <tr><th style="color:#16a34a;">Answered</th><td id="mAnsQs">0</td></tr>
        <tr><th style="color:#dc2626;">Not Answered</th><td id="mNotAnsQs">0</td></tr>
        <tr><th style="color:#7c3aed;">Marked for Review</th><td id="mMarkedQs">0</td></tr>
        <tr><th style="color:#64748b;">Not Visited</th><td id="mNotVisQs">0</td></tr>
      </table>
      <p style="font-size:0.8rem; color:#94a3b8; margin-top:12px;">No further changes can be made after submitting.</p>
    </div>
    <div class="modal-actions">
      <button class="btn btn-secondary" id="btnCancelModal">Resume Test</button>
      <button class="btn btn-success" id="btnConfirmSubmit">Confirm & Submit</button>
    </div>
  </div>
</div>

<!-- ===================================================================
     POST-TEST PHASE 1: Executive Scorecard Dashboard
=================================================================== -->
<div class="results-dashboard" id="resultsDashboard">
  <header class="dash-header">
    <div>
      <h2 style="font-size:1.3rem; font-weight:800;">Exam Performance & Solution Analytics</h2>
      <p style="font-size:0.82rem; color:#94a3b8;">{title}</p>
    </div>
    <div style="display:flex; gap:10px;">
      <button class="btn btn-primary" id="btnStartInteractiveReviewTop">Start Interactive CBT Review</button>
      <button class="btn btn-secondary" onclick="window.print()">Print / Save PDF</button>
    </div>
  </header>
  <div class="dash-content">
    <div class="scorecard-banner">
      <div class="score-box">
        <div class="score-box-title">Total Marks</div>
        <div class="score-box-val score-green" id="dashTotalScore">0.00 / 150</div>
      </div>
      <div class="score-box">
        <div class="score-box-title">Accuracy</div>
        <div class="score-box-val score-blue" id="dashAccuracy">0%</div>
      </div>
      <div class="score-box">
        <div class="score-box-title">Attempted</div>
        <div class="score-box-val" id="dashAttempted">0 / 150</div>
      </div>
      <div class="score-box">
        <div class="score-box-title">Marked for Review</div>
        <div class="score-box-val score-purple" id="dashMarkedReview">0</div>
      </div>
      <div class="score-box">
        <div class="score-box-title">Qualifying Status</div>
        <div class="score-box-val" id="dashStatus" style="font-size:1.25rem; line-height:2.2;">QUALIFIED</div>
      </div>
    </div>

    <!-- Action Hub Card: Launches interactive review by filter -->
    <div class="action-hub-card">
      <div class="action-hub-text">
        <h3>Question-by-Question CBT Review Mode</h3>
        <p>Review solutions in the authentic CBT interface with verified rationales, candidate response comparison, and instant palette jumps.</p>
      </div>
      <div class="action-hub-buttons">
        <button class="btn btn-primary" id="btnStartInteractiveReview">Review All (150)</button>
        <button class="btn btn-warning" id="btnReviewIncorrectOnly">Review Incorrect</button>
        <button class="btn btn-purple" id="btnReviewMarkedOnly">Review Marked for Review</button>
        <button class="btn btn-secondary" id="btnToggleListSolutions">Expand Full List</button>
      </div>
    </div>

    <h3 style="font-size:1.05rem; font-weight:700; color:#1e293b; margin-bottom:12px;">Section-wise Performance Breakdown</h3>
    <table class="sec-breakdown-table" id="dashSectionTable">
      <thead>
        <tr>
          <th>Section</th>
          <th>Total Qs</th>
          <th>Attempted</th>
          <th>Correct</th>
          <th>Incorrect</th>
          <th>Score</th>
          <th>Accuracy</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>

    <!-- Full scrollable solution list container (collapsible) -->
    <div class="full-list-container" id="fullListSolutionsContainer">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <h3 style="font-size:1.05rem; font-weight:700; color:#1e293b;">Complete Solutions & Rationales List</h3>
        <button class="btn btn-secondary" id="btnCloseListSolutions">Collapse List</button>
      </div>
      <div id="solutionReviewContainer"></div>
    </div>
  </div>
</div>

<!-- ===================================================================
     POST-TEST PHASE 2: Interactive Question-by-Question CBT Review
=================================================================== -->
<div class="review-mode-overlay" id="interactiveReviewMode">
  <header class="rev-header">
    <div class="rev-header-left">
      <h2>CBT Solution Review • {title}</h2>
      <p id="revScoreSubtitle">Score: 0 / 150 | Accuracy: 0%</p>
    </div>
    <div style="display:flex; gap:10px;">
      <button class="btn btn-secondary" id="btnBackToDashboard">Back to Score Summary</button>
    </div>
  </header>

  <!-- Review Filter Bar -->
  <nav class="rev-filter-bar">
    <div class="rev-filters-group">
      <span style="font-size:0.75rem; font-weight:700; color:#64748b; text-transform:uppercase;">Filter:</span>
      <button class="rev-filter-pill active" data-rev-filter="all">All <span class="pill-count" id="revPillAll">150</span></button>
      <button class="rev-filter-pill pill-correct" data-rev-filter="correct">Correct <span class="pill-count" id="revPillCorrect">0</span></button>
      <button class="rev-filter-pill pill-incorrect" data-rev-filter="incorrect">Incorrect <span class="pill-count" id="revPillIncorrect">0</span></button>
      <button class="rev-filter-pill" data-rev-filter="unattempted">Unattempted <span class="pill-count" id="revPillUnatt">0</span></button>
      <button class="rev-filter-pill pill-marked" data-rev-filter="marked">Marked for Review <span class="pill-count" id="revPillMarked">0</span></button>
    </div>
    <div style="font-size:0.8rem; font-weight:600; color:#475569;" id="revFilterStatusInfo">Showing All 150 Questions</div>
  </nav>

  <!-- Review Body Split (Same CBT Layout) -->
  <div class="rev-body-wrapper">
    <!-- Left Review Pane -->
    <main class="rev-question-pane">
      <div class="question-meta-bar">
        <div class="q-number-box">
          <span id="revDisplayNum">Question No. 1</span>
          <span id="revMarksBadge" class="badge badge-marks">+1.00 Marks</span>
        </div>
        <div class="q-meta-tags">
          <span class="badge badge-origin" id="revOriginTag">PYQ</span>
          <span class="badge" id="revDiffTag">Medium</span>
          <span class="badge" style="background:#f1f5f9; color:#475569;" id="revSyllabusTag">Ref</span>
          <span class="badge badge-reviewed" id="revMarkedBadge" style="display:none;">★ Marked for Review</span>
        </div>
      </div>

      <div class="rev-question-content">
        <!-- Result status banner (Correct / Incorrect / Unattempted) -->
        <div class="rev-status-banner" id="revStatusBanner">
          <span id="revStatusBannerText">Outcome</span>
          <span id="revCandidateChoiceText">Your Choice: A | Key: A</span>
        </div>

        <div class="q-text-en" id="revTextEn">Loading Question...</div>
        <div class="q-text-alt" id="revTextAlt" style="display:none;"></div>

        <div class="options-container" id="revOptionsContainer"></div>

        <!-- Verified Rationale Card -->
        <div class="rev-rationale-box">
          <div class="rev-rationale-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            Verified Rationale & Core Concepts
          </div>
          <div class="rev-rationale-text" id="revRationaleText">Detailed explanation...</div>
        </div>
      </div>

      <footer class="question-footer-controls">
        <div style="display:flex; gap:10px;">
          <button class="btn btn-secondary" id="btnRevPrev">Previous</button>
          <button class="btn btn-primary" id="btnRevNext">Next</button>
        </div>
        <div style="display:flex; gap:10px;">
          <button class="btn btn-secondary" id="btnRevJumpToSummary">Back to Scorecard</button>
        </div>
      </footer>
    </main>

    <!-- Right Review Palette Pane -->
    <aside class="rev-palette-pane">
      <div class="rev-pal-legend">
        <div class="legend-item"><div class="legend-badge" style="background:var(--rev-correct);">✓</div> Correct</div>
        <div class="legend-item"><div class="legend-badge" style="background:var(--rev-incorrect);">✗</div> Incorrect</div>
        <div class="legend-item"><div class="legend-badge" style="background:var(--rev-unatt);">-</div> Unattempted</div>
        <div class="legend-item"><div class="legend-badge" style="background:var(--rev-marked);">★</div> Was Marked</div>
      </div>
      <div class="palette-grid-scroll">
        <div class="palette-grid-title" id="revPaletteTitle">SOLUTION PALETTE (ALL)</div>
        <div class="palette-grid" id="revPaletteGrid"></div>
      </div>
    </aside>
  </div>
</div>

<script>
const QUESTIONS = {questions_json};
const SECTIONS = {sections_json};
const TOTAL_QS = QUESTIONS.length;
const INITIAL_DURATION_SEC = {duration_minutes} * 60;

// Test Taking State
let currentIndex = 0;
let userAnswers = new Array(TOTAL_QS).fill(null); // 'A', 'B', 'C', 'D' or null
let questionStatus = new Array(TOTAL_QS).fill('not-visited'); // 'not-visited','not-answered','answered','marked','ans-marked'
let wasEverMarked = new Array(TOTAL_QS).fill(false); // boolean tracking if marked for review at any point
let remainingSeconds = INITIAL_DURATION_SEC;
let timerSpeedMultiplier = 1;
let timerInterval = null;

// Review Mode State
let reviewCurrentIndex = 0;
let activeReviewFilter = 'all'; // 'all', 'correct', 'incorrect', 'unattempted', 'marked'
let reviewQuestionIndices = []; // indices matching current review filter

// Initialize on load
document.addEventListener("DOMContentLoaded", () => {{
  initSectionTabs();
  initPaletteGrid();
  loadQuestion(0);
  startTimer();
  setupTestEventListeners();
  updatePaletteCounts();
}});

function initSectionTabs() {{
  const container = document.getElementById("sectionTabsContainer");
  container.innerHTML = "";
  SECTIONS.forEach((sec, idx) => {{
    const tab = document.createElement("div");
    tab.className = `section-tab ${{idx === 0 ? 'active' : ''}}`;
    tab.id = `tab-${{sec.id}}`;
    tab.innerHTML = `${{sec.name}} <span class="section-count-badge">${{sec.count}}</span>`;
    tab.onclick = () => jumpToSection(sec.id);
    container.appendChild(tab);
  }});
}}

function initPaletteGrid() {{
  const grid = document.getElementById("paletteGrid");
  grid.innerHTML = "";
  for (let i = 0; i < TOTAL_QS; i++) {{
    const btn = document.createElement("button");
    btn.className = "pal-btn not-visited";
    btn.id = `pal-${{i}}`;
    btn.innerText = i + 1;
    btn.onclick = () => {{
      markCurrentStateBeforeLeave();
      loadQuestion(i);
    }};
    grid.appendChild(btn);
  }}
}}

function loadQuestion(idx) {{
  currentIndex = idx;
  const q = QUESTIONS[idx];
  
  if (questionStatus[idx] === 'not-visited') {{
    questionStatus[idx] = 'not-answered';
  }}

  document.querySelectorAll(".pal-btn").forEach(b => b.classList.remove("current"));
  const currentPal = document.getElementById(`pal-${{idx}}`);
  if (currentPal) currentPal.classList.add("current");

  document.getElementById("qDisplayNum").innerText = `Question No. ${{idx + 1}} of ${{TOTAL_QS}}`;
  document.getElementById("qOriginTag").innerText = q.origin_tag || (q.label || "Mock");
  
  const diffTag = document.getElementById("qDiffTag");
  diffTag.innerText = (q.difficulty || "medium").toUpperCase();
  diffTag.className = `badge badge-diff-${{(q.difficulty || "medium").toLowerCase().slice(0,4)}}`;

  document.getElementById("qSyllabusTag").innerText = q.syllabus_id || "";

  document.getElementById("qTextEn").innerText = q.text;
  const altBox = document.getElementById("qTextAlt");
  if (q.text_alt) {{
    altBox.innerText = q.text_alt;
    altBox.style.display = "block";
  }} else {{
    altBox.style.display = "none";
  }}

  const optContainer = document.getElementById("optionsContainer");
  optContainer.innerHTML = "";
  const selectedAns = userAnswers[idx];

  q.options.forEach(opt => {{
    const card = document.createElement("label");
    card.className = `option-label-card ${{selectedAns === opt.label ? 'selected' : ''}}`;
    card.innerHTML = `
      <input type="radio" name="opt_choice" value="${{opt.label}}" class="option-radio" ${{selectedAns === opt.label ? 'checked' : ''}}>
      <span class="option-label-letter">${{opt.label}}.</span>
      <span class="option-text">${{opt.text}}</span>
    `;
    card.onclick = () => {{
      document.querySelectorAll(".option-label-card").forEach(c => c.classList.remove("selected"));
      card.classList.add("selected");
      card.querySelector("input").checked = true;
    }};
    optContainer.appendChild(card);
  }});

  const sec = SECTIONS.find(s => s.id === q.section_id) || SECTIONS[0];
  document.querySelectorAll(".section-tab").forEach(t => t.classList.remove("active"));
  const secTab = document.getElementById(`tab-${{sec.id}}`);
  if (secTab) secTab.classList.add("active");
  document.getElementById("currentSectionTitle").innerText = `SECTION: ${{sec.name.toUpperCase()}}`;

  updatePaletteButton(idx);
  updatePaletteCounts();
}}

function markCurrentStateBeforeLeave() {{
  const selectedRadio = document.querySelector('input[name="opt_choice"]:checked');
  if (selectedRadio) {{
    userAnswers[currentIndex] = selectedRadio.value;
  }}
}}

function updatePaletteButton(idx) {{
  const btn = document.getElementById(`pal-${{idx}}`);
  if (!btn) return;
  btn.className = `pal-btn ${{questionStatus[idx]}} ${{currentIndex === idx ? 'current' : ''}}`;
}}

function updatePaletteCounts() {{
  let ans = 0, notAns = 0, notVis = 0, marked = 0, ansMarked = 0;
  for (let s of questionStatus) {{
    if (s === 'answered') ans++;
    else if (s === 'not-answered') notAns++;
    else if (s === 'not-visited') notVis++;
    else if (s === 'marked') marked++;
    else if (s === 'ans-marked') ansMarked++;
  }}
  document.getElementById("badgeCountAns").innerText = ans;
  document.getElementById("badgeCountNotAns").innerText = notAns;
  document.getElementById("badgeCountNotVis").innerText = notVis;
  document.getElementById("badgeCountMarked").innerText = marked;
  document.getElementById("badgeCountAnsMarked").innerText = ansMarked;
}}

function jumpToSection(secId) {{
  markCurrentStateBeforeLeave();
  const firstIdx = QUESTIONS.findIndex(q => q.section_id === secId);
  if (firstIdx !== -1) {{
    loadQuestion(firstIdx);
  }}
}}

function setupTestEventListeners() {{
  document.getElementById("btnSaveNext").onclick = () => {{
    const selected = document.querySelector('input[name="opt_choice"]:checked');
    if (selected) {{
      userAnswers[currentIndex] = selected.value;
      questionStatus[currentIndex] = 'answered';
    }} else {{
      userAnswers[currentIndex] = null;
      questionStatus[currentIndex] = 'not-answered';
    }}
    updatePaletteButton(currentIndex);
    if (currentIndex < TOTAL_QS - 1) {{
      loadQuestion(currentIndex + 1);
    }} else {{
      updatePaletteCounts();
    }}
  }};

  document.getElementById("btnMarkReview").onclick = () => {{
    const selected = document.querySelector('input[name="opt_choice"]:checked');
    wasEverMarked[currentIndex] = true;
    if (selected) {{
      userAnswers[currentIndex] = selected.value;
      questionStatus[currentIndex] = 'ans-marked';
    }} else {{
      userAnswers[currentIndex] = null;
      questionStatus[currentIndex] = 'marked';
    }}
    updatePaletteButton(currentIndex);
    if (currentIndex < TOTAL_QS - 1) {{
      loadQuestion(currentIndex + 1);
    }} else {{
      updatePaletteCounts();
    }}
  }};

  document.getElementById("btnClearResponse").onclick = () => {{
    userAnswers[currentIndex] = null;
    questionStatus[currentIndex] = 'not-answered';
    document.querySelectorAll(".option-label-card").forEach(c => c.classList.remove("selected"));
    const checked = document.querySelector('input[name="opt_choice"]:checked');
    if (checked) checked.checked = false;
    updatePaletteButton(currentIndex);
    updatePaletteCounts();
  }};

  document.getElementById("btnPrev").onclick = () => {{
    markCurrentStateBeforeLeave();
    if (currentIndex > 0) loadQuestion(currentIndex - 1);
  }};

  document.getElementById("btnSpeedToggle").onclick = (e) => {{
    if (timerSpeedMultiplier === 1) {{
      timerSpeedMultiplier = 10;
      e.target.innerText = "10x Fast";
      e.target.style.background = "#0284c7";
    }} else {{
      timerSpeedMultiplier = 1;
      e.target.innerText = "1x Speed";
      e.target.style.background = "#334155";
    }}
  }};

  document.getElementById("btnOpenSubmitModal").onclick = () => openSubmitModal();
  document.getElementById("btnCancelModal").onclick = () => document.getElementById("submitModal").style.display = "none";
  document.getElementById("btnConfirmSubmit").onclick = () => {{
    document.getElementById("submitModal").style.display = "none";
    finishExam();
  }};
}}

function openSubmitModal() {{
  markCurrentStateBeforeLeave();
  let ans = 0, notAns = 0, marked = 0, notVis = 0;
  for (let i = 0; i < TOTAL_QS; i++) {{
    if (userAnswers[i] !== null) ans++;
    else if (questionStatus[i] === 'not-visited') notVis++;
    else if (questionStatus[i] === 'marked') marked++;
    else notAns++;
  }}
  document.getElementById("mTotalQs").innerText = TOTAL_QS;
  document.getElementById("mAnsQs").innerText = ans;
  document.getElementById("mNotAnsQs").innerText = notAns;
  document.getElementById("mMarkedQs").innerText = marked;
  document.getElementById("mNotVisQs").innerText = notVis;
  document.getElementById("submitModal").style.display = "flex";
}}

function startTimer() {{
  const disp = document.getElementById("timeDisplay");
  timerInterval = setInterval(() => {{
    remainingSeconds -= timerSpeedMultiplier;
    if (remainingSeconds <= 0) {{
      remainingSeconds = 0;
      clearInterval(timerInterval);
      disp.innerText = "00:00";
      alert("Time is up! Submitting exam automatically.");
      finishExam();
      return;
    }}
    const m = Math.floor(remainingSeconds / 60);
    const s = remainingSeconds % 60;
    disp.innerText = `${{m < 10 ? '0' : ''}}${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
    if (remainingSeconds <= 300) disp.classList.add("danger");
  }}, 1000);
}}

/* =====================================================================
   FINISH EXAM & LAUNCH RESULTS
===================================================================== */
function finishExam() {{
  clearInterval(timerInterval);
  markCurrentStateBeforeLeave();

  let correctCount = 0;
  let incorrectCount = 0;
  let unattemptedCount = 0;
  let markedCount = 0;
  let secStats = {{}};
  SECTIONS.forEach(s => {{ secStats[s.id] = {{ name: s.name, total: 0, attempted: 0, correct: 0, incorrect: 0 }}; }});

  QUESTIONS.forEach((q, idx) => {{
    const secId = q.section_id || SECTIONS[0].id;
    if (!secStats[secId]) secStats[secId] = {{ name: secId, total: 0, attempted: 0, correct: 0, incorrect: 0 }};
    secStats[secId].total++;

    if (wasEverMarked[idx] || questionStatus[idx] === 'marked' || questionStatus[idx] === 'ans-marked') {{
      wasEverMarked[idx] = true;
      markedCount++;
    }}

    const userAns = userAnswers[idx];
    if (userAns === null) {{
      unattemptedCount++;
    }} else if (userAns === q.answer) {{
      correctCount++;
      secStats[secId].attempted++;
      secStats[secId].correct++;
    }} else {{
      incorrectCount++;
      secStats[secId].attempted++;
      secStats[secId].incorrect++;
    }}
  }});

  const totalScore = (correctCount * 1.0) - (incorrectCount * 0.25);
  const attemptedTotal = correctCount + incorrectCount;
  const accuracy = attemptedTotal > 0 ? ((correctCount / attemptedTotal) * 100).toFixed(1) : 0;
  const percentage = ((Math.max(0, totalScore) / TOTAL_QS) * 100).toFixed(1);

  // Populate Dashboard Banner
  document.getElementById("dashTotalScore").innerText = `${{totalScore.toFixed(2)}} / ${{TOTAL_QS}} (${{percentage}}%)`;
  document.getElementById("dashAccuracy").innerText = `${{accuracy}}%`;
  document.getElementById("dashAttempted").innerText = `${{attemptedTotal}} / ${{TOTAL_QS}} (${{unattemptedCount}} Unattempted)`;
  document.getElementById("dashMarkedReview").innerText = markedCount;
  
  const statusElem = document.getElementById("dashStatus");
  if (totalScore >= (TOTAL_QS * 0.50)) {{
    statusElem.innerText = "QUALIFIED (≥50%)";
    statusElem.style.color = "#16a34a";
  }} else {{
    statusElem.innerText = "NEEDS REVISION (<50%)";
    statusElem.style.color = "#dc2626";
  }}

  // Subtitle in Review Mode
  document.getElementById("revScoreSubtitle").innerText = `Score: ${{totalScore.toFixed(2)}} / ${{TOTAL_QS}} | Accuracy: ${{accuracy}}% | Attempted: ${{attemptedTotal}}/${{TOTAL_QS}}`;

  // Populate Review Filter Counts
  document.getElementById("revPillAll").innerText = TOTAL_QS;
  document.getElementById("revPillCorrect").innerText = correctCount;
  document.getElementById("revPillIncorrect").innerText = incorrectCount;
  document.getElementById("revPillUnatt").innerText = unattemptedCount;
  document.getElementById("revPillMarked").innerText = markedCount;

  // Populate Section Table
  const tbody = document.querySelector("#dashSectionTable tbody");
  tbody.innerHTML = "";
  Object.values(secStats).forEach(s => {{
    const sScore = (s.correct * 1.0) - (s.incorrect * 0.25);
    const sAcc = s.attempted > 0 ? ((s.correct / s.attempted) * 100).toFixed(1) + "%" : "0%";
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td><strong>${{s.name}}</strong></td>
      <td>${{s.total}}</td>
      <td>${{s.attempted}}</td>
      <td style="color:#16a34a; font-weight:700;">${{s.correct}}</td>
      <td style="color:#dc2626;">${{s.incorrect}}</td>
      <td><strong>${{sScore.toFixed(2)}}</strong></td>
      <td>${{sAcc}}</td>
    `;
    tbody.appendChild(tr);
  }});

  // Render Full Solution List (for optional scrollable view)
  renderFullListSolutions();

  // Setup Result Dashboard Button Actions
  document.getElementById("btnStartInteractiveReview").onclick = () => openInteractiveReview("all");
  document.getElementById("btnStartInteractiveReviewTop").onclick = () => openInteractiveReview("all");
  document.getElementById("btnReviewIncorrectOnly").onclick = () => openInteractiveReview("incorrect");
  document.getElementById("btnReviewMarkedOnly").onclick = () => openInteractiveReview("marked");

  const listContainer = document.getElementById("fullListSolutionsContainer");
  document.getElementById("btnToggleListSolutions").onclick = () => {{
    listContainer.style.display = listContainer.style.display === "block" ? "none" : "block";
  }};
  document.getElementById("btnCloseListSolutions").onclick = () => {{
    listContainer.style.display = "none";
  }};

  // Show Dashboard
  document.getElementById("resultsDashboard").style.display = "flex";
}}

/* =====================================================================
   INTERACTIVE REVIEW MODE ENGINE
===================================================================== */
function openInteractiveReview(filter = "all") {{
  document.getElementById("resultsDashboard").style.display = "none";
  document.getElementById("interactiveReviewMode").style.display = "flex";
  
  setupReviewEventListeners();
  initReviewPalette();
  setReviewFilter(filter);
}}

function setupReviewEventListeners() {{
  document.getElementById("btnBackToDashboard").onclick = () => {{
    document.getElementById("interactiveReviewMode").style.display = "none";
    document.getElementById("resultsDashboard").style.display = "flex";
  }};
  document.getElementById("btnRevJumpToSummary").onclick = () => {{
    document.getElementById("interactiveReviewMode").style.display = "none";
    document.getElementById("resultsDashboard").style.display = "flex";
  }};

  // Filter Pills click handlers
  document.querySelectorAll(".rev-filter-pill").forEach(pill => {{
    pill.onclick = () => {{
      setReviewFilter(pill.dataset.revFilter);
    }};
  }});

  // Prev / Next in Review Mode
  document.getElementById("btnRevPrev").onclick = () => {{
    const pos = reviewQuestionIndices.indexOf(reviewCurrentIndex);
    if (pos > 0) {{
      loadReviewQuestion(reviewQuestionIndices[pos - 1]);
    }}
  }};

  document.getElementById("btnRevNext").onclick = () => {{
    const pos = reviewQuestionIndices.indexOf(reviewCurrentIndex);
    if (pos !== -1 && pos < reviewQuestionIndices.length - 1) {{
      loadReviewQuestion(reviewQuestionIndices[pos + 1]);
    }}
  }};
}}

function initReviewPalette() {{
  const grid = document.getElementById("revPaletteGrid");
  grid.innerHTML = "";
  for (let i = 0; i < TOTAL_QS; i++) {{
    const q = QUESTIONS[i];
    const uAns = userAnswers[i];
    const btn = document.createElement("button");
    btn.className = "rev-pal-btn";
    btn.id = `rev-pal-${{i}}`;
    btn.innerText = i + 1;

    if (uAns === null) {{
      btn.classList.add("btn-rev-unatt");
    }} else if (uAns === q.answer) {{
      btn.classList.add("btn-rev-correct");
    }} else {{
      btn.classList.add("btn-rev-incorrect");
    }}

    if (wasEverMarked[i]) {{
      btn.classList.add("was-marked");
    }}

    btn.onclick = () => loadReviewQuestion(i);
    grid.appendChild(btn);
  }}
}}

function setReviewFilter(filter) {{
  activeReviewFilter = filter;
  
  // Highlight active pill
  document.querySelectorAll(".rev-filter-pill").forEach(pill => {{
    if (pill.dataset.revFilter === filter) {{
      pill.classList.add("active");
    }} else {{
      pill.classList.remove("active");
    }}
  }});

  // Compute matching indices
  reviewQuestionIndices = [];
  QUESTIONS.forEach((q, idx) => {{
    const uAns = userAnswers[idx];
    const isCorrect = uAns === q.answer;
    const isUnatt = uAns === null;
    const isMarked = wasEverMarked[idx];

    let match = false;
    if (filter === "all") match = true;
    else if (filter === "correct" && isCorrect) match = true;
    else if (filter === "incorrect" && (!isCorrect && !isUnatt)) match = true;
    else if (filter === "unattempted" && isUnatt) match = true;
    else if (filter === "marked" && isMarked) match = true;

    if (match) reviewQuestionIndices.push(idx);

    // Dim non-matching buttons in review palette
    const palBtn = document.getElementById(`rev-pal-${{idx}}`);
    if (palBtn) {{
      if (match) palBtn.classList.remove("is-dimmed");
      else palBtn.classList.add("is-dimmed");
    }}
  }});

  // Update Status text
  const filterNames = {{
    all: "All Questions",
    correct: "Correct Answers",
    incorrect: "Incorrect Answers",
    unattempted: "Unattempted Questions",
    marked: "Marked for Review"
  }};
  document.getElementById("revFilterStatusInfo").innerText = 
    `Filter: ${{filterNames[filter]}} (${{reviewQuestionIndices.length}} of ${{TOTAL_QS}} questions)`;
  document.getElementById("revPaletteTitle").innerText = `PALETTE: ${{filterNames[filter].toUpperCase()}}`;

  // Load first matching question
  if (reviewQuestionIndices.length > 0) {{
    const targetIdx = reviewQuestionIndices.includes(reviewCurrentIndex) ? reviewCurrentIndex : reviewQuestionIndices[0];
    loadReviewQuestion(targetIdx);
  }} else {{
    alert(`No questions found under filter: "${{filterNames[filter]}}"`);
    setReviewFilter("all");
  }}
}}

function loadReviewQuestion(idx) {{
  reviewCurrentIndex = idx;
  const q = QUESTIONS[idx];
  const uAns = userAnswers[idx];
  const isCorrect = uAns === q.answer;
  const isUnatt = uAns === null;
  const isMarked = wasEverMarked[idx];

  // Palette current highlight
  document.querySelectorAll(".rev-pal-btn").forEach(b => b.classList.remove("current"));
  const curBtn = document.getElementById(`rev-pal-${{idx}}`);
  if (curBtn) curBtn.classList.add("current");

  // Meta bar
  document.getElementById("revDisplayNum").innerText = `Question No. ${{idx + 1}} of ${{TOTAL_QS}}`;
  document.getElementById("revOriginTag").innerText = q.origin_tag || (q.label || "Mock");
  
  const diffTag = document.getElementById("revDiffTag");
  diffTag.innerText = (q.difficulty || "medium").toUpperCase();
  diffTag.className = `badge badge-diff-${{(q.difficulty || "medium").toLowerCase().slice(0,4)}}`;

  document.getElementById("revSyllabusTag").innerText = q.syllabus_id || "";

  const markedBadge = document.getElementById("revMarkedBadge");
  if (isMarked) {{
    markedBadge.style.display = "inline-block";
  }} else {{
    markedBadge.style.display = "none";
  }}

  // Status Banner
  const banner = document.getElementById("revStatusBanner");
  const bannerText = document.getElementById("revStatusBannerText");
  const choiceText = document.getElementById("revCandidateChoiceText");
  const marksBadge = document.getElementById("revMarksBadge");

  if (isCorrect) {{
    banner.className = "rev-status-banner status-correct";
    bannerText.innerHTML = "✓ Correct Answer (+1.00 Marks)";
    marksBadge.innerText = "+1.00 Marks";
    marksBadge.style.background = "#dcfce7";
    marksBadge.style.color = "#166534";
  }} else if (isUnatt) {{
    banner.className = "rev-status-banner status-unattempted";
    bannerText.innerHTML = "○ Unattempted (0.00 Marks)";
    marksBadge.innerText = "0.00 Marks";
    marksBadge.style.background = "#f1f5f9";
    marksBadge.style.color = "#475569";
  }} else {{
    banner.className = "rev-status-banner status-incorrect";
    bannerText.innerHTML = "✗ Incorrect Answer (-0.25 Negative Marking)";
    marksBadge.innerText = "-0.25 Marks";
    marksBadge.style.background = "#fee2e2";
    marksBadge.style.color = "#991b1b";
  }}

  choiceText.innerHTML = `Your Choice: <strong>${{uAns ? uAns : 'None'}}</strong> | Official Key: <strong>${{q.answer}}</strong>`;

  // Question statements
  document.getElementById("revTextEn").innerText = q.text;
  const altBox = document.getElementById("revTextAlt");
  if (q.text_alt) {{
    altBox.innerText = q.text_alt;
    altBox.style.display = "block";
  }} else {{
    altBox.style.display = "none";
  }}

  // Option Cards rendering with clear badges
  const optContainer = document.getElementById("revOptionsContainer");
  optContainer.innerHTML = "";

  q.options.forEach(opt => {{
    const isThisOfficial = opt.label === q.answer;
    const isThisUserChoice = opt.label === uAns;

    const card = document.createElement("div");
    card.className = "rev-option-card";

    let badgeHtml = "";
    if (isThisOfficial && isThisUserChoice) {{
      card.classList.add("is-official-correct");
      badgeHtml = `<span class="rev-option-badge badge-rev-correct">✓ Your Choice (Correct Key)</span>`;
    }} else if (isThisOfficial) {{
      card.classList.add("is-official-correct");
      badgeHtml = `<span class="rev-option-badge badge-rev-correct">✓ Official Key</span>`;
    }} else if (isThisUserChoice) {{
      card.classList.add("is-user-incorrect");
      badgeHtml = `<span class="rev-option-badge badge-rev-wrong">✗ Your Choice (Incorrect)</span>`;
    }}

    card.innerHTML = `
      <span class="option-label-letter" style="font-weight:700; width:28px;">${{opt.label}}.</span>
      <span class="option-text" style="flex:1;">${{opt.text}}</span>
      ${{badgeHtml}}
    `;
    optContainer.appendChild(card);
  }});

  // Rationale box
  document.getElementById("revRationaleText").innerHTML = q.explanation || "No explanation provided.";

  // Update Prev / Next button states
  const pos = reviewQuestionIndices.indexOf(idx);
  document.getElementById("btnRevPrev").disabled = (pos <= 0);
  document.getElementById("btnRevNext").disabled = (pos >= reviewQuestionIndices.length - 1);
}}

/* =====================================================================
   FULL PRINTABLE SOLUTION LIST
===================================================================== */
function renderFullListSolutions() {{
  const container = document.getElementById("solutionReviewContainer");
  container.innerHTML = "";

  QUESTIONS.forEach((q, idx) => {{
    const userAns = userAnswers[idx];
    const isCorrect = userAns === q.answer;
    const isUnattempted = userAns === null;
    const isMarked = wasEverMarked[idx];

    const card = document.createElement("div");
    card.className = `list-q-card ${{isCorrect ? 'correct' : (isUnattempted ? 'unattempted' : 'incorrect')}}`;
    
    let optHtml = "";
    q.options.forEach(o => {{
      let style = "padding:6px 12px; margin:4px 0; border-radius:4px; font-size:0.88rem;";
      if (o.label === q.answer && o.label === userAns) {{
        style += " background:#dcfce7; color:#166534; font-weight:700; border:1.5px solid #22c55e;";
      }} else if (o.label === q.answer) {{
        style += " background:#dcfce7; color:#166534; font-weight:700; border:1px solid #86efac;";
      }} else if (o.label === userAns) {{
        style += " background:#fee2e2; color:#991b1b; font-weight:700; border:1px solid #fca5a5;";
      }} else {{
        style += " background:#f8fafc; color:#475569;";
      }}
      optHtml += `<div style="${{style}}">${{o.label}}. ${{o.text}}</div>`;
    }});

    card.innerHTML = `
      <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
        <span style="font-weight:700; font-size:0.95rem;">Q${{idx + 1}}. (${{q.subject || ''}})</span>
        <div>
          ${{isMarked ? '<span class="badge badge-reviewed" style="margin-right:6px;">★ Marked Review</span>' : ''}}
          <span class="badge badge-origin">${{q.origin_tag || (q.label || 'Mock')}}</span>
        </div>
      </div>
      <div style="font-size:0.98rem; font-weight:600; margin-bottom:8px; color:#0f172a;">${{q.text}}</div>
      ${{q.text_alt ? `<div style="font-size:0.88rem; color:#475569; margin-bottom:10px;">${{q.text_alt}}</div>` : ''}}
      <div style="margin:10px 0;">${{optHtml}}</div>
      <div style="font-size:0.84rem; margin-top:8px;">
        <strong>Your Choice:</strong> ${{userAns ? userAns : '<span style="color:#64748b;">Not Attempted</span>'}} |
        <strong style="color:#16a34a;">Official Key:</strong> ${{q.answer}}
      </div>
      <div class="rev-rationale-box" style="margin-top:10px;">
        <div class="rev-rationale-title">Verified Explanation</div>
        <div class="rev-rationale-text">${{q.explanation || 'No detailed explanation provided.'}}</div>
      </div>
    `;
    container.appendChild(card);
  }});
}}
</script>
</body>
</html>
"""
    return html
