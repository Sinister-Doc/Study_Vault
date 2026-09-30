---
exam: KEA Land Surveyor 2026
subject: Paper-II Mathematics (A) — Algebra & Coordinate Geometry
topic: Identities, linear & quadratic equations, factorisation, HCF/LCM of polynomials, graphs, coordinate geometry
priority: Tier 1 (part of 40 marks Mathematics)
tags: [land-surveyor, paper-2, mathematics, algebra, coordinate-geometry]
---

# 12. Maths — Algebra & Coordinate Geometry

> [!IMPORTANT] Exam focus
> Expect direct-formula questions: identities, discriminant, sum/product of roots, distance and section formulas. Learn the boxes below.

---

## 1. Basics of algebra

- **Term:** a product of a number and variables ($5x^2y$). **Coefficient:** the numeric part (5). **Degree:** sum of exponents in a term (3 for $5x^2y$); degree of an expression = highest term degree.
- **Like terms** have the same variables with the same powers; only like terms can be added or subtracted.
- Types: monomial (1 term), binomial (2), trinomial (3), polynomial (many).
- **Signed number rules:** $(+)(+)=+$, $(-)(-)=+$, $(+)(-)=-$. $-(a-b)=b-a$. $a^m\cdot a^n=a^{m+n}$, $(a^m)^n=a^{mn}$, $a^0=1$.
- Symbols: $\in$ belongs to, $\Rightarrow$ implies, $\therefore$ therefore, $\neq$ not equal, $\approx$ approximately.

---

## 2. Multiplication of expressions and identities

| Identity | Name |
| :--- | :--- |
| $(a+b)^2=a^2+2ab+b^2$ | square of a sum |
| $(a-b)^2=a^2-2ab+b^2$ | square of a difference |
| $(a+b)(a-b)=a^2-b^2$ | difference of squares |
| $(x+a)(x+b)=x^2+(a+b)x+ab$ | product of binomials |
| $(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$ | square of a trinomial |
| $(a\pm b)^3=a^3\pm3a^2b+3ab^2\pm b^3$ | cube identities |
| $a^3+b^3=(a+b)(a^2-ab+b^2)$ | sum of cubes |
| $a^3-b^3=(a-b)(a^2+ab+b^2)$ | difference of cubes |
| $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$ | special identity |

- If $a+b+c=0$ then $a^3+b^3+c^3=3abc$.
- $a^2+b^2=(a+b)^2-2ab=(a-b)^2+2ab$; $(a+b)^2-(a-b)^2=4ab$.
- If $x+\dfrac1x=k$ then $x^2+\dfrac1{x^2}=k^2-2$.

> [!EXAMPLE] $103^2=(100+3)^2=10000+600+9=$ **10609**. $98\times102=(100-2)(100+2)=$ **9996**.

---

## 3. Linear equations

- Form $ax+b=0$ → $x=-\dfrac ba$. Move variable terms to one side, constants to the other; whatever is done to one side is done to the other (balance-scale idea).
- **Word problems:** let the unknown be $x$, translate each sentence into an equation. Typical: ages, consecutive numbers ($x, x+1, x+2$), digits, fractions, perimeters.
- **Two variables (simultaneous):**
  - Substitution: express one variable from an equation and substitute.
  - Elimination: multiply to equalise coefficients, add/subtract.
  - Cross-multiplication for $a_1x+b_1y+c_1=0$, $a_2x+b_2y+c_2=0$: $\dfrac{x}{b_1c_2-b_2c_1}=\dfrac{y}{c_1a_2-c_2a_1}=\dfrac1{a_1b_2-a_2b_1}$.
  - Consistency: $\dfrac{a_1}{a_2}\neq\dfrac{b_1}{b_2}$ → one solution; all three ratios equal → infinite; $\dfrac{a_1}{a_2}=\dfrac{b_1}{b_2}\neq\dfrac{c_1}{c_2}$ → none (parallel lines).

**Graph of a linear equation**
- Rectangular (Cartesian) coordinate system: $x$-axis horizontal, $y$-axis vertical, origin $(0,0)$.
- **Quadrants and signs:** I $(+,+)$, II $(-,+)$, III $(-,-)$, IV $(+,-)$ (counter-clockwise from top right).
- Points on the $x$-axis have $y=0$; on the $y$-axis have $x=0$.
- $y=mx+c$: slope $m$, $y$-intercept $c$. Plot two points and join.
- The solution of two simultaneous equations is the **intersection point** of their lines.

---

## 4. Quadratic equations

Standard form: $ax^2+bx+c=0$, $a\neq0$.

| Type | Method |
| :--- | :--- |
| Pure quadratic ($b=0$) | $x^2=-c/a$; $x=\pm\sqrt{-c/a}$ |
| Affected quadratic — factorisation | split the middle term: find $p,q$ with $p+q=b$, $pq=ac$ |
| Formula method | $x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$ |
| Completing the square | $x^2+\dfrac bax=-\dfrac ca$ → add $\left(\dfrac b{2a}\right)^2$ |

**Discriminant $D=b^2-4ac$ (nature of roots)**

| $D$ | Roots |
| :--- | :--- |
| $D>0$ | two distinct real roots (rational if $D$ is a perfect square) |
| $D=0$ | two equal real roots, $x=-\dfrac b{2a}$ |
| $D<0$ | no real roots (complex) |

**Roots and coefficients** (roots $\alpha,\beta$)
$$\alpha+\beta=-\frac ba,\qquad \alpha\beta=\frac ca$$
- **Forming an equation from roots:** $x^2-(\alpha+\beta)x+\alpha\beta=0$.
- $\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta$; $\lvert\alpha-\beta\rvert=\dfrac{\sqrt D}{\lvert a\rvert}$.
- Equations reducible to quadratic: e.g. $x+\dfrac1x=\dfrac{10}3$ → multiply by $x$; $x^4-5x^2+4=0$ → put $y=x^2$; radical equations → square both sides and check roots.
- **Graphical method:** plot $y=ax^2+bx+c$ (a parabola). Its $x$-intercepts are the roots; vertex at $x=-\dfrac b{2a}$; opens upward if $a>0$, downward if $a<0$. No intercepts means no real roots.

> [!EXAMPLE] $x^2-5x+6=0$ → $(x-2)(x-3)=0$ → $x=2,3$. Sum $=5=-(-5)/1$ ✓, product $=6$ ✓. Equation with roots 4 and −1: $x^2-3x-4=0$.

---

## 5. Factorisation

1. **Common factor:** $6x^2+9x=3x(2x+3)$.
2. **Grouping:** $ax+ay+bx+by=(a+b)(x+y)$.
3. **Trinomial $x^2+bx+c$:** find two numbers with sum $b$, product $c$. $x^2+7x+12=(x+3)(x+4)$.
4. **$ax^2+bx+c$ (split the middle term):** find $p,q$ with $p+q=b$, $pq=ac$. $2x^2+7x+3$: $ac=6$, $p,q=6,1$ → $2x^2+6x+x+3=(2x+1)(x+3)$.
5. **Perfect squares:** $a^2\pm2ab+b^2=(a\pm b)^2$.
6. **Difference of squares:** $a^2-b^2=(a+b)(a-b)$.
7. Cubes: use the sum/difference of cubes identities.
- Algebraic tiles idea: $x^2$ tile, $x$ strip, unit square; arrange into a rectangle whose sides are the factors.

---

## 6. HCF and LCM of polynomials

- Factorise each expression completely.
- **HCF** = product of common factors with the lowest powers. **LCM** = product of all factors with the highest powers.
- $\text{HCF}\times\text{LCM}=$ product of the two expressions.

> [!EXAMPLE] $x^2-1=(x-1)(x+1)$ and $x^2+2x+1=(x+1)^2$ → HCF $=x+1$; LCM $=(x-1)(x+1)^2$.

---

## 7. Coordinate geometry (plane)

For $A(x_1,y_1)$ and $B(x_2,y_2)$:

| Quantity | Formula |
| :--- | :--- |
| Distance | $AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$ |
| Distance from origin | $\sqrt{x^2+y^2}$ |
| Mid-point | $\left(\dfrac{x_1+x_2}2,\dfrac{y_1+y_2}2\right)$ |
| Section formula (internal, $m:n$) | $\left(\dfrac{mx_2+nx_1}{m+n},\dfrac{my_2+ny_1}{m+n}\right)$ |
| Slope | $m=\dfrac{y_2-y_1}{x_2-x_1}=\tan\theta$ |
| Parallel lines | $m_1=m_2$ |
| Perpendicular lines | $m_1m_2=-1$ |
| Triangle area | $\dfrac12\lvert x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)\rvert$ |
| Collinear points | triangle area $=0$ |
| Centroid | $\left(\dfrac{x_1+x_2+x_3}3,\dfrac{y_1+y_2+y_3}3\right)$ |

**Equations of a line**
- Slope-intercept: $y=mx+c$. Point-slope: $y-y_1=m(x-x_1)$. Two-point: $\dfrac{y-y_1}{y_2-y_1}=\dfrac{x-x_1}{x_2-x_1}$.
- Intercept form: $\dfrac xa+\dfrac yb=1$. Axes: $x=0$ ($y$-axis), $y=0$ ($x$-axis).
- **Finding a value along one axis when the other is given:** substitute the known coordinate into the line equation. For $2x+3y=12$, at $x=3$: $y=2$.
- Plotting simple equations: pick 2–3 values of $x$, compute $y$, mark points, join.

> [!EXAMPLE] $A(1,2)$, $B(4,6)$: $AB=\sqrt{9+16}=5$; mid-point $(2.5,4)$; slope $=4/3$. Points dividing $AB$ in $1:2$: $\left(\dfrac{4+2}{3},\dfrac{6+4}{3}\right)=(2,\,10/3)$.

---

## Quick Revision Box

```
+---------------------------------------------------------------+
| (a+b)^2 = a^2+2ab+b^2 | a^2-b^2=(a+b)(a-b)                    |
| a^3+b^3=(a+b)(a^2-ab+b^2) | a+b+c=0 => a^3+b^3+c^3=3abc       |
| x+1/x=k => x^2+1/x^2 = k^2-2                                  |
| Quadrants: I(+,+) II(-,+) III(-,-) IV(+,-)                    |
| Quadratic: x = [-b +/- sqrt(b^2-4ac)]/2a                      |
| D>0 two real | D=0 equal | D<0 none                           |
| Sum of roots = -b/a | Product = c/a | x^2-(S)x+P = 0          |
| HCF: common factors, lowest power | LCM: all, highest power   |
| Distance = sqrt(dx^2+dy^2) | Slope = dy/dx | perp: m1.m2=-1   |
| Triangle area = 1/2|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|            |
+---------------------------------------------------------------+
```

*Related:* [[11_Maths_Arithmetic]] · [[13_Maths_Geometry_and_Mensuration]] · [[09_Survey_Mathematics_and_Applied_Physics]] (coordinate area determinant)
