# Mathematical Object Origin Archive | De Rham Cohomology

## 1. Archive Information

- Standard Name: De Rham cohomology
- Mathematical Field: Differential Geometry; Algebraic Topology
- Abstract: De Rham cohomology is the graded real vector space obtained from closed differential forms on a smooth manifold by identifying forms that differ by an exact form. It was formed around the problem of separating, in positive degree, the local differential condition for a form to possess primitives from the global topological obstruction to choosing one primitive over the whole manifold. Its period pairing with cycles turns this analytic obstruction into real-valued topological data.

## 2. Core Record

### Precise Description

Let $M$ be a smooth manifold. The exterior derivative gives a cochain complex
\[
0\longrightarrow \Omega^0(M)\xrightarrow{d}\Omega^1(M)\xrightarrow{d}\Omega^2(M)\xrightarrow{d}\cdots,
\qquad d^2=0.
\]
For $k\geq 0$, the degree-$k$ de Rham cohomology of $M$ is
\[
H^k_{\mathrm{dR}}(M)
 =\frac{Z^k(M)}{B^k(M)}
 =\frac{\ker(d:\Omega^k(M)\to\Omega^{k+1}(M))}
 {\operatorname{im}(d:\Omega^{k-1}(M)\to\Omega^k(M))},
\]
where in degree zero the denominator is understood to be $0$. Thus its elements are equivalence classes $[\omega]$ of closed $k$-forms, with $\omega\sim\omega+d\eta$ when $k\geq1$. The wedge product descends to the quotient and makes $H^*_{\mathrm{dR}}(M)=\bigoplus_k H^k_{\mathrm{dR}}(M)$ a graded-commutative real algebra.

For a smooth singular $k$-cycle $z$, integration defines the period $\int_z\omega$. Stokes' theorem implies that this depends only on the de Rham class $[\omega]$ and the homology class $[z]$: adding an exact form or a boundary does not change the value. Integration therefore induces
\[
I_k:H^k_{\mathrm{dR}}(M)\longrightarrow
\operatorname{Hom}_{\mathbb R}(H_k(M;\mathbb R),\mathbb R).
\]
The de Rham theorem identifies $H^k_{\mathrm{dR}}(M)$ naturally with $H^k_{\mathrm{sing}}(M;\mathbb R)$; combined with the universal coefficient identification over $\mathbb R$, it says that $I_k$ is an isomorphism [1][2]. This theorem is a property of the object, not part of its definition.

### Mathematical Context and Formation

Fix $k\geq1$. A concrete motivating problem is the **global primitive problem**: for a given smooth closed $k$-form $\omega$ on $M$, decide whether there is a globally defined $(k-1)$-form $\eta$ satisfying $d\eta=\omega$. In period language, this is the exactness-detection problem: does the vanishing of $\int_z\omega$ for every $k$-cycle force a global primitive? A distinct companion problem is **period realization**: given a real linear functional
\[
\lambda:H_k(M;\mathbb R)\to\mathbb R,
\]
can one find a closed $k$-form whose integral over each cycle $z$ equals $\lambda([z])$? Such a functional is an admissible period system because its values are linear and depend only on homology classes.

The difficulty in the primitive problem is genuinely global. The Poincaré lemma solves $d\eta=\omega$ on every sufficiently small coordinate ball for $k\geq1$, so the differential equation itself has no local obstruction once $d\omega=0$. Nevertheless, the local primitives need not patch to one global primitive. On $S^1$, for example, the globally defined closed form represented in angular coordinates by $d\theta$ has nonzero integral around the circle and therefore cannot be the exterior derivative of a globally defined function. Direct local integration misses this obstruction; its attempted primitives return with a changed value after one circuit. Conversely, simplicial or singular cycles record the global topology, but by themselves do not organize differential forms according to which ones differ only by a choice of primitive.

Two facts indicate the needed construction. First, $d^2=0$ places every exact form among the closed forms. Second, Stokes' theorem gives
\[
\int_z d\eta=\int_{\partial z}\eta=0
\]
for every cycle $z$, so exact forms contribute no period data. Closed forms therefore contain both globally significant forms and exact forms that are invisible to every period; retaining all closed forms fails to isolate the obstruction, while discarding differential forms for purely combinatorial invariants loses the analytic representative.

The resulting insight is to quotient closed forms by exact forms. For $k\geq1$, the class $[\omega]$ then measures precisely whether $\omega$ has a global primitive: it vanishes exactly when such a primitive exists. Integration supplies the map $I_k$ from these classes to functionals on homology. Injectivity of $I_k$ answers exactness detection by showing that no nonzero de Rham class has every period zero. Surjectivity answers the separate realization problem by producing a de Rham class for every linear functional on $H_k(M;\mathbb R)$.

De Rham's 1931 work established, in the language then used for differentiable manifolds, the decisive correspondence between differential forms and topological period data [1]. The modern cochain-complex formulation above packages that correspondence as de Rham cohomology and the de Rham theorem [2]. This last sentence is interpretive synthesis: it distinguishes the modern formulation from the notation and language of the original work.

### Essential Role

For $k\geq1$, de Rham cohomology replaces the global patching question by the exact algebraic criterion
\[
d\eta=\omega\text{ globally for some }\eta
\quad\Longleftrightarrow\quad
[\omega]=0\text{ in }H^k_{\mathrm{dR}}(M).
\]
This works because the denominator consists exactly of closed forms possessing global primitives, while $d^2=0$ ensures that it is a subspace of the closed forms under consideration. The quotient does not merely record that patching failed: it identifies two closed forms when their difference can be repaired by changing a global primitive.

The period pairing makes this criterion accessible through topology. If $\omega=d\eta$, all its periods vanish by Stokes' theorem. The nontrivial converse—if a closed $k$-form, $k\geq1$, has zero periods on all $k$-cycles, then it is exact—is precisely the injectivity of $I_k$, supplied by the de Rham isomorphism over $\mathbb R$. Hence the object makes tractable exactly the step that local calculus could not handle: deciding whether locally available primitives globalize. Separately, surjectivity of $I_k$ solves period realization: every real linear functional on $H_k(M;\mathbb R)$ has a closed differential-form representative, unique up to addition of an exact form at the level of its de Rham class.

The deeper structural change is that differential and topological information become two descriptions of the same real cohomology class. A class can be manipulated using smooth forms, exterior differentiation, pullback, and wedge product, while its periods and its image under the de Rham isomorphism depend only on the topology of $M$. This is the direct structural contribution relevant to the motivating problems; later uses in characteristic classes, Hodge theory, and other subjects are not needed to justify the object's formation.

## 3. Notes

- Degree zero is part of the object but not of the positive-degree primitive problem: $H^0_{\mathrm{dR}}(M)$ consists of locally constant real-valued functions, with one copy of $\mathbb R$ for each connected component.
- De Rham cohomology uses real coefficients and detects no torsion in integral cohomology. Thus it solves the period and primitive problem for real differential forms but is not a replacement for $H^*(M;\mathbb Z)$ when torsion matters.
- The statement about the angular form on $S^1$ means the intrinsic global $1$-form obtained by restricting $-y\,dx+x\,dy$ to the unit circle; the symbol $d\theta$ is local notation, since no single-valued global angle function exists.
- De Rham cohomology is distinct from the de Rham theorem: the former is the quotient object defined from the differential-form complex; the latter identifies that object with singular cohomology over $\mathbb R$.

## 4. Sources

[1] Georges de Rham, “Sur l'analysis situs des variétés à $n$ dimensions,” *Journal de Mathématiques Pures et Appliquées*, 9e série, 10 (1931), 115–200. https://eudml.org/doc/234905

[2] Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Graduate Texts in Mathematics 82, Springer, 1982, Chapters I–II.
