# Mathematical Object Origin Archive | Jacobian Variety

## 1. Archive Information

- Standard Name: Jacobian variety of a smooth projective curve
- Mathematical Field: Algebraic Geometry; Complex Analysis
- Abstract: The Jacobian variety \(J(C)\) packages the periods of all holomorphic differentials on a smooth projective complex curve \(C\) into a \(g\)-dimensional complex torus, canonically identifiable with the group \(\operatorname{Pic}^0(C)\) of degree-zero line bundles. Its formation resolves the natural target and inversion space for Abelian integrals: modulo periods, every prescribed vector of integral values is represented by a degree-zero divisor, and indeed by an effective divisor of degree \(g\) after a base point is fixed.

## 2. Core Record

### Precise Description

Let \(C\) be a smooth, projective, connected complex curve, equivalently a compact connected Riemann surface, of genus \(g\). Put
\[
V=H^0(C,\Omega_C^1)^*.
\]
Integration defines a homomorphism
\[
H_1(C,\mathbb Z)\longrightarrow V,\qquad
\gamma\longmapsto\left(\omega\longmapsto\int_\gamma\omega\right).
\]
Its image \(\Lambda_C\) is a lattice of real rank \(2g\), and the **Jacobian variety** is
\[
J(C)=V/\Lambda_C.
\]
Thus \(J(C)\) is a complex torus of complex dimension \(g\). The intersection pairing on \(H_1(C,\mathbb Z)\), together with the Riemann bilinear relations, supplies its canonical principal polarization; in particular, this torus is projective and therefore an abelian variety [1][2].

For a degree-zero divisor \(D=\sum_p n_p p\), choose paths from a base point \(p_0\) to the points in its support and set
\[
A(D)(\omega)=\sum_p n_p\int_{p_0}^{p}\omega\pmod{\Lambda_C}.
\]
Because \(\sum_p n_p=0\), changing \(p_0\) does not alter the result, and changing paths changes it only by a period. Abel's theorem and the Jacobi inversion theorem together give an isomorphism
\[
\operatorname{Pic}^0(C)=\operatorname{Div}^0(C)/\operatorname{Prin}(C)
\xrightarrow{\;\sim\;}J(C),
\]
so the same object is equivalently the moduli group of degree-zero holomorphic line bundles on \(C\) [1][3]. For fixed \(p_0\), Jacobi inversion can also be expressed as surjectivity of
\[
\alpha_g:\operatorname{Sym}^g(C)\longrightarrow J(C),\qquad
p_1+\cdots+p_g\longmapsto
\bigl[\mathcal O_C(p_1+\cdots+p_g-gp_0)\bigr].
\]

### Mathematical Context and Formation

The motivating problem is the inversion of Abelian integrals on an algebraic curve. Choose a basis \(\omega_1,\ldots,\omega_g\) of holomorphic differentials. Given a vector \(u=(u_1,\ldots,u_g)\), the inversion problem asks for points \(p_1,\ldots,p_g\in C\) satisfying
\[
\sum_{j=1}^{g}\int_{p_0}^{p_j}\omega_i\equiv u_i,
\qquad i=1,\ldots,g,
\]
with the congruences understood modulo all period vectors obtained by integrating around closed cycles [2][4]. This generalizes inversion of an elliptic integral, where one point on a genus-one curve and one integral variable suffice.

For \(g>1\), neither the curve itself nor a collection of single-valued scalar inverse functions provides an adequate solution space. First, continuation of an integral along different paths adds periods, so its value is intrinsically multivalued in \(\mathbb C^g\). Second, \(C\) has complex dimension one while the simultaneous values of the \(g\) independent integrals require a \(g\)-dimensional target; one generally has to vary an unordered \(g\)-tuple of points, represented by \(\operatorname{Sym}^g(C)\), rather than one point. Third, Abel's theorem shows that divisors differing by the divisor of a meromorphic function have the same integral data. A satisfactory inversion space therefore had to quotient both the path ambiguity by the full period lattice and the divisor ambiguity by principal divisors.

The decisive construction is to collect all holomorphic integrals into the functional space \(H^0(C,\Omega_C^1)^*\), quotient that space by the period lattice \(\Lambda_C\), and map divisors to the resulting classes. This produces \(J(C)\). The number of variables in \(\operatorname{Sym}^g(C)\) now matches \(\dim J(C)=g\), while Abel's theorem identifies the kernel on degree-zero divisors and Jacobi inversion supplies surjectivity. In this precise mathematical sense, the Jacobian is the object formed by reorganizing the higher-genus inversion problem into a map between spaces of the correct dimension with its unavoidable period equivalence built in [1][2][4].

### Essential Role

The Jacobian makes the **target and solvability** portions of Abelian inversion tractable. A prescribed vector \(u\in\mathbb C^g\) is not treated as an absolute value, which would depend on choices of paths, but as a point \([u]\in J(C)=\mathbb C^g/\Lambda_C\). The quotient by \(\Lambda_C\) removes exactly the monodromy caused by changing integration paths. The additive law on the torus simultaneously mirrors addition of divisors, so sums of point integrals become one group-valued Abel–Jacobi map rather than a system of unrelated multivalued expressions.

Surjectivity of \(\alpha_g\) then states precisely that every admissible period class has a solution by \(g\) points. Abel's theorem states precisely when two degree-zero divisors produce the same point: their difference is principal. Hence the Jacobian does more than record periods; through
\[
J(C)\cong\operatorname{Pic}^0(C),
\]
it reformulates inversion as the classification of degree-zero divisor classes or line bundles, with tensor product providing the group law. The hard ambiguities of path choice and meromorphic equivalence are thereby converted into the lattice quotient and the Picard quotient, respectively. This is the object's direct contribution to the motivating problem. The principal polarization and the later role of Jacobians in moduli and arithmetic are important further structures, but they are not substitutes for this original inversion mechanism.

## 3. Notes

- “Jacobian variety” here is not the Jacobian matrix or determinant from multivariable calculus.
- For \(g=0\), \(J(C)\) is the trivial abelian variety; for \(g=1\) and a chosen base point, \(C\cong J(C)\).
- The analytic quotient \(H^0(C,\Omega_C^1)^*/\Lambda_C\) is specific to the complex setting. Over a general field, the Jacobian is defined algebraically as the degree-zero Picard variety.
- Singular curves lead to generalized Jacobians, which are distinct objects and are not covered by this archive.

## 4. Sources

[1] Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry*, Wiley-Interscience, 1978, Chapter 2.

[2] David Mumford, *Curves and Their Jacobians*, University of Michigan Press, 1975.

[3] J. S. Milne, “Jacobian Varieties,” in Gary Cornell and Joseph H. Silverman (eds.), *Arithmetic Geometry*, Springer, 1986, pp. 167–212.

[4] C. G. J. Jacobi, “De functionibus duarum variabilium quadrupliciter periodicis, quibus theoria transcendentium Abelianarum innititur,” *Journal für die reine und angewandte Mathematik* **13** (1835), 55–78.
