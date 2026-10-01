---
exam: KEA Land Surveyor 2026
subject: Paper-II Mathematics (A) — Geometry & Mensuration
topic: Axioms, lines, triangles, congruence, polygons, quadrilaterals, theorems, circles, similarity, Pythagoras, solids
priority: Tier 1 (part of 40 marks Mathematics)
tags: [land-surveyor, paper-2, mathematics, geometry, mensuration]
---

# 13. Maths — Geometry & Mensuration

> [!IMPORTANT] Exam focus
> Geometry is the largest block of the Mathematics syllabus (16 sub-topics). Questions are usually "state the theorem / find the angle or length / find area or volume". Learn the property lists and the formula tables.

---

## 1. Axioms and postulates (Euclid)

**Axioms (common notions)**
1. Things equal to the same thing are equal to one another.
2. If equals are added to equals, the wholes are equal.
3. If equals are subtracted from equals, the remainders are equal.
4. Things which coincide with one another are equal to one another.
5. The whole is greater than the part.
6. Things which are double of the same thing are equal to one another.
7. Things which are halves of the same thing are equal to one another.

**Postulates**
1. A straight line may be drawn from any point to any other point.
2. A terminated line can be produced indefinitely.
3. A circle can be drawn with any centre and any radius.
4. All right angles are equal to one another.
5. If a straight line falling on two straight lines makes the interior angles on one side together less than two right angles, the two lines meet on that side when produced.

> [!NOTE] Numbering
> The notification says "axioms 1–6 and postulates 1–6". Textbooks number these differently (some add Playfair's axiom, an equivalent of the fifth postulate: *through a point not on a line, exactly one line parallel to the given line*). Memorise the statements above; do not rely on the number.

**Definitions:** point (no part), line (breadthless length), ray (starts at a point, extends one way), line segment (two end points), collinear points (on one line), plane. **Theorem:** a statement proved logically; **converse:** swap hypothesis and conclusion (may not be true); **corollary:** result following directly from a theorem; **rider:** an application problem based on a theorem.

---

## 2. Lines and angles

- **Linear pair:** two adjacent angles on a straight line sum to $180^\circ$.
- **Vertically opposite angles** are equal.
- Angles at a point sum to $360^\circ$.
- **Transversal cutting two parallel lines:**
  - corresponding angles equal;
  - alternate interior angles equal;
  - interior angles on the same side (co-interior) sum to $180^\circ$.
  - The **converse** also holds (equal alternate angles ⇒ lines parallel).
- Lines parallel to the same line are parallel to each other.
- Angle sum of a triangle $=180^\circ$; exterior angle $=$ sum of the two opposite interior angles.

---

## 3. Triangles

| Classification | Types |
| :--- | :--- |
| By sides | equilateral (3 equal), isosceles (2 equal), scalene (none) |
| By angles | acute, right, obtuse |

- Isosceles: angles opposite equal sides are equal (and converse).
- Any two sides sum to more than the third; the greater side is opposite the greater angle.
- **Congruence** (identical shape and size; corresponding parts are equal — **CPCT**):

| Rule | Meaning |
| :--- | :--- |
| SAS | two sides and the included angle |
| SSS | three sides |
| ASA / AAS | two angles and a side |
| RHS | right angle, hypotenuse, one side |

(AAA is *not* a congruence rule; it gives similarity.)

**Special points (concurrent lines)**

| Lines | Meet at | Facts |
| :--- | :--- | :--- |
| Medians | **Centroid** G | divides each median $2:1$ from the vertex; always inside |
| Perpendicular bisectors of sides | **Circumcentre** | centre of the circumcircle; equidistant from vertices |
| Angle bisectors | **Incentre** | centre of the inscribed circle (incircle); equidistant from sides |
| Altitudes | **Orthocentre** | inside for acute, on the right-angle vertex for right, outside for obtuse |

- In an equilateral triangle all four points coincide.
- Circumcentre of a right triangle is the mid-point of the hypotenuse.
- **Constructions (steps to remember):** SSS triangle — draw base, arcs from both ends; perpendicular bisector — arcs of equal radius above and below from both ends; angle bisector — arc cuts both arms, two equal arcs from those points intersect; equilateral triangle — arcs of equal radius from both ends of a side; altitude — perpendicular from a vertex to the opposite side.

---

## 4. Polygons

| Item | Formula |
| :--- | :--- |
| Sum of interior angles | $(n-2)\times180^\circ$ |
| Sum of exterior angles | $360^\circ$ |
| Each interior angle (regular) | $\dfrac{(n-2)\times180^\circ}{n}$ |
| Each exterior angle (regular) | $\dfrac{360^\circ}n$ |
| Number of diagonals | $\dfrac{n(n-3)}2$ |

- Regular polygon: all sides and angles equal (regular pentagon interior $108^\circ$, hexagon $120^\circ$, octagon $135^\circ$). Irregular: otherwise. Convex: every interior angle $<180^\circ$.
- **Inscribing regular polygons in a circle:** hexagon — step off the radius around the circle (side $=r$); pentagon and octagon — divide $360^\circ$ into 5 or 8 equal central angles ($72^\circ$, $45^\circ$).
- **Well-conditioned figure (survey usage):** a shape whose angles are not too sharp, so that plotting and computation errors stay small. For a triangle, keep each angle between about $30^\circ$ and $120^\circ$ (the equilateral triangle is ideal). Polygons close to regular and convex are well conditioned; long thin slivers are ill-conditioned.

---

## 5. Quadrilaterals

Angle sum $=360^\circ$. Ten elements of a quadrilateral: 4 sides, 4 angles, 2 diagonals (a quadrilateral is constructed from 5 independent measurements).

| Figure | Key properties | Area |
| :--- | :--- | :--- |
| **Parallelogram** | opposite sides parallel and equal; opposite angles equal; diagonals bisect each other; consecutive angles supplementary | $b\times h$ |
| **Rectangle** | parallelogram with all angles $90^\circ$; diagonals equal | $l\times b$ |
| **Rhombus** | parallelogram with all sides equal; diagonals bisect at right angles | $\tfrac12d_1d_2$ |
| **Square** | equal sides and $90^\circ$ angles; diagonals equal and perpendicular | $a^2$ (diagonal $a\sqrt2$) |
| **Trapezium** | one pair of parallel sides | $\tfrac12(a+b)h$ |
| **Kite** | two pairs of adjacent equal sides; diagonals perpendicular | $\tfrac12d_1d_2$ |

- **Any quadrilateral:** $\text{Area}=\tfrac12\times d\times(h_1+h_2)$, where $d$ is a diagonal and $h_1,h_2$ are perpendiculars to it from the opposite vertices.
- Triangle area: $\tfrac12bh$; equilateral $\dfrac{\sqrt3}4a^2$; **Heron:** $\sqrt{s(s-a)(s-b)(s-c)}$, $s=\dfrac{a+b+c}2$.
- Cyclic quadrilateral (Brahmagupta): $\sqrt{(s-a)(s-b)(s-c)(s-d)}$.

**Parallelogram theorems and corollaries**
- A quadrilateral is a parallelogram if: both pairs of opposite sides are equal; **or** both pairs of opposite angles are equal; **or** diagonals bisect each other; **or** one pair of opposite sides is equal *and* parallel.
- Corollary: a diagonal divides a parallelogram into two congruent triangles. A rectangle's diagonals are equal; a rhombus's diagonals are perpendicular.

**Mid-point theorem:** the line joining the mid-points of two sides of a triangle is **parallel to the third side and half of it**. *Converse:* a line through the mid-point of one side, parallel to another side, bisects the third side. Quadrilateral formed by joining mid-points of the sides of any quadrilateral is a parallelogram.

---

## 6. Areas (theorems)

- Parallelograms on the **same base and between the same parallels** are equal in area.
- Triangles on the same base and between the same parallels are equal in area.
- Area of a triangle = **half** the area of a parallelogram on the same base and between the same parallels.
- Triangles with equal bases and equal heights have equal area; a median divides a triangle into two triangles of equal area.

---

## 7. Cyclic quadrilaterals

A quadrilateral whose four vertices lie on a circle.
- **Opposite angles are supplementary** ($\angle A+\angle C=180^\circ$). Converse also true.
- Exterior angle = interior opposite angle.
- Ptolemy: product of diagonals = sum of products of opposite sides.
- A cyclic parallelogram is a rectangle; a cyclic trapezium is isosceles.

---

## 8. Circles

| Property | Statement |
| :--- | :--- |
| Chord | perpendicular from the centre bisects the chord; equal chords are equidistant from the centre (and converse) |
| Distance of chord from centre | $d=\sqrt{r^2-(c/2)^2}$, $c$ = chord length |
| Central vs inscribed angle | angle at the centre $=2\times$ angle at the circumference on the same arc |
| Same segment | angles in the same segment are equal |
| Semicircle | angle in a semicircle $=90^\circ$ |
| Equal arcs | subtend equal angles at the centre |
| Circumference / area | $2\pi r$ ; $\pi r^2$ |
| Arc / sector | arc $=\dfrac\theta{360}2\pi r$ ; sector $=\dfrac\theta{360}\pi r^2$ |

- **Concentric circles:** same centre. **Congruent circles:** equal radii. Segment: region between a chord and its arc.
- **Secant** cuts the circle at two points; **tangent** touches at one point.

**Tangents**
- Tangent is **perpendicular to the radius** at the point of contact.
- Tangents from an external point are **equal in length**; they subtend equal angles at the centre; the line from the point to the centre bisects the angle between them.
- Length of tangent from a point at distance $d$ from the centre: $\sqrt{d^2-r^2}$.
- Secant–tangent: $PT^2=PA\cdot PB$. Intersecting chords: $PA\cdot PB=PC\cdot PD$.
- **Two circles** (radii $R>r$, centres $d$ apart):

| Position | Condition | Common tangents |
| :--- | :--- | :--- |
| Separate | $d>R+r$ | 4 (2 direct, 2 transverse) |
| Touch externally | $d=R+r$ | 3 |
| Intersect | $R-r<d<R+r$ | 2 |
| Touch internally | $d=R-r$ | 1 |
| One inside the other | $d<R-r$ | 0 |

- Direct common tangent length $=\sqrt{d^2-(R-r)^2}$; transverse $=\sqrt{d^2-(R+r)^2}$.
- Constructions: tangent at a point — draw radius, then perpendicular at that point; tangent from an external point — draw a semicircle on (centre–point) as diameter, its intersection with the circle gives the points of contact.

---

## 9. Similarity and the Pythagoras theorem

- Similar figures: same shape, proportional sides, equal angles.
- **Basic Proportionality Theorem (Thales):** a line parallel to one side of a triangle divides the other two sides in the same ratio. *Converse* also true.
- Similarity criteria: **AA (AAA), SAS, SSS**.
- Ratio of areas of similar triangles $=$ (ratio of corresponding sides)$^2$ $=$ (ratio of altitudes / medians)$^2$.
- **Pythagoras:** in a right triangle $a^2+b^2=c^2$ ($c$ hypotenuse). Converse: if $a^2+b^2=c^2$, the triangle is right-angled.
- Triples: $(3,4,5)$, $(5,12,13)$, $(8,15,17)$, $(7,24,25)$, $(9,40,41)$ and their multiples.
- Altitude on the hypotenuse creates two triangles similar to the whole and to each other.

> [!EXAMPLE] A 13 m ladder reaches 12 m up a wall → foot is $\sqrt{169-144}=5$ m from the wall.

---

## 10. Surface areas and volumes of solids

| Solid | Lateral / curved surface | Total surface | Volume |
| :--- | :--- | :--- | :--- |
| Cube (side $a$) | $4a^2$ | $6a^2$ | $a^3$ |
| Cuboid ($l,b,h$) | $2h(l+b)$ | $2(lb+bh+hl)$ | $lbh$ |
| **Prism** | perimeter of base $\times$ height | LSA $+\,2\times$ base area | **base area $\times$ height** |
| **Pyramid** | $\tfrac12\times$ perimeter of base $\times$ slant height | LSA $+$ base area | $\tfrac13\times$ base area $\times$ height |
| Cylinder | $2\pi rh$ | $2\pi r(r+h)$ | $\pi r^2h$ |
| Cone | $\pi rl$ | $\pi r(r+l)$ | $\tfrac13\pi r^2h$ |
| Sphere | — | $4\pi r^2$ | $\tfrac43\pi r^3$ |
| Hemisphere | $2\pi r^2$ | $3\pi r^2$ | $\tfrac23\pi r^3$ |

- Cuboid diagonal $=\sqrt{l^2+b^2+h^2}$; cube diagonal $=a\sqrt3$.
- Cone: slant height $l=\sqrt{r^2+h^2}$. Pyramid on a square base: slant height $=\sqrt{h^2+(a/2)^2}$.
- **Prism vs pyramid:** a prism has two identical parallel bases joined by rectangles; a pyramid has one base and triangular faces meeting at an apex. A pyramid's volume is one-third of the prism on the same base and height.
- Prisms/pyramids are named by their base (triangular, square, pentagonal...). Euler: $F+V-E=2$.

> [!EXAMPLE] Square pyramid, base 6 m, height 4 m: slant $=\sqrt{16+9}=5$ m; LSA $=\tfrac12\times24\times5=60$ m²; volume $=\tfrac13\times36\times4=48$ m³.

---

## Quick Revision Box

```
+----------------------------------------------------------------+
| Linear pair 180 | Vertically opposite equal                    |
| Parallel + transversal: corresp=, alt int=, co-int=180         |
| Congruence: SAS SSS ASA AAS RHS (not AAA) | Similarity: AA SAS SSS |
| Centroid 2:1 | Circumcentre: perp bisectors | Incentre: bisectors |
| Polygon: (n-2)180 | diagonals n(n-3)/2 | ext angle sum 360     |
| Rhombus 1/2 d1 d2 | Trapezium 1/2(a+b)h | Heron sqrt(s(s-a)..)   |
| Mid-point thm: parallel & half | Cyclic quad: opp angles 180   |
| Centre angle = 2 x circumference angle | Semicircle = 90        |
| Tangent equal from ext point | length = sqrt(d^2 - r^2)        |
| BPT (Thales) | Area ratio = (side ratio)^2 | a^2+b^2=c^2         |
| Prism V=Bh | Pyramid V=Bh/3 | Cone V=pi r^2 h/3 | Sphere 4/3 pi r^3 |
+----------------------------------------------------------------+
```

*Related:* [[LandSurveyor/AGY/03_Notes/_Out_of_Syllabus/Drafts_Archive/11_Maths_Arithmetic]] · [[LandSurveyor/AGY/03_Notes/_Out_of_Syllabus/Drafts_Archive/12_Maths_Algebra_and_Coordinate_Geometry]] · [[09_Survey_Mathematics_and_Applied_Physics]]
