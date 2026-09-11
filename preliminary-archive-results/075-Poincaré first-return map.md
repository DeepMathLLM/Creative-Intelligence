# Mathematical Object Origin Archive | Poincaré First-Return Map

## 1. Archive Information

- Standard Name: Poincaré first-return map
- Mathematical Field: Dynamical Systems
- Abstract: The Poincaré first-return map records where trajectories of a continuous-time dynamical system next meet a hypersurface transverse to the flow. It was formed within the qualitative study of nonlinear differential equations and celestial mechanics, where the central problem was to determine periodic motions, their stability, and nearby asymptotic behavior without explicitly integrating the equations. By turning a periodic orbit into a fixed point of a lower-dimensional discrete map and suppressing the dynamically neutral direction along the flow, it made recurrence and transverse stability accessible to fixed-point, linearization, and iteration methods.

## 2. Core Record

### Precise Description

Let \(M\) be a smooth \(n\)-manifold, let \(X\) be a \(C^r\) vector field with local flow \(\varphi^t\), and let \(\gamma\) be a periodic orbit of least period \(T>0\). Choose \(p\in\gamma\) and a local embedded codimension-one submanifold \(\Sigma\subset M\) through \(p\) such that
\[
X(p)\notin T_p\Sigma.
\]
Thus \(\Sigma\) is transverse to the flow at \(p\). After shrinking \(\Sigma\) to a neighborhood \(U\) of \(p\), transversality and the implicit-function theorem give a return-time function \(\tau:U\to(0,\infty)\), with \(\tau(p)=T\), for which \(\varphi^{\tau(x)}(x)\in\Sigma\). The local Poincaré first-return map is
\[
P:U\longrightarrow\Sigma,
\qquad
P(x)=\varphi^{\tau(x)}(x).
\]
For sufficiently small \(U\), this is the next relevant transverse crossing and \(P\) is a local \(C^r\) diffeomorphism onto its image [2,3]. More globally, a first-return map may be defined only on those points of a cross-section that return; its domain need not be all of \(\Sigma\), and its return time may be unbounded.

The defining correspondences are
\[
p=P(p) \quad\Longleftrightarrow\quad \gamma\text{ is periodic through }p,
\]
and, subject to the orbit remaining in the return domain,
\[
P^k(x)=x \quad\Longleftrightarrow\quad x\text{ lies on an orbit closing after }k\text{ successive section crossings}.
\]
The derivative
\[
DP(p):T_p\Sigma\to T_p\Sigma
\]
measures displacement transverse to \(\gamma\). Its eigenvalues are the nontrivial characteristic, or Floquet, multipliers of the periodic orbit: the automatic multiplier \(1\) arising from time translation along an autonomous orbit has been removed by passage to the transverse section. In particular, if every eigenvalue of \(DP(p)\) has modulus less than \(1\), the periodic orbit is locally asymptotically stable modulo phase; if an eigenvalue has modulus greater than \(1\), it is unstable. Unit-modulus multipliers generally require nonlinear analysis [2,3].

### Mathematical Context and Formation

The motivating problem class was the qualitative analysis of nonlinear ordinary differential equations, especially the gravitational few-body equations studied in celestial mechanics: determine whether periodic motions exist, whether nearby motions remain close to them, and how trajectories recur or approach and depart from an unstable periodic motion. In the restricted three-body problem, even after using conserved quantities and reducing symmetries, one confronts a nonlinear continuous flow for which general trajectories cannot be expressed by elementary or globally convergent formulas. The desired conclusions are long-time and geometric, whereas a finite segment of an explicit approximation does not by itself decide recurrence or orbital stability [1,4].

Several features made the problem resistant to methods designed for equilibria or exactly integrable systems. A periodic solution is not a stationary point in phase space but an entire closed curve. Comparing nearby solutions at equal clock times mixes two effects: genuine displacement away from the orbit and harmless displacement in phase along it. Correspondingly, the variational equation around an autonomous periodic orbit always contains a neutral direction tangent to the orbit. First integrals restrict motion to an energy surface, but they do not ordinarily say where an orbit returns after one revolution, whether it closes, or whether repeated passages drift toward or away from a given periodic motion. Direct integration also retains the full dimension and continuous time even though the questions concern what changes from one recurrence to the next.

The formative insight was to compare trajectories only when they cross a suitably chosen transverse section. The flow itself then determines both the next crossing and the elapsed return time. This replaces an orbit segment by its endpoint on \(\Sigma\), converts repeated revolutions into iterates
\[
x,\;P(x),\;P^2(x),\ldots,
\]
and lowers the state-space dimension by one. Most importantly, transversality separates the direction of evolution from the directions in which neighboring orbits genuinely diverge. A closed trajectory becomes a fixed or periodic point rather than a moving curve. Poincaré's qualitative program for differential equations and his study of periodic and asymptotic solutions in celestial mechanics supplied this construction's original mathematical setting [1]. The archive's claim is not that every modern formulation already appeared in present notation, but that the return construction crystallizes the mathematical response developed there: replace unavailable global integration by the iteration of a section map encoding successive passages.

### Essential Role

The first-return map made three precise parts of the motivating problem tractable.

First, it reformulated the search for periodic motions as a fixed-point problem. Instead of solving the differential equation together with an unknown closing time and phase condition, one chooses initial data on \(\Sigma\) and solves
\[
P(x)-x=0,
\]
or \(P^k(x)-x=0\) for an orbit with several crossings. The return-time function restores the physical period afterward. This formulation removes the continuous phase ambiguity and permits local fixed-point and continuation arguments to be applied to periodic solutions [2,4].

Second, it isolated orbital stability. Linearizing the full flow around a closed orbit includes the uninformative tangent multiplier caused by shifting the starting time. Because \(DP(p)\) acts only in directions tangent to the transverse section, its multipliers record the growth or decay that matters for separation from the orbit. Thus the long-time question “do nearby trajectories remain near this closed motion after many revolutions?” becomes the discrete question “do iterates of \(P\) remain near its fixed point?” Hyperbolic contraction and expansion can then be detected from \(DP(p)\), while stable and unstable sets of the periodic orbit appear on the section as invariant sets of the fixed point.

Third, the map exposed recurrent geometry that formulas for isolated trajectory arcs concealed. Intersections of stable and unstable manifolds with a section become lower-dimensional curves or submanifolds whose successive images can be compared. In the restricted three-body setting, after fixing an energy and taking an appropriate section, repeated orbital passages can in important regimes be represented by iterations of a two-dimensional return map; periodic motions become periodic points, while asymptotic and homoclinic behavior becomes the geometry of invariant curves and their intersections [1,4]. The direct contribution is therefore not merely convenient visualization. The map replaces a continuous-time, phase-redundant recurrence problem by a lower-dimensional discrete dynamical system whose fixed points, derivatives, invariant sets, and iterates encode exactly the closing and transverse-stability data that were difficult to extract from the original equations.

## 3. Notes

A Poincaré first-return map is distinct from a time-\(T\), or stroboscopic, map. The former advances each point by its own hitting time \(\tau(x)\); the latter advances every point by the same prescribed time. For a periodically forced nonautonomous system, adjoining the forcing phase can turn stroboscopic sampling into a section construction, but the two definitions should not be conflated.

Different transverse sections through the same periodic orbit produce locally conjugate return dynamics after points are transported along nearby flow lines. Hence coordinates and return times depend on the section, whereas the local transverse dynamical information, including characteristic multipliers up to the usual identification, does not. The construction is local unless a global cross-section and return for all relevant points have separately been established.

## 4. Sources

[1] Henri Poincaré, *Les méthodes nouvelles de la mécanique céleste*, 3 vols., Gauthier-Villars, Paris, 1892–1899.

[2] Morris W. Hirsch, Stephen Smale, and Robert L. Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos*, 3rd ed., Academic Press, 2013.

[3] Anatole Katok and Boris Hasselblatt, *Introduction to the Modern Theory of Dynamical Systems*, Cambridge University Press, 1995.

[4] Kenneth R. Meyer, Glen R. Hall, and Dan Offin, *Introduction to Hamiltonian Dynamical Systems and the N-Body Problem*, 2nd ed., Springer, 2009.
