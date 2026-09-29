# -*- coding: utf-8 -*-
"""
Deterministic QA checks for both KEA study kits.

Run:  python _qa_check.py

Checks, per kit (LandSurveyor\ClaudeCode and VAO\ClaudeCode):
  1. forbidden markers   [VERIFY] / [verify] / TODO / TBD / PLACEHOLDER
  2. broken wikilinks    every [[target]] (and [[target|alias]]) must resolve to a file
  3. empty / stub files  markdown files under ~500 bytes, or with no headings
  4. mermaid blocks      extracted and written out for mermaid-cli to validate
  5. http(s) URLs        listed, so reachability can be checked separately
Exit code is non-zero if any check fails.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
KITS = {
    "LandSurveyor": os.path.join(VAULT, "LandSurveyor", "ClaudeCode"),
    "VAO": os.path.join(VAULT, "VAO", "ClaudeCode"),
}

MARKERS = ["[VERIFY]", "[verify]", "TODO", "TBD", "PLACEHOLDER", "FIXME", "XXX"]
WIKILINK = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]")
MERMAID = re.compile(r"```mermaid\s*\n(.*?)```", re.S)
CODE_FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
URL = re.compile(r"https?://[^\s\)\]\>\}\"'`]+")

problems = 0
mermaid_out = []


def rel(p):
    return os.path.relpath(p, VAULT).replace("\\", "/")


for kit, root in KITS.items():
    print("\n" + "=" * 72)
    print("KIT: %s   (%s)" % (kit, rel(root)))
    print("=" * 72)

    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != "_pdf_pages"]
        for f in filenames:
            if f.lower().endswith(".md"):
                md_files.append(os.path.join(dirpath, f))
    md_files.sort()

    # all resolvable targets: every file in the kit, by stem and by relative path
    stems, relpaths = {}, set()
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            full = os.path.join(dirpath, f)
            rp = os.path.relpath(full, root).replace("\\", "/")
            relpaths.add(rp)
            relpaths.add(os.path.splitext(rp)[0])
            stems.setdefault(os.path.splitext(f)[0], []).append(rp)

    # ---- 1. forbidden markers ---------------------------------------------
    print("\n[1] Forbidden markers")
    marker_hits = 0
    for p in md_files:
        try:
            text = open(p, encoding="utf-8").read()
        except Exception as e:
            print("    !! cannot read %s (%s)" % (rel(p), e))
            problems += 1
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for m in MARKERS:
                if m in line:
                    print("    %s:%d  %s" % (rel(p), i, m))
                    marker_hits += 1
    print("    -> %d marker occurrence(s)" % marker_hits)
    if marker_hits:
        problems += 1

    # ---- 2. wikilinks ------------------------------------------------------
    print("\n[2] Wikilinks")
    total_links, broken = 0, []
    for p in md_files:
        text = open(p, encoding="utf-8").read()
        # Obsidian does not render a wikilink inside code as a link, so drop fenced
        # blocks and inline code spans before scanning. Also un-escape the alias
        # separator "\|", which Obsidian uses inside markdown tables.
        scan = INLINE_CODE.sub(" ", CODE_FENCE.sub(" ", text.replace("\\|", "|")))
        for target in WIKILINK.findall(scan):
            total_links += 1
            t = target.strip().replace("\\", "/").lstrip("/")
            ok = (t in relpaths or t + ".md" in relpaths or t + ".html" in relpaths
                  or os.path.basename(t) in stems
                  or os.path.splitext(os.path.basename(t))[0] in stems)
            if not ok:
                broken.append((rel(p), t))
    print("    -> %d wikilinks, %d broken" % (total_links, len(broken)))
    for src, t in broken:
        print("       BROKEN  %s  ->  [[%s]]" % (src, t))
    if broken:
        problems += 1

    # ---- 3. stub / empty files --------------------------------------------
    print("\n[3] Stub / empty markdown files")
    stubs = []
    for p in md_files:
        text = open(p, encoding="utf-8").read()
        if len(text) < 500:
            stubs.append((rel(p), len(text), "under 500 bytes"))
        elif not re.search(r"^#{1,3}\s+\S", text, re.M):
            stubs.append((rel(p), len(text), "no heading"))
    print("    -> %d markdown file(s), %d stub(s)" % (len(md_files), len(stubs)))
    for s in stubs:
        print("       STUB  %s (%d bytes, %s)" % s)
    if stubs:
        problems += 1

    # ---- 4. mermaid --------------------------------------------------------
    print("\n[4] Mermaid blocks")
    count = 0
    for p in md_files:
        text = open(p, encoding="utf-8").read()
        for i, block in enumerate(MERMAID.findall(text), 1):
            count += 1
            out = os.path.join(HERE, "_mermaid_%s_%02d.mmd" % (kit, count))
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(block.strip() + "\n")
            mermaid_out.append(out)
            nodes = len(re.findall(r"^\s*[A-Za-z0-9_]+\s*[\[\{\(]", block, re.M))
            flag = "  <-- over 15 nodes" if nodes > 15 else ""
            print("    %s #%d  (%d nodes)%s" % (rel(p), i, nodes, flag))
    print("    -> %d mermaid block(s) written for validation" % count)

    # ---- 5. URLs -----------------------------------------------------------
    print("\n[5] External URLs found in markdown")
    urls = set()
    for p in md_files:
        urls.update(URL.findall(open(p, encoding="utf-8").read()))
    print("    -> %d unique URL(s)" % len(urls))
    with open(os.path.join(HERE, "_urls_%s.txt" % kit), "w", encoding="utf-8") as fh:
        fh.write("\n".join(sorted(urls)))
    print("       written to _urls_%s.txt" % kit)

print("\n" + "=" * 72)
print("mermaid files to validate: %d" % len(mermaid_out))
print("RESULT: %s" % ("FAIL — see problems above" if problems else "PASS"))
sys.exit(1 if problems else 0)
