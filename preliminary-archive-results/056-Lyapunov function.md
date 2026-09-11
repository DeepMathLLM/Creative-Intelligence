# Mathematical Object Origin Archive | Lyapunov Function

## 1. Archive Information

- Standard Name: Lyapunov function
- Mathematical Field: Dynamical Systems; Differential Equations
- Abstract: A Lyapunov function is an energy-like scalar function whose sign and monotonicity along trajectories certify the stability of an equilibrium or invariant set without requiring explicit solutions of the governing differential equation. It was formed within the problem of deciding stability of motion for nonlinear systems, where direct trajectory calculation is usually unavailable and linear approximation can be inconclusive.

## 2. Core Record

### Precise Description

Consider the autonomous system
\[
\dot x=f(x),\qquad x\in \mathbb R^n,
\]
where \(f\) is locally Lipschitz on an open set and \(x_e\) is an equilibrium, so \(f(x_e)=0\). A standard local Lyapunov function for \(x_e\) is a continuously differentiable function \(V:D\to\mathbb R\), defined on a neighborhood \(D\) of \(x_e\), such that
\[
V(x_e)=0,\qquad V(x)>0\quad (x\ne x_e),
\]
and whose orbital derivative
\[
\dot V(x)=\nabla V(x)\cdot f(x)
\]
is nonpositive. If \(\dot V(x)\le 0\) on \(D\), the standard Lyapunov theorem gives stability of \(x_e\), under these local hypotheses. If \(\dot V(x)<0\) for every \(x\ne x_e\) in \(D\), it gives local asymptotic stability [2]. For a global asymptotic-stability conclusion, one standard sufficient set of stronger assumptions is that the system and inequalities hold globally, \(V\) is positive definite and radially unbounded, and \(\dot V\) is negative definite.

The term has established variants: positive definiteness can be measured relative to an invariant set rather than a point; nonsmooth systems can use generalized derivatives; and the LaSalle invariance principle permits \(\dot V\le 0\) when the largest invariant subset of \(\{x:\dot V(x)=0\}\) is suitably small [3]. These are extensions of the same structural object, not part of its minimal local definition.

### Mathematical Context and Formation

The motivating problem is the stability-of-motion problem: given a differential system and a reference equilibrium or motion, decide whether every solution starting sufficiently close remains close, and whether it eventually approaches the reference state. For a nonlinear system this question concerns all nearby trajectories for all future time. Explicit integration is usually impossible. Linearization gives strong but incomplete information: for a \(C^1\) system, an equilibrium is locally asymptotically stable if every eigenvalue of the Jacobian has negative real part, and it is unstable if at least one eigenvalue has positive real part. The usual indirect test is generally inconclusive when no eigenvalue has positive real part but one or more have zero real part, because higher-order nonlinear terms can then determine the answer [2].

Lyapunov's direct method reframed this trajectory-wide problem by extracting the operative feature of conserved or dissipated mechanical energy without requiring the system itself to be mechanical [1]. Instead of solving for \(x(t)\), one seeks a scalar \(V(x)\) that measures displacement from the equilibrium through positive definiteness and has a controlled derivative along the vector field. The key formation step is the conjunction of two properties that neither an arbitrary norm nor a first integral supplies by itself: near the equilibrium, \(V\) has nested sublevel neighborhoods, and the sign of \(\nabla V\cdot f\) prevents trajectories from crossing their bounding level surfaces outward. An ordinary distance may increase along trajectories, while a conserved quantity alone need not have an isolated minimum; the Lyapunov conditions encode both geometry around the equilibrium and direction of evolution.

Thus the Lyapunov function arose as the central object of a direct stability test: a difficult quantification over unknown solutions is replaced by inequalities for one scalar function on state space. Finding such a function may itself be difficult, and failure to find one is not evidence of instability, but its existence supplies a certificate that can be checked without an explicit general solution [1,2].

### Essential Role

The object makes the forward-time control required in the definition of stability tractable. Let \(U\) be a prescribed neighborhood of \(x_e\). Choose \(r>0\) so that the closed ball \(\overline B_r(x_e)\) is contained in \(U\cap D\). By continuity and positive definiteness,
\[
\alpha=\min_{\lVert x-x_e\rVert=r}V(x)>0.
\]
Choose \(0<c<\alpha\), and then choose \(\delta>0\) so that \(\lVert x-x_e\rVert<\delta\) implies both \(x\in B_r(x_e)\) and \(V(x)<c\). If \(\dot V\le0\), then \(t\mapsto V(x(t))\) cannot increase. A trajectory starting in \(B_\delta(x_e)\) therefore cannot first leave \(B_r(x_e)\): at such a first exit its value of \(V\) would be at least \(\alpha>c\), contradicting monotonicity. The compact containment \(\overline B_r(x_e)\subset D\), together with the local existence and continuation theorem, ensures that this local confinement argument applies for all forward time. This converts the requirement that every sufficiently nearby trajectory remain nearby into a boundary estimate for a scalar function.

When \(\dot V<0\) away from \(x_e\), the same structure adds strict dissipation: \(V(x(t))\) decreases whenever the state is not the equilibrium, and the local asymptotic-stability theorem then yields convergence to \(x_e\) as well as confinement [2]. When strict decrease is unavailable, LaSalle's principle identifies the remaining obstruction as the invariant dynamics inside the zero-derivative set [3]. The defining features of \(V\)—a strict minimum at the reference state, enclosing local level surfaces, and monotonicity along the vector field—therefore overcome, respectively, the lack of a suitable scalar measure of displacement, the need to solve individual trajectories, and the inconclusiveness of linearization in its critical spectral cases.

The deeper structural viewpoint is that stability can be witnessed by an order-like scalar certificate on state space. The nonlinear dynamical question is not eliminated but reformulated as the construction and verification of inequalities for \(V\), allowing energy arguments to apply to systems for which no physical energy or closed-form solution exists.

## 3. Notes

A Lyapunov function should not be confused with a Lyapunov exponent. The former is a scalar function on state space used to certify stability; the latter measures asymptotic rates of growth of infinitesimal perturbations along a trajectory. Lyapunov functions are not unique, and several sign conventions occur in the literature (for example, using a function with a strict maximum and nonnegative orbital derivative). The positive-function/nonpositive-derivative convention is used here.

## 4. Sources

[1] A. M. Lyapunov, *The General Problem of the Stability of Motion* (1892), English translation, Taylor & Francis, 1992.

[2] Hassan K. Khalil, *Nonlinear Systems*, 3rd ed., Prentice Hall, 2002, Chapter 4.

[3] Joseph P. LaSalle and Solomon Lefschetz, *Stability by Liapunov's Direct Method with Applications*, Academic Press, 1961.
