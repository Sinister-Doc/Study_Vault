import pymupdf, os

src = {
    'LS': r'D:\SUPREETH N\Program Files\.claude\projects\D--SUPREETH-N-Program-Files-ObsidianVaults-StudyPrep\4d0cf695-d4d7-4fa9-945e-504038bfe281\tool-results\webfetch-1790667292814-vguwje.pdf',
    'VAO': r'D:\SUPREETH N\Program Files\.claude\projects\D--SUPREETH-N-Program-Files-ObsidianVaults-StudyPrep\4d0cf695-d4d7-4fa9-945e-504038bfe281\tool-results\webfetch-1790667288701-kiw123.pdf',
}
out = r'D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\ClaudeCode\07_Agent_Log\_pdf_pages'
os.makedirs(out, exist_ok=True)
for tag, f in src.items():
    d = pymupdf.open(f)
    for i in range(d.page_count):
        pix = d[i].get_pixmap(dpi=170)
        pix.save(os.path.join(out, '%s_p%02d.png' % (tag, i + 1)))
    print(tag, d.page_count, 'pages rendered')
    d.close()