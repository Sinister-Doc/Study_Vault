---
exam: KEA Land Surveyor 2026
subject: Paper-II Computer Applications (C-ii) — GIS Software & Applications
topic: Open-source desktop GIS (QGIS), GeoServer/MapServer, OGC web services, PostGIS
priority: Tier 1 (part of 20 marks)
tags: [land-surveyor, paper-2, computer, qgis, geoserver, postgis, wms, wfs]
---

# 18. GIS Software — QGIS, GeoServer/MapServer, PostGIS

> [!IMPORTANT] Exam focus
> The notification describes an **open-source desktop GIS** (QGIS is the standard example): installation, interface, loading vector/raster, layer management, attribute table, spatial queries, digitising, styling, map layout and printing, plugins, **CRS management**, cadastral mapping; then **GeoServer/MapServer** publishing **WMS, WFS, WCS**; then **PostGIS**, the spatial extension to PostgreSQL.

---

## 1. Open-source desktop GIS — QGIS

- **QGIS** (formerly Quantum GIS): free, open-source (GPL) desktop GIS; runs on Windows, Linux, macOS; supports many formats via **GDAL/OGR**; can also use GRASS and SAGA tools. LTR = long-term-release versions are recommended for stability.
- **Installation:** download the installer (OSGeo4W or standalone MSI) from qgis.org; choose the LTR; installs QGIS Desktop + GRASS + SAGA + Python console.

**Interface**

| Panel | Function |
| :--- | :--- |
| **Browser panel** | navigate folders, databases, web services (add layers by drag-drop) |
| **Layers panel** | list, order, show/hide, style layers (layer on top draws above) |
| **Map canvas** | main map view |
| **Toolbars / menus** | Project, Edit, View, Layer, Settings, Plugins, Vector, Raster, Processing |
| **Processing Toolbox** | geoprocessing algorithms (Buffer, Clip, Intersection, Dissolve, Reproject...) |
| **Status bar** | coordinates, scale, rotation, **project CRS** |

**File formats**

| Type | Formats |
| :--- | :--- |
| Vector | **Shapefile** (`.shp` geometry, `.shx` index, `.dbf` attributes, `.prj` CRS — minimum), GeoPackage (`.gpkg`, modern single file), GeoJSON, KML, GPX, DXF, CSV with X/Y |
| Raster | GeoTIFF (`.tif`), JPEG2000, ECW, IMG, DEM (ASCII grid) |
| Database/services | PostGIS, SpatiaLite, WMS/WFS/XYZ tiles |

**Loading data:** Layer → Add Layer → Add Vector Layer / Add Raster Layer (or drag from Browser). CSV with coordinates: *Add Delimited Text Layer* (choose X and Y fields and the CRS).

**Layer management:** reorder, group, rename, zoom to layer, **export → Save As** (change format/CRS), set scale-dependent visibility, layer transparency, saving the **project** (`.qgz`/`.qgs`) stores layer links and styles (not the data itself).

**Attribute table operations:** open table (F6); select by clicking, expression, or location; sort; **field calculator** (create/update fields, e.g. `$area`, `$length`, `$x`); add/delete fields; join tables (Layer Properties → Joins); filter (Provider filter); statistics panel.

**Spatial queries and analysis**
- *Select by Expression* (`"area" > 1000`), *Select by Location* (intersects, within, touches...).
- **Vector tools:** Buffer, Clip, Intersect, Union, Difference, Dissolve, Merge, Centroids, Spatial join, Voronoi, Convex hull.
- **Raster tools:** Raster Calculator (map algebra), Clip, Reclassify, Slope/Aspect/Hillshade, Contour from DEM, Zonal statistics.

**Digitising and editing vector layers**
1. Create a new layer (Layer → Create Layer → New Shapefile/GeoPackage; choose geometry type, CRS, fields).
2. **Toggle Editing** (pencil).
3. **Add Polygon/Line/Point Feature**; left-click vertices, right-click to finish; fill attributes.
4. **Vertex Tool** edits nodes; Move, Split, Merge, Reshape features.
5. Turn on **Snapping** (Project → Snapping Options) to avoid gaps/overlaps; run **Topology Checker** plugin/tools (Check Validity, overlaps, gaps).
6. **Save Layer Edits**, then Toggle Editing off.
- **Georeferencer** (Layer → Georeferencer): convert a scanned map to a georeferenced raster using ground control points and a transformation (Linear, Polynomial, Thin Plate Spline), then resampling method.

**Styling and symbology (Layer Properties → Symbology)**
- **Single symbol**, **Categorized** (unique values, e.g. land-use type), **Graduated** (numeric ranges, e.g. area classes), **Rule-based**; labels (Labels tab) with placement/halo; transparency; **QML/SLD** style files can be saved and re-used.

**Map layout and printing:** Project → New Print Layout → Add Map, Legend, Scale Bar, North Arrow, Title/Label, Grid; set paper size and scale; **Export as PDF/Image/SVG**. **Atlas** creates a series of maps (e.g. one per village).

**Plugins and extensions:** Plugins → Manage and Install Plugins (core plugins and third-party repository). Useful: **QuickMapServices** (basemaps), **Semi-Automatic Classification**, **Topology Checker**, **DigitizingTools**, **QField Sync** (field data), **Freehand raster georeferencer**. Python (PyQGIS) console for scripting.

**Coordinate Reference System (CRS) management**
- **Project CRS** (status-bar) sets the map display; each layer has its own **layer CRS**. QGIS reprojects **on the fly**, but to permanently change a layer's CRS you must **export/reproject** it (Save As / *Reproject Layer*).
- **EPSG:4326** = WGS-84 geographic (lat/long, degrees); **EPSG:3857** = Web Mercator (web maps); **EPSG:32643** = WGS-84 / **UTM zone 43N** (75° E central meridian region; covers most of Karnataka), **EPSG:32644** = UTM zone 44N (east). India also uses Everest/WGS-84 datum-based grids (Lambert Conformal Conic for India).
- "Assign projection" (Set Layer CRS) vs "Reproject" — assigning only declares what the coordinates already are; reproject actually **transforms** the coordinates.

**Use in cadastral mapping:** load ORI/satellite basemap → georeference old village sheets → digitise parcel polygons (closed, no gaps/overlaps, topology checked) → attributes: survey number, hissa, owner/land class, area → calculate area with `$area` (in an equal-area or UTM CRS) → overlay with village boundary, roads → layouts/PDF maps.

---

## 2. GeoServer and MapServer — open-source map servers

- **GeoServer:** open-source (Java) server to **share and edit geospatial data** using **OGC standards**. Web administration UI. Concepts: **Workspace** (namespace), **Store** (connection to data: shapefile, PostGIS, GeoTIFF), **Layer** (published resource), **Style** (SLD — Styled Layer Descriptor), **Layer Groups**; caches tiles with GeoWebCache (WMTS).
- **MapServer:** open-source (C, CGI/FastCGI) engine by University of Minnesota; configured through a text **mapfile**; renders maps and serves WMS/WFS. Lightweight and fast.

**OGC web services (OGC = Open Geospatial Consortium)**

| Service | Returns | Main requests |
| :--- | :--- | :--- |
| **WMS** (Web Map Service) | **map images** (PNG/JPEG) — picture only | `GetCapabilities`, `GetMap`, `GetFeatureInfo` |
| **WFS** (Web Feature Service) | actual **vector features** (geometry + attributes) in GML/GeoJSON; **WFS-T** allows editing | `GetCapabilities`, `DescribeFeatureType`, `GetFeature`, `Transaction` |
| **WCS** (Web Coverage Service) | **raster coverages** (real pixel values: DEM, imagery) | `GetCapabilities`, `DescribeCoverage`, `GetCoverage` |
| **WMTS** | pre-rendered tiles for fast web mapping | `GetTile` |

- Remember: **WMS = look, WFS = features, WCS = coverages (rasters).**
- Clients: QGIS (Layer → Add WMS/WFS layer), web maps (OpenLayers, Leaflet), other GIS.
- Typical architecture: **PostGIS** (database) → **GeoServer** (publishes WMS/WFS) → **web/mobile app** (e.g. Dishank-type portals) → citizen.

## 3. PostGIS

- **PostGIS** = open-source **spatial extension to PostgreSQL** (object-relational database). It adds geometry/geography data types, spatial functions and **spatial indexes**, so location data can be stored and queried with SQL. Follows OGC Simple Features.
- Enable: `CREATE EXTENSION postgis;`
- Data types: `geometry` (planar, uses SRID/projection units), `geography` (spherical, metres), `raster`.
- **SRID** = spatial reference ID (EPSG code), e.g. 4326.
- Spatial index: **GiST** (`CREATE INDEX ... USING GIST (geom)`); makes searches fast.
- **Common functions:** `ST_Area`, `ST_Length`, `ST_Distance`, `ST_Buffer`, `ST_Intersects`, `ST_Contains`, `ST_Within`, `ST_Union`, `ST_Intersection`, `ST_Transform` (reproject), `ST_SetSRID`, `ST_AsText` (WKT), `ST_GeomFromText`, `ST_X/ST_Y`, `ST_Centroid`.
- **Example queries**

```sql
-- parcels of village 'X' with area over 1 hectare, in UTM 43N
SELECT survey_no, ST_Area(ST_Transform(geom, 32643)) AS area_m2
FROM parcels WHERE village = 'X'
  AND ST_Area(ST_Transform(geom, 32643)) > 10000;

-- parcels touching a road line
SELECT p.survey_no FROM parcels p, roads r
WHERE ST_Intersects(p.geom, r.geom);
```
- **Loading data:** `shp2pgsql` (shapefile → SQL), `ogr2ogr`, QGIS DB Manager, `raster2pgsql`.
- **Why use a spatial database for land records:** multi-user editing, integrity, security, backup, fast queries, integration with web services and RTC/Bhoomi text data.

---

## High-Yield Mnemonics

> [!NOTE] Memory aids
> - **Shapefile needs .shp + .shx + .dbf (+ .prj for CRS).**
> - **WMS = Map picture; WFS = Feature data; WCS = Coverage (raster).**
> - **Assign CRS ≠ Reproject.**
> - **PostGIS = PostgreSQL + spatial; index = GiST.**
> - **GeoServer = Java; MapServer = C, mapfile.**

## Likely Exam Questions

1. QGIS is a — **free and open-source desktop GIS**.
2. Which file stores attributes in a shapefile — **.dbf**.
3. OGC service that returns vector features — **WFS**.
4. OGC service that returns map images — **WMS**.
5. Spatial extension of PostgreSQL — **PostGIS**.
6. Language in which GeoServer is written — **Java**.
7. EPSG code of WGS-84 geographic — **4326**.
8. Tool to convert a scanned map into a geo-referenced map in QGIS — **Georeferencer**.
9. Toggle editing must be turned on to — **digitise/edit** features.

## Quick Revision Box

```
+---------------------------------------------------------------+
| QGIS: open-source desktop GIS (GDAL/OGR) | Project .qgz        |
| Shapefile = .shp .shx .dbf .prj | GeoPackage .gpkg | GeoTIFF   |
| Panels: Browser, Layers, Canvas, Processing Toolbox           |
| Edit: Toggle Editing > Add Feature > Vertex Tool > Save       |
| Snapping + Topology Checker for cadastral parcels             |
| Symbology: Single | Categorized | Graduated | Rule-based       |
| CRS: 4326 WGS84 | 3857 Web Mercator | 32643 UTM 43N            |
| Layout: Map, Legend, Scale bar, North arrow > PDF             |
| GeoServer (Java) / MapServer (C, mapfile) -> OGC services      |
| WMS image | WFS features (WFS-T edits) | WCS raster coverage  |
| PostGIS: PostgreSQL + geometry, ST_ functions, GiST index      |
+---------------------------------------------------------------+
```

*Related:* [[LandSurveyor/AGY/03_Notes/_Out_of_Syllabus/Drafts_Archive/15_Satellite_Imagery_Remote_Sensing_and_GIS]] · [[LandSurveyor/AGY/03_Notes/_Out_of_Syllabus/Drafts_Archive/17_Computer_MSOffice_and_AutoCAD]] · [[LandSurveyor/AGY/03_Notes/_Out_of_Syllabus/Drafts_Archive/19_Computer_Software_Solutions_and_Land_Records_IT]]
