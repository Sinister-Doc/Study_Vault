# -*- coding: utf-8 -*-
import json

with open('VAO/AGY/08_Paper_Review/_work/p1_items_with_exps.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)

with open('VAO/AGY/08_Paper_Review/_work/p2_parsed_eval.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)

with open('VAO/AGY/08_Paper_Review/_work/all_qs_brief.txt', 'w', encoding='utf-8') as f:
    f.write("=== PAPER 1 ===\n")
    for it in p1:
        f.write(f"P1-Q{it['q_num']:03d} (Key={it['key']}, Marked={it['marked']}): {it['question'][:120]}\n")
    f.write("\n=== PAPER 2 ===\n")
    for it in p2:
        f.write(f"P2-Q{it['q_num']:03d} (Key={it['key']}, Marked={it['marked']}): {it['question'][:120]}\n")

print("Saved all_qs_brief.txt successfully")
