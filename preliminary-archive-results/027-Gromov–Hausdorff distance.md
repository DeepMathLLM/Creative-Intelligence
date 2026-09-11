# Mathematical Object Origin Archive | Gromov–Hausdorff Distance

## 1. Archive Information

- Standard Name: Gromov–Hausdorff distance
- Mathematical Field: Differential Geometry; Metric Geometry
- Abstract: The Gromov–Hausdorff distance is a metric on isometry classes of compact metric spaces. It was formed to compare intrinsic metric spaces that are not presented as subsets of one fixed ambient space, thereby making convergence and compactness meaningful for varying Riemannian manifolds and for metric limits that may change topology or dimension.

## 2. Core Record

### Precise Description

For nonempty compact subsets \(A,B\) of a metric space \((Z,d_Z)\), their Hausdorff distance is
\[
d_H^Z(A,B)=\max\!\left\{
\sup_{a\in A}\inf_{b\in B}d_Z(a,b),
\sup_{b\in B}\inf_{a\in A}d_Z(a,b)
\right\}.
\]
If \((X,d_X)\) and \((Y,d_Y)\) are nonempty compact metric spaces, their Gromov–Hausdorff distance is
\[
d_{GH}(X,Y)=
\inf_{Z,\,\iota_X,\,\iota_Y}
d_H^Z\bigl(\iota_X(X),\iota_Y(Y)\bigr),
\]
where the infimum ranges over metric spaces \(Z\) and isometric embeddings \(\iota_X:X\to Z\) and \(\iota_Y:Y\to Z\). Equivalently, one may range over metrics on the disjoint union \(X\sqcup Y\) whose restrictions are \(d_X\) and \(d_Y\) [1,2].

A correspondence is a relation \(R\subseteq X\times Y\) whose projections onto both factors are surjective. Its distortion is
\[
\operatorname{dis}(R)=
\sup_{(x,y),(x',y')\in R}
\left|d_X(x,x')-d_Y(y,y')\right|.
\]
The intrinsic formula
\[
d_{GH}(X,Y)=\frac12\inf_R\operatorname{dis}(R)
\]
shows that no ambient space is actually needed for estimates [2]. On isometry classes of nonempty compact metric spaces, \(d_{GH}\) is a genuine metric: in particular, \(d_{GH}(X,Y)=0\) exactly when \(X\) and \(Y\) are isometric [1,2].

### Mathematical Context and Formation

The motivating problem class is compactness and convergence for varying Riemannian manifolds equipped with their intrinsic distance functions. A typical question begins with a sequence \((M_i,g_i)\) satisfying uniform geometric controls and asks whether a subsequence has a meaningful geometric limit. At the metric level, the relevant hypothesis can be stated as uniform total boundedness: the diameters are uniformly bounded and, for every \(\varepsilon>0\), each \(M_i\) has an \(\varepsilon\)-net with at most \(N(\varepsilon)\) points. The desired conclusion is convergence, after passage to a subsequence, to some compact metric space [1,2].

The difficulty is that \(M_i\) and \(M_j\) need not be subsets of a common space, and there may be no preferred map pairing their points. Hausdorff distance therefore cannot be applied directly, because it compares subsets only after an ambient metric has already supplied cross-distances. Smooth or \(C^k\) convergence is too rigid for this problem: it requires smooth identifications of manifolds of fixed dimension and does not accommodate collapsing sequences or singular metric limits. Conversely, choosing arbitrary coordinates, embeddings, or point maps would make the resulting comparison depend on auxiliary choices rather than on the intrinsic distances.

The formation of the Gromov–Hausdorff distance follows from isolating the common datum that survives these failures: each space's full distance function. One retains ordinary Hausdorff comparison but allows every possible common metric realization of the two spaces, requires each realization to preserve the original distances exactly, and then takes the least possible Hausdorff discrepancy. Optimization over common realizations removes dependence on a chosen ambient space. The correspondence formula expresses the same insight without embeddings: two spaces are close when their points can be related so that all pairwise distances differ by little. Thus approximate point identification is derived from the metrics rather than imposed beforehand.

### Essential Role

This object makes the compactness problem precise by putting all nonempty compact metric spaces, modulo isometry, into one metric space. A sequence of varying manifolds can therefore be Cauchy or convergent even though its terms have different underlying sets, and its limit is allowed to be a general compact metric space rather than a smooth manifold of the original dimension. The Gromov compactness criterion then states that a uniformly totally bounded family of compact metric spaces is relatively compact in the Gromov–Hausdorff topology [1,2]. This is the exact portion of the motivating problem made tractable: uniform finite-net control becomes a subsequential convergence statement in a topology independent of coordinates and ambient embeddings.

The definition's two principal features perform distinct jobs. Isometric embeddings protect each space's intrinsic geometry from alteration, while the infimum over all common ambient spaces eliminates irrelevant placement. Equivalently, low-distortion correspondences convert convergence into quantitative comparisons of finite distance data. Under a uniform bound on the size of \(\varepsilon\)-nets, one can pass to subsequences of finite approximations; the distortion formulation then promotes compatible approximations at successively smaller scales to a compact metric limit. The construction thereby bypasses the absence of canonical maps and reformulates possible changes of topology, dimension, or smoothness as ordinary convergence in a larger moduli space. Its deeper structural contribution is the viewpoint that a geometric space may itself be treated as a point, determined up to isometry by its internal distance relations.

## 3. Notes

The unpointed compact theory above is the basic object. Pointed Gromov–Hausdorff convergence is a related extension used for noncompact proper spaces and requires the basepoints, and usually bounded balls around them, to converge. Measured Gromov–Hausdorff variants add measures and are distinct objects. The Gromov–Hausdorff distance records metric geometry only; additional smooth, measure-theoretic, or algebraic structure is not preserved unless incorporated into a strengthened notion of convergence.

## 4. Sources

[1] M. Gromov, *Metric Structures for Riemannian and Non-Riemannian Spaces*, based on the 1981 French original, Progress in Mathematics 152, Birkhäuser, 1999, especially the discussion of Hausdorff distance and compactness for metric spaces.

[2] D. Burago, Y. Burago, and S. Ivanov, *A Course in Metric Geometry*, Graduate Studies in Mathematics 33, American Mathematical Society, 2001, Sections 7.3–7.4.
