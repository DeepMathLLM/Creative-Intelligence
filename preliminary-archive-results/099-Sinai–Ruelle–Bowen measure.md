# Mathematical Object Origin Archive | Sinai–Ruelle–Bowen Measure

## 1. Archive Information

- Standard Name: Sinai–Ruelle–Bowen measure (SRB measure)
- Mathematical Field: Ergodic Theory and Dynamical Systems
- Abstract: An SRB measure is an invariant probability measure whose conditional measures in dynamically expanding directions are absolutely continuous with respect to Riemannian leaf volume. It was formed to solve the natural-measure problem for dissipative hyperbolic dynamics: to identify the invariant distribution governing long-time observations from volume-typical initial conditions even when the distribution is singular in the ambient phase space.

## 2. Core Record

### Precise Description

Let \(f:M\to M\) be a \(C^2\) diffeomorphism of a compact Riemannian manifold, and let \(\mu\) be an \(f\)-invariant Borel probability measure. In a standard modern convention, \(\mu\) is an **SRB measure** if \((f,\mu)\) has at least one positive Lyapunov exponent at \(\mu\)-almost every point and, for every measurable partition \(\xi\) subordinate to the corresponding unstable manifolds \(W^u(x)\), its Rokhlin conditional measures satisfy
\[
\mu_x^\xi\ll m_x^u
\quad\text{for }\mu\text{-almost every }x,
\]
where \(m_x^u\) is the Riemannian volume induced on the unstable leaf containing \(\xi(x)\) [1]. Thus \(\mu\) need not be absolutely continuous on \(M\); its volume compatibility is required only along directions that expand under forward iteration.

The model case that generated the object is a nontrivial irreducible Axiom A attractor \(\Lambda\) of a \(C^2\) diffeomorphism. There the hyperbolic splitting
\[
T_\Lambda M=E^s\oplus E^u
\]
provides stable and unstable manifolds. The unique SRB measure supported on \(\Lambda\) is equivalently the Gibbs equilibrium state for the unstable potential
\[
\varphi^u(x)=-\log J^u f(x),
\qquad
J^u f(x)=\left|\det\!\left(Df_x\big|_{E_x^u}\right)\right|,
\]
and it satisfies the entropy formula
\[
h_\mu(f)=\int_\Lambda \log J^u f\,d\mu.
\]
Its conditional measures on local unstable plaques are not only absolutely continuous but equivalent to unstable-leaf volume, with strictly positive Gibbs densities. For an irreducible attractor, these characterizations agree with the statistical one: if \(U\) is a trapping neighborhood in the basin, then for Lebesgue-almost every \(x\in U\) and every continuous observable \(g\),
\[
\frac1n\sum_{k=0}^{n-1}g(f^k x)\longrightarrow \int_\Lambda g\,d\mu
\]
[1,3,4].

### Mathematical Context and Formation

The motivating problem was concrete: given a smooth dissipative system with a hyperbolic attractor, determine one invariant probability measure that predicts the asymptotic statistics observed from Riemannian-volume-typical initial states in the attractor's basin. Merely proving that invariant measures exist did not solve this selection problem. A hyperbolic attractor supports many invariant measures, including measures on periodic orbits. Birkhoff's theorem describes time averages only after a measure has already been selected, and only for points typical with respect to that measure; it therefore does not identify which measure, if any, is seen by ambient-volume-typical initial conditions.

For the dissipative systems at issue, ambient Riemannian volume \(m\) is not invariant: in differential terms, the total Jacobian \(|\det Df|\) does not satisfy the volume-preservation condition (and in strongly dissipative examples produces net volume contraction). Stable contraction by itself would not imply this, because unstable expansion can compensate it in the total Jacobian. On a proper attractor, forward dynamics can consequently concentrate initially smooth mass onto a set of zero ambient volume, so the desired invariant distribution may be singular on \(M\); global absolute continuity is therefore too strong.

Hyperbolicity nevertheless separates transverse attraction from forward instability: mass contracts toward the attractor along \(E^s\) while being stretched along \(E^u\). The decisive reformulation was to retain absolute continuity only in the unstable directions. Markov partitions encode hyperbolic orbits symbolically, and Gibbs-state methods compensate expansion by the potential \(-\log J^u f\); geometrically, the resulting measure has conditional measures equivalent to Riemannian volume on unstable leaves [1–4]. This synthesis is the SRB measure.

### Essential Role

For an irreducible Axiom A attractor, the SRB condition makes the unresolved selection step tractable: it singles out a unique invariant probability measure and identifies it with the limit statistics of Lebesgue-almost every initial point in a trapping neighborhood [1]. Its structure is fitted to the obstruction. It permits singular concentration transverse to unstable leaves, as attraction may require, while excluding singular concentration along unstable leaves, where initially smooth ensembles are stretched. The factor \(J^u f\) records exactly that stretching, so the Gibbs weight for \(-\log J^u f\) compensates unequal unstable expansion and yields coherent invariant statistics [2–4].

The passage from this leafwise property to ambient observations uses more than positive leaf measure. Birkhoff's theorem first gives a \(\mu\)-full set of generic points. Disintegration, together with equivalence of the Axiom A SRB conditionals and unstable-leaf volume with positive densities, makes this a full leaf-volume set on the relevant local unstable plaques. Points on the same local stable manifold have asymptotically indistinguishable forward observables; stable saturation therefore preserves the limiting statistics. Absolute continuity of the stable foliation transfers the full leaf-volume statement to full Riemannian volume in local basin product sets, and the trapping/basin-covering argument using forward iterates extends it to a full-volume subset of \(U\) [1,3,4]. Thus the object bypasses the absence of invariant ambient volume without replacing the question by an arbitrary invariant measure. It introduces the structural viewpoint that a natural statistical state in dissipative chaos may be smooth in expanding directions and singular in transverse contracting directions.

## 3. Notes

Terminology outside uniformly hyperbolic attractors is not completely uniform. This archive uses the leafwise absolute-continuity convention in [1]. A **physical measure** is instead defined by having a positive-ambient-volume basin of points whose empirical measures converge to it. Under the irreducible Axiom A hypotheses above, the SRB measure is physical and its basin has full volume in a trapping neighborhood, but the two terms should not be identified without additional hypotheses in more general systems. An attracting periodic orbit, for example, is physical while being excluded by the positive-Lyapunov-exponent convention used here.

## 4. Sources

[1] Lai-Sang Young, “What Are SRB Measures, and Which Dynamical Systems Have Them?”, *Journal of Statistical Physics* **108** (2002), 733–754. https://cims.nyu.edu/~lsy/papers/SRBsurvey.pdf

[2] Ya. G. Sinai, “Gibbs Measures in Ergodic Theory,” *Russian Mathematical Surveys* **27**:4 (1972), 21–69.

[3] Rufus Bowen and David Ruelle, “The Ergodic Theory of Axiom A Flows,” *Inventiones Mathematicae* **29** (1975), 181–202.

[4] David Ruelle, “A Measure Associated with Axiom-A Attractors,” *American Journal of Mathematics* **98**:3 (1976), 619–654.
