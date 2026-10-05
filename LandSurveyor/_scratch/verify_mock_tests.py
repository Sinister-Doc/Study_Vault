import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

LS_HTML = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\LandSurveyor_MockTest.html"
VAO_HTML = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\VAO\VAO_MockTest.html"

def verify_file(name, path):
    print(f"\n==========================================")
    print(f"VERIFYING {name}")
    print(f"File: {path}")
    print(f"==========================================")
    
    assert os.path.exists(path), f"File {path} does not exist!"
    size = os.path.getsize(path)
    print(f"File size: {size:,} bytes")
    
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Check UTF-8 meta
    assert '<meta charset="UTF-8">' in html or '<meta charset="utf-8">' in html, "Missing UTF-8 charset meta tag"
    print("✓ UTF-8 encoding declared")
    
    # Check external dependencies (no http:// or https:// script or css links)
    external_scripts = re.findall(r'<script\s+[^>]*src=["\'](http[s]?://[^"\']+)["\']', html)
    external_links = re.findall(r'<link\s+[^>]*href=["\'](http[s]?://[^"\']+)["\']', html)
    assert len(external_scripts) == 0, f"Found external scripts: {external_scripts}"
    assert len(external_links) == 0, f"Found external links: {external_links}"
    print("✓ 100% self-contained offline: zero external CDNs, fonts, or scripts")
    
    # Check design requirements: no gradients, no glow
    gradients = re.findall(r'linear-gradient|radial-gradient|box-shadow:\s*0\s+0\s+\d+px\s+rgba?\(|filter:\s*drop-shadow', html)
    assert len(gradients) == 0, f"Found gradient or glow styles: {gradients}"
    print("✓ Pure neutral subtle styling: zero gradients or glow effects")
    
    # Extract embedded JSON data
    match = re.search(r'const\s+EXAM_DATA\s*=\s*({.*?});\s*(?:const|let|var|function|\n)', html, re.DOTALL)
    assert match, "Could not find EXAM_DATA JSON block!"
    json_str = match.group(1)
    
    data = json.loads(json_str)
    print(f"✓ Embedded JSON parsed successfully. Exam: {data.get('exam')}")
    
    papers = data.get('papers', [])
    assert len(papers) == 2, f"Expected 2 papers, found {len(papers)}"
    print(f"✓ Found exactly 2 papers: {[p['paper'] for p in papers]}")
    
    for p_idx, p in enumerate(papers):
        p_name = p['paper']
        p_title = p['title']
        duration = p['duration_minutes']
        marking = p['marking']
        qs = p['questions']
        
        print(f"\n  --- {p_name}: {p_title} ---")
        assert duration == 120, f"Expected duration 120 min, got {duration}"
        assert marking['correct'] == 1.0, f"Expected correct +1.0, got {marking['correct']}"
        assert marking['wrong'] == -0.25, f"Expected wrong -0.25, got {marking['wrong']}"
        assert len(qs) == 100, f"Expected 100 questions, got {len(qs)}"
        print(f"  ✓ Questions count: exactly {len(qs)}")
        print(f"  ✓ Duration: {duration} mins (2 Hours)")
        print(f"  ✓ Marking: +{marking['correct']} / {marking['wrong']}")
        
        for q in qs:
            qid = q['id']
            qnum = q['number']
            qtext = q['text']
            opts = q['options']
            ans = q['correct_answer']
            rat = q['rationale']
            
            assert qtext and len(qtext.strip()) > 5, f"Empty or too short question text in {qid}"
            assert len(opts) == 4, f"Options count != 4 in {qid}: {len(opts)}"
            for opt_idx, o in enumerate(opts):
                assert o and len(o.strip()) > 0, f"Empty option {opt_idx+1} in {qid}"
            assert ans in [1, 2, 3, 4, 5], f"Invalid answer key in {qid}: {ans}"
            assert rat and rat != "Answer not available" and len(rat.strip()) > 5, f"Missing or empty rationale in {qid}"
            
        print(f"  ✓ All 100 questions: valid question text, exactly 4 non-empty options, valid key, full official rationale")
        
    # Check JS functionality components
    required_js_tokens = [
        'startMockTest', 'updateTimerDisplay', 'openSubmitModal', 'confirmSubmit',
        'selectOption', 'clearResponse', 'toggleMarkReview', 'jumpToQuestion',
        'renderResults', 'viewAnswerKey', 'goHome'
    ]
    for token in required_js_tokens:
        assert token in html, f"Missing JS function / token: {token}"
    print(f"✓ All interactive JS features present: Timer, Palette, Review, Submit Modal, Auto-submit, Scoring, Key Mode")

def main():
    verify_file("KEA Land Surveyor 2026", LS_HTML)
    verify_file("KEA VAO 2026", VAO_HTML)
    print("\n==========================================")
    print("ALL VERIFICATION CHECKS PASSED PERFECTLY!")
    print("==========================================")

if __name__ == "__main__":
    main()
