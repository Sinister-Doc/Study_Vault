---
exam: KEA Land Surveyor 2026
subject: Paper-II Computer Applications (C-i) — MS Office, AutoCAD, DXF
topic: Word, Excel, PowerPoint essentials; AutoCAD commands, coordinates, hatching, 3D, DXF import/export
priority: Tier 1 (part of 20 marks)
tags: [land-surveyor, paper-2, computer, ms-office, autocad, dxf]
---

# 17. Computer Applications — MS Office & AutoCAD

> [!IMPORTANT] Exam focus
> Notified: MS Word, Excel, PowerPoint; **AutoCAD**: introduction, *all commands*, drawing triangles/rectangles, text, hatching, 2D→3D, extrusion, mirror; DXF import, export and editing of cadastral data. Expect "which command does X" and shortcut-key MCQs.

---

## 1. MS Word

- File formats: `.docx` (document), `.dotx` (template), `.doc` (older), `.pdf` (export).
- Tabs: File, Home, Insert, Design, Layout, References, Mailings, Review, View.
- **Formatting:** font, size, bold/italic/underline, alignment (left, centre, right, justify), line spacing, bullets/numbering, styles and headings (used to build a Table of Contents), page margins/orientation/size.
- **Insert:** table, picture, header/footer, page number, hyperlink, text box, symbol.
- **Mail Merge** (Mailings tab): one letter + a data source → many personalised letters.
- **Review:** spelling & grammar, Track Changes, Comments.
- **Shortcuts:** Ctrl+C copy, Ctrl+X cut, Ctrl+V paste, Ctrl+Z undo, Ctrl+Y redo, Ctrl+B/I/U, Ctrl+A select all, Ctrl+S save, Ctrl+P print, Ctrl+F find, Ctrl+H replace, Ctrl+E centre, Ctrl+L left, Ctrl+R right, Ctrl+J justify, Ctrl+Enter page break, F12 Save As, F7 spell check.

## 2. MS Excel

- Workbook = file (`.xlsx`); worksheet = sheet; cell address like `B3`; a range like `A1:C10`. A sheet has 1,048,576 rows and 16,384 columns (A to XFD).
- Formulas always start with **`=`**.
- **Functions:** `SUM`, `AVERAGE`, `MIN`, `MAX`, `COUNT` (numbers), `COUNTA` (non-blank), `COUNTIF`, `SUMIF`, `IF`, `ROUND`, `VLOOKUP`/`XLOOKUP`, `CONCATENATE`/`&`, `TODAY()`, `SQRT`, `PI()`, trigonometry (`SIN` etc. use **radians**; convert with `RADIANS()`).
- **References:** relative (`A1`), absolute (`$A$1`, press **F4**), mixed (`$A1`).
- Common errors: `#DIV/0!` (divide by zero), `#NAME?` (unknown function/name), `#VALUE!` (wrong data type), `#REF!` (deleted reference), `#N/A` (lookup not found), `####` (column too narrow).
- Tools: Sort, Filter, Conditional Formatting, Data Validation, **PivotTable**, charts (column, line, pie), Freeze Panes, Format as Table.
- Survey use: coordinate and area computation (shoelace formula), traverse tables, bearing–angle conversions, earthwork tables.
- **Shortcuts:** F2 edit cell, Ctrl+; today's date, Ctrl+Shift+L filter, Alt+= AutoSum, Ctrl+Arrow jump to data edge, F4 toggle absolute reference.

## 3. MS PowerPoint

- Presentation (`.pptx`), show (`.ppsx`). Slide layouts, themes/design, master slide, animations (objects) vs **transitions** (between slides), slide sorter view, notes page, Presenter view.
- **Shortcuts:** F5 start from beginning, Shift+F5 from current slide, Esc end show, Ctrl+M new slide, B/W blank/white screen during a show.

---

## 4. AutoCAD — introduction

- **AutoCAD** (Autodesk) = CAD software for 2D drafting and 3D modelling; the survey profession uses it for plans, sheets and cadastral maps.
- Native format **`.dwg`**; exchange format **`.dxf`**; templates `.dwt`; backup `.bak`; auto-save `.sv$`.
- Interface: Application menu, Quick Access toolbar, **Ribbon** (Home, Insert, Annotate, Layout, View...), **Command line** (bottom), **Drawing area** (model space), **Status bar**, ViewCube, Layout tabs (paper space).
- Units: `UNITS` command (metric: metres/millimetres; decimal degrees or DMS). Limits: `LIMITS`. Model space = drawing at full scale (1:1); Paper space/layout = sheet with viewports and scale.
- **Coordinate entry**

| Method | Format | Meaning |
| :--- | :--- | :--- |
| Absolute | `x,y` | from the origin (0,0) |
| Relative Cartesian | `@dx,dy` | from the last point |
| Relative polar | `@distance<angle` | angle counter-clockwise from +X (0° = East) |
| Direct distance | type a number after pointing direction (Ortho on) | quick lines |

> [!EXAMPLE] Triangle: `LINE` → `0,0` → `@100<0` → `@100<120` → `C` (close) draws an equilateral triangle of side 100. Rectangle: `RECTANG` → `0,0` → `@50,30`.

## 5. Function keys and drafting aids

| Key | Function |
| :--- | :--- |
| F1 | Help |
| F2 | Text window |
| F3 | Object snap on/off |
| F7 | Grid |
| F8 | Ortho (horizontal/vertical only) |
| F9 | Snap mode |
| F10 | Polar tracking |
| F11 | Object snap tracking |
| F12 | Dynamic input |
| Esc | cancel command |
| Enter / Space | repeat/confirm |
| Ctrl+Z / Ctrl+Y | undo / redo (`U`, `REDO`) |

**Object snaps (OSNAP):** Endpoint, Midpoint, Centre, Node, Quadrant, Intersection, Extension, Perpendicular, Tangent, Nearest.

## 6. Commands (alias in brackets)

**Draw**

| Command | Purpose |
| :--- | :--- |
| `LINE` (L) | straight segments |
| `POLYLINE` (PL) | connected segments as one object; can have width; used for parcel boundaries (closed) |
| `CIRCLE` (C) | centre-radius, 2P, 3P, TTR |
| `ARC` (A) | many options |
| `RECTANG` (REC) | rectangle |
| `POLYGON` (POL) | regular polygon 3–1024 sides (inscribed/circumscribed) |
| `ELLIPSE` (EL), `SPLINE` (SPL), `POINT` (PO) | curves, points |
| `HATCH` (H) | fill an enclosed area with a pattern |
| `TEXT` (DT single-line) / `MTEXT` (T, MT multi-line) | text writing |
| `BLOCK` (B), `INSERT` (I) | define/insert reusable objects |

**Modify**

| Command | Purpose |
| :--- | :--- |
| `ERASE` (E) | delete |
| `COPY` (CO/CP), `MOVE` (M) | copy/move |
| `ROTATE` (RO) | rotate about a base point |
| `SCALE` (SC) | resize |
| `MIRROR` (MI) | mirror image about a line (option: delete source or keep) |
| `OFFSET` (O) | parallel copy at distance |
| `TRIM` (TR), `EXTEND` (EX) | cut/lengthen to boundaries |
| `FILLET` (F), `CHAMFER` (CHA) | round/bevel corners |
| `STRETCH` (S) | move part of an object (crossing window) |
| `ARRAY` (AR) | rectangular/polar/path copies |
| `EXPLODE` (X) | break polyline/block to parts; `JOIN` (J) joins |
| `BREAK` (BR), `LENGTHEN` (LEN), `PEDIT` (PE) | edit lines/polylines |

**Annotation and inquiry**
- `DIM` and `DIMLINEAR` (DLI), `DIMALIGNED`, `DIMANGULAR`, `DIMRADIUS`, `DIMDIAMETER`; `LEADER`, `TABLE`; `DIMSTYLE`, `TEXTSTYLE`.
- `DIST` (DI) distance/angle; `AREA` (AA) area and perimeter (Object option for closed polylines); `ID` coordinates of a point; `LIST` object properties; `MEASURE`, `DIVIDE` (place points along an object).
- `ZOOM` (Z) (Extents, Window, All), `PAN` (P), `REGEN` (RE), `PURGE`, `AUDIT`, `OVERKILL`.
- `LAYER` (LA): manage layers (colour, linetype, lineweight, on/off, freeze, lock). Good practice: separate layers for boundary, survey numbers, text, dimensions, roads.

**Hatching:** `H` → pick internal point or select objects → choose pattern (ANSI31, SOLID...), scale, angle. Area must be **closed**; gaps make hatch fail. Associative hatch updates with the boundary.

## 7. 2D to 3D basics

- Switch workspace to **3D Modeling**; views: Top, SW Isometric etc. (ViewCube); `3DORBIT`; visual styles (`VSCURRENT`: 2D Wireframe, Conceptual, Realistic).
- **`EXTRUDE` (EXT):** gives height to a closed 2D shape (closed polyline, circle, region) → 3D solid (rectangle → cuboid; circle → cylinder). Option Taper angle.
- **`REVOLVE` (REV)** spins a profile about an axis; **`SWEEP`, `LOFT`**.
- Primitives: `BOX`, `CYLINDER`, `SPHERE`, `CONE`, `WEDGE`, `PYRAMID`, `TORUS`.
- Boolean: **`UNION` (UNI)**, **`SUBTRACT` (SU)**, **`INTERSECT` (IN)**.
- `3DMIRROR` mirrors 3D objects about a plane; `3DROTATE`, `3DMOVE`; `UCS` (User Coordinate System) sets the working plane; `PRESSPULL` pushes/pulls faces.
- Extrusion of a **closed polyline** requires that the polyline is closed (use `PEDIT` → Close, or `REGION`).

---

## 8. DXF files — import, export, editing cadastral data

- **DXF = Drawing Exchange Format**: Autodesk's open format to exchange drawings between CAD, GIS and survey software. Available as ASCII (text) or binary. Sections: HEADER, CLASSES, TABLES, BLOCKS, ENTITIES, OBJECTS.
- **DWG** is the native (proprietary) binary; DXF is more portable but geometry-only (no GIS attribute table).
- **Export:** `SAVEAS` → choose *AutoCAD DXF* version (e.g. 2018/2013/R12); or `DXFOUT` (older).
- **Import/open:** `OPEN` a `.dxf` directly; or `INSERT`/`IMPORT` into an existing drawing; QGIS/ArcGIS can also read DXF (convert layers to shapefiles).
- **Cadastral DXF data (typical):** parcel boundaries as **closed polylines** on a layer; survey/hissa numbers as text; corner points as `POINT` entities; road, water and village boundary on their own layers; coordinates in a projected system (UTM/local).
- **Editing steps:** open DXF → check units (`UNITS`), `ZOOM E` → run `PURGE`/`OVERKILL` → fix gaps (`PEDIT` join, snap endpoints), ensure polylines are **closed** → correct text/layers → `AREA` to verify parcel areas → save as new file (keep the original) → export DXF/shapefile for GIS or Mojini/Bhoomi upload.
- **Common problems:** wrong units (mm vs m), missing closure, duplicate lines, mixed coordinate systems, missing SHX fonts, overlapping parcels.

---

## High-Yield Mnemonics

> [!NOTE] Memory aids
> - **F3 osnap, F8 ortho, F9 snap, F10 polar, F7 grid, F2 text window.**
> - **DWG = native, DXF = exchange.**
> - **Absolute `x,y`; relative `@dx,dy`; polar `@d<a`.**
> - **Extrude needs a CLOSED shape.**
> - **Excel formulas start with `=`; `$` locks (F4).**

## Likely Exam Questions

1. Command to make a mirror image — **MIRROR**.
2. Command to give height to a 2D closed object — **EXTRUDE**.
3. Key to toggle Ortho mode — **F8**; Object Snap — **F3**.
4. File format for exchanging drawings between CAD/GIS — **DXF**.
5. Relative coordinate format — **@dx,dy**.
6. Command used to fill an enclosed area with a pattern — **HATCH**.
7. Excel function to count numeric cells — **COUNT**.
8. Shortcut to start a slide show from the beginning — **F5**.

## Quick Revision Box

```
+---------------------------------------------------------------+
| AutoCAD: DWG native, DXF exchange | Commands: L, PL, C, REC   |
| Coord: x,y | @dx,dy | @dist<angle | F3 osnap F8 ortho F10 polar |
| Modify: CO, M, RO, SC, MI, O, TR, EX, F, CHA, S, AR, X, J     |
| HATCH (closed area) | TEXT/MTEXT | DIM | LAYER | AREA | DIST    |
| 3D: EXTRUDE, REVOLVE, UNION, SUBTRACT, 3DORBIT                |
| DXF: Drawing eXchange Format | SAVEAS / OPEN | cadastral:     |
|   closed polylines + text on layers | check units, closure     |
| Excel: = | SUM AVERAGE IF VLOOKUP COUNTIF | $A$1 (F4)          |
| Word: Ctrl+C X V Z Y | Mail merge | PPT: F5 show                |
+---------------------------------------------------------------+
```

*Related:* [[18_Computer_GIS_Software_QGIS_GeoServer_PostGIS]] · [[19_Computer_Software_Solutions_and_Land_Records_IT]]
