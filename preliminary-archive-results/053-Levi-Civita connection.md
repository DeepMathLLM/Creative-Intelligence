# Mathematical Object Origin Archive | Levi-Civita Connection

## 1. Archive Information

- Standard Name: Levi-Civita connection
- Mathematical Field: Differential Geometry (Riemannian Geometry)
- Abstract: The Levi-Civita connection is the unique affine connection determined by a Riemannian metric that is both metric-compatible and torsion-free. It supplies the intrinsic differentiation and parallel transport needed to compare tangent vectors at nearby points of a curved manifold without introducing geometric data beyond the metric.

## 2. Core Record

### Precise Description

Let \((M,g)\) be a smooth Riemannian manifold. Its Levi-Civita connection is the map
\[
\nabla:\Gamma(TM)\times\Gamma(TM)\longrightarrow\Gamma(TM),
\qquad (X,Y)\longmapsto \nabla_XY,
\]
which is \(C^\infty(M)\)-linear in \(X\), \(\mathbb R\)-linear in \(Y\), and satisfies
\[
\nabla_X(fY)=X(f)Y+f\nabla_XY.
\]
It is characterized by two additional conditions:
\[
X\bigl(g(Y,Z)\bigr)=g(\nabla_XY,Z)+g(Y,\nabla_XZ)
\tag{metric compatibility}
\]
and
\[
\nabla_XY-\nabla_YX=[X,Y].
\tag{zero torsion}
\]
The fundamental theorem of Riemannian geometry states that exactly one such connection exists [1,2]. Equivalently, it is determined by the Koszul formula
\[
\begin{aligned}
2g(\nabla_XY,Z)={}&Xg(Y,Z)+Yg(Z,X)-Zg(X,Y)\\
&-g(X,[Y,Z])+g(Y,[Z,X])+g(Z,[X,Y]).
\end{aligned}
\]
Because \(g\) is nondegenerate, the right-hand side determines \(\nabla_XY\) uniquely. In local coordinates, its coefficients are
\[
\Gamma^k_{ij}=\frac12 g^{k\ell}
\left(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}\right),
\qquad
\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k.
\]
For a pseudo-Riemannian metric the same characterization and formulas apply, since nondegeneracy, rather than positive definiteness, is what the construction uses [1].

### Mathematical Context and Formation

The motivating problem was to define parallelism and differentiation intrinsically on a Riemannian manifold [3]. In Euclidean space, tangent vectors based at different points may be regarded as elements of one fixed vector space, so a vector field can be differentiated by subtracting its values at nearby points. On a manifold, however, \(Y(p)\in T_pM\) and \(Y(q)\in T_qM\) lie in different vector spaces. Their difference has no coordinate-independent meaning. Differentiating the coordinate components of \(Y\) does not solve the problem: under a nonlinear coordinate change, the resulting first derivatives acquire inhomogeneous terms and therefore do not transform as the components of a tensor.

A Riemannian metric resolves only the pointwise part of this difficulty. It assigns lengths and angles inside each \(T_pM\), but by itself a pointwise inner product is not yet a rule for comparing vectors in distinct tangent spaces. Conversely, one can impose many affine connections on the same smooth manifold, but an arbitrary one adds choices not determined by the Riemannian geometry and may fail to preserve the metric. Thus the precise problem was to extract from \(g\) a canonical correction to coordinate differentiation that has the Euclidean properties needed for geometric comparison.

Two requirements isolate that correction. Metric compatibility demands that differentiation obey the usual product rule for inner products; consequently, parallel vector fields retain their inner products. Zero torsion requires the antisymmetric part of covariant differentiation to agree with the intrinsic Lie bracket, as ordinary differentiation does in Euclidean coordinates. Applying metric compatibility to the three cyclic arrangements of \(X,Y,Z\), and using the torsion identity to eliminate reversed derivatives, yields the Koszul formula. The formula both constructs the connection from the first derivatives of \(g\) and proves that no second choice can satisfy the same requirements. In coordinates, this construction produces the Christoffel correction terms displayed above; their non-tensorial transformation exactly compensates for the non-tensorial part of differentiating vector components [1,2]. Levi-Civita's formulation of parallelism gave this comparison rule its geometric interpretation [3].

### Essential Role

The Levi-Civita connection makes the previously undefined comparison of nearby tangent vectors into an invariant operation. Along a smooth curve \(\gamma\), it defines the covariant derivative \(D V/dt=\nabla_{\dot\gamma}V\). The equation
\[
\frac{DV}{dt}=0
\]
therefore defines parallel transport without choosing an ambient Euclidean space or a preferred coordinate chart. Metric compatibility gives the decisive control
\[
\frac{d}{dt}g(V,W)
=g\!\left(\frac{DV}{dt},W\right)
+g\!\left(V,\frac{DW}{dt}\right),
\]
so parallel transport preserves lengths and angles. The connection is not merely one possible comparison rule: torsion-freeness together with metric compatibility makes it the unique rule determined by \(g\).

The same mechanism turns the geometric notion of a locally straight path into the intrinsic differential equation
\[
\nabla_{\dot\gamma}\dot\gamma=0,
\]
or, in coordinates,
\[
\ddot x^k+\Gamma^k_{ij}\dot x^i\dot x^j=0.
\]
Thus the obstacle of subtracting velocities in different tangent spaces is bypassed by covariantly differentiating them. Zero torsion also ensures that the Hessian \(\nabla df\) of a smooth function is symmetric. More structurally, the curvature operator
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z
\]
measures the failure of this metric-determined parallel transport to be path-independent. This reframes Riemannian curvature from coordinate expressions into an obstruction intrinsic to the canonical comparison rule. Geodesics and curvature are therefore not generic later applications appended to the object: they express the direct geometric content of the differentiation and parallelism problem that the Levi-Civita connection resolves [1-3].

## 3. Notes

An affine connection is extra data on a smooth manifold; the term “Levi-Civita connection” is reserved for the unique connection selected by a specified Riemannian or pseudo-Riemannian metric. Its Christoffel symbols are coordinate-dependent and are not themselves tensor components, although the covariant derivative and curvature formed from the connection are coordinate-independent. Parallel transport is generally path-dependent; metric compatibility guarantees that each transport map is an isometry between the tangent spaces along that path, not that transport is independent of the chosen path.

## 4. Sources

[1] John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Graduate Texts in Mathematics 176, Springer, 2018, especially Chapters 4–5.

[2] Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992, Chapter 2.

[3] Tullio Levi-Civita, “Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura Riemanniana,” *Rendiconti del Circolo Matematico di Palermo* 42 (1917), 173–205.
