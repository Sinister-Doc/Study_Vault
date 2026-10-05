# -*- coding: utf-8 -*-
"""
Script to build Paper 1 Evaluation report for KEA VAO 2026
"""
import json, re

with open('VAO/AGY/08_Paper_Review/_work/p1_parsed_eval.json', 'r', encoding='utf-8') as f:
    p1_items = json.load(f)

# Load coaching text for explanations
with open('VAO/AGY/08_Paper_Review/_work/p1_coaching_text.txt', 'r', encoding='utf-8') as f:
    c_text = f.read()

# Build mapping of coaching explanations
# Coaching questions 1-100
c_items = re.findall(r'(\d+)\)\s*(.*?)(?=\n\s*\d+\)|\Z)', c_text, re.DOTALL)
coaching_exps = {}
for qnum_str, c_content in c_items:
    qn = int(qnum_str)
    # clean text
    clean_c = ' '.join(c_content.split())
    # remove leading 'ಸರಿಯಾದ ಉತ್ತರ : X' if present
    clean_c = re.sub(r'^ಸರಿಯಾದ\s*ಉತ\s*ರ\s*:\s*[A-D]\s*', '', clean_c)
    coaching_exps[qn] = clean_c

print(f"Loaded {len(coaching_exps)} coaching explanations")

# Map to our questions
# Coaching_Q = (Our_Q - 10) if Our_Q > 10 else (Our_Q + 90)
for item in p1_items:
    our_q = item['q_num']
    coaching_q = (our_q - 10) if our_q > 10 else (our_q + 90)
    item['coaching_q'] = coaching_q
    item['coaching_exp'] = coaching_exps.get(coaching_q, '')

with open('VAO/AGY/08_Paper_Review/_work/p1_items_with_exps.json', 'w', encoding='utf-8') as f:
    json.dump(p1_items, f, ensure_ascii=False, indent=2)

print("Saved p1_items_with_exps.json successfully")
