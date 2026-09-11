# Mathematical Object Origin Archive | Khovanov–Rozansky sl(n) link homology

## 1. Archive Information

- Standard Name: Khovanov–Rozansky sl(n) link homology
- Mathematical Field: Knot Theory and Low-Dimensional Topology; Representation Theory
- Abstract: Khovanov–Rozansky \(\mathfrak{sl}_n\) link homology is a bigraded link invariant whose graded Euler characteristic is the quantum \(\mathfrak{sl}_n\) polynomial, the one-variable specialization of the HOMFLY polynomial associated with the defining representation of \(\mathfrak{sl}_n\). It was formed to solve the categorification problem for these polynomials uniformly in \(n\). Its defining mechanism replaces scalar evaluations of resolved diagrams by graded matrix factorizations of the potential \(x^{n+1}\), so that local pieces can be glued, crossing relations can be lifted to chain maps, and Reidemeister invariance can be proved at chain level [1].

## 2. Core Record

### Precise Description

Fix an integer \(n\ge 2\) and a coefficient field such as \(\mathbb{Q}\). For an oriented link \(L\), Khovanov–Rozansky \(\mathfrak{sl}_n\) link homology is an isomorphism class of finite-dimensional bigraded vector spaces
\[
H_n(L)=\bigoplus_{i,j}H_n^{i,j}(L),
\]
where \(i\) is a homological grading and \(j\) is an internal, or quantum, grading. With the grading shifts and polynomial normalization fixed as in the construction, it satisfies
\[
\sum_{i,j}(-1)^i q^j\dim_{\mathbb Q}H_n^{i,j}(L)=P_n(L),
\]
where \(P_n(L)\) is the quantum \(\mathfrak{sl}_n\) specialization of the HOMFLY polynomial [1].

The chain model is built locally from matrix factorizations. If \(R\) is a graded polynomial ring and \(w\in R\), a matrix factorization of \(w\) is a \(\mathbb Z/2\)-graded free \(R\)-module \(M=M^0\oplus M^1\) with odd maps \(d_0:M^0\to M^1\) and \(d_1:M^1\to M^0\) satisfying
\[
d_1d_0=w\,\mathrm{id}_{M^0},\qquad d_0d_1=w\,\mathrm{id}_{M^1}.
\]
To an oriented resolved diagram or planar web \(\Gamma\), with variables on boundary edges, the construction assigns a graded matrix factorization whose potential has the form
\[
w_\Gamma=\sum_{e\,\mathrm{out}}x_e^{n+1}-\sum_{e\,\mathrm{in}}x_e^{n+1}.
\]
Potentials add under tensor-product gluing. For a closed web the boundary terms cancel, so \(w_\Gamma=0\) and the matrix-factorization differential becomes an actual differential.

At each crossing of a link diagram \(D\), the two local resolutions—an oriented smoothing and a singular or wide-edge resolution—give matrix factorizations connected by specified homogeneous morphisms. A positive crossing is replaced by a shifted two-term complex in one direction and a negative crossing by the corresponding complex in the reverse direction. Tensoring these local complexes over all crossings produces a complex \(C_n(D)\) of matrix factorizations. For a closed diagram, taking the matrix-factorization cohomology and then the cohomology of the crossing complex, with the prescribed normalization shifts, gives \(H_n(D)\). Homotopy equivalences associated with the Reidemeister moves imply that its bigraded isomorphism class depends only on \(L\), not on \(D\) [1].

### Mathematical Context and Formation

The motivating problem was to categorify the family of quantum \(\mathfrak{sl}_n\) link polynomials. A categorification had to do substantially more than reproduce a polynomial by a state sum: it had to assign a graded chain complex to a diagram, recover the polynomial as the complex's graded Euler characteristic, and make Reidemeister moves induce homotopy equivalences. Khovanov homology had achieved this for the Jones polynomial, corresponding to \(n=2\) [2]. The unresolved problem was to construct such homology theories for general \(n\) in a way compatible with the richer \(\mathfrak{sl}_n\) web calculus.

The polynomial-level \(\mathfrak{sl}_n\) invariant could be computed by resolving crossings into planar graphs and evaluating those graphs through local Murakami–Ohtsuki–Yamada relations [3]. That calculus supplied the right decategorified combinatorics but only scalar Laurent polynomials. Scalars do not provide chain groups, differentials, or homotopies, and a polynomial identity among web evaluations does not itself lift to the direct-sum decompositions and contractible summands needed for Reidemeister invariance. Moreover, the ordinary Frobenius-algebra model underlying the \(n=2\) theory did not by itself supply a uniform local object for the singular, wide-edge graphs appearing in the general \(\mathfrak{sl}_n\) resolutions.

The formative insight was to interpret each resolved web through the singularity potential \(x^{n+1}\) and use matrix factorizations as its chain-level linear algebra [1]. The Jacobi algebra of this potential is
\[
\mathbb Q[x]/(\partial_x x^{n+1})\cong \mathbb Q[x]/(x^n),
\]
up to the invertible scalar \(n+1\); its graded dimension matches the \(\mathfrak{sl}_n\) label carried by a circle after the conventional shift. More importantly, a matrix-factorization differential is allowed to square to a boundary potential rather than to zero. Thus an open local piece can carry nonzero potential, while signed boundary potentials cancel when pieces are glued into a closed diagram. This resolves the local-to-global obstruction: local web data remain composable before closure and become genuine complexes after closure. Morphisms between the factorizations of the two crossing resolutions then lift the crossing expansion from a polynomial equation to a two-term complex.

### Essential Role

Khovanov–Rozansky \(\mathfrak{sl}_n\) link homology made the chain-level categorification step tractable. Its matrix factorizations replace each scalar web evaluation by a homological object while preserving exactly the local behavior needed for the \(\mathfrak{sl}_n\) polynomial. The potential \(x^{n+1}\) records the chosen rank \(n\); the equation \(d^2=w\) permits local tangle pieces with boundary; additivity of potentials permits tensor-product gluing; and cancellation of boundary potentials turns a closed link diagram into a genuine differential object. The crossing morphisms organize the two resolutions into complexes whose Euler-characteristic relation is the polynomial crossing relation.

These features address the precise inadequacy of the polynomial state sum. Polynomial web relations become homotopy-theoretic statements—such as decompositions and cancellation of contractible summands—strong enough to compare complexes across Reidemeister moves [1]. Consequently, diagram independence and recovery of \(P_n\) are established within one chain-level framework rather than imposed after computing scalar evaluations.

The resulting object also reformulates what the polynomial records. The coefficient of \(q^j\) in \(P_n(L)\) is no longer merely a signed integer: it is the alternating sum of dimensions of the groups \(H_n^{i,j}(L)\). The extra homological grading and the groups themselves retain information erased by Euler characteristic. This is the deeper structural viewpoint introduced by the construction, but it follows directly from the motivating categorification mechanism rather than from a later application.

## 3. Notes

For \(n=2\), the theory recovers the Jones-polynomial categorification up to standard choices of normalization. The object archived here is the fixed-\(n\), bigraded \(\mathfrak{sl}_n\) theory of [1], not the triply graded HOMFLY-PT homology developed in related Khovanov–Rozansky work. Different conventions shift or rescale the quantum grading and normalize the link polynomial differently; the Euler-characteristic statement must be read with a consistent convention on both sides.

## 4. Sources

[1] Mikhail Khovanov and Lev Rozansky, “Matrix factorizations and link homology,” arXiv:math/0401268; published in *Fundamenta Mathematicae* 199 (2008), 1–91. https://arxiv.org/abs/math/0401268

[2] Mikhail Khovanov, “A categorification of the Jones polynomial,” *Duke Mathematical Journal* 101 (2000), 359–426. https://doi.org/10.1215/S0012-7094-00-10131-7

[3] Hitoshi Murakami, Tomotada Ohtsuki, and Shuji Yamada, “HOMFLY polynomial via an invariant of colored plane graphs,” *L'Enseignement Mathématique* 44 (1998), 325–360.
