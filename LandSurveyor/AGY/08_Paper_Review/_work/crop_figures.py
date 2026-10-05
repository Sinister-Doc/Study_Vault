# -*- coding: utf-8 -*-
"""
Crop referenced diagrams/figures for KEA Land Surveyor 2026 Paper 1 and Paper 2
Refined high-precision bounding boxes.
"""
import os
import pymupdf

BASE_DIR = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\AGY\08_Paper_Review"
PAGES_DIR = os.path.join(BASE_DIR, "_pages")
FIGURES_DIR = os.path.join(BASE_DIR, "_figures")

os.makedirs(FIGURES_DIR, exist_ok=True)

crops = [
    {
        "page": "paper1_p17.png",
        "out": "P1-Q048_barchart.png",
        "bbox": (120, 210, 710, 700)
    },
    {
        "page": "paper2_p11.png",
        "out": "P2-Q032_map.png",
        "bbox": (75, 135, 495, 605)
    },
    {
        "page": "paper2_p22.png",
        "out": "P2-Q064_triangle.png",
        "bbox": (70, 1085, 535, 1405)
    },
    {
        "page": "paper2_p23.png",
        "out": "P2-Q066_triangle.png",
        "bbox": (75, 905, 465, 1335)
    },
    {
        "page": "paper2_p25.png",
        "out": "P2-Q069_midpoints.png",
        "bbox": (80, 185, 410, 535)
    },
    {
        "page": "paper2_p28.png",
        "out": "P2-Q082_rectangles.png",
        "bbox": (70, 950, 460, 1275)
    },
    {
        "page": "paper2_p30.png",
        "out": "P2-Q086_parabola.png",
        "bbox": (90, 130, 530, 420)
    },
    {
        "page": "paper2_p31.png",
        "out": "P2-Q092_cyclic_quad.png",
        "bbox": (70, 860, 440, 1270)
    },
    {
        "page": "paper2_p34.png",
        "out": "P2-Q100_parallelogram.png",
        "bbox": (90, 130, 600, 410)
    }
]

for c in crops:
    in_path = os.path.join(PAGES_DIR, c["page"])
    out_path = os.path.join(FIGURES_DIR, c["out"])
    doc = pymupdf.open(in_path)
    page = doc[0]
    pix_orig = pymupdf.Pixmap(in_path)
    scale_x = pix_orig.width / page.rect.width
    scale_y = pix_orig.height / page.rect.height
    x0, y0, x1, y1 = c["bbox"]
    clip_pts = pymupdf.Rect(x0 / scale_x, y0 / scale_y, x1 / scale_x, y1 / scale_y)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(scale_x, scale_y), clip=clip_pts)
    pix.save(out_path)
    print(f"Cropped {c['out']}: size={pix.width}x{pix.height}")
