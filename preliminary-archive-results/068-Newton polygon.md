# Mathematical Object Origin Archive | Newton Polygon

## 1. Archive Information

- Standard Name: Newton polygon
- Mathematical Field: Algebraic Geometry and Algebraic Number Theory
- Abstract: The Newton polygon is the lower convex envelope of exponent or coefficient-valuation data associated with a polynomial. It arose from the problem of solving an algebraic equation \(f(x,y)=0\) for \(y\) as a series, when the first exponent may be fractional and cannot be chosen in advance. A lower edge identifies exactly the monomials that can cancel at lowest order; its slope gives a candidate leading exponent, and its edge polynomial gives the candidate leading coefficients. Repeating this construction organizes the successive terms of a fractional-power branch.

## 2. Core Record

### Precise Description

Let \(k\) be an algebraically closed field of characteristic zero, and write a nonzero polynomial, or a polynomial in \(y\) with formal-power-series coefficients, as
\[
f(x,y)=\sum_{i=0}^{n}a_i(x)y^i
      =\sum_{i,j}c_{ij}x^jy^i,
\qquad a_i(x)\in k[[x]].
\]
For each nonzero \(a_i(x)\), put
\[
m_i=\operatorname{ord}_x a_i(x)=\min\{j:c_{ij}\ne0\}.
\]
The Newton polygon of \(f\) relative to \(x\) is the polygonal lower boundary of
\[
\operatorname{Conv}\!\left(
  \bigcup_{a_i\ne0}\bigl((i,m_i)+\mathbb R_{\ge0}(0,1)\bigr)
\right).
\]
Equivalently, it is the lower convex envelope of the exponent points \((i,j)\) for the nonzero monomials \(c_{ij}x^jy^i\); points above the lowest point with a fixed \(i\) do not affect that envelope. This convention puts the exponent of \(y\) on the horizontal axis and the exponent of \(x\) on the vertical axis [1,2].

Suppose a lower edge \(E\) lies on
\[
j+\lambda i=\mu
\]
with all exponent points on or above that line. The edge has slope \(-\lambda\). Its associated edge polynomial is
\[
\Phi_E(C)=\sum_{(i,j)\in E}c_{ij}C^i.
\]
If \(\lambda=k_0/\ell>0\) in lowest terms and \(c\ne0\) satisfies \(\Phi_E(c)=0\), then \(cx^\lambda\) passes the necessary lowest-order test for being the leading term of a fractional-power solution. Indeed, after setting
\[
x=X^\ell,\qquad y=X^{k_0}(c+Y)
\]
and dividing \(f\) by \(X^{\ell\mu}\), every exponent of \(X\) is nonnegative, the terms from \(E\) give \(\Phi_E(c+Y)\), and its constant term vanishes. A Newton polygon for the transformed equation can then select the next exponent and coefficient [2,3]. Under the stated algebraic-closure and characteristic-zero hypotheses, the Newton–Puiseux theorem guarantees that the roots of a polynomial monic in \(y\) lie in some \(k((x^{1/N}))\); when the coefficients lie in \(k[[x]]\), its integral roots have nonnegative exponents. Thus the recursive candidate construction lifts to fractional-power roots after allowing a finite ramification \(x=X^N\) [2].

For example, over an algebraically closed field \(k\) of characteristic zero,
\[
f(x,y)=y^2-x^3-x^4
\]
has relevant exponent points \((2,0)\), \((0,3)\), and \((0,4)\). Its lower edge joins \((0,3)\) to \((2,0)\), so its slope is \(-3/2\), and
\[
\Phi_E(C)=C^2-1.
\]
Thus the two possible leading terms are \(y=\pm x^{3/2}+\cdots\). In \(k[[x^{1/2}]]\) the resulting roots are
\[
y=\pm x^{3/2}(1+x)^{1/2}
 =\pm x^{3/2}\left(1+\frac{x}{2}-\frac{x^2}{8}+\cdots\right),
\]
which exhibit the fractional exponent detected by the edge.

### Mathematical Context and Formation

The motivating problem was to determine series branches \(y=y(x)\) satisfying a polynomial equation \(f(x,y)=0\). Newton described his polygonal procedure in his letter to Henry Oldenburg of 24 October 1676; the method was later developed into the Newton–Puiseux procedure [1,2]. The concrete task is not merely to verify a proposed series, but to discover its leading term
\[
y=cx^\lambda+\text{terms of higher }x\text{-order}
\]
when neither \(c\) nor the rational exponent \(\lambda\) is known.

The exact condition for ordinary implicit-function recursion, after centering at a solution \((0,y_0)\), is
\[
f(0,y_0)=0,\qquad \frac{\partial f}{\partial y}(0,y_0)\ne0.
\]
Then \(y\) can be solved uniquely as an ordinary formal power series in \(x\) near \(y_0\). When this derivative vanishes, or when the projection of the branch to the \(x\)-axis is ramified, that linear recursion no longer applies. Restricting the ansatz to integral powers also loses genuine branches: \(y^2=x^3\), for example, begins with \(x^{3/2}\). Directly comparing every term of a general fractional series is not an effective starting procedure because its denominator and first exponent are themselves part of the unknown. In modern language, these facts diagnose why an ordinary Taylor-series ansatz is inadequate; they are not a claim that later formal tools were available in Newton's period.

The formation of the polygon follows from the exact lowest-order cancellation condition. Substituting \(y=cx^\lambda+\cdots\) into one monomial gives
\[
c_{ij}x^jy^i=c_{ij}c^i x^{j+\lambda i}+\text{higher-order terms}.
\]
Let \(\mu=\min(j+\lambda i)\). If this minimum occurred at only one exponent point, its nonzero term could not be cancelled, so \(f(x,y)\) could not vanish. The minimum must therefore be attained by at least two points. Those points lie on a lower supporting line \(j+\lambda i=\mu\), hence on an edge of slope \(-\lambda\). Cancellation of their common lowest power \(x^\mu\) is exactly the equation
\[
\Phi_E(c)=0.
\]
Thus the diagram is forced by the need to identify simultaneous lowest-order terms: edge slopes enumerate candidate leading exponents, while the polynomial carried by an edge determines candidate leading coefficients [2,3].

The same construction has an exact modern valuation formulation. Regard \(f\) as a polynomial in \(y\) over the Laurent-series field \(k((x))\), equipped with the \(x\)-adic valuation. Then the coefficient point \((i,\operatorname{ord}_x a_i)\) is the usual valued-field Newton-polygon point. This formulation explains, retrospectively, why exponent balance and valuation balance are the same mathematics. It should not be confused with a claim that the abstract theory of valued or Henselian fields formed part of the original setting.

### Essential Role

The polygon made the otherwise undetermined first step of series construction finite and calculable. Rather than guessing arbitrary rational exponents, one reads a finite list from the negative slopes of the lower edges. Rather than expanding the entire equation at once, one retains only the edge terms, which are precisely those of common lowest order, and solves the finite algebraic equation \(\Phi_E(c)=0\). In the example \(y^2-x^3-x^4=0\), the edge immediately supplies \(\lambda=3/2\) and \(c=\pm1\), the two pieces of information an integral-power ansatz cannot provide.

Its role continues recursively. After choosing an edge and a root \(c\), the substitution
\[
y=x^\lambda(c+y_1)
\]
cancels the selected leading order and produces a new equation for a remainder of positive order. Constructing the new equation's Newton polygon determines the next increment in the exponent and its coefficient. Over an algebraically closed coefficient field of characteristic zero, for a polynomial monic in \(y\), the Newton–Puiseux theorem ensures that this recursive process yields roots in \(k((x^{1/N}))\) for some finite \(N\), and it can compute arbitrarily many terms of each branch [2,3]. In positive characteristic the unrestricted statement fails: Puiseux exponents can require unbounded denominators, so additional hypotheses or larger generalized-series fields are needed. The original polygon alone does not encode an entire branch; the edge polynomial and successive transformed polygons are essential. Nor does the first polygon by itself prove convergence or determine the number of analytic branches in every singular case.

The deeper structural contribution was to replace an unorganized symbolic expansion by weighted convex geometry. A supporting line assigns weights \(1\) to \(x\) and \(\lambda\) to \(y\); the monomials on its edge form the weighted initial part of \(f\). Solving that initial part removes the lowest-order obstruction before recursion continues. The polygon therefore made visible both the permissible scale of a branch and the exact terms responsible for its first cancellation.

Root valuations and factorization over \(p\)-adic or other complete valued fields are later extensions of this same mechanism, not the motivating role asserted here. In that later setting, after extending the valuation to an algebraic closure, an edge of slope \(s\) and horizontal length \(h\) records \(h\) roots, counted with multiplicity, of valuation \(-s\); over a Henselian field, slope decompositions also guide factorization [2,4]. These arithmetic uses explain the object's central place in algebraic number theory while remaining distinct from its formation in the series-solution problem.

## 3. Notes

- The attribution of the polygonal procedure to Newton and its connection with solving \(f(x,y)=0\) by fractional-power series are established in Newton's 1676 letter and modern accounts of it [1,2]. The convex-hull, valuation, and weighted-initial-form language used above is a retrospective mathematical synthesis.
- Puiseux's later work supplied a more systematic development. Accordingly, the full theorem on fractional-power branches should not be attributed in its modern form solely to Newton [2].
- This one-dimensional lower polygon is related to, but distinct from, the full Newton polytope of a multivariable polynomial. It uses one exponent as a coefficient valuation and reads branch orders from lower edges.
- Some conventions interchange the coordinate axes or use upper hulls; the sign relation between slope and leading exponent changes accordingly.

## 4. Sources

[1] Isaac Newton, “Letter from Newton to Henry Oldenburg, dated 24 October 1676,” manuscript MS Add. 9597/2/18/56, Cambridge University Library; normalized text, The Newton Project, https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00270.

[2] Bill Casselman, “Newton Polygons,” University of British Columbia, revised 21 October 2018, especially §§3–4, https://www.math.ubc.ca/~cass/research/pdf/Newton.pdf.

[3] Michel Talon, “Puiseux Expansions,” 23 March 2020, https://www.lpthe.jussieu.fr/~talon/puiseux_examples.pdf.

[4] Andrei Jorza, “Newton Polygons and Factoring Polynomials over Local Fields,” 8 March 2005, https://www.wstein.org/129-05/section/m129-section-newton-polygons/newton_polygons.pdf.
