# Mathematical Object Origin Archive | Étale Cohomology

## 1. Archive Information

- Standard Name: Étale cohomology
- Mathematical Field: Algebraic Geometry
- Abstract: Étale cohomology is sheaf cohomology on the étale site of a scheme. It was formed to supply algebraic varieties—especially varieties over finite fields—with the kind of cohomological invariants, duality, and fixed-point formalism that ordinary singular cohomology supplies over the complex numbers, thereby making the cohomological strategy behind the Weil conjectures mathematically available.

## 2. Core Record

### Precise Description

For a scheme $X$, the **small étale site** $X_{\mathrm{\acute et}}$ has as objects étale morphisms $U\to X$ and as morphisms maps over $X$. A family $\{U_i\to U\}$ is a covering when its maps are jointly surjective. If $\mathcal F$ is a sheaf of abelian groups on this site, its étale cohomology groups are the right-derived functors of global sections:

\[
H^i_{\mathrm{\acute et}}(X,\mathcal F)
  :=R^i\Gamma(X_{\mathrm{\acute et}},\mathcal F).
\]

Thus the defining change from Zariski sheaf cohomology is not a new cochain formula but a new notion of algebraic locality: sections may be glued after passing to étale maps, including nontrivial finite étale covers [1][2].

For arithmetic applications, let $X$ be of finite type over a field $k$ of characteristic $p\ge 0$, choose a separable closure $\bar k$, and take a prime $\ell\ne p$. The finite-level groups

\[
H^i_{\mathrm{\acute et}}(X_{\bar k},\mathbf Z/\ell^n\mathbf Z)
\]

form an inverse system. Under the standard finiteness hypotheses used in this setting, one obtains

\[
H^i_{\mathrm{\acute et}}(X_{\bar k},\mathbf Z_\ell)
 :=\varprojlim_n H^i_{\mathrm{\acute et}}(X_{\bar k},\mathbf Z/\ell^n\mathbf Z),
\qquad
H^i_{\mathrm{\acute et}}(X_{\bar k},\mathbf Q_\ell)
 :=H^i_{\mathrm{\acute et}}(X_{\bar k},\mathbf Z_\ell)\otimes_{\mathbf Z_\ell}\mathbf Q_\ell.
\]

These $\ell$-adic groups are the realization most directly used for the Weil conjectures. They carry functorial actions of endomorphisms of $X$ and of $\operatorname{Gal}(\bar k/k)$. Étale cohomology itself is the underlying site-theoretic theory; $\ell$-adic cohomology is its inverse-limit realization and should not be conflated with cohomology of a naively chosen constant $\mathbf Z_\ell$-sheaf [2].

### Mathematical Context and Formation

The motivating problem class is concrete. Given a smooth projective variety $X/\mathbf F_q$, determine the numbers

\[
N_m=\#X(\mathbf F_{q^m})
\]

and prove the predicted properties of

\[
Z(X,t)=\exp\!\left(\sum_{m\ge1}N_m\frac{t^m}{m}\right):
\]

rationality, a functional equation, an interpretation of its degrees by topological Betti numbers, and absolute-value bounds on its reciprocal zeros and poles. These are the Weil conjectures [3]. Their form suggested a Lefschetz-style solution: construct finite-dimensional graded cohomology groups, let Frobenius act on them, and express each $N_m$ as an alternating trace.

The obstruction was that the required topology was absent. If a variety is defined over $\mathbf C$, singular cohomology can be taken on its analytic space, but a variety over a finite field has no corresponding classical manifold. Passing to the Zariski topology did not solve the problem: it is so coarse that an irreducible variety has no nontrivial finite open partition, and higher Zariski cohomology of constant finite sheaves cannot detect finite étale covering data or reproduce the expected topological Betti groups. A lift to characteristic zero is not available for every variety and, when it exists, does not by itself provide the uniform intrinsic functorial theory required to compare maps, families, and Frobenius. The difficulty was therefore not merely to invent numerical invariants, but to define an algebraic notion of local neighborhood rich enough to support topological-style descent while remaining meaningful in every characteristic.

The forming insight was to replace open subsets by étale neighborhoods. Étale morphisms are the algebraic analogues of local isomorphisms: they are locally of finite presentation, flat, and unramified; they are stable under base change; and finite étale morphisms furnish the unramified finite covers needed to encode algebraic monodromy. Declaring jointly surjective étale families to be covers creates a Grothendieck topology whose sheaves can register monodromy and finite-covering phenomena invisible in the Zariski topology. Applying derived-functor sheaf cohomology on that site then converts this enlarged locality into graded invariants. Finite coefficients of order prime to the characteristic have the robust finiteness, base-change, and duality behavior needed here; passing through the tower $\mathbf Z/\ell^n\mathbf Z$ produces finite-dimensional $\mathbf Q_\ell$-cohomology on which Frobenius acts [1][2]. This combination—étale descent, derived cohomology, and prime-to-characteristic $\ell$-adic passage—formed the sought algebraic replacement for the unavailable classical cohomology.

### Essential Role

Étale cohomology made the central translation in the Weil problem precise: it changed point counting into linear algebra. Let $F$ denote the Frobenius operator on $X_{\overline{\mathbf F}_q}$, with the convention used in the étale Grothendieck–Lefschetz trace formula. For separated $X/\mathbf F_q$ of finite type, that formula gives, with compact supports,

\[
\#X(\mathbf F_{q^m})
 =\sum_i(-1)^i\operatorname{Tr}\!\left((F^m)^*\mid
 H^i_{c,\mathrm{\acute et}}(X_{\overline{\mathbf F}_q},\mathbf Q_\ell)\right).
\]

Consequently,

\[
Z(X,t)=
\prod_i\det\!\left(1-tF^*\mid
H^i_{c,\mathrm{\acute et}}(X_{\overline{\mathbf F}_q},\mathbf Q_\ell)\right)^{(-1)^{i+1}}.
\]

Finite dimensionality turns the originally infinite generating series into a finite alternating product of polynomials, giving the mechanism for rationality [2][4]. For smooth proper varieties, Poincaré duality and the trace pairing relate degrees $i$ and $2\dim X-i$, supplying the cohomological mechanism behind the functional equation. Comparison theorems recover classical finite-coefficient cohomology over $\mathbf C$, explaining why the dimensions have the expected topological meaning [2]. The final size bounds on Frobenius eigenvalues required Deligne's additional deep argument; they do not follow from the definition of the site alone [5].

The specific features of the object answer the earlier obstruction one by one. Étale covers supply nontrivial algebraic local neighborhoods without requiring an analytic space. Sheaf descent and derived functors assemble their local data into global graded groups. When $\ell\ne p$, the Kummer maps $\mathbf G_m\xrightarrow{\ell^n}\mathbf G_m$ are surjective as maps of étale sheaves, and constructible $\ell$-power torsion sheaves satisfy the finiteness, smooth/proper base-change, and duality theorems supporting the usual $\ell$-adic Weil formalism. The inverse limit then supplies characteristic-zero coefficient spaces while retaining the compatible information at every $\ell^n$-level. Functoriality gives Frobenius a linear action; compact supports, cup products, trace maps, and duality provide the operations needed for a fixed-point formula [1][4].

This prime-to-characteristic choice is a statement about the required formal package, not a claim that all $p$-primary étale cohomology is unavailable. In characteristic $p$, for example, the Artin–Schreier sequence is exact on the étale site. What fails is the direct $p$-primary analogue of the usual Kummer-based $\ell$-adic package: the $p$-power map on $\mathbf G_m$ is not étale-locally surjective, and ordinary $p$-adic étale cohomology does not provide the same finiteness and duality theory used in this proof strategy.

The resulting structural viewpoint is deeper than a new way to compute $N_m$: arithmetic point counts are shadows of the spectrum of Frobenius on cohomology. Étale cohomology did not by itself prove every estimate in the Weil conjectures, but it identified and constructed the missing mathematical object in which those estimates could be formulated as statements about eigenvalues and attacked with geometric operations.

## 3. Notes

Étale cohomology and the étale fundamental group are related but distinct: finite locally constant sheaves and finite étale covers belong to the same étale topology, whereas the cohomology groups are derived invariants of sheaves on that topology. Coefficients at the residue characteristic are not simply forbidden, but they require different exact sequences and, for a Weil-cohomology-style characteristic-zero theory, generally different constructions such as crystalline cohomology.

## 4. Sources

[1] M. Artin, A. Grothendieck, and J.-L. Verdier, *Théorie des topos et cohomologie étale des schémas (SGA 4)*, Lecture Notes in Mathematics 269, 270, 305, Springer, 1972–1973.

[2] J. S. Milne, *Lectures on Étale Cohomology*, version 2.21, 2013, https://www.jmilne.org/math/CourseNotes/LEC.pdf.

[3] A. Weil, “Numbers of Solutions of Equations in Finite Fields,” *Bulletin of the American Mathematical Society* 55 (1949), 497–508.

[4] A. Grothendieck et al., *Cohomologie $\ell$-adique et fonctions $L$ (SGA 5)*, Lecture Notes in Mathematics 589, Springer, 1977.

[5] P. Deligne, “La conjecture de Weil. I,” *Publications Mathématiques de l'IHÉS* 43 (1974), 273–307.
