# -*- coding: utf-8 -*-
"""
Script to format match-the-following and pairs questions in Paper 1 and Paper 2 as Markdown tables.
"""

import os

P1_PATH = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\AGY\08_Paper_Review\Paper1_Questions.md"
P2_PATH = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\LandSurveyor\AGY\08_Paper_Review\Paper2_Questions.md"

# Define replacements for Paper 1
# Each item is (target_substring, replacement_substring)
p1_replacements = [
    # P1-Q003
    (
"""List - I
(Place)
(a) Dhaka
(b) Machilipatnam
(c) Calicut
(d) Baroda

List - II
(Handloom Industry)
(i) Calico
(ii) Chintz
(iii) Muslin
(iv) Baftan""",
"""| List - I (Place) | List - II (Handloom Industry) |
| :--- | :--- |
| (a) Dhaka | (i) Calico |
| (b) Machilipatnam | (ii) Chintz |
| (c) Calicut | (iii) Muslin |
| (d) Baroda | (iv) Baftan |"""
    ),

    # P1-Q005
    (
"""Initiatives - Focus Regions
(a) Great Green Wall - Sahara and Sahel
(b) Climate Smart Villages - India
(c) Zai and Ngro - Equatorial Region""",
"""| Initiatives | Focus Regions |
| :--- | :--- |
| (a) Great Green Wall | Sahara and Sahel |
| (b) Climate Smart Villages | India |
| (c) Zai and Ngro | Equatorial Region |"""
    ),

    # P1-Q009
    (
"""List - I
(Earthquake Waves)
(a) P-Waves
(b) Surface Waves
(c) Harbour Waves
(d) S-Waves

List - II
(Specifications)
(i) Epicentre
(ii) Longitudinal waves
(iii) Transverse waves
(iv) Tsunami""",
"""| List - I (Earthquake Waves) | List - II (Specifications) |
| :--- | :--- |
| (a) P-Waves | (i) Epicentre |
| (b) Surface Waves | (ii) Longitudinal waves |
| (c) Harbour Waves | (iii) Transverse waves |
| (d) S-Waves | (iv) Tsunami |"""
    ),

    # P1-Q010
    (
"""Drainage System - Examples
(a) Rectangular Pattern - Shyamak Hills
(b) Dendritic Pattern - Giridih
(c) Trellis Pattern - Aravalli Hills
(d) Annular Pattern - Girnar Hills""",
"""| Drainage System | Examples |
| :--- | :--- |
| (a) Rectangular Pattern | Shyamak Hills |
| (b) Dendritic Pattern | Giridih |
| (c) Trellis Pattern | Aravalli Hills |
| (d) Annular Pattern | Girnar Hills |"""
    ),

    # P1-Q012
    (
"""List - I
(Shifting Cultivation)
(a) Jhum
(b) Koman
(c) Ponam
(d) Kumri

List - II
(States)
(i) Kerala
(ii) Odisha
(iii) Andhra Pradesh
(iv) Assam""",
"""| List - I (Shifting Cultivation) | List - II (States) |
| :--- | :--- |
| (a) Jhum | (i) Kerala |
| (b) Koman | (ii) Odisha |
| (c) Ponam | (iii) Andhra Pradesh |
| (d) Kumri | (iv) Assam |"""
    ),

    # P1-Q017
    (
"""List - I
(Provisions)
(a) Elections to Panchayats
(b) Duration of Panchayats
(c) Reservation of seats in Panchayats
(d) Audit of accounts of Panchayats

List - II
(Articles)
(i) 243J
(ii) 243D
(iii) 243E
(iv) 243K""",
"""| List - I (Provisions) | List - II (Articles) |
| :--- | :--- |
| (a) Elections to Panchayats | (i) 243J |
| (b) Duration of Panchayats | (ii) 243D |
| (c) Reservation of seats in Panchayats | (iii) 243E |
| (d) Audit of accounts of Panchayats | (iv) 243K |"""
    ),

    # P1-Q019
    (
"""List - I
(Tiers of Panchayat Raj System)
(a) Traditional councils of village elders
(b) Only one-tier system
(c) Two-tier system
(d) Three-tier system

List - II
(States)
(i) Punjab
(ii) Orissa
(iii) Sikkim
(iv) Nagaland""",
"""| List - I (Tiers of Panchayat Raj System) | List - II (States) |
| :--- | :--- |
| (a) Traditional councils of village elders | (i) Punjab |
| (b) Only one-tier system | (ii) Orissa |
| (c) Two-tier system | (iii) Sikkim |
| (d) Three-tier system | (iv) Nagaland |"""
    ),

    # P1-Q026
    (
"""List - I
(Subjects)
(a) Consolidated Fund of India
(b) Contingency Fund of India
(c) Money Bill
(d) Annual Financial Statement

List - II
(Articles)
(i) Article 110
(ii) Article 112
(iii) Article 266
(iv) Article 267""",
"""| List - I (Subjects) | List - II (Articles) |
| :--- | :--- |
| (a) Consolidated Fund of India | (i) Article 110 |
| (b) Contingency Fund of India | (ii) Article 112 |
| (c) Money Bill | (iii) Article 266 |
| (d) Annual Financial Statement | (iv) Article 267 |"""
    ),

    # P1-Q030
    (
"""List - I
(Missile by DRDO)
(a) Astra Missile
(b) Maitri Missile
(c) Nag Missile
(d) Nirbhay Missile

List - II
(Types)
(i) Subsonic Cruise Missile
(ii) Short-Range Surface to Air Missile
(iii) Anti-Tank Guided Missile
(iv) Air-to-Air Missile""",
"""| List - I (Missile by DRDO) | List - II (Types) |
| :--- | :--- |
| (a) Astra Missile | (i) Subsonic Cruise Missile |
| (b) Maitri Missile | (ii) Short-Range Surface to Air Missile |
| (c) Nag Missile | (iii) Anti-Tank Guided Missile |
| (d) Nirbhay Missile | (iv) Air-to-Air Missile |"""
    ),

    # P1-Q032
    (
"""Anticorruption Agencies - Year of Establishment
(a) CBI - 1962
(b) ED - 1956
(c) ACB - 1961
(d) CVC - 1961""",
"""| Anticorruption Agencies | Year of Establishment |
| :--- | :--- |
| (a) CBI | 1962 |
| (b) ED | 1956 |
| (c) ACB | 1961 |
| (d) CVC | 1961 |"""
    ),

    # P1-Q037
    (
"""List - I
(a) To check the speed of overspeeding vehicles
(b) To study blood flow in different parts of the body
(c) To determine the depth of sea
(d) To get images of internal organs of the human body

List - II
(i) SONAR
(ii) Ultrasound scanning
(iii) RADAR
(iv) Sonography""",
"""| List - I (Application) | List - II (Technique / Device) |
| :--- | :--- |
| (a) To check the speed of overspeeding vehicles | (i) SONAR |
| (b) To study blood flow in different parts of the body | (ii) Ultrasound scanning |
| (c) To determine the depth of sea | (iii) RADAR |
| (d) To get images of internal organs of the human body | (iv) Sonography |"""
    ),

    # P1-Q039
    (
"""List - I
(Alkaloids)
(a) Quinine
(b) Morphine
(c) Nicotine
(d) Caffeine

List - II
(Source plant)
(i) Tobacco
(ii) Cinchona bark
(iii) Coffee beans
(iv) Opium poppy""",
"""| List - I (Alkaloids) | List - II (Source plant) |
| :--- | :--- |
| (a) Quinine | (i) Tobacco |
| (b) Morphine | (ii) Cinchona bark |
| (c) Nicotine | (iii) Coffee beans |
| (d) Caffeine | (iv) Opium poppy |"""
    ),

    # P1-Q041
    (
"""List - I
(Compounds)
(a) Acetylcholine
(b) Sucralose
(c) Chloramphenicol
(d) Phenol

List - II
(Functions)
(i) Artificial sweetener
(ii) Antibiotic
(iii) Disinfectant
(iv) Neurotransmitters""",
"""| List - I (Compounds) | List - II (Functions) |
| :--- | :--- |
| (a) Acetylcholine | (i) Artificial sweetener |
| (b) Sucralose | (ii) Antibiotic |
| (c) Chloramphenicol | (iii) Disinfectant |
| (d) Phenol | (iv) Neurotransmitters |"""
    ),

    # P1-Q054
    (
"""(a) Australian open - Alexander Zverev
(b) French open - Carlos Alcaraz
(c) Wimbledon - Jannik Sinner""",
"""| Tournament | Winner |
| :--- | :--- |
| (a) Australian open | Alexander Zverev |
| (b) French open | Carlos Alcaraz |
| (c) Wimbledon | Jannik Sinner |"""
    ),

    # P1-Q061
    (
"""(a) Ramananda - Varanasi
(b) Vallabhacharya - Allahabad
(c) Chaitanya - Nadiya
(d) Ekanath - Paithan""",
"""| Saint | Place |
| :--- | :--- |
| (a) Ramananda | Varanasi |
| (b) Vallabhacharya | Allahabad |
| (c) Chaitanya | Nadiya |
| (d) Ekanath | Paithan |"""
    ),

    # P1-Q064
    (
"""(a) Allasani Peddanna - Manucharitamu
(b) Thimmana - Parijatapaharanamu
(c) Durjati - Kalahasti Shatakam
(d) Tenali Ramakrishna - Panduranga Mahathme""",
"""| Poet / Author | Work |
| :--- | :--- |
| (a) Allasani Peddanna | Manucharitamu |
| (b) Thimmana | Parijatapaharanamu |
| (c) Durjati | Kalahasti Shatakam |
| (d) Tenali Ramakrishna | Panduranga Mahathme |"""
    ),

    # P1-Q065
    (
"""List-I
(a) Rupnath Rock Edict
(b) Sahasram Rock Edict
(c) Bairat Rock Edict
(d) Maski Rock Edict

List-II
(i) Karnataka
(ii) Rajasthan
(iii) Bihar
(iv) Madhya Pradesh""",
"""| List - I (Rock Edict) | List - II (State) |
| :--- | :--- |
| (a) Rupnath Rock Edict | (i) Karnataka |
| (b) Sahasram Rock Edict | (ii) Rajasthan |
| (c) Bairat Rock Edict | (iii) Bihar |
| (d) Maski Rock Edict | (iv) Madhya Pradesh |"""
    ),

    # P1-Q069
    (
"""Important sites of Indus Civilization  Name of the Archaeologists
(a) Kot Diji – F.A. Khan
(b) Lothal – Dr. S.R. Rao
(c) Harappa – Daya Ram Sahani
(d) Mohenjo Daro – R.D. Banerji""",
"""| Important sites of Indus Civilization | Name of the Archaeologists |
| :--- | :--- |
| (a) Kot Diji | F.A. Khan |
| (b) Lothal | Dr. S.R. Rao |
| (c) Harappa | Daya Ram Sahani |
| (d) Mohenjo Daro | R.D. Banerji |"""
    ),

    # P1-Q071
    (
"""List – I
(Presidents)
(a) Vallabhbhai Patel
(b) A.C. Mazumdar
(c) Rash Behari Ghosh
(d) Badruddin Tyabji

List – II
(Sessions)
(i) Surat
(ii) Karachi
(iii) Lucknow
(iv) Madras""",
"""| List – I (Presidents) | List – II (Sessions) |
| :--- | :--- |
| (a) Vallabhbhai Patel | (i) Surat |
| (b) A.C. Mazumdar | (ii) Karachi |
| (c) Rash Behari Ghosh | (iii) Lucknow |
| (d) Badruddin Tyabji | (iv) Madras |"""
    ),

    # P1-Q080
    (
"""List – I
(a) Govinda Rao Committee
(b) Nijalingappa Committee
(c) G.K. Veeresh Committee
(d) Nanjundappa Committee

List – II
(i) Recommended for the establishment of Farmers Welfare Fund and Raita Sanjeevini Health Insurance
(ii) Recommended abolition of Malnad and Bayaluseeme Area Development Boards
(iii) Recommended compulsory water cess on farmers of common area even if they are not using water for the maintenance of canals
(iv) Recommended establishment of Regional Development Boards""",
"""| List – I (Committees) | List – II (Recommendations) |
| :--- | :--- |
| (a) Govinda Rao Committee | (i) Recommended for the establishment of Farmers Welfare Fund and Raita Sanjeevini Health Insurance |
| (b) Nijalingappa Committee | (ii) Recommended abolition of Malnad and Bayaluseeme Area Development Boards |
| (c) G.K. Veeresh Committee | (iii) Recommended compulsory water cess on farmers of common area even if they are not using water for the maintenance of canals |
| (d) Nanjundappa Committee | (iv) Recommended establishment of Regional Development Boards |"""
    ),

    # P1-Q089
    (
"""List – I
(Boards)
(a) Coconut Development Board
(b) National Horticulture Board
(c) National Turmeric Board
(d) Tobacco Board

List – II
(Places)
(i) Gurgaon, Haryana
(ii) Kochi, Kerala
(iii) Guntur, Andhra Pradesh
(iv) Nizamabad, Telangana""",
"""| List – I (Boards) | List – II (Places) |
| :--- | :--- |
| (a) Coconut Development Board | (i) Gurgaon, Haryana |
| (b) National Horticulture Board | (ii) Kochi, Kerala |
| (c) National Turmeric Board | (iii) Guntur, Andhra Pradesh |
| (d) Tobacco Board | (iv) Nizamabad, Telangana |"""
    ),

    # P1-Q095
    (
"""Thermal Plant  Located District
(a) Annechakanahalli – Hassan
(b) Kalkunike – Ballari
(c) Hanakona – Uttara Kannada""",
"""| Thermal Plant | Located District |
| :--- | :--- |
| (a) Annechakanahalli | Hassan |
| (b) Kalkunike | Ballari |
| (c) Hanakona | Uttara Kannada |"""
    )
]

# Define replacements for Paper 2
p2_replacements = [
    # P2-Q003
    (
"""List-I
(Physical Quantity)
(a) Electric charge
(b) Electric current
(c) Resistivity
(d) Power

List-II
(SI Unit)
(i) Ohm-meter (Ω-m)
(ii) Watt (W)
(iii) Coulomb (C)
(iv) Ampere (A)""",
"""| List-I (Physical Quantity) | List-II (SI Unit) |
| :--- | :--- |
| (a) Electric charge | (i) Ohm-meter (Ω-m) |
| (b) Electric current | (ii) Watt (W) |
| (c) Resistivity | (iii) Coulomb (C) |
| (d) Power | (iv) Ampere (A) |"""
    ),

    # P2-Q005
    (
"""List-I
(Radiation)
(a) Ultraviolet radiation
(b) X-rays
(c) Infrared radiation
(d) Gamma radiation

List-II
(Wavelength Range (in Å))
(i) 0.01 Å to 1 Å
(ii) 7000 Å to 20000 Å
(iii) 1000 Å to 4000 Å
(iv) 1 Å to 100 Å""",
"""| List-I (Radiation) | List-II (Wavelength Range (in Å)) |
| :--- | :--- |
| (a) Ultraviolet radiation | (i) 0.01 Å to 1 Å |
| (b) X-rays | (ii) 7000 Å to 20000 Å |
| (c) Infrared radiation | (iii) 1000 Å to 4000 Å |
| (d) Gamma radiation | (iv) 1 Å to 100 Å |"""
    ),

    # P2-Q012
    (
"""List - I
(a) Exposure station
(b) Flightline
(c) Perspective centre
(d) Plumbline

List - II
(i) The flying path an aircraft takes while taking the photographs
(ii) It is a vertical line from exposure station indicating the direction of gravity
(iii) Location of aircraft in the air at the time of taking photograph
(iv) The point of origin or termination of bundles of perspective light rays""",
"""| List - I (Concepts) | List - II (Explanations) |
| :--- | :--- |
| (a) Exposure station | (i) The flying path an aircraft takes while taking the photographs |
| (b) Flightline | (ii) It is a vertical line from exposure station indicating the direction of gravity |
| (c) Perspective centre | (iii) Location of aircraft in the air at the time of taking photograph |
| (d) Plumbline | (iv) The point of origin or termination of bundles of perspective light rays |"""
    ),

    # P2-Q026
    (
"""List - I
(a) HDoP
(b) PDoP
(c) Low DoP
(d) High DoP

List - II
(i) Better satellite geometry
(ii) Poor satellite geometry
(iii) Accuracy of horizontal position
(iv) Position accuracy in 3-dimension""",
"""| List - I (Dilution of Precision) | List - II (Satellite Geometry) |
| :--- | :--- |
| (a) HDoP | (i) Better satellite geometry |
| (b) PDoP | (ii) Poor satellite geometry |
| (c) Low DoP | (iii) Accuracy of horizontal position |
| (d) High DoP | (iv) Position accuracy in 3-dimension |"""
    ),

    # P2-Q029
    (
"""List - I
(a) Base station
(b) Rover receiver
(c) Data link
(d) Multipath error

List - II
(i) Receives correction data and determines the rover position
(ii) Transmits corrections from the base station to the rover
(iii) A signal distortion that happens when satellite waves bounce off nearby surfaces
(iv) GNSS receiver established over a known coordinate point.""",
"""| List - I (RTK Surveying Component) | List - II (Description) |
| :--- | :--- |
| (a) Base station | (i) Receives correction data and determines the rover position |
| (b) Rover receiver | (ii) Transmits corrections from the base station to the rover |
| (c) Data link | (iii) A signal distortion that happens when satellite waves bounce off nearby surfaces |
| (d) Multipath error | (iv) GNSS receiver established over a known coordinate point. |"""
    ),

    # P2-Q035
    (
"""List - I
(Types of map)
(a) Physical map
(b) Political map
(c) Topographic map
(d) Thematic map

List - II
(Uses)
(i) Shows political boundaries
(ii) Focuses on specific theme
(iii) Depicts physical features
(iv) Uses contour lines to illustrate the elevation and shape of the land.""",
"""| List - I (Types of map) | List - II (Uses) |
| :--- | :--- |
| (a) Physical map | (i) Shows political boundaries |
| (b) Political map | (ii) Focuses on specific theme |
| (c) Topographic map | (iii) Depicts physical features |
| (d) Thematic map | (iv) Uses contour lines to illustrate the elevation and shape of the land. |"""
    ),

    # P2-Q036
    (
"""List - I
(Discontinuity)
(a) Conrad
(b) Mohorovicic
(c) Gutenberg
(d) Lehman

List - II
(Separate layers)
(i) Sial and Sima
(ii) Outer core and inner core
(iii) Crust and mantle Zone
(iv) Mantle zone and core""",
"""| List - I (Discontinuity) | List - II (Separate layers) |
| :--- | :--- |
| (a) Conrad | (i) Sial and Sima |
| (b) Mohorovicic | (ii) Outer core and inner core |
| (c) Gutenberg | (iii) Crust and mantle Zone |
| (d) Lehman | (iv) Mantle zone and core |"""
    ),

    # P2-Q043
    (
"""List - I
(a) Vector line operations (eg: buffering)
(b) Raster grid/pixel processing
(c) Vector to raster conversion
(d) Overlay analysis (composite mapping)

List - II
(i) Best suited for continuous surface backgrounds
(ii) Ideal for rendering precise land boundaries and transit networks with clean text labels
(iii) Combines multiple administrative and land cover layers to calculate cartographic overlap
(iv) Converting crisp outline geometries into pixel grids often causing jagged edges or loss in line resolution""",
"""| List - I (Plugins) | List - II (Cartographic Application) |
| :--- | :--- |
| (a) Vector line operations (eg: buffering) | (i) Best suited for continuous surface backgrounds |
| (b) Raster grid/pixel processing | (ii) Ideal for rendering precise land boundaries and transit networks with clean text labels |
| (c) Vector to raster conversion | (iii) Combines multiple administrative and land cover layers to calculate cartographic overlap |
| (d) Overlay analysis (composite mapping) | (iv) Converting crisp outline geometries into pixel grids often causing jagged edges or loss in line resolution |"""
    ),

    # P2-Q044
    (
"""List-I
(a) WMS
(b) WFS
(c) WCS
(d) Get capabilities
(e) Get Feature

List-II
(i) Returns a raw multidimensional raster data suitable for analysis
(ii) Core operation used to fetch the actual spatial features with geometric attributes
(iii) Returns styled map images (PNG, JPEG)
(iv) Standard operation across all services
(v) Returns raw vector features""",
"""| List - I (OGC Web Services) | List - II (Descriptions) |
| :--- | :--- |
| (a) WMS | (i) Returns a raw multidimensional raster data suitable for analysis |
| (b) WFS | (ii) Core operation used to fetch the actual spatial features with geometric attributes |
| (c) WCS | (iii) Returns styled map images (PNG, JPEG) |
| (d) Get capabilities | (iv) Standard operation across all services |
| (e) Get Feature | (v) Returns raw vector features |"""
    ),

    # P2-Q048
    (
"""List-I
(a) F6
(b) F7
(c) F8
(d) F9

List-II
(i) Toggles the SNAP on and off
(ii) Toggles ORTHO on and off
(iii) Toggles GRID on and off
(iv) Toggles the co-ordinate readout from absolute to incremental to off and back""",
"""| List - I (Function Keys) | List - II (Functions in AutoCAD) |
| :--- | :--- |
| (a) F6 | (i) Toggles the SNAP on and off |
| (b) F7 | (ii) Toggles ORTHO on and off |
| (c) F8 | (iii) Toggles GRID on and off |
| (d) F9 | (iv) Toggles the co-ordinate readout from absolute to incremental to off and back |"""
    ),

    # P2-Q065
    (
"""List – I
(a) Opposite sides of a parallelogram
(b) The diagonals of a parallelogram
(c) In parallelogram, consecutive angles are

List – II
(i) Supplementary angle
(ii) Equal
(iii) Parallelogram
(iv) Bisect each other""",
"""| List – I | List – II |
| :--- | :--- |
| (a) Opposite sides of a parallelogram | (i) Supplementary angle |
| (b) The diagonals of a parallelogram | (ii) Equal |
| (c) In parallelogram, consecutive angles are | (iii) Parallelogram |
| | (iv) Bisect each other |"""
    ),

    # P2-Q067
    (
"""List – I
(Polygons)
(a) Decagon
(b) Hexagon
(c) Octagon
(d) Pentagon

List – II
(Number of sides)
(i) 8
(ii) 5
(iii) 10
(iv) 6""",
"""| List – I (Polygons) | List – II (Number of sides) |
| :--- | :--- |
| (a) Decagon | (i) 8 |
| (b) Hexagon | (ii) 5 |
| (c) Octagon | (iii) 10 |
| (d) Pentagon | (iv) 6 |"""
    ),

    # P2-Q070
    (
"""List-I
(a) { 1, 2, 3, 6, 9, 18 }
(b) { 1, 2, 3, 6 }
(c) { 4, – 4 }
(d) { 1, 3, 5, 7, 9 }

List-II
(i) { x : x is an integer and $x^2 - 16 = 0$ }
(ii) { x : x is an odd natural number less than 10 }
(iii) { x : x is a natural number and divisor of 6 }
(iv) { x : x is a positive integer and a divisor of 18 }""",
"""| List - I (Roster Form) | List - II (Set Builder Form) |
| :--- | :--- |
| (a) { 1, 2, 3, 6, 9, 18 } | (i) { x : x is an integer and $x^2 - 16 = 0$ } |
| (b) { 1, 2, 3, 6 } | (ii) { x : x is an odd natural number less than 10 } |
| (c) { 4, – 4 } | (iii) { x : x is a natural number and divisor of 6 } |
| (d) { 1, 3, 5, 7, 9 } | (iv) { x : x is a positive integer and a divisor of 18 } |"""
    ),

    # P2-Q081
    (
"""List-I
(a) Identity matrix
(b) Diagonal matrix
(c) Column matrix
(d) Row matrix

List-II
(i) [a 0 a]
(ii) $\\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}$
(iii) $\\begin{bmatrix} a & 0 \\\\ 0 & b \\end{bmatrix}$
(iv) $\\begin{bmatrix} a \\\\ b \\end{bmatrix}$""",
"""| List - I (Matrix Name) | List - II (Example) |
| :--- | :--- |
| (a) Identity matrix | (i) [a 0 a] |
| (b) Diagonal matrix | (ii) $\\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}$ |
| (c) Column matrix | (iii) $\\begin{bmatrix} a & 0 \\\\ 0 & b \\end{bmatrix}$ |
| (d) Row matrix | (iv) $\\begin{bmatrix} a \\\\ b \\end{bmatrix}$ |"""
    ),

    # P2-Q083
    (
"""List-I
(a) $\\sqrt[3]{2744}$
(b) $\\left(\\frac{2}{3}\\right)^3 \\sqrt{729}$
(c) $\\sqrt{18^2 + 24^2}$
(d) $\\sqrt{\\sqrt[3]{4096}}$

List-II
(i) 8
(ii) 30
(iii) 4
(iv) 14""",
"""| List - I (Expression) | List - II (Value) |
| :--- | :--- |
| (a) $\\sqrt[3]{2744}$ | (i) 8 |
| (b) $\\left(\\frac{2}{3}\\right)^3 \\sqrt{729}$ | (ii) 30 |
| (c) $\\sqrt{18^2 + 24^2}$ | (iii) 4 |
| (d) $\\sqrt{\\sqrt[3]{4096}}$ | (iv) 14 |"""
    ),

    # P2-Q091
    (
"""List-I
(a) (x – 3y) (x + 5y)
(b) (x + 3y) (x + 5y)
(c) (x – 3y) (x – 5y)
(d) (x + 3y) (x – 5y)

List-II
(i) $x^2 - 8xy + 15y^2$
(ii) $x^2 - 2xy - 15y^2$
(iii) $x^2 + 8xy + 15y^2$
(iv) $x^2 + 2xy - 15y^2$""",
"""| List - I (Algebraic Expression) | List - II (Simplified Form) |
| :--- | :--- |
| (a) (x – 3y) (x + 5y) | (i) $x^2 - 8xy + 15y^2$ |
| (b) (x + 3y) (x + 5y) | (ii) $x^2 - 2xy - 15y^2$ |
| (c) (x – 3y) (x – 5y) | (iii) $x^2 + 8xy + 15y^2$ |
| (d) (x + 3y) (x – 5y) | (iv) $x^2 + 2xy - 15y^2$ |"""
    )
]

def test_replacements(path, replacements, name):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    missing = []
    for idx, (target, repl) in enumerate(replacements):
        if target not in content:
            missing.append((idx, target[:40].replace('\n', ' ')))
    
    if missing:
        print(f"FAILED {name}: {len(missing)} targets not found:")
        for idx, m in missing:
            print(f"  Item {idx}: {m}")
        return False
    else:
        print(f"SUCCESS {name}: All {len(replacements)} targets found uniquely!")
        return True

if __name__ == '__main__':
    t1 = test_replacements(P1_PATH, p1_replacements, "Paper 1")
    t2 = test_replacements(P2_PATH, p2_replacements, "Paper 2")
    if t1 and t2:
        print("\nAll replacements verified! Applying changes...")
        with open(P1_PATH, 'r', encoding='utf-8') as f:
            c1 = f.read()
        for target, repl in p1_replacements:
            c1 = c1.replace(target, repl, 1)
        with open(P1_PATH, 'w', encoding='utf-8') as f:
            f.write(c1)
        print("Paper 1 updated.")

        with open(P2_PATH, 'r', encoding='utf-8') as f:
            c2 = f.read()
        for target, repl in p2_replacements:
            c2 = c2.replace(target, repl, 1)
        with open(P2_PATH, 'w', encoding='utf-8') as f:
            f.write(c2)
        print("Paper 2 updated.")
