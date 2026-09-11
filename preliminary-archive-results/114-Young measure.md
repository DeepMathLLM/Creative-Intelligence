# Mathematical Object Origin Archive | Young Measure

## 1. Archive Information

- Standard Name: Young measure
- Mathematical Field: Calculus of variations; nonlinear partial differential equations
- Abstract: A Young measure is a measurable family of probability measures used to retain the local value distribution of an oscillating sequence when ordinary weak convergence records only its average. It was formed in connection with the existence problem for minima of nonconvex variational integrals: by replacing an unresolved fine-scale choice of derivative values with a probability distribution over those values, one obtains generalized curves and relaxed limits on which nonlinear integrands have a meaningful limit.

## 2. Core Record

### Precise Description

Let \(\Omega\subset\mathbb R^n\) have finite measure and let \(K\) be a compact metric space, commonly a compact subset of \(\mathbb R^m\). A Young measure on \(\Omega\) with values in \(K\) is a family \(\nu=(\nu_x)_{x\in\Omega}\) of Borel probability measures on \(K\), defined for almost every \(x\), such that
\[
x\longmapsto \langle \nu_x,\varphi\rangle
:=\int_K\varphi(\lambda)\,d\nu_x(\lambda)
\]
is measurable for every \(\varphi\in C(K)\).

A sequence of measurable maps \((z_j)\), with \(z_j:\Omega\to K\), generates \(\nu\) if
\[
\varphi(z_j)\stackrel{*}{\rightharpoonup}
\langle\nu_x,\varphi\rangle
\quad\text{in }L^\infty(\Omega)
\]
along that full sequence for every \(\varphi\in C(K)\). Equivalently, for every \(a\in L^1(\Omega)\),
\[
\lim_{j\to\infty}\int_\Omega a(x)\varphi(z_j(x))\,dx
=
\int_\Omega a(x)\int_K\varphi(\lambda)\,d\nu_x(\lambda)\,dx.
\]
Separately, the compact-valued fundamental theorem ensures that any such sequence has a subsequence that generates a Young measure; once extracted, that subsequence may be relabeled as \((z_j)\) [2]. The barycenter
\[
\bar z(x)=\int_K\lambda\,d\nu_x(\lambda)
\]
recovers the ordinary weak limit when the identity is an admissible test, but the entire measure also retains oscillatory information lost by that limit. A Dirac family \(\nu_x=\delta_{z(x)}\) represents no residual oscillation; a non-Dirac measure represents mixing among several values.

### Mathematical Context and Formation

The motivating problem class is the existence of attained minima for nonconvex variational integrals, the setting of Young's generalized curves [1]. A concrete scalar model is
\[
\inf_{u\in W^{1,4}_0(0,1)} I[u],\qquad
I[u]=\int_0^1\bigl((u'(x)^2-1)^2+u(x)^2\bigr)\,dx.
\]
Piecewise-linear sawtooth functions can have slopes \(+1\) and \(-1\) on alternating intervals of length tending to zero while their amplitudes tend uniformly to zero. For such a sequence \(u_j\),
\[
u_j\to0,\qquad u_j'\rightharpoonup0,
\qquad (u_j'^2-1)^2=0\ \text{a.e.},
\]
so \(I[u_j]\to0\). Yet no ordinary admissible function attains zero: \(I[u]=0\) would force both \(u=0\) and \(|u'|=1\) almost everywhere, which is impossible. Thus the infimum is approached by ever finer oscillations rather than by a classical minimizer.

The exact obstruction is that weak compactness supplies only the average derivative. It sends the alternating derivatives to \(0\), while the nonconvex nonlinear expression does not follow that weak limit:
\[
(u_j'^2-1)^2=0,
\qquad
((0)^2-1)^2=1.
\]
Consequently the integral is not weakly lower semicontinuous, and the ordinary weak limit erases precisely the information needed to evaluate the limiting energy. Strong convergence would control the nonlinear expression, but the minimizing sequence has no strongly convergent derivative subsequence; simply enlarging the class by weak closure therefore does not preserve its energy.

The formative insight is to replace the limiting derivative at each base point by its local probability distribution. In the sawtooth example the derivative sequence generates
\[
\nu_x=\tfrac12\delta_{-1}+\tfrac12\delta_{1}
\quad\text{for a.e. }x.
\]
Its barycenter is \(0\), agreeing with the derivative of the uniform limit, while its nonlinear moment gives
\[
\int_{\mathbb R}(\lambda^2-1)^2\,d\nu_x(\lambda)=0.
\]
This simultaneous retention of the average constraint and the nonlinear energy is the mathematical mechanism behind the passage from ordinary curves to measure-valued generalized curves [1,3].

### Essential Role

The Young measure makes the missing compactness tractable by changing what is compactified. Rather than demanding that the oscillating values \(z_j(x)\) converge pointwise or strongly, it embeds each value as the Dirac mass \(\delta_{z_j(x)}\) and takes a weak limit in a space of parameterized probability measures. The limit can therefore be non-Dirac even when the underlying sequence has no strong limit.

For a continuous nonlinear density \(W\), the Young-measure limit records
\[
W(z_j)\rightharpoonup
\int_K W(\lambda)\,d\nu_x(\lambda),
\]
whereas the ordinary weak limit records at most the barycenter \(\bar z\) and would substitute \(W(\bar z)\). These are generally unequal for nonconvex \(W\). In the model problem, the relaxed pair
\[
u=0,
\qquad
\nu_x=\tfrac12\delta_{-1}+\tfrac12\delta_{1}
\]
attains generalized energy zero: the barycenter enforces the macroscopic derivative, and the support at the two wells \(\{-1,1\}\) preserves the zero microscopic energy. Thus the object does not manufacture an ordinary minimizer; it represents the limit of minimizing oscillations and turns nonattainment into attainment in a measure-valued relaxation.

The deeper structural change is that a weak limit is no longer treated as one effective state. It is decomposed into local states and their proportions, so nonlinear observables are computed by averaging the observable, \(\int W\,d\nu_x\), rather than by applying it after averaging, \(W(\int\lambda\,d\nu_x)\). This directly identifies oscillation as the source of the relaxation gap. In higher-dimensional problems where \(z_j=\nabla u_j\), not every parameterized measure is generated by gradients; gradient Young measures carry the additional differential constraints. Their characterization is part of the later developed variational framework [3].

## 3. Notes

Classical Young measures encode oscillation but, without augmentation, may fail to record concentration caused by unbounded or non-equiintegrable sequences; generalized Young measures add concentration data. A Young measure is also not automatically a measure-valued solution of a particular PDE: admissibility conditions inherited from that PDE or from the gradient structure must be imposed separately.

## 4. Sources

[1] L. C. Young, “Generalized curves and the existence of an attained absolute minimum in the calculus of variations,” *Comptes Rendus des Séances de la Société des Sciences et des Lettres de Varsovie, Classe III* **30** (1937), 212–234.

[2] J. M. Ball, “A version of the fundamental theorem for Young measures,” in *PDEs and Continuum Models of Phase Transitions*, Lecture Notes in Physics 344, Springer, 1989, pp. 207–215.

[3] P. Pedregal, *Parametrized Measures and Variational Principles*, Progress in Nonlinear Differential Equations and Their Applications 30, Birkhäuser, 1997.
