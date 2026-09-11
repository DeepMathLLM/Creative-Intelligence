# Mathematical Object Origin Archive | Bergman Kernel

## 1. Archive Information

- Standard Name: Bergman kernel
- Mathematical Field: Complex Analysis
- Abstract: The Bergman kernel is the canonical reproducing kernel of the Hilbert space of square-integrable holomorphic functions on a domain. It was formed in response to the problem class of constructing and comparing conformal and biholomorphic maps: it packages a domain's holomorphic functions into a basis-independent two-point function whose transformation law directly reflects the Jacobian of a change of complex coordinates.

## 2. Core Record

### Precise Description

Let \(\Omega\subset\mathbb C^n\) be a domain, let \(dV\) denote Euclidean volume measure, and define the Bergman space
\[
A^2(\Omega)=\left\{f\in\mathcal O(\Omega):\int_\Omega |f|^2\,dV<\infty\right\},
\qquad
\langle f,g\rangle=\int_\Omega f(w)\overline{g(w)}\,dV(w).
\]
The mean-value inequality makes point evaluation \(f\mapsto f(z)\) continuous on \(A^2(\Omega)\). Its Riesz representers therefore determine a unique function \(K_\Omega:\Omega\times\Omega\to\mathbb C\), holomorphic in its first variable and antiholomorphic in its second, satisfying
\[
f(z)=\int_\Omega K_\Omega(z,w)f(w)\,dV(w)
\quad (f\in A^2(\Omega)).
\]
This \(K_\Omega\) is the Bergman kernel. If \((\phi_j)\) is any complete orthonormal basis of \(A^2(\Omega)\), then
\[
K_\Omega(z,w)=\sum_j \phi_j(z)\overline{\phi_j(w)},
\]
with locally uniform convergence; the sum is independent of the chosen basis. Equivalently, integration against \(K_\Omega\) is the orthogonal projection \(L^2(\Omega)\to A^2(\Omega)\). On the diagonal it has the extremal description
\[
K_\Omega(z,z)=\sup\bigl\{|f(z)|^2:f\in A^2(\Omega),\ \|f\|_2\le 1\bigr\}.
\]
For a biholomorphism \(F:\Omega\to\Omega'\), it obeys
\[
K_\Omega(z,w)=\det F'(z)\,K_{\Omega'}(F(z),F(w))\,
\overline{\det F'(w)}. \tag{1}
\]
These properties and conventions are standard; changing the convention for which inner-product argument is complex-linear only changes where conjugation is written [1][3].

### Mathematical Context and Formation

The motivating problem class was to construct maps of complex domains onto canonical domains and to recognize when two domains are biholomorphically equivalent. In one complex variable, a normalized conformal map can often be approached through the Green function, harmonic conjugation, or boundary integral formulas. Those methods do not supply a comparable general procedure for domains in several complex variables: biholomorphic equivalence is a nonlinear system for several holomorphic coordinate functions, a general domain has no universal canonical target, and one-variable harmonic-conjugate constructions do not extend as a mechanism for producing all coordinates. A list of holomorphic functions or an orthogonal basis was also not by itself a canonical domain invariant, because it depended on choices [1][2].

The formation of the kernel rests on replacing the direct search for coordinate functions by Hilbert-space data that transform naturally. If \(F:\Omega\to\Omega'\) is biholomorphic, then
\[
(U_Fg)(z)=\det F'(z)\,g(F(z))
\]
defines a unitary map \(A^2(\Omega')\to A^2(\Omega)\); the factor \(\det F'\) is exactly what compensates for the real volume change \(dV(F(z))=|\det F'(z)|^2dV(z)\). Meanwhile, holomorphy makes each point evaluation bounded. Representing all evaluations by Riesz vectors and summing against an orthonormal basis removes the basis choice, producing \(K_\Omega\). Unitarity then forces the covariance law (1). Thus the same construction joins two requirements imposed by the mapping problem: computability through orthogonal expansion and precise behavior under unknown biholomorphic changes of coordinates.

This is the mathematical content behind Bergman's introduction of the kernel in the study of pseudoconformal mapping by analytic functions of several complex variables, followed by its use in classical conformal mapping [2]. The object was not merely an arbitrary kernel later applied to mapping: its determinant-weighted covariance is a direct consequence of choosing the \(L^2\)-holomorphic space to match the Jacobian appearing in the mapping problem.

### Essential Role

The Bergman kernel made the coordinate-change portion of the mapping problem tractable by converting an unknown map into a functional identity between canonically computable domain functions. Instead of selecting individual holomorphic functions and then tracking how that selection changes, one may compute \(K_\Omega\) from any orthonormal basis; basis independence eliminates that auxiliary choice, while (1) records exactly the derivative determinant of every candidate biholomorphism.

For a concrete instance, let \(\Omega\subsetneq\mathbb C\) be simply connected, choose \(a\in\Omega\), and let \(F:\Omega\to\mathbb D\) be normalized by \(F(a)=0\) and \(F'(a)>0\). Since
\[
K_{\mathbb D}(u,v)=\frac{1}{\pi(1-u\overline v)^2},
\]
formula (1) at \(w=a\) gives
\[
K_\Omega(z,a)=\frac{F'(z)F'(a)}{\pi},
\qquad
F'(a)^2=\pi K_\Omega(a,a).
\]
Consequently the normalized mapping derivative, and hence the map itself, are recovered by
\[
F'(z)=\sqrt{\frac{\pi}{K_\Omega(a,a)}}\,K_\Omega(z,a),
\qquad
F(z)=\sqrt{\frac{\pi}{K_\Omega(a,a)}}\int_a^z K_\Omega(\zeta,a)\,d\zeta. \tag{2}
\]
Thus the nonlinear conformal-map problem is reformulated as construction of a reproducing kernel—accessible by orthogonalizing holomorphic functions—followed by one integration [1].

In several variables there is no analogue of (2) that maps every domain to one fixed model. Nevertheless, (1) supplies the same essential mechanism: its logarithmic derivatives yield coordinate-covariant differential data and Bergman representative coordinates, providing equations and invariants with which candidate pseudoconformal maps can be normalized and compared [1][2]. The deeper structural change is that the domain is studied through the geometry of its entire \(L^2\)-holomorphic function space and its evaluation vectors, rather than through one guessed mapping function. This directly overcomes basis dependence and exposes the Jacobian behavior that the original mapping problem requires; it does not, by itself, decide biholomorphic equivalence for arbitrary domains.

## 3. Notes

The Bergman kernel should be distinguished from the Bergman space \(A^2(\Omega)\), of which it is the reproducing kernel; from the Bergman projection, for which it is the integral kernel; and from the Bergman metric, obtained on suitable domains from \(\partial\bar\partial\log K_\Omega(z,z)\). On unbounded domains \(A^2(\Omega)\) may be trivial, in which case the kernel is identically zero. The nontriviality and positivity needed for mapping constructions such as (2) hold for bounded domains and, in the displayed one-variable case, follow directly from the existence of the normalized Riemann map.

## 4. Sources

[1] Stefan Bergman, *The Kernel Function and Conformal Mapping*, revised edition, Mathematical Surveys 5, American Mathematical Society, 1970.

[2] Stefan Bergman and Menahem Schiffer, “Kernel Functions and Conformal Mapping,” *Compositio Mathematica* 8 (1951), 205–249, https://www.numdam.org/item/CM_1951__8__205_0/.

[3] Steven G. Krantz, *Function Theory of Several Complex Variables*, 2nd ed., AMS Chelsea Publishing, 2001.
