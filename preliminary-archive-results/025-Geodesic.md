# Mathematical Object Origin Archive | Geodesic

## 1. Archive Information

- Standard Name: Geodesic
- Mathematical Field: Differential Geometry
- Abstract: A geodesic is an intrinsically straight curve on a manifold with a connection; on a Riemannian manifold it is characterized by zero covariant acceleration and, equivalently for constant-speed parametrizations, by stationarity of the energy under fixed-endpoint variations. The object resolves the problem of replacing Euclidean straight line segments when distance and motion are studied on curved spaces, where ordinary coordinate acceleration is not invariant.

## 2. Core Record

### Precise Description

Let \(M\) be a smooth manifold equipped with an affine connection \(\nabla\). A smooth curve \(\gamma:I\to M\) is an *affinely parametrized geodesic* if
\[
\nabla_{\dot\gamma}\dot\gamma=0.
\]
In local coordinates \((x^1,\ldots,x^n)\), this condition is the system
\[
\frac{d^2\gamma^k}{dt^2}+\Gamma^k_{ij}(\gamma(t))
\frac{d\gamma^i}{dt}\frac{d\gamma^j}{dt}=0,
\qquad k=1,\ldots,n,
\]
where \(\Gamma^k_{ij}\) are the connection coefficients. Although the individual coefficients and coordinate second derivatives depend on coordinates, their combination in this equation expresses the invariant condition above [1,2]. A reparametrized curve is commonly called an unparametrized geodesic when it admits an affine parametrization satisfying this equation.

If \((M,g)\) is Riemannian and \(\nabla\) is its Levi-Civita connection, a geodesic has constant speed because
\[
\frac{d}{dt}g(\dot\gamma,\dot\gamma)
=2g(\nabla_{\dot\gamma}\dot\gamma,\dot\gamma)=0.
\]
For a piecewise smooth curve, define length and energy by
\[
L(\gamma)=\int_a^b\|\dot\gamma(t)\|_g\,dt,
\qquad
E(\gamma)=\frac12\int_a^b\|\dot\gamma(t)\|_g^2\,dt.
\]
The first-variation formula shows that a smooth curve is a critical point of \(E\) among smooth fixed-endpoint variations exactly when it is a geodesic. A nonconstant constant-speed curve is stationary for \(L\) under fixed-endpoint variations exactly when its image is geodesic, with the usual qualification that length is invariant under reparametrization [1,3]. Every sufficiently short geodesic segment minimizes length between its endpoints, but a geodesic need not minimize globally and can cease to minimize after phenomena such as a cut point [1,3].

### Mathematical Context and Formation

The motivating problem class is intrinsic shortest-path and free-motion problems on a curved surface or, more generally, a Riemannian manifold: given points \(p,q\in M\), one seeks curves joining them with least length, and one needs a local equation that candidate minimizers must satisfy. In Euclidean space the answer is a straight segment \(\gamma(t)=p+t(q-p)\), equivalently a curve with \(\ddot\gamma=0\). Neither formulation transfers directly to a manifold. Points of a general manifold cannot be subtracted, tangent vectors based at different points do not belong to one vector space without additional structure, and the coordinate condition \(d^2\gamma^k/dt^2=0\) is destroyed by nonlinear changes of coordinates. Thus ordinary straightness and ordinary acceleration are inadequate precisely where the geometry is curved.

The Riemannian metric supplies an intrinsic length functional, so the shortest-path question can be posed without embedding the manifold in Euclidean space. Merely defining length, however, does not give a differential equation for its minimizers. Varying a candidate curve through curves with the same endpoints and computing the first variation converts the global optimization question into a local stationarity condition. The resulting Euler–Lagrange expression is not the raw coordinate acceleration but
\[
\ddot\gamma^k+\Gamma^k_{ij}\dot\gamma^i\dot\gamma^j.
\]
The correction term compensates for the changing coordinate frame. The Levi-Civita connection packages that expression invariantly as \(\nabla_{\dot\gamma}\dot\gamma\). This leads to the geodesic: the curve whose tangent vector transports parallel to itself, or equivalently whose covariant acceleration vanishes [1,2].

This formation connects the two aspects of the problem rather than choosing between them. The variational construction identifies the curves forced on us by the least-length problem, while the connection formulation expresses their defining condition independently of coordinates and even continues to make sense for an affine connection without a metric. The geodesic is therefore the intrinsic replacement for a Euclidean straight line produced by reconciling metric minimization with coordinate-invariant differentiation.

### Essential Role

The geodesic makes the necessary local part of the shortest-path problem tractable. Instead of searching directly over the infinite-dimensional collection of all curves from \(p\) to \(q\), one first restricts candidate smooth minimizers to solutions of the finite-dimensional second-order geodesic equation. Given an initial point \(p\) and initial velocity \(v\in T_pM\), standard ordinary differential equation theory gives a unique local geodesic with \(\gamma(0)=p\) and \(\dot\gamma(0)=v\). The original endpoint problem is thereby reformulated as choosing an initial velocity whose geodesic reaches \(q\), rather than varying an arbitrary path [1,2].

The defining feature \(\nabla_{\dot\gamma}\dot\gamma=0\) overcomes the failure of coordinate acceleration by comparing tangent vectors through the connection. Its variational equivalence ensures that this invariant notion of straightness is not merely formal: it is exactly the Euler–Lagrange condition imposed by the metric energy, and constant speed connects energy stationarity to the length problem. In a normal neighborhood of \(p\), the geodesic determined by the appropriate initial vector is the unique radial geodesic to a nearby point and minimizes length there [1,3]. Thus the object supplies both a computable differential equation and the local minimizing curves sought by the motivating problem.

The limitation is mathematically essential. The geodesic condition is local and necessary for smooth length minimizers, not a guarantee of global minimality. Multiple geodesics may join the same endpoints, and a geodesic can lose minimizing status. Far from weakening the object, this distinction exposes the deeper structure of the original problem: local straightness is governed by the geodesic ODE, whereas global minimization additionally depends on the manifold's topology and on global metric phenomena such as cut and conjugate points [1,3].

## 3. Notes

- In a general affine manifold, a geodesic is defined by the connection even when no length functional exists; its direct variational interpretation above pertains to the Levi-Civita connection of a Riemannian metric.
- Some authors reserve “geodesic” for an affine parametrization and use “pregeodesic” for a curve that becomes geodesic after reparametrization.
- A geodesic should not be identified with an arbitrary globally shortest path. On a smooth Riemannian manifold, smooth minimizing segments are geodesic, while geodesics are guaranteed to minimize only under suitable local restrictions.

## 4. Sources

[1] Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992, Chapters 3 and 6.

[2] John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018, chapters on connections and geodesics.

[3] Peter Petersen, *Riemannian Geometry*, 3rd ed., Springer, 2016, chapters on geodesics, distance, and the first and second variation formulas.
