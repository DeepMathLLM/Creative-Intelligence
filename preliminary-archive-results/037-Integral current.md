# Mathematical Object Origin Archive | Integral Current

## 1. Archive Information

- Standard Name: Integral current
- Mathematical Field: Differential Geometry; Geometric Measure Theory
- Abstract: An integral current is an oriented, countably rectifiable generalized surface with integer multiplicity whose boundary has the same structure. Federer and Fleming isolated this class to make the oriented Plateau problem—minimizing area among surfaces with a prescribed boundary—amenable to the direct method of the calculus of variations: integral currents retain geometric and homological information, are closed under boundary, satisfy a compactness theorem under mass bounds, and have lower-semicontinuous mass.

## 2. Core Record

### Precise Description

Let $U\subset\mathbb{R}^n$ be open. A $k$-current on $U$ is a continuous linear functional on the space $\mathcal D^k(U)$ of smooth compactly supported $k$-forms. An integer-rectifiable $k$-current can be represented as
\[
T(\omega)=\int_M \langle \omega(x),\xi(x)\rangle\,\theta(x)\,d\mathcal H^k(x),
\]
where $M\subset U$ is countably $k$-rectifiable, $\xi(x)$ is a measurable unit simple $k$-vector orienting the approximate tangent $k$-plane of $M$ for $\mathcal H^k$-almost every $x$, and $\theta:M\to\mathbb Z$ is an integrable integer-valued multiplicity. Its boundary is the $(k-1)$-current
\[
\partial T(\eta)=T(d\eta).
\]
A finite-mass integral $k$-current is an integer-rectifiable $T$ of finite mass such that $\partial T$ is also integer-rectifiable and has finite mass. Its mass is
\[
\mathbf M(T)=\sup\bigl\{T(\omega):\omega\in\mathcal D^k(U),\ \|\omega(x)\|_*\le 1\bigr\},
\]
with $\|\cdot\|_*$ the comass; for the representation above, $\mathbf M(T)=\int_M |\theta|\,d\mathcal H^k$.

A compact oriented $C^1$ $k$-submanifold $S$ with $C^1$ boundary and integer multiplicity defines a finite-mass integral current by integration, and Stokes's theorem becomes $\partial[S]=[\partial S]$. More generally, a suitably locally finite oriented submanifold defines a locally integral current, but need not have finite global mass. Weak convergence $T_j\rightharpoonup T$ means $T_j(\omega)\to T(\omega)$ for every test form. The Federer–Fleming compactness and closure theorem states, in a standard Euclidean form, that integral currents $T_j$ supported in a common compact set and satisfying
\[
\sup_j\bigl(\mathbf M(T_j)+\mathbf M(\partial T_j)\bigr)<\infty
\]
have a weakly convergent subsequence whose limit is integral. Moreover, mass is weakly lower semicontinuous [1,3,4].

### Mathematical Context and Formation

The motivating problem class was the oriented Plateau problem. Given a compactly supported integral $(k-1)$-cycle $B$ in Euclidean space that is known to bound at least one compactly supported integral $k$-current, one seeks a $k$-dimensional oriented spanning surface of least area; in modern notation the variational problem is
\[
\inf\{\mathbf M(T): T\text{ is an integral }k\text{-current and }\partial T=B\}.
\]
The bounding assumption makes the competitor class nonempty; for example, when $k=1$, a compactly supported integral $0$-cycle can bound only if the sum of its integer coefficients is zero. The issue was not merely how to write an area functional, but how to choose an admissible notion of surface for which the infimum is attained. A minimizing sequence of smooth or parametrized surfaces can develop singularities, sheets with multiplicity, cancellations, or changes of topology. Consequently, it need not converge within the same smooth or fixed-parametrization class. At the other extreme, de Rham's general currents supplied a linear weak topology and the distributional boundary operator, but arbitrary currents were too broad to ensure that a weak limit still represented an oriented surface with integer sheet structure or that its mass had the required geometric interpretation [1,5].

Federer and Fleming's formation of integral currents joined two requirements that the minimization problem imposed simultaneously. Rectifiability forces the object to be concentrated on countably many Lipschitz images and hence to retain an almost-everywhere tangent plane and geometric $k$-area. Integer multiplicity records oriented sheets and their cancellation algebraically. Requiring the boundary to be integer rectifiable makes the class compatible with Stokes's theorem and iteration of the boundary operation. Their deformation and closure arguments then established that this geometrically restricted class nevertheless remains closed under the weak limits selected by uniform mass and boundary-mass bounds [1]. Thus the object was not simply a generalized smooth surface: it was a generalized surface designed so that geometric area, algebraic boundary, and variational compactness coexist.

### Essential Role

Integral currents make the existence step in the oriented Plateau problem tractable. Choose a minimizing sequence $T_j$ with $\partial T_j=B$. Its masses are uniformly bounded, while
\[
\mathbf M(\partial T_j)=\mathbf M(B)
\]
is fixed. In Euclidean space the competitors may, without increasing mass, be confined to a suitable compact set—for example, by the $1$-Lipschitz nearest-point retraction onto the compact convex hull of $\operatorname{spt}B$, which fixes $B$. Federer–Fleming compactness then gives a subsequence $T_{j_\ell}\rightharpoonup T$. Since boundary is defined by duality with exterior differentiation,
\[
\partial T_{j_\ell}\rightharpoonup \partial T,
\]
so $\partial T=B$; the closure theorem ensures that $T$ is still integral rather than a diffuse arbitrary current. Finally,
\[
\mathbf M(T)\le \liminf_{\ell\to\infty}\mathbf M(T_{j_\ell}),
\]
so $T$ attains the infimum [1–4].

Each defining feature addresses a particular failure of the classical admissible class. Weak current convergence provides subsequences despite geometric degeneration; the boundary operator preserves the spanning condition in the limit; rectifiability and integer multiplicity preserve an oriented surface interpretation; and mass lower semicontinuity prevents area from increasing upon passage to the limit. The object therefore reformulates the existence question from “find a smooth least-area surface directly” into “first obtain a generalized mass minimizer in a compact, boundary-stable class, then study its regularity.” This separation of existence from regularity is the deeper structural viewpoint introduced into the problem. Integral currents do not by themselves prove that every minimizer is smooth; singular-set and boundary-regularity questions require additional arguments [2–4].

## 3. Notes

- A general current is only a continuous functional on test forms. A normal current has finite mass and finite boundary mass. An integral current adds integer rectifiability of both the current and its boundary; these terms are not interchangeable.
- Integral currents encode orientation and allow cancellation of oppositely oriented sheets. They therefore solve an oriented Plateau problem. Unoriented, nonorientable, or soap-film problems with junctions may require currents modulo $2$, flat chains with other coefficients, varifolds, or different spanning-surface frameworks.
- “Locally integral current” is the corresponding local notion, requiring finite mass and integral structure on compact subsets rather than globally finite mass.

## 4. Sources

[1] Herbert Federer and Wendell H. Fleming, “Normal and Integral Currents,” *Annals of Mathematics*, Second Series 72 (1960), 458–520. https://doi.org/10.2307/1970227

[2] Wendell H. Fleming, “On the Oriented Plateau Problem,” *Rendiconti del Circolo Matematico di Palermo*, Series II 11 (1962), 69–90. https://doi.org/10.1007/BF02849427

[3] Herbert Federer, *Geometric Measure Theory*, Grundlehren der mathematischen Wissenschaften 153, Springer, 1969.

[4] Leon Simon, *Lectures on Geometric Measure Theory*, Proceedings of the Centre for Mathematical Analysis, Australian National University 3, 1983.

[5] Georges de Rham, *Variétés différentiables: formes, courants, formes harmoniques*, Hermann, 1955.
