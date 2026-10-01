---
exam: KEA Land Surveyor 2026
subject: Paper-II Modern Methods of Surveying (B) — Advanced Positioning & Satellite Communication
topic: NAVSTAR GPS, signal structure, errors, DOP, DGPS, RTK, CORS, NTRIP, constellations, software
priority: Tier 1 (part of 20 marks)
tags: [land-surveyor, paper-2, gps, gnss, dgps, rtk, cors, ntrip, dop]
---

# 16. GNSS — GPS, DGPS, RTK, CORS & Constellations

> [!IMPORTANT] Exam focus
> Notified items: **NAVSTAR GPS architecture, signal structure, trilateration, errors and corrections; DGPS (base + rover, real-time and post-processed, accuracy); RTK, CORS, Karnataka State CORS network, NTRIP, field data collection, cadastral precision; constellations (GPS, GLONASS, Galileo, NavIC), frequencies, satellite geometry and DOP; processing software and GIS integration.**
> Your note [[08_GPS_GIS_and_Remote_Sensing]] has the basic segments and DGPS vs RTK table. This note adds signals, errors, DOP, CORS/NTRIP.

---

## 1. NAVSTAR GPS architecture

**GNSS** (Global Navigation Satellite System) is the general term; **GPS (NAVSTAR)** is the US system operated by the US Space Force.

| Segment | Content |
| :--- | :--- |
| **Space** | 24+ operational satellites in **6 orbital planes**, inclination **55°**, altitude about **20,200 km** (medium Earth orbit), period about 12 sidereal hours; at least 4 visible from anywhere |
| **Control** | Master Control Station (Colorado), monitor stations, ground antennas; track satellites, upload orbit and clock data |
| **User** | receivers (handheld, geodetic, RTK rovers) |

- Each satellite carries very accurate **atomic clocks** (rubidium/caesium).
- Reference frame: **WGS-84** (ellipsoidal height; convert to orthometric/MSL height using a geoid model).

## 2. Signal structure

| Item | Value |
| :--- | :--- |
| Fundamental frequency | 10.23 MHz |
| **L1** | 1575.42 MHz (154 × 10.23) |
| **L2** | 1227.60 MHz (120 × 10.23) |
| **L5** | 1176.45 MHz (safety-of-life, modern signal) |
| **C/A code** | 1.023 MHz, civil, repeats every 1 ms, on L1 |
| **P(Y) code** | 10.23 MHz, military (encrypted), on L1 and L2 |
| **Navigation message** | 50 bps, carries satellite orbit (ephemeris), almanac, clock corrections, health; full frame 12.5 min |

- Signals are **Code Division Multiple Access (CDMA)**: every satellite uses a unique pseudo-random code (PRN) on the same frequency. (GLONASS historically used FDMA.)
- **Two measurements:** *pseudorange* from the code (metre-level) and *carrier phase* from the wave itself (mm–cm level, used for survey-grade work).
- Dual-frequency receivers (L1+L2) **remove ionospheric error**.

## 3. Trilateration principle

- Receiver measures signal travel time $\Delta t$ to each satellite: distance $=c\,\Delta t$ (pseudorange).
- One satellite puts you on a sphere; two on a circle; three on two points (one is discarded).
- **Four satellites are needed for a 3D fix** because the receiver's own clock is inexpensive and wrong: unknowns are $X,Y,Z$ and the **clock bias** → 4 equations.
- Note: *trilateration* uses **distances**; *triangulation* uses **angles**.

## 4. Errors and corrections

| Error | Cause | Correction / reduction |
| :--- | :--- | :--- |
| Satellite clock | small clock drift | corrections in nav message; differential methods |
| Orbit (ephemeris) | satellite position uncertainty | precise ephemeris (post-processing), differential |
| **Ionospheric delay** | free electrons, 50–1000 km altitude; the biggest atmospheric error | dual-frequency; models; differential |
| **Tropospheric delay** | water vapour and dry gases below ~50 km | models; differential |
| **Multipath** | signal reflected from buildings, water, metal | choke-ring antennas, avoid reflective sites, longer observation |
| Receiver noise / clock | electronics | better receiver, more satellites |
| Cycle slips / ambiguity | loss of carrier tracking | ambiguity resolution in RTK/static |
| Geometry (DOP) | poor satellite spread | observe when DOP is low |
| Selective Availability (SA) | intentional degradation, **switched off in May 2000** | no longer applies |

## 5. Satellite geometry and DOP

**Dilution of Precision (DOP)** measures how satellite geometry magnifies range errors: position error $\approx$ DOP $\times$ range error. **Lower DOP is better.**

| Term | Meaning |
| :--- | :--- |
| GDOP | geometric (3D position + time) |
| **PDOP** | position (3D) |
| HDOP | horizontal |
| VDOP | vertical |
| TDOP | time |

| PDOP | Quality |
| :--- | :--- |
| 1–2 | excellent |
| 2–5 | good |
| 5–10 | moderate |
| > 10 | poor |

Survey practice: keep **PDOP below about 3–4** (many specs say < 6 maximum). Best geometry: one satellite overhead and others spread evenly low on the horizon; worst: satellites clustered together. Use an elevation mask of about 10–15° to avoid low-angle noisy signals. Vertical accuracy is usually worse than horizontal.

## 6. DGPS (Differential GPS)

- **Concept:** errors at two nearby receivers are nearly the same. A **base station** on a point of **known coordinates** computes the error for each satellite and provides **corrections**; the **rover** applies them.
- **Configuration:** one base + one or more rovers, base–rover distance typically within about 10–50 km for good results (accuracy degrades with baseline length).
- **Real-time DGPS:** corrections sent instantly by radio, GSM/internet, or satellite (SBAS such as India's **GAGAN**; WAAS in USA). **Post-processed DGPS:** raw data from base and rover are stored and combined later in software.
- **Accuracy levels (typical):**

| Method | Horizontal accuracy |
| :--- | :--- |
| Standalone GPS (civil) | about 3–5 m (up to 10 m) |
| Code-based DGPS | about 0.5–1 m |
| SBAS (GAGAN) | about 1.5–3 m |
| RTK (carrier phase) | about 1–2 cm (+1 ppm) |
| Static / post-processed carrier phase | mm to cm |

## 7. GNSS rovers, RTK and CORS

**RTK (Real Time Kinematic):** uses **carrier-phase** measurements with corrections sent in real time; the software resolves the integer **ambiguity** — result is a **Fixed** solution (cm accuracy) or **Float** (decimetre level, not acceptable for cadastral work).

**CORS (Continuously Operating Reference Station) network:**
- Permanent GNSS base stations that record and transmit data 24×7 from fixed, accurately known monuments.
- **Network RTK** models errors across the network (techniques like VRS, FKP), so a single rover in the coverage area gets cm-level positions **without setting up its own base**.
- Data is streamed over the internet using **NTRIP** (**Networked Transport of RTCM via Internet Protocol**), an application protocol for streaming RTCM correction data; a rover connects to a **caster** using a mount-point, username and password (via a mobile SIM).
- **RTCM** = standard correction message format; **RINEX** = standard file format for storing raw observations for post-processing.
- **Karnataka State CORS network:** a state network of permanent reference stations set up for the Survey Settlement and Land Records department to support **RTK-based cadastral survey, village/abadi and re-survey work** with a common, accurate reference. (Station numbers and details are on the department's site; the exam usually tests the concept.)
- **Benefits for cadastral surveys:** one uniform coordinate framework across the state; fast, cm-level, parcel-corner fixing; fewer control points; reduces boundary disputes; digital records integrate with Bhoomi/Mojini.

**Field data collection with a GNSS rover**
1. Set up pole with antenna, level the bubble, measure antenna height.
2. Connect to CORS/base via NTRIP; wait for a **Fixed** solution.
3. Choose coordinate system/datum (WGS-84 or UTM/local), check PDOP and number of satellites.
4. Occupy each parcel corner for a few seconds/epochs; record point ID, attributes, photo; repeat a control point for QC.
5. Export to CSV/DXF/shapefile; import to GIS/AutoCAD.

## 8. Constellations and satellite communication

| System | Country/Agency | Satellites / orbit | Note |
| :--- | :--- | :--- | :--- |
| **GPS** | USA | 24+; MEO 20,200 km | global |
| **GLONASS** | Russia | 24; MEO 19,100 km | global, higher inclination (good at high latitudes) |
| **Galileo** | European Union | 24+ ; MEO 23,222 km | civil-controlled; high accuracy |
| **BeiDou** | China | 35+ ; MEO + GEO + IGSO | global |
| **NavIC (IRNSS)** | India (ISRO) | **7 satellites** (3 GEO + 4 IGSO); regional | covers India and up to about 1,500 km around; L5 and S band; "Navigation with Indian Constellation" |
| QZSS | Japan | regional | augments GPS |

- **Multi-GNSS receivers** track several systems → more satellites, better DOP, faster fixes.
- **SBAS:** GAGAN (India), WAAS (USA), EGNOS (Europe), MSAS (Japan) — geostationary satellites broadcasting corrections.
- **Satellite communication** links CORS to users (internet/GSM, VSAT, radio modems UHF) and carries corrections; RTCM 3.x messages are the standard.

## 9. Related software

- **GNSS data processing:** Trimble Business Center, Leica Infinity, Spectra Survey Office, RTKLIB (open source), Emlid Studio, TEQC (RINEX quality check); **post-processing** and **network adjustment (least squares)** tools produce final adjusted coordinates.
- **Integration with GIS:** coordinates exported to shapefile, GeoPackage, KML; used in QGIS/ArcGIS for parcel mapping; field apps (QField, Survey123, Collector, Bhoomi/Mojini/Dishank apps) collect geotagged features.

---

## High-Yield Mnemonics

> [!NOTE] Memory aids
> - **"20,200 – 55 – 6 – 24":** altitude km, inclination degrees, planes, satellites.
> - **L1 = 1575.42, L2 = 1227.60, L5 = 1176.45** (MHz).
> - **Four satellites: X, Y, Z + clock.**
> - **Lower DOP = better.** PDOP < 3 good.
> - **CORS + NTRIP + RTK = cm accuracy without your own base.**
> - **NavIC = 7 satellites, regional (India + 1,500 km).**

## Likely Exam Questions

1. Minimum satellites for a 3D position — **4**.
2. GPS orbital altitude — **about 20,200 km**; number of orbital planes — **6**.
3. Error removed by dual-frequency receivers — **ionospheric**.
4. Full form of NTRIP — **Networked Transport of RTCM via Internet Protocol**.
5. Full form of CORS — **Continuously Operating Reference Station**.
6. Typical RTK accuracy — **1–2 cm**.
7. Selective Availability was turned off in — **2000**.
8. India's regional navigation system — **NavIC (IRNSS)**, 7 satellites.
9. DOP whose value is best when the sky view is wide — **PDOP** (lower = better).

## Quick Revision Box

```
+---------------------------------------------------------------+
| GPS: 24+ sats, 6 planes, 55 deg, 20,200 km, WGS-84            |
| Segments: Space, Control, User | Atomic clocks                |
| L1 1575.42 | L2 1227.60 | L5 1176.45 MHz | C/A 1.023 | P 10.23  |
| 4 satellites -> X,Y,Z + clock bias | Trilateration = distances |
| Errors: clock, orbit, IONOSPHERE (largest), troposphere,       |
|         multipath, noise | SA off May 2000                    |
| DOP: G, P, H, V, T | lower better | PDOP<3 good               |
| DGPS: base at known point sends corrections | 0.5-1 m          |
| RTK: carrier phase, Fixed solution | 1-2 cm                    |
| CORS network + NTRIP (RTCM over internet) | RINEX = raw file   |
| GNSS: GPS, GLONASS, Galileo, BeiDou | NavIC 7 sats (regional)  |
+---------------------------------------------------------------+
```

*Related:* [[08_GPS_GIS_and_Remote_Sensing]] · [[LandSurveyor/AGY/03_Notes/_Out_of_Syllabus/Drafts_Archive/14_Photogrammetry_Aerial_and_Drone_Survey]] · [[07_Total_Station_and_EDM]] · [[10_Karnataka_Land_Records_Bhoomi_Mojini_Dishank]]
