# Mathematical Object Origin Archive | Riemann Curvature Tensor

## 1. Archive Information

- Standard Name: Riemann curvature tensor
- Mathematical Field: Differential Geometry
- Abstract: The Riemann curvature tensor is the tensorial obstruction to commuting covariant derivatives for a Riemannian metric. It was formed to address the intrinsic local-equivalence problem: determine whether a metric can be transformed by coordinates into the Euclidean metric on a neighborhood, and, when it cannot, measure the failure without depending on the chosen coordinates. Its construction cancels the non-tensorial coordinate effects present in connection coefficients and packages the metric's intrinsic second-order geometry.

## 2. Core Record

### Precise Description

Let \((M,g)\) be a smooth Riemannian manifold, and let \(\nabla\) be the Levi-Civita connection of \(g\). With one standard sign convention, its curvature operator is
\[
R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z
\]
for smooth vector fields \(X,Y,Z\). Although each covariant derivative in this expression depends on derivatives of chosen extensions of the vectors, their indicated combination is \(C^\infty(M)\)-linear in \(X,Y,Z\). It therefore defines a tensor \(R\in\Gamma(\Lambda^2T^*M\otimes \operatorname{End}(TM))\). Lowering the output index gives the \((0,4)\)-tensor
\[
\operatorname{Rm}(X,Y,Z,W)=g(R(X,Y)Z,W).
\]
The opposite overall sign is also common; statements involving the sign of curvature must therefore declare a convention.

In local coordinates,
\[
R^{\ell}{}_{kij}
=\partial_i\Gamma^{\ell}_{jk}-\partial_j\Gamma^{\ell}_{ik}
 +\Gamma^{m}_{jk}\Gamma^{\ell}_{im}
 -\Gamma^{m}_{ik}\Gamma^{\ell}_{jm},
\]
for the convention above. For linearly independent \(u,v\in T_pM\), the associated sectional curvature is
\[
K(u,v)=\frac{g(R(u,v)v,u)}{g(u,u)g(v,v)-g(u,v)^2}.
\]
Thus \(R_p\) records curvature for every two-plane at \(p\); conversely, the sectional curvatures determine the full algebraic curvature tensor [1,2].

### Mathematical Context and Formation

The motivating problem is the local equivalence problem for Riemannian metrics: given \(g\), decide whether each point has a neighborhood with coordinates in which
\[
g=\sum_i (dx^i)^2,
\]
and, if not, identify an intrinsic local obstruction. Directly differentiating the matrix \((g_{ij})\) does not solve this problem. Its entries and ordinary derivatives change under a coordinate transformation. Normal coordinates can arrange \(g_{ij}(p)=\delta_{ij}\) and \(\partial_k g_{ij}(p)=0\) at one point even on a curved manifold, so first-order coordinate data cannot distinguish genuine local Euclidean geometry from a coordinate normalization. Christoffel symbols organize those first derivatives and the geodesic equation, but they too are not tensor components: they can vanish at a selected point without the geometry being flat there [1].

The remaining information is second order, but raw second derivatives of \(g_{ij}\) still contain coordinate artifacts. The decisive structural move is first to use the metric's canonical covariant derivative and then antisymmetrize its second covariant derivatives. In
\[
[\nabla_X,\nabla_Y]Z-\nabla_{[X,Y]}Z,
\]
the derivative-of-vector-field terms and the non-tensorial transformation terms cancel. What remains is pointwise and coordinate invariant. Equivalently, it measures the leading-order failure of parallel transport around an infinitesimal loop to return a vector unchanged. This cancellation turns precisely the otherwise ambiguous second-order metric information into the Riemann curvature tensor. For surfaces, the resulting tensor contains the same intrinsic curvature data as Gaussian curvature; the tensorial formulation is what extends the obstruction coherently to all dimensions and all tangent two-planes [1,2].

### Essential Role

The tensor makes the obstruction part of the local-equivalence problem tractable. If a metric is Euclidean in local coordinates, its Levi-Civita connection has zero curvature, so \(R=0\). Conversely, if \(R\) vanishes identically on a sufficiently small neighborhood, parallel transport there is path independent; a parallel orthonormal frame can be constructed and integrated to local Euclidean coordinates. Hence a Riemannian manifold is locally flat exactly when its Riemann curvature tensor vanishes locally [1,2]. Vanishing merely at one point is weaker: it removes the intrinsic second-order obstruction at that point but does not imply flatness on a neighborhood.

More generally, \(R\) replaces the impossible demand to compare coordinate coefficients directly by invariant tests on tangent vectors and two-planes. Its multilinearity permits pointwise comparison, while its commutator definition identifies the precise failure of covariant derivatives to commute. Its contractions and evaluations provide computable consequences, but the direct mechanism is already present in \(R\) itself: it controls infinitesimal holonomy and the relative acceleration of neighboring geodesics. For a geodesic with tangent \(T\), a variation field \(J\) satisfies the Jacobi equation
\[
\nabla_T\nabla_TJ+R(J,T)T=0,
\]
with the stated sign convention. Thus the same object that detects failure of local Euclidean coordinates also converts that failure into a linear differential equation describing how nearby geodesics converge or separate [2]. The deeper viewpoint introduced is that curvature is not a defect of an embedding or of a coordinate picture; it is intrinsic second-order information encoded by the metric through its connection.

## 3. Notes

The Riemann curvature tensor is distinct from the Ricci tensor and scalar curvature, which are contractions and therefore discard information in dimensions at least four. It is also distinct from the Weyl tensor, the trace-free conformal part of curvature. In dimension two, \(\operatorname{Rm}\) is determined by one scalar, the Gaussian curvature; in dimension three it is determined algebraically by the Ricci tensor, while in higher dimensions the Ricci tensor generally does not determine it [1,2]. The construction extends to any affine connection, but this archive concerns the curvature tensor of the Levi-Civita connection associated with a Riemannian metric.

## 4. Sources

[1] Manfredo P. do Carmo, *Riemannian Geometry*, translated by Francis Flaherty, Birkhäuser, 1992, Chapters 3–4.

[2] John M. Lee, *Riemannian Manifolds: An Introduction to Curvature*, Springer, 1997, Chapters 7–8.
