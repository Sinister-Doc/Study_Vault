import re
import json
import os

def parse_evaluation(filepath):
    answers = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        if line.strip().startswith('|') and 'Question ID' not in line and '---' not in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) > 8:
                q_id = parts[2]
                key = parts[5]
                rationale = parts[8]
                try:
                    key_int = int(key)
                except:
                    key_int = None
                answers[q_id] = {
                    'key': key_int,
                    'rationale': rationale
                }
    return answers

def markdown_to_html(text):
    if not text:
        return ""
    # bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    
    # obsidian images
    text = re.sub(r'!\[\[(.*?)\]\]', r'[Image removed: \1]', text)
    
    # tables
    lines = text.split('\n')
    in_table = False
    html_lines = []
    
    for line in lines:
        if line.strip().startswith('|'):
            if not in_table:
                html_lines.append('<table border="1" style="border-collapse: collapse; margin-bottom: 10px;">')
                in_table = True
            
            if '---' in line:
                continue # skip separator
            
            cells = [c.strip() for c in line.split('|')[1:-1]]
            html_lines.append('<tr>' + ''.join(f'<td style="padding: 5px;">{c}</td>' for c in cells) + '</tr>')
        else:
            if in_table:
                html_lines.append('</table>')
                in_table = False
            html_lines.append(line)
            
    if in_table:
        html_lines.append('</table>')
        
    res = '<br>'.join(html_lines)
    # fix the <br> after table
    res = res.replace('</table><br>', '</table>')
    res = res.replace('<table border="1" style="border-collapse: collapse; margin-bottom: 10px;"><br>', '<table border="1" style="border-collapse: collapse; margin-bottom: 10px;">')
    return res

def parse_questions(filepath, answers):
    questions = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Split by horizontal rule
    blocks = re.split(r'\n---\n', content)
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        # Ignore warning block if any
        if '> [!warning]' in block and 'Question:' not in block:
            continue
            
        # Match QID line
        qid_match = re.search(r'^(P[12]-Q\d{3})', block)
        if not qid_match:
            continue
            
        q_id = qid_match.group(1)
        
        # Match Question:
        q_text_match = re.search(r'Question:\s*(.*?)(?=\n- \[ \] \([1-5]\)|\Z)', block, re.DOTALL)
        if not q_text_match:
            continue
            
        q_text = q_text_match.group(1).strip()
        
        # Match options
        options = []
        for i in range(1, 5):
            opt_match = re.search(rf'- \[ \] \({i}\)\s*(.*?)(?=\n- \[ \] \([1-5]\)|\Z)', block, re.DOTALL)
            if opt_match:
                options.append(markdown_to_html(opt_match.group(1).strip()))
            else:
                options.append(f"Option {i}")
                
        # Get answer
        ans_data = answers.get(q_id, {})
        key = ans_data.get('key')
        rationale = ans_data.get('rationale', "Answer not available")
        
        # Parse question text to HTML
        html_text = markdown_to_html(q_text)
        
        q_num = int(q_id.split('-Q')[1])
        
        questions.append({
            "id": q_id,
            "number": q_num,
            "text": html_text,
            "options": options,
            "correct_answer": key,
            "rationale": markdown_to_html(rationale) if rationale != "Answer not available" else rationale
        })
        
    return questions

def main():
    base_dir = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\AGY\08_Paper_Review"
    p1_eval = os.path.join(base_dir, "Paper1_Evaluation.md")
    p1_ques = os.path.join(base_dir, "Paper1_Questions.md")
    p2_eval = os.path.join(base_dir, "Paper2_Evaluation.md")
    p2_ques = os.path.join(base_dir, "Paper2_Questions.md")
    
    out_file = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\_scratch\exam_data.json"
    
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    
    ans1 = parse_evaluation(p1_eval)
    q1 = parse_questions(p1_ques, ans1)
    
    ans2 = parse_evaluation(p2_eval)
    q2 = parse_questions(p2_ques, ans2)
    
    exam_data = {
        "papers": [
            {
                "paper": "Paper 1",
                "title": "General Knowledge / General Studies",
                "duration_minutes": 120,
                "total_questions": len(q1),
                "marking": { "correct": 1.0, "wrong": -0.25, "unattempted": 0.0 },
                "questions": q1
            },
            {
                "paper": "Paper 2",
                "title": "Specific Paper",
                "duration_minutes": 120,
                "total_questions": len(q2),
                "marking": { "correct": 1.0, "wrong": -0.25, "unattempted": 0.0 },
                "questions": q2
            }
        ]
    }
    
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(exam_data, f, indent=2, ensure_ascii=False)
        
    print(f"Parsed {len(q1)} questions for Paper 1 and {len(q2)} questions for Paper 2.")
    print("Writing HTML...")
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEA Land Surveyor 2026 Mock Test</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background-color: #fff;
            padding: 20px;
            border-bottom: 1px solid #ddd;
            text-align: center;
        }}
        .paper-card {{
            background: #fff;
            padding: 20px;
            margin: 20px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        .btn {{
            padding: 10px 20px;
            margin: 10px 10px 0 0;
            background: #eee;
            border: 1px solid #ccc;
            cursor: pointer;
            font-size: 14px;
            border-radius: 4px;
        }}
        .btn:hover {{ background: #ddd; }}
        .btn-primary {{ background: #333; color: #fff; border-color: #333; }}
        .btn-primary:hover {{ background: #555; }}
        
        /* Test interface */
        #test-interface, #result-interface, #answer-key-interface {{ display: none; }}
        
        .test-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #fff;
            padding: 15px;
            border: 1px solid #ddd;
            margin-bottom: 20px;
        }}
        .timer {{ font-size: 20px; font-weight: bold; }}
        
        .test-body {{ display: flex; gap: 20px; }}
        .question-area {{
            flex: 1;
            background: #fff;
            padding: 20px;
            border: 1px solid #ddd;
        }}
        .palette-area {{
            width: 250px;
            background: #fff;
            padding: 20px;
            border: 1px solid #ddd;
        }}
        
        .q-text {{ margin-bottom: 20px; font-size: 16px; line-height: 1.5; }}
        .option {{
            display: block;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            cursor: pointer;
            border-radius: 4px;
        }}
        .option:hover {{ background: #f9f9f9; }}
        .option input {{ margin-right: 10px; }}
        
        .palette-grid {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 5px;
            margin-top: 15px;
        }}
        .palette-btn {{
            width: 100%;
            padding: 8px 0;
            text-align: center;
            border: 1px solid #ccc;
            background: #fff;
            cursor: pointer;
            font-size: 12px;
        }}
        .palette-btn.answered {{ background: #4CAF50; color: white; border-color: #4CAF50; }}
        .palette-btn.marked {{ background: #FF9800; color: white; border-color: #FF9800; }}
        .palette-btn.unanswered {{ background: #f44336; color: white; border-color: #f44336; }}
        .palette-btn.active {{ border: 2px solid #333; font-weight: bold; }}
        
        .controls {{
            margin-top: 20px;
            display: flex;
            justify-content: space-between;
            border-top: 1px solid #ddd;
            padding-top: 20px;
        }}
        
        .stat-box {{
            background: #fff;
            padding: 20px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        
        .review-q {{ margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid #eee; }}
        .correct-opt {{ background: #e8f5e9; border-color: #4CAF50; }}
        .wrong-opt {{ background: #ffebee; border-color: #f44336; }}
        .rationale {{ background: #fff3e0; padding: 15px; margin-top: 15px; border-left: 4px solid #ff9800; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>KEA Land Surveyor Competitive Examination 2026</h1>
        <p>Mock Test Platform</p>
    </div>

    <div class="container" id="home-interface">
        <div class="paper-card">
            <h2>Paper 1: General Knowledge / General Studies</h2>
            <p>Duration: 120 minutes | 100 Questions | +1.0 for correct, -0.25 for wrong</p>
            <button class="btn btn-primary" onclick="startTest(0)">Take Mock Test</button>
            <button class="btn" onclick="showAnswerKey(0)">View Answer Key</button>
        </div>
        <div class="paper-card">
            <h2>Paper 2: Specific Paper</h2>
            <p>Duration: 120 minutes | 100 Questions | +1.0 for correct, -0.25 for wrong</p>
            <button class="btn btn-primary" onclick="startTest(1)">Take Mock Test</button>
            <button class="btn" onclick="showAnswerKey(1)">View Answer Key</button>
        </div>
    </div>

    <div class="container" id="test-interface">
        <div class="test-header">
            <h2 id="test-title">Paper Name</h2>
            <div class="timer" id="timer">120:00</div>
            <button class="btn btn-primary" onclick="submitTestConfirm()">Submit Test</button>
        </div>
        <div class="test-body">
            <div class="question-area">
                <h3 id="q-number">Question 1</h3>
                <div class="q-text" id="q-text"></div>
                <div id="options-area"></div>
                <div class="controls">
                    <div>
                        <button class="btn" onclick="clearResponse()">Clear Response</button>
                        <button class="btn" onclick="markReview()">Mark for Review</button>
                    </div>
                    <div>
                        <button class="btn" onclick="prevQuestion()">Previous</button>
                        <button class="btn btn-primary" onclick="nextQuestion()">Next</button>
                    </div>
                </div>
            </div>
            <div class="palette-area">
                <h3>Question Palette</h3>
                <div style="font-size: 12px; margin-bottom: 10px;">
                    <span style="display:inline-block; width:10px; height:10px; background:#4CAF50; margin-right:5px;"></span> Answered<br>
                    <span style="display:inline-block; width:10px; height:10px; background:#FF9800; margin-right:5px;"></span> Marked<br>
                    <span style="display:inline-block; width:10px; height:10px; background:#fff; border:1px solid #ccc; margin-right:5px;"></span> Unanswered
                </div>
                <div class="palette-grid" id="palette-grid"></div>
            </div>
        </div>
    </div>

    <div class="container" id="result-interface">
        <h2>Test Results</h2>
        <div class="stat-box" id="score-card"></div>
        <button class="btn btn-primary" onclick="goHome()">Back to Home</button>
        <h3 style="margin-top: 30px;">Review Questions</h3>
        <div id="review-area" class="stat-box"></div>
    </div>

    <div class="container" id="answer-key-interface">
        <h2 id="ak-title">Answer Key</h2>
        <button class="btn" onclick="goHome()">Back to Home</button>
        <div id="ak-area" style="margin-top: 20px;"></div>
    </div>

    <script>
        const examData = {json.dumps(exam_data)};
        let currentPaperIdx = 0;
        let currentQIdx = 0;
        let responses = []; // {{ selected: null, marked: false }}
        let timerInterval = null;
        let timeRemaining = 0;
        
        function goHome() {{
            document.getElementById('home-interface').style.display = 'block';
            document.getElementById('test-interface').style.display = 'none';
            document.getElementById('result-interface').style.display = 'none';
            document.getElementById('answer-key-interface').style.display = 'none';
            clearInterval(timerInterval);
        }}
        
        function startTest(paperIdx) {{
            currentPaperIdx = paperIdx;
            currentQIdx = 0;
            let paper = examData.papers[paperIdx];
            responses = Array(paper.total_questions).fill(null).map(() => ({{selected: null, marked: false}}));
            timeRemaining = paper.duration_minutes * 60;
            
            document.getElementById('home-interface').style.display = 'none';
            document.getElementById('test-interface').style.display = 'block';
            document.getElementById('test-title').innerText = paper.title;
            
            initPalette();
            renderQuestion();
            
            clearInterval(timerInterval);
            updateTimerDisplay();
            timerInterval = setInterval(() => {{
                timeRemaining--;
                updateTimerDisplay();
                if(timeRemaining <= 0) {{
                    clearInterval(timerInterval);
                    alert("Time's up! Auto-submitting test.");
                    submitTest();
                }}
            }}, 1000);
        }}
        
        function updateTimerDisplay() {{
            let m = Math.floor(timeRemaining / 60);
            let s = timeRemaining % 60;
            document.getElementById('timer').innerText = `${{m.toString().padStart(2, '0')}}:${{s.toString().padStart(2, '0')}}`;
        }}
        
        function initPalette() {{
            let grid = document.getElementById('palette-grid');
            grid.innerHTML = '';
            for(let i=0; i<examData.papers[currentPaperIdx].total_questions; i++) {{
                let btn = document.createElement('div');
                btn.className = 'palette-btn';
                btn.innerText = i + 1;
                btn.id = 'pal-' + i;
                btn.onclick = () => {{ currentQIdx = i; renderQuestion(); }};
                grid.appendChild(btn);
            }}
            updatePalette();
        }}
        
        function updatePalette() {{
            for(let i=0; i<responses.length; i++) {{
                let btn = document.getElementById('pal-' + i);
                btn.className = 'palette-btn';
                if(responses[i].marked) btn.classList.add('marked');
                else if(responses[i].selected !== null) btn.classList.add('answered');
                if(i === currentQIdx) btn.classList.add('active');
            }}
        }}
        
        function renderQuestion() {{
            let q = examData.papers[currentPaperIdx].questions[currentQIdx];
            document.getElementById('q-number').innerText = "Question " + (currentQIdx + 1);
            document.getElementById('q-text').innerHTML = q.text;
            
            let optsHtml = '';
            for(let i=0; i<4; i++) {{
                let isChecked = responses[currentQIdx].selected === (i+1) ? 'checked' : '';
                optsHtml += `
                    <label class="option">
                        <input type="radio" name="opt" value="${{i+1}}" ${{isChecked}} onchange="selectOption(${{i+1}})">
                        (${{i+1}}) ${{q.options[i]}}
                    </label>
                `;
            }}
            document.getElementById('options-area').innerHTML = optsHtml;
            updatePalette();
        }}
        
        function selectOption(val) {{
            responses[currentQIdx].selected = val;
            updatePalette();
        }}
        
        function clearResponse() {{
            responses[currentQIdx].selected = null;
            renderQuestion();
        }}
        
        function markReview() {{
            responses[currentQIdx].marked = !responses[currentQIdx].marked;
            updatePalette();
        }}
        
        function nextQuestion() {{
            if(currentQIdx < examData.papers[currentPaperIdx].total_questions - 1) {{
                currentQIdx++;
                renderQuestion();
            }}
        }}
        
        function prevQuestion() {{
            if(currentQIdx > 0) {{
                currentQIdx--;
                renderQuestion();
            }}
        }}
        
        function submitTestConfirm() {{
            if(confirm("Are you sure you want to submit the test?")) {{
                submitTest();
            }}
        }}
        
        function submitTest() {{
            clearInterval(timerInterval);
            document.getElementById('test-interface').style.display = 'none';
            document.getElementById('result-interface').style.display = 'block';
            
            let paper = examData.papers[currentPaperIdx];
            let correct = 0;
            let wrong = 0;
            let unattempted = 0;
            
            let reviewHtml = '';
            
            for(let i=0; i<paper.total_questions; i++) {{
                let q = paper.questions[i];
                let ans = responses[i].selected;
                let key = q.correct_answer;
                
                let qStatus = "Unattempted";
                if(ans === null) {{
                    unattempted++;
                }} else if(ans === key) {{
                    correct++;
                    qStatus = "Correct";
                }} else {{
                    wrong++;
                    qStatus = "Wrong";
                }}
                
                reviewHtml += `<div class="review-q">`;
                reviewHtml += `<h4>Q${{i+1}}. [${{qStatus}}]</h4>`;
                reviewHtml += `<div>${{q.text}}</div><div style="margin-top:10px;">`;
                
                for(let j=0; j<4; j++) {{
                    let optNum = j+1;
                    let cls = "option";
                    if(optNum === key) cls += " correct-opt";
                    else if(optNum === ans) cls += " wrong-opt";
                    
                    let mark = "";
                    if(optNum === ans) mark += " (Your Answer)";
                    if(optNum === key) mark += " (Correct Answer)";
                    
                    reviewHtml += `<div class="${{cls}}">(${{optNum}}) ${{q.options[j]}} <b>${{mark}}</b></div>`;
                }}
                reviewHtml += `</div><div class="rationale"><b>Rationale:</b> ${{q.rationale}}</div></div>`;
            }}
            
            let score = (correct * paper.marking.correct) + (wrong * paper.marking.wrong);
            
            document.getElementById('score-card').innerHTML = `
                <h3>Score: ${{score.toFixed(2)}} / ${{paper.total_questions}}</h3>
                <p>Correct: ${{correct}}</p>
                <p>Wrong: ${{wrong}}</p>
                <p>Unattempted: ${{unattempted}}</p>
            `;
            
            document.getElementById('review-area').innerHTML = reviewHtml;
        }}
        
        function showAnswerKey(paperIdx) {{
            document.getElementById('home-interface').style.display = 'none';
            document.getElementById('answer-key-interface').style.display = 'block';
            let paper = examData.papers[paperIdx];
            document.getElementById('ak-title').innerText = paper.title + " - Answer Key";
            
            let akHtml = '';
            for(let i=0; i<paper.total_questions; i++) {{
                let q = paper.questions[i];
                akHtml += `<div class="stat-box review-q">`;
                akHtml += `<h4>Q${{i+1}}.</h4>`;
                akHtml += `<div>${{q.text}}</div><div style="margin-top:10px;">`;
                for(let j=0; j<4; j++) {{
                    let optNum = j+1;
                    let cls = "option";
                    if(optNum === q.correct_answer) cls += " correct-opt";
                    let mark = optNum === q.correct_answer ? " (Correct Answer)" : "";
                    akHtml += `<div class="${{cls}}">(${{optNum}}) ${{q.options[j]}} <b>${{mark}}</b></div>`;
                }}
                akHtml += `</div><div class="rationale"><b>Rationale:</b> ${{q.rationale}}</div></div>`;
            }}
            document.getElementById('ak-area').innerHTML = akHtml;
        }}
    </script>
</body>
</html>
"""
    
    html_file = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\LandSurveyor_MockTest.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"Generated HTML at {html_file}")

if __name__ == "__main__":
    main()
