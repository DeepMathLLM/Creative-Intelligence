# Mathematical Object Origin Archive | Hilbert Scheme

## 1. Archive Information

- Standard Name: Hilbert scheme
- Mathematical Field: Algebraic Geometry
- Abstract: The Hilbert scheme is the representing space for flat families of closed subschemes of a fixed projective scheme, usually with a prescribed Hilbert polynomial. It arose from the problem of turning a collection of algebraic subspaces—including their degenerations and nonreduced structures—into an algebraic parameter space carrying a universal family.

## 2. Core Record

### Precise Description

Let \(S\) be a noetherian scheme, let \(X\to S\) be projective, choose a relatively very ample invertible sheaf \(L\), and fix a numerical polynomial \(P\). The classical fixed-polynomial Hilbert functor assigns to an \(S\)-scheme \(T\) the set
\[
\operatorname{Hilb}^{P,L}_{X/S}(T)
=
\left\{
Z\hookrightarrow X_T=X\times_S T:
\begin{array}{l}
Z\text{ is a closed subscheme flat over }T,\\
\chi(Z_t,L_t^{\otimes m}|_{Z_t})=P(m)\text{ for every geometric }t
\end{array}
\right\},
\]
with pullback of families defining its contravariant functoriality. Because \(X_T\to T\) is projective, each such \(Z\to T\) is also projective; finite-presentation hypotheses are understood in this classical noetherian formulation. Grothendieck's representability theorem states that this functor is represented by a projective \(S\)-scheme \(H=\operatorname{Hilb}^{P,L}_{X/S}\) [1][2]. Thus there is a universal closed subscheme
\[
\mathcal U\hookrightarrow X\times_S H,
\]
flat over \(H\), and, naturally in \(T\),
\[
\operatorname{Hom}_S(T,H)\cong \operatorname{Hilb}^{P,L}_{X/S}(T),
\qquad
f\longmapsto (1_X\times f)^*\mathcal U.
\]
A geometric point of \(H\) therefore represents a closed subscheme, not merely its underlying set or associated cycle: its defining ideal, nilpotent structure, and embedded components are part of the datum.

### Mathematical Context and Formation

The motivating problem class was an embedded moduli problem: for a projective \(S\)-scheme \(X\), construct an algebraic parameter space for all subspaces of \(X\) having fixed numerical type, in such a way that a family varying over any base \(T\) is itself encoded by a morphism from \(T\) to that parameter space. A bare set of subvarieties could not support specialization, tangent directions, or a universal family. Cycle or Chow coordinates provided parameters for effective cycles, but a cycle records generic components with multiplicities and forgets the ideal-sheaf information that distinguishes embedded components and different nonreduced subschemes with the same associated cycle. Directly parameterizing polynomial equations was also unstable: the number and degrees of generators can vary, while arbitrary subspaces of a vector space of equations need not be ideals because they may fail compatibility with multiplication.

The formation of the Hilbert scheme resolves these connected obstacles by changing both the objects and the notion of variation. First, one parameterizes closed subschemes, equivalently quotient algebras \(\mathcal O_{X_T}\twoheadrightarrow\mathcal O_Z\), rather than only reduced subvarieties or cycles. Second, one admits precisely flat families. In a projective flat family the Hilbert polynomial of the fibers is locally constant, so fixing \(P\) selects a bounded numerical class stable under base change and specialization. Third, boundedness and uniform regularity reduce the apparently unbounded ideal-sheaf problem to finite-dimensional linear algebra: for a sufficiently large degree \(m\), chosen uniformly from \(P\), the relevant ideal sheaves are controlled by their degree-\(m\) global sections. Those sections define points of a Grassmannian, and compatibility with multiplication and with the equations of \(X\) cuts out the required locus by algebraic conditions. This is the central construction behind the projective representing scheme, rather than merely a convenient later model [1][2].

### Essential Role

The Hilbert scheme makes the family aspect of the embedded moduli problem tractable. Its representing property replaces the task of separately describing every base-dependent family \(Z\subset X\times_S T\) by the ordinary geometric task of studying maps \(T\to H\); the universal subscheme recovers every family by a unique pullback. Flatness prevents changes of Hilbert polynomial inside a connected family, while the fixed polynomial supplies the boundedness needed for a finite-type projective parameter space. Consequently, a degenerating collection of subschemes has a scheme-theoretic limit inside the same numerical class when the properness criterion applies, and the limit retains ideal-theoretic information—such as infinitesimal or embedded structure—that cycle data can discard.

The scheme structure of \(H\), rather than only its closed points, is also essential. For a closed subscheme \(Z\subset X\) over a field with ideal sheaf \(\mathcal I_Z\), its first-order embedded deformations are the tangent vectors at \([Z]\), canonically described by
\[
T_{[Z]}H\cong \operatorname{Hom}_{\mathcal O_X}(\mathcal I_Z,\mathcal O_Z).
\]
Thus collisions, degenerations, and infinitesimal motions become local geometric questions about \(H\). The direct achievement is not simply that subschemes can be listed, but that their variation, specialization, and infinitesimal deformation are unified in one algebraic object through flatness, representability, and the universal family.

## 3. Notes

The Hilbert scheme is an embedded fine moduli space: it classifies subschemes inside the chosen ambient \(X\), not abstract schemes up to isomorphism, and it does not quotient by automorphisms of \(X\). The fixed Hilbert polynomial depends on the chosen relatively ample line bundle. Hilbert schemes can themselves be reducible, nonreduced, or singular; representability organizes the moduli problem but does not guarantee a smooth parameter space. The Hilbert scheme should also be distinguished from the Quot scheme, which parameterizes suitable flat quotients of a fixed coherent sheaf; the Hilbert functor is the special case arising from quotients of \(\mathcal O_X\) that are quotient algebras [2][3].

## 4. Sources

[1] Alexander Grothendieck, “Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert,” *Séminaire Bourbaki*, exp. 221, vol. 6 (1960–1961), pp. 249–276. https://www.numdam.org/item/SB_1960-1961__6__249_0/

[2] Nitin Nitsure, “Construction of Hilbert and Quot Schemes,” in Barbara Fantechi et al., *Fundamental Algebraic Geometry: Grothendieck's FGA Explained*, Mathematical Surveys and Monographs 123, American Mathematical Society, 2005, pp. 105–137; arXiv:math/0504590. https://arxiv.org/abs/math/0504590

[3] The Stacks Project Authors, “The Hilbert Functor” and “Properties of the Hilbert Functor,” Tags 0CZX and 0DM5. https://stacks.math.columbia.edu/tag/0CZX and https://stacks.math.columbia.edu/tag/0DM5
